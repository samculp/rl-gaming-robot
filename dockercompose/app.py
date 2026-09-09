# pyright: reportMissingImports=false

import os
#Connects Python to the Redis Server to store the "hit" counter.
import redis
#allows the creation of web application.
from flask import Flask

#Creates new Flask application.
app = Flask(__name__)
#Creates a new Redis client and stores the "cache" variable.
cache = redis.Redis(
    #Finds the enviroment variable called "REDIS_HOST" from our OS and uses the value.
    host=os.getenv("REDIS_HOST", "redis"),
    #Similar to the above line, it looks for the port labeled "REDIS_PORT" and uses its value.
    port=int(os.getenv("REDIS_PORT", "6379")),
    #Both lines of code above have backup values to use if "REDIS" can not be found.
)

#Executes the following code when anyone visits the page created.
@app.route("/")
#Pythong function named "hello" that will increase a counter by 1 everytime the page is visited.
def hello():
    count = cache.incr("hits")
    return f"Hello from Docker! I have been seen {count} time(s).\n"