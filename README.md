# VS Code + Django Config

Este paquete incluye:

- `.vscode/settings.json`
  - Formateo automático al guardar
  - Organización automática de imports
  - Límite visual de 88 caracteres
  - Ruff como formatter/linter
  - Configuración optimizada para Python/Django

- `.vscode/extensions.json`
  - Extensiones recomendadas para VS Code

- `pyproject.toml`
  - Configuración de Ruff y pytest

## Instalar dependencias

```bash
pip install ruff pytest pytest-django
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno

Linux/macOS:
```bash
source .venv/bin/activate
```

Windows:
```powershell
.venv\Scripts\activate
```