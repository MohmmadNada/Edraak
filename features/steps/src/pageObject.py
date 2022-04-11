
from lib.pages.home_page import HomePage
from lib.pages.explore_page import ExplorePage
from lib.pages.programs_page import ProgramsPage
from lib.pages.partners_page import PartnersPage
from lib.pages.k12_page import k12Page

PAGE_OBJECT_MAP = {
    "home page": HomePage(),
    "explore page": ExplorePage(),
    "programs page": ProgramsPage(),
    "partners page": PartnersPage(),
    "k12 page": k12Page(),
}