# Copyright (c) 2025, IntraPro and contributors
# For license information, please see license.txt

import frappe
from erpnext.stock.doctype.item.item import Item


class CustomItem(Item):
	def autoname(self):
		from frappe.model.naming import make_autoname
		self.name = make_autoname("ART-.#####")


def uppercase_item_name(doc, method):
	# Convertir le nom de l'article en majuscules s'il existe
	if doc.item_name:
		doc.item_name = doc.item_name.upper()
