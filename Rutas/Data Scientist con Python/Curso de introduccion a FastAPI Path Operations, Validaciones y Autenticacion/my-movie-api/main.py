from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()
app.title = "My app with FastAPI"
# app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_lenght=5, max_lenght=15)
    overview: str = Field(min_lenght=15, max_lenght=50)
    year: int = Field(ge=1900, le=2023)
    rating: float = Field(ge=0, le = 10)
    category: str = Field(min_lenght=5, max_lenght=50)

    class Config():
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula", 
                "overview": "Overview (description)",
                "year": 2023,
                "rating": 5.0,
                "category": "Action"
            }
        }

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un planeta llamado pandora existe una raza llamada los navi...",
        "rating": 7.8,
        "category": "Science Fiction"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un planeta llamado pandora existe una raza llamada los navi...",
        "rating": 7.8,
        "category": "Science Fiction"
    }
]

@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello dear </h1>')


@app.get('/movies', tags = ['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags = ['movies'])
def get_movies(id: int):
    for m in movies:
        if(m["id"] == id):
            return m
        else:
            return "Doesnt exist that movie"
        
@app.get('/movies/', tags = ['movies'])
def get_movies_by_category(category: str, year: int):
    return [m for m in movies if m["category"] == category]

@app.post('/movies', tags = ['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return "Se agrego la movie correctly"

@app.put('/movies/{id}', tags = ['movies'])
def update_movie(id: int, movie: Movie):
    for m in movies:
        if(m['id'] == id):
            m['title'] = movie.title
            m['overview'] = movie.overview
            m['year'] = movie.year
            m['rating'] = movie.rating
            m['category'] = movie.category
            return movies

@app.delete('/movies/{id}', tags = ['movies'])
def delete_movie(id: int):
    for m in movies:
        if(m['id'] == id):
            movies.remove(m)
            return movies
