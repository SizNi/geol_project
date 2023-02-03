from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class CrossIndexView(TemplateView):

    template_name = 'cross_section/index_cross.html'