import mathutils
import bge

def shoot(self):
    obj = self.owner
    vec = mathutils.Vector((0, 1, 0)) 
    sender = obj
    previous = obj.worldPosition
    
    while True: 
        mirror, location, normal = sender.rayCast(sender.worldPosition + vec, None, 60)
        
        bge.render.drawLine(previous, location, mathutils.Color((255, 0, 0)))
        previous = location
        
        if mirror != None and mirror.name.find("Mirror") != -1:
            vec = vec.reflect(normal)
            print(mirror)
            sender = mirror
        else:
            #At this point mirror is the last object hit (not an actual mirror)
            print("Reached end")
            #print(mirror) 
            break

