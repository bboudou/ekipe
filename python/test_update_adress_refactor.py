from models.pages import ResetDBPage, AddEmployeePage, EditEmployeePage

def test_update_adress(page):

    reset_db_page = ResetDBPage(page)
    add_employee_page = AddEmployeePage(page)
    edit_employee_page = EditEmployeePage(page)

    # Make sure db is empty
    reset_db_page.navigate()
    reset_db_page.reset_db()

    # Create a user
    add_employee_page.navigate()

    # Set the user data
    user_name = "test"
    user_mail = "test@mail.fr"
    adress_line1 = "test adress"
    city = "test city"
    zip_code = "11111"
    hiring_date = "2025-01-01"
    job_title = "ekipier"
    add_employee_page.add_employee(user_name, user_mail, adress_line1, city, zip_code, hiring_date, job_title)

    # Edit the user

    edit_employee_page.navigate()

    # Update the adress

    address_input2 = "test adress 2"
    edit_employee_page.update_address(address_input2)

    # Check the new adress is there

    page.click("text='Update address'")
    assert page.is_visible(f"td:has-text('{address_input2}')")

