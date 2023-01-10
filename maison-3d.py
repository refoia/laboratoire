
import bpy

# Définition des dimensions de la maison
width = 10
depth = 10
height = 10

# Création d'un cube pour représenter la maison
bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
bpy.ops.transform.resize(value=(width, depth, height))

# Création d'un toit en triangle
bpy.ops.mesh.primitive_plane_add(size=1, location=(0,0,height))
bpy.ops.transform.resize(value=(width, depth, height))
bpy.ops.transform.rotate(value=1.5708, axis=(1,0,0))

# Ajout d'une porte
door_width = 1
door_depth = 0.5
bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
bpy.ops.transform.resize(value=(door_width, door_depth, height))
bpy.ops.transform.translate(value=(-(width-door_width)/2, -(depth-door_depth)/2, 0))

# Ajout de fenêtres
window_width = 1
window_depth = 1
bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
bpy.ops.transform.resize(value=(window_width, window_depth, height))
bpy.ops.transform.translate(value=(-(width-window_width)/2, (depth-window_depth)/2, 0))

bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
bpy.ops.transform.resize(value=(window_width, window_depth, height))
bpy.ops.transform.translate(value=((width-window_width)/2, (depth-window_depth)/2, 0))

# Ajout d'un sol
bpy.ops.mesh.primitive_plane_add(size=1, location=(0,0,0))
bpy.ops.transform.resize(value=(width, depth, height))
bpy.ops.transform.rotate(value=1.5708, axis=(1,0,0))

# Affichage de la maison en 3D
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.view3d.camera_to_view_selected()
bpy.ops.object.mode_set(mode='EDIT')



# Ce code crée un cube pour 
# représenter la maison, ajoute 
# un toit en triangle, une porte et
#  des fenêtres, puis ajoute un sol.
#  Enfin, il affiche la maison 
# en 3D en sélectionnant tous 
# les objets et en faisant pivoter la
#  caméra pour vo















