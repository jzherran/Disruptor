#!flask/bin/python

# Import app variable from our app package
from app import create_app

# Invokes the run method to start the server
# Don't forget the app variable holds the Flask instance

### DEVELOPMENT (Internal-facing, Debug on)
create_app(test_config=False).run(debug=True)

### PRODUCTION (External-facing, Debug off)
#app.run(debug=False, host='0.0.0.0')