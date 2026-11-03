#!/usr/bin/env python3
"""FIRE-NET Alpha benign telemetry/health reference implementation.

Research scaffold only. No physical suppression or hazardous actuation is implemented.
"""

from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import Enum


class SystemState(str, Enum):
    NORMAL = "NORMAL"
    DEGRADED = "DEGRADED"
    ESSENTIAL = "ESSENTIAL"
    SAFE_STATE = "SAFE_STATE"
    RECOVERY = "RECOVERY"


@dataclass
class Health:
    primary_power_ok: bool = True
    edge_compute_ok: bool = True
    primary_link_ok: bool = True
    thermal_sensor_ok: bool = True
    estop_clear: bool = True


@dataclass
class Telemetry:
    timestamp: str
    state: str
    temperature_c: float
    humidity_pct: float
    battery_v: float
    link_quality_pct: int
    payload_enabled: bool
    health: dict


def evaluate_state(h: Health) -> SystemState:
    """Illustrative state mapping; not production safety logic."""
    if not h.estop_clear:
        return SystemState.SAFE_STATE
    if not h.primary_power_ok:
        return SystemState.ESSENTIAL
    failures = sum(
        not value
        for value in (h.edge_compute_ok, h.primary_link_ok, h.thermal_sensor_ok)
    )
    if failures >= 2:
        return SystemState.ESSENTIAL
    if failures == 1:
        return SystemState.DEGRADED
    return SystemState.NORMAL


def simulated_health(cycle: int) -> Health:
    """Inject benign demonstration faults so state transitions can be observed."""
    h = Health()
    phase = cycle % 12
    if phase == 4:
        h.primary_link_ok = False
    elif phase == 7:
        h.edge_compute_ok = False
        h.primary_link_ok = False
    elif phase == 9:
        h.estop_clear = False
    return h


def sample(cycle: int) -> Telemetry:
    h = simulated_health(cycle)
    state = evaluate_state(h)
    # Public demo uses synthetic values only.
    return Telemetry(
        timestamp=datetime.now(timezone.utc).isoformat(),
        state=state.value,
        temperature_c=round(22.0 + random.uniform(-0.8, 0.8), 2),
        humidity_pct=round(45.0 + random.uniform(-2.0, 2.0), 2),
        battery_v=round(25.6 + random.uniform(-0.15, 0.15), 2),
        link_quality_pct=max(0, min(100, 96 + random.randint(-4, 3))) if h.primary_link_ok else 0,
        payload_enabled=False,  # Hazardous actuation intentionally absent.
        health=asdict(h),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="FIRE-NET Alpha telemetry simulator")
    parser.add_argument("--cycles", type=int, default=10, help="number of samples")
    parser.add_argument("--period", type=float, default=0.25, help="seconds between samples")
    args = parser.parse_args()

    if args.cycles < 1 or args.period < 0:
        parser.error("cycles must be >= 1 and period must be >= 0")

    for cycle in range(args.cycles):
        print(json.dumps(asdict(sample(cycle)), separators=(",", ":")))
        if cycle + 1 < args.cycles:
            time.sleep(args.period)


if __name__ == "__main__":
    main()
