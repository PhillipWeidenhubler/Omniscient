# ui_components/geolocation.py
import customtkinter as ctk
import logging
import requests
import ipaddress
import re
import webbrowser
import io
from PIL import Image, ImageTk

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def get_public_ip():
    """
    Ermittelt die öffentliche IP-Adresse, z. B. über ipify.org.
    """
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print("Fehler beim Abrufen der öffentlichen IP:", e)
        return None

def get_geolocation(ip):
    """
    Ruft Standortinformationen für die angegebene IP-Adresse von ipinfo.io ab.
    """
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Fehler beim Abrufen der Geolokation:", e)
        return None

class GeolocationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.current_coordinates = None  # Für die Kartenansicht (IP-Lookup)

        self.grid_columnconfigure(1, weight=1)

        # Titel
        title = ctk.CTkLabel(self, text="Geolocation & Netzwerk-Suche", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 5), sticky="w")

        # Auswahl des Suchtyps
        type_label = ctk.CTkLabel(self, text="Suchtyp:")
        type_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.lookup_type_menu = ctk.CTkOptionMenu(self, 
                                                  values=["IP (v4/v6)", "Öffentliche IP (automatisch)", "MAC", "Netzwerkbereich"])
        self.lookup_type_menu.set("IP (v4/v6)")
        self.lookup_type_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Eingabefeld
        query_label = ctk.CTkLabel(self, text="Eingabe:")
        query_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.query_entry = ctk.CTkEntry(self)
        self.query_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Buttons: Lookup und Reset
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=(10, 5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_fields)
        reset_button.grid(row=0, column=1, padx=5)

        # Statusanzeige
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)

        # Textfeld für detaillierte Ergebnisse
        self.result_box = ctk.CTkTextbox(self, width=480, height=150)
        self.result_box.grid(row=5, column=0, columnspan=2, padx=10, pady=(5, 10))
        self.result_box.configure(state="disabled")

        # Button für Kartenansicht (wird nur aktiviert, wenn gültige Koordinaten vorliegen)
        self.map_button = ctk.CTkButton(self, text="Auf Karte anzeigen", command=self.show_map_window, state="disabled")
        self.map_button.grid(row=6, column=0, columnspan=2, pady=(5, 10))

    def perform_lookup(self):
        lookup_type = self.lookup_type_menu.get().strip()
        if lookup_type == "IP (v4/v6)":
            self.lookup_ip()
        elif lookup_type == "Öffentliche IP (automatisch)":
            self.lookup_public_ip()
        elif lookup_type == "MAC":
            self.lookup_mac()
        elif lookup_type == "Netzwerkbereich":
            self.lookup_network_range()

    def lookup_ip(self):
        query = self.query_entry.get().strip()
        try:
            ip_obj = ipaddress.ip_address(query)
        except Exception:
            self.status_label.configure(text="Ungültiges IP-Adressformat.")
            return

        self.status_label.configure(text="IP-Lookup gestartet...")
        logging.info("Suche nach Geolocation für IP: %s", query)

        # Bei privaten IPs erfolgt eine simulierte Antwort.
        if ip_obj.is_private:
            logging.info("IP %s ist privat.", query)
            data = {
                "query": query,
                "networkType": "Private",
                "country": "Lokales Netzwerk",
                "regionName": "Simulierte Region",
                "city": "Simulierte Stadt",
                "zip": "Nicht verfügbar",
                "lat": 37.7749,     # Simulierte Koordinate (z. B. San Francisco)
                "lon": -122.4194,   # Simulierte Koordinate
                "timezone": "Lokal (simuliert)",
                "isp": "Privater ISP",
                "org": "Lokale Organisation",
                "status": "success"
            }
        else:
            try:
                # Hier könnte auch ein anderer externer Dienst verwendet werden
                response = requests.get(f"http://ip-api.com/json/{query}")
                if response.status_code != 200:
                    self.status_label.configure(text="Fehler: Konnte Daten für die öffentliche IP nicht abrufen.")
                    logging.error("HTTP-Fehler: %s", response.status_code)
                    return
                data = response.json()
                if data.get("status") != "success":
                    message = data.get("message", "Unbekannter Fehler")
                    self.status_label.configure(text=f"Fehler: {message}")
                    logging.error("API-Fehler: %s", message)
                    return
            except Exception as e:
                logging.error("Fehler beim IP-Lookup: %s", e)
                self.status_label.configure(text="Fehler beim IP-Lookup.")
                return

        result_text = (
            f"IP: {data.get('query', 'Nicht verfügbar')}\n"
            f"Netzwerk: {data.get('networkType', 'Public')}\n"
            f"Land: {data.get('country', 'Nicht verfügbar')}\n"
            f"Region: {data.get('regionName', 'Nicht verfügbar')}\n"
            f"Stadt: {data.get('city', 'Nicht verfügbar')}\n"
            f"ZIP: {data.get('zip', 'Nicht verfügbar')}\n"
            f"Latitude: {data.get('lat', 'Nicht verfügbar')} - Longitude: {data.get('lon', 'Nicht verfügbar')}\n"
            f"Timezone: {data.get('timezone', 'Nicht verfügbar')}\n"
            f"ISP: {data.get('isp', 'Nicht verfügbar')}\n"
            f"Organisation: {data.get('org', 'Nicht verfügbar')}\n"
        )
        self.status_label.configure(text="Lookup erfolgreich!")
        logging.info("Lookup-Ergebnis: %s", result_text)

        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("0.0", result_text)
        self.result_box.configure(state="disabled")

        if data.get("lat") is not None and data.get("lon") is not None:
            self.current_coordinates = (data["lat"], data["lon"])
            self.map_button.configure(state="normal")
        else:
            self.map_button.configure(state="disabled")
            self.current_coordinates = None

    def lookup_public_ip(self):
        """
        Ermittelt die öffentliche IP über ipify und ruft die Geolokationsdaten über ipinfo.io ab.
        """
        self.status_label.configure(text="Öffentliche IP wird ermittelt...")
        public_ip = get_public_ip()
        if not public_ip:
            self.status_label.configure(text="Fehler bei der Ermittlung der öffentlichen IP.")
            return

        self.status_label.configure(text=f"Öffentliche IP ({public_ip}) wurde ermittelt.")
        data = get_geolocation(public_ip)
        if data:
            loc = data.get("loc", "nicht verfügbar")
            result_text = (
                f"Öffentliche IP: {public_ip}\n"
                f"Land: {data.get('country', 'nicht verfügbar')}\n"
                f"Region: {data.get('region', 'nicht verfügbar')}\n"
                f"Stadt: {data.get('city', 'nicht verfügbar')}\n"
                f"Postleitzahl: {data.get('postal', 'nicht verfügbar')}\n"
                f"Koordinaten (lat, lon): {loc}\n"
            )
            self.result_box.configure(state="normal")
            self.result_box.delete("1.0", "end")
            self.result_box.insert("0.0", result_text)
            self.result_box.configure(state="disabled")
            # Versuche, die Koordinaten zu extrahieren
            if loc != "nicht verfügbar":
                try:
                    lat, lon = loc.split(',')
                    self.current_coordinates = (float(lat), float(lon))
                    self.map_button.configure(state="normal")
                except Exception as e:
                    logging.error("Fehler beim Parsen der Koordinaten: %s", e)
                    self.map_button.configure(state="disabled")
                    self.current_coordinates = None
            else:
                self.map_button.configure(state="disabled")
                self.current_coordinates = None
        else:
            self.status_label.configure(text="Keine Geolokationsdaten gefunden.")

    def lookup_mac(self):
        query = self.query_entry.get().strip()
        mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[-:]){5}([0-9A-Fa-f]{2})$')
        if not mac_pattern.match(query):
            self.status_label.configure(text="Ungültiges MAC-Adressformat.")
            return

        self.status_label.configure(text="MAC-Lookup gestartet...")
        logging.info("Suche nach MAC-Adresse: %s", query)

        try:
            response = requests.get(f"https://api.macvendors.com/{query}")
            if response.status_code == 200:
                vendor = response.text.strip()
                result_text = f"MAC-Adresse: {query}\nHersteller: {vendor}"
                self.status_label.configure(text="MAC-Lookup erfolgreich!")
                logging.info("MAC Lookup-Ergebnis: %s", result_text)
            else:
                result_text = f"MAC-Adresse: {query}\nHersteller-Lookup fehlgeschlagen (Status Code: {response.status_code})"
                self.status_label.configure(text="Fehler beim MAC-Lookup.")
                logging.error("MAC API Fehler mit Status %s", response.status_code)
        except Exception as e:
            logging.error("Fehler beim MAC-Lookup: %s", e)
            result_text = f"MAC-Adresse: {query}\nFehler beim Lookup: {e}"
            self.status_label.configure(text="Fehler beim MAC-Lookup.")

        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("0.0", result_text)
        self.result_box.configure(state="disabled")
        self.map_button.configure(state="disabled")
        self.current_coordinates = None

    def lookup_network_range(self):
        query = self.query_entry.get().strip()
        try:
            network = ipaddress.ip_network(query, strict=False)
        except Exception as e:
            self.status_label.configure(text="Ungültiger Netzwerkbereich. Bitte CIDR-Notation verwenden (z.B. 192.168.1.0/24).")
            return

        if network.num_addresses > 256:
            self.status_label.configure(text="Netzwerk zu groß zum Scannen (maximal 256 Adressen).")
            return

        self.status_label.configure(text="Netzwerkscan gestartet...")
        logging.info("Scanne Netzwerk: %s", query)
        results_text = ""
        for ip in network.hosts():
            ip_str = str(ip)
            try:
                if ip.is_private:
                    data = {
                        "query": ip_str,
                        "networkType": "Private",
                        "country": "Lokales Netzwerk",
                        "regionName": "Simulierte Region",
                        "city": "Simulierte Stadt",
                    }
                else:
                    response = requests.get(f"http://ip-api.com/json/{ip_str}")
                    if response.status_code != 200:
                        data = {"query": ip_str, "status": "fail", "message": "HTTP Fehler"}
                    else:
                        data = response.json()
                if data.get("status", "success") != "success":
                    results_text += f"IP: {ip_str} - Lookup fehlgeschlagen ({data.get('message', 'Unbekannter Fehler')})\n"
                else:
                    results_text += (f"IP: {data.get('query', ip_str)}, Land: {data.get('country', 'Nicht verfügbar')}, "
                                     f"Region: {data.get('regionName', 'Nicht verfügbar')}, Stadt: {data.get('city', 'Nicht verfügbar')}\n")
            except Exception as ex:
                results_text += f"IP: {ip_str} - Exception: {ex}\n"

        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("0.0", results_text)
        self.result_box.configure(state="disabled")
        self.status_label.configure(text="Netzwerkscan abgeschlossen!")
        self.map_button.configure(state="disabled")
        self.current_coordinates = None

    def show_map_window(self):
        if not self.current_coordinates:
            return

        lat, lon = self.current_coordinates
        interactive_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=14/{lat}/{lon}"

        map_window = ctk.CTkToplevel(self)
        map_window.title("Kartenansicht")
        map_window.geometry("620x500")

        frame = ctk.CTkFrame(map_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        instruction = ctk.CTkLabel(frame, text="Kartenansicht (OpenStreetMap)", font=("Arial", 14, "bold"))
        instruction.pack(pady=(10, 5))

        open_button = ctk.CTkButton(frame, text="Interaktive Karte im Browser öffnen", command=lambda: webbrowser.open(interactive_url))
        open_button.pack(pady=5)

        url_label = ctk.CTkLabel(frame, text=interactive_url, fg_color="transparent")
        url_label.pack(pady=5)

        static_map_url = (f"http://staticmap.openstreetmap.de/staticmap.php?center={lat},{lon}"
                          f"&zoom=14&size=600x400&markers={lat},{lon},red")
        try:
            response = requests.get(static_map_url)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((600, 400))
                photo = ImageTk.PhotoImage(image)
                image_label = ctk.CTkLabel(frame, image=photo)
                image_label.image = photo  # Referenz halten
                image_label.pack(pady=10)
            else:
                error_label = ctk.CTkLabel(frame, text="Kartenbild konnte nicht geladen werden.")
                error_label.pack(pady=10)
        except Exception as e:
            logging.error("Fehler beim Laden des Kartenbildes: %s", e)
            error_label = ctk.CTkLabel(frame, text="Fehler beim Laden des Kartenbildes.")
            error_label.pack(pady=10)

    def reset_fields(self):
        self.query_entry.delete(0, "end")
        self.status_label.configure(text="")
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.configure(state="disabled")
        self.map_button.configure(state="disabled")
        self.current_coordinates = None

# Für Testzwecke: Einfaches Hauptfenster erstellen
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Geolocation & Netzwerk-Suche")
    frame = GeolocationFrame(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()