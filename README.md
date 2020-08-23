# Bezel Remover

## Usage

```
python main.py file_to_edit.mp4 output_file.mp4
```

You can also run it with the `--debug` option

```
python main.py --debug file_to_edit.mp4 frame.jpg
```

This will output the first frame of the modified video to `frame.jpg` so you can see how much will be trimmed.

### Arguments

```
positional arguments:
  input_video  the video that will have its bezels removed
  output       output destination

optional arguments:
  -h, --help   show this help message and exit
  --debug      if set the output will be the first frame of the modified video
```
