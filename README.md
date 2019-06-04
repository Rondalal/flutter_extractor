# flutter_extractor
Extracting strings and function names from Flutter apks, based on this blogpost 

## Usage
```
flutter_extractor.py [OPTIONS] APP_PATH

app_path: path to the extracted apk directory (the output directory of the apktool)

Options:
  --out TEXT  The output dir
  --help      Show this message and exit.
```
## Example
```python flutter_extractor.py /path/to/extracted_apk/ --out ./flutter_data```
