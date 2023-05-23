from django.db import models


class TerminalPath(models.Model):
    string = models.CharField(max_length=256)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.string
