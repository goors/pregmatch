import sys
sys.path.append('/Volumes/Data/projects/pregmatch/')
from flask.ext.sqlalchemy import SQLAlchemy
from blog import app as appp
db = SQLAlchemy(appp)
