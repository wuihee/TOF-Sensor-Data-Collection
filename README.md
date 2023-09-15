# Traffic Data Collection

## Table of Contents

1. [Introduction](#introduction)
2. [Notebooks](#notebooks)
3. [Installation](#installation)

## Introduction

### Context

In Singapore, in the face of bicycle related traffic accidents, traffic rules require cars to overtake bicycles at a minimum distance of 1.5m.

### Goals

The goal of this project is to collect data on the passing distance of cars to bicycles. I use various sensors to measure the distance of passing vehicles. The sensors were mounted a bike which was used to ride around Singapore roads and collect data.

## Notebooks

### Basic Tests

The results and analysis of each sensor's baseline capabilities in a static environment.

- [WaveShare's TOF Sensor](./notebooks/TOF_Basic_Tests.ipynb)
- [Chengdu JRT Laser Distance Sensor](./notebooks/Laser_Basic_Tests.ipynb)
- [Garmin's LIDAR-Lite V4](./notebooks/LIDAR_Basic_Tests.ipynb)

### Outdoor Tests

Analysis and conclusions of the vehicle-to-cyclist passing distance data collected by each sensor.

- [TOF Sensor](./notebooks/TOF_Outdoor_Tests.ipynb): TOF sensor unreliable due to high amount of spurious data generated.
- [Laser Sensor](./notebooks/Laser_Outdoor_Tests.ipynb): Laser sensor too slow if not used with windows software.
- [LIDAR Sensor](./notebooks/LIDAR_Outdoor_Tests.ipynb): Successful automated data collection with AI camera! Also showcases sample automated data analysis with DBSCAN cluster identification.

## Installation

To run the notebooks, install the dependencies:

```bash
pip install -r requirements.txt
```

The setup and code used to run the sensors can be found in my [`traffic-data-sensors`](https://github.com/wuihee/traffic-data-sensors) module.
