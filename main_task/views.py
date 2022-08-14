from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from TestTaskV2.settings import airtable_conn


class AllUsersView(TemplateView):
    template_name = "main_task/all_users.html"

    def get_context_data(self, **kwargs):
        result = []
        data = airtable_conn.get_all()
        for i in data:
            user = i.get("fields")
            result.append(user)
        return {"users": result}
