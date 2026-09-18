        # browser-agent-flight-recorder

        Classifies browser-agent traces and blocks risky submit, publish, delete, pay, and account actions.

        ## Why This Exists

        The July 2026 GitHub AI tools roundup highlighted a useful pattern: the best
        open-source AI repos are not just demos. They become infrastructure when they
        are testable, local-first, agent-friendly, and honest about risk. This repo
        turns that lesson into an original, runnable portfolio artifact.

        ## Features

        - Synthetic browser trace fixtures for search, draft, checkout, and publish flows.
- Risk classifier for DOM/action events.
- Redaction of email-like and token-like fields in traces.
- Approval cards for actions that should not execute automatically.
- Unit tests for blocked and allowed browser actions.

        ## Quick Start

        ```bash
        python -m unittest discover -s tests
        python scripts/classify_trace.py data/sample_browser_trace.json
        ```

        ## Repository Structure

        ```text
        browser-agent-flight-recorder/
          README.md
          LINKEDIN_DESCRIPTION.md
          docs/
          data/
          examples/
          scripts/
          tests/
          browser_agent_flight_recorder/
        ```

        ## Safety Boundary

        This repo uses synthetic or public example data. It does not connect to private
        accounts, scrape logged-in pages, send messages, publish content, trade assets,
        or ask for credentials. Any real-world integration should be approval-gated.

        ## Skills Demonstrated

        - Browser-agent QA
- Trace review
- Approval gates
- Privacy redaction
- Tool-use safety

        ## Recruiter Summary

        A compact proof-of-work repo showing that I can convert AI tool research into
        practical automation, evaluation rubrics, safe agent design, and testable Python.

## Replay verification boundary

Only the explicit read/navigation/inspection allowlist is classified for safe replay. Unknown actions require review and an empty trace is unverified. This static classifier does not execute a browser or authorize a real action; a mislabeled input cannot establish what the UI actually did.
