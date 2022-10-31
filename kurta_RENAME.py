
"""
pant_FRONT_2683
1 : disp
5 : norm
6 : diff

"""

import bpy

mat = 'pant_FRONT_2683'
print('-----')
nodes = bpy.data.materials[mat].node_tree.nodes
print(bpy.data.materials[mat])

#nodes[1].name = 'disp'
#nodes[5].name = 'norm'
#nodes[6].name = 'diff' 

i = 0
for node in nodes:
    try:
        print(f'{node}, {node.image}  : {i}')
    except:
        pass
    i+=1
    
    
"""
'kurta_FRONT_2692'

0 : diff
1 : norm
6 : disp

"""

mat = 'kurta_FRONT_2692'
print('-----')
print(bpy.data.materials[mat])
nodes = bpy.data.materials[mat].node_tree.nodes

#nodes[0].name = 'diff'
#nodes[1].name = 'norm'
#nodes[6].name = 'disp' 

i = 0  
for node in nodes:
    try:
        print(f'{node}, {node.image}  : {i}')
    except:
        pass
    i+=1



"""
'Material3016'

0 : norm
2 : diff
6 : disp

"""

mat = 'Material3016'
print('-----')
print(bpy.data.materials[mat])
nodes = bpy.data.materials[mat].node_tree.nodes

#nodes[0].name = 'norm'
#nodes[2].name = 'diff'
#nodes[6].name = 'disp' 

i = 0  
for node in nodes:
    try:
        print(f'{node}, {node.image}  : {i}')
    except:
        pass
    i+=1


    