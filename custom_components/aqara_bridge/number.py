import logging
from homeassistant.components.number import NumberEntity

from .core.aiot_manager import (
    AiotManager,
    AiotEntityBase,
)
from .core.const import (
    DOMAIN,
    HASS_DATA_AIOT_MANAGER,
)

_LOGGER = logging.getLogger(__name__)

TYPE = "number"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {"default": AiotNumberEntity}
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotNumberEntity(AiotEntityBase, NumberEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_native_min_value = kwargs.get("min_value", 0)
        self._attr_native_max_value = kwargs.get("max_value", 100)
        self._attr_native_step = kwargs.get("step", 1)
        self._attr_native_unit_of_measurement = kwargs.get("unit_of_measurement")

    async def async_set_native_value(self, value: float) -> None:
        """Set new value."""
        resource_key = list(self._res_params.keys())[0]
        resource_id = self._res_params[resource_key][0]
        await self._device.write_resource(resource_id, int(value))
