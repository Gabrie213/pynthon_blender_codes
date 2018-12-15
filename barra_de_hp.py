from bge import logic as g

c = g.getCurrentController()
o = c.owner

cena = g.getCurrentScene()

for i in c.sensors:
    exec(i.name+"=i")
    
#if ini.positive:
g.addScene("hud")
    
hud = g.getSceneList()[1].objects
barra = hud["barraDeVida"]

barra.localScale[0] = o['vida']/120

if sensorCollision.positive:
    o['vida']-= 1

if o ['vida'] < 1:
    o['vida'] = 0  
