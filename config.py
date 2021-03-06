#! /usr/bin/python3

import os

"""
    Configuration variables for the whole application

	Author : Quentin Bouvet
"""

    # Enable printing debug information
DEBUG = True

    # GPIO configuration
PIR_pin=11          
LEDSWITCH_PIN=17    
PIR_CYCLE_PERIOD=15 # (in seconds)
    # Sleep pattern for PIR activation : activate, sleep at least x[0], activate, sleep at least x[1], ...
PIR_ACTIVATION_SEQUENCE=[4, 5, 10, 20, 30, 60] 


    # Camera settings and file storage
    # general
dcim="/opt/dcim"
CAM_WARMUP_TIME=0.2
    # Photo
PHOTO_RES=(1296, 972)
PHOTO_QUALITY = 25          # 1-100
    # Video
VIDEO_RES=(1296, 972) 
VIDEO_FPS = 12
VIDEO_QUALITY = 30          # 1-40, "reasonable trade-off between bandwidth and quality being between 20 and 25."
VIDEO_BITRATE = 9000000    # default 17000000, max 25000000

    # Telegram settings
TGTOKEN='674761733:AAHF_pBnumgdXRR1SKe6psQLi1cmWu_AAd0'
PHOTO_SEND_TIMEOUT=30
#TG_DEFAULT_USERS=[  {'conv': 766567777, 'user': 766567777, 'name': 'el_olo'},
#                    {'conv': 185940826, 'user': 185940826, 'name': 'sgpepper'},
#                    {'conv': 668752478, 'user': 668752478, 'name': 'ldunoyer'} ]
TG_DEFAULT_USERS=[ {'conv': 185940826, 'user': 185940826, 'name': 'sgpepper'} ]

    # Webserver settings
PORT=8384
WS_PING_INTERVAL=5
WS_NB_PING_TIMEOUT=12
stream_separator = bytearray.fromhex('00000001')
STREAM_SEPARATOR = bytearray.fromhex('00000001')
STATIC_WEB_RESSOURCES = os.path.join(os.path.dirname(__file__), "static")

    # 
CAMERA_WRAPPER_BUFFER_SIZE = 1024 * 100
