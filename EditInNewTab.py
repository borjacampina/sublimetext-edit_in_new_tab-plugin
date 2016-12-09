import sublime, sublime_plugin

class EditInNewTabCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        region1 = sel[0]
        selectionText = self.view.substr(region1)

        view = sublime.active_window().new_file()
        view.insert(edit, 0, selectionText)
