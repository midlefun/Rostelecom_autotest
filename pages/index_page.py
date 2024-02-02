import time

from playwright.sync_api import Page, expect
import playwright
import pytest
import config


class IndexPage:
    _BUTTON_LOGIN_MENU = '#lk-enter'
    _LINK_LOGIN_PAGE = '.lk-popup__links .'
    _BUTTON_TOWN_CHANGE_MODAL = '#block-b2cpanellichnykhkabinetoviligeo'

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN_MSC)

    def press_login_menu_button(self, page: Page) -> None:
        page.locator(self._BUTTON_LOGIN_MENU).click()

    def press_login_page_link(self, page: Page) -> None:
        page.get_by_text('Личный кабинет РФ').nth(0).click()

    def go_to_and_compare_url_login_page(self, page: Page) -> None:
        with page.context.expect_page() as login_page:
            self.press_login_page_link(page)
        new_page = login_page.value
        assert new_page.url == config.url.LOGIN

    ############################

    _POPUP_CHANGE_TOWN = '.cmp-regions-popup__rtp'
    _POPUP_CHANGE_TOWN_ACTIVE = '.rt-popup-wrapper--is-active'

    def press_town_change_modal_button(self, page: Page) -> None:
        page.locator(self._BUTTON_TOWN_CHANGE_MODAL).click()

    _SELECTOR = '.cmp-regions-select__result'

    def input_text_in_modal_input(self, page: Page) -> None:
        input = page.get_by_placeholder('Найти город')
        input.fill('Краснодар')
        page.wait_for_selector(self._SELECTOR)
        input.press('Enter')

    _BUTTON_TOWN_CHANGE_MODAL_TEXT_HEADER = '#block-b2cpanellichnykhkabinetoviligeo >> .geo-name'
    _BUTTON_TOWN_CHANGE_MODAL_TEXT_ORANGE = '#cards-title >> .rt-link--orange'

    def check_that_town_is_change(self, page: Page) -> None:
        page.wait_for_selector(self._BUTTON_TOWN_CHANGE_MODAL_TEXT_ORANGE)
        assert 'Краснодар' in page.locator(
            self._BUTTON_TOWN_CHANGE_MODAL_TEXT_HEADER).text_content() and 'Краснодар' in page.locator(
            self._BUTTON_TOWN_CHANGE_MODAL_TEXT_ORANGE).text_content() and page.url == config.url.DOMAIN_KRASNODAR

