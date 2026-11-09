# This was created by hand following the tutorial at https://blog.postman.com/how-to-build-an-api-in-python/
# The creator of that tutorial was nice enough to not say how to start the server. GFG had the answer here: https://www.geeksforgeeks.org/python/fastapi-uvicorn/
#
# Start the server (in this dir):
# uvicorn main:app --host 0.0.0.0 --port 1337
#
# Other citations:
# https://www.geeksforgeeks.org/python/python-async/ - explained async!
# https://stackoverflow.com/questions/66622020/fastapi-detailmethod-not-allowed - this helped me figure out why the requests were failing. A browser only does GET but other methods are required.


# imports
from fastapi import FastAPI

# setup
app = FastAPI() # an instance of the FastAPI class is created and assigned to var app. This handles and routes requests. Now we can use app.xyz insteal of FastAPI.xyz later.
static_str = "Default string"

# DELETEs
@app.delete("/remove") # endpoint for emptying the saved string
async def rm_text():
	global static_str
	static_str = ""
	return {"Message": "Text removed"} # tell the user the text was removed


# GETs
@app.get("/get-greeting") # this is a new function that demonstrates passing a parameter
async def greeting(name: str): # read the query string for somebody's name
        return {"Message": "Hi " + name + "! Your API is working!"} # this returns the variable sent in the query string

@app.get("/get-message") # this creates the /get-message endpoint for GET requests at that URL.
async def read_root(): # this function is aynchronous, meaning that it will not stop the rest of the code when called. This is good for many HTTP requests, each one won't freeze everything up until completeion. https://www.geeksforgeeks.org/python/python-async/
	return {"Message": "Hello world! This is my first API!"} # This is the data sent back when requested.

@app.get("/get-string") # I created this endpoint on my own, to just see whatever is in the "static_str" variable. We have the editing, but what if I don't want to change it?
async def read_str():
	global static_str
	return {"Message":"Static_str is currently: " + static_str}

# POSTs
@app.post("/add") # endpoint for adding text to the text var
async def add_text(text: str):
	global static_str
	static_str += text
	return {"Message": "Text added", "current_str": static_str} # send back saved string


# PUTs
@app.put("/change") # endpoint to erase the saved string and replace it with something else.
async def change_text(new_text: str):
	global static_str
	static_str = new_text
	return {"message": "Text changed to: ", "current_str": static_str}
