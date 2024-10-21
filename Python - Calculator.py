import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #080808;")
        
        # Create a vertical layout for the calculator display and buttons
        self.layout = QVBoxLayout()
        
        # Calculator display (QLineEdit)
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 24))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)  # Only output displayed
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("background-color: white; color: black; border-radius: 10px; padding: 10px;")
        self.layout.addWidget(self.display)
        
        # Button layout (QGridLayout)
        self.buttonLayout = QGridLayout()

        # Button labels
        buttons = ['(', ')', 'C', '←', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        # Add buttons to grid layout
        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(80, 80)
            btn.setFont(QFont("Arial", 18))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #393939;  /* Blue color */
                    border: none;
                    border-radius: 10px;
                    color: white;
                }
                QPushButton:pressed {
                    background-color: #6b6b6b;  /* Darker blue when pressed */
                }
            """)

            self.buttonLayout.addWidget(btn, row, col, 1, 1)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
            # Connect the button clicks to the method
            btn.clicked.connect(self.on_button_clicked)

        self.layout.addLayout(self.buttonLayout)

        # Set the layout to the main window
        self.setLayout(self.layout)

    def on_button_clicked(self):
        button = self.sender().text()
        
        # If clear (C) button is pressed, reset display
        if button == 'C':
            self.display.setText('')
        # If backspace (←) button is pressed, remove last character
        elif button == '←':
            current_text = self.display.text()[:-1]
            self.display.setText(current_text)
        # If equals (=) button is pressed, it calculates the problem
        elif button == '=':
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        # Otherwise, update the display with the pressed button's text
        else:
            current_text = self.display.text()
            self.display.setText(current_text + button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
