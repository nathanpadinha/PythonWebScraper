from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class TextInputApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a text input
        self.text_input = TextInput(
            hint_text="Enter some text",
            size_hint=(1, 0.2),
            multiline=False
        )

        # Create a button
        button = Button(
            text="Submit",
            size_hint=(1, 0.2)
        )
        button.bind(on_press=self.on_submit)

        # Create a label to display the output
        self.output_label = Label(
            text="Your input will appear here.",
            size_hint=(1, 0.2)
        )

        # Add widgets to the layout
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.output_label)

        return layout

    def on_submit(self, instance):
        # Update the label text with the input from the text box
        userInput = self.text_input.text
        return userInput



# Run the app
if __name__ == "__main__":
    TextInputApp().run()