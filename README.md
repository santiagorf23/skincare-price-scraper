# Skincare Price Scraper 🧴

Herramienta en Python que extrae automáticamente nombres y precios de productos de skincare desde páginas web y los exporta a Excel para análisis de precios.

---

## ¿Qué hace este proyecto?

- Extrae nombre y precio de productos de skincare desde sitios web
- Limpia y organiza los datos automáticamente
- Exporta los resultados a un archivo Excel listo para analizar
- Permite comparar precios entre diferentes tiendas

---

## Tecnologías usadas

| Librería | Para qué se usa |
|---|---|
| `requests` | Hacer solicitudes HTTP a las páginas web |
| `BeautifulSoup4` | Leer y extraer datos del HTML |
| `openpyxl` | Generar el archivo Excel con los resultados |

---

## Estructura del proyecto

```
skincare-price-scraper/
├── data/              # Archivos Excel generados
├── scraper.py         # Script principal
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Este archivo
```

---

## Cómo usarlo

**1. Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/skincare-price-scraper.git
cd skincare-price-scraper
```

**2. Instala las dependencias**
```bash
pip install -r requirements.txt
```

**3. Ejecuta el scraper**
```bash
python scraper.py
```

**4. Encuentra tu archivo Excel en la carpeta `data/`**

---

## Ejemplo de resultado

| Producto | Precio |
|---|---|
| Vitamin C Serum 30ml | $25.99 |
| Hydrating Toner 150ml | $18.50 |
| SPF 50 Sunscreen | $32.00 |

---

## Estado del proyecto

🟡 En desarrollo — Versión 1.0 (extracción básica)

**Próximas funciones:**
- [ ] Soporte para múltiples tiendas
- [ ] Alertas de bajada de precio por correo
- [ ] Historial de precios con gráficas

---

## Autor

Desarrollado por **[Tu Nombre]** como parte de una ruta de aprendizaje en Python con enfoque en automatización y generación de ingresos.

[GitHub](https://github.com/santiagorf23) · [LinkedIn](https://www.linkedin.com/in/santiagorf23/)