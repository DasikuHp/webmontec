# Skills

Colección de skills para agentes de IA bajo la filosofía
[ponytail](https://github.com/DietrichGebert/ponytail): *el mejor código es el
que no escribes*. Cada skill es un `.md` con frontmatter (`name`, `description`
con frases-gatillo) que un agente puede leer y ejecutar.

## Skills disponibles

### `godot-4.6-rpg` → [`skillgodot4.6.md`](./skillgodot4.6.md)

Construir un **RPG 3D libre en Godot 4.6** (GDScript y C#) resolviendo cada
sistema con nodos y Resources nativos antes que con arquitectura propia.
Incluye la escalera de decisión ponytail, las features nuevas de 4.6 (Jolt por
defecto, `IKModifier3D`, diccionarios tipados, clases `@abstract`, SSR/LOD) y
patrones de RPG (locomoción, inventario, estados, guardado, navegación,
combate).

Ejemplos ejecutables y tipados que la skill referencia, con guía de cableado de
principio a fin, en [`godot-rpg-examples/`](./godot-rpg-examples/).

## Cómo se usa una skill

Apunta tu agente al `.md`. La sección `description` del frontmatter lista las
frases que la activan (p. ej. "RPG en Godot", "Godot 4.6", "inventario"). El
cuerpo es la guía que el agente sigue.
