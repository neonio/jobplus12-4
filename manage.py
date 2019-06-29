from jobplus.app import create_app
from jobplus.config import DeployType
app = create_app(DeployType.Development)

if __name__ == '__main__':
    app.run()
