from django import forms

class WebScrapeForm(forms.Form):
    search_url = forms.URLField( initial="http://", label="Insert URL")
