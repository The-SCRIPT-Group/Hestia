from django.shortcuts import render
from django.views.generic import View

from new_app.csv_code import locate
from new_app.forms import PageForm


class PageView(View):

    def get(self, request, *args, **kwargs):
        found = False
        csv_form = PageForm()
        msg = ""
        context = {
            'csv_form': csv_form,
            'found': found,
            'msg': msg
        }
        return render(request, 'page.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)

        if form.is_valid():
            found = True
            key = form.cleaned_data.get('key')
            data = locate(key)
            if data == 0:
                found = False
                msg = "Data not found!"
                context = {
                    'found': found,
                    'msg': msg
                }
                return render(request, 'page.html', context)
            else:
                print(data)
                context = {
                    'data':data,
                    'found':found
                }

                return render(request, 'page.html', context)
