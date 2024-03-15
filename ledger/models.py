from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default = 'user')
    createdOn = models.DateTimeField(auto_now_add = True)
    updatedOn = models.DateTimeField(auto_now = False)
    
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredientField = models.ForeignKey('Ingredient',
        on_delete = models.CASCADE,
        default = 1,
        related_name = 'recipe'
    )
    recipeField = models.ForeignKey('Recipe',
        on_delete = models.CASCADE,
        default = 1,
        related_name = 'ingredients'
    )

    def __str__(self):
        return f'{self.recipeField.name}: {self.ingredientField.name}, {self.quantity}'

    class Meta:
        ordering = ['ingredientField']
        unique_together = [ 
            ['quantity', 'ingredientField'],
        ]