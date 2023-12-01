import os
from django.shortcuts import render, get_object_or_404, redirect
import stripe
from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotenv import load_dotenv

from .models import Item
load_dotenv()

stripe.api_key = os.getenv('stripe_api_key', default='stripe_api_key')


@api_view(['GET'])
def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1, currency='pln',
        payment_method_types=['card'],
        receipt_email='test@example.com')
    return Response(status=HTTPStatus.OK, data=test_payment_intent.id)


@api_view(['GET', 'POST'])
def get_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {'item': item}
    # if request.method == 'POST':
    #     session_id = buy_item(request, id)
    #     return stripe.redirectToCheckout(sessionId=session_id)
    if request.method == 'POST':
        session_id = buy_item(request, id)
        context = {'item': item,
                   'session_id': session_id}
        return redirect('index.html', context)
    return render(request, 'index.html', context)
    #return redirect('items:buy', id)


@api_view(['POST'])
def confirm_payment_intent(request):
    data = request.data
    payment_intent_id = data['payment_intent_id']
    stripe.PaymentIntent.confirm(payment_intent_id)
    return Response(status=HTTPStatus.OK, data={"message": "Success"})