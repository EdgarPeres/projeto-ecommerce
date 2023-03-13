from models import product_model, user_model

def main():
    user1 = user_model.User(id=1, name='John', email='john@example.com', password='password')
    user1.save()

    product1 = product_model.Product(id=1, name='T-shirt', description='A comfortable cotton T-shirt', price=19.99, stock=50)
    product1.save()

    product2 = product_model.Product(id=2, name='Jeans', description='A pair of classic denim jeans', price=49.99, stock=25)
    product2.save()

    product3 = product_model.Product(id=3, name='Sneakers', description='A pair of stylish sneakers', price=79.99, stock=10)
    product3.save()

if __name__ == '__main__':
    main()
