from flask import Blueprint, render_template, request

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def index():
    products = get_all_products() # função que busca todos os produtos
    return render_template('products.html', products=products)

@product_bp.route('/products/<int:product_id>')
def details(product_id):
    product = get_product_by_id(product_id) # função que busca um produto pelo ID
    return render_template('product_details.html', product=product)

@product_bp.route('/products/search')
def search():
    query = request.args.get('query') # busca termo de pesquisa a partir da query string
    results = search_products(query) # função que busca produtos por termo de pesquisa
    return render_template('product_search.html', results=results, query=query)
