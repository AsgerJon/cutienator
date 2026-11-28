"""
The 'cutienator.QtSensorsQuick' package provides the cute classes of the
part of Qt named QtSensorsQuick, under the name PySide6 has for it.

  from cutienator.QtSensorsQuick import QmlSensor, QmlSensorGlobal

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QmlSensor',
    'QmlSensorGlobal',
    'QmlSensorOutputRange',
    'QmlSensorRange',
    'QmlSensorReading',
    'QmlAccelerometer',
    'QmlAmbientLightSensor',
    'QmlAmbientTemperatureSensor',
    'QmlCompass',
    'QmlGyroscope',
    'QmlHumiditySensor',
    'QmlIRProximitySensor',
    'QmlLidSensor',
    'QmlLightSensor',
    'QmlMagnetometer',
    'QmlOrientationSensor',
    'QmlPressureSensor',
    'QmlProximitySensor',
    'QmlRotationSensor',
    'QmlTapSensor',
    'QmlTiltSensor',
    'QmlAccelerometerReading',
    'QmlAmbientLightSensorReading',
    'QmlAmbientTemperatureReading',
    'QmlCompassReading',
    'QmlGyroscopeReading',
    'QmlHumidityReading',
    'QmlIRProximitySensorReading',
    'QmlLidReading',
    'QmlLightSensorReading',
    'QmlMagnetometerReading',
    'QmlOrientationSensorReading',
    'QmlPressureReading',
    'QmlProximitySensorReading',
    'QmlRotationSensorReading',
    'QmlTapSensorReading',
    'QmlTiltSensorReading',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._qml_sensor import QmlSensor
  from ._qml_sensor_global import QmlSensorGlobal
  from ._qml_sensor_output_range import QmlSensorOutputRange
  from ._qml_sensor_range import QmlSensorRange
  from ._qml_sensor_reading import QmlSensorReading
  from ._qml_accelerometer import QmlAccelerometer
  from ._qml_ambient_light_sensor import QmlAmbientLightSensor
  from ._qml_ambient_temperature_sensor import QmlAmbientTemperatureSensor
  from ._qml_compass import QmlCompass
  from ._qml_gyroscope import QmlGyroscope
  from ._qml_humidity_sensor import QmlHumiditySensor
  from ._qml_i_r_proximity_sensor import QmlIRProximitySensor
  from ._qml_lid_sensor import QmlLidSensor
  from ._qml_light_sensor import QmlLightSensor
  from ._qml_magnetometer import QmlMagnetometer
  from ._qml_orientation_sensor import QmlOrientationSensor
  from ._qml_pressure_sensor import QmlPressureSensor
  from ._qml_proximity_sensor import QmlProximitySensor
  from ._qml_rotation_sensor import QmlRotationSensor
  from ._qml_tap_sensor import QmlTapSensor
  from ._qml_tilt_sensor import QmlTiltSensor
  from ._qml_accelerometer_reading import QmlAccelerometerReading
  from ._qml_ambient_light_sensor_reading import QmlAmbientLightSensorReading
  from ._qml_ambient_temperature_reading import QmlAmbientTemperatureReading
  from ._qml_compass_reading import QmlCompassReading
  from ._qml_gyroscope_reading import QmlGyroscopeReading
  from ._qml_humidity_reading import QmlHumidityReading
  from ._qml_i_r_proximity_sensor_reading import QmlIRProximitySensorReading
  from ._qml_lid_reading import QmlLidReading
  from ._qml_light_sensor_reading import QmlLightSensorReading
  from ._qml_magnetometer_reading import QmlMagnetometerReading
  from ._qml_orientation_sensor_reading import QmlOrientationSensorReading
  from ._qml_pressure_reading import QmlPressureReading
  from ._qml_proximity_sensor_reading import QmlProximitySensorReading
  from ._qml_rotation_sensor_reading import QmlRotationSensorReading
  from ._qml_tap_sensor_reading import QmlTapSensorReading
  from ._qml_tilt_sensor_reading import QmlTiltSensorReading
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QmlSensor': '_qml_sensor',
      'QmlSensorGlobal': '_qml_sensor_global',
      'QmlSensorOutputRange': '_qml_sensor_output_range',
      'QmlSensorRange': '_qml_sensor_range',
      'QmlSensorReading': '_qml_sensor_reading',
      'QmlAccelerometer': '_qml_accelerometer',
      'QmlAmbientLightSensor': '_qml_ambient_light_sensor',
      'QmlAmbientTemperatureSensor': '_qml_ambient_temperature_sensor',
      'QmlCompass': '_qml_compass',
      'QmlGyroscope': '_qml_gyroscope',
      'QmlHumiditySensor': '_qml_humidity_sensor',
      'QmlIRProximitySensor': '_qml_i_r_proximity_sensor',
      'QmlLidSensor': '_qml_lid_sensor',
      'QmlLightSensor': '_qml_light_sensor',
      'QmlMagnetometer': '_qml_magnetometer',
      'QmlOrientationSensor': '_qml_orientation_sensor',
      'QmlPressureSensor': '_qml_pressure_sensor',
      'QmlProximitySensor': '_qml_proximity_sensor',
      'QmlRotationSensor': '_qml_rotation_sensor',
      'QmlTapSensor': '_qml_tap_sensor',
      'QmlTiltSensor': '_qml_tilt_sensor',
      'QmlAccelerometerReading': '_qml_accelerometer_reading',
      'QmlAmbientLightSensorReading': '_qml_ambient_light_sensor_reading',
      'QmlAmbientTemperatureReading': '_qml_ambient_temperature_reading',
      'QmlCompassReading': '_qml_compass_reading',
      'QmlGyroscopeReading': '_qml_gyroscope_reading',
      'QmlHumidityReading': '_qml_humidity_reading',
      'QmlIRProximitySensorReading': '_qml_i_r_proximity_sensor_reading',
      'QmlLidReading': '_qml_lid_reading',
      'QmlLightSensorReading': '_qml_light_sensor_reading',
      'QmlMagnetometerReading': '_qml_magnetometer_reading',
      'QmlOrientationSensorReading': '_qml_orientation_sensor_reading',
      'QmlPressureReading': '_qml_pressure_reading',
      'QmlProximitySensorReading': '_qml_proximity_sensor_reading',
      'QmlRotationSensorReading': '_qml_rotation_sensor_reading',
      'QmlTapSensorReading': '_qml_tap_sensor_reading',
      'QmlTiltSensorReading': '_qml_tilt_sensor_reading',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSensorsQuick import QmlTiltSensorReading'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
