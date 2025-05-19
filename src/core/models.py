from django.db import models


class BaseModel(models.Model):
    """
    Абстрактная модель.
    Добавляет к моделям дату создания и последнего изменения.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """
    Абстрактная модель для добавления поля title к моделям
    """

    title = models.CharField(max_length=128)

    class Meta:
        abstract = True


class OriginalTitle(TitleModel):
    pass


class ProductType(TitleModel):
    pass


class Director(models.Model):
    full_name = models.CharField(max_length=128)


class VideoProduct(BaseModel, TitleModel):
    original_title = models.OneToOneField(
        OriginalTitle, on_delete=models.CASCADE
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
    )
    directors = models.ManyToManyField(Director)
