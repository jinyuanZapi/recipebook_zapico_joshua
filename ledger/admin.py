from django.contrib import admin

from .models import Recipe, RecipeIngredient

class Inline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [Inline,]

class RecipeIngredientAdmin (admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ['ingredientField', 'quantity', 'recipeField']
    search_fields = ['ingredientField', 'quantity', 'recipeField']
    list_filter = ['recipeField']

    fieldsets = [('Details', {'fields' : ['ingredientField', 'quantity', 'recipeField']})]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)