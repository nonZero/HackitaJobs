from ads.models import Tag, Ad
from django.test import TestCase


class AdsTest(TestCase):

    def test_create_ads(self):

        tag1 = Tag.objects.create(name="HTML 5", slug="html5")
        tag2 = Tag.objects.create(name="jQuery", slug="jquery")
        tag3 = Tag.objects.create(name="Python", slug="python")

        self.assertEquals(0, Ad.objects.count())

        ad1 = Ad()
        ad1.company_name = "ACME International"
        ad1.company_url = "http://acme.com/"
        ad1.title = "Ninja Top Developer"
        ad1.description = """
        We are growing, we need more developers.
        Apply if you are cool and sexy.
        """
        ad1.apply_email = "jobs@acme.com"

        ad1.full_clean()
        ad1.save()

        self.assertEquals(1, Ad.objects.count())

        ad1.tags.add(tag1)

        self.assertEquals(1, tag1.ads.count())

        tag2.ads.add(ad1)

        self.assertEquals(2, ad1.tags.count())

        self.assertEquals(0, tag3.ads.count())
