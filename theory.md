## Postgres docker commands

```
docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 -p 5432:5432 -v /data:/var/lib/postgresql/data --name postgresql postgres
```

`database` -> `postgres`

### Important timestamps

Why we need Schema:

- [check out here](https://youtu.be/0sOvCWFmrtA?t=4068) - use of pydantic

## psycopg2

```
brew install postgresql
sudo pip install psycopg2
```
In venv:

```
env LDFLAGS='-L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/readline/lib' pip install psycopg2==2.8.4
```

## table:

```SQL
CREATE TABLE IF NOT EXISTS posts (
   id SERIAL primary key,
   title varchar(50) NOT NULL,
   content varchar(255) NOT NULL,
   published bool default true,
   created_at TIMESTAMP default now()
);

-- Inserting a single post
INSERT INTO posts (title, content) VALUES ('First Post', 'This is the content of the first post.');

-- Inserting multiple posts in a single statement
INSERT INTO posts (title, content, published) VALUES 
('Second Post', 'Content of the second post.', true),
('Third Post', 'Here is some more content in another post.', false);

-- Inserting a post with a specific published status
INSERT INTO posts (title, content, published) VALUES ('Fourth Post', 'This is another post, which is unpublished.', false);

-- Inserting a post with a specified creation time
INSERT INTO posts (title, content, published) VALUES 
('Fifth Post', 'Content for the fifth post', true);

select * from posts p ;
```

### gunicorn
`gunicorn main:app --workers 4 --worker-class`

## alembic

`alembic init <directory>`

❯ alembic revision --m "create post table"
