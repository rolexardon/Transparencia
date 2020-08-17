import os
ROOT_PATH =  os.path.dirname(__file__)
SITE_ROOT =  os.path.realpath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
     ('Rolando Ardon', 'rolando_ardon299@hotmail.com'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'OPTIONS': {
                    'init_command': 'SET storage_engine=INNODB',
                    },
        'NAME': 'transparenciadb',       # Not used with sqlite3.
		'USER': '',
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
TIME_ZONE = 'America/Tegucigalpa'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'es'
SITE_ID = 1
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = '/var/www/Transparencia/imagenes_encuestas/'
MEDIA_ROOT = os.path.join(ROOT_PATH, 'imagenes_encuestas')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/imagenes_encuestas/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/var/www/Transparencia/site_static/'
#STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
#STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
#STATIC_ROOT = os.path.join(SITE_ROOT, 'Resources')
#STATIC_ROOT = '/var/www/Transparencia/Resources'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
#TATIC_URL = '/home/rolex/workspace/Transparencia/Transparencia/Resources/'
# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'
#ADMIN_MEDIA_PREFIX = os.path.join(ROOT_PATH, 'Resources/admin/media')
# Additional locations of static files
STATICFILES_DIRS = (
    # Don't forget to use absolute paths, not relative paths.

    #("static_resources","/var/www/Transparencia/Transparencia/Resources"),
    #("static_encuesta","/var/www/Transparencia/Transparencia/Encuesta/Static"),
    #("resources_icons","/var/www/Transparencia/Transparencia/Resources/css/images/icons"),
    #("resources_imgs","/var/www/Transparencia/Transparencia/Resources/css/images"),
    #("resources_css","/var/www/Transparencia/Transparencia/Resources/css"),
    #("resources_reportes","/var/www/Transparencia/Transparencia/Resources/jquery/HighCharts/js"),
    os.path.join(ROOT_PATH, 'static'),
    #os.path.join(ROOT_PATH, 'imagenes_encuestas'),
    #("resources_jquery",os.path.join(ROOT_PATH, 'Resources/jquery')),
    #("resources_icons",os.path.join(ROOT_PATH,'Resources/css/images/icons')),
    #("resources_imgs",os.path.join(ROOT_PATH,'Resources/css/images')),
    #("resources_css",os.path.join(ROOT_PATH,'Resources/css')),
    #("resources_reportes",os.path.join(ROOT_PATH,'Resources/jquery/HighCharts/js')),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
#DEFAULT_FILE_STORAGE = (
 #   'django.core.files.storage.FileSystemStorage',
#)
#STATICFILES_STORAGE = (
 #   'django.contrib.staticfiles.storage.staticfiles_storage',
#)
# Make this unique, and don't share it with anybody.

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
ROOT_URLCONF = 'Transparencia.urls'
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'Templates'),
    os.path.join(ROOT_PATH, 'Administration/Templates'),
    os.path.join(ROOT_PATH, 'Encuesta/Templates'),
    os.path.join(ROOT_PATH, 'Reportes/Templates'),

)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    #'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'Administration',
    'Encuesta',
    'Reportes',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
#AUTHENTICATION_BACKENDS = (
#    'Transparencia.Administration.auth_backends.CustomUserModelBackend',
#)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	#'impostor.backend.AuthBackend',

)
CUSTOM_USER_MODEL = 'Administration.Usuario'
#AUTH_PROFILE_MODULE = "Administration.Usuario"
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
