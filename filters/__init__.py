

from loader import dp
from . admins import Admin
from . group import Group
from . shaxsiy import Shaxsiy
if __name__ == "filters":
    dp.filters_factory.bind(Admin)
    dp.filters_factory.bind(Group)
    dp.filters_factory.bind(Shaxsiy)


