import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from a2wsgi import ASGIMiddleware

from main import app as asgi_app

application = ASGIMiddleware(asgi_app)
