from django.shortcuts import render
from django.http import HttpResponse

#def inicio(request):
 #   return render(request,'paginas/Inicio.html')

def base(request):
    #print(request)
    datos = [
	{'Numero_de_documento': '10009875','Tipo':'CC','nombre':'juan', 'Apellido':'Marquez','Correo':'Juancho@gmail.com','Telefono':'317393'},
	{'Numero_de_documento': '10009875','Tipo':'NIT','nombre':'juan', 'Apellido':'Marquez','Correo':'Juancho@gmail.com','Telefono':'317393'},
    {'Numero_de_documento': '10009875','Tipo':'CC','nombre':'Santi', 'Apellido':'merchan','Correo':'Santi@gmail.com','Telefono':'317393'}
    ]
    
    return render(request,'base.html',context={'Saludo':datos},)

#def inicio(request):
  #  return render(request, 'Inicio/index.html',{'Saludo':'Hello'})
# Create your views here.
