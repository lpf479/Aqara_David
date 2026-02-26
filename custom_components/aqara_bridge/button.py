import logging
from homeassistant.components.button import ButtonEntity

from .core.aiot_manager import AiotManager, AiotEntityBase
from .core.const import DOMAIN, HASS_DATA_AIOT_MANAGER

_LOGGER = logging.getLogger(__name__)

TYPE = "button"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {"default": AiotButtonEntity}
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotButtonEntity(AiotEntityBase, ButtonEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)

    async def async_press(self) -> None:
        """Handle the button press."""
        resource_key = list(self._res_params.keys())[0]
        resource_id = self._res_params[resource_key][0]
        await self._device.write_resource(resource_id, 1)
