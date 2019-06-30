from enum import Enum, unique


@unique
class DeployType(Enum):
    Development = 'DevelopmentConfig.py'
    Production = 'ProductionConfig.py'
    Test = 'TestingConfig.py'

    def configPath(self) -> str:
        return 'Configs/{}'.format(self.value)


preConfig = {
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    "ADMIN_PER_PAGE": 20,
    "INDEX_PER_PAGE": 8
}
