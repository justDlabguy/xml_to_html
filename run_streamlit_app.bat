@echo off
:: This batch file runs the Streamlit app for XML to HTML form conversion.

:: Set the directory where your script is located (update this path)
set SCRIPT_DIR=C:\Users\USER\Documents\Medplum\xml_to_html

:: Navigate to the script directory
cd /d "%SCRIPT_DIR%"

:: Run the Streamlit app
streamlit run xml_html.py

:: Pause to keep the command prompt open (optional)
pause
