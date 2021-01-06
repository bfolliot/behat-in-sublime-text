import os
import sys
import shlex
import subprocess
import sublime
import sublime_plugin

if sys.version_info < (3, 3):
    raise RuntimeError('RunBehat works with Sublime Text 3 only')

SPU_THEME = 'Packages/RunBehat/RunBehat.hidden-tmTheme'
SPU_SYNTAX = 'Packages/RunBehat/RunBehat.hidden-tmLanguage'

class ShowInPanel:
    def __init__(self, window):
        self.window = window

    def display_results(self):
        self.panel = self.window.get_output_panel("exec")
        self.window.run_command("show_panel", {"panel": "output.exec"})

        self.panel.settings().set("color_scheme", SPU_THEME)
        self.panel.set_syntax_file(SPU_SYNTAX)

class RunBehatCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunBehatCommand, self).__init__(*args, **kwargs)
        settings = sublime.load_settings('RunBehat.sublime-settings')
        self.behat_path = settings.get('behat_path')

    def run(self, *args, **kwargs):
        try:
            self.PROJECT_PATH = self.window.folders()[0]
            if os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'behat.yml')) or os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'config/behat.yml')):
                self.params = kwargs.get('params', False)
                self.args = [self.behat_path, '--format=progress']
                if self.params is True:
                    self.window.show_input_panel('Params:', '', self.on_params, None, None)
                else:
                    self.on_done()
            else:
                sublime.status_message("behat.yml or config/behat.yml not found")
        except IndexError:
            sublime.status_message("Please open a project with Behat")

    def on_params(self, command):
        self.command = command
        self.args.extend(shlex.split(str(self.command)))
        self.on_done()

    def on_done(self):
        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)
        try:
            self.run_shell_command(self.args, self.PROJECT_PATH)
        except IOError:
            sublime.status_message('IOError - command aborted')

    def run_shell_command(self, command, working_dir):
            self.window.run_command("exec", {
                "cmd": command,
                "shell": os.name == 'nt',
                "working_dir": working_dir
            })
            self.display_results()
            return True

    def display_results(self):
        display = ShowInPanel(self.window)
        display.display_results()

    def window(self):
        return self.view.window()
