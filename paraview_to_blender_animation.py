import bpy
import os

# Define the directory and file name pattern
pathName = "C:/Users/Azeddine.Rachih/OneDrive - Eramet SA/ParaView/ParaView_Pipeline_VR/shell/"
fileName = "shell"
numRange = list(range(37))

# Scaling factor
scale_factor = 0.001
decimate_ratio = 0.2

# Function to apply scaling to an object
def apply_scaling(obj, scale_factor):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
    bpy.ops.object.transform_apply(scale=True)

# Function to apply a Decimate modifier to an object
def apply_decimate_modifier(obj, ratio):
    # Add a Decimate modifier
    decimate_mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
    decimate_mod.ratio = ratio
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=decimate_mod.name)

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
    node_attribute = nodes.new(type="ShaderNodeAttribute")
    node_attribute.attribute_name = "Col"
    new_mat.node_tree.links.new(node_attribute.outputs[0], nodes.get("Principled BSDF").inputs[0])

# Apply Decimate modifier to all objects
for obj in bpy.data.objects:
    if obj.type == 'MESH':  # Apply only to mesh objects
        apply_decimate_modifier(obj, decimate_ratio)

# Apply scaling and export objects
for i in numRange:
    obj_name = f"{fileName}_{i:03d}"
    
    if obj_name in bpy.data.objects:
        obj = bpy.data.objects[obj_name]
        apply_scaling(obj, scale_factor)
        # Uncomment if you need to export each scaled object
        # output_path = os.path.join(pathName, f"{obj_name}_scaled.ply")
        # bpy.ops.export_mesh.ply(filepath=output_path, use_selection=True)

print("Scaling and Decimate application completed.")

# Animate objects
startFrame = 0
endFrame = 36
isoScale = 1
init_frame = 1
animStep = 2
count = 1

for i in range(startFrame, endFrame):
    tempName = f"{fileName}_{i:03d}"
    nextName = f"{fileName}_{i + 1:03d}"

    if tempName in bpy.data.objects and nextName in bpy.data.objects:
        obj_current = bpy.data.objects[tempName]
        obj_next = bpy.data.objects[nextName]

        obj_current.scale = [isoScale, isoScale, isoScale]
        obj_current.keyframe_insert(data_path="scale", frame=count)

        obj_next.scale = [0.0, 0.0, 0.0]
        obj_next.keyframe_insert(data_path="scale", frame=count)

        obj_current.scale = [0.0, 0.0, 0.0]
        obj_current.keyframe_insert(data_path="scale", frame=count + animStep)

        obj_next.scale = [isoScale, isoScale, isoScale]
        obj_next.keyframe_insert(data_path="scale", frame=count + animStep)

        count += animStep
    else:
        print(f"Object {tempName} or {nextName} not found in scene")

# Adjust interpolation curves
for obj in bpy.data.objects:
    if obj.animation_data and obj.animation_data.action:
        fcurves = obj.animation_data.action.fcurves
        for fcurve in fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'CONSTANT'

# Adjust frame range of animation
bpy.context.scene.frame_end = init_frame + (endFrame - startFrame + 1) * animStep

# Export file
bpy.ops.export_scene.gltf(filepath=pathName + "/" + fileName + "_Dynamic.glb", export_nla_strips=False)

print("Script completed successfully.")


# Clean all animations

# import bpy

# # Clear all keyframes from all objects
# for obj in bpy.data.objects:
#     if obj.animation_data and obj.animation_data.action:
#         obj.animation_data_clear()  # Clear keyframes from this object

# # Remove all actions
# for action in bpy.data.actions:
#     bpy.data.actions.remove(action)

# # Purge orphaned data
# bpy.ops.outliner.orphans_purge()

# print("All animations have been cleared.")
