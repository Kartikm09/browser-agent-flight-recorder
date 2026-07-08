from __future__ import annotations

import re
from typing import Any

EMAIL = re.compile(r"\b[\w.-]+@[\w.-]+\.[A-Za-z]{2,}\b")
TOKEN = re.compile(r"\b(?:ghp|gho|sk|tok)_[A-Za-z0-9_\-]{12,}\b", re.IGNORECASE)
BLOCKED = {"submit_payment", "publish_post", "send_message", "delete_record", "upload_file", "connect_account"}
APPROVAL = {"submit_form", "calendar_edit", "profile_edit", "comment"}


def redact_value(value: str) -> str:
    value = TOKEN.sub("[REDACTED_TOKEN]", value)
    value = EMAIL.sub("[REDACTED_EMAIL]", value)
    return value


def classify_event(event: dict[str, Any]) -> dict[str, Any]:
    action = str(event.get("action", "")).lower()
    target = redact_value(str(event.get("target", "")))
    text = redact_value(str(event.get("text", "")))
    if action in BLOCKED:
        decision = "blocked"
        reason = "risky browser action requires separate explicit workflow"
    elif action in APPROVAL:
        decision = "approval_required"
        reason = "external or account-modifying action needs approval"
    else:
        decision = "allow"
        reason = "read-only or local navigation action"
    return {"step": event.get("step"), "action": action, "target": target, "text": text, "decision": decision, "reason": reason}


def classify_trace(trace: dict[str, Any]) -> dict[str, Any]:
    events = [classify_event(event) for event in trace.get("events", [])]
    return {
        "task_id": trace.get("task_id", "unknown"),
        "events": events,
        "blocked_count": sum(1 for event in events if event["decision"] == "blocked"),
        "approval_count": sum(1 for event in events if event["decision"] == "approval_required"),
        "safe_to_replay": all(event["decision"] == "allow" for event in events),
    }
