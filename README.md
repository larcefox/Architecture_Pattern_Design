# Architecture_Pattern_Design
GB Architecture and Pattern Design course

# launch
gunicorn main:application --bind=127.0.0.1:8080 --reload -timeout=7200

# lesson2 curl test
curl -d "param1=value1&param2=value2" -X POST http://127.0.0.1:8080/

# lesson4 updates
/admin/