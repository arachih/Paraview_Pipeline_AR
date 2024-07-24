import bpy
import os

# Define the directory and file name pattern
pathName = "C:/Users/Azeddine.Rachih/OneDrive - Eramet SA/ParaView/ParaView_Pipeline_VR/shell/"
fileName = "shell"
numRange = list(range(37))

# Scaling factor
scale_factor = 0.001

# Function to apply scaling to an object
def apply_scaling(obj, scale_factor):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
    bpy.ops.object.transform_apply(scale=True)

# Get all objects in the scene
objects = bpy.data.objects

for i in numRange:
    # Construct the object name with leading zeroes (up to 3 digits)
    obj_name = f"{fileName}_{i:03d}"
    
    # Check if the object exists
    print(obj_name)
    if obj_name in objects:
        print(obj_name)
        obj = objects[obj_name]
        
        # Apply scaling to the object
        apply_scaling(obj, scale_factor)
        
        # Export the scaled object
        #output_path = os.path.join(pathName, f"{obj_name}_scaled.ply")
        #bpy.ops.export_mesh.ply(filepath=output_path, use_selection=True)

print("Scaling and export completed.")

# Function to apply smooth shading and material to an object
def apply_material_to_object(obj, mat_name, i):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    
    # Apply smooth shading
    bpy.ops.object.shade_smooth()

    # Add color map (material)
    new_mat = bpy.data.materials.new(name=mat_name)
    if len(obj.data.materials):
        # assign to first material slot
        obj.data.materials[0] = new_mat
    else:
        # no slots
        obj.data.materials.append(new_mat)
    
    new_mat.use_nodes = True
    nodes = new_mat.node_tree.nodes
    material_output = nodes.get("Material Output")
    material_input = nodes.get("Material Input")
    node_attribute = nodes.new(type="ShaderNodeAttribute")
    node_attribute.attribute_name = "Col"
    new_mat.node_tree.links.new(node_attribute.outputs[0], nodes.get("Principled BSDF").inputs[0])

# Get all objects in the scene
objects = bpy.data.objects

for i in numRange:
    # Construct the object name with leading zeroes (up to 3 digits)
    obj_name = f"{fileName}_{i:03d}"
    
    # Check if the object exists
    if obj_name in objects:
        obj = objects[obj_name]
        temp_matName = "Material_" + str(i)
        
        # Apply material to the object
        apply_material_to_object(obj, temp_matName, i)

print("Material assignment completed.")



import bpy

pathName = "C:/Users/Azeddine.Rachih/OneDrive - Eramet SA/ParaView/ParaView_Pipeline_VR"
fileName = "shell"
startFrame = 0
endFrame = 36
numRange = range(startFrame, endFrame + 1)
isoScale = 1

init_frame = 1
animStep = 2
count = 1

# ANIMATE OBJECTS
for i in range(startFrame, endFrame):
    tempName = f"{fileName}_{i:03d}"
    nextName = f"{fileName}_{i + 1:03d}"

    if tempName in bpy.data.objects and nextName in bpy.data.objects:
        obj_current = bpy.data.objects[tempName]
        obj_next = bpy.data.objects[nextName]

        # Animate current object
        obj_current.scale = [isoScale, isoScale, isoScale]
        obj_current.keyframe_insert(data_path="scale", frame=count)

        obj_next.scale = [0.0, 0.0, 0.0]
        obj_next.keyframe_insert(data_path="scale", frame=count)

        # Animate next object
        obj_current.scale = [0.0, 0.0, 0.0]
        obj_current.keyframe_insert(data_path="scale", frame=count + animStep)

        obj_next.scale = [isoScale, isoScale, isoScale]
        obj_next.keyframe_insert(data_path="scale", frame=count + animStep)

        count += animStep
    else:
        print(f"Object {tempName} or {nextName} not found in scene")

# ADJUST INTERPOLATION CURVES
for obj in bpy.data.objects:
    if obj.animation_data and obj.animation_data.action:
        fcurves = obj.animation_data.action.fcurves
        for fcurve in fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'CONSTANT'

# ADJUST FRAME RANGE OF ANIMATION
bpy.context.scene.frame_end = init_frame + (endFrame - startFrame + 1) * animStep

# ADD LIGHTING
# Uncomment and adjust lighting setup if needed
# light_data = bpy.data.lights.new(name="my-light-data", type='POINT')
# light_data.energy = 100
# light_object = bpy.data.objects.new(name="LIGHT", object_data=light_data)
# bpy.context.collection.objects.link(light_object)
# light_object.location = (0, 0, 0.5)

# EXPORT FILE
bpy.ops.export_scene.gltf(filepath=pathName + "/" + fileName + "_Dynamic.glb", export_nla_strips=False)

print("Script completed successfully.")


import bpy

pathName = "C:/Users/Azeddine.Rachih/OneDrive - Eramet SA/ParaView/ParaView_Pipeline_VR/"
fileName = "shell"
startFrame = 0
endFrame = 36
isoScale = 1

init_frame = 1
animStep = 2
count = 1

# Check if the scene is clear before starting
bpy.ops.object.select_all(action='SELECT')


# ANIMATE OBJECTS
for i in range(startFrame, endFrame):
    tempName = f"{fileName}_{i:03d}"
    nextName = f"{fileName}_{i + 1:03d}"

    # Check if objects exist before animating
    if tempName in bpy.data.objects and nextName in bpy.data.objects:
        obj_current = bpy.data.objects[tempName]
        obj_next = bpy.data.objects[nextName]

        # Animate current object
        obj_current.scale = [isoScale, isoScale, isoScale]
        obj_current.keyframe_insert(data_path="scale", frame=count)

        obj_next.scale = [0.0, 0.0, 0.0]
        obj_next.keyframe_insert(data_path="scale", frame=count)

        # Animate next object
        obj_current.scale = [0.0, 0.0, 0.0]
        obj_current.keyframe_insert(data_path="scale", frame=count + animStep)

        obj_next.scale = [isoScale, isoScale, isoScale]
        obj_next.keyframe_insert(data_path="scale", frame=count + animStep)

        count += animStep
    else:
        print(f"Object {tempName} or {nextName} not found in scene")

# ADJUST INTERPOLATION CURVES
for obj in bpy.data.objects:
    if obj.animation_data and obj.animation_data.action:
        fcurves = obj.animation_data.action.fcurves
        for fcurve in fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'CONSTANT'

# ADJUST FRAME RANGE OF ANIMATION
bpy.context.scene.frame_end = init_frame + (endFrame - startFrame + 1) * animStep

# EXPORT FILE
bpy.ops.export_scene.gltf(filepath=pathName + "/" + fileName + "_Dynamic.glb", export_nla_strips=False)

print("Script completed successfully.")
