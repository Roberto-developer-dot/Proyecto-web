🌱 Trabajo entre ramas en Git
🔹 1. Actualizar siempre main antes de trabajar

Antes de hacer cualquier cosa, asegúrate de tener el código más reciente:

git checkout main
git pull origin main

🔹 2. Crear una nueva rama para tu tarea

Nunca trabajes directamente en main.
Cada funcionalidad o corrección debe hacerse en una rama nueva:

git checkout -b nombre-de-tu-rama


Ejemplo:

git checkout -b feature-login

🔹 3. Hacer cambios y guardarlos

Cuando hayas avanzado en tu tarea:

git add .
git commit -m "Agregada la funcionalidad de login"

🔹 4. Subir tu rama a GitHub
git push origin nombre-de-tu-rama


Ejemplo:

git push origin feature-login

🔹 5. Crear un Pull Request (PR)

Ve a GitHub → tu repositorio.

Verás un aviso: “Compare & pull request”.

Haz clic, describe los cambios y envíalo.

Tus compañeros revisan y aprueban.

Al aprobarlo → se hace el merge a main.

🔹 6. Volver a main y actualizar

Después de que tu rama se haya fusionado:

git checkout main
git pull origin main