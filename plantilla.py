print('Bienvenido al WindfuryWeapon calculator')

#
Nivel = input('Ingrese su nivel: ')

try:
    Nivel = int(Nivel)
except:
    Nivel = ('Palabra')

if Nivel == 'Palabra':
    print('El valor ingresado no es numero')
    exit()

#       
Fuerza = input('Introduzca su fuerza: ')

try:
    Fuerza = int(Fuerza)
except:
    Fuerza = ('Palabra')

if Fuerza == 'Palabra':
    print('El valor ingresado no es numero')
    exit()

#
Agilidad = input('Ingrese su agilidad: ')

try:
    Agilidad = int(Agilidad)
except:
    Agilidad = ('Palabra')

if Agilidad == 'Palabra':
    print('El valor ingresado no es numero')
    exit()

#
AttackPowerBonus = input('Introduce Attack Power Bonuses: ')

try:
    AttackPowerBonus = float(AttackPowerBonus)
except:
    AttackPowerBonus = ('Palabra')

if AttackPowerBonus == 'Palabra':
    print('Value is not a number')
    exit()

#
ArmaMin = input('Ingrese el daño minimo: ')

try:
    ArmaMin = float(ArmaMin)
except:
    ArmaMin = ('Palabra')

if ArmaMin == 'Palabra':
    print('El valor ingresado no es numero')
    exit()

#
ArmaMax = input('Ingrese el daño maximo: ')

try:
    ArmaMax = float(ArmaMax)
except:
    ArmaMax = ('Palabra')

if ArmaMax == 'Palabra':
    print('El valor ingresado no es un numero')
    exit()

#
ArmaSpeed = input('Ingrese la velocidad de ataque: ')

try:
    ArmaSpeed = float(ArmaSpeed)
except:
    ArmaSpeed = ('Palabra')

if ArmaSpeed == 'Palabra':
    print('El valor ingresado no es un numero')
    exit()

#
Timespace = input('Ingrese tiempo: ')

try:
    Timespace = float(Timespace)
except:
    Timespace = ('Palabra')

if Timespace == 'Palabra':
    print('El valor ingresado no es un numero')
    exit()


Class = input('Introduce Class: ')

try:
    Class = str(Class)
except:
    Class = int

#######
def warr_pala(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace):

        AttackPower1 = (AttackPowerBonus) + Nivel * 3 + (Fuerza * 2) - 20 # War y pal
        avg1 = ((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + AttackPower1/14) * ArmaSpeed
        hits = Timespace/ArmaSpeed
        dpsall1 = avg1 * hits 
        proc1 = (((((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + (AttackPower1 + 104)/14) * ArmaSpeed)) * 2)  * (20/100)
        resultado_1 = print('El daño durante', Timespace,'Sec', 'sera de:', dpsall1, '\n' 'El daño con Windfury durante', Timespace,'Sec', 'sera de:', dpsall1 + proc1)
        
        
        return warr_pala(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,resultado_1)
         
######

def shaman(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace):

        AttackPower2 = (AttackPowerBonus) + Nivel * 2 + (Fuerza * 2) - 20 # Shaman
        avg2 = ((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + AttackPower2/14) * ArmaSpeed
        hits = Timespace/ArmaSpeed
        dpsall2 = avg2 * hits   
        proc2 = (((((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + (AttackPower2 + 104)/14) * ArmaSpeed)) * 2)  * (20/100)
        resultado_2 = print('El daño durante', Timespace,'Sec', 'sera de:', dpsall2, '\n' 'El daño con Windfury durante', Timespace,'Sec', 'sera de:', dpsall2 + proc2 )
        

        return shaman(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,resultado_2)

########

def rog_hunt(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,Agilidad):
        AttackPower3 = (AttackPowerBonus) + Nivel * 2 + (Fuerza) + (Agilidad) - 20 # Rogue Hunter
        avg3 = ((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + AttackPower3/14) * ArmaSpeed
        hits = Timespace/ArmaSpeed
        dpsall3 = avg3 * hits
        proc3 = (((((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + (AttackPower3 + 104)/14) * ArmaSpeed)) * 2)  * (20/100)
        resultado_3 = print('El daño durante', Timespace,'Sec', 'sera de:', dpsall3, '\n' 'El daño con Windfury durante', Timespace,'Sec', 'sera de:', dpsall3 + proc3 )
       

        return rog_hunt(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,Agilidad,resultado_3)

########

def wizards(AttackPowerBonus, Nivel ,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace):

        AttackPower4 = (AttackPowerBonus) + (Fuerza - 20) # Mage, priest, warlock
        avg4 = ((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + AttackPower4/14) * ArmaSpeed
        hits = Timespace/ArmaSpeed
        dpsall4 = avg4 * hits
        proc4 = (((((((ArmaMin + ArmaMax)/2)/ArmaSpeed) + (AttackPower4 + 104)/14) * ArmaSpeed)) * 2)  * (20/100)
        resultado_4 = print('El daño durante', Timespace,'Sec', 'sera de:', dpsall4, '\n' 'El daño con Windfury durante', Timespace,'Sec', 'sera de:', dpsall4 + proc4)
        

        return wizards(AttackPowerBonus, Nivel ,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,resultado_4)
    
clase_11 = warr_pala(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace)
clase_22 = shaman(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace)
clase_33 = rog_hunt(AttackPowerBonus, Nivel,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace,Agilidad)
clase_44 = wizards(AttackPowerBonus, Nivel ,Fuerza,ArmaMin,ArmaMax,ArmaSpeed,Timespace)

if Class.lower =='warrior' or  Class.lower == 'paladin':
    print(clase_11)
elif Class.lower == 'shaman':
    print(clase_22)
elif Class.lower == 'rogue' or Class.lower == 'hunter':
    print(clase_33)
elif Class.lower == 'mage' or Class.lower == 'priest' or Class.lower == 'warlock':
    print(clase_44)