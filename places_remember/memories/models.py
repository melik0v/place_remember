from django.db import models
from users.models import CustomUser


class Memory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default=None)
    user_id = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, blank=True, null=True, default=None)
    created = models.DateField(auto_now_add=True, auto_now=False)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Memory"
        verbose_name_plural = "Memories"


class Image(models.Model):
    memory = models.ForeignKey(
        Memory, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    image = models.ImageField(
        default="static/media/placeholder.png",
        upload_to="static/media/test_user"
        # upload_to="static/media/test_user"
    )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "Photo from {0}".format(self.memory)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
