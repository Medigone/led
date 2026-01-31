def apply_custom_type_flags(doc, method):
	"""Forcer is_paid et update_stock selon custom_type."""
	if not getattr(doc, "custom_type", None):
		return

	if doc.custom_type in ("Bon Pour", "Ticket de Caisse"):
		doc.is_paid = 1
		doc.update_stock = 1
	else:
		doc.is_paid = 0
		doc.update_stock = 0
