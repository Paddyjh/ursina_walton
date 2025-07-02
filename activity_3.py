# making entities (building blocks of making anyhting in ursina)

from ursina import * 

def update():
    # to have the entity update rotate per frame
    firstEntity.rotation_y += 1
    
    # issue with the above is that items will rotate more or less based on fps
    
    # fix for this is we mutiply by the time between each frame :
    #  we then increase the number we mulitiply as time.dt is less than one
    firstEntity.rotation_y += 50 * time.dt

    # show this running
    
    # to change the position of the entity we can the forward position of the entity
    firstEntity.position += firstEntity.forward * time.dt

    # show this running and can also move right left etc as above 
    # or use a vetor to update left, right etc at smae time as below:
    
    firstEntity.position += Vec3(1, 0, 0) * time.dt


app = Ursina()



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



# looking at the parent argument

# this means that any transformations happening to the parent will be inherited by the child

# good example would be where a player must stay on a moving obsactle like a boat or place, platofrm etc

secondEntity = Entity(
    parent = firstEntity,
    model='sphere', 
    position = (1, 1, 1)
                     )

app.run()