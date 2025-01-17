from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/search/{song_name}")
def search_song(song_name: str):
    return {"search": f"You searched for {song_name}"}
