# Task 2: Blender Python Script for Cube Grid Manipulation

## Overview
This task demonstrates the use of Blender's Python API (`bpy`) to
programmatically create and manipulate 3D objects.

Due to hardware and OpenGL limitations on the system
(Intel HD Graphics 4400), Blender addon UI registration could not be
completed successfully. Therefore, the task has been implemented
using a Blender Python script approach, which uses the same `bpy`
API and logic as an addon.

## Features Implemented

### Cube Grid Creation
- Creates N cubes arranged in a 2D grid
- Enforces constraint: N < 20
- Automatically clears existing cubes before creation

### Delete Selected Cubes
- Deletes all selected mesh objects from the scene

## How the Script Works
- Uses Blender's `bpy.ops.mesh.primitive_cube_add` to create cubes
- Positions cubes using a grid-based calculation
- Uses Blender data API to remove selected objects

## Limitations
- UI panel and buttons could not be registered due to system graphics limitations
- The logic is implemented as a script instead of an interactive addon

## Conclusion
This implementation demonstrates understanding of Blender's Python API,
object manipulation, and logical problem-solving, while adapting to
system constraints in a transparent and professional manner.
