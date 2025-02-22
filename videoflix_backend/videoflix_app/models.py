from django.db import models
from user.models import CustomUser
class Video(models.Model):

    CATEGORY_OPTIONS = (('documentary','documentary'),('action','action'),('horror','horror'),('drama','drama'),('romance','romance'))
    LANGUAGE_OPTIONS = (('french','french'),('english','english'),('german','german'))
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=150, blank=True,default="")
    category = models.CharField(choices=CATEGORY_OPTIONS,max_length=100,blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=1)
    is_favorite = models.BooleanField(default=False)
    language = models.CharField(max_length=150,choices=LANGUAGE_OPTIONS, blank=True, null=True)
    video_file = models.FileField(upload_to='videos',blank=True,null=True)
    duration=models.PositiveIntegerField(blank=True,null=True)


    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            "id":self.id,
            "title" :self.title,
            "description" :self.description,
            "author" :self.author,
            "category" :self.category,
            "uploaded_at" :self.uploaded_at,
            "updated_at" :self.updated_at,
            "uploaded_by" :self.created_by,
            "is_favorite" :self.is_favorite,
            "language" :self.language,
            "video_file" :self.video_file,
            "duration" :self.duration,
        }
