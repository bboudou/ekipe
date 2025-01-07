def test_delete_team(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    # Create a team
    page.goto("/add_team")
    name_input = page.locator('#id_name')
    team_name = "test"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Delete the team

    page.click("text='Delete'")
    page.click("text='Proceed'")

    # Check the team is not there

    assert not page.is_visible(f"td:has-text('{team_name}')")