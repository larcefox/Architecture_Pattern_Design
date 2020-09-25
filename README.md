# Architecture_Pattern_Design
GB Architecture and Pattern Design course

#launch

gunicorn main_wsgi:application --bind=127.0.0.1:8080 --reload -timeout=7200
