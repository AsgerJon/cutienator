"""
The 'cutienator.QtPositioningQuick' package provides the cute classes of
the part of Qt named QtPositioningQuick, under the name PySide6 has for
it.

  from cutienator.QtPositioningQuick import QDeclarativeGeoAddress, QDeclarativePluginParameter

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
    'QDeclarativeGeoAddress',
    'QDeclarativePluginParameter',
    'QGeoAddressForeign',
    'QGeoCircleForeign',
    'QGeoCoordinateForeign',
    'QGeoCoordinateObjectForeign',
    'QGeoLocationForeign',
    'QGeoPathForeign',
    'QGeoPolygonForeign',
    'QGeoPositionInfoForeign',
    'QGeoRectangleForeign',
    'QGeoSatelliteInfoForeign',
    'QGeoShapeForeign',
    'QGeoSatelliteInfoDerived',
    'QDeclarativePosition',
    'QDeclarativeSatelliteSource',
    'QDeclarativeGeoLocation',
    'QDeclarativePositionSource',
    'LocationSingleton',
    'QQuickGeoCoordinateAnimation',
    'QQuickGeoCoordinateAnimationPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_declarative_geo_address import QDeclarativeGeoAddress
  from ._q_declarative_plugin_parameter import QDeclarativePluginParameter
  from ._q_geo_address_foreign import QGeoAddressForeign
  from ._q_geo_circle_foreign import QGeoCircleForeign
  from ._q_geo_coordinate_foreign import QGeoCoordinateForeign
  from ._q_geo_coordinate_object_foreign import QGeoCoordinateObjectForeign
  from ._q_geo_location_foreign import QGeoLocationForeign
  from ._q_geo_path_foreign import QGeoPathForeign
  from ._q_geo_polygon_foreign import QGeoPolygonForeign
  from ._q_geo_position_info_foreign import QGeoPositionInfoForeign
  from ._q_geo_rectangle_foreign import QGeoRectangleForeign
  from ._q_geo_satellite_info_foreign import QGeoSatelliteInfoForeign
  from ._q_geo_shape_foreign import QGeoShapeForeign
  from ._q_geo_satellite_info_derived import QGeoSatelliteInfoDerived
  from ._q_declarative_position import QDeclarativePosition
  from ._q_declarative_satellite_source import QDeclarativeSatelliteSource
  from ._q_declarative_geo_location import QDeclarativeGeoLocation
  from ._q_declarative_position_source import QDeclarativePositionSource
  from ._location_singleton import LocationSingleton
  from ._q_quick_geo_coordinate_animation import QQuickGeoCoordinateAnimation
  from ._q_quick_geo_coordinate_animation_private import QQuickGeoCoordinateAnimationPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QDeclarativeGeoAddress': '_q_declarative_geo_address',
      'QDeclarativePluginParameter': '_q_declarative_plugin_parameter',
      'QGeoAddressForeign': '_q_geo_address_foreign',
      'QGeoCircleForeign': '_q_geo_circle_foreign',
      'QGeoCoordinateForeign': '_q_geo_coordinate_foreign',
      'QGeoCoordinateObjectForeign': '_q_geo_coordinate_object_foreign',
      'QGeoLocationForeign': '_q_geo_location_foreign',
      'QGeoPathForeign': '_q_geo_path_foreign',
      'QGeoPolygonForeign': '_q_geo_polygon_foreign',
      'QGeoPositionInfoForeign': '_q_geo_position_info_foreign',
      'QGeoRectangleForeign': '_q_geo_rectangle_foreign',
      'QGeoSatelliteInfoForeign': '_q_geo_satellite_info_foreign',
      'QGeoShapeForeign': '_q_geo_shape_foreign',
      'QGeoSatelliteInfoDerived': '_q_geo_satellite_info_derived',
      'QDeclarativePosition': '_q_declarative_position',
      'QDeclarativeSatelliteSource': '_q_declarative_satellite_source',
      'QDeclarativeGeoLocation': '_q_declarative_geo_location',
      'QDeclarativePositionSource': '_q_declarative_position_source',
      'LocationSingleton': '_location_singleton',
      'QQuickGeoCoordinateAnimation': '_q_quick_geo_coordinate_animation',
      'QQuickGeoCoordinateAnimationPrivate': '_q_quick_geo_coordinate_animation_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtPositioningQuick import QQuickGeoCoordinateAnimationPrivate'. Python calls
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
