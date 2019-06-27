from jobplus.Configs.password import DevelopmentPassword, DevelopmentSecretKey
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/jobplus?charset=utf8'.format(DevelopmentPassword)
SECRET_KEY = DevelopmentSecretKey