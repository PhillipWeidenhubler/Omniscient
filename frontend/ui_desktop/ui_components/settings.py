# ui_components/settings.py
import customtkinter as ctk
import json
import os
from tkinter import colorchooser, filedialog

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master, settings_file="settings.json", **kwargs):
        super().__init__(master, **kwargs)
        self.settings_file = settings_file
        self.settings = self.load_settings()
        self.build_ui()

    def load_settings(self):
        """
        Lädt die Einstellungen aus einer JSON-Datei.
        Falls diese nicht existieren oder ein Fehler auftritt, werden Standardwerte verwendet.
        """
        default_settings = {
            "appearance_mode": "Light",          # "Light" oder "Dark"
            "font_size": 14,
            "auto_complete_enabled": True,
            "show_advanced_filters": False,
            "custom_primary_color": "#0078D7",     # Default Primärfarbe
            "custom_accent_color": "#00B4FF",      # Default Akzentfarbe
            "auto_dark_mode": False,               # Automatische Dark/Light Umschaltung
            "selected_language": "de",             # z. B. "de" oder "en"
            "layout_spacing": 10,                  # Abstand (in Pixel) für das Layout
            "log_level": "INFO",                   # Log-Level: "INFO", "DEBUG", "ERROR"
            "notifications_enabled": True,
            "sound_enabled": True
        }
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    settings = json.load(f)
                    # Fehlende Schlüssel mit Standardwerten auffüllen
                    for key, value in default_settings.items():
                        if key not in settings:
                            settings[key] = value
                    return settings
            except Exception as e:
                print("Fehler beim Laden der Einstellungen:", e)
                return default_settings
        else:
            return default_settings

    def save_settings(self):
        """
        Speichert die aktuellen Einstellungen in der JSON-Datei.
        """
        try:
            with open(self.settings_file, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print("Fehler beim Speichern der Einstellungen:", e)

    def build_ui(self):
        """
        Baut die Benutzeroberfläche für die Einstellungen inklusive all der erweiterten Features auf.
        """
        self.grid_columnconfigure(0, weight=1)
        row = 0

        # Überschrift
        title_label = ctk.CTkLabel(self, text="Einstellungen", font=("Helvetica", 20, "bold"))
        title_label.grid(row=row, column=0, padx=20, pady=20, sticky="ew")
        row += 1

        # Erscheinungsbild (Dark/Light Mode)
        mode_label = ctk.CTkLabel(self, text="Erscheinungsbild:")
        mode_label.grid(row=row, column=0, sticky="w", padx=20, pady=(5, 0))
        row += 1
        self.appearance_var = ctk.StringVar(value=self.settings.get("appearance_mode", "Light"))
        self.mode_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark"],
            variable=self.appearance_var,
            command=self.change_appearance
        )
        self.mode_optionmenu.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Schriftgröße
        font_label = ctk.CTkLabel(self, text="Standard Schriftgröße:")
        font_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.font_slider = ctk.CTkSlider(self, from_=10, to=30, number_of_steps=21, command=self.update_font_size)
        self.font_slider.set(self.settings.get("font_size", 14))
        self.font_slider.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Autovervollständigung aktivieren
        self.auto_complete_var = ctk.BooleanVar(value=self.settings.get("auto_complete_enabled", True))
        self.autocomplete_checkbox = ctk.CTkCheckBox(
            self,
            text="Autovervollständigung aktivieren",
            variable=self.auto_complete_var,
            command=self.update_auto_complete
        )
        self.autocomplete_checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        row += 1

        # Erweiterte Filter anzeigen
        self.adv_filters_var = ctk.BooleanVar(value=self.settings.get("show_advanced_filters", False))
        self.adv_filters_checkbox = ctk.CTkCheckBox(
            self,
            text="Erweiterte Filter anzeigen",
            variable=self.adv_filters_var,
            command=self.update_adv_filters
        )
        self.adv_filters_checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        row += 1

        # Primärfarbe auswählen
        primary_color_label = ctk.CTkLabel(self, text="Primärfarbe:")
        primary_color_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.primary_color_button = ctk.CTkButton(
            self,
            text=f"Primärfarbe: {self.settings.get('custom_primary_color')}",
            command=self.choose_primary_color, 
            corner_radius=8
        )
        self.primary_color_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Akzentfarbe auswählen
        accent_color_label = ctk.CTkLabel(self, text="Akzentfarbe:")
        accent_color_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.accent_color_button = ctk.CTkButton(
            self,
            text=f"Akzentfarbe: {self.settings.get('custom_accent_color')}",
            command=self.choose_accent_color,
            corner_radius=8
        )
        self.accent_color_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Automatische Dark/Light Mode Umschaltung
        self.auto_mode_var = ctk.BooleanVar(value=self.settings.get("auto_dark_mode", False))
        self.auto_mode_checkbox = ctk.CTkCheckBox(
            self,
            text="Automatische Dark/Light Umschaltung aktivieren",
            variable=self.auto_mode_var,
            command=self.update_auto_mode
        )
        self.auto_mode_checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        row += 1

        # Sprachauswahl / Internationalisierung
        language_label = ctk.CTkLabel(self, text="Sprache:")
        language_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.language_var = ctk.StringVar(value=self.settings.get("selected_language", "de"))
        self.language_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["de", "en"],
            variable=self.language_var,
            command=self.update_language
        )
        self.language_optionmenu.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Layout Abstand
        spacing_label = ctk.CTkLabel(self, text="Layout Abstand (px):")
        spacing_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.layout_slider = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=31, command=self.update_layout_spacing)
        self.layout_slider.set(self.settings.get("layout_spacing", 10))
        self.layout_slider.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Log Level Auswahl
        log_level_label = ctk.CTkLabel(self, text="Log Level:")
        log_level_label.grid(row=row, column=0, sticky="w", padx=20, pady=(10, 0))
        row += 1
        self.log_level_var = ctk.StringVar(value=self.settings.get("log_level", "INFO"))
        self.log_level_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["INFO", "DEBUG", "ERROR"],
            variable=self.log_level_var,
            command=self.update_log_level
        )
        self.log_level_optionmenu.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Benachrichtigungen aktivieren
        self.notifications_var = ctk.BooleanVar(value=self.settings.get("notifications_enabled", True))
        self.notifications_checkbox = ctk.CTkCheckBox(
            self,
            text="Benachrichtigungen aktivieren",
            variable=self.notifications_var,
            command=self.update_notifications
        )
        self.notifications_checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        row += 1

        # Sound aktivieren
        self.sound_var = ctk.BooleanVar(value=self.settings.get("sound_enabled", True))
        self.sound_checkbox = ctk.CTkCheckBox(
            self,
            text="Sound aktivieren",
            variable=self.sound_var,
            command=self.update_sound
        )
        self.sound_checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        row += 1

        # Backup erstellen
        backup_button = ctk.CTkButton(self, text="Backup erstellen", command=self.backup_settings, corner_radius=8)
        backup_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Backup importieren
        restore_button = ctk.CTkButton(self, text="Backup importieren", command=self.restore_settings, corner_radius=8)
        restore_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Einstellungen speichern
        save_button = ctk.CTkButton(self, text="Einstellungen speichern", command=self.on_save, corner_radius=8)
        save_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

        # Einstellungen zurücksetzen
        reset_button = ctk.CTkButton(self, text="Einstellungen zurücksetzen", command=self.reset_settings, corner_radius=8)
        reset_button.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        row += 1

    # ------------------------- Callback-Methoden -------------------------
    def change_appearance(self, value):
        self.settings["appearance_mode"] = value
        ctk.set_appearance_mode(value)
        self.save_settings()

    def update_font_size(self, value):
        try:
            font_size = int(round(float(value)))
            self.settings["font_size"] = font_size
            self.save_settings()
        except Exception as e:
            print("Fehler beim Aktualisieren der Schriftgröße:", e)

    def update_auto_complete(self):
        self.settings["auto_complete_enabled"] = self.auto_complete_var.get()
        self.save_settings()

    def update_adv_filters(self):
        self.settings["show_advanced_filters"] = self.adv_filters_var.get()
        self.save_settings()

    def choose_primary_color(self):
        color = colorchooser.askcolor(title="Wähle Primärfarbe")
        if color[1]:
            self.settings["custom_primary_color"] = color[1]
            self.primary_color_button.configure(text=f"Primärfarbe: {color[1]}")
            self.save_settings()

    def choose_accent_color(self):
        color = colorchooser.askcolor(title="Wähle Akzentfarbe")
        if color[1]:
            self.settings["custom_accent_color"] = color[1]
            self.accent_color_button.configure(text=f"Akzentfarbe: {color[1]}")
            self.save_settings()

    def update_auto_mode(self):
        self.settings["auto_dark_mode"] = self.auto_mode_var.get()
        self.save_settings()

    def update_language(self, value):
        self.settings["selected_language"] = value
        self.save_settings()

    def update_layout_spacing(self, value):
        try:
            spacing = int(round(float(value)))
            self.settings["layout_spacing"] = spacing
            self.save_settings()
        except Exception as e:
            print("Fehler beim Aktualisieren des Layout-Abstands:", e)

    def update_log_level(self, value):
        self.settings["log_level"] = value
        self.save_settings()

    def update_notifications(self):
        self.settings["notifications_enabled"] = self.notifications_var.get()
        self.save_settings()

    def update_sound(self):
        self.settings["sound_enabled"] = self.sound_var.get()
        self.save_settings()

    def backup_settings(self):
        backup_file = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Dateien", "*.json")],
            title="Backup speichern"
        )
        if backup_file:
            try:
                with open(backup_file, "w", encoding="utf-8") as f:
                    json.dump(self.settings, f, indent=4)
                print("Backup erfolgreich erstellt.")
            except Exception as e:
                print("Fehler beim Erstellen des Backups:", e)

    def restore_settings(self):
        backup_file = filedialog.askopenfilename(
            filetypes=[("JSON Dateien", "*.json")],
            title="Backup importieren"
        )
        if backup_file:
            try:
                with open(backup_file, "r", encoding="utf-8") as f:
                    restored = json.load(f)
                self.settings = restored
                self.update_ui_from_settings()
                self.save_settings()
                print("Einstellungen wurden wiederhergestellt.")
            except Exception as e:
                print("Fehler beim Wiederherstellen der Einstellungen:", e)

    def reset_settings(self):
        # Zurücksetzen auf Standardwerte
        self.settings = {
            "appearance_mode": "Light",
            "font_size": 14,
            "auto_complete_enabled": True,
            "show_advanced_filters": False,
            "custom_primary_color": "#0078D7",
            "custom_accent_color": "#00B4FF",
            "auto_dark_mode": False,
            "selected_language": "de",
            "layout_spacing": 10,
            "log_level": "INFO",
            "notifications_enabled": True,
            "sound_enabled": True
        }
        self.update_ui_from_settings()
        self.save_settings()

    def on_save(self):
        self.save_settings()
        print("Einstellungen wurden gespeichert.")

    def update_ui_from_settings(self):
        """
        Aktualisiert alle UI-Elemente mit den aktuellen Einstellungen.
        """
        self.appearance_var.set(self.settings.get("appearance_mode", "Light"))
        self.mode_optionmenu.set(self.settings.get("appearance_mode", "Light"))
        self.font_slider.set(self.settings.get("font_size", 14))
        self.auto_complete_var.set(self.settings.get("auto_complete_enabled", True))
        self.adv_filters_var.set(self.settings.get("show_advanced_filters", False))
        self.primary_color_button.configure(text=f"Primärfarbe: {self.settings.get('custom_primary_color')}")
        self.accent_color_button.configure(text=f"Akzentfarbe: {self.settings.get('custom_accent_color')}")
        self.auto_mode_var.set(self.settings.get("auto_dark_mode", False))
        self.language_var.set(self.settings.get("selected_language", "de"))
        self.language_optionmenu.set(self.settings.get("selected_language", "de"))
        self.layout_slider.set(self.settings.get("layout_spacing", 10))
        self.log_level_var.set(self.settings.get("log_level", "INFO"))
        self.log_level_optionmenu.set(self.settings.get("log_level", "INFO"))
        self.notifications_var.set(self.settings.get("notifications_enabled", True))
        self.sound_var.set(self.settings.get("sound_enabled", True))

# ------------------------- Test / Beispiel -------------------------
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Einstellungen")
    app.geometry("600x900")
    settings_frame = SettingsFrame(app)
    settings_frame.pack(fill="both", expand=True)
    app.mainloop()