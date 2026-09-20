```
{
  "_id": "3a3090wHP",
  "name": "AV1 Replacer Sonarr",
  "description": "AV1 Replacer Sonarr",
  "tags": "",
  "flowPlugins": [
    {
      "name": "Add To Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedAdd",
      "version": "1.0.0",
      "id": "Bf8biy1YS",
      "position": {
        "x": 852,
        "y": 504
      },
      "fpEnabled": true
    },
    {
      "name": "Input File",
      "sourceRepo": "Community",
      "pluginName": "inputFile",
      "version": "1.0.0",
      "id": "Sjoe0VMPw",
      "position": {
        "x": 840,
        "y": -252
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
        "y": -156
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
        "y": -36
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
        "y": 252
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
        "y": 204
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
        "y": 300
      },
      "fpEnabled": true
    },
    {
      "name": "Notify Radarr or Sonarr",
      "sourceRepo": "Community",
      "pluginName": "notifyRadarrOrSonarr",
      "version": "2.0.0",
      "id": "bU5KZPbCE",
      "position": {
        "x": 648,
        "y": 504
      },
      "fpEnabled": true,
      "inputsDB": {
        "arr": "sonarr",
        "arr_host": "https://sonarr.jovian.local.sch-apps.com",
        "arr_api_key": "ADD_ME"
      }
    },
    {
      "name": "Replace Original File",
      "sourceRepo": "Community",
      "pluginName": "replaceOriginalFile",
      "version": "1.0.0",
      "id": "QfDBUN7OT",
      "position": {
        "x": 648,
        "y": 456
      },
      "fpEnabled": true
    },
    {
      "name": "Copy to Working Directory",
      "sourceRepo": "Community",
      "pluginName": "copyToWorkDirectory",
      "version": "1.0.0",
      "id": "RRkl-aiMA",
      "position": {
        "x": 912,
        "y": -84
      },
      "fpEnabled": true
    },
    {
      "name": "Add To Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedAdd",
      "version": "1.0.0",
      "id": "GG3jailrX",
      "position": {
        "x": 708,
        "y": 24
      },
      "fpEnabled": true
    },
    {
      "name": "Check Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedCheck",
      "version": "1.0.0",
      "id": "mRAI66JAd",
      "position": {
        "x": 840,
        "y": -204
      },
      "fpEnabled": true
    },
    {
      "name": "Compare File Size",
      "sourceRepo": "Community",
      "pluginName": "compareFileSize",
      "version": "1.0.0",
      "id": "ov5u9NtOB",
      "position": {
        "x": 816,
        "y": 384
      },
      "fpEnabled": true
    },
    {
      "name": "Delete File",
      "sourceRepo": "Community",
      "pluginName": "deleteFile",
      "version": "1.0.0",
      "id": "5SCtjmoyp",
      "position": {
        "x": 852,
        "y": 456
      },
      "fpEnabled": true
    },
    {
      "name": "Remove Stream By Property",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandRemoveStreamByProperty",
      "version": "1.0.0",
      "id": "EuaZPoHlq",
      "position": {
        "x": 912,
        "y": 24
      },
      "fpEnabled": true,
      "inputsDB": {
        "codecType": "subtitle",
        "valuesToRemove": "mov_text",
        "propertyToCheck": "codec_name"
      }
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
      "source": "QfDBUN7OT",
      "sourceHandle": "1",
      "target": "bU5KZPbCE",
      "targetHandle": null,
      "id": "cqo4JrCnh"
    },
    {
      "source": "Sjoe0VMPw",
      "sourceHandle": "1",
      "target": "mRAI66JAd",
      "targetHandle": null,
      "id": "l_7Frbkon"
    },
    {
      "source": "mRAI66JAd",
      "sourceHandle": "1",
      "target": "rGFh1c2P5",
      "targetHandle": null,
      "id": "_VmIaQD46"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "2",
      "target": "RRkl-aiMA",
      "targetHandle": null,
      "id": "be3Q8NR16"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "1",
      "target": "GG3jailrX",
      "targetHandle": null,
      "id": "Hy6B1JWce"
    },
    {
      "source": "85XIJlyOT",
      "sourceHandle": "1",
      "target": "ov5u9NtOB",
      "targetHandle": null,
      "id": "36HusOCNb"
    },
    {
      "source": "ov5u9NtOB",
      "sourceHandle": "1",
      "target": "QfDBUN7OT",
      "targetHandle": null,
      "id": "z5l7R1qK4"
    },
    {
      "source": "ov5u9NtOB",
      "sourceHandle": "3",
      "target": "5SCtjmoyp",
      "targetHandle": null,
      "id": "fC7Xkj9ow"
    },
    {
      "source": "5SCtjmoyp",
      "sourceHandle": "1",
      "target": "Bf8biy1YS",
      "targetHandle": null,
      "id": "FFHDukGcQ"
    },
    {
      "source": "RRkl-aiMA",
      "sourceHandle": "1",
      "target": "6QuhrjnFC",
      "targetHandle": null,
      "id": "VCh8aSQPn"
    },
    {
      "source": "6QuhrjnFC",
      "sourceHandle": "1",
      "target": "EuaZPoHlq",
      "targetHandle": null,
      "id": "s9GgOO8YA"
    },
    {
      "source": "ov5u9NtOB",
      "sourceHandle": "2",
      "target": "QfDBUN7OT",
      "targetHandle": null,
      "id": "QIjG23yQd"
    },
    {
      "source": "EuaZPoHlq",
      "sourceHandle": "1",
      "target": "iX6jNLa8J",
      "targetHandle": null,
      "id": "dcoQi_B9p"
    }
  ]
}
```