from uuid import uuid4

def product_image_path(instance, filename):
  product = instance.product
  store = product.store
  brand = product.brand
  filename = f'{uuid4().hex}{filename}'
  return f'products/{store.name}/{brand.name}/{product.name}/{filename}'
