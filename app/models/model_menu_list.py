class Field:
    def __init__(self, name, field_type, **kwargs):
        self.name = name
        self.field_type = field_type
        self.kwargs = kwargs

    def get_value(self, instance):
        return getattr(instance, self.name)

   
class CharField(Field):
    pass

class IntegerField(Field):
    pass

class ListField(Field):
    def __init__(self, name, field_type):
        self.name = name
        self.field_type = field_type
        
    def get_value(self, instance):
        value = super().get_value(instance)
        if value is None:
            return []
        return value


class CharArrayField(ListField):
    pass

class Meal:
    id = IntegerField(name="id", field_type=int)
    name = CharField(name="name", field_type=str, max_length=200)
    ingredients = CharArrayField(name="ingredients", field_type=list)
    
    def __init__(self, id=None, name=None, ingredients=None):
        self.id = id
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return f"id={self.id}, name={self.name}, ingredients={self.ingredients}"
