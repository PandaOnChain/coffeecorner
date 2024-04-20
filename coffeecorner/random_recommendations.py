# python manage.py shell
import random
from shop.models import Product
from shop.recommender import Recommender


products = list(Product.objects.all())

r = Recommender()

for _ in range(100):
    num_products = random.randint(1, 9)
    bought_products = random.sample(products, num_products)
    r.products_bought(bought_products)


for product in products:
    print(f"Рекомендации для {product.name}:")
    recommended_products = r.suggest_products_for([product])
    for recommended_product in recommended_products:
        print(f"- {recommended_product.name}")
    print()
