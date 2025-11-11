from ninja import Schema


class PostSchema(Schema):
    id: int
    title: str
    body: str