import random, os
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
log = logging.getLogger(__name__)


REPO_URL = 'https://github.com/Emmanuel289/python-tdd.git'
KEY_FILENAME = os.path.join(os.environ['HOME'], '.ssh/staging-key.pem')

def deploy():
    """
    Main function used by fabric to automate the deployment to the server
    """

    log.info('Creating site folder')
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    

    with cd(site_folder):
         _get_latest_source()
         _update_virtualenv()
         _create_or_update_dotenv()
         _update_static_files()
         _update_database()
    

def _get_latest_source():
    """
    Pulls down our source code with Git
    """
    log.info("Pulling down source code")
   
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    """
    Create or update the virtualenv
    """
    log.info("Creating or updating the virtualenv")
    if not exists('virtualenv/bin/pip'):
        run(f'python3 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    """
    Create a new env file if necessary
    """
    log.info("Creating new .env file if necessary")
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')
    email_password = os.environ['EMAIL_PASSWORD']
    append('.env', f'EMAIL_PASSWORD={email_password}')


def _update_static_files():
    """
    Update the static files
    """
    log.info("Updating the static files")
    run('./virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    """
    Migrate the database if necessary
    """
    log.info("Migrate the database if necessary")
    run('./virtualenv/bin/python manage.py migrate --noinput')
