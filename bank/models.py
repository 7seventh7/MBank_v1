from django.db import models
from django.contrib.auth.models import User
from django.db import transaction  #здесь функция atomic() для работы с транзакциями

class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Account(models.Model):
    balance = models.IntegerField(
        default=1_000_000
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT  # we cannot delete user with money
    )

    def __str__(self):
        return f'{self.id} of {self.user.username}'

class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    merchant = models.CharField(max_length=255)

    def __str__(self):
        return f'Account number {self.account.id} ' +\
            f'sent {str(self.amount)} to {self.merchant}'

    @classmethod
    def make_transaction(cls, amount, account, merchant):
        if account.balance < amount:
            raise(ValueError('Not enough money'))

        with transaction.atomic():
            account.balance -= amount
            account.save()
            tran = cls.objects.create(
                amount=amount, account=account, merchant=merchant)

        return account, tran


class Transfer(models.Model):

    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account'
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )

    amount = models.IntegerField(

    )

    date = models.DateTimeField(auto_now_add=True)
