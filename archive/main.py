from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

from .database import create_connection


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    is_published: bool = True
    rating: Optional[int] = None


conn, cursor = create_connection()
my_posts = [
    {"id": 1, "title": "Hello world", "content": "Bharat it is"},
    {"id": 2, "title": "Fav food", "content": "I love Paneer Butter Masala"},
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index
    return None


@app.get("/posts")
def fetch_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES
                    (%s, %s, %s) RETURNING *""",
        (post.title, post.content, post.is_published),
    )  # dont use f str-interpolition, that might results into sql injection

    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[-1]
    return {"post": post}


# {id} is path parameter
@app.get("/posts/{id}")
def get_post(id: int):  # to vaidate the id always be int, provide it as int
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    fetched_post = cursor.fetchone()

    print(fetched_post)
    # convert the id to integer since id is string here
    found_post = find_post(int(id))

    if not found_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f'post with id: {id} not found'}
    return {"post_details": found_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # find the index in the array that has required ID
    index: int | None = find_index_post(id)
    print(index)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index: int | None = find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"message": f"updated_post: {post_dict}"}
