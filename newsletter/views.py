import stripe
from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, "newsletter/about.html", {})

def payment(request):
    stripe.api_key = "sk_test_a53eN187P0pYwmu8SXPV6QSZ"
    stripe.api_base = "https://api-tls12.stripe.com"

    # Get the credit card details submitted by the form
    token = request.GET.get('stripeToken')
    logger.debug(request.GET)
    logger.debug("token")
    logger.debug(token)
    if token:
        # Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency="usd",
                source=token,
                description="Example charge",
            )
            logger.debug("charge")
            logger.debug(charge)
        except stripe.error.CardError as e:
          # The card has been declined
          pass
    logger.debug("before render")
    return render(request, "newsletter/contact.html", {})