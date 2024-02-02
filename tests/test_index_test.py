import pages
import playwright


class TestFooter:

    # def test_user_should_be_able_to_go_to_login_page(self, page):
    #     index_page = pages.index_page
    #     index_page.open_index_page(page)
    #     index_page.press_login_menu_button(page)
    #     pages.index_page.press_login_page_link(page)
    #     index_page.go_to_and_compare_url_login_page(page)

    def test_user_should_be_able_to_change_town(self, page):
        index_page = pages.index_page
        index_page.open_index_page(page)
        index_page.press_town_change_modal_button(page)
        index_page.input_text_in_modal_input(page)
        index_page.press_town_change_modal_button(page)
        index_page.check_that_town_is_change(page)

    def test_user_should_be_able_to_change_town_special_symbol(self, page):
        pass