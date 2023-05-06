from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Min, Max
from django.db.models.functions import Concat
from django.db.models import DecimalField

from Playground.models import Product, OrderItem, CartItem, Order, Collection, Customer

from bson import Decimal128 as Decimal

# Create your views here.


def Hello(request):

    result = Product.objects.annotate(
        discount=ExpressionWrapper(
            F('unit_price') ** 3, output_field=DecimalField())

    )
    print(result)

    # result = Customer.objects.annotate(
    #     orders_total=Count('order')

    # )

    # query_product = Product.objects.filter(id__range=(5, 50))

    # in prefetch im using orderitem_set because in order class we have not built relationship woth orderitem by default jgango offer this
    # query_product = Order.objects.select_related(
    #    'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # select_relacted only fetch table with 1 coloum
    # prefetch related fetch all items
    # query_product = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()
    # print(type(query_product[0].unit_price))

    # query_product = Product.objects.filter(id__in=(OrderItem.objects.values(
    #     'product__id').distinct()))

    # GETTING SOME COLOUMS NOT ALL
    # query_product = Product.objects.values_list(
    #    'id', 'title', 'collection__title')

    # query_product = Product.objects.filter(unit_price__lt=30)

    # Order By string
    # query_product = Product.objects.order_by('-title', 'unit_price').reverse()

    # Query for comapring database coloums
    # query_product = Product.objects.filter(description=F('description'))

    # Query for OR implementation using Q
    # query_product = Product.objects.filter(Q(
    #     title__icontains="beef") | Q(description__icontains="maecenas"))

    return render(request, 'hello.html', {'name': 'worlds', 'Result': result})

    # return render(request, 'hello.html', {'name': 'worlds', 'products': list(query_product)})


def Sigin(requset):
    return HttpResponse('<h1>Sign In</h1>')
