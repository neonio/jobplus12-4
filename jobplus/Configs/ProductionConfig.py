from jobplus.Configs.password import ProductionPassword, ProductionSecretKey
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/jobplus?charset=utf8'.format(ProductionPassword)
SECRET_KEY = ProductionSecretKey