{
    'name': 'EcoSphere ESG Management',
    'version': '1.0',
    'summary': 'ESG Management Platform for Odoo Hackathon 2026',
    'description': 'Track carbon emissions, CSR activities, and ESG scores by department.',
    'category': 'Human Resources',
    'author': 'Ashish Sharma',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/esg_department_views.xml',
    ],
    'installable': True,
    'application': True,
}
