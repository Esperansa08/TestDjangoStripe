import stripe
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from dotenv import load_dotenv
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Item
from StripeApp.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

load_dotenv()

stripe.api_key = STRIPE_SECRET_KEY


def index(request):
    return render(request, "index.html")


@csrf_exempt
def buy_item(request, id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": "price_1Opq4zDCDH2ouR18HmWviwtW",
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success"))
        + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse("index")),
    )

    return JsonResponse(
        {"session_id": session.id, "stripe_public_key": STRIPE_PUBLIC_KEY}
    )


def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")


@api_view(["GET", "POST"])
def get_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {"item": item}
    return render(request, "product_page.html", context)
