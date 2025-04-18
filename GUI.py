import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QHBoxLayout, QScrollArea, QSplitter, QFrame, 
                            QMessageBox, QDialog, QTextEdit, QStackedWidget)
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import visualization as vis

class CollapsibleSection(QWidget):
    def __init__(self, title, parent=None):
        super(CollapsibleSection, self).__init__(parent)
        self.setObjectName("CollapsibleSection")
        
        self.secondary_color = "#2c3e50"
        self.text_color = "#ecf0f1"
        self.hover_color = "#34495e"
        
        self.setStyleSheet(f"""
            #CollapsibleSection {{
                background-color: {self.secondary_color};
                color: {self.text_color};
                border: none;
            }}
            QPushButton {{
                color: {self.text_color};
                background-color: {self.secondary_color};
                border: none;
                padding: 8px;
                text-align: left;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.hover_color};
            }}
        """)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)        
        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(10, 5, 10, 5)        
        self.title_button = QPushButton(title)
        self.title_button.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.title_button.setCursor(Qt.PointingHandCursor)
        self.title_button.clicked.connect(self.toggle_content)
        self.toggle_button = QPushButton("▼")
        self.toggle_button.setFixedWidth(24)
        self.toggle_button.setFont(QFont("Segoe UI", 10))
        self.toggle_button.setCursor(Qt.PointingHandCursor)
        self.toggle_button.clicked.connect(self.toggle_content)
        self.header_layout.addWidget(self.title_button)
        self.header_layout.addWidget(self.toggle_button)
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(10, 5, 10, 5)
        self.content_layout.setSpacing(5)
        self.content_widget.setStyleSheet(f"background-color: {self.secondary_color};")        
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.separator.setStyleSheet(f"background-color: #34495e; max-height: 1px;")        
        self.layout.addLayout(self.header_layout)
        self.layout.addWidget(self.content_widget)
        self.layout.addWidget(self.separator)        
        self.is_expanded = True
    
    def toggle_content(self):
        self.is_expanded = not self.is_expanded
        self.content_widget.setVisible(self.is_expanded)
        self.toggle_button.setText("▼" if self.is_expanded else "►")
    
    def add_button(self, text, callback):
        button = QPushButton(text)
        button.setFont(QFont("Segoe UI", 10))
        button.setCursor(Qt.PointingHandCursor)
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: #ecf0f1;
                border: none;
                padding: 8px;
                border-radius: 4px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1a5276;
            }
        """)
        button.clicked.connect(callback)
        self.content_layout.addWidget(button)
        return button

class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super(HelpDialog, self).__init__(parent)
        self.setWindowTitle("Help Documentation")
        self.setMinimumSize(600, 400)
        self.setStyleSheet("background-color: #f5f7fa;")
        
        layout = QVBoxLayout(self)        
        header = QLabel("Healthviz Visualizer Help Guide")
        header.setFont(QFont("Segoe UI", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        help_text = QTextEdit()
        help_text.setReadOnly(True)
        help_text.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 10px;
                font-family: 'Segoe UI';
                font-size: 11pt;
            }
        """)
        
        help_content = """
<h2>Healthviz Visualizer Help Guide</h2>

<h3>1. Navigation:</h3>
<ul>
    <li>Select visualizations from the categorized sidebar</li>
    <li>Toggle sidebar visibility with the ≡ button</li>
    <li>Collapse/expand categories by clicking the category headers</li>
    <li>Use the visualization toolbar to interact with plots (zoom, pan, save)</li>
</ul>

<h3>2. Visualization Categories:</h3>
<ul>
    <li><b>Basic Distributions:</b> Univariate analysis</li>
    <li><b>Comparative Analysis:</b> Group comparisons</li>
    <li><b>Correlation Analysis:</b> Relationship matrices</li>
    <li><b>Multivariate Analysis:</b> Multiple variable relationships</li>
    <li><b>Advanced Visualizations:</b> Complex representations</li>
</ul>

<h3>3. Tips:</h3>
<ul>
    <li>Hover over data points in some visualizations for details</li>
    <li>Use the save button to export visualizations</li>
    <li>Larger datasets may take longer to render</li>
    <li>Right-click on the visualization for additional options</li>
</ul>
        """
        
        help_text.setHtml(help_content)
        layout.addWidget(help_text)
        
        close_button = QPushButton("Close")
        close_button.setFont(QFont("Segoe UI", 10))
        close_button.setCursor(Qt.PointingHandCursor)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)

class HealthvizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.primary_color = "#3498db"
        self.secondary_color = "#2c3e50"
        self.accent_color = "#e74c3c"
        self.text_color = "#ecf0f1"
        self.light_bg = "#f5f7fa"
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Healthviz Visualizer")
        self.setMinimumSize(1000, 750)
        self.setStyleSheet(f"background-color: {self.light_bg};")
        
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setCentralWidget(central_widget)
        
        self.create_header(main_layout)
        
        self.create_main_content(main_layout)
        
        self.create_footer(main_layout)
        
        self.show_empty_state()
        
        self.show()
    
    def create_header(self, parent_layout):
        header = QWidget()
        header.setStyleSheet(f"""
            background-color: {self.secondary_color};
            color: {self.text_color};
            padding: 10px;
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 10, 15, 10)
        
        logo_label = QLabel("📊")
        logo_label.setFont(QFont("Segoe UI", 24))
        logo_label.setStyleSheet(f"color: {self.text_color};")
        
        title_label = QLabel("Advanced AI Data Visualizer")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title_label.setStyleSheet(f"color: {self.text_color};")
        
        header_layout.addWidget(logo_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        self.toggle_btn = QPushButton("≡")
        self.toggle_btn.setFont(QFont("Segoe UI", 14))
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.setFixedSize(40, 40)
        self.toggle_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.accent_color};
                color: {self.text_color};
                border: none;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: #c0392b;
            }}
        """)
        self.toggle_btn.clicked.connect(self.toggle_sidebar)
        
        header_layout.addWidget(self.toggle_btn)
        parent_layout.addWidget(header)
    
    def create_main_content(self, parent_layout):
        self.main_splitter = QSplitter(Qt.Horizontal)
        
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(300)
        self.sidebar.setStyleSheet(f"background-color: {self.secondary_color};")
        
        sidebar_scroll = QScrollArea()
        sidebar_scroll.setWidgetResizable(True)
        sidebar_scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #34495e;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #3498db;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
        sidebar_content = QWidget()
        self.sidebar_layout = QVBoxLayout(sidebar_content)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)
        
        self.create_sidebar_categories(self.sidebar_layout)
        
        self.sidebar_layout.addStretch()
        
        sidebar_scroll.setWidget(sidebar_content)
        
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.addWidget(sidebar_scroll)
        
        self.viz_panel = QWidget()
        self.viz_panel.setStyleSheet("background-color: white;")
        self.viz_layout = QVBoxLayout(self.viz_panel)
        
        self.main_splitter.addWidget(self.sidebar)
        self.main_splitter.addWidget(self.viz_panel)
        self.main_splitter.setStretchFactor(0, 0) 
        self.main_splitter.setStretchFactor(1, 1)  
        
        parent_layout.addWidget(self.main_splitter)
        
        self.viz_stack = QStackedWidget()
        self.viz_layout.addWidget(self.viz_stack)
        
        self.empty_state = QWidget()
        empty_layout = QVBoxLayout(self.empty_state)
        empty_layout.setAlignment(Qt.AlignCenter)
        
        empty_label = QLabel("Select a visualization from the sidebar to begin")
        empty_label.setFont(QFont("Segoe UI", 14))
        empty_label.setStyleSheet("color: #6c757d;")
        empty_label.setAlignment(Qt.AlignCenter)
        
        empty_layout.addWidget(empty_label)
        self.viz_stack.addWidget(self.empty_state)
        
        self.viz_widget = QWidget()
        self.viz_widget_layout = QVBoxLayout(self.viz_widget)
        self.viz_stack.addWidget(self.viz_widget)
    
    def create_sidebar_categories(self, parent_layout):
        categories = {
            "Basic Distributions": [
                ("Age Distribution", lambda: self.show_visualization(vis.plot_age_distribution)),
                ("BMI Distribution", lambda: self.show_visualization(vis.plot_bmi_distribution)),
                ("Sleep Distribution", lambda: self.show_visualization(vis.plot_sleep_distribution))
            ],
            "Comparative Analysis": [
                ("BMI by Gender", lambda: self.show_visualization(vis.plot_bmi_by_gender)),
                ("Exercise by Smoker", lambda: self.show_visualization(vis.plot_exercise_by_smoker)),
                ("BMI vs Smoker by Gender", lambda: self.show_visualization(vis.plot_bmi_vs_smoker_by_gender)),
                ("Alcohol by Gender", lambda: self.show_visualization(vis.plot_alcohol_kde_by_gender))
            ],
            "Correlation Analysis": [
                ("Heatmap", lambda: self.show_visualization(vis.plot_heatmap)),
                ("Advanced Correlation", lambda: self.show_visualization(vis.plot_advanced_correlation_heatmap)),
                ("Clustermap", lambda: self.show_visualization(vis.plot_clustermap))
            ],
            "Multivariate Analysis": [
                ("Steps vs BMI", lambda: self.show_visualization(vis.plot_steps_vs_bmi)),
                ("BMI vs Age", lambda: self.show_visualization(vis.plot_bmi_vs_age)),
                ("Alcohol vs Heart Rate", lambda: self.show_visualization(vis.plot_alcohol_vs_heart_rate))
            ],
            "Advanced Visualizations": [
                ("FacetGrid Steps vs BMI", lambda: self.show_visualization(vis.plot_facetgrid_steps_vs_bmi)),
                ("Radar Chart", lambda: self.show_visualization(vis.plot_radar_chart)),
                ("Health Dashboard", lambda: self.show_visualization(vis.plot_health_dashboard)),
                ("Sunburst Chart", lambda: self.show_visualization(vis.plot_sunburst))
            ]
        }
        
        for category, buttons in categories.items():
            section = CollapsibleSection(category)
            
            for button_text, callback in buttons:
                section.add_button(button_text, callback)
            
            parent_layout.addWidget(section)
    
    def create_footer(self, parent_layout):
        footer = QWidget()
        footer.setStyleSheet(f"""
            background-color: {self.secondary_color};
            color: {self.text_color};
        """)
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(15, 8, 15, 8)
        
        version_label = QLabel("AI Visualizer v1.0")
        version_label.setFont(QFont("Segoe UI", 8))
        version_label.setStyleSheet(f"color: {self.text_color};")
        
        footer_layout.addWidget(version_label)
        footer_layout.addStretch()
        
        help_button = QPushButton("Help")
        help_button.setFont(QFont("Segoe UI", 10))
        help_button.setCursor(Qt.PointingHandCursor)
        help_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.primary_color};
                color: {self.text_color};
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
        """)
        help_button.clicked.connect(self.show_help)
        
        exit_button = QPushButton("Exit")
        exit_button.setFont(QFont("Segoe UI", 10))
        exit_button.setCursor(Qt.PointingHandCursor)
        exit_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.primary_color};
                color: {self.text_color};
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
        """)
        exit_button.clicked.connect(self.close_application)
        
        footer_layout.addWidget(help_button)
        footer_layout.addWidget(exit_button)
        
        parent_layout.addWidget(footer)
    
    def show_empty_state(self):
        self.viz_stack.setCurrentWidget(self.empty_state)
    
    def show_visualization(self, viz_function):
        try:
            while self.viz_widget_layout.count():
                item = self.viz_widget_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            fig = viz_function()
            
            canvas = FigureCanvas(fig)
            self.viz_widget_layout.addWidget(canvas)
            
            toolbar = NavigationToolbar(canvas, self.viz_widget)
            self.viz_widget_layout.addWidget(toolbar)
            
            self.viz_stack.setCurrentWidget(self.viz_widget)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate visualization:\n{str(e)}")
            self.show_empty_state()
    
    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide()
            self.toggle_btn.setText("≡")
        else:
            self.sidebar.show()
            self.toggle_btn.setText("◀")
    
    def show_help(self):
        help_dialog = HelpDialog(self)
        help_dialog.exec_()
    
    def close_application(self):
            self.close()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Exit", 
                                    "Are you sure you want to exit the application?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#f5f7fa"))
    palette.setColor(QPalette.WindowText, QColor("#2c3e50"))
    palette.setColor(QPalette.Base, QColor("#ffffff"))
    palette.setColor(QPalette.AlternateBase, QColor("#f5f7fa"))
    palette.setColor(QPalette.Button, QColor("#3498db"))
    palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
    palette.setColor(QPalette.Link, QColor("#3498db"))
    app.setPalette(palette)
    
    window = HealthvizApp()
    sys.exit(app.exec_())

