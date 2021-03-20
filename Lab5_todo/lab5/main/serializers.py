from rest_framework import serializers
from .models import TodoList, Todo


class TodoListSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        todoList = TodoList.objects.create(name=validated_data.get('name'))
        return todoList

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TodoListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TodoSerializer(serializers.Serializer):
    name = serializers.CharField()
    created_date = serializers.DateTimeField()
    due_on_date = serializers.DateTimeField()
    owner = serializers.CharField()
    list_id = serializers.IntegerField()
    category = serializers.CharField()

    def create(self, validated_data):
        todo = Todo.objects.create(name=validated_data.get('name'), created_date=validated_data.get('created_date'),
                                   due_on_date=validated_data.get('due_on_date'), owner=validated_data.get('owner'),
                                   list_id=validated_data.get('list_id'), category=validated_data.get('category'))
        return todo

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.due_on_date = validated_data.get('due_on_date', instance.due_on_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.list_id = validated_data.get('list_id', instance.list_id)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'created_date', 'due_on_date', 'owner', 'list_id', 'category')