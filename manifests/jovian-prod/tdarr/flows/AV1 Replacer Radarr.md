```
{
  "_id": "UYh60Jd4w",
  "name": "AV1 Replacer Radarr",
  "description": "AV1 Replacer Radarr",
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
        "y": -324
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
        "y": -204
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
        "x": 936,
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
        "x": 936,
        "y": 216
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
        "x": 936,
        "y": 156
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
        "x": 936,
        "y": 276
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
        "x": 720,
        "y": 492
      },
      "fpEnabled": true,
      "inputsDB": {
        "arr": "radarr",
        "arr_host": "https://radarr.jovian.local.sch-apps.com",
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
        "x": 720,
        "y": 432
      },
      "fpEnabled": true
    },
    {
      "name": "Copy to Working Directory",
      "sourceRepo": "Community",
      "pluginName": "copyToWorkDirectory",
      "version": "1.0.0",
      "id": "Xi4WXoqHW",
      "position": {
        "x": 936,
        "y": -84
      },
      "fpEnabled": true
    },
    {
      "name": "Add To Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedAdd",
      "version": "1.0.0",
      "id": "LbIIQY0eT",
      "position": {
        "x": 744,
        "y": -84
      },
      "fpEnabled": true
    },
    {
      "name": "Check Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedCheck",
      "version": "1.0.0",
      "id": "Y9cCOtnCa",
      "position": {
        "x": 840,
        "y": -276
      },
      "fpEnabled": true
    },
    {
      "name": "Compare File Size",
      "sourceRepo": "Community",
      "pluginName": "compareFileSize",
      "version": "1.0.0",
      "id": "iU-R98DkF",
      "position": {
        "x": 828,
        "y": 360
      },
      "fpEnabled": true
    },
    {
      "name": "Add To Skiplist",
      "sourceRepo": "Community",
      "pluginName": "processedAdd",
      "version": "1.0.0",
      "id": "VBGYkzOQV",
      "position": {
        "x": 900,
        "y": 492
      },
      "fpEnabled": true
    },
    {
      "name": "Delete File",
      "sourceRepo": "Community",
      "pluginName": "deleteFile",
      "version": "1.0.0",
      "id": "BsnjXu0UJ",
      "position": {
        "x": 900,
        "y": 432
      },
      "fpEnabled": true
    },
    {
      "name": "Remove Stream By Property",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandRemoveStreamByProperty",
      "version": "1.0.0",
      "id": "VW-z_I6Pk",
      "position": {
        "x": 936,
        "y": 24
      },
      "fpEnabled": true,
      "inputsDB": {
        "codecType": "subtitle",
        "valuesToRemove": "mov_text"
      }
    },
    {
      "name": "Remove Data Streams",
      "sourceRepo": "Community",
      "pluginName": "ffmpegCommandRemoveDataStreams",
      "version": "1.0.0",
      "id": "-q5IJ0ePU",
      "position": {
        "x": 936,
        "y": 96
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
      "source": "QfDBUN7OT",
      "sourceHandle": "1",
      "target": "bU5KZPbCE",
      "targetHandle": null,
      "id": "cqo4JrCnh"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "2",
      "target": "Xi4WXoqHW",
      "targetHandle": null,
      "id": "skjNbKzuM"
    },
    {
      "source": "Xi4WXoqHW",
      "sourceHandle": "1",
      "target": "6QuhrjnFC",
      "targetHandle": null,
      "id": "rjC5EUvG2"
    },
    {
      "source": "Sjoe0VMPw",
      "sourceHandle": "1",
      "target": "Y9cCOtnCa",
      "targetHandle": null,
      "id": "QuiCyV6w-"
    },
    {
      "source": "Y9cCOtnCa",
      "sourceHandle": "1",
      "target": "rGFh1c2P5",
      "targetHandle": null,
      "id": "AjCiCaOFh"
    },
    {
      "source": "rGFh1c2P5",
      "sourceHandle": "1",
      "target": "LbIIQY0eT",
      "targetHandle": null,
      "id": "fiPCeXInM"
    },
    {
      "source": "85XIJlyOT",
      "sourceHandle": "1",
      "target": "iU-R98DkF",
      "targetHandle": null,
      "id": "8CtmIh-Cx"
    },
    {
      "source": "iU-R98DkF",
      "sourceHandle": "1",
      "target": "QfDBUN7OT",
      "targetHandle": null,
      "id": "tfsXur-IM"
    },
    {
      "source": "iU-R98DkF",
      "sourceHandle": "3",
      "target": "BsnjXu0UJ",
      "targetHandle": null,
      "id": "GcVU3Bui5"
    },
    {
      "source": "BsnjXu0UJ",
      "sourceHandle": "1",
      "target": "VBGYkzOQV",
      "targetHandle": null,
      "id": "HCZTU7Old"
    },
    {
      "source": "6QuhrjnFC",
      "sourceHandle": "1",
      "target": "VW-z_I6Pk",
      "targetHandle": null,
      "id": "kOaJhRy2V"
    },
    {
      "source": "iU-R98DkF",
      "sourceHandle": "2",
      "target": "QfDBUN7OT",
      "targetHandle": null,
      "id": "xw2AY608W"
    },
    {
      "source": "VW-z_I6Pk",
      "sourceHandle": "1",
      "target": "-q5IJ0ePU",
      "targetHandle": null,
      "id": "OxMXqx5U3"
    },
    {
      "source": "-q5IJ0ePU",
      "sourceHandle": "1",
      "target": "iX6jNLa8J",
      "targetHandle": null,
      "id": "SBN_oaRE2"
    }
  ]
}
```