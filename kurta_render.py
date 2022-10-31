import bpy
import os

PATH = '/Users/amanankesh/Desktop/TEXTURE/'
DIFF_PATH = os.path.join(PATH, 'DIFFUSE')
DISP_PATH = os.path.join(PATH, 'DISPLACEMENT')
NORM_PATH = os.path.join(PATH,  'NORMAL')
RENDER_PATH = os.path.join(PATH, 'RENDER')
TEXTURE_PATH = os.path.join(PATH, 'TEXTURE')
TOTAL_RENDER = 6

#append the camera name in the CAMERA_LIST
CAMERA_LIST = ['Camera'] 
#append the materials name in the MATERIAL_LIST
MATERIAL_LIST = ['kurta_FRONT_2692', 'pant_FRONT_2683', 'Material3016']

def read_images(NORM_PATH, DISP_PATH, DIFF_PATH):
    norm_list = sorted(os.listdir(NORM_PATH))
    disp_list = sorted(os.listdir(DISP_PATH))
    diff_list = sorted(os.listdir(DIFF_PATH))

    MAP_DATA = []
    total = len(norm_list)
    for i in range(total):
        norm = norm_list[i]
        disp = disp_list[i]
        diff = diff_list[i]
        name = norm_list[i]
        
        if norm == '.DS_Store' or disp == '.DS_Store' or diff == '.DS_Store':
            continue
        norm = os.path.join(NORM_PATH, norm)
        disp = os.path.join(DISP_PATH, disp)
        diff = os.path.join(DIFF_PATH, diff)

        map_dict = {
            'name' : name,
            'norm' : norm,
            'disp': disp,
            'diff' : diff
        }

        MAP_DATA.append(map_dict)
        
    return MAP_DATA

def load_maps(maps, materials = ['kurta_FRONT_2692', 'pant_FRONT_2683', 'Material3016']):

    norm = maps['norm']
    disp = maps['disp']
    diff = maps['diff']

    norm = bpy.data.images.load(norm)
    disp = bpy.data.images.load(disp)
    diff = bpy.data.images.load(diff)

    for mat in materials:
        bpy.data.materials[mat].node_tree.nodes['norm'].image = norm
        bpy.data.materials[mat].node_tree.nodes['disp'].image = disp
        bpy.data.materials[mat].node_tree.nodes['diff'].image = diff
        
def render_images(name):
    bpy.context.scene.render.filepath = name
    bpy.ops.render.render(write_still=True)
    

def load_texture(TEXTURE_PATH, mat = 'Man2'):
    TEXTURE_LIST = os.listdir(TEXTURE_PATH)
    norm = os.path.join(TEXTURE_PATH, 'normal.jpg')
    diff = os.path.join(TEXTURE_PATH, 'diffuse.jpg')
    roug = os.path.join(TEXTURE_PATH, 'roughness.jpg')
    meta = os.path.join(TEXTURE_PATH, 'metallic.jpg')


    NORM = bpy.data.images.load(norm)
    DIFF = bpy.data.images.load(diff)
    ROUG = bpy.data.images.load(roug)
    META = bpy.data.images.load(meta)
    
    bpy.data.materials[mat].node_tree.nodes['norm'].image = NORM
    bpy.data.materials[mat].node_tree.nodes['diff'].image = DIFF
    bpy.data.materials[mat].node_tree.nodes['roug'].image = ROUG
    bpy.data.materials[mat].node_tree.nodes['meta'].image = META

#load_texture(TEXTURE_PATH)
MAP_DATA = read_images(NORM_PATH, DISP_PATH, DIFF_PATH)
print('all the maps has been loaded')

for i in range(TOTAL_RENDER):
    try:
        print(f'started rendering for apperal number : {i}')
        load_maps(MAP_DATA[i], MATERIAL_LIST)
        for camera in CAMERA_LIST:
            print(f'started rendering for camera : {camera}')
            name = MAP_DATA[i]['name'].split('.')[0]
            name = f'{name}_{camera}.png'
            name = os.path.join(RENDER_PATH, name)
            bpy.context.scene.camera = bpy.data.objects[camera]
            render_images(name)
            print('completed')
        print(f'completed rendering for apperal number : {i}')
    except: 
        print(f'some issue with apperal number : {i}')
    