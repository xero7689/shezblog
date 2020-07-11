import datetime
from django.test import TestCase
from .models import Article

# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        Article.object.create(
            title='UnitTest Article',
            abstract='UnitTest Abstract',
            content='<strong>UnitTest Content</strong>',
            create_date = datetime.datetime.now(),
            modify_date = datetime.datetime.now(),
            visible = True
        )

    def test_is_valid_titile(self):
        article = Article.objects.get(title='UnitTest Article')
        self.assertEqual(article.title, 'UnitTest Article')
