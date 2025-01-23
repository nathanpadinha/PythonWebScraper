from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from Functions.ProductFunctions import *
from Functions.ProductScraperFunctions import *

class ProductScraperApp(App):
    def build(self):
        # Check connection at the start
        CheckConnection()

        # Main layout
        self.file = None  # Placeholder for the open file
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Input for URL
        self.url_input = TextInput(
            hint_text="Enter the product URL",
            size_hint=(1, 0.2),
            multiline=False,
            background_color=(0.9, 0.9, 0.9, 1),  # Light gray background
            foreground_color=(0, 0, 0, 1),        # Black text
            cursor_color=(1, 0, 0, 1),            # Red cursor
            font_size=24,                         # Adjust font size
            padding=(10, 10),                     # Inner padding
            hint_text_color=(0.5, 0.5, 0.5, 1)    # Gray hint text
        )

        # Submit button
        self.submit_button = Button(
            text="Submit URL",
            size_hint=(1, 0.2)
        )
        self.submit_button.bind(on_press=self.process_url)

        # Label for status/output
        self.status_label = Label(
            text="Enter a URL and click Submit.",
            size_hint=(1, 0.2)
        )

        # Add widgets to the layout
        self.layout.add_widget(self.url_input)
        self.layout.add_widget(self.submit_button)
        self.layout.add_widget(self.status_label)

        return self.layout

    def process_url(self, instance):
        # Get URL from input
        url = self.url_input.text.strip()

        if not url:
            self.status_label.text = "Please enter a valid URL."
            return

        try:
            # Open file
            if not self.file:
                self.file = OpenFile()

            # Get retailer from URL
            retailer = GetRetailer(url)

            if retailer == -1:
                self.status_label.text = "Please provide a valid URL."
                return

            # Check if retailer matches
            if not ProductMatch(retailer):
                self.status_label.text = "Retailer not recognized. Skipping entry."
                return

            # Scrape title and price
            title, price = ScrapeRetailer(retailer, url)

            # Write the data to the file
            WriteToFile(url, retailer, title, price, self.file)

            # Update the status label
            self.status_label.text = f"Data written: {title} - {price}"

        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
        finally:
            # Ensure file is closed properly
            if self.file:
                self.file.close()
                self.file = None


if __name__ == "__main__":
    try:
        ProductScraperApp().run()
    except KeyboardInterrupt:
        print("\nUser Cancelled")