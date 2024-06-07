# ทดลองสร้างเว็บไซต์ด้วย PYTHON โดยใช้ DJANGO ทำระบบ crud

สร้างเว็บไซด้วย python django ทดลองทำระบบ create, read, update, delete โดยเชื่อมต่อกับฐานข้อมูล sqlite


## install django
ติดตั้ง django
	
    pip install django

เริ่มต้นโปรเจค

    django-admin startproject app-name

รันโปรเจค

    python manage.py runserver

   
## run project
เริ่มโปรเจ็ค

    pip instll -r requirement.txt

migrate database

    python manage.py makemigrations
    python manage.py migrate
    
สร้าง superuser

    python manage.py createsuperuser
    
รันโปรเจค

    python manage.py runserver
    
