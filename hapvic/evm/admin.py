from django.contrib import admin

from .models import Chain, Contract, RPCUrl


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ("chain_id", "chain_symbol", "chain_name", "chain_description")
    search_fields = ("chain_symbol", "chain_name")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("chain_id", "contract_address", "contract_name", "active", "creation_date", "creator")
    list_filter = ("chain_id", "active")
    search_fields = ("chain_id__chain_symbol", "contract_address", "contract_name", "creator")
    readonly_fields = ("creation_date",)  # If you want to make creation_date read-only


# @admin.register(RPCUrl)
# class RPCUrlAdmin(admin.ModelAdmin):
#     list_display = ("chain_id", "url", "active")
#     list_filter = ("chain_id", "active")
#     search_fields = ("chain_id__chain_symbol", "url")
