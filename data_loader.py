from storage.models import Category, Storage, Currency, TaxRate, Item, ItemsBucket, Country, Client, DocumentType
from decimal import *

#Populates database with initial data
def load():
	#adding new category
	cat1 = Category(name = 'Opony')
	cat1.save()

	#adding new storage
	stor1 = Storage(name = 'Magazyn 1')
	stor2 = Storage(name = 'Magazyn 2')
	stor3 = Storage(name = 'Magazyn 3')
	stor1.save()
	stor2.save()
	stor3.save()

	#adding new currency
	cur1 = Currency(name = 'PLN')
	cur1.save()

	#adding new price
	# pr1 = Price(amount = Decimal(100.0000), currency = cur1)
	# pr1.save()
	# pr2 = Price(amount = Decimal(120.0000), currency = cur1)
	# pr2.save()

	#adding new tax rate
	tx = TaxRate(percentage = 12)
	tx.save()

	#adding new item
	it1 = Item(name = 'Opony 165/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it1.save()
	it2 = Item(name = 'Opony 175/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it2.save()
	it3 = Item(name = 'Opony 185/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it3.save()
	it4 = Item(name = 'Opony 195/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it4.save()
	it5 = Item(name = 'Opony 205/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it5.save()
	it6 = Item(name = 'Opony 215/65R15', description = 'Opony...', category = cat1, tax_rate = tx)
	it6.save()

	#adding new items bucket
	ib1 = ItemsBucket(item = it1, count = 10, buy_price = Decimal(100.0000), sell_price = Decimal(120.0000), storage = stor1)
	ib1.save()
	ib2 = ItemsBucket(item = it2, count = 10, buy_price = Decimal(100.0000), sell_price = Decimal(120.0000), storage = stor1)
	ib2.save()
	ib3 = ItemsBucket(item = it3, count = 10, buy_price = Decimal(100.0000), sell_price = Decimal(120.0000), storage = stor1)
	ib3.save()
	ib4 = ItemsBucket(item = it4, count = 10, buy_price = Decimal(100.0000), sell_price = Decimal(120.0000), storage = stor1)
	ib4.save()
	
	#adding new country
	pl = Country(name = 'Polska')
	pl.save()

	#adding new clients
	cl1 = Client(name = 'ACMA', address = 'ul. Krakowska 1/2', zip_code = '30100', country = pl)
	cl1.save()
	cl2 = Client(name = 'ACMA 2', address = 'ul. Wadowicka 1/2', zip_code = '30100', country = pl)
	cl2.save()
	cl3 = Client(name = 'ACMA 3', address = 'ul. Zakopianska 8', zip_code = '30100', country = pl)
	cl3.save()

	#adding doc types
	# dt1 = DocumentType(name = 'invoice')
	# dt1.save()
	dt2 = DocumentType(name = 'mmplus')
	dt2.save()
	dt3 = DocumentType(name = 'mmminus')
	dt3.save()
	# dt4 = DocumentType(name = 'pz')
	# dt4.save()
	# dt5 = DocumentType(name = 'wz')
	# dt5.save()

load()