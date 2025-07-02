# making entities (building blocks of making anyhting in ursina)

from ursina import * 
app = Ursina()

# We can make an entity really easily by simply doing:
firstEntity = Entity(model='cube', 
                     color = color.rgb(255, 0, 0), 
                     texture = 'brick', 
                    #  x, y, z
                     position= (0, 0, 0), 
                     rotation = (0, 0, 0),
                    #  scale = (2, 2, 2)
                    #  can set scale for x, y, z as aboe or uniformly as below
                    
                    scale = 2
                     )

# cube is a built in model by ursina, but note that we can pass in our own models
# to ursina using something like blender

# can set colour using rgb or pre-defined color arguments like "blue"

app.run()