import logging
from homeassistant.components.select import SelectEntity

from .core.aiot_manager import AiotManager, AiotEntityBase
from .core.const import DOMAIN, HASS_DATA_AIOT_MANAGER

_LOGGER = logging.getLogger(__name__)

TYPE = "select"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {"default": AiotSelectEntity}
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotSelectEntity(AiotEntityBase, SelectEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_options = kwargs.get("options", [])

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        if option not in self._attr_options:
            _LOGGER.error("Invalid option: %s", option)
            return
        
        resource_key = list(self._res_params.keys())[0]
        resource_id = self._res_params[resource_key][0]
        
        option_index = self._attr_options.index(option)
        await self._device.write_resource(resource_id, option_index)
