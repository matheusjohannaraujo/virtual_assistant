# [Virtual Assistant](https://github.com/matheusjohannaraujo/virtual_assistant)

```php
const DEVELOPER_INFO = [
    "autor" => "Matheus Johann Araújo",
    "country" => "Brasil",
    "state" => "Pernambuco",
    "date" => "2021-11-09"
];
```

### List of commands used to install [`Tuxi CLI`](https://www.youtube.com/watch?v=RXKWSZlJyY8&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-) and its dependencies:
```php
# Tuxi CLI official website: https://github.com/Bugswriter/tuxi

# Update and install packages (cURL, Wget, UnZip, Recode and JQ)
apt update
apt install -y curl wget unzip recode jq

# Install Pup
wget "https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip"
unzip pup_v0.4.0_linux_amd64.zip
chmod +x pup
mv pup /usr/local/bin/
rm pup_v0.4.0_linux_amd64.zip

# Install Tuxi
wget "https://raw.githubusercontent.com/Bugswriter/tuxi/main/tuxi"
chmod +x tuxi
mv tuxi /usr/local/bin/

# Testing Tuxi
tuxi "dolar hoje?"
```

### Dependencies to install in Python:

> *File: [textoParaFala.py](https://www.youtube.com/watch?v=OjoiJzg7Ags&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-)*

>> pip install gtts

>> pip install playsound

> *File: [falaParaTexto.py](https://www.youtube.com/watch?v=jUXjBTIWqKY&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-)*

>> pip install SpeechRecognition

>> pip install pyaudio

### Python main execution file

> *File: [principal.py](https://www.youtube.com/watch?v=ZUqDb0H5OEc&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-)*

### PHP file that calls the [`Tuxi CLI`](https://www.youtube.com/watch?v=RXKWSZlJyY8&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-) installed on the `WSL Ubuntu`

> *File: [tuxi.php](https://www.youtube.com/watch?v=RXKWSZlJyY8&list=PLODC80noz2kKXR3fXKwprtOhFxI7qX1_-)*
