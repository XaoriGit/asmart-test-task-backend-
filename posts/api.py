from faker import Faker
from ninja import Router, Query
from ninja_jwt.authentication import JWTAuth

from posts.schemas import PostSchema

router = Router()
fake = Faker()


@router.get('/', auth=JWTAuth(), response=PostSchema)
def get_posts(request, page: int = Query(1, ge=1), page_size: int = Query(25, le=100)):
    start = (page - 1) * page_size
    end = start + page_size
    posts = [PostSchema(id=i, title=fake.sentence(), body=fake.paragraph()) for i in range(start, end)]
    return posts
