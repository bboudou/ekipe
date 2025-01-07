from models.pages import ResetDBPage, AddTeamPage, TeamManagement

def test_delete_team(page):

    reset_db_page = ResetDBPage(page)
    add_team_page = AddTeamPage(page)
    team_management_page = TeamManagement(page)

    # Make sure db is empty
    reset_db_page.navigate()
    reset_db_page.reset_db()

    # Create a team
    add_team_page.navigate()
    team_name = "ekip"
    add_team_page.add_team(team_name)

    # Delete the team
    team_management_page.navigate()
    team_management_page.delete_team()

    # Check the team is not there
    assert not page.is_visible(f"td:has-text('{team_name}')")