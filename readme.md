# arte-dl
[![Python](https://img.shields.io/badge/python-2.7, 3.x-blue.svg)](https://www.python.org/) [![MIT License](https://img.shields.io/badge/license-MIT-black.svg)](https://opensource.org/licenses/MIT)

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
You may alter the list of categories (`config['categories']`), the following keys are valid:
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

The script will store a list of previously downloaded videos to prevent storing multiple duplicates of files in a text file thats path is specified in the `config['list-path']` setting.

By default, this text file and the downloaded videos will be stored in the script directory.

### Execute the script
```bash
python arte-dl.py
```

### Advanced
If you wish to check for new videos on a regular basis, you may add the script as a cronjob. Adding the following to your crontab using `crontab -e` for example will run the script at 1:00 AM on a daily basis:
```
0 1 * * * python [[path-to-script]]/arte-dl.py > [[path-to-script]]/arte.log
```

## Contributing
If you found another category, a bug, want to propose a feature or feel the urge to complain about your life, feel free to visit [the issues page](https://github.com/juliuste/arte-dl/issues).