from django.shortcuts import render
from django.http import HttpResponse
import json
from root.mainFunctions.composite_slab import compositeslab
from root.mainFunctions.composite_cylinder import compositesCylinderlab
from root.mainFunctions.composite_sphere import compositesSpherelab
from root.mainFunctions.LHCAslab import LHCASlab
# Create your views here.


def index(request):
    return render(request,'home.html')

    
#----------------------     Conduction    ------------------------------



def conduction(request):
    return  render(request,"conduction/conduction.html")


def conductionSlabInput1(request):
    return  render(request,"conduction/slabs/input1.html")


def conductionSlabInput2(request):
    
    if request.method == 'POST':
        noOfWalls = request.POST.get('noOfWalls')
        crossSecion = request.POST.get('crossSecion')
        walls = request.POST.get('walls')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        # n1 = request.POST.get('n1')

        nt = [i for i in range(int(noOfWalls)+1)]
        nr = [i for i in range(int(noOfWalls))]
        nc = [i for i in range(int(noOfWalls))]

        data = {
            "noOfWalls": noOfWalls,
            "crossSecion":crossSecion,
            "walls":walls,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nt":nt,
            "nr":nr,
            "nc":nc,
            "n1":int(noOfWalls)
        }

        print(data)

        return  render(request,"conduction/slabs/input2.html",data)

    return  render(request,"conduction/slabs/input2.html")


def conductionSlabInput3(request):

    if request.method == 'POST':
        noOfWalls = request.POST.get('noOfWalls')
        crossSecion = request.POST.get('crossSecion')
        walls = request.POST.get('walls')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        n = request.POST.get('n')
        n1 = request.POST.get('n1')
        temps = []
        lengs = []
        therms = []
        
        for i in range(int(n1)+1):
            temps.append(request.POST.get(f"nTemp{i}"))
        for i in range(int(n1)):
            lengs.append(request.POST.get(f"nLength{i}"))
            therms.append(request.POST.get(f"nThermal{i}"))
        

        data = {
            "noOfWalls": noOfWalls,
            "crossSecion":crossSecion,
            "walls":walls,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":json.dumps(temps),
            "nLength":json.dumps(lengs),
            "nThermal":json.dumps(therms),
        }
        

        return  render(request,"conduction/slabs/input3.html",data)
    return  render(request,"conduction/slabs/input3.html")

def conductionSlabSolution(request):
    
    if request.method == 'POST':
        noOfWalls = int(request.POST.get('noOfWalls'))
        crossSecion = float(request.POST.get('crossSecion'))
        walls = request.POST.get('walls')
        heatCoef1 = float(request.POST.get('heatCoef1'))
        heatCoef2 = float(request.POST.get('heatCoef2'))
        ambTemp1 = float(request.POST.get('ambTemp1'))
        ambTemp2 = float(request.POST.get('ambTemp2'))
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        xtemp = request.POST.get('xtemp')
        hRate = request.POST.get('hRate')
        uTemp = request.POST.get('uTemp')
        output = float(request.POST.get('output'))

        series = False
        parallel = False

        if walls == "series":
            series = True
            parallel = False
        elif walls == "parallel":
            parallel = True
            series = False
        

        print(uTemp,xtemp,hRate)

        if xtemp ==  "on":
            xtemp = True
        else:
            xtemp = False
        
        if hRate ==  "on":
            hRate = True
        else:
            hRate = False
        
        if uTemp ==  "on":
            uTemp = True
        else:
            uTemp = False
        
        # print(nTemp)
        # print(nLength)
        # print(nLength)

        nTemp = list(map(float,json.loads(nTemp)))
        # print(nTemp)

        nLength = list(map(float,json.loads(nLength)))
        # print(nLength)

        nThermal = list(map(float,json.loads(nThermal)))
        # print(nThermal)

        data = {
            "noOfWalls": noOfWalls,
            "crossSecion":crossSecion,
            "series":series,
            "parallel":parallel,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":nTemp,
            "nLength":nLength,
            "nThermal":nThermal,
            "xtemp":xtemp,
            "hRate":hRate,
            "uTemp":uTemp,
            "output":output
        }

        print(data)
        data = compositeslab(noOfWalls,nTemp,nThermal,nLength,series,parallel,ambTemp1,ambTemp2,heatCoef1,heatCoef2,crossSecion,hRate,uTemp,xtemp,output)

        print(data)
        

        return  render(request,"conduction/slabs/solution.html",{"data":data})

    return  render(request,"conduction/slabs/solution.html")

def conductionSphereInput1(request):
    return  render(request,"conduction/sphere/input1.html")


def conductionSphereInput2(request):

    if request.method == 'POST':
        nMaterial = request.POST.get('nMaterial')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        # n1 = request.POST.get('n1')

        nt = [i for i in range(int(nMaterial)+1)]
        nr = [i for i in range(int(nMaterial))]
        nc = [i for i in range(int(nMaterial))]

        data = {
            "nMaterial": nMaterial,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nt":nt,
            "nr":nr,
            "nc":nc,
            "n1":int(nMaterial)
        }

        print(data)

        return  render(request,"conduction/sphere/input2.html",data)

    return  render(request,"conduction/sphere/input2.html")


def conductionSphereInput3(request):

    if request.method == 'POST':
        nMaterial = request.POST.get('nMaterial')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        n = request.POST.get('n')
        n1 = request.POST.get('n1')
        temps = []
        lengs = []
        therms = []
        
        for i in range(int(n1)+1):
            temps.append(request.POST.get(f"nTemp{i}"))
        for i in range(int(n1)):
            lengs.append(request.POST.get(f"nLength{i}"))
            therms.append(request.POST.get(f"nThermal{i}"))
        

        data = {
            "nMaterial": nMaterial,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":json.dumps(temps),
            "nLength":json.dumps(lengs),
            "nThermal":json.dumps(therms),
        }
        

        return  render(request,"conduction/sphere/input3.html",data)

    return  render(request,"conduction/sphere/input3.html")

def conductionSphereSolution(request):
        
    if request.method == 'POST':
        nMaterial = int(request.POST.get('nMaterial'))
        heatCoef1 = float(request.POST.get('heatCoef1'))
        heatCoef2 = float(request.POST.get('heatCoef2'))
        ambTemp1 = float(request.POST.get('ambTemp1'))
        ambTemp2 = float(request.POST.get('ambTemp2'))
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        xtemp = request.POST.get('xtemp')
        hRate = request.POST.get('hRate')
        uTemp = request.POST.get('uTemp')
        output = float(request.POST.get('output'))
        
        if xtemp ==  "on":
            xtemp = True
        else:
            xtemp = False
        
        if hRate ==  "on":
            hRate = True
        else:
            hRate = False
        
        if uTemp ==  "on":
            uTemp = True
        else:
            uTemp = False

        nTemp = list(map(float,json.loads(nTemp)))

        nLength = list(map(float,json.loads(nLength)))

        nThermal = list(map(float,json.loads(nThermal)))

        data = {
            "nMaterial": nMaterial,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":nTemp,
            "nLength":nLength,
            "nThermal":nThermal,
            "xtemp":xtemp,
            "hRate":hRate,
            "uTemp":uTemp,
            "output":output
        }

        data = compositesSpherelab(nMaterial,nTemp,nThermal,nLength,ambTemp1,ambTemp2,heatCoef1,heatCoef2,hRate,uTemp,xtemp,output)

        print(data)
        

        return  render(request,"conduction/sphere/solution.html",{"data":data})

    return  render(request,"conduction/sphere/solution.html")



def conductionCylinderInput1(request):
    return  render(request,"conduction/cylinder/input1.html")


def conductionCylinderInput2(request):
    if request.method == 'POST':
        noMatr = request.POST.get('noMatr')
        lCylinder = request.POST.get('lCylinder')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        # n1 = request.POST.get('n1')

        nt = [i for i in range(int(noMatr)+1)]
        nr = [i for i in range(int(noMatr))]
        nc = [i for i in range(int(noMatr))]

        data = {
            "noMatr": noMatr,
            "lCylinder":lCylinder,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nt":nt,
            "nr":nr,
            "nc":nc,
            "n1":int(noMatr)
        }
        print(data)

        return  render(request,"conduction/cylinder/input2.html",data)
    return  render(request,"conduction/cylinder/input2.html")


def conductionCylinderInput3(request):

    if request.method == 'POST':
        noMatr = request.POST.get('noMatr')
        lCylinder = request.POST.get('lCylinder')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        ambTemp2 = request.POST.get('ambTemp2')
        n = request.POST.get('n')
        n1 = request.POST.get('n1')
        temps = []
        lengs = []
        therms = []
        
        for i in range(int(n1)+1):
            temps.append(request.POST.get(f"nTemp{i}"))
        for i in range(int(n1)):
            lengs.append(request.POST.get(f"nLength{i}"))
            therms.append(request.POST.get(f"nThermal{i}"))
        

        data = {
            "noMatr": noMatr,
            "lCylinder":lCylinder,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":json.dumps(temps),
            "nLength":json.dumps(lengs),
            "nThermal":json.dumps(therms),
        }

        print(data)
        

        return  render(request,"conduction/cylinder/input3.html",data)
    return  render(request,"conduction/cylinder/input3.html")

def conductionCylinderSolution(request):
    
    if request.method == 'POST':
        noMatr = int(request.POST.get('noMatr'))
        lCylinder = float(request.POST.get('lCylinder'))
        heatCoef1 = float(request.POST.get('heatCoef1'))
        heatCoef2 = float(request.POST.get('heatCoef2'))
        ambTemp1 = float(request.POST.get('ambTemp1'))
        ambTemp2 = float(request.POST.get('ambTemp2'))
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        xtemp = request.POST.get('xtemp')
        hRate = request.POST.get('hRate')
        uTemp = request.POST.get('uTemp')
        output = float(request.POST.get('output'))

        if xtemp ==  "on":
            xtemp = True
        else:
            xtemp = False
        
        if hRate ==  "on":
            hRate = True
        else:
            hRate = False
        
        if uTemp ==  "on":
            uTemp = True
        else:
            uTemp = False
        

        nTemp = list(map(float,json.loads(nTemp)))
        nLength = list(map(float,json.loads(nLength)))

        nThermal = list(map(float,json.loads(nThermal)))

        data = {
            "noMatr": noMatr,
            "lCylinder":lCylinder,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "nTemp":nTemp,
            "nLength":nLength,
            "nThermal":nThermal,
            "xtemp":xtemp,
            "hRate":hRate,
            "uTemp":uTemp,
            "output":output
        }

        print(data)
        data = compositesCylinderlab(noMatr,nTemp,nThermal,lCylinder,nLength,ambTemp1,ambTemp2,heatCoef1,heatCoef2,hRate,uTemp,xtemp,output)

        print(data)
        

        return  render(request,"conduction/cylinder/solution.html",{"data":data})
    return  render(request,"conduction/cylinder/solution.html")
    

    
#----------------------     LCHA    ------------------------------



def lcha(request):
    return  render(request,"lcha/lcha.html")


def lchaSlabInput1(request):
    return  render(request,"lcha/slabs/input1.html")


def lchaSlabInput2(request):
    if request.method == 'POST':
        nWalls = request.POST.get('nWalls')
        density = request.POST.get('density')
        sheat = request.POST.get('sheat')
        temp = request.POST.get('temp')
        thermal = request.POST.get('thermal')
        # n1 = request.POST.get('n1')

        data = {
            "nWalls": nWalls,
            "density":density,
            "sheat":sheat,
            "temp":temp,
            "thermal":thermal,
        }

        print(data)

        return  render(request,"lcha/slabs/input2.html",data)
    return  render(request,"lcha/slabs/input2.html")


def lchaSlabInput3(request):
    
    if request.method == 'POST':
        nWalls = request.POST.get('nWalls')
        density = request.POST.get('density')
        sheat = request.POST.get('sheat')
        temp = request.POST.get('temp')
        thermal = request.POST.get('thermal')
        pTemp = request.POST.get('pTemp')
        heatTransferCoefficient = request.POST.get('heatTransferCoefficient')
        

        data = {
            "nWalls": nWalls,
            "density":density,
            "sheat":sheat,
            "temp":temp,
            "thermal":thermal,
            "pTemp":pTemp,
            "heatTransferCoefficient":heatTransferCoefficient,
        }

        print(data)
        

        return  render(request,"lcha/slabs/input3.html",data)
    return  render(request,"lcha/slabs/input3.html")

def lchaSlabSolution(request):
    
    if request.method == 'POST':
        nWalls = request.POST.get('nWalls')
        density = request.POST.get('density')
        sheat = request.POST.get('sheat')
        temp = request.POST.get('temp')
        thermal = request.POST.get('thermal')
        pTemp = request.POST.get('pTemp')
        heatTransferCoefficient = request.POST.get('heatTransferCoefficient')
        check = request.POST.get('check')
        time = request.POST.get('time')
        ftemp = request.POST.get('ftemp')

        

        data = {
            "nWalls": nWalls,
            "density":density,
            "sheat":sheat,
            "temp":temp,
            "thermal":thermal,
            "pTemp":pTemp,
            "time":time,
            "ftemp":ftemp,
            "heatTransferCoefficient":heatTransferCoefficient,
        }


        print(data)
        data = LHCASlab(nWalls,temp,density,sheat,thermal,pTemp,heatTransferCoefficient,Time,Finaltemp)
        
    return  render(request,"lcha/slabs/solution.html")

def lchaSphereInput1(request):
    return  render(request,"lcha/sphere/input1.html")


def lchaSphereInput2(request):
    return  render(request,"lcha/sphere/input2.html")


def lchaSphereInput3(request):
    return  render(request,"lcha/sphere/input3.html")

def lchaSphereSolution(request):
    return  render(request,"lcha/sphere/solution.html")



def lchaCylinderInput1(request):
    return  render(request,"lcha/cylinder/input1.html")


def lchaCylinderInput2(request):
    return  render(request,"lcha/cylinder/input2.html")


def lchaCylinderInput3(request):
    return  render(request,"lcha/cylinder/input3.html")

def lchaCylinderSolution(request):
    return  render(request,"lcha/cylinder/solution.html")



def lchaCubeInput1(request):
    return  render(request,"lcha/cube/input1.html")


def lchaCubeInput2(request):
    return  render(request,"lcha/cube/input2.html")


def lchaCubeInput3(request):
    return  render(request,"lcha/cube/input3.html")

def lchaCubeSolution(request):
    return  render(request,"lcha/cube/solution.html")
    


    
def heat(request):
    return  HttpResponse("""HEAT""")
    
