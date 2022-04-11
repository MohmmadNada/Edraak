from selenium.webdriver.common.by import By

class HomePage(object):
    
    
    def __init__(self):
        self.base_url = "https://www.edraak.org/en"    
        self.page_url = "/"
        self.full_url = self.base_url + self.page_url 
        # Selectors
        self.close_cookies_container = '//div[@id="onetrust-close-btn-container"]/button'
        self.explore_button = '//a[@href="/en/explore/"]'
        self.discover_programs_button = '//button[text()="Discover programs"]'
        self.explore_specializations_button = '//button[text()="Explore specializations"]'
        self.first_course_card = '(//div[@class="courseCard"])[1]'
        self.show_all_partners_button = '//button[text()="Show all partners"]'
        self.visit_k12_platform_button = '//button[text()="Visit K-12 Platform"]'
        self.business_and_entrepreneurship = '//div[@class="coursesCategories"]/span[text()="Business and Entrepreneurship"]'
        self.persona_development = '//div[@class="coursesCategories"]/span[text()="Personal Development"]'
        self.science_and_technology = '//div[@class="coursesCategories"]/span[text()="Science & Technology"]'
        self.first_course_card = '//div[@class="courses"]/a[1]//h4'
        self.second_course_card = '//div[@class="courses"]/a[2]//h4'
        self.third_course_card = '//div[@class="courses"]/a[3]//h4'
