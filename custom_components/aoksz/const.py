# const.py

from datetime import timedelta
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_SCAN_INTERVAL, CONF_DEVICE_ID

DOMAIN = "aoksz"
DEFAULT_PORT = 26
DEFAULT_SLAVE_ID = 1
SCAN_INTERVAL = timedelta(seconds=1)  # seconds

DEFAULT_SCAN_INTERVAL = 10

ERRORS_MAP = {
    "cannot_connect": "无法连接",
    "modbus_error": "Modbus通信错误",
    "invalid_auth": "认证错误",
    "unknown": "未知错误"
}
