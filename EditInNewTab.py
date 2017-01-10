import sublime, sublime_plugin

class EditInNewTabCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection_text = ""
        # open a new file
        view = sublime.active_window().new_file()

        # get selected text
        sels = self.view.sel()
        for sel in sels:
           selection_text = selection_text + self.view.substr(sel) + '\n'

        # insert selected text into the new file
        view.insert(edit, 0, selection_text[:-1])
