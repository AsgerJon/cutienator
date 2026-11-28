"""
The 'cutienator.QtSensors' package provides the cute classes of the part
of Qt named QtSensors, under the name PySide6 has for it.

  from cutienator.QtSensors import QAccelerometerReadingPrivate, QAmbientLightReadingPrivate

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
    'QAccelerometerReadingPrivate',
    'QAmbientLightReadingPrivate',
    'QAmbientTemperatureReadingPrivate',
    'QCompassReadingPrivate',
    'QGyroscopeReadingPrivate',
    'QHumidityReadingPrivate',
    'QIRProximityReadingPrivate',
    'QLidReadingPrivate',
    'QMagnetometerReadingPrivate',
    'QOrientationReadingPrivate',
    'QPressureReadingPrivate',
    'QProximityReadingPrivate',
    'QRotationReadingPrivate',
    'QSensorChangesInterface',
    'QSensorPluginInterface',
    'QSensorReadingPrivate',
    'QTapReadingPrivate',
    'QTiltReadingPrivate',
    'qoutputrange',
    'QLightReadingPrivate',
    'QSensorPrivate',
    'QSensorReading',
    'QAccelerometerPrivate',
    'QAccelerometerReading',
    'QAmbientLightReading',
    'QAmbientTemperatureReading',
    'QCompassReading',
    'QGyroscopeReading',
    'QHumidityReading',
    'QHumiditySensorPrivate',
    'QIRProximityReading',
    'QLidReading',
    'QLightReading',
    'QLightSensorPrivate',
    'QMagnetometerPrivate',
    'QMagnetometerReading',
    'QOrientationReading',
    'QPressureReading',
    'QProximityReading',
    'QRotationReading',
    'QRotationSensorPrivate',
    'QSensor',
    'QSensorFilter',
    'QTapReading',
    'QTapSensorPrivate',
    'QTiltReading',
    'QAccelerometer',
    'QAccelerometerFilter',
    'QAmbientLightFilter',
    'QAmbientLightSensor',
    'QAmbientTemperatureFilter',
    'QAmbientTemperatureSensor',
    'QCompass',
    'QCompassFilter',
    'QGyroscope',
    'QGyroscopeFilter',
    'QHumidityFilter',
    'QHumiditySensor',
    'QIRProximityFilter',
    'QIRProximitySensor',
    'QLidFilter',
    'QLidSensor',
    'QLightFilter',
    'QLightSensor',
    'QMagnetometer',
    'QMagnetometerFilter',
    'QOrientationFilter',
    'QOrientationSensor',
    'QPressureFilter',
    'QPressureSensor',
    'QProximityFilter',
    'QProximitySensor',
    'QRotationFilter',
    'QRotationSensor',
    'QSensorBackend',
    'QSensorBackendFactory',
    'QTapFilter',
    'QTapSensor',
    'QTiltFilter',
    'QTiltSensor',
    'QSensorManager',
    'qoutputrangelist',
    'QFilterList',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_accelerometer_reading_private import QAccelerometerReadingPrivate
  from ._q_ambient_light_reading_private import QAmbientLightReadingPrivate
  from ._q_ambient_temperature_reading_private import QAmbientTemperatureReadingPrivate
  from ._q_compass_reading_private import QCompassReadingPrivate
  from ._q_gyroscope_reading_private import QGyroscopeReadingPrivate
  from ._q_humidity_reading_private import QHumidityReadingPrivate
  from ._q_i_r_proximity_reading_private import QIRProximityReadingPrivate
  from ._q_lid_reading_private import QLidReadingPrivate
  from ._q_magnetometer_reading_private import QMagnetometerReadingPrivate
  from ._q_orientation_reading_private import QOrientationReadingPrivate
  from ._q_pressure_reading_private import QPressureReadingPrivate
  from ._q_proximity_reading_private import QProximityReadingPrivate
  from ._q_rotation_reading_private import QRotationReadingPrivate
  from ._q_sensor_changes_interface import QSensorChangesInterface
  from ._q_sensor_plugin_interface import QSensorPluginInterface
  from ._q_sensor_reading_private import QSensorReadingPrivate
  from ._q_tap_reading_private import QTapReadingPrivate
  from ._q_tilt_reading_private import QTiltReadingPrivate
  from ._qoutputrange import qoutputrange
  from ._q_light_reading_private import QLightReadingPrivate
  from ._q_sensor_private import QSensorPrivate
  from ._q_sensor_reading import QSensorReading
  from ._q_accelerometer_private import QAccelerometerPrivate
  from ._q_accelerometer_reading import QAccelerometerReading
  from ._q_ambient_light_reading import QAmbientLightReading
  from ._q_ambient_temperature_reading import QAmbientTemperatureReading
  from ._q_compass_reading import QCompassReading
  from ._q_gyroscope_reading import QGyroscopeReading
  from ._q_humidity_reading import QHumidityReading
  from ._q_humidity_sensor_private import QHumiditySensorPrivate
  from ._q_i_r_proximity_reading import QIRProximityReading
  from ._q_lid_reading import QLidReading
  from ._q_light_reading import QLightReading
  from ._q_light_sensor_private import QLightSensorPrivate
  from ._q_magnetometer_private import QMagnetometerPrivate
  from ._q_magnetometer_reading import QMagnetometerReading
  from ._q_orientation_reading import QOrientationReading
  from ._q_pressure_reading import QPressureReading
  from ._q_proximity_reading import QProximityReading
  from ._q_rotation_reading import QRotationReading
  from ._q_rotation_sensor_private import QRotationSensorPrivate
  from ._q_sensor import QSensor
  from ._q_sensor_filter import QSensorFilter
  from ._q_tap_reading import QTapReading
  from ._q_tap_sensor_private import QTapSensorPrivate
  from ._q_tilt_reading import QTiltReading
  from ._q_accelerometer import QAccelerometer
  from ._q_accelerometer_filter import QAccelerometerFilter
  from ._q_ambient_light_filter import QAmbientLightFilter
  from ._q_ambient_light_sensor import QAmbientLightSensor
  from ._q_ambient_temperature_filter import QAmbientTemperatureFilter
  from ._q_ambient_temperature_sensor import QAmbientTemperatureSensor
  from ._q_compass import QCompass
  from ._q_compass_filter import QCompassFilter
  from ._q_gyroscope import QGyroscope
  from ._q_gyroscope_filter import QGyroscopeFilter
  from ._q_humidity_filter import QHumidityFilter
  from ._q_humidity_sensor import QHumiditySensor
  from ._q_i_r_proximity_filter import QIRProximityFilter
  from ._q_i_r_proximity_sensor import QIRProximitySensor
  from ._q_lid_filter import QLidFilter
  from ._q_lid_sensor import QLidSensor
  from ._q_light_filter import QLightFilter
  from ._q_light_sensor import QLightSensor
  from ._q_magnetometer import QMagnetometer
  from ._q_magnetometer_filter import QMagnetometerFilter
  from ._q_orientation_filter import QOrientationFilter
  from ._q_orientation_sensor import QOrientationSensor
  from ._q_pressure_filter import QPressureFilter
  from ._q_pressure_sensor import QPressureSensor
  from ._q_proximity_filter import QProximityFilter
  from ._q_proximity_sensor import QProximitySensor
  from ._q_rotation_filter import QRotationFilter
  from ._q_rotation_sensor import QRotationSensor
  from ._q_sensor_backend import QSensorBackend
  from ._q_sensor_backend_factory import QSensorBackendFactory
  from ._q_tap_filter import QTapFilter
  from ._q_tap_sensor import QTapSensor
  from ._q_tilt_filter import QTiltFilter
  from ._q_tilt_sensor import QTiltSensor
  from ._q_sensor_manager import QSensorManager
  from ._qoutputrange import qoutputrangelist
  from ._q_sensor_filter import QFilterList
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAccelerometerReadingPrivate': '_q_accelerometer_reading_private',
      'QAmbientLightReadingPrivate': '_q_ambient_light_reading_private',
      'QAmbientTemperatureReadingPrivate': '_q_ambient_temperature_reading_private',
      'QCompassReadingPrivate': '_q_compass_reading_private',
      'QGyroscopeReadingPrivate': '_q_gyroscope_reading_private',
      'QHumidityReadingPrivate': '_q_humidity_reading_private',
      'QIRProximityReadingPrivate': '_q_i_r_proximity_reading_private',
      'QLidReadingPrivate': '_q_lid_reading_private',
      'QMagnetometerReadingPrivate': '_q_magnetometer_reading_private',
      'QOrientationReadingPrivate': '_q_orientation_reading_private',
      'QPressureReadingPrivate': '_q_pressure_reading_private',
      'QProximityReadingPrivate': '_q_proximity_reading_private',
      'QRotationReadingPrivate': '_q_rotation_reading_private',
      'QSensorChangesInterface': '_q_sensor_changes_interface',
      'QSensorPluginInterface': '_q_sensor_plugin_interface',
      'QSensorReadingPrivate': '_q_sensor_reading_private',
      'QTapReadingPrivate': '_q_tap_reading_private',
      'QTiltReadingPrivate': '_q_tilt_reading_private',
      'qoutputrange': '_qoutputrange',
      'QLightReadingPrivate': '_q_light_reading_private',
      'QSensorPrivate': '_q_sensor_private',
      'QSensorReading': '_q_sensor_reading',
      'QAccelerometerPrivate': '_q_accelerometer_private',
      'QAccelerometerReading': '_q_accelerometer_reading',
      'QAmbientLightReading': '_q_ambient_light_reading',
      'QAmbientTemperatureReading': '_q_ambient_temperature_reading',
      'QCompassReading': '_q_compass_reading',
      'QGyroscopeReading': '_q_gyroscope_reading',
      'QHumidityReading': '_q_humidity_reading',
      'QHumiditySensorPrivate': '_q_humidity_sensor_private',
      'QIRProximityReading': '_q_i_r_proximity_reading',
      'QLidReading': '_q_lid_reading',
      'QLightReading': '_q_light_reading',
      'QLightSensorPrivate': '_q_light_sensor_private',
      'QMagnetometerPrivate': '_q_magnetometer_private',
      'QMagnetometerReading': '_q_magnetometer_reading',
      'QOrientationReading': '_q_orientation_reading',
      'QPressureReading': '_q_pressure_reading',
      'QProximityReading': '_q_proximity_reading',
      'QRotationReading': '_q_rotation_reading',
      'QRotationSensorPrivate': '_q_rotation_sensor_private',
      'QSensor': '_q_sensor',
      'QSensorFilter': '_q_sensor_filter',
      'QTapReading': '_q_tap_reading',
      'QTapSensorPrivate': '_q_tap_sensor_private',
      'QTiltReading': '_q_tilt_reading',
      'QAccelerometer': '_q_accelerometer',
      'QAccelerometerFilter': '_q_accelerometer_filter',
      'QAmbientLightFilter': '_q_ambient_light_filter',
      'QAmbientLightSensor': '_q_ambient_light_sensor',
      'QAmbientTemperatureFilter': '_q_ambient_temperature_filter',
      'QAmbientTemperatureSensor': '_q_ambient_temperature_sensor',
      'QCompass': '_q_compass',
      'QCompassFilter': '_q_compass_filter',
      'QGyroscope': '_q_gyroscope',
      'QGyroscopeFilter': '_q_gyroscope_filter',
      'QHumidityFilter': '_q_humidity_filter',
      'QHumiditySensor': '_q_humidity_sensor',
      'QIRProximityFilter': '_q_i_r_proximity_filter',
      'QIRProximitySensor': '_q_i_r_proximity_sensor',
      'QLidFilter': '_q_lid_filter',
      'QLidSensor': '_q_lid_sensor',
      'QLightFilter': '_q_light_filter',
      'QLightSensor': '_q_light_sensor',
      'QMagnetometer': '_q_magnetometer',
      'QMagnetometerFilter': '_q_magnetometer_filter',
      'QOrientationFilter': '_q_orientation_filter',
      'QOrientationSensor': '_q_orientation_sensor',
      'QPressureFilter': '_q_pressure_filter',
      'QPressureSensor': '_q_pressure_sensor',
      'QProximityFilter': '_q_proximity_filter',
      'QProximitySensor': '_q_proximity_sensor',
      'QRotationFilter': '_q_rotation_filter',
      'QRotationSensor': '_q_rotation_sensor',
      'QSensorBackend': '_q_sensor_backend',
      'QSensorBackendFactory': '_q_sensor_backend_factory',
      'QTapFilter': '_q_tap_filter',
      'QTapSensor': '_q_tap_sensor',
      'QTiltFilter': '_q_tilt_filter',
      'QTiltSensor': '_q_tilt_sensor',
      'QSensorManager': '_q_sensor_manager',
      'qoutputrangelist': '_qoutputrange',
      'QFilterList': '_q_sensor_filter',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSensors import QFilterList'. Python calls
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
