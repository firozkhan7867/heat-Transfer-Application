from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),


    path('conduction',views.conduction,name="conduction"),
    path('conduction/slabs/input1',views.conductionSlabInput1,name="conduction-slabs-input1"),
    path('conduction/slabs/input2',views.conductionSlabInput2,name="conduction-slabs-input2"),
    path('conduction/slabs/input3',views.conductionSlabInput3,name="conduction-slabs-input3"),
    path('conduction/slabs/solution',views.conductionSlabSolution,name="conduction-slabs-solution"),
    path('conduction/sphere/input1',views.conductionSphereInput1,name="conduction-sphere-input1"),
    path('conduction/sphere/input2',views.conductionSphereInput2,name="conduction-sphere-input2"),
    path('conduction/sphere/input3',views.conductionSphereInput3,name="conduction-sphere-input3"),
    path('conduction/sphere/solution',views.conductionSphereSolution,name="conduction-sphere-solution"),
    path('conduction/cylinder/input1',views.conductionCylinderInput1,name="conduction-cylinder-input1"),
    path('conduction/cylinder/input2',views.conductionCylinderInput2,name="conduction-cylinder-input2"),
    path('conduction/cylinder/input3',views.conductionCylinderInput3,name="conduction-cylinder-input3"),
    path('conduction/cylinder/solution',views.conductionCylinderSolution,name="conduction-cylinder-solution"),




    path('lcha',views.lcha,name="lcha"),
    path('lcha/slabs/input1',views.lchaSlabInput1,name="lcha-slabs-input1"),
    path('lcha/slabs/input2',views.lchaSlabInput2,name="lcha-slabs-input2"),
    path('lcha/slabs/input3',views.lchaSlabInput3,name="lcha-slabs-input3"),
    path('lcha/slabs/solution',views.lchaSlabSolution,name="lcha-slabs-solution"),
    path('lcha/sphere/input1',views.lchaSphereInput1,name="lcha-sphere-input1"),
    path('lcha/sphere/input2',views.lchaSphereInput2,name="lcha-sphere-input2"),
    path('lcha/sphere/input3',views.lchaSphereInput3,name="lcha-sphere-input3"),
    path('lcha/sphere/solution',views.lchaSphereSolution,name="lcha-sphere-solution"),
    path('lcha/cylinder/input1',views.lchaCylinderInput1,name="lcha-cylinder-input1"),
    path('lcha/cylinder/input2',views.lchaCylinderInput2,name="lcha-cylinder-input2"),
    path('lcha/cylinder/input3',views.lchaCylinderInput3,name="lcha-cylinder-input3"),
    path('lcha/cylinder/solution',views.lchaCylinderSolution,name="lcha-cylinder-solution"),
    path('lcha/cube/input1',views.lchaCubeInput1,name="lcha-cube-input1"),
    path('lcha/cube/input2',views.lchaCubeInput2,name="lcha-cube-input2"),
    path('lcha/cube/input3',views.lchaCubeInput3,name="lcha-cube-input3"),
    path('lcha/cube/solution',views.lchaCubeSolution,name="lcha-cube-solution"),
    path('heat',views.heat,name="heat"),
]

