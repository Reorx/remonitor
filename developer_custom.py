#coding=utf8
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'nmadmin',
        #'NAME': os.path.join(ROOT, '../MEDIA/testDB.sqlite'),
        'USER': 'root',                      # Not used with sqlite3.
        #'USER': '',                      # Not used with sqlite3.
        'PASSWORD': 'mx320lf2',                  # Not used with sqlite3.
        #'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        #'HOST': '10.10.10.59',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        #'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}
