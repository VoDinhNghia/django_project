from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['created_at']
        def __unicode__(self):
            return self.title