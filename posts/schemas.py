from ninja import Schema


class PostSchema(Schema):
    id: int
    title: str
    body: str
    img_url: str | None