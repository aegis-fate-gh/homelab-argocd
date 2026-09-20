```
{
  "_id": "pXBpiwSNO",
  "name": "AV1 Import",
  "description": "AV1 Import",
  "tags": "",
  "flowPlugins": [
    {
      "name": "Input File",
      "sourceRepo": "Community",
      "pluginName": "inputFile",
      "version": "1.0.0",
      "id": "Sjoe0VMPw",
      "position": {
        "x": 840,
        "y": -48
      },
      "fpEnabled": true,
      "inputsDB": {
        "fileAccessChecks": "true",
        "pauseNodeIfAccessChecksFail": "true"
      }
    },
    {
      "name": "Check Video Codec",
      "sourceRepo": "Community",
      "pluginName": "checkVideoCodec",
      "version": "1.0.0",
      "id": "rGFh1c2P5",
      "position": {
        "x": 816,
        "y": 72
      },
      "fpEnabled": true,
      "inputsDB": {
        "codec": "av1"
      }
    },
    {
      "name": "Begin Command",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandStart",
      "version": "1.0.0",
      "id": "6QuhrjnFC",
      "position": {
        "x": 912,
        "y": 216
      },
      "fpEnabled": true
    },
    {
      "name": "Set Container",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandSetContainer",
      "version": "1.0.0",
      "id": "xp5_wyZvP",
      "position": {
        "x": 912,
        "y": 492
      },
      "fpEnabled": true
    },
    {
      "name": "Set Video Encoder",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandSetVideoEncoder",
      "version": "1.0.0",
      "id": "iX6jNLa8J",
      "position": {
        "x": 912,
        "y": 432
      },
      "fpEnabled": true,
      "inputsDB": {
        "outputCodec": "av1",
        "ffmpegPreset": "slow",
        "ffmpegQuality": "30",
        "forceEncoding": "false",
        "hardwareEncoding": "false"
      }
    },
    {
      "name": "Execute",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandExecute",
      "version": "1.0.0",
      "id": "85XIJlyOT",
      "position": {
        "x": 912,
        "y": 552
      },
      "fpEnabled": true
    },
    {
      "name": "Move To Directory",
      "sourceRepo": "Community",
      "pluginName": "moveToDirectory",
      "version": "2.0.0",
      "id": "TvuunHXwb",
      "position": {
        "x": 816,
        "y": 636
      },
      "fpEnabled": true,
      "inputsDB": {
        "keepRelativePath": "true",
        "outputDirectory": "/media/downloads/completed/{{{args.userVariables.library.folder}}}"
      }
    },
    {
      "name": "Check Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedCheck",
      "version": "1.0.0",
      "id": "wLRWSxVLd",
      "position": {
        "x": 840,
        "y": 12
      },
      "fpEnabled": true
    },
    {
      "name": "Add To Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedAdd",
      "version": "1.0.0",
      "id": "pDPIUy0C2",
      "position": {
        "x": 816,
        "y": 684
      },
      "fpEnabled": true
    },
    {
      "name": "Remove Stream By Property",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandRemoveStreamByProperty",
      "version": "1.0.0",
      "id": "rY8CQBlOc",
      "position": {
        "x": 912,
        "y": 288
      },
      "fpEnabled": true,
      "inputsDB": {
        "valuesToRemove": "mov_text",
        "codecType": "subtitle"
      }
    },
    {
      "name": "Check File Exists",
      "sourceRepo": "Community",
      "pluginName": "checkFileExists",
      "version": "1.0.0",
      "id": "P1nRFM6pe",
      "position": {
        "x": 888,
        "y": 144
      },
      "fpEnabled": true,
      "inputsDB": {
        "fileToCheck": "${fileName}.${container}",
        "directory": "/media/downloads/completed/{{{args.userVariables.library.folder}}}"
      }
    },
    {
      "name": "Remove Data Streams",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandRemoveDataStreams",
      "version": "1.0.0",
      "id": "-M93YOLrW",
      "position": {
        "x": 912,
        "y": 372
      },
      "fpEnabled": true
    }
  ],
  "flowEdges": [
    {
      "source": "iX6jNLa8J",
      "sourceHandle": "1",
      "target": "xp5_wyZvP",
      "targetHandle": null,
      "id": "jIHrsCTfs"
    },
    {
      "source": "xp5_wyZvP",
      "sourceHandle": "1",
      "target": "85XIJlyOT",
      "targetHandle": null,
      "id": "P9dbwNXLW"
    },
    {
      "source": "85XIJlyOT",
      "sourceHandle": "1",
      "target": "TvuunHXwb",
      "targetHandle": null,
      "id": "glMrXINMW"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "1",
      "target": "TvuunHXwb",
      "targetHandle": null,
      "id": "teQkE4099"
    },
    {
      "source": "Sjoe0VMPw",
      "sourceHandle": "1",
      "target": "wLRWSxVLd",
      "targetHandle": null,
      "id": "8DCR5xD8y"
    },
    {
      "source": "wLRWSxVLd",
      "sourceHandle": "1",
      "target": "rGFh1c2P5",
      "targetHandle": null,
      "id": "HPFqOD9Ru"
    },
    {
      "source": "TvuunHXwb",
      "sourceHandle": "1",
      "target": "pDPIUy0C2",
      "targetHandle": null,
      "id": "4dq-k68Qu"
    },
    {
      "source": "6QuhrjnFC",
      "sourceHandle": "1",
      "target": "rY8CQBlOc",
      "targetHandle": null,
      "id": "VRIqludzd"
    },
    {
      "source": "P1nRFM6pe",
      "sourceHandle": "2",
      "target": "6QuhrjnFC",
      "targetHandle": null,
      "id": "j96-nI0UL"
    },
    {
      "source": "rY8CQBlOc",
      "sourceHandle": "1",
      "target": "-M93YOLrW",
      "targetHandle": null,
      "id": "7jvqcZ1CO"
    },
    {
      "source": "-M93YOLrW",
      "sourceHandle": "1",
      "target": "iX6jNLa8J",
      "targetHandle": null,
      "id": "559aXEVay"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "2",
      "target": "P1nRFM6pe",
      "targetHandle": null,
      "id": "qE0em-u3u"
    }
  ]
}
```