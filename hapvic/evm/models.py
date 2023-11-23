from django.db import models

from hapvic.common.models import Common


class Chain(Common):
    chain_id = models.IntegerField(unique=True)
    chain_symbol = models.CharField(max_length=255, unique=True)
    chain_name = models.CharField(max_length=255)
    chain_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.chain_symbol}"


class Contract(Common):
    chain_id = models.ForeignKey(Chain, on_delete=models.SET_NULL, null=True, blank=True)
    contract_address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    contract_name = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(null=True, blank=True, max_length=255)
    compiler_version = models.CharField(max_length=50, null=True, blank=True)
    contract_type = models.CharField(max_length=50, null=True, blank=True)
    contract_abi = models.JSONField(null=True, blank=True)
    contract_code = models.TextField(null=True, blank=True)
    contract_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.chain_id} {self.contract_address} {self.contract_name}"


class RPCUrl(Common):
    chain_id = models.ForeignKey(Chain, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
