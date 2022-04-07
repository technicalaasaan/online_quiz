from django.http import HttpResponseRedirect
from django.shortcuts import redirect, resolve_url

class QuizMiddleware:
    def __init__(self, resp):
        self.get_response = resp

    def __call__(self, req):
        resp = self.get_response(req)
        return resp

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'admin' in request.path_info:
            return None
        if request.user.is_authenticated:
           if request.path_info in ['/login/', '/register/']:
               return redirect('/')
           return
        else:
            if request.path_info in ['/login/', '/register/']:
                return
            else:
                return redirect(resolve_url('login'))

        # if request.path_info in ['/login/', '/register/']:
        #     if request.user.is_authenticated:
        #         return redirect('/')
        #     return redirect(request.path_info)
        # else:
        #     if request.user.is_authenticated:
        #         return redirect(request.path_info)
            # return redirect(resolve_url('login'))
    
    # def process_view(self):
