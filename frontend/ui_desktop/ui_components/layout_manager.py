import customtkinter as ctk

def create_main_layout(root):
    """
    Creates and returns a main layout frame for the application.

    The layout is divided into three sections:
      - Header: A top section for the application title or navigation.
      - Sidebar: A left-side panel for navigation or auxiliary controls.
      - Content: The main area for displaying dynamic content.

    Args:
        root (ctk.CTk): The main application window.

    Returns:
        dict: A dictionary containing the created frames with keys:
              'main_frame', 'header', 'sidebar', and 'content'.
    """
    # Create the main frame that fills the entire window with some padding.
    main_frame = ctk.CTkFrame(root, corner_radius=8)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Configure grid layout for the main frame.
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Header: occupies the top row spanning both columns.
    header = ctk.CTkFrame(main_frame, height=60, corner_radius=8)
    header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    header_label = ctk.CTkLabel(header, text="Application Header", font=("Arial", 20, "bold"))
    header_label.pack(side="left", padx=20, pady=10)

    # Sidebar: located in the left column of the second row.
    sidebar = ctk.CTkFrame(main_frame, width=200, corner_radius=8)
    sidebar.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    sidebar_label = ctk.CTkLabel(sidebar, text="Sidebar", font=("Arial", 14))
    sidebar_label.pack(padx=10, pady=10)

    # Content: the remaining space to the right.
    content = ctk.CTkFrame(main_frame, corner_radius=8)
    content.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    content_label = ctk.CTkLabel(content, text="Main Content Area", font=("Arial", 16))
    content_label.pack(padx=10, pady=10)

    return {
        "main_frame": main_frame,
        "header": header,
        "sidebar": sidebar,
        "content": content
    }

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1200x800")

    # Create and retrieve the layout sections.
    layout = create_main_layout(app)

    # You can later use layout["header"], layout["sidebar"], or layout["content"]
    # to add more widgets to those regions.

    app.mainloop()