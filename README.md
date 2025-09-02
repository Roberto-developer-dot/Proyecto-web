📌 Guía de instalación para compañeros
🔹 1. Clonar el repositorio
Abre la terminal (PowerShell, CMD o Git Bash) y ejecuta:
git clone https://github.com/Roberto-developer-dot/Proyecto-web.git
cd Proyecto-web
🔹 2. Crear el entorno virtual (venv)
En Windows:
python -m venv venv
venv\Scripts\activate
👉 Verás que aparece algo como (venv) al inicio de la terminal, lo que significa que ya está activo.
🔹 3. Instalar dependencias
Ejecutar:
pip install -r requirements.txt
Esto instalará Django y cualquier otra librería que use el proyecto.
🔹 4. Aplicar migraciones de la base de datos
python manage.py migrate
Esto prepara la base de datos local.
🔹 5. Levantar el servidor
python manage.py runserver
Ahora abre tu navegador en 👉 http://127.0.0.1:8000/ y verás el proyecto corriendo. 🚀

