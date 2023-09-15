from import_export import fields,resources
from .models import Positions, Prices, Comment, Infos, Food_Type

class PositionDetail(resources.ModelResource):

    class Meta:
        model = Positions
        fields =  ('Name', 'Area', 'Road', 'Door_num', 'Floor')

class PriceDetail(resources.ModelResource):
   
    class Meta:
        model = Prices
        fields =  ('Name', 'Service_charge', 'min_charge', 'Avg_charge')

class CommentDetail(resources.ModelResource):
   
    class Meta:
        model = Comment
        fields =  ('Name', 'CP', 'Service', 'Delicious_level', 'Clean')

class InfoDetail(resources.ModelResource):
   
    class Meta:
        model = Infos
        fields =  ('Name', 'START_Time', 'Close_Time', 'Menu', 'FB', 'Phone')

class FoodDetail(resources.ModelResource):
   
    class Meta:
        model = Food_Type
        fields =  ('Name', 'Type', 'Style', 'Veg')