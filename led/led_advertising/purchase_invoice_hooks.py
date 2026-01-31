import frappe


def apply_custom_type_flags(doc, method):
	"""Forcer is_paid et pre-remplir la caisse selon custom_type."""
	if not getattr(doc, "custom_type", None):
		return

	if doc.custom_type in ("Bon Pour", "Ticket de Caisse"):
		doc.is_paid = 1

		if doc.company and not doc.cash_bank_account:
			cash_account = frappe.get_cached_value(
				"Company", doc.company, "default_cash_account"
			)
			if not cash_account:
				cash_account = frappe.get_cached_value(
					"Company", doc.company, "default_bank_account"
				)
			if cash_account:
				doc.cash_bank_account = cash_account
	else:
		doc.is_paid = 0
