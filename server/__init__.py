import os

from server.app import create_app

config_name = os.getenv('ENV', 'development')
app = create_app(config_name)

# Importing after app setup.
import server.service

if __name__ == '__main__':
    app.run()
