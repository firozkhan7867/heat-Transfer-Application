import math

def convertSpecParams(spec):
    valDict = {1: ["thickness of wall/ slab", 2],
               2: ["Radius of cylinder", 2],
               3: ["Radius of sphere", 3],
               4: ["Length of cube", 6]}
    dimension = thickness = float(input("Enter the {} in meters : ".format(valDict[spec][0])))
    Lc = dimension / valDict[spec][1]
    specMap = {"dim": dimension, "Lc": Lc}
    return specMap

def specimen():
    # 1 = plane wall
    # 2 = cylinder
    # 3 = sphere
    # 4 = cube
    print("\nSelect the type of Solid \n")
    print(" 1 : Plane Wall \n 2 : Cylinder \n 3 : Sphere \n 4 : Cube\n")
    spec = int(input("Enter the Number representing type of solid : "))
    specMap = convertSpecParams(spec)
    specMap["Ti"] = float(input("Enter Initial Temperature of Solid in `C : "))
    specMap["density"] = float(input("Enter Density of Solid in kg/m^3 : "))
    specMap["Cp"] = float(input("Enter Specific Heat of Solid in J/kg-k : "))
    specMap["k"] = float(input("Enter Thermal Conductivity of Solid in W/m-k : "))
    
    specMap["Ta"] = float(input("Enter Temperature of Immersed Medium in `C : "))
    specMap["h"] = float(input("Enter Heat Transfer coefficient of medium in w/m^2-k  : "))

    print("\n Select the Unknown parameter : \n")
    print(" 0 : Final Temperature (Tf) \n 1 : Time Taken (t) \n")
    unk = int(input("Enter the Value : "))
    
    specMap["unk"] = unk
    
    if unk == 1:
        specMap["Tf"] = float(input("\nEnter the final temperature of Solid in `C : \n"))
    else:
        specMap["t"] = float(input("\nEnter the TimeTaken in sec : \n"))

    return specMap

def calBiotNumber(paramsMap):
    biotNumber = (paramsMap["h"] * paramsMap["Lc"]) / paramsMap["k"]
    return biotNumber

def calFourierNumber(paramsMap):
    t = 1 if paramsMap["unk"] == 1 else paramsMap["t"]
    fourierNumber = (paramsMap["thermalDiff"] * t ) / paramsMap["Lc"] ** 2
    return fourierNumber
def calThermalDiffusivity(paramsMap):
    td = paramsMap["k"] / (paramsMap["density"] * paramsMap["Cp"])
    return td

def solve(): 
    specMap = specimen()
    specMap["thermalDiff"] = calThermalDiffusivity(specMap)
    biotNumber = calBiotNumber(specMap)
    fourNumber = calFourierNumber(specMap)
    exponent = (-1) * biotNumber * fourNumber
    if specMap["unk"] == 0:
        ans = (math.exp(exponent) * (specMap["Ti"] - specMap["Ta"])) + specMap["Ta"]
        print("\nThe Final Temperature of the Solid is : {} `C".format(ans))
    else:
        ans = math.log(((specMap["Tf"] - specMap["Ta"]) / (specMap["Ti"] - specMap["Ta"]))) / exponent
        print("\nThe Time Taken for attaining a Final Temperature of {} is : {} seconds".format(specMap["Tf"], ans))
solve()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if spec == 1:
    #     thickness = float(input("Enter the thickness of wall/ slab in meters : "))
    #     specMap["dim"] = thickness
    #     specMap["Lc"] = thickness / 2        
    # if spec == 2:
    #     radius = float(input("Enter the Radius of cylinder in meters : "))
    #     specMap["dim"] = radius
    #     specMap["Lc"] = radius / 2
    # if spec == 3:
    #     radius = float(input("Enter the Radius of sphere in meters : "))
    #     specMap["dim"] = radius
    #     specMap["Lc"] = radius / 3
    # if spec == 4:
    #     length = float(input("Enter the Length of cube in meters : "))
    #     specMap["dim"] = length
    #     specMap["Lc"] = length / 6
        
    

    
