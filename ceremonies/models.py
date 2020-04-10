from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Ceremony(models.Model):
    CHOICES_TYPE = (('RETRO', _('Retro Meeting')),)
    DEFAULT_TYPE = 'RETRO'
    create_at = models.DateField(auto_now_add=True, verbose_name=_("Create at"))
    schedule = models.DateTimeField(verbose_name=_("Schedule"))
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    event_type = models.CharField(
        max_length=20,
        choices=CHOICES_TYPE,
        default=DEFAULT_TYPE,
        verbose_name=_("event type")
    )
    achieved = models.BooleanField(default=False, verbose_name=_("Completed"))

    def __str__(self):
        text = "{0} {1}{2}".format(
            self.title,
            self.get_event_type_display(),
            _("Closed") if self.achieved else ""
        )
        return text

    class Meta:
        verbose_name_plural = _("Ceremonies")
