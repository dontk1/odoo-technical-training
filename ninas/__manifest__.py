# -*- coding: utf-8 -*-
# @author TK
# Date: 4/06/18


{
    'name': 'Ninas Academy', 
    'summary': 'Ninas Academy',
    'description': """ Ninas Academy
                        The best academy in MCEE. 
                        You won't believe what you can see. 
                    """,
    'author': 'Tosin K',
    'website': 'http://tosinkomolafe.com',
    'version': '10.0.0.0.1',
    'category': 'Ninas Academy',
    'application':True,
    'installable':True,
    'auto-install':False,
    'depends': ['base', 'hr', 'mail', 'website'],
    'external_dependencies': {
        'python':[],
        'bin':[]
    },
    'data':['security/ninas_security.xml',
            'security/ir.model.access.csv',
            'views/course_view.xml',
            'views/section_view.xml',
            'views/student_view.xml',
            'views/employee_view.xml',
            'views/menuitem_view.xml',
            'data/ninas_student_data.xml',
            'wizard/ninas_student_wizard_view.xml',
            'controllers/web_templates.xml'
            #'report/ninas_student_report.xml'
            #'report/ninas_student_report_template.xml',
            ],
    'css':[],
    'demo':['demo/ninas_student_demo.xml'],
    'test':[],
}