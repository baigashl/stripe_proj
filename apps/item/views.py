from django.http import HttpResponse
from django.shortcuts import render

import stripe
from django.template import loader
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
import os

stripe.api_key = 'sk_test_51Lg6uJACJ0hmrHGCnJMIMus6yTosn76emhHVTrINrAnPJpljDjBTVf02dO0ehmNcMbkgYp4F6vOQLjugUuuOSskF00Ts9ew9r1'


class GetItemListAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    snippet = Item.objects.all()
    serializer = ItemSerializer(snippet, many=True)
    return Response(serializer.data)


# class GetItemSessionAPIView(APIView):
#   permission_classes = [permissions.AllowAny]
#
#   def get(self, request, id):
#     try:
#       item = Item.objects.get(id=id)
#       product = stripe.Product.create(name=item.name)
#       price = stripe.Price.create(
#         unit_amount=item.price,
#         currency="usd",
#         recurring={"interval": "month"},
#         product=product.id,
#       )
#       res = stripe.checkout.Session.create(
#         success_url="https://example.com/success",
#         cancel_url="https://example.com/cancel",
#         line_items=[
#           {
#             "price": price.id,
#             "quantity": 1,
#           },
#         ],
#         mode="subscription",
#       )
#       print(res)
#     except Exception as e:
#       return str(e)
#
#     return Response({"session_id": res.id}, status=status.HTTP_200_OK)



class GetItemSessionAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request, id):
    try:
      item = Item.objects.get(id=id)
      session = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': item.name,
            },
            'unit_amount': item.price,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
      )
      print(session)
    except Exception as e:
      return str(e)

    return Response({"session_id": session.id}, status=status.HTTP_200_OK)


def index(request, id):
  item = Item.objects.get(id=id)
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': item.name,
        },
        'unit_amount': item.price,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:8000/success',
    cancel_url='http://localhost:8000/cancel',
  )
  template = loader.get_template('checkout.js')
  return HttpResponse(template.render())

