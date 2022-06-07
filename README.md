># django-cursos
>## Proyecto de aprendizaje de django 
>### Nota: para el contenido de entre comillas dobles sustituir el contenido y eliminar comillas.  
>
>Algunos pasos --por confirmar los orrectos despues de clonar el proyecto.
>
>1.- git clone git@github.com:"tu usuario"/django-cursos.git   
>2.- cd django-curso 
>3.- docker-compose run web django-admin startproject "nombre del proyecto(TiendaOnline)" .   
>4.- docker-compose up -d  
>
>5.- docker ps 
>6.- docker exec -ti "bb02e78306cf-container id" /bin/bash  
>
>## Si estas clonando este proyecto
> python manage.py migrate  
> python manage.py createsuperuser   
>
>
>## Para iniciar el proyecto desde 0 
> python manage.py startapp "nombre del proyecto (gestionPedidos)"  
> python manage.py startapp "nombre del proyecto (gestionPedidos)"  
> python manage.py check "nombre del proyecto (gestionPedidos)"  
> python manage.py makemigrations  
> python manage.py sqlmigrate "nombre del proyecto (gestionPedidos)" 0001  
> python manage.py migrate  
> python manage.py createsuperuser 
