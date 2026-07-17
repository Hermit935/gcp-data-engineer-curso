import functions_framework

@functions_framework.http
def hello_http(request):

    return f'Hello World desde GCP Cloud Functions!'