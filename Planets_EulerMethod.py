from visual import *

filename="D:\\Fall_2016\\PHYS2300\\Assignment7\\planetData.txt"
datafile = open(filename,"r")

#read 2 lines to skip header
datafile.readline()
datafile.readline()

G = 6.67e-11
objects = []
dt = 6.3e4
AUtoM = (1./1.496e11) #AU to meters conversion
AUtoMS = (86400.)/(1.496e11) # Au/Day to Meters/Second conversion


#===========================================DEFINE PLANETS AND THEIR ATTRIBUTES================================
sun = sphere(pos = (0,0,0), radius=695.7e6, color = color.yellow, make_trail = True)
sun.velocity = vector(0,0,0)
sun.mass = 1.989e30

mercury = sphere(pos=((0.343926450169642/AUtoM),(0.0456154799533135/AUtoM),(-0.0109240372119325/AUtoM)),radius = 2.44e6, color=color.white, make_trail=True)
mercury.velocity = vector((-0.00846653204500986/AUtoMS),  (0.0256146053072818/AUtoMS),  (0.0145868453362396/AUtoMS))
mercury.mass = 3.285e23

venus = sphere(pos=((0.142965184343246/AUtoM),(.647005066033887/AUtoM),(.28248240066038/AUtoM)), radius = 6.052e6, color=color.green, make_trail=True)
venus.velocity = vector((-0.0198938122793425/AUtoMS),  (0.00311311946611859/AUtoMS),  (0.0026594458057458/AUtoMS))
venus.mass = 4.867e24

earth = sphere(pos=((-.136364695954795/AUtoM),(.893397922857/AUtoM),(.387458344639667/AUtoM)), radius = 6.371e6, material = materials.earth, make_trail=True)
earth.velocity = vector((-0.0173199988485296/AUtoMS),  (-0.0022443047317656/AUtoMS),  (-0.000973361115758044/AUtoMS))
earth.mass = 5.927e24

mars = sphere(pos=((-1.36983397618342/AUtoM),(.843135248017904/AUtoM), (.423832906611437/AUtoM)),radius = 3.39e6, color = color.red, make_trail=True)
mars.velocity = vector((-0.0073845383127117/AUtoMS),  (-0.0094773586392742/AUtoMS),  (-0.00415165513666213/AUtoMS))
mars.mass = 6.39e23

jupiter =sphere(pos=((3.34936422369601/AUtoM),(-3.47376144901258/AUtoM), (-1.5721496863938/AUtoM)), radius = 69.911e6, color = color.magenta, make_trail=True)
jupiter.velocity = vector((0.00558564314958231/AUtoMS),  (0.00496226113722250/AUtoMS),  (0.00199227692673937/AUtoMS))
jupiter.mass = 1.898e27

saturn =sphere(pos=((-8.97250506828211/AUtoM),(2.27968200813286/AUtoM), (1.33033860971146/AUtoM)), radius =58.232e6 , color = color.orange, make_trail=True)
saturn.velocity = vector((-0.00185825195699671/AUtoMS),  (-0.00498685858141744/AUtoMS),  (-0.0019802574128075/AUtoMS))
saturn.mass = 5.683e26

uranus =sphere(pos=((-1.00300399532732/AUtoM),(17.3235084732718/AUtoM), (7.60482504641591/AUtoM)), radius =25.362e6 , color = color.cyan, make_trail=True)
uranus.velocity = vector((-0.00395525416301772/AUtoMS),  (-0.000375913785112941/AUtoMS),  (-0.000108849991287794/AUtoMS))
uranus.mass = 8.681e25

neptune =sphere(pos=((-29.1945807386112/AUtoM),(-7.71928519199847/AUtoM), (-2.42724537828877/AUtoM)), radius = 24.622e6, color = color.green, make_trail=True)
neptune.velocity = vector((0.000820748057818085/AUtoMS),  (-0.00277209825958023/AUtoMS),  (-0.00115611603043592/AUtoMS))
neptune.mass = 1.024e26

pluto =sphere(pos=((-26.2336507820155/AUtoM),(20.5619754200559/AUtoM), (14.4445571277807/AUtoM)), radius =1.187e6 , color = color.orange, make_trail=True)
pluto.velocity = vector((-0.00131588869828116/AUtoMS),  (-0.00262012820549352/AUtoMS),  (-0.000427083355026298/AUtoMS))
pluto.mass = 1.30900e22
#===========================================DEFINE PLANETS AND THEIR ATTRIBUTES================================


#===============================Append add Planets to Ojects Array=======================
objects.append(sun)
objects.append(mercury)
objects.append(venus)
objects.append(earth)
objects.append(mars)
objects.append(jupiter)
objects.append(saturn)
objects.append(uranus)
objects.append(neptune)
objects.append(pluto)
#===============================Append add Planets to Ojects Array=======================


#=============================compensates for center of mass===============================

rcm = vector(0,0,0)
vcm = vector(0,0,0)

for i in objects:
  rcm = rcm + i.mass*i.pos
  vcm = vcm + i.mass*i.velocity

totalmass = 0
for i in objects:
  totalmass = totalmass + i.mass
rcm = rcm / totalmass
vcm = vcm / totalmass

for i in objects:
  i.pos = i.pos - rcm
  i.velocity = i.velocity - vcm

#=============================compensates for center of mass===============================



#====================Euler Method to calculate timestep/movement==========================
while(True):
   # rate(50000)
    rate(1000)
    for i in objects:
        i.acceleration = vector(0,0,0)
        for j in objects:
            if i != j:
                dist = j.pos - i.pos
                i.acceleration = i.acceleration + G * j.mass * dist / mag(dist)**3
    for i in objects:
        i.velocity = i.velocity + i.acceleration*dt
        i.pos = i.pos + i.velocity * dt
#====================Euler Method to calculate timestep/movement==========================
