from django.db import models


class Card(models.Model):
    serial_number = models.IntegerField('Serial Number',)
    card_number = models.BigIntegerField('Card Number')
    release_date = models.DateTimeField('Release Date', auto_now_add=True)
    end_date = models.DateTimeField('Expire Date')
    cvv = models.IntegerField('CVV')
    money_on_card = models.FloatField('Amount of Money')
    card_status = models.CharField('Card Status', default="activated", max_length=25)

    # def __str__(self):
    #     return "<Card Info(serial_number='%s' card_number='%s', release_date='%s', end_date='%s', cvv='%s'," \
    #            "money_on_card='%s', card_status='%s')>" \
    #            % (self.serial_number, self.card_number, self.release_date, self.end_date, self.cvv,
    #               self.money_on_card, self.card_status)
