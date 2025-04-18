import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import visualization as vis
from PIL import Image, ImageTk
import webbrowser

class AIVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthviz visualizer")
        self.root.geometry("1000x750")
        self.root.configure(bg="#2c3e50")
        self.root.minsize(800, 600)
        
        self.sidebar_visible = True
        self.primary_color = "#3498db"
        self.secondary_color = "#2c3e50"
        self.accent_color = "#e74c3c"
        self.text_color = "#ecf0f1"
        self.light_bg = "#f5f7fa"
        
        self.setup_styles()
        self.setup_header()
        self.setup_main_container()
        self.setup_visualization_panel()
        self.setup_sidebar()
        self.setup_footer()
        
        self.current_viz_frame = None
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('TButton', 
                       font=('Segoe UI', 10), 
                       padding=6,
                       relief='flat',
                       background=self.primary_color,
                       foreground=self.text_color)
                       
        style.map('TButton',
                 foreground=[('pressed', self.text_color), ('active', self.text_color)],
                 background=[('pressed', '#297fb8'), ('active', '#1a5276')])
        
        style.configure('Toggle.TButton', 
                       font=('Segoe UI', 10),
                       padding=4,
                       relief='flat',
                       background=self.accent_color)
                       
        style.map('Toggle.TButton',
                 foreground=[('pressed', self.text_color), ('active', self.text_color)],
                 background=[('pressed', '#c0392b'), ('active', '#e74c3c')])
        
        style.configure('Header.TLabel', 
                      font=('Segoe UI', 24, 'bold'), 
                      background=self.secondary_color,
                      foreground=self.text_color)
        
        style.configure('Panel.TLabelframe', 
                      font=('Segoe UI', 12, 'bold'), 
                      background='#ffffff',
                      foreground='#495057')
        
        style.configure('Viz.TFrame',
                      background='#ffffff',
                      borderwidth=2,
                      relief='sunken')
                      
        style.configure('Category.TButton',
                      font=('Segoe UI', 10),
                      padding=6,
                      relief='flat',
                      background='#34495e',
                      foreground=self.text_color)
                      
        style.map('Category.TButton',
                 foreground=[('pressed', self.text_color), ('active', self.text_color)],
                 background=[('pressed', '#2c3e50'), ('active', '#2c3e50')])
                 
        style.configure('Sidebar.TFrame', background=self.secondary_color)
        style.configure('Main.TFrame', background='#ffffff')
        style.configure('Footer.TFrame', background=self.secondary_color)
        style.configure('Header.TFrame', background=self.secondary_color)
        
        style.configure('CategoryTitle.TLabel',
                      font=('Segoe UI', 11, 'bold'),
                      background=self.secondary_color,
                      foreground=self.text_color)
    
    def setup_header(self):
        header_frame = ttk.Frame(self.root, style='Header.TFrame')
        header_frame.pack(fill=tk.X)
        
        self.logo_label = ttk.Label(header_frame, text="📊", font=('Segoe UI', 24),
                                  background=self.secondary_color,
                                  foreground=self.text_color)
        self.logo_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.header = ttk.Label(header_frame, text="Advanced AI Data Visualizer", 
                              style='Header.TLabel')
        self.header.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.toggle_sidebar_btn = ttk.Button(header_frame, text="≡", 
                                          command=self.toggle_sidebar,
                                          style='Toggle.TButton',
                                          width=3)
        self.toggle_sidebar_btn.pack(side=tk.RIGHT, padx=15, pady=10)
    
    def setup_main_container(self):
        self.main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar_panel = ttk.Frame(self.main_container, style='Sidebar.TFrame', width=250)
        self.viz_panel = ttk.Frame(self.main_container, style='Main.TFrame')
        
        self.main_container.add(self.sidebar_panel, weight=1)
        self.main_container.add(self.viz_panel, weight=3)
    
    def setup_sidebar(self):
        self.sidebar_canvas = tk.Canvas(self.sidebar_panel, bg=self.secondary_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.sidebar_panel, orient="vertical", command=self.sidebar_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.sidebar_canvas, style='Sidebar.TFrame')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.sidebar_canvas.configure(scrollregion=self.sidebar_canvas.bbox("all")))
        
        self.sidebar_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=230)
        self.sidebar_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.sidebar_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        categories = {
            "Basic Distributions": [
                ("Age Distribution", vis.plot_age_distribution),
                ("BMI Distribution", vis.plot_bmi_distribution),
                ("Sleep Distribution", vis.plot_sleep_distribution)
            ],
            "Comparative Analysis": [
                ("BMI by Gender", vis.plot_bmi_by_gender),
                ("Exercise by Smoker", vis.plot_exercise_by_smoker),
                ("BMI vs Smoker by Gender", vis.plot_bmi_vs_smoker_by_gender),
                ("Alcohol by Gender", vis.plot_alcohol_kde_by_gender)
            ],
            "Correlation Analysis": [
                ("Heatmap", vis.plot_heatmap),
                ("Advanced Correlation", vis.plot_advanced_correlation_heatmap),
                ("Clustermap", vis.plot_clustermap)
            ],
            "Multivariate Analysis": [
                ("Steps vs BMI", vis.plot_steps_vs_bmi),
                ("BMI vs Age", vis.plot_bmi_vs_age),
                ("Alcohol vs Heart Rate", vis.plot_alcohol_vs_heart_rate)
            ],
            "Advanced Visualizations": [
                ("FacetGrid Steps vs BMI", vis.plot_facetgrid_steps_vs_bmi),
                ("Radar Chart", vis.plot_radar_chart),
                ("Health Dashboard", vis.plot_health_dashboard),
                ("Sunburst Chart", vis.plot_sunburst)
            ]
        }
        
        self.category_frames = {}
        
        row = 0
        for category, buttons in categories.items():
            category_frame = ttk.Frame(self.scrollable_frame, style='Sidebar.TFrame')
            category_frame.grid(row=row, column=0, sticky='ew', padx=5)
            row += 1
            
            category_header = ttk.Frame(category_frame, style='Sidebar.TFrame')
            category_header.pack(fill='x')
            
            cat_label = ttk.Label(category_header, text=category, style='CategoryTitle.TLabel')
            cat_label.pack(side='left', pady=(15, 5), padx=5)
            
            toggle_btn = ttk.Button(category_header, text="▼", width=2, 
                                  command=lambda c=category: self.toggle_category(c),
                                  style='Toggle.TButton')
            toggle_btn.pack(side='right', pady=(15, 5), padx=5)
            
            content_frame = ttk.Frame(category_frame, style='Sidebar.TFrame')
            content_frame.pack(fill='x')
            
            self.category_frames[category] = (content_frame, toggle_btn)
            
            for text, command in buttons:
                btn_frame = ttk.Frame(content_frame, style='Sidebar.TFrame')
                btn_frame.pack(fill='x', pady=2)
                
                btn = ttk.Button(btn_frame, text=text, 
                               command=lambda cmd=command: self.show_visualization(cmd),
                               style='TButton')
                btn.pack(fill='x', padx=10)
            
            if category != list(categories.keys())[-1]:
                ttk.Separator(self.scrollable_frame, orient='horizontal').grid(
                    row=row, column=0, pady=5, sticky='ew', padx=10)
                row += 1
    
    def toggle_category(self, category):
        content_frame, toggle_btn = self.category_frames[category]
        
        if content_frame.winfo_viewable():
            content_frame.pack_forget()
            toggle_btn.configure(text="►")
        else:
            content_frame.pack(fill='x')
            toggle_btn.configure(text="▼")
            
        self.sidebar_canvas.configure(scrollregion=self.sidebar_canvas.bbox("all"))
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.main_container.forget(self.sidebar_panel)
            self.toggle_sidebar_btn.configure(text="≡")
            self.sidebar_visible = False
        else:
            self.main_container.insert(0, self.sidebar_panel, weight=1)
            self.toggle_sidebar_btn.configure(text="◀")
            self.sidebar_visible = True
    
    def setup_visualization_panel(self):
        self.viz_empty_label = ttk.Label(
            self.viz_panel, 
            text="Select a visualization from the sidebar to begin",
            font=('Segoe UI', 12),
            background='#ffffff',
            foreground='#6c757d'
        )
        self.viz_empty_label.pack(expand=True)
        
        self.viz_canvas_frame = None
        self.toolbar_frame = None
    
    def show_visualization(self, viz_function):
        if self.current_viz_frame:
            self.current_viz_frame.destroy()
        if self.toolbar_frame:
            self.toolbar_frame.destroy()
        if self.viz_empty_label.winfo_ismapped():
            self.viz_empty_label.pack_forget()
        
        try:
            self.current_viz_frame = ttk.Frame(self.viz_panel)
            self.current_viz_frame.pack(fill=tk.BOTH, expand=True)
            
            fig = viz_function()
            
            canvas = FigureCanvasTkAgg(fig, master=self.current_viz_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            self.toolbar_frame = ttk.Frame(self.viz_panel)
            self.toolbar_frame.pack(fill=tk.X)
            toolbar = NavigationToolbar2Tk(canvas, self.toolbar_frame)
            toolbar.update()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate visualization:\n{str(e)}")
            if self.current_viz_frame:
                self.current_viz_frame.destroy()
            self.viz_empty_label.pack(expand=True)
    
    def setup_footer(self):
        footer_frame = ttk.Frame(self.root, style='Footer.TFrame')
        footer_frame.pack(fill=tk.X)
        
        exit_btn = ttk.Button(footer_frame, text="Exit", command=self.on_exit,
                            style='TButton')
        exit_btn.pack(side=tk.RIGHT, padx=10, pady=8)
        
        docs_btn = ttk.Button(footer_frame, text="Help", command=self.show_help,
                            style='TButton')
        docs_btn.pack(side=tk.RIGHT, padx=5, pady=8)
        
        version_label = ttk.Label(footer_frame, text="AI Visualizer v1.0",
                                font=('Segoe UI', 8),
                                foreground=self.text_color,
                                background=self.secondary_color)
        version_label.pack(side=tk.LEFT, padx=10, pady=8)
    
    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help Documentation")
        help_window.geometry("600x400")
        help_window.configure(bg=self.light_bg)
        
        help_frame = ttk.Frame(help_window)
        help_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        help_header = ttk.Label(help_frame, text="AI Data Visualizer Help Guide", 
                             font=('Segoe UI', 16, 'bold'),
                             background=self.light_bg)
        help_header.pack(pady=10)
        
        text = tk.Text(help_frame, wrap=tk.WORD, padx=10, pady=10,
                     font=('Segoe UI', 10),
                     background=self.light_bg,
                     borderwidth=0)
        text.pack(fill=tk.BOTH, expand=True)
        
        help_text = """Healthviz Visualizer Help Guide

1. Navigation:
- Select visualizations from the categorized sidebar
- Toggle sidebar visibility with the ≡ button
- Collapse/expand categories by clicking ▼/► buttons
- Use the toolbar to interact with plots (zoom, pan, save)

2. Visualization Categories:
- Basic Distributions: Univariate analysis
- Comparative Analysis: Group comparisons
- Correlation Analysis: Relationship matrices
- Multivariate Analysis: Multiple variable relationships
- Advanced Visualizations: Complex representations

3. Tips:
- Hover over data points in some visualizations for details
- Use the save button to export visualizations
- Larger datasets may take longer to render
"""
        text.insert(tk.END, help_text)
        text.config(state=tk.DISABLED)
        
        close_btn = ttk.Button(help_frame, text="Close", 
                             command=help_window.destroy,
                             style='TButton')
        close_btn.pack(pady=10)
    
    def on_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit the application?"):
            self.root.quit()

