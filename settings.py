load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PG_DBNAME'),
        'USER': getenv('PG_USER'),
        'PASSWORD': getenv('PG_PASSWORD'),
        'HOST': getenv('PG_HOST'),
        'PORT': getenv('PG_PORT'),
        # 'OPTIONS': {'options': '-c search_path=public,myschema'},
        # 'TEST': {
        #     'NAME': 'test_db',
        # },
    }
}
