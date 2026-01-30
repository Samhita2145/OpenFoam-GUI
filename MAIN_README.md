# OpenFOAM Screening Task Submission

## Overview
This repository contains my submission for the OpenFOAM screening tasks as part
of the internship selection process.

The submission consists of **two tasks**, each placed in a separate folder with
its own detailed README.

---

## Task 1: Binary Tree with YAML Integration

### Description
Task 1 focuses on implementing a binary tree data structure in Python and
integrating it with YAML for serialization and deserialization.

### Key Features
- Binary tree implemented using a Node-based structure
- Add, edit, and delete operations using path-based traversal (`L`, `R`, `LL`, etc.)
- Load tree structure from a YAML file
- Write the updated tree back to a YAML file
- Readable tree visualization in the terminal
- Automated unit tests using `pytest`

### How to Run
```bash
cd Task1_BinaryTree_YAML
python main.py
pytest
```

### Output
Tree structure printed in the terminal
Updated tree written to output.yaml

📁 Detailed implementation and design decisions are documented in
Task1_BinaryTree_YAML/README.md

## Task 2: Blender Python Script for Cube Grid Manipulation

### Description
Task 2 demonstrates the use of Blender’s Python API (bpy) to programmatically
create and manipulate 3D objects.

### Key Features
- Creation of N cubes arranged in a 2D grid (N < 20 enforced)
- Deletion of selected mesh objects
- Grid-based positioning logic
- Clean and modular Python implementation

### Implementation Note
Due to hardware and OpenGL limitations on the system (Intel HD Graphics 4400),
Blender add-on UI registration could not be completed reliably.
Therefore, Task 2 is implemented as a Blender Python script using the same
bpy API and logic that an addon would use, with clear documentation of this
limitation.
This approach still demonstrates correct understanding of Blender’s Python API,
object creation, and mesh manipulation.

📁 Detailed explanation and limitations are documented in
Task2_Blender_Addon/README.md