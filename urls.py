from config import api
from views import *

api.add_resource(Register, '/register/')
api.add_resource(Login, '/login/')
api.add_resource(Logout, '/logout/')
api.add_resource(Floor, '/floor/')
api.add_resource(Nft, '/nft/')
api.add_resource(Loan, '/loan/')
