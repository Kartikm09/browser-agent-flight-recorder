from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from browser_agent_flight_recorder import classify_trace

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/sample_browser_trace.json")
print(json.dumps(classify_trace(json.loads(path.read_text(encoding="utf-8"))), indent=2, sort_keys=True))
