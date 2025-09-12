def transform_products(products, category, discount):
    """
    Transforms a list of product dicts by filtering by category and applying a discount.
    Args:
        products (list): List of dicts with keys 'name', 'category', 'price'.
        category (str): Category to filter by.
        discount (float): Discount percentage (e.g., 0.1 for 10%).
    Returns:
        list: List of dicts with 'name', 'category', and 'discounted_price'.
    """
    filtered = [p for p in products if p['category'] == category]
    return [
        {
            'name': p['name'],
            'category': p['category'],
            'discounted_price': round(p['price'] * (1 - discount), 2)
        }
        for p in filtered
    ]


 