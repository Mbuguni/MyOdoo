{
    'name': "RealEstateApplication",
    'installable': True,
    'application': True,
    'auto_install': False,
    'category': 'services',

    'icon': 'REALESTATE/static/description/__myIcon.png',
    'data': ['views/real_estate_views.xml',
             'security/ir.model.access.csv',
             'security/real_estate_security.xml', ],
}
