import subprocess

from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    subprocess.run(["python", "-Xutf8", "./manage.py", "dumpdata"], stdout=open("database.json", "w"), check=True)
    return User.objects.count()
