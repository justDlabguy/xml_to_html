import streamlit as st
import xml.etree.ElementTree as ET
from jinja2 import Environment

def parse_xml(xml_content):
    """Parse the XML content and extract form data."""
    root = ET.fromstring(xml_content)

    form_data = {
        'form_title': root.find('title').text if root.find('title') is not None else "Untitled Form",
        'form_description': root.find('description').text if root.find('description') is not None else "",
        'fields': [],
        'submit_label': root.find('submit/label').text if root.find('submit/label') is not None else "Submit"
    }

    for field in root.findall('field'):
        field_data = {
            'type': field.find('type').text if field.find('type') is not None else "text",
            'name': field.find('name').text if field.find('name') is not None else "",
            'label': field.find('label').text if field.find('label') is not None else "",
            'required': field.find('required').text == 'true' if field.find('required') is not None else False,
            'placeholder': field.find('placeholder').text if field.find('placeholder') is not None else None,
            'minlength': field.find('minlength').text if field.find('minlength') is not None else None,
            'checked': field.find('checked').text == 'true' if field.find('checked') is not None else False,
            'options': []
        }

        if field_data['type'] in ['select', 'radio']:
            options = field.find('options')
            if options is not None:
                for option in options:
                    field_data['options'].append({
                        'value': option.get('value'),
                        'text': option.text
                    })

        form_data['fields'].append(field_data)

    return form_data

def generate_html(form_data, styling_options):
    """Generate HTML form using Jinja2 template with custom styling."""
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ form_title }}</title>
        <style>
            body {
                font-family: '{{ styling_options.font }}';
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: {{ styling_options.background_color }};
                color: {{ styling_options.text_color }};
            }
            h1 {
                color: {{ styling_options.title_color }};
            }
            .form-group {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            input[type="text"],
            input[type="email"],
            input[type="password"],
            select,
            textarea {
                width: 100%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: {{ styling_options.input_background_color }};
                color: {{ styling_options.input_text_color }};
            }
            textarea {
                height: 100px;
            }
            .radio-group, .checkbox-group {
                margin-top: 5px;
            }
            .radio-option, .checkbox-option {
                margin-right: 10px;
            }
            button {
                background-color: {{ styling_options.button_color }};
                color: {{ styling_options.button_text_color }};
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: {{ styling_options.button_hover_color }};
            }
        </style>
    </head>
    <body>
        <h1>{{ form_title }}</h1>
        <p>{{ form_description }}</p>
        <form>
            {% for field in fields %}
            <div class="form-group">
                <label for="{{ field.name }}">{{ field.label }}</label>
                {% if field.type == 'text' or field.type == 'email' or field.type == 'password' %}
                    <input type="{{ field.type }}"
                           id="{{ field.name }}"
                           name="{{ field.name }}"
                           placeholder="{{ field.placeholder if field.placeholder else '' }}"
                           {% if field.required %}required="required"{% endif %}
                           {% if field.minlength %}minlength="{{ field.minlength }}"{% endif %}>
                {% elif field.type == 'select' %}
                    <select id="{{ field.name }}" name="{{ field.name }}" {% if field.required %}required="required"{% endif %}>
                        {% for option in field.options %}
                            <option value="{{ option.value }}" {% if option.value == field.selected %}selected{% endif %}>{{ option.text }}</option>
                        {% endfor %}
                    </select>
                {% elif field.type == 'checkbox' %}
                    <input type="checkbox"
                           id="{{ field.name }}"
                           name="{{ field.name }}"
                           {% if field.checked %}checked="checked"{% endif %}>
                {% elif field.type == 'radio' %}
                    <div class="radio-group">
                        {% for option in field.options %}
                            <label class="radio-option">
                                <input type="radio"
                                       name="{{ field.name }}"
                                       value="{{ option.value }}"
                                       {% if loop.first %}checked="checked"{% endif %}> {{ option.text }}
                            </label>
                        {% endfor %}
                    </div>
                {% elif field.type == 'textarea' %}
                    <textarea id="{{ field.name }}"
                              name="{{ field.name }}"
                              placeholder="{{ field.placeholder if field.placeholder else '' }}"></textarea>
                {% endif %}
            </div>
            {% endfor %}
            <button type="submit">{{ submit_label }}</button>
        </form>
    </body>
    </html>
    """

    env = Environment()
    template = env.from_string(html_template)
    html_output = template.render(
        form_title=form_data['form_title'],
        form_description=form_data['form_description'],
        fields=form_data['fields'],
        submit_label=form_data['submit_label'],
        styling_options=styling_options
    )
    return html_output

def main():
    st.title("XML to HTML Form Converter")
    st.write("Upload an XML file to convert it into an HTML form.")

    # Styling options sidebar
    st.sidebar.header("Styling Options")

    font_options = ["Arial", "Verdana", "Times New Roman", "Courier New", "Georgia"]
    selected_font = st.sidebar.selectbox("Font", font_options)

    background_color = st.sidebar.color_picker("Background Color", "#ffffff")
    text_color = st.sidebar.color_picker("Text Color", "#000000")
    title_color = st.sidebar.color_picker("Title Color", "#333333")
    input_background_color = st.sidebar.color_picker("Input Background Color", "#f9f9f9")
    input_text_color = st.sidebar.color_picker("Input Text Color", "#000000")
    button_color = st.sidebar.color_picker("Button Color", "#4CAF50")
    button_text_color = st.sidebar.color_picker("Button Text Color", "#ffffff")
    button_hover_color = st.sidebar.color_picker("Button Hover Color", "#45a049")

    styling_options = {
        'font': selected_font,
        'background_color': background_color,
        'text_color': text_color,
        'title_color': title_color,
        'input_background_color': input_background_color,
        'input_text_color': input_text_color,
        'button_color': button_color,
        'button_text_color': button_text_color,
        'button_hover_color': button_hover_color
    }

    uploaded_file = st.file_uploader("Choose an XML file", type="xml")

    if uploaded_file is not None:
        try:
            xml_content = uploaded_file.read().decode("utf-8")
            form_data = parse_xml(xml_content)
            html_output = generate_html(form_data, styling_options)

            st.subheader("Generated HTML Form Preview")
            st.components.v1.html(html_output, height=600, scrolling=True)

            st.subheader("Download HTML")
            st.download_button(
                label="Download HTML",
                data=html_output,
                file_name="generated_form.html",
                mime="text/html"
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
