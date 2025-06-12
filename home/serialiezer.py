from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    headline = serializers.CharField(max_length=255)
    text = serializers.CharField()
    image = serializers.URLField()
    pub_date = serializers.DateTimeField()
    url = serializers.URLField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['pub_date'] = instance['pub_date'].isoformat() if instance['pub_date'] else None
        return representation
class TopNewsSerializer(serializers.Serializer):
    headline = serializers.CharField(max_length=255)
    text = serializers.CharField()
    image = serializers.URLField()
    pub_date = serializers.DateTimeField()
    url = serializers.URLField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['pub_date'] = instance['pub_date'].isoformat() if instance['pub_date'] else None
        return representation
# class weatherSerializer(serializers.Serializer):
#     city = serializers.CharField(max_length=100)
#     temperature = serializers.FloatField()
#     description = serializers.CharField(max_length=255)  
#     icon = serializers.CharField(max_length=100)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['temperature'] = f"{instance['temperature']} °C"
#         return representation
    
class profileSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    picture = serializers.ImageField(required=False)
    city = serializers.CharField(max_length=100, required=False)
    date_of_search = serializers.ChoiceField(choices=[
        ('yesterday', 'yesterday'),
        ('last week', 'last week'),
        ('last month', 'last month')
    ], default='yesterday')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    
class userSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation