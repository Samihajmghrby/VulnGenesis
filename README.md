# VulnGenesis

### AI-Assisted Security Hypothesis Generation for Contextual Vulnerability Discovery

VulnGenesis is an open-source security research project exploring how artificial intelligence and program analysis can support more contextual approaches to vulnerability discovery.

Rather than treating security findings as isolated alerts, VulnGenesis aims to understand relationships between application components, user-controlled input, sensitive operations, and security controls. The project explores whether this contextual understanding can help generate and prioritize meaningful security hypotheses for human security researchers.

> **Important:** VulnGenesis is designed exclusively for authorized security research, defensive testing, and controlled environments.

---

## The Problem

Modern application security tools can generate large volumes of alerts. Security researchers and developers often need to manually determine:

* Which findings are likely to represent meaningful security risks
* How different pieces of security evidence are related
* Which application paths deserve further investigation
* Whether a potential issue has sufficient contextual evidence to justify testing

Traditional approaches can identify known patterns, but they may not fully capture the relationships between application structure, data flow, security controls, and sensitive operations.

VulnGenesis explores a context-driven approach to this problem.

---

## Project Vision

The long-term vision of VulnGenesis is to build an intelligent security research platform capable of:

1. Understanding the structure of an authorized application
2. Identifying relationships between application components
3. Modeling relevant code and data flows
4. Detecting potentially risky paths
5. Generating security hypotheses for human review
6. Prioritizing hypotheses based on contextual evidence
7. Supporting safe validation in controlled and isolated environments
8. Providing explainable evidence for each potential finding

The goal is not to replace human security researchers, but to help them focus their time on the areas that may deserve deeper investigation.

---

## Conceptual Architecture

```text
                 Authorized Application
                          │
                          ▼
               Program Understanding Layer
                          │
                          ▼
                 Code & Data-Flow Analysis
                          │
                          ▼
                 Security Knowledge Graph
                          │
                          ▼
                Security Hypothesis Engine
                          │
                          ▼
               Contextual Risk Prioritization
                          │
                          ▼
                  Human Researcher Review
                          │
                          ▼
              Controlled Validation Environment
                          │
                          ▼
                 Evidence & Findings Report
```

---

## Core Research Areas

VulnGenesis combines research from several areas:

### Program Analysis

Exploring application structure, functions, API endpoints, dependencies, and relevant code relationships.

### Data-Flow Analysis

Studying how potentially untrusted data moves through an application toward sensitive operations.

### Security Knowledge Graphs

Representing relationships between application components, inputs, controls, dependencies, and security-relevant operations.

### AI-Assisted Security Reasoning

Exploring how AI can help generate hypotheses from contextual security evidence.

### Contextual Risk Prioritization

Ranking potential areas for investigation based on multiple factors rather than relying only on isolated severity scores.

### Explainable Security Findings

Providing evidence and context explaining why a particular path or hypothesis deserves investigation.

---

## Research Question

> **Can contextual program analysis and AI-assisted security hypothesis generation help security researchers identify and prioritize meaningful vulnerability investigation paths more effectively than isolated rule-based findings?**

This question will guide the research and evaluation of the project.

---

## Proposed Security Reasoning Loop

```text
OBSERVE
   ↓
UNDERSTAND
   ↓
MODEL CONTEXT
   ↓
GENERATE HYPOTHESIS
   ↓
PRIORITIZE
   ↓
HUMAN REVIEW
   ↓
SAFE VALIDATION
   ↓
COLLECT EVIDENCE
   ↓
IMPROVE THE MODEL
```

This iterative approach is intended to support human-led security research rather than autonomous exploitation.

---

## Planned Features

* Application structure analysis
* Code and data-flow modeling
* Security knowledge graph generation
* Contextual security hypothesis generation
* Explainable risk prioritization
* Evidence correlation
* Human-in-the-loop review workflows
* Controlled validation support
* Reproducible research experiments
* Modular architecture for future analysis modules

---

## Technology Direction

The project is currently in its early research and development stage.

Potential technologies include:

* **Python** — Core analysis and backend services
* **FastAPI** — API development
* **Tree-sitter** — Source code parsing
* **NetworkX / Neo4j** — Graph-based security modeling
* **PostgreSQL** — Structured data storage
* **Docker** — Reproducible and isolated environments
* **React / Next.js** — Future visualization interface

The final technology choices may evolve as the research develops.

---

## Development Roadmap

### Phase 1 — Foundation

* [x] Define project vision
* [x] Define initial research question
* [x] Create public repository
* [ ] Design system architecture
* [ ] Define core data model
* [ ] Establish reproducible development environment

### Phase 2 — Program Understanding

* [ ] Parse source code structure
* [ ] Identify functions and application components
* [ ] Build initial application graph

### Phase 3 — Security Context Modeling

* [ ] Implement basic data-flow representation
* [ ] Identify security-relevant operations
* [ ] Build the initial security knowledge graph

### Phase 4 — Hypothesis Generation

* [ ] Define contextual security rules
* [ ] Generate candidate security hypotheses
* [ ] Develop explainable prioritization

### Phase 5 — Evaluation

* [ ] Create controlled research environments
* [ ] Define evaluation methodology
* [ ] Compare approaches and measure results
* [ ] Document findings

### Phase 6 — Open Source Community

* [ ] Add contribution guidelines
* [ ] Add code of conduct
* [ ] Add security policy
* [ ] Publish architecture documentation
* [ ] Create issues and contribution roadmap

---

## Responsible Use

VulnGenesis is intended exclusively for:

* Authorized security testing
* Defensive security research
* Secure software development
* Educational purposes
* Controlled laboratory environments

Users are responsible for ensuring they have explicit authorization before analyzing any application or system.

The project does not support unauthorized access, exploitation, or harmful activity.

---

## Contributing

VulnGenesis is currently in its early development stage.

Contributions, research discussions, ideas, and feedback will be welcome as the project develops. Formal contribution guidelines will be added in a future release.

---

## Project Status

🚧 **Early Research & Development**

VulnGenesis is currently being developed as an open-source research project.

The architecture, methodology, and implementation will evolve as the project grows.

---

## License

A license will be selected and added during the initial development phase.

---

## Author

Developed and maintained by **Samiha Moghraby**.

---

### Building intelligent tools to support responsible security research.
