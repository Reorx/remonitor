from utils.viewsbase import ApiBaseError

class BaseMiddleware(object):
    #def process_request(self, req):
        #return None

    def process_exception(self, req, e):
        if isinstance(e, ApiBaseError):
            return e.get_resp()

    #def process_response(self, req, resp):
        #return resp

