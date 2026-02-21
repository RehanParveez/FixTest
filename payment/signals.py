from django.db.models.signals import post_save
from django.dispatch import receiver
from payment.models import Payment

@receiver(post_save, sender=Payment)
def claim_status(sender, instance, created, **kwargs):
    if created:
        claim = instance.claim
        claim.status = 'approved'
        claim.save()