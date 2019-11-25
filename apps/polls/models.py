from django.db import models

ANSWER_CHOICES = (
    ("yes", "yes"),
    ("no", "no"),
    ("often", "often"),
    ("not often", "not often"),
)


class Polls(models.Model):
    question = models.CharField("question", blank=False, max_length=255)
    answers = models.CharField("answers", blank=False, max_length=60, choices=ANSWER_CHOICES)

    def __str__(self):
        return "%s %s" % (self.question, self.answers)
