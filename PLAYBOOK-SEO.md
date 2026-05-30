# Playbook SEO / GEO / AEO — Moncatec

Guía para posicionar Moncatec en Google **y** en los buscadores de IA (ChatGPT, Perplexity, Google
AI Overviews). Lo de la web ya está hecho; **la mayor parte de la visibilidad de un negocio local es
off-page** y depende de ti. Ordenado por impacto real (factores de ranking local 2026).

---

## ✅ Ya aplicado en la web (on-page)

- Tipografía propia (Fraunces + Hanken Grotesk), fuera la fuente genérica.
- `<title>`, meta description, Open Graph, canonical y un único `<h1>` con la keyword.
- **Datos estructurados JSON-LD**: `LocalBusiness` (con dirección de Moncada, horario, teléfono,
  servicios y credencial Fermax), `Organization`, `WebSite` y **`FAQPage`**.
- Sección **FAQ** visible (la palanca nº1 para que la IA te cite).
- Sección de **opiniones reales** (5,0★ · 52 reseñas) enlazada a Google.
- Sección **Zonas de actuación** (Moncada + L'Horta Nord) para consultas "videoportero en [pueblo]".
- **Botón sticky de llamada/WhatsApp** en móvil (las llamadas son una señal de ranking fuerte).
- `robots.txt` (permite GPTBot, ClaudeBot, PerplexityBot, Google-Extended), `sitemap.xml`, `llms.txt`.

> **Pendiente tuyo en la web:** sustituir en `prueba.html` el enlace de opiniones y el `sameAs` del
> JSON-LD por la **URL exacta de tu Google Business Profile**, Facebook y LinkedIn (busca los `TODO`).

---

## 🚀 Off-page — lo que mueve de verdad la aguja (por orden de impacto)

### 1. Google Business Profile (GBP) — ~32% del posicionamiento local
- Completa el perfil al **100%**: nombre, dirección (Moncada), teléfono **653 33 69 93**, web, horario.
- **Categoría principal correcta** (la que más pesa): p. ej. "Servicio de reparación" / "Instalador
  de sistemas de seguridad" / "Electricista", y categorías secundarias (videoporteros, alarmas…).
- Sube **fotos reales** a menudo (trabajos, fachada, equipo).
- **Publica ~2 veces por semana** (ofertas, trabajos, avisos). La frecuencia de publicación puntúa.
- Rellena la sección de **Servicios** y responde la sección **Preguntas y respuestas**.

### 2. Reseñas — ~16%
- Ya tienes 52 con 5,0★: **mantén el ritmo**. Las reseñas de los **últimos 30 días pesan más**.
- Pide la reseña al terminar cada trabajo; pon el enlace directo en facturas/WhatsApp.
- **Responde** a todas (también las de 4★), con naturalidad.
- ⚠️ **Nunca compres ni falsees reseñas**: Google las detecta con IA y puede borrarlas en masa y
  echarte del *local pack* en horas.

### 3. Enlaces y menciones — ~15%
- **Menciones sin enlace**: si una web/blog/periódico local nombra "Moncatec" sin enlazar, pídeles
  el enlace. Es el mayor retorno con el menor esfuerzo.
- Aparece en **artículos tipo "mejores instaladores de videoporteros en Valencia / L'Horta Nord"**.

### 4. Comportamiento — ~8%
- Clic-para-llamar, solicitudes de cómo llegar y tiempo en el perfil. El botón de llamada de la web
  ya ayuda; en GBP, tener teléfono y dirección visibles también.

### 5. Citaciones / NAP — ~7%
- Da de alta el negocio en directorios con el **mismo nombre, dirección y teléfono EXACTOS**:
  Páginas Amarillas, Bing Places, Apple Maps, directorios de telecomunicaciones, el directorio
  oficial de Fermax, etc. Las inconsistencias de NAP perjudican.

---

## 🤖 Para aparecer en la IA (GEO/AEO)

- **Consenso de terceros**: la IA te cita con confianza cuando varias fuentes externas coinciden con
  tu web. Consigue presencia en GBP, directorios, foros locales, Reddit/Quora cuando alguien
  pregunte por instaladores en Valencia, y en artículos del sector.
- **Entidad**: crea una ficha en **Wikidata** y, si tu reputación lo permite, reclama el Knowledge
  Panel de Google. Mantén los mismos datos (NAP) en todas partes.
- La **FAQ** y las **opiniones** de la web ya están en formato fácil de extraer y citar por la IA.

---

## ⛔ Lo que NO debes hacer (penaliza, no ayuda)

El sistema antispam de Google (SpamBrain) actúa casi en tiempo real; estas tácticas provocan caídas
del 50-95% del tráfico en ~72 h y recuperaciones de 6-18 meses:
- Comprar o falsear reseñas.
- Schema falso (marcar FAQ/reseñas que no coinciden con lo visible de la página).
- Texto oculto / relleno de palabras clave invisibles.
- Cloaking, doorway pages, comprar enlaces, PBNs, contenido de IA masivo sin revisar.

---

## 🔎 Validación

- Datos estructurados: **Google Rich Results Test** (https://search.google.com/test/rich-results)
  con la URL de moncatec.es — debe detectar `LocalBusiness` y `FAQPage` sin errores.
- Rendimiento/SEO técnico: **PageSpeed Insights** / Lighthouse.
- Indexación y sitemap: **Google Search Console** (envía `sitemap.xml`).
