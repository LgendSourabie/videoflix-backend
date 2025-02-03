import factory
import factory.fuzzy
from user.models import CustomUser
from videoflix_app.models import Video
from datetime import datetime


class UserDataFactory(factory.Factory):

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"user{n}@videoflix.com")
    # username = factory.Faker("first_name")
    # email = factory.Faker("email")
    custom = factory.Faker("text", max_nb_chars=500)
    phone = factory.Faker("phone_number")
    address = factory.Faker("address")
    password = factory.PostGenerationMethodCall('set_password', 'FakePassword123!*')

    class Meta:
        model = CustomUser

class UserFactory(factory.django.DjangoModelFactory):

    username = factory.Faker("first_name")
    email = factory.Faker("email")
    custom = factory.Faker("text", max_nb_chars=500)
    phone = factory.Faker("phone_number")
    address = factory.Faker("address")
    password = factory.PostGenerationMethodCall('set_password', 'FakePassword123!*')

    class Meta:
        model = CustomUser



class VideoFactory(factory.django.DjangoModelFactory):

    title = factory.Faker("text", max_nb_chars=100)
    description = factory.Faker("text", max_nb_chars=1000)
    category = factory.fuzzy.FuzzyChoice(choices=["documentary","action","horror"])
    uploaded_at = factory.LazyFunction(datetime.utcnow)
    updated_at = factory.LazyAttribute(lambda obj: obj.uploaded_at)
    created_by = factory.SubFactory(UserFactory, id=1)  
    is_favorite = factory.fuzzy.FuzzyChoice(choices=[True,False])
    language = factory.fuzzy.FuzzyChoice(choices=["french","english","german"])
    video_file = factory.Faker("file_path",depth=4,category='video',extension="mp4")


    class Meta:
        model = Video