from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    featured_products = get_featured_products() # função que busca produtos em destaque
    return render_template('index.html', products=featured_products)