import sublime
import sublime_plugin

class CleanSpaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Iterate over all selected regions in the current view
        for region in self.view.sel():
            # Get the selected text
            selected_text = self.view.substr(region)

            # Remove consecutive spaces
            cleaned_text = ' '.join(selected_text.split())

            # Replace the selected text with the cleaned text
            self.view.replace(edit, region, cleaned_text)
