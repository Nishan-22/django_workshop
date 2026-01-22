#!/user/bin/env bash
#exit on error
set -o errexit


pip instrall -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput