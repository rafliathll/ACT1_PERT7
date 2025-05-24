from flask import request, jsonfy, current_app
from functools import wraps

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = request.headers.get('X-Api-Key')
        if not current_app.config['API_KEY'] or key not in current_app.config['API_KEY']:            
            current_app.logger.warning(f"Percobaan kunci api tidak sah: {key} dari request")
            return jsonfy({"error": "Tidak berwenang"}), 401
        return f(*args, **kwargs)
    return decorated_function