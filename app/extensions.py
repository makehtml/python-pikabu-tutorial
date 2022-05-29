# from flask_babel import Babel
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_executor import Executor
# from flask_mailman import Mail

# from flask_mailing import Mail
from flask_migrate import Migrate

# from flask_resize import Resize
# from flask_security import Security
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# from flask_whooshee import Whooshee
from flask_wtf.csrf import CSRFProtect

# babel = Babel()
# csrf = CSRFProtect()
db = SQLAlchemy()
# executor = Executor()
# mail = Mail()
migrate = Migrate()
# resize = Resize()
# security = Security()
# session = Session()
# toolbar = DebugToolbarExtension()
# whooshee = Whooshee()
