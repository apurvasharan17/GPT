import os
from main import create_app

print("Current working directory", os.getcwd())

# Create an instance for the flask application
app=create_app()

if __name__=='__main__':
    app.run(debug=True)


