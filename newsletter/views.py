import stripe
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "newsletter/about.html", {})

def payment(request):
    stripe.api_key = "sk_test_a53eN187P0pYwmu8SXPV6QSZ"

    # Get the credit card details submitted by the form
    token = request.POST.get('stripeToken')

    if token:
        # Create a charge: this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=1000, # Amount in cents
              currency="usd",
              source=token,
              description="Example charge"
          )
        except stripe.error.CardError as e:
          # The card has been declined
          pass
    print("sdfsfd")
    return render(request, "newsletter/contact.html", {})