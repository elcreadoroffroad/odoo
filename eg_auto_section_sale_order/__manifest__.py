{
    'name': ' Auto Section In Sale Order ',
    'version': '17.0',
    'category': "Sales",
    
    'summary': 'Automatically assign sale order lines to product sections in Odoo, ensuring seamless organization and matching invoice structure. , Automatic Sale Order Sections, Group Sale Order Lines by Section, Product Section Management in Sales, Section-Based Sale Orders, Organized Sale Order Line Items, Invoice Sections Matching Sale Orders, Auto Sections for Product Organization, Sale Order Line Automation, Predefined Sections in Sale Orders, Dynamic Sale Order Sections, Streamlined Sale Order Organization, Sectioned Invoices for Sales, Product Grouping in Sale Orders, Sale Order Section Workflow, Automated Section Creation for Sales.',
    'description': """
        The "Auto Section in Sale Order" app allows users to define product sections and automatically assign sale order lines to these sections. This feature enhances the organization of products within sale orders, improving workflow efficiency. Additionally, the invoice structure reflects the same sections as the sale order, maintaining consistency between the order and invoice.
        
        Key Features:
        1) **Section Management in Product and Sale Order Menus**:
           - Define sections for products and create new sections directly from the sale order section menu.
        
        2) **Sectioned Sale Order Lines**:
           - Group products in sale orders under defined sections for better organization.
        
        3) **Auto Section Creation**:
           - Automatically create sections in the sale order lines based on product definitions, eliminating manual setup.
        
        4) **Consistency Between Sale Order and Invoice**:
           - Ensure that the invoice structure mirrors the same sections as the sale order, maintaining consistency across documents.
        
        This app automates the sectioning of sale order lines, providing a smooth and organized experience from order creation to invoicing.
    """,

    'author': 'INKERP',
    'website': 'https://www.inkerp.com/',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/sale_order_section_views.xml',

    ],
    'images': ['static/description/banner.gif'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': '19.00',
    'currency': 'EUR',
}
