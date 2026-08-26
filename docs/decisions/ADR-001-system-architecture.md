# ADR-001 — System Architecture

- **Status:** Accepted
- **Date:** 2026-08-26
- **Decision Type:** Architecture
- **Scope:** System-wide

---

## 1. Context

BAYXMO is intended to become an integrated physical educational companion robot combining artificial intelligence, adaptive learning, computer vision, speech, robotics, embedded systems, and human-robot interaction.

These systems have different computational, timing, reliability, and safety requirements.

A clear architectural strategy is therefore required before significant implementation begins.

---

## 2. Problem

BAYXMO must support both:

- High-level computationally intensive systems
- Low-level real-time physical control

The architecture must also allow individual components to evolve without requiring the entire system to be redesigned.

The system must provide clear boundaries between:

- Artificial intelligence
- Perception
- Human-robot interaction
- Control
- Embedded systems
- Physical hardware
- Safety mechanisms

---

## 3. Options Considered

### Option A — Monolithic Architecture

A single application would control most BAYXMO functionality.

#### Advantages

- Simple initial implementation
- Easy to start
- Fewer interfaces
- Low initial architectural overhead

#### Disadvantages

- Poor separation of responsibilities
- Difficult subsystem testing
- Hardware and AI become tightly coupled
- Increased risk of a single failure affecting the whole system
- Difficult long-term scalability
- More difficult replacement of individual components

---

### Option B — Fully Distributed Architecture

Every major function would operate as an independent distributed service.

#### Advantages

- High modularity
- Strong subsystem isolation
- Independent deployment
- High scalability

#### Disadvantages

- High architectural complexity
- Increased communication overhead
- More difficult debugging
- Excessive complexity for early prototypes
- Higher infrastructure requirements

---

### Option C — Layered Modular Architecture

BAYXMO would use modular layers with clearly defined interfaces while avoiding unnecessary distributed-system complexity during early development.

Conceptually:

```text
Human
  ↓
HRI
  ↓
Cognitive / AI
  ↓
Perception
  ↓
Control
  ↓
Hardware
```

---

Safety mechanisms operate across multiple layers and include independent physical protections where appropriate.

Advantages
Clear separation of responsibilities
Easier testing
Easier hardware/software integration
Supports incremental development
Allows components to evolve independently
Appropriate for prototype development
Can evolve toward more distributed systems when justified
Disadvantages
Requires interface design
Additional architectural planning
Some communication overhead
More complex than a simple monolithic prototype
4. Decision

BAYXMO will use a Layered Modular Architecture.

The architecture will separate major system responsibilities while keeping the early implementation practical.

The initial high-level layers are:

┌─────────────────────────────┐
│       Human / User          │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│            HRI              │
│ Interaction & Behaviors     │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│      Cognitive / AI         │
│ Dialogue • Reasoning • EDU  │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│         Perception          │
│ Vision • Speech • Sensors   │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│          Control            │
│ Motion • Safety • State     │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│          Hardware           │
│ MCU • Motors • Sensors      │
└─────────────────────────────┘
5. Compute Separation

BAYXMO will initially use a heterogeneous computing model.

High-Level Compute

Responsible for computationally intensive or flexible workloads such as:

AI inference
Dialogue
Computer vision
Speech processing
Adaptive learning
HRI coordination
Embedded Compute

Responsible for time-sensitive and hardware-facing operations such as:

Sensor acquisition
Motor control
Actuator control
Low-level safety monitoring
Hardware communication

This separation allows the AI system to evolve independently from low-level physical control.

6. Safety Decision

Safety-critical physical behavior shall not depend exclusively on the high-level AI system.

Where appropriate, safety mechanisms should exist at multiple levels:

AI / Behavioral Safety
        ↓
Control Safety
        ↓
Embedded Safety
        ↓
Hardware Safety
        ↓
Physical Safety

The final safety architecture will depend on the actual hardware and risk analysis.

7. Communication Strategy

Subsystem communication will use explicit interfaces.

Early prototypes may use mechanisms such as:

Serial communication
USB
Local process communication
Network communication where necessary

The final communication technology will be selected according to:

Latency
Reliability
Complexity
Hardware availability
Debuggability
Safety requirements

No communication technology is permanently selected by this ADR.

8. Consequences
Positive Consequences

The selected architecture provides:

Better modularity
Clear subsystem boundaries
Easier testing
Easier debugging
Hardware/software separation
Better long-term scalability
Safer control boundaries
Easier replacement of individual components
Negative Consequences

The architecture introduces:

Additional interfaces
More design work
More documentation
Communication complexity
Higher initial engineering effort

These costs are accepted because they support the long-term goals of BAYXMO.

9. Implementation Strategy

The architecture will be implemented incrementally.

Early prototypes may simplify some boundaries for development speed.

As the system becomes more complex, subsystem interfaces should become more explicit and stable.

Architecture should evolve based on:

Prototype results
Performance measurements
Hardware constraints
Safety analysis
Software complexity
Testing results
10. Validation

This architectural decision will be evaluated through future prototypes.

Evidence should include:

Successful subsystem integration
Communication reliability
Control responsiveness
Fault handling
Testability
Maintainability
Safety performance

If significant evidence demonstrates that the architecture is no longer appropriate, a new ADR should document the change.

11. Related Documents
vision.md
requirements.md
roadmap.md
12. Status

Accepted

This ADR represents the initial architectural direction of BAYXMO.

It may be superseded by a future ADR if major architectural evidence requires a different approach.

<> BAYXMO

Learn. Grow. Belong.
