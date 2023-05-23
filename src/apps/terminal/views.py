import os
import subprocess
from pathlib import Path

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import TerminalForm
from .models import TerminalPath


class TerminalMethodsMixin:
    @staticmethod
    def get_path_and_object() -> tuple:
        path_object = TerminalPath.objects.get_or_create(
            pk=1,
            defaults={'string': Path(os.getcwd())},
        )[0]
        path = Path(path_object.string)
        return path_object, path

    @staticmethod
    def execute_command(command: str) -> str:
        response_bytes = subprocess.check_output(command, shell=True)
        return response_bytes.decode('utf-8')

    @staticmethod
    def correct_command(command: str):
        if command.strip(' ') == 'ls':
            command = 'ls -F'
        return command


class TerminalView(TerminalMethodsMixin, View):
    title = 'Terminal'
    template = 'terminal/terminal.html'
    base_path = os.getcwd()

    def get(self, request: WSGIRequest) -> HttpResponse:
        _, path = self.get_path_and_object()

        terminal_form = TerminalForm()
        context = {
            'terminal_form': terminal_form,
            "path": path,
        }
        return self.get_context_data(**context)

    def post(self, request):
        path_object, path = self.get_path_and_object()

        response: str | None = None
        if (terminal_form := TerminalForm(request.POST)).is_valid():
            command = terminal_form.cleaned_data["command"]
            try:
                command: str = self.correct_command(command)
                response: str = self.execute_command(command)

                match command.split():
                    case [command_name, add_path, *t] if command_name == 'cd':
                        if t:
                            response = 'error: command cd must have ' \
                                       'one argument'
                        else:
                            if add_path == '..':
                                path = path.parent
                            elif add_path != '..':
                                path = path / add_path

            except (
                FileNotFoundError,
                subprocess.CalledProcessError,
                UnboundLocalError,
            ) as exp:
                response = f'error: {exp}'

        elif request.POST.get("reset"):
            path = self.base_path

        os.chdir(path)

        path_object.string = path
        path_object.save()

        context = {
            'terminal_form': terminal_form,
            "path": path,
            'response': response,
        }

        return self.get_context_data(**context)

    def get_context_data(self, **kwargs):
        kwargs |= {
            'title': self.title,
        }
        return render(self.request, self.template, kwargs)
