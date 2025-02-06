import os
from .base import *

DEBUG = os.environ.get("DEBUG", "True") == "True"

if DEBUG:
    from .dev import *
else:
    from .prod import *
    
