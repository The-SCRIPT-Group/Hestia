from django.shortcuts import render
from django.views.generic import View

from new_app.csv_code import locate
from new_app.forms import PageForm
import os


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
            event = form.cleaned_data.get('event')
            data = {}
            folder = ''
            if event == 'codex-dec':
                os.environ["CSV_URL"] = 'http://csv.thescriptgroup.in/Participants.csv'
                folder = 'CodeX-December-2019'
                data = locate(key, 3)
            elif event == 'bov':
                os.environ["CSV_URL"] = 'http://csv.thescriptgroup.in/ranksortedfinal.csv'
                folder = 'Battle-of-Vars'
                data = locate(key, 6)

            if not bool(data):
                found = False
                msg = "Data not found!"
                context = {
                    'found': found,
                    'msg': msg
                }
                return render(request, 'page.html', context)
            else:
                cert_url = f'https://certificates.thescriptgroup.in/{folder}/' + str(
                    data['Credential Id']) + '.jpg'
                context = {
                    'data': data,
                    'found': found,
                    'certificate': cert_url
                }

                return render(request, 'page.html', context)
