from django.db import models
# Create your models here.
class Post(models.Model): #建立類別
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #自動取得時間
    
    class Meta: 
        ordering = ('-pub_date',) #ordering 指定排序 -pub_date 排序方式
        
    def __str__(self):
        return self.title
    
