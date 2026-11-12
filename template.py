# This template was created from the main.py file, it is designed to be a quick API that you can copy and have up in minutes!
#
# Start the server (in this dir):
# uvicorn main:app --host 0.0.0.0 --port 1337
#
# Docs on this and the main project can be found on my website at: INSERT LINK



# imports
from fastapi import FastAPI

# setup
app = FastAPI() # use "app.method" for your endpoints
static_str = "Default string" # Some default endpoints interact with this variable as proof-of-function

# DELETEs
@app.delete("/remove") # empty the saved string
async def rm_text():
	global static_str
	static_str = ""
	return {"Message": "Text removed"} # tell the user the text was removed


# GETs
@app.get("/get-greeting") # greet the name var
async def greeting(name: str):
        return {"Message": "Hi " + name + "! Your API is working!"}

@app.get("/get-message") # most basic test, use /get-message to test connectivity.
async def read_root():
	return {"Message": "Hello world! This is my first API!"}

@app.get("/get-string") # return static_str, no modifications
async def read_str():
	global static_str
	return {"Message":"Static_str is currently: " + static_str}

# POSTs
@app.post("/add") # append text to static_str
async def add_text(text: str):
	global static_str
	static_str += text
	return {"Message": "Text added", "static_str": static_str} # send back full contents of static_str


# PUTs
@app.put("/change") # erase the saved string and replace it.
async def change_text(new_text: str):
	global static_str
	static_str = new_text
	return {"message": "Text changed to: ", "current_str": static_str}
