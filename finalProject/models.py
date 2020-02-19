from django.db import models

# Create your models here.

# class Recom(models.Model):
#       category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
#       author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='documents')
# # on_delete=models.SET_NULL : 참조하고 있는 Category 객체가 지워져도 삭제되지 않음
#       title = models.CharField(max_length=100)
# # db_index=True : DB에 인덱싱 가능
#       slug = models.SlugField(max_length=120, db_index=True, unique= True, allow_unicode=True, blank=True)
#       text = models.TextField()
#       image = models.ImageField(upload_to='board_images/%Y/%m/%d')
#       created = models.DateTimeField(auto_now_add=True)
#       updated = models.DateTimeField(auto_now=True)
#
# def __str__(self):
#     return self.title
#
# def save(self, *args, **kwargs):
#     self.slug = slugify(self.title, allow_unicode=True)
#     super(Recom, self).save(*args, **kwargs)
#
# def get_absolute_url(self):
#     return reverse('board:detail', args=[self.id])