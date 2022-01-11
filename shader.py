from shader_primitives import *

### SHADER

class vertdata(shaderdata):
    colour = fixed4(1.0, 1.0, 1.0, 1.0)
    vertex = fixed4(0.0, 0.0, 0.0, 0.0)
    uv = fixed2(0.0, 0.0)
    vid = 0.0

class fragdata(shaderdata):
    colour = fixed4(1.0, 1.0, 1.0, 1.0)
    fragment = fixed4(0.0, 0.0, 0.0, 0.0)
    uv = fixed2(0.0, 0.0)
    fid = 1.0

def vert(dataIn):
    dataOut = dataIn.copy()
    dataOut.colour.a = 0.50
    return dataOut

def frag(dataIn):
    dataIn.colour.a = 0.26
    dataOut = dataIn.copy()
    print(dataIn.colour.a, dataOut.colour.a)
    dataOut.colour.a = 0.25
    print(dataIn.colour.a, dataOut.colour.a)
    return dataOut

### MAIN

def main():
    #Initial Datatype Testing
    f4 = fixed4(1.0, 2.0, 3.0, 4.0)
    print(f4)
    f4.r = 0.1
    print(f4)
    print(f4.r)
    print(f4.x)
    f4.x = 0.2
    print(f4)
    print(f4.r)
    print(f4.x)

    verts = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0]
    
    while True:
        try:
            for v in range(0, int(len(verts) / 4), 4):
                vertexData = vertdata()
                vertexData.vertex.x = verts[v + 0]
                vertexData.vertex.y = verts[v + 1]
                vertexData.vertex.z = verts[v + 2]
                vertexData.vertex.w = verts[v + 3]
                vertexOut = vert(vertexData)
                #print(vertexOut.vertex)
                frags = [0.0, 0.0, 1.0, 1.0]
                # Sub-Region should be defined by vertices
                for f in range(0, int(len(frags) / 4), 4):
                    fragmentData = fragdata()
                    fragmentData.fragment.r = frags[f + 0]
                    fragmentData.fragment.g = frags[f + 1]
                    fragmentData.fragment.b = frags[f + 2]
                    fragmentData.fragment.w = frags[f + 3]
                    fragmentOut = frag(fragmentData)
                    #Do Something with the Colour here...
                    ###print(fragmentOut.colour)
            break #Uncomment to run once
        except Exception as error:
            print(error)
            #raise #Uncomment to debug on error

### BOOT

if __name__ == "__main__":
    main()

### LOG


""" # Expected Output:
========= RESTART: C:\\Users\\Alastair\\Documents\\Python\\Shader\\shader.py =========
[1.0, 2.0, 3.0, 4.0]
[0.1, 2.0, 3.0, 4.0]
0.1
0.1
[0.2, 2.0, 3.0, 4.0]
0.2
0.2
0.26 0.26
0.26 0.25
>>> f4.rgba
[1.0, 2.0, 3.0, 4.0]
>>> f4.xyzw
[1.0, 2.0, 3.0, 4.0]
>>>
"""
