import random

from faker import Faker
from ninja import Router, Query
from ninja_jwt.authentication import JWTAuth

from posts.models import Image
from posts.schemas import PostSchema

router = Router()
fake = Faker()


@router.get('/', auth=JWTAuth(), response=list[PostSchema])
def get_posts(request, page: int = Query(1, ge=1), page_size: int = Query(25, le=100)):
    images = list(Image.objects.all())
    start = (page - 1) * page_size
    end = start + page_size
    posts = []
    for i in range(start, end):
        img = random.choice(images) if images else None
        posts.append(
            PostSchema(
                id=i,
                title=fake.sentence(),
                body=fake.paragraph(),
                img_url=request.build_absolute_uri(img.image.url) if img else None,
            )
        )
    return posts
