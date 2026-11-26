
# CAPTURA DE DADOS DE PROCESSOS DO SITE TJRJ 

## Run Locally

Clone the project

```bash
  git clone https://github.com/mbersot/aut_dados_processos.git
```

Go to the project directory

```bash
  cd aut_dados_processos
```

Create virtual environment

```bash
  python -m venv .venv
  .venv\Scripts\activate
```

Install dependencies

```bash
  python.exe -m pip install --upgrade pip

  pip install pandas

  python -c "import pandas; print(pandas.__version__)"

  pip install -r requirements.txt

  playwright install chromium --dry-run
  
  playwright install chromium
  
  pip install pyinstaller ##Comando para instalar biblioteca que gera arquivos executaveis (.exe) a partir de um arquivo .py
  
```

Start the automation

```bash
  python main.py
```

## Acknowledgements

 - [Readme on line editor](https://readme.so/editor)



##  Build

Specify Chromium directory and version (inside build.bat)

```bash

--add-data "%APPDATA%\..\Local\ms-playwright\{chromium_folder};./playwright/driver/package/.local-browsers/{chromium_version}"

EX: --add-data "%APPDATA%\..\Local\ms-playwright\chromium-1097;./playwright/driver/package/.local-browsers/1097" ^

```

Generate .exe

```bash
    ./main.bat
```

## Requirements

Create requirements.txt file (activate .venv before these codes)

```bash
  python.exe -m pip install --upgrade pip

  pip install pipreqs

  pipreqs --force --encoding=utf8 --ignore bin,etc,include,lib,lib64,.venv

  pip freeze > requirements.txt ## caso o pipreqs não funcione

```