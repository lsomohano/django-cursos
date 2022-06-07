># django-cursos
>## Proyecto de aprendizaje de django 
>
>Algunos pasos --por confirmar los orrectos despues de clonar el proyecto.
>
>1.- git clone git@github.com:lsomohano/django-cursos.git   
>2.- cd django-curso 
>3.- λ docker-compose run web django-admin startproject TiendaOnline . 
>4.- λ docker-compose up -d 
>
>  docker ps 
>λ docker exec -ti "bb02e78306cf-containerid" /bin/bash  
> python manage.py startapp gestionPedidos  
> python manage.py startapp gestionPedidos  
> python manage.py check gestionPedidos  
> python manage.py makemigrations  
> python manage.py sqlmigrate gestionPedidos 0001  
> python manage.py migrate  
> python manage.py createsuperusuario  
