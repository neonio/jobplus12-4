from jobplus.Configs.password import TestingPassword, TestingSecretKey
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/jobplus?charset=utf8'.format(TestingPassword)
SECRET_KEY = TestingSecretKey