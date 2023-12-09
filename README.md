# Face and Body Detection Video Recorder

## Overview

This Python script captures video from the default camera (usually the built-in webcam) and records video clips when it detects faces or bodies in the frames. The detection is performed using Haar cascades provided by the OpenCV library. The recorded video clips are saved with filenames containing the date and time of detection.

## Prerequisites

Make sure you have the following installed:

- Python 3
- OpenCV library (`cv2`)

You can install OpenCV using the following command:

```bash
pip install opencv-python
```

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python security_camera.py
   ```

4. The camera window will appear, and the script will start detecting faces and bodies.
5. Press 'q' to exit the script.

## Configuration

You can customize the following parameters in the script:

- `sec_rec_after_detection`: The number of seconds to continue recording after detection stops.

## Note

The script uses Haar cascades for face and body detection. Ensure that the required Haar cascade XML files are available in the OpenCV data directory. The default files used in this script are:

- `haarcascade_frontalface_default.xml` for face detection
- `haarcascade_fullbody.xml` for body detection

Make sure these files are present in the OpenCV data directory. If not, you can download them from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).
