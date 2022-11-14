from django.shortcuts import render
from django.http import HttpResponse
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
        series = request.POST.get('series')
        parallel = request.POST.get('parallel')
        heatCoef1 = request.POST.get('heatCoef1')
        heatCoef2 = request.POST.get('heatCoef2')
        ambTemp1 = request.POST.get('ambTemp1')
        ambTemp2 = request.POST.get('ambTemp2')

        data = {
            "noOfWalls": noOfWalls,
            "crossSecion":crossSecion,
            "series":series,
            "parallel":parallel,
            "heatCoef1":heatCoef1,
            "heatCoef2":heatCoef2,
            "ambTemp1":ambTemp1,
            "ambTemp2":ambTemp2,
        }

        return  render(request,"conduction/slabs/input2.html",data)

    return  render(request,"conduction/slabs/input2.html")


def conductionSlabInput3(request):

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

        data = {
            "sol":0
        }

        return  render(request,"conduction/slabs/input3.html",data)

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
    
