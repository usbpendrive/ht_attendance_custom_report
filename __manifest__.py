{
    'name': 'Attendance Custom Report',
    'summary': 'Odoo Attendance Module Custom Report',
    'description': """Odoo Attendance Module Custom Report""",
    'website': 'https://github.com/usbpendrive/ht_attendance_custom_report',
    'category': 'Attendance',
    'version': '11.0.1.0.0',
    'depends': ['base','hr_attendance'],
    'data': [
        'views/attendance_recap_report_view.xml',
        'reports/recap_report.xml',
    ],
}
