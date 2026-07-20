import hmac
import hashlib
import os
import subprocess
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def deploy_webhook(request):
    # Retrieve signature header from GitHub
    signature = request.META.get('HTTP_X_HUB_SIGNATURE_256')
    if not signature:
        return HttpResponseForbidden("Missing signature")

    # Retrieve secret token from settings/environment
    webhook_secret = os.getenv('DEPLOY_WEBHOOK_SECRET')
    if not webhook_secret:
        return HttpResponseForbidden("Webhook not configured on server")

    # Validate HMAC signature
    payload = request.body
    mac = hmac.new(webhook_secret.encode('utf-8'), msg=payload, digestmod=hashlib.sha256)
    expected_signature = 'sha256=' + mac.hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        return HttpResponseForbidden("Invalid signature")

    # Run deployment commands
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        # Run git pull
        subprocess.run(["git", "pull"], cwd=project_dir, check=True)
        
        # Touch WSGI file to reload PythonAnywhere webapp
        username = os.environ.get('USER', 'sudarshankakde')
        wsgi_path = f"/var/www/{username}_pythonanywhere_com_wsgi.py"
        if os.path.exists(wsgi_path):
            os.utime(wsgi_path, None)
        return HttpResponse("Deployment successful")
    except Exception as e:
        return HttpResponse(f"Deployment failed: {str(e)}", status=500)
