# arte-dl
[![Build Status](https://travis-ci.org/juliuste/tf-idf.svg?branch=master)](https://travis-ci.org/juliuste/arte-dl) [![Python](https://img.shields.io/badge/python-3.2, 3.3, 3.4, 3.5-blue.svg)](https://www.python.org/) [![MIT License](https://img.shields.io/badge/license-MIT-black.svg)](https://opensource.org/licenses/MIT)

This script downloads videos from the [german arte +7 library](http://www.arte.tv/guide/de/plus7/) out of given categories like `Dokumentation`, `Dokumentationsreihe`, `Reportage`,  etc... 

## Usage
### Install the dependencies
```bash
pip install feedparser youtube_dl
```

### Download the script
```bash
git clone https://github.com/juliuste/arte-dl.git
```

### Configurate the script
```bash
cd arte-dl
nano arte-dl.py
```
You may alter the list of categories, the following keys are valid:
- `Dokumentarfilm`
- `Dokumentation`
- `Dokumentationsreihe`
- `Fernsehfilm`
- `Fernsehserie`
- `Kindersendung`
- `Kurzfilm`
- `Magazin`
- `Musik`
- `Nachrichten`
- `Oper`
- `Reportage`
- `Theater`

If you leave the list empty, all videos regardless of their category will be downloaded.

### Execute the script
```bash
python arte-dl.py
```

## Contributing
If you found another category, a bug, want to propose a feature or feel the urge to complain about your life, feel free to visit [the issues page](https://github.com/juliuste/arte-dl/issues).