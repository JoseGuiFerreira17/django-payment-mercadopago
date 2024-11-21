from django.contrib.admin import site
from apps.plans.models.plan import Plan
from apps.plans.models.subscription import Subscription
from apps.plans.admin.subscription import SubscriptionAdmin
from apps.plans.admin.plan import PlanAdmin


site.register(Plan, PlanAdmin)
site.register(Subscription, SubscriptionAdmin)
