# FIRE-NET Alpha — Portable Robotic Multi-Mechanism Fire-Safety Research Platform

**Revision:** 0.1 — architecture / pre-Rev-A  
**Status:** Conceptual research and engineering platform; not certified fire-protection equipment.

## 1. Purpose

FIRE-NET (Fire Infrastructure Resilience & Extinguishment Network) is a portable, modular and robotics-centered research platform intended to make emerging fire-safety concepts measurable before they are treated as products.

The Alpha objective is deliberately narrower than the long-term vision: build a rugged sensing, edge-computing, communications, telemetry and robotic-integration core that can host interchangeable **research** payloads while retaining human supervision and independent conventional fire-safety provisions during qualified testing.

FIRE-NET does **not** assume that acoustic, electric/electromagnetic, inert-gas, pressure/flow-management, smart-material, thermal-recovery or other experimental mechanisms will prove operationally useful. The platform exists to generate evidence that can advance, modify or reject them.

## 2. Design principles

1. **Portable first.** Field nodes and robots should be deployable without dependence on a hydrant or fixed municipal installation.
2. **Human supervised.** Critical decisions and hazardous experiments remain under qualified human control.
3. **Modular.** Compute, sensing, communications and payload interfaces are separated so modules can evolve independently.
4. **Measure before claiming.** Each research mechanism receives explicit metrics, controls and failure criteria.
5. **Graceful degradation.** System states are Normal → Degraded → Essential → Safe State → Recovery.
6. **Fail safely.** Loss of high-level compute, communications or a nonessential sensor must not create uncontrolled actuation.
7. **Defense in depth.** Electromagnetic resilience is addressed through architecture, bonding, shielding, filtering, protected interfaces, power integrity, isolation where justified, watchdogs and recovery—not a single 'EMP-proof' component.
8. **Interoperability.** Alpha should use documented electrical/data/mechanical interfaces rather than lock the project to one payload or robot.
9. **Conventional safety remains independent.** Experimental mechanisms are not substitutes for required suppression or life-safety systems until independently validated and appropriately certified.

## 3. Alpha architecture

```text
[THERMAL / VISIBLE / ENVIRONMENT / MOTION / DEPTH]
                       |
                       v
              [FIRE-NET EDGE CORE]
             /          |          \
     [Safety MCU]  [Edge Compute]  [Data Logger]
          |              |              |
          +--------[Health Manager]-----+
                         |
          +--------------+--------------+
          |              |              |
      Ethernet         CAN-FD          RS-485
          |              |              |
    Command Node     Robot Base     Research I/O
          |
   Multi-path telemetry
          |
  Human operator / test team
```

The safety/supervisory controller and physical emergency-stop path should remain independent from higher-level analytics wherever practicable.

## 4. Portable system family

### 4.1 Field Node
Rugged portable enclosure containing Edge Core electronics, thermal/environmental sensing, local logging, networking and system-health telemetry.

### 4.2 R-1 Research Robot
A tracked research carrier for remote sensing and interchangeable low-risk Alpha payloads. Early builds should favor a commercially supported mobile base rather than custom locomotion.

### 4.3 Reconnaissance platform
A smaller ground or aerial platform can eventually provide thermal mapping, scene imagery and environmental measurements before a larger system approaches.

### 4.4 Mobile research lab
A transportable integration/test environment for data acquisition, charging, maintenance, payload configuration and controlled experiment support.

## 5. Edge Core Rev-A

Rev-A should prioritize instrumentation and resilience rather than hazardous actuation.

Minimum functional blocks:
- industrial supervisory MCU;
- Linux-capable edge-compute module;
- independent watchdog/brownout supervision;
- local nonvolatile logging;
- Ethernet, CAN-FD and RS-485;
- protected sensor I/O;
- power/current/temperature telemetry;
- hardware emergency-stop/status interface;
- modular research I/O;
- secure device identity capability;
- clearly defined debug/programming interface.

Rev-A should use a payload emulator/dummy loads for integration tests. Hazardous suppression actuation is intentionally outside the public Rev-A implementation.

## 6. Electromagnetic and electrical resilience

FIRE-NET should use **testable immunity targets**, not an unqualified 'EMP-proof' claim.

The current IEC 61000-4-2:2025 standard provides a reproducible laboratory basis for ESD immunity testing. Additional IEC 61000-4 family methods can inform radiated/conducted RF, burst and surge testing when the intended environment and applicable product requirements are established.

NASA KSC-STD-E-0022 is a useful public engineering reference because its scope integrates bonding, grounding, shielding, EMI, lightning, ESD, transient protection and surge suppression for electrical/electronic ground systems. It is a reference—not a statement that FIRE-NET is NASA-qualified or compliant.

Design study areas:
- conductive enclosure and controlled penetrations;
- short, low-impedance chassis bonding;
- cable-shield termination appropriate to the interface;
- TVS/transient protection at exposed interfaces;
- common-mode filtering where analysis supports it;
- galvanic isolation for selected interfaces where grounding analysis supports it;
- protected power entry;
- brownout/overvoltage/overcurrent monitoring;
- separate essential-control and high-level-compute domains;
- independent watchdog/recovery;
- local store-and-forward logging;
- communications diversity;
- deterministic safe state after defined failures.

### Proposed resilience validation ladder

**R0 — bench:** reverse-polarity prevention, brownout, power cycling, watchdog recovery, interface fault injection.  
**R1 — pre-compliance:** ESD and conducted/radiated susceptibility screening with qualified equipment/partners.  
**R2 — environmental:** temperature, vibration/transport, enclosure and ingress targets as requirements mature.  
**R3 — formal:** testing against the standards and severity levels actually applicable to the selected market and deployment environment.

No level should be described as certified until an authorized laboratory/test program supports that statement.

## 7. Research payload families

These are research hypotheses, not validated products.

### A. Precision low-water / mist
Measure control time, water/agent use, heat flux, temperature decay, visibility, runoff and reignition against an appropriate baseline.

### B. Localized inert-gas / atmosphere management
Research only in facilities with appropriate ventilation, gas monitoring and qualified supervision. Measure concentration, distribution, control effectiveness, consumption and re-entry/recovery conditions.

### C. Acoustic flame interaction
Laboratory research into whether controlled acoustic fields produce repeatable effects in defined flame regimes. Alpha public hardware should provide measurement/synchronization interfaces, not high-power acoustic actuation instructions.

### D. Electric/electromagnetic flame interaction
Fundamental laboratory research only. Public Alpha documentation intentionally excludes high-voltage/high-energy construction details.

### E. Localized smoke / heat / flow management
Investigate whether extraction or directed flow can improve visibility, heat management or suppression effectiveness under controlled configurations. Avoid treating 'vacuum suppression' as a proven universal mechanism.

### F. Smart materials
Instrumented fixtures for characterized thermal barriers, intumescent structures, phase-change materials or other candidate materials. Material chemistry and deployment systems require separate safety review.

### G. Thermal recovery
Measure heat-flow opportunities and determine whether recovery can reduce unwanted heat transfer or support auxiliary loads without impairing fire control. No net-energy claim is assumed.

### H. Hybrid orchestration
Only mechanisms that individually demonstrate useful behavior should advance to coordinated experiments.

## 8. Data and validation model

Each experiment should record, where applicable:
- synchronized time;
- thermal imagery and reference temperatures;
- ambient temperature/humidity/pressure;
- selected gas/particulate measurements;
- robot pose/standoff distance;
- communications quality and latency;
- power/current/energy consumption;
- payload state;
- operator commands;
- fault/safe-state events;
- control time;
- agent/water consumption;
- temperature decay and heat flux;
- reignition observation window;
- post-test hardware health.

Raw data should be preserved. Derived metrics should identify software version, calibration information and analysis method.

## 9. Safety architecture

- Physical emergency stop independent of high-level software.
- Hazardous payloads disabled by default.
- Loss of command link produces a defined safe behavior.
- High-level AI/ML output is advisory unless separately verified for a specific control function.
- Experimental fire testing occurs only at appropriately equipped facilities with qualified personnel.
- Inert gases require atmosphere monitoring and occupancy controls.
- High-energy acoustic/electrical/EM experiments require dedicated laboratory risk assessment.
- Battery systems require appropriate BMS, fusing/protection, containment and charging procedures.
- No FIRE-NET research module should impair required building/fire-protection systems.

## 10. Rev-A acceptance targets

Rev-A succeeds if it can:
1. boot reliably and report system health;
2. acquire synchronized data from multiple sensors;
3. log locally during network loss;
4. exchange telemetry through at least one primary interface;
5. command a benign payload emulator through the modular interface;
6. demonstrate hardware emergency stop / actuation inhibit;
7. recover predictably from defined brownout/watchdog tests;
8. integrate with a mobile research base;
9. export a reproducible test dataset;
10. document failures and convert them into Rev-B requirements.

## 11. Development roadmap

**Phase 0 — Requirements:** hazards, interfaces, power budget, environmental assumptions, validation plan.  
**Phase 1 — Rev-A electronics:** schematic/PCB, Field Node, sensor integration, payload emulator.  
**Phase 2 — Bench validation:** power, communications, sensing, logging, fault injection, EMC pre-compliance planning.  
**Phase 3 — Robotics integration:** tracked carrier, remote operation, emergency stop, payload interface.  
**Phase 4 — Controlled fire-science experiments:** qualified partners and separately reviewed research payloads.  
**Phase 5 — Rev-B:** evidence-driven redesign, then determine whether any subsystem merits certification/product development.

## 12. Public vs. protected information

Appropriate for the public repository:
- project objectives;
- high-level architecture;
- public BOM classes;
- benign telemetry/source-code examples;
- test philosophy;
- conceptual renders;
- non-confidential results and lessons learned.

Keep private until deliberately released:
- patentable mechanisms;
- proprietary CAD/PCB implementation before IP review;
- credentials/keys;
- safety-critical actuation logic;
- detailed high-energy/high-voltage suppression hardware;
- partner-confidential material;
- information that would enable unsafe operation of experimental equipment.

## 13. Reference basis

- IEC 61000-4-2:2025 — Electrostatic discharge immunity test.
- NASA KSC-STD-E-0022 — public reference covering bonding, grounding, shielding, EMI, lightning, ESD, transient protection and surge suppression for KSC ground systems.
- NASA-STD-4003A with Change 1 — public electrical bonding reference, revalidated in 2026.

These references inform engineering discipline. Applicability and test severity must be determined for the actual product category, environment and certification path.

---

**FIRE-NET principle:** *Prove what works. Preserve what works. Improve what can be improved.*
