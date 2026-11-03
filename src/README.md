# FIRE-NET Alpha Source Code

This directory is the **public, non-hazardous software scaffold** for FIRE-NET Alpha.

The initial code intentionally covers telemetry, system-health state, graceful degradation and simulated sensor/payload data. It does **not** contain suppression-agent delivery instructions, high-voltage/electromagnetic actuation, high-power acoustic actuation, pressure-system control, autonomous hazardous actuation, credentials or safety-critical production logic.

## Quick start

Requires Python 3.11+ and only the standard library.

```bash
python src/fire_net_alpha.py --cycles 5
```

Example JSON Lines output can be redirected to a file:

```bash
python src/fire_net_alpha.py --cycles 20 > fire_net_alpha_telemetry.jsonl
```

## Architecture

- `fire_net_alpha.py` — benign reference implementation for telemetry and health-state transitions.
- Future public modules can cover sensor adapters, schemas, logging, replay, simulation and hardware-abstraction interfaces.
- Physical emergency stop and safety interlocks must not depend solely on this software.

## State model

`NORMAL -> DEGRADED -> ESSENTIAL -> SAFE_STATE -> RECOVERY`

The demonstration maps simulated health conditions to these states. This is a software research model, not certified safety logic.

## Development rule

Before real hardware actuation is added, define requirements, hazards, independent safety controls, interface electrical limits, test fixtures and qualified validation procedures. Experimental fire-suppression payloads should be developed and tested separately with appropriate fire-science/safety partners.
