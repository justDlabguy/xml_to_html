# XML to HTML Form Converter

Convert XML configuration files into interactive HTML forms with custom styling using this Streamlit app.

---

## Features

- **Upload XML**: Drag and drop your XML configuration file.
- **Preview Form**: Instantly see a live preview of the generated HTML form.
- **Custom Styling**: Personalize fonts, colors, and more using the sidebar.
- **Download HTML**: Save the generated form as an HTML file.

---

## Setup

### Prerequisites

- Python 3.6 or later
- `pip` for installing dependencies

### Installation

1. **Clone the Repository** (if applicable) or download the script:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit jinja2
   ```

---

## Usage

1. **Run the App**:
   ```bash
   streamlit run xml_to_html_streamlit.py in terminal 
   or
  open  `run_streamlit_app.bat` in file_explorer
   ```

2. **Upload XML**:
   - Use the file uploader to select your XML configuration file.

3. **Customize Styling** (Optional):
   - Use the sidebar to change fonts, colors, and other styling options.

4. **Preview and Download**:
   - Preview the generated form in the app.
   - Click the "Download HTML" button to save the form as an HTML file.

---

## XML Configuration Guide

Your XML file should follow this structure:

```xml
<form>
    <title>Form Title</title>
    <description>Form Description</description>

    <field>
        <type>text</type>
        <name>field_name</name>
        <label>Field Label</label>
        <required>true</required>
        <placeholder>Enter text here</placeholder>
    </field>

    <!-- Add more fields as needed -->

    <submit>
        <label>Submit Button Text</label>
    </submit>
</form>
```

### Supported Field Types

- `text`: Text input
- `email`: Email input
- `password`: Password input
- `select`: Dropdown menu
- `checkbox`: Checkbox
- `radio`: Radio buttons
- `textarea`: Text area

---

## Styling Options

Customize the appearance of your form using the sidebar:

- **Font**: Choose from Arial, Verdana, Times New Roman, Courier New, or Georgia.
- **Background Color**: Set the background color of the form.
- **Text Color**: Set the color of the text.
- **Title Color**: Set the color of the form title.
- **Input Background Color**: Set the background color of input fields.
- **Input Text Color**: Set the color of text inside input fields.
- **Button Color**: Set the color of the submit button.
- **Button Text Color**: Set the color of the button text.
- **Button Hover Color**: Set the color of the button when hovered.

---

## Example XML

```xml
<form>
    <title>User Registration</title>
    <description>Please fill out this form to register.</description>

    <field>
        <type>text</type>
        <name>full_name</name>
        <label>Full Name</label>
        <required>true</required>
        <placeholder>Enter your full name</placeholder>
    </field>

    <field>
        <type>email</type>
        <name>email</name>
        <label>Email Address</label>
        <required>true</required>
        <placeholder>Enter your email</placeholder>
    </field>

    <submit>
        <label>Register</label>
    </submit>
</form>
```

---

## Troubleshooting

- **Error: "text is not a known attribute of None"**: Ensure your XML file has all required fields (e.g., `title`, `description`, `submit/label`).
- **Preview Not Showing**: Make sure your XML is valid and the app is running without errors.
- **Styling Not Applied**: Double-check the color pickers and font selection in the sidebar.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Support

For questions or issues, please contact [your contact information] or open an issue on the repository.