# Smarter-Technologies-Assessment

# Package Sorting Function

This project contains a simple function used to classify packages in a robotic warehouse system.  
The goal is to determine where a package should be dispatched based on its **dimensions** and **mass**.

## Problem Overview

Each package has the following properties:

- **Width (cm)**
- **Height (cm)**
- **Length (cm)**
- **Mass (kg)**

The robotic system sorts packages into three stacks:

| Stack | Description |
|------|-------------|
| **STANDARD** | Package is neither bulky nor heavy and can be handled automatically. |
| **SPECIAL** | Package is either bulky or heavy and requires special handling. |
| **REJECTED** | Package is both bulky and heavy and cannot be processed. |

## Rules

A package is considered **bulky** if:

- The **volume** (width × height × length) is **≥ 1,000,000 cm³**, OR
- **Any dimension** is **≥ 150 cm**

A package is considered **heavy** if:

- The **mass** is **≥ 20 kg**

Sorting logic:

- **Bulky AND Heavy → REJECTED**
- **Bulky OR Heavy → SPECIAL**
- **Neither → STANDARD**

## Function

```python
sort(width, height, length, mass)
