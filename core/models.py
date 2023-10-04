from django.db import models


class Category(models.Model):
    """Category model."""

    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"#{self.id} - {self.description}"


class PublishingCompany(models.Model):
    """Publishing company model."""

    name = models.CharField(max_length=100)
    site = models.URLField()

    def __str__(self) -> str:
        return f"#{self.id} - {self.name}"


class Author(models.Model):
    """Author model."""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"#{self.id} - {self.name}"


class Book(models.Model):
    """Book model."""

    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="books"
    )
    publishing_company = models.ForeignKey(
        PublishingCompany, on_delete=models.PROTECT, related_name="books"
    )
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self) -> str:
        return f"#{self.id} - {self.title}"


class Client(models.Model):
    """Client model."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"#{self.id} - {self.name}"


class Order(models.Model):
    """Order model."""

    class Status(models.IntegerChoices):
        """Order status."""

        CART = 0, "Cart"
        REALIZED = 1, "Realized"
        PAY = 2, "Pay"
        DELIVERED = 3, "Delivered"
        CANCELLED = 4, "Cancelled"

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="orders")
    status = models.IntegerField(choices=Status.choices, default=Status.CART)

    @property
    def total(self):
        """Get the total of an object."""
        query = self.items.all()
        aggregate = query.aggregate(
            total=models.Sum(models.F("book__price") * models.F("quantity"))
        )
        return aggregate["total"]

    def __str__(self) -> str:
        return f"#{self.id} - {self.client.name}"


class OrderItem(models.Model):
    """Order item model."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="+")
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.book)
