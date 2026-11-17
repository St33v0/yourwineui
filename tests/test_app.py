from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"

INPUT_LABELS = [
    "Fixed Acidity",
    "Volatile Acidity",
    "Citric Acid",
    "Residual Sugar",
    "Free Sulfur Dioxide",
    "Total Sulfur Dioxide",
    "Chlorides",
    "Density",
    "Sulphates",
    "pH",
    "Alcohol",
]

SLIDER_LABELS = [
    "Fixed Acidity",
    "Volatile Acidity",
    "Citric Acidity",
    "Residual Sugar",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "chlorides",
    "density",
    "sulphates",
    "pH",
    "Alcohol",
]


def test_markdown_texts():
    """Check the text content on the main page."""
    at = AppTest.from_file(str(APP_PATH)).run()

    assert at.markdown[0].value == "# Wine Quality Prediction App 🍷🍇"
    assert at.markdown[2].value == "### **Select Mode:**"


def test_selectbox_options():
    """Check the available input modes."""
    at = AppTest.from_file(str(APP_PATH)).run()

    assert at.selectbox[0].options == ["Choose", "Input version", "Slider version"]


def test_input_version_features():
    """Check all chemical inputs in input mode."""
    at = AppTest.from_file(str(APP_PATH)).run()
    at.selectbox[0].set_value("Input version").run()

    assert [widget.label for widget in at.number_input] == INPUT_LABELS
    assert [button.label for button in at.button] == ["Predict"]
    assert at.button[0].value is False


def test_slider_version_features():
    """Check all chemical sliders in slider mode."""
    at = AppTest.from_file(str(APP_PATH)).run()
    at.selectbox[0].set_value("Slider version").run()

    assert [widget.label for widget in at.slider] == SLIDER_LABELS
    assert [button.label for button in at.button] == ["Predict"]


def test_predict_button_initial_status():
    """Check that the prediction button is available but not clicked."""
    at = AppTest.from_file(str(APP_PATH)).run()
    at.selectbox[0].set_value("Input version").run()

    assert at.button[0].value is False
