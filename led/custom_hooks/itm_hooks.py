# Copyright (c) 2025, IntraPro and contributors
# For license information, please see license.txt

import frappe
from erpnext.stock.doctype.item.item import Item


class CustomItem(Item):
	def autoname(self):
		from frappe.model.naming import make_autoname
		self.name = make_autoname("ART-.#####")
