from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Author, Book, Category, Order, OrderItem, PublishingCompany


class CategorySerializer(ModelSerializer):
    """Serializer class that serializes data from the Category model."""

    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    """Serializer class that serializes data from the Author: Firstname Lastname."""

    class Meta:
        model = Author
        fields = "__all__"


class PublishingCompanySerializer(ModelSerializer):
    """Serializer class that serializes data from the PublishingCompany model."""

    class Meta:
        model = PublishingCompany
        fields = "__all__"


class BookSerializer(ModelSerializer):
    """Serializer class that serializes data from the Book model."""

    category = SerializerMethodField()
    authors = SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

    def get_category(self, obj):
        """Get the category of an object.

        Returns:
            str: The description of the category.
        """
        return obj.category.description

    def get_authors(self, obj):
        authors = obj.authors.all()
        return [author.name for author in authors]


class OrderItemSerializer(ModelSerializer):
    """Serializer class that serializes data from the OrderItem model."""

    sub_total = SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("id", "book", "quantity", "sub_total")
        depth = 1

    def get_sub_total(self, obj):
        """Get the sub-total of an object."""
        return obj.book.price * obj.quantity


class OrderSerializer(ModelSerializer):
    """Serializer class that serializes data from the Order model."""

    client = SerializerMethodField()
    status = SerializerMethodField()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "total", "client", "status", "items")

    def get_client(self, obj):
        """Get the user of an object."""
        return obj.client.name

    def get_status(self, obj):
        """Get the status of an object."""
        return obj.get_status_display()


class OrderItemCreateSerializer(ModelSerializer):
    """Serializer class that serializes data from the OrderItem model."""

    class Meta:
        model = OrderItem
        fields = ("book", "quantity")


class OrderCreateSerializer(ModelSerializer):
    """Serializer class that serializes data from the OrderItem model."""

    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "client", "items")

    def create(self, validated_data):
        items = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        order.save()
        return order

    def update(self, instance, validated_data):
        """Update an instance of the model."""
        items = validated_data.pop("items")
        if items:
            instance.items.all().delete()
        for item in items:
            OrderItem.objects.create(order=instance, **item)
        return instance
