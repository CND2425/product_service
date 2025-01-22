
# Product Service

## Beschreibung
Der **Product Service** ist ein zentraler Bestandteil einer Microservices-basierten E-Commerce-Anwendung. Er bietet eine REST-API zur Verwaltung des Produktkatalogs und unterstützt Funktionen wie das Hinzufügen, Abrufen, Aktualisieren und Löschen von Produktinformationen.

### Hauptfunktionen:
1. **Produkt hinzufügen**: Erstellung neuer Produkte im Katalog.
2. **Produkte abrufen**: Anzeigen aller Produkte oder eines spezifischen Produkts.
3. **Produkte aktualisieren**: Ändern von Details bestehender Produkte.
4. **Produkte löschen**: Entfernen von Produkten aus dem Katalog.

Dieser Service wurde mit **FastAPI** entwickelt und verwendet **MongoDB** zur Speicherung von Produktinformationen.

---

## Technologien
1. **FastAPI**: Framework für die API-Entwicklung.
2. **MongoDB**: NoSQL-Datenbank zur Speicherung von Produktdaten.
3. **Docker**: Containerisierung des Services.
4. **GitHub Actions**: CI/CD-Pipeline zur Qualitätssicherung.

---

## Verwendete Endpunkte
### Produkt-Endpunkte:
1. **POST** `/products/` - Fügt ein neues Produkt hinzu.
2. **GET** `/products/` - Listet alle Produkte auf.
3. **GET** `/products/{id}` - Ruft ein spezifisches Produkt ab.
4. **PUT** `/products/{id}` - Aktualisiert ein Produkt.
5. **DELETE** `/products/{id}` - Löscht ein Produkt.

---

## Installation und Verwendung
### Voraussetzungen
- **Python 3.9+**
- **Docker** und **Docker Compose**

### Lokale Ausführung
- **Repository klonen**:
  ```bash
  git clone <REPOSITORY_URL>
  cd product_service
  ```

- **Virtuelle Umgebung erstellen und aktivieren**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Auf Windows: venv\Scripts\activate
  ```

- **Abhängigkeiten installieren**:
  ```bash
  pip install -r requirements.txt
  ```

- **Service starten**:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8001
  ```

### Docker-Ausführung
- **Docker-Image erstellen und starten**:
  ```bash
  docker build -t product_service .
  docker run -p 8001:8001 product_service
  ```

- **Alternativ mit Docker Compose** (aus dem `Compose`-Repository):
  ```bash
  docker-compose up -d
  ```

### API-Dokumentation
FastAPI bietet eine automatisch generierte API-Dokumentation:
- Swagger UI: [http://localhost:8001/docs](http://localhost:8001/docs)
- ReDoc: [http://localhost:8001/redoc](http://localhost:8001/redoc)

---

## Datenbank
1. **MongoDB** wird verwendet, um Produktdaten persistent zu speichern.
2. Standardmäßig verbindet sich der Service zu `mongodb://localhost:27017`.
3. Anpassung der URL über Umgebungsvariablen:
   ```bash
   MONGODB_URL=mongodb://<host>:<port>
   ```

---

## Tests
1. **Testumgebung installieren**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Tests ausführen**:
   ```bash
   pytest tests/
   ```

---

## CI/CD
1. Der Service verwendet **GitHub Actions**, um Tests und Linting automatisch bei jedem Commit auszuführen.
2. Die Konfiguration befindet sich in `.github/workflows/ci.yml`.

---

## Umgebungsvariablen
1. `MONGODB_URL`: MongoDB-Verbindungs-URL.

---
