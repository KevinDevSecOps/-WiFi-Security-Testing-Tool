# WiFi Security Testing Tool 🔒

Herramienta educativa para pruebas de seguridad en redes WiFi.

## ⚠️ ADVERTENCIA LEGAL

Esta herramienta es **SOLO PARA FINES EDUCATIVOS**. 
El uso no autorizado de técnicas de desautenticación es ILEGAL.
Solo debe usarse en:
- Tus propias redes
- Redes con permiso explícito del propietario
- Entornos de laboratorio controlados

## Características

- 📡 Escaneo de redes WiFi
- 📊 Visualización de redes detectadas
- 🔍 Detección de tipo de encriptación
- 📡 Modo monitor automático
- 🛡️ Prueba de desautenticación controlada

## Instalación

```bash
git clone https://github.com/tuusuario/wifi-security-tool
cd wifi-security-tool
pip install -r requirements.txt
Uso

```bash
sudo python3 examples/basic_usage.py
```

Requisitos

· Python 3.7+
· Linux con adaptador WiFi compatible
· Permisos de root
· Scapy y dependencias

Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de:

1. Solo código ético y educativo
2. Documentar adecuadamente
3. No incluir funcionalidades maliciosas

Licencia

MIT - Solo para uso educativo

```

### Características del Proyecto:

1. **Estructura modular** y bien organizada
2. **Uso de Scapy** para manipulación de paquetes
3. **Interfaz colorida** con Rich y Colorama
4. **Escaneo de redes** con información detallada
5. **Implementación educativa** de desautenticación
6. **Manejo automático** del modo monitor
7. **Documentación completa** y advertencias legales

### Para GitHub:

```bash
# Inicializar repositorio
git init
git add .
git commit -m "Initial commit: WiFi Security Testing Tool"

# Agregar .gitignore
echo "__pycache__/\n*.pyc\n.env/\nvenv/\n*.log" > .gitignore

# Crear repositorio en GitHub y subir
git remote add origin https://github.com/tuusuario/wifi-security-tool
git push -u origin main
```

Recuerda: Este proyecto es estrictamente para aprendizaje y testing ético. Nunca lo uses en redes sin autorización.