from django.db import models
from django import db
from django.db import transaction as tr


class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True)
    credit = models.IntegerField(default=0)


class BaseOrder(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()

    class State(models.TextChoices):
        SUCCESSFUL = 'SUC'
        FAILED = 'FAI'

    state = models.CharField(
        max_length=10,
        choices=State.choices,
        default=State.FAILED
    )

    class Meta:
        abstract = True

    def update_credit(self):
        pass

    def seller_has_enough_credit(self):
        pass

    def record_transaction(self):
        pass

    def perform_order(self):
        try:
            with tr.atomic():
                if self.seller_has_enough_credit():
                    self.update_credit()
                    self.state = self.State.SUCCESSFUL
                    self.record_transaction()
        except db.DatabaseError:
            # this line of code exists because atomic only rolls back database transactions not the entire code
            self.state = self.State.FAILED

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.perform_order()
        super().save(*args, **kwargs)


class AccountRechargeOrder(BaseOrder):

    class Action(models.TextChoices):
        INCREASE_CREDIT = 'INC'
        DECREASE_CREDIT = 'DEC'

    action = models.CharField(
        max_length=10,
        choices=Action.choices,
        default=Action.INCREASE_CREDIT
    )

    def seller_has_enough_credit(self):
        if self.action == self.Action.DECREASE_CREDIT and self.seller.credit < self.amount:
            return False
        else:
            return True

    def update_credit(self):
        if self.action == self.Action.INCREASE_CREDIT:
            self.seller.credit += self.amount
        elif self.action == self.Action.DECREASE_CREDIT:
            self.seller.credit -= self.amount
        self.seller.save()

    def record_transaction(self):
        directed_amount = self.amount if self.action == self.Action.INCREASE_CREDIT else -1 * self.amount
        print(directed_amount)
        Transaction(
            seller=self.seller,
            directed_amount=directed_amount
        ).save()


class SaleOrder(BaseOrder):
    phone_number = models.CharField(max_length=15)

    def update_credit(self):
        self.seller.credit -= self.amount
        self.seller.save()

    def seller_has_enough_credit(self):
        if self.seller.credit >= self.amount:
            return True
        else:
            return False

    def record_transaction(self):
        Transaction(
            seller=self.seller,
            directed_amount= -1 * self.amount
        ).save()


class Transaction(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, related_name='transactions')
    directed_amount = models.IntegerField()  # can be positive or negative














