Simple function with just the admin enabled along with an app included just for example. Meant to be used as a starter for your very own django app wrapped in a function.
## Requirements
* [Azure Function Core Tools](https://github.com/Azure/azure-functions-core-tools/releases)
* [Python 3.9](https://www.python.org/downloads/release/python-3910/)
* [Microsoft Visual C++ Build tools v142](https://visualstudio.microsoft.com/downloads/) Use the visual studio installer to install
* [VSCode](https://code.visualstudio.com/Download)
* VSCode Extensions
   * [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
   * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)


## Birth Certificate
1. Run this
    ```
    python -m venv .venv
    .venv\scripts\activate
    func init --python
    func new --name MyFunction --template "HTTP trigger" --authlevel "anonymous"
    ```
1. add to [requirements.txt](requirements.txt)
    ```
    azure-functions
    django
    whitenoise
    ```
1. run:
    ```
    pip install -r requirements.txt
    django-admin startproject djangoAPI .
    django-admin startproject MyApp
    ```
1. Update [MyFunction\function.json](MyFunction/function.json) to include `"route": "MyFunction/{*path_info}"` in `bindings`
1. Update [MyFunction\init.py](MyFunction/__init__.py)
   * Redefine `main` in  
   * ```
     from djangoAPI.wsgi import application

     def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
         return func.WsgiMiddleware(application).handle(req, context)
     ```
1. Update [djangoAPI\settings.py](djangoAPI/settings.py)
   * add `FUNCTION_APP_PATH = 'api/ServiceFunction'`
   * modity `STATIC_URL` to `STATIC_URL = '/' + FUNCTION_APP_PATH + '/static/'`
1. Update [djangoAPI\urls.py](djangoAPI/urls.py) admin path
   * `path(FUNCTION_APP_PATH + '/admin/', admin.site.urls)`
1. Setup Django admin
   * ```
     python .\manage.py makemigrations
     python .\manage.py migrate
     python .\manage.py createsuperuser
     ```
