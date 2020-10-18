from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from collections import deque

MENU_OPTIONS = {"inflate_tires": 'Inflate tires',
                "change_oil": 'Change Oil',
                "diagnostic": 'Get diagnostic test'}

ticket_number = 0
time_diagnostic = 30
time_tires = 5
time_oil = 2
line_of_cars = {'change_oil': deque(), 'inflate_tires': deque(),
                'diagnostic': deque()}

next_ticket = 'Waiting for the next client'

class WelcomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/welcome.html')


class MenuView(View):

    def get(self, request, *args, **kwargs):
        context = {"menu_options": MENU_OPTIONS,
                   "tickets": "get_ticket"}
        return render(request, 'tickets/menu.html', context=context)


class ServiceView(View):

    def get(self, request, service, *args, **kwargs):
        time = 0
        global ticket_number
        ticket_number += 1
        if service == 'change_oil':
            time = len(line_of_cars['change_oil']) * time_oil
            line_of_cars['change_oil'].appendleft(ticket_number)
        elif service == 'inflate_tires':
            time = len(line_of_cars['change_oil']) * time_oil + len(
                line_of_cars['inflate_tires']) * time_tires
            line_of_cars['inflate_tires'].appendleft(ticket_number)
        elif service == 'diagnostic':
            time = len(line_of_cars['change_oil']) * time_oil + len(
                line_of_cars['inflate_tires']) * time_tires + len(
                line_of_cars['diagnostic']) * time_diagnostic
            line_of_cars['diagnostic'].appendleft(ticket_number)

        context = {'ticket_number': ticket_number, 'minutes_to_wait': time}
        return render(request, 'tickets/service.html', context=context)


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        context = {'change_oil': len(line_of_cars['change_oil']),
                       'inflate_tires': len(line_of_cars['inflate_tires']),
                       'diagnostic': len(line_of_cars['diagnostic'])}
        return render(request, 'tickets/processing.html', context=context)

    def post(self, request, *args, **kwargs):
        global next_ticket
        next_v = None
        if len(line_of_cars['change_oil']):
            next_v = line_of_cars['change_oil'].pop()
        elif len(line_of_cars['inflate_tires']):
            next_v = line_of_cars['inflate_tires'].pop()
        elif len(line_of_cars['diagnostic']):
            next_v = line_of_cars['diagnostic'].pop()

        context = {'text': ''}
        if next_v:
            next_ticket = 'Next ticket #{}'.format(next_v)
        else:
            next_ticket = 'Waiting for the next client'

        return redirect('/next')


class NextView(View):

    def get(self, request, *args, **kwargs):
        global next_ticket
        context = {'text': next_ticket}

        return render(request, 'tickets/next.html', context=context)