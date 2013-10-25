#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author: Panagiotis Mavrogiorgos
email : gmail, pmav99
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserAdmin(admin.ModelAdmin):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


admin.site.register(User, UserAdmin)
