# CPT Framework Foundation
"""
Default settings. Override these with settings in the module pointed to
by the PROJECT_SETTINGS_MODULE environment variable.
"""

####################
# CORE             #
####################

# 用例执行的平台
PLATFORMS = [
    {'mobile_model': 'MI6', 'os_api_name': 'MIUI10', 'screen_resolution': ''}
]

# 时区
TIME_ZONE = 'Asia/Shanghai'

MOBILE_POOL = {
    'MI6': {
        'devices'
    }
}

#
MOBILE_DRIVER_CREATORS = {

}
