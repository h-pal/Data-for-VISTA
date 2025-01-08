# Data-for-VISTA

**Data for VISTA: A Visual and Textual Attention Dataset for Interpreting Multimodal Models**

## Updates

- [x] Release of the dataset
- [ ] Release of the heatmap generation code

---

## Overview

The VISTA dataset combines visual fixation data and corresponding textual transcriptions for each image to enable the study of multimodal models. Each image in the dataset is associated with a `.json` file named after the image file itself, e.g., `000000001083.json` (based on MS COCO naming conventions).

The JSON files are structured to include two main sections:
- **Fixation Data**: Captures visual attention through time-series fixation points.
- **Transcription Data**: Represents textual descriptions or transcriptions aligned temporally with the image or visual attention.

---

## File Structure

Each JSON file contains the following keys:

### 1. `fixation_data`
A list of objects where each object represents a single fixation. Each fixation object contains:

- `start_time` *(float)*: The timestamp (in seconds) when the fixation started.
- `end_time` *(float)*: The timestamp (in seconds) when the fixation ended.
- `duration` *(float)*: The total duration (in seconds) of the fixation.
- `x_coordinates` *(list of floats)*: The x-coordinates of gaze points recorded during the fixation.
- `y_coordinates` *(list of floats)*: The y-coordinates of gaze points recorded during the fixation.
- `Avg_x_coordinates` *(float)*: The average x-coordinate of the fixation.
- `Avg_y_coordinates` *(float)*: The average y-coordinate of the fixation.
- `fixation_id` *(int)*: A unique identifier for the fixation.

**Example Fixation Entry:**
```json
{
    "start_time": 0.012,
    "end_time": 0.511,
    "duration": 0.499,
    "x_coordinates": [1841.0, 1841.0, 1852.0],
    "y_coordinates": [982.0, 1006.0],
    "Avg_x_coordinates": 1845,
    "Avg_y_coordinates": 997,
    "fixation_id": 0
}
```

### 2. `transcription_data`
A list of objects where each object represents a segment of transcription associated with the image. Each transcription object contains:

- `text` *(string)*: The text segment.
- `start` *(float)*: The timestamp (in seconds) when the transcription starts.
- `end` *(float)*: The timestamp (in seconds) when the transcription ends.

**Example Transcription Entry:**
```json
{
    "text": "A",
    "start": 1.7,
    "end": 2.46
}
```

---

## Dataset Usage

### Sample JSON File
```json
{
    "fixation_data": [
        {
            "start_time": 0.012,
            "end_time": 0.511,
            "duration": 0.499,
            "x_coordinates": [1841.0, 1841.0, 1852.0],
            "y_coordinates": [982.0, 1006.0],
            "Avg_x_coordinates": 1845,
            "Avg_y_coordinates": 997,
            "fixation_id": 0
        }
    ],
    "transcription_data": [
        {
            "text": "A",
            "start": 1.7,
            "end": 2.46
        }
    ]
}
```
## Download the Zipped Fixation Data

The zipped fixation data can be downloaded from [this Google Drive link](https://drive.google.com/file/d/1V6TxyBx82SIJe6Mgf8WldbbgSiSKVNGZ/view?usp=sharing). This archive contains all the fixation data in a compressed format for easy access and use.

Once decompressed, you will find individual JSON files, each corresponding to a specific image from the MS COCO dataset. The naming convention for the JSON files follows the format `{image_id}.json`, where `{image_id}` is the unique identifier of the MS COCO image used as stimuli. For example, if the image ID is `000000001083`, the corresponding JSON file will be named `000000001083.json`.

This naming convention ensures easy mapping of fixation and transcription data to their corresponding stimuli images from the MS COCO dataset.

## Additional Tools

The repository also contains the `get_images.py` script, which allows users to download the relevant MS COCO images that were used as stimuli to collect the dataset's fixation and transcription data. 

### Purpose of `get_images.py`
The script automates the process of fetching images from the MS COCO dataset that correspond to the JSON files provided in this repository. This ensures that users can easily reproduce experiments or analyses by having access to the exact images used during the data collection process.

#### Features of `get_images.py`
- **Automatic Image Retrieval**: The script downloads images using their MS COCO IDs, ensuring consistency with the dataset.
- **Customizable Output Directory**: Images are saved in a user-specified directory (default: `coco_images`).
- **Error Handling**: Handles timeouts and connection issues gracefully, printing an error message if a download fails.

#### How to Use `get_images.py`
1. Ensure you have Python installed and the necessary dependencies (`requests`, `pathlib`, and `tqdm`). Install them using:
   ```bash
   pip install requests tqdm
   ```
2. Place a text file named `image_filenames.txt` in the root directory of the repository. This file should contain the IDs of the images to be downloaded (one per line).
3. Run the script as follows:
   ```bash
   python get_images.py
   ```
4. The images will be downloaded into the `coco_images` folder by default. You can modify the `save_dir` parameter in the script to change the output directory.

#### Example `image_filenames.txt` Content
```
000000001083
000000002947
000000009781
```



### Applications
- **Multimodal Model Analysis**: Study the alignment between visual and textual modalities.
- **Attention Modeling**: Understand how humans perceive and interpret visual content.
- **Dataset Benchmarking**: Use as a benchmark for multimodal learning tasks.

---

## Citation
If you use the VISTA dataset in your research, please cite:
```
@article{
  title={VISTA: A Visual and Textual Attention Dataset for Interpreting Multimodal Models},
  author={Harshit,Sang Hyun Chun, Joseph Lieskovan, Tolga Tasdizen},
  journal={Proceedings of the Gaze Meets Computer Vision Workshop (GMCV), WACV 2025},
  year={2024}
}
```

---

For any questions or issues, feel free to open an issue on this repository or contact the maintainers.
