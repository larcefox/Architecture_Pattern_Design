# Architecture_Pattern_Design
GB Architecture and Pattern Design course

#launch.json for vscode
{
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Python: Webapp",
            "type": "python",
            "request": "launch",
            "program": "/home/larce/.virtualenvs/APD/bin/gunicorn",
            "gevent": true,
            "args": ["main_wsgi:application", "--bind=127.0.0.1:8080", "--reload", "--timeout=7200"],  //"--bind=127.0.0.1:8080", "--reload", "--worker-class", "eventlet", "-w", "1", "--timeout=7200"
            //"postDebugTask": "killdebugger",
            "console": "integratedTerminal"
        }
    ]
}

#bash
gunicorn main_wsgi:application --bind=127.0.0.1:8080 --reload -timeout=7200
