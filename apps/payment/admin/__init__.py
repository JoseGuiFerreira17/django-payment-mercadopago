from django.contrib.admin import site
from apps.payment.admin.payment import PaymentAdmin
from apps.payment.admin.payment_method import PaymentMethodAdmin
from apps.payment.models.payment import Payment
from apps.payment.models.payment_method import PaymentMethod


site.register(Payment, PaymentAdmin)
site.register(PaymentMethod, PaymentMethodAdmin)
