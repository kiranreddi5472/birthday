from django.db import models

class Wish(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the person making the wish")
    message = models.TextField(help_text="Heartfelt birthday message")
    image = models.ImageField(upload_to='wishes/', blank=True, null=True, help_text="Optional polaroid picture")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Wish from {self.name} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Gallery(models.Model):
    title = models.CharField(max_length=200, help_text="Short description of this memory")
    image = models.ImageField(upload_to='gallery/', help_text="High resolution gallery photo")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Gallery Memories"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class Dialogue(models.Model):
    text = models.TextField(help_text="Famous dialogue, catchphrase, or quote")
    added_by = models.CharField(max_length=100, blank=True, null=True, help_text="Student name who added this (optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        author = self.added_by if self.added_by else "Anonymous"
        return f'"{self.text[:50]}..." - added by {author}'
