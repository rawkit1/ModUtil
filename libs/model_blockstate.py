"""
1.12 Blockstate Generator
by enwash
"""
import time
import os
from os.path import join as pjoin

def main(blockName, textureName, ):    
    #-Model Write-#
    fDir = pjoin(os.getcwd(), "__OUTPUT__",  "blocks", "models")
    if (not os.path.exists(fDir)):
        os.makedirs(fDir)
    model = open(pjoin(fDir, blockName.split(":")[1]) + ".json", "w")
    model.write('{\n\t"parent": "block/cube_all",\n\t"textures": {\n\t\t"all": "blocks/' + textureName + '"\n\t}\n}')
    model.close()
    print("Model created at " + pjoin(fDir, blockName.split(":")[1]) + ".json")
    
    #-Blockstate Write-#
    fDir = pjoin(os.getcwd(), "__OUTPUT__", "blocks", "blockstates")
    if (not os.path.exists(fDir)):
        os.makedirs(fDir)
    blockstate = open(pjoin(fDir, blockName.split(":")[1]) + ".json", "w")
    blockstate.write('{\n\t"variants": {\n\t\t"normal": { "model": "' + blockName + '" }\n\t}\n}')
    blockstate.close()
    print("Blockstate created at " + pjoin(fDir, blockName.split(":")[1]) + ".json")
    time.sleep(1)
# main(input("Block name: (i.e. minecraft:dirt)\n"), input("Texture filename: (i.e. diamond_block)\n").split(".png")[0])
