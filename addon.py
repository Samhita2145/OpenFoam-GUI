""" Blender Python Script for Grid-Based Cube Creation

Note:
Due to hardware and OpenGL limitations (Intel HD Graphics 4400),
the addon UI could not be registered in Blender 2.93.
This script demonstrates the required logic using Blender's bpy API.
"""

import bpy
import math


def create_cube_grid(N):
    """
    Creates N cubes arranged in a 2D grid.
    N must be less than 20.
    """
    if N > 20:
        raise ValueError("N must be less than 20")

    # Remove existing cubes
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and obj.name.startswith("Cube"):
            bpy.data.objects.remove(obj, do_unlink=True)

    cols = math.ceil(math.sqrt(N))
    spacing = 2

    for i in range(N):
        x = (i % cols) * spacing
        y = (i // cols) * spacing

        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0))


def delete_selected_cubes():
    """
    Deletes all selected mesh objects.
    """
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            bpy.data.objects.remove(obj, do_unlink=True)
