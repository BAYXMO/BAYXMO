# BAYXMO — System Architecture

## 1. Purpose

This document defines the high-level software, AI, perception, control, communication, and hardware architecture of BAYXMO.

The architecture is designed to support modular development, testing, safety, scalability, and eventual physical integration.

---

## 2. Architectural Principles

BAYXMO architecture follows these principles:

- Modularity
- Separation of responsibilities
- Safety by design
- Hardware/software separation
- Testability
- Observability
- Replaceable components
- Incremental development

---

## 3. High-Level Architecture

```text
                         HUMAN
                           │
                           ▼
                  ┌─────────────────┐
                  │      HRI        │
                  │ Interaction    │
                  └────────┬────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │    COGNITIVE LAYER     │
              │                        │
              │ AI • Dialogue •        │
              │ Reasoning • Learning   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │    PERCEPTION LAYER    │
              │                        │
              │ Vision • Speech •      │
              │ Sensors • State        │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │     CONTROL LAYER      │
              │                        │
              │ Planning • Motion •    │
              │ Safety • Coordination  │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │   HARDWARE INTERFACE   │
              │                        │
              │ MCU • Motors • Sensors │
              │ Power • Actuators      │
              └────────────────────────┘

```
---

4. HRI Layer

The Human-Robot Interaction layer is responsible for coordinating interaction between BAYXMO and humans.

Responsibilities include:

Interaction state
Turn-taking
Attention management
Interaction modes
Conversational state
Expressive behaviors
User feedback

The HRI layer should not directly control hardware.

It should communicate desired behaviors to the appropriate control systems.

5. Cognitive / AI Layer

The cognitive layer provides the primary intelligence of BAYXMO.

Potential components include:

Language models
Dialogue management
Reasoning
Context management
User modeling
Educational reasoning
Adaptive learning
Safety-aware decision making

The cognitive layer produces intentions and decisions rather than directly commanding motors.

6. Perception Layer

The perception layer converts raw sensor information into meaningful system information.

Potential inputs include:

Microphones
Cameras
Distance sensors
Touch sensors
IMU
Encoders
Environmental sensors

Potential outputs include:

Speech input
Detected objects
Human presence
Visual landmarks
Robot orientation
Touch events
Sensor states
7. Control Layer

The control layer translates high-level intentions into safe physical actions.

Responsibilities include:

Motion planning
Motor control coordination
Actuator commands
State management
Motion constraints
Safety checks
Emergency handling

The control layer acts as a boundary between AI-level decisions and physical hardware.

8. Hardware Layer

The hardware layer consists of the physical components of BAYXMO.

Potential components include:

Microcontrollers
Edge computing hardware
Motors
Servos
Cameras
Microphones
Speakers
Sensors
Power systems
Mechanical structures

Hardware decisions will evolve as prototypes are developed and tested.

9. Compute Architecture

BAYXMO is expected to use a heterogeneous computing architecture.

High-Level Compute

Potential responsibilities:

AI inference
Computer vision
Speech processing
Dialogue
Learning systems
HRI coordination
Embedded Compute

Potential responsibilities:

Sensor acquisition
Motor control
Real-time control
Safety monitoring
Low-level communication

This separation allows high-level intelligence to evolve independently from low-level physical control.

10. Communication

Subsystem communication should use clearly defined interfaces.

Potential communication mechanisms include:

Serial communication
USB
Network communication
Message-based interfaces
Structured data formats

The final communication architecture will be selected according to latency, reliability, complexity, and hardware requirements.

11. Safety Architecture

Safety should exist across multiple layers.

```text
AI Safety
    ↓
Behavioral Safety
    ↓
HRI Safety
    ↓
Control Safety
    ↓
Hardware Safety
    ↓
Physical Safety
```

---

No single software component should be considered the only safety mechanism.

Critical physical safety mechanisms should remain capable of operating independently of high-level AI behavior where appropriate.

12. Data Flow

A typical interaction may follow:
```text
Human
  ↓
Microphone / Camera / Sensors
  ↓
Perception
  ↓
Context & State
  ↓
AI / Dialogue / Learning
  ↓
HRI Decision
  ↓
Control
  ↓
Actuators / Speech / Display
  ↓
Human
```

---

The resulting interaction generates new observations that can be processed by the perception layer.

13. State Management

BAYXMO should maintain explicit system states where appropriate.

Examples include:

Idle
Listening
Processing
Speaking
Learning
Moving
Paused
Safety Stop
Error
Shutdown

State transitions should be deterministic and observable.

14. Observability

The system should provide appropriate logging and diagnostics.

Important information may include:

System state
Sensor states
Errors
Warnings
AI events
Interaction events
Control events
Safety events

Logging should be designed with privacy considerations.

15. Modularity

Each major subsystem should have defined interfaces.

Example:
```text
AI
 │
 ├── Dialogue Interface
 ├── Learning Interface
 └── HRI Interface

Perception
 │
 ├── Vision Interface
 ├── Speech Interface
 └── Sensor Interface

Control
 │
 ├── Motion Interface
 ├── Safety Interface
 └── Hardware Interface
```

---

This allows components to be replaced without redesigning the entire system.

16. Development Strategy

Architecture will evolve through prototypes.

The current architecture is intentionally high-level.

Future versions should be based on:

Hardware constraints
Performance measurements
Prototype results
Safety analysis
Software complexity
Interaction testing

Architecture decisions should be documented using Architecture Decision Records.

17. Current Status

Architecture maturity: Initial conceptual architecture

Implementation maturity: Early development

Hardware architecture: Under investigation

Software architecture: Under development

<> BAYXMO

Learn. Grow. Belong.
