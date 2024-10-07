from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import * #Importa todo lo que haya en el modelo (mas facil)
from django.contrib import messages

#Index del sistema
def index(request):
    control = request.session.get("logueado", False)
    if control:
        return render(request,"index.html")
    else: 
        messages.warning(request, "Por favor inicie sesion ...")
        return redirect ("login")


#Ingresar al sistema
def login(request):
    if request.method == "POST":
        #procesar datos
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")
        #select * from Usuario where email = " " and clave = " "
        try:
            q = Usuario.objects.get(correo=correo, clave=clave)# la coma funciona como un {AND}
            messages.success(request, "Bienvenido!!")
            datos = {
                "id":q.id,
                "nombre":q.nombre,
                "apellido":q.apellido,
                "rol":q.rol
            }
            #Crear una variable de sesion (variable que tiene datos y seguirle la pista al usuario)
            request.session["logueado"] = datos #Esto es para que exita a lo largo del proyecto
            return redirect("index")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o Contraseña no validos D:")
            return redirect("login")
    else:
        control = request.session.get("logueado", False)
        if control == False:
            return render (request,"login/login_form.html")
        else:
            return redirect ("index")         
        
#Salir del sistema
def logout(request):
    try:
        del request.session["logueado"]
        return redirect ("login")
    except:
        messages.error(request, "Erroe, intente de nuevo D:")
        return redirect("index")
    
#Crear un nuevo perfil-formulario
def nuevo_perfil_form(request):
    if request.method == "POST":
        # Procesar los datos del formulario
        correo = request.POST.get("correo")
        nombre = request.POST.get("nombre")  
        apellido = request.POST.get("apellido")  
        clave = request.POST.get("clave")  
        rol = request.POST.get("rol")  

        try:
            # Crear y guardar el nuevo perfil
            query = Usuario(
                correo=correo,
                nombre=nombre,
                apellido=apellido,
                clave=clave,
                rol=rol,
            )
            query.save()
            # Mostrar mensaje de éxito
            messages.success(request, "Perfil creado correctamente")
            # Redirigir a la página de inicio de sesión
            return redirect('login')  # Cambia esto si es necesario

        except Exception as e:
            # Mostrar mensaje de error
            messages.error(request, f"Ocurrió un error. No se guardó el perfil: {e}")
    
    return render(request, 'login/nuevperf_form.html')
