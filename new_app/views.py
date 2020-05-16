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
            cert_available = True
            key = form.cleaned_data.get('key')
            event = form.cleaned_data.get('event')
            data = {}
            folder = ''
            if event == 'codex-dec':
                folder = 'CodeX-December-2019'
                cert_available = False
                data = locate('Participants.csv', key, 3)
            elif event == 'bov':
                folder = 'Battle-of-Vars'
                data = locate('ranksortedfinal.csv', key, 6)

            if not bool(data):
                found = False
                msg = "Data not found!"
                context = {
                    'found': found,
                    'msg': msg,
                    'cert_available': cert_available
                }
            else:
                cert_url = f'https://certificates.thescriptgroup.in/{folder}/' + str(
                    data['Credential Id']) + '.jpg'
                context = {
                    'data': data,
                    'found': found,
                    'certificate': cert_url,
                    'cert_available': cert_available
                }

            return render(request, 'page.html', context)
