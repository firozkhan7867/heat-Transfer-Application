import math

# def convertSpecParams(spec):
#     valDict = {1: ["thickness of wall/ slab", 2],
#                2: ["Radius of cylinder", 2],
#                3: ["Radius of sphere", 3],
#                4: ["Length of cube", 6]}
#     dimension = thickness = float(input("Enter the {} in meters : ".format(valDict[spec][0])))
#     Lc = dimension / valDict[spec][1]
#     specMap = {"dim": dimension, "Lc": Lc}
#     return specMap
def LHCASlab(thick,Temp,Density,specheat,thermalcon,mediumtemp,heatcoeff,Time,Finaltemp):
    def specimen():
        # 1 = plane wall
        # 2 = cylinder
        # 3 = sphere
        # 4 = cube
        # print("\nSelect the type of Solid \n")
        # print(" 1 : Plane Wall \n 2 : Cylinder \n 3 : Sphere \n 4 : Cube\n")
        # spec = int(input("Enter the Number representing type of solid : "))
        # specMap = convertSpecParams(spec)
        specMap={}
        specMap["dim"]=float(thick)
        specMap["Lc"]=thick/2
        specMap["Ti"] = float(Temp)
        specMap["density"] = float(Density)
        specMap["Cp"] = float(specheat)
        specMap["k"] = float(thermalcon)
        
        specMap["Ta"] = float(mediumtemp)
        specMap["h"] = float(heatcoeff)

        # print("\n Select the Unknown parameter : \n")
        # print(" 0 : Final Temperature (Tf) \n 1 : Time Taken (t) \n")
        # unk = int(input("Enter the Value : "))
        
        # specMap["unk"] = unk
        
        if Time == True:
            specMap["Tf"] = float(Finaltemp)
        elif Finaltemp==True:
            specMap["t"] = float(Time)

        return specMap

    def calBiotNumber(paramsMap):
        biotNumber = (paramsMap["h"] * paramsMap["Lc"]) / paramsMap["k"]
        return biotNumber

    def calFourierNumber(paramsMap):
        t = 1 if Time == True else paramsMap["t"]
        fourierNumber = (paramsMap["thermalDiff"] * t ) / paramsMap["Lc"] ** 2
        return fourierNumber
    def calThermalDiffusivity(paramsMap):
        td = paramsMap["k"] / (paramsMap["density"] * paramsMap["Cp"])
        return td

    output={}
    specMap = specimen()
    specMap["thermalDiff"] = calThermalDiffusivity(specMap)
    biotNumber = calBiotNumber(specMap)
    fourNumber = calFourierNumber(specMap)
    exponent = (-1) * biotNumber * fourNumber
    if Finaltemp==True:
        ans = (math.exp(exponent) * (specMap["Ti"] - specMap["Ta"])) + specMap["Ta"]
        output["tf"]=ans
    elif Time==True:
        ans = math.log(((specMap["Tf"] - specMap["Ta"]) / (specMap["Ti"] - specMap["Ta"]))) / exponent
        output["time"]=ans

    return output
        
    
#print(LHCASlab(0.06,100,2700,900,204,500,120,True,250))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
        
    

    
