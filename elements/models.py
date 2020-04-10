from django.db import models
from django.contrib.auth.models import User
from ceremonies.models import Ceremony
from django.utils.translation import gettext as _


class Column(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    color = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Board(models.Model):
    ceremony = models.ForeignKey(
        Ceremony,
        on_delete=models.CASCADE,
        related_name="board",
        verbose_name=_("ceremony")
        )
    intro_message = models.TextField(verbose_name=_("Intro message"), null=True, blank=True)
    conclusion_message = models.TextField(verbose_name=_("Conclusion message"), null=True, blank=True)
    style = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Style"))

    def __str__(self):
        return "Board of {0}".format(str(self.ceremony))


class BoardColumn(models.Model):
    board = models.ForeignKey(Board, related_name="items", on_delete=models.CASCADE)
    column = models.ForeignKey(Column, related_name="columns", on_delete=models.CASCADE)

    def __str__(self):
        return self.column.__str__()


class PostIt(models.Model):
    user = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name=_("Usuario"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update at"))
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    explanation = models.TextField(null=True, blank=True, verbose_name=_("Explanation"))
    column = models.ForeignKey(
        BoardColumn,
        null=True,
        related_name="posts",
        on_delete=models.SET_NULL,
        verbose_name=_("Column"))
    private = models.BooleanField(default=False, verbose_name=_("Private"))
    hidden = models.BooleanField(default=True)
    color = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        TITLE_LEN_SHOWED = 80
        text = "[{0}] {1}{2}".format(
            str(self.user),
            self.title[:TITLE_LEN_SHOWED],
            "..." if len(self.title) > TITLE_LEN_SHOWED else ""
            )
        return text
