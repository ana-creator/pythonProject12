from pages import login_page


def test_create_report(self):
    login_page.login()
    pim.goto_reports()
    reports.add()
    new_report.set_name(report_name)
    new_report.select_selection_criteria("Job Title")
    new_report.select_display_field_groups("Personal")
    new_report.enable_display_fields()
    new_report.save()
    reports.search(report_name)

