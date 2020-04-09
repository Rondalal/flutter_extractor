# flutter_extractor
Extracting strings and function names from Flutter apks, based on this blogpost - https://medium.com/@rondalal54/reverse-engineering-flutter-apps-5d620bb105c0

## Usage
```
flutter_extractor.py [OPTIONS] APP_PATH

app_path: path to the extracted apk directory (the output directory of the apktool)

Options:
  --out TEXT  The output dir
  --help      Show this message and exit.
```
**Please use [ApkTool](https://ibotpeaches.github.io/Apktool/) or jadx** before running the extractor. Due to the fact that APKs are somewhat a zip file, there's need to extract the files first, for the extractor to use them.

## Example
```python flutter_extractor.py /path/to/extracted_apk/ --out ./flutter_data```
