from logging import raiseExceptions
from behave import * 
from features.environment import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
use_step_matcher("re")
from features.steps.src.pageObject import PAGE_OBJECT_MAP

@when("the user visits the (.*)")
def visit_page_and_check_url(context, page_name):
    """
    :param context: Behave convention. Variable that holds all test data
    :param page_name: Page Object
    Every page object will have self.url on it, if we want to directly visit pages
    :return: browser visits the url
    """
    context.page = PAGE_OBJECT_MAP[page_name.lower()]
    context.driver.get(context.page.full_url)
    assert(context.page.page_url in context.driver.current_url), f"Expect {context.driver.current_url} to contain {context.page.page_url}"

@when("the (?i)user (?:clicks|checks)(?: the)? (.*)")
def click_web_element(context, element):
    """
    :param context: Behave convention. Variable that holds all test data
    :param element: name of PageElement we want to click
    :return: click() the element
    """
    element = element.lstrip().replace(" ", "_").lower()
    selector = getattr(context.page, element)
    try:
        element_to_click = context.driver.find_element_by_xpath(selector)
    except:
        raise Exception(f"We could not find the {element} element ")

    ActionChains(context.driver).move_to_element(element_to_click).click().perform()

@step("the user opens a specific page by clicks the following elements")
def press_cmd_and_click_on(context):
    """
    :param context: context.table
    the table contains element to click and target page, By press command from keyboard and click the element the new page will open in new tab
    chicking new tab will deacrease the test time
    :return: Checking correct page link
    """

    for row in context.table:
        element = row[0].lstrip().replace(" ", "_").lower()
        selector = getattr(context.page, element)
        try:
            element_to_click = context.driver.find_element_by_xpath(selector)
        except:
            raise Exception(f"We could not find the {element} element In the page")
        ActionChains(context.driver).key_down(Keys.COMMAND).click(element_to_click).key_up(Keys.COMMAND).perform()
        context.driver.switch_to.window(context.driver.window_handles[1])
        try:
            page_name = row[1].lstrip().lower()
            context.tab_page = PAGE_OBJECT_MAP[page_name]
        except:
            raiseExceptions(f"Couldn't find the page {page_name}")
        
        assert(context.tab_page.page_url in context.driver.current_url), f"When the user clicks on {element}; Expected {context.driver.current_url} link to contain {context.tab_page.page_url}"
        context.driver.close()
        context.driver.switch_to.window(context.driver.window_handles[0])


@step(r"the (.*) should be displayed with text")
def validate_element_text(context, page_element):
    """
    :type context: behave.runner.Context
    :param page_element: element we want to validate text or value of
    context.text - a Behave convention. Anytime a step is found with text in triple quotes
    Behave stores this as 'context.text' (our expected text in this case)
    """
    element = page_element.lstrip().replace(" ", "_").lower()
    selector = getattr(context.page, element)
    web_element = context.driver.find_element_by_xpath(selector)
    actual_element_text = web_element.text
    assert(actual_element_text == context.text), f"Expected: {element} element to have text {context.text} but we get {actual_element_text}"

@then(r"the following elements should be displayed with specific text")
def validate_elements_text(context):
    for row in context.table:
        context.text = row[1]
        validate_element_text(context=context, page_element=row[0])