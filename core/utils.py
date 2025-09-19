import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from.models import Course, Enrollment
from django.contrib.auth import get_user_model

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(View):
    def post(self, request, ):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            course_id = session.get('metadata', {}).get('course_id')
            user_id = session.get('metadata', {}).get('user_id')
            
            if user_id and course_id:
                user = User.objects.get(id=user_id)
                course = Course.objects.get(id=course_id)

                if not Enrollment.objects.filter(student=user, course=course).exists():
                    Enrollment.objects.create(student=user, course=course)


        return HttpResponse(status=200)