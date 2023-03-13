from flask import Blueprint, render_template, redirect, url_for, session

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
def index():
    cart_items = get_cart_items(session.get('cart', [])) # função que busca itens do carrinho de compras
    total = calculate_cart_total(cart_items) # função que calcula o valor total do carrinho
    return render_template('cart.html', cart_items=cart_items, total=total)

@cart_bp.route('/cart/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id) # adiciona o ID do produto ao carrinho
    session['cart'] = cart # atualiza a sessão do carrinho
    return redirect(url_for('cart.index'))

@cart_bp.route('/cart/remove/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id) # remove o ID do produto do carrinho
        session['cart'] = cart # atualiza a sessão do carrinho
    return redirect(url_for('cart.index'))
