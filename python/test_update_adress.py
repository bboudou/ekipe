def test_update_adress(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    # Create a user
    page.goto("/")
    page.goto("/add_employee")
    name_input = page.locator('#id_name')
    user_name = "test"
    name_input.fill(user_name)
    mail_input = page.locator('#id_email')
    user_mail = "test@mail.fr"
    mail_input.fill(user_mail)

    adress_input = page.locator('#id_address_line1')
    adress_line1 = "test adress"
    adress_input.fill(adress_line1)
    city_input = page.locator('#id_city')
    city = "test city"
    city_input.fill(city)
    zip_input = page.locator('#id_zip_code')
    zip_code = "11111"
    zip_input.fill(zip_code)

    date_input = page.locator('#id_hiring_date')
    hiring_date = "2025-01-01"
    date_input.fill(hiring_date)
    job_input = page.locator('#id_job_title')
    job_title = "ekipier"
    job_input.fill(job_title)

    page.click("text='Add'")

    # Edit the user

    page.click("text='Edit'")
    page.click("text='Update address'")

    # Update the adress

    adress_input2 = page.locator('#id_address_line2')
    adress_line2 = "test adress 2"
    adress_input2.fill(adress_line2)

    page.click("text='Update'")

    # Check the new adress is there

    page.click("text='Update address'")
    assert page.is_visible(f"td:has-text('{adress_line2}')")

