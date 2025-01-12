from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "post"  # 任意でデータベーステーブル名を指定可能
