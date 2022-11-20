from django.shortcuts import render
from django.http import HttpResponse
import json
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

        n = [i for i in range(int(noOfWalls))]

        data = {
            "noOfWalls": noOfWalls,
            "crossSecion":crossSecion,
            "walls":walls,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
            "n":n,
            "n1":int(noOfWalls)
        }

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
        for i in range(int(n1)):
            temps.append(request.POST.get(f"nTemp{i}"))
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
        noOfWalls = request.POST.get('noOfWalls')
        crossSecion = request.POST.get('crossSecion')
        series = request.POST.get('series')
        parallel = request.POST.get('parallel')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')
        nTemp = request.POST.get('nTemp')
        nLength = request.POST.get('nLength')
        nThermal = request.POST.get('nThermal')
        xtemp = request.POST.get('xtemp')
        hRate = request.POST.get('hRate')
        uTemp = request.POST.get('uTemp')
        output = request.POST.get('output')


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
        

        return  render(request,"conduction/slabs/solution.html",data)

    return  render(request,"conduction/slabs/solution.html")

def conductionSphereInput1(request):
    return  render(request,"conduction/sphere/input1.html")


def conductionSphereInput2(request):
    return  render(request,"conduction/sphere/input2.html")


def conductionSphereInput3(request):
    return  render(request,"conduction/sphere/input3.html")

def conductionSphereSolution(request):
    return  render(request,"conduction/sphere/solution.html")



def conductionCylinderInput1(request):
    return  render(request,"conduction/cylinder/input1.html")


def conductionCylinderInput2(request):
    return  render(request,"conduction/cylinder/input2.html")


def conductionCylinderInput3(request):
    return  render(request,"conduction/cylinder/input3.html")

def conductionCylinderSolution(request):
    return  render(request,"conduction/cylinder/solution.html")
    

    
#----------------------     LCHA    ------------------------------



def lcha(request):
    return  render(request,"lcha/lcha.html")


def lchaSlabInput1(request):
    return  render(request,"lcha/slabs/input1.html")


def lchaSlabInput2(request):
    return  render(request,"lcha/slabs/input2.html")


def lchaSlabInput3(request):
    return  render(request,"lcha/slabs/input3.html")

def lchaSlabSolution(request):
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
    
