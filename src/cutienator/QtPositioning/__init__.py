"""
The 'cutienator.QtPositioning' package provides the cute classes of the
part of Qt named QtPositioning, under the name PySide6 has for it.

  from cutienator.QtPositioning import QPendingGeoPositionInfo, SatelliteInfo

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
    'QPendingGeoPositionInfo',
    'SatelliteInfo',
    'QGeoAddressPrivate',
    'QGeoLocationPrivate',
    'QDoubleVector2D',
    'QDoubleVector3D',
    'QClipperUtils',
    'QGeoAddress',
    'QDoubleMatrix4x4',
    'QGeoCoordinate',
    'QGeoCoordinatePrivate',
    'QGeoPositionInfoSourceFactory',
    'QGeoSatelliteInfo',
    'QGeoSatelliteInfoPrivate',
    'QGeoSatelliteInfoSourcePrivate',
    'QGeoCoordinateObject',
    'QGeoMercatorCoordinatePrivate',
    'QGeoPositionInfo',
    'QGeoPositionInfoPrivate',
    'QGeoSatelliteInfoSource',
    'QGeoShape',
    'QGeoShapePrivate',
    'QNmeaSatelliteInfoUpdate',
    'QWebMercator',
    'QGeoAreaMonitorInfo',
    'QGeoCircle',
    'QGeoCirclePrivate',
    'QGeoLocation',
    'QGeoPath',
    'QGeoPathPrivateBase',
    'QGeoPolygon',
    'QGeoPositionInfoSource',
    'QGeoPositionInfoSourcePrivate',
    'QGeoRectangle',
    'QGeoRectanglePrivate',
    'QLocationUtils',
    'QNmeaSatelliteInfoSource',
    'QGeoAreaMonitorSource',
    'QGeoPathEager',
    'QGeoPathPrivate',
    'QGeoPolygonEager',
    'QGeoPolygonPrivate',
    'QNmeaPositionInfoSource',
    'QNmeaSatelliteInfoSourcePrivate',
    'QGeoPathPrivateEager',
    'QGeoPolygonPrivateEager',
    'QNmeaPositionInfoSourcePrivate',
    'QNmeaSatelliteReader',
    'QNmeaReader',
    'QNmeaSatelliteRealTimeReader',
    'QNmeaSatelliteSimulationReader',
    'QNmeaRealTimeReader',
    'QNmeaSimulatedReader',
    'PolygonVector',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_pending_geo_position_info import QPendingGeoPositionInfo
  from ._satellite_info import SatelliteInfo
  from ._q_geo_address_private import QGeoAddressPrivate
  from ._q_geo_location_private import QGeoLocationPrivate
  from ._q_double_vector2_d import QDoubleVector2D
  from ._q_double_vector3_d import QDoubleVector3D
  from ._q_clipper_utils import QClipperUtils
  from ._q_geo_address import QGeoAddress
  from ._q_double_matrix4x4 import QDoubleMatrix4x4
  from ._q_geo_coordinate import QGeoCoordinate
  from ._q_geo_coordinate_private import QGeoCoordinatePrivate
  from ._q_geo_position_info_source_factory import QGeoPositionInfoSourceFactory
  from ._q_geo_satellite_info import QGeoSatelliteInfo
  from ._q_geo_satellite_info_private import QGeoSatelliteInfoPrivate
  from ._q_geo_satellite_info_source_private import QGeoSatelliteInfoSourcePrivate
  from ._q_geo_coordinate_object import QGeoCoordinateObject
  from ._q_geo_mercator_coordinate_private import QGeoMercatorCoordinatePrivate
  from ._q_geo_position_info import QGeoPositionInfo
  from ._q_geo_position_info_private import QGeoPositionInfoPrivate
  from ._q_geo_satellite_info_source import QGeoSatelliteInfoSource
  from ._q_geo_shape import QGeoShape
  from ._q_geo_shape_private import QGeoShapePrivate
  from ._q_nmea_satellite_info_update import QNmeaSatelliteInfoUpdate
  from ._q_web_mercator import QWebMercator
  from ._q_geo_area_monitor_info import QGeoAreaMonitorInfo
  from ._q_geo_circle import QGeoCircle
  from ._q_geo_circle_private import QGeoCirclePrivate
  from ._q_geo_location import QGeoLocation
  from ._q_geo_path import QGeoPath
  from ._q_geo_path_private_base import QGeoPathPrivateBase
  from ._q_geo_polygon import QGeoPolygon
  from ._q_geo_position_info_source import QGeoPositionInfoSource
  from ._q_geo_position_info_source_private import QGeoPositionInfoSourcePrivate
  from ._q_geo_rectangle import QGeoRectangle
  from ._q_geo_rectangle_private import QGeoRectanglePrivate
  from ._q_location_utils import QLocationUtils
  from ._q_nmea_satellite_info_source import QNmeaSatelliteInfoSource
  from ._q_geo_area_monitor_source import QGeoAreaMonitorSource
  from ._q_geo_path_eager import QGeoPathEager
  from ._q_geo_path_private import QGeoPathPrivate
  from ._q_geo_polygon_eager import QGeoPolygonEager
  from ._q_geo_polygon_private import QGeoPolygonPrivate
  from ._q_nmea_position_info_source import QNmeaPositionInfoSource
  from ._q_nmea_satellite_info_source_private import QNmeaSatelliteInfoSourcePrivate
  from ._q_geo_path_private_eager import QGeoPathPrivateEager
  from ._q_geo_polygon_private_eager import QGeoPolygonPrivateEager
  from ._q_nmea_position_info_source_private import QNmeaPositionInfoSourcePrivate
  from ._q_nmea_satellite_reader import QNmeaSatelliteReader
  from ._q_nmea_reader import QNmeaReader
  from ._q_nmea_satellite_real_time_reader import QNmeaSatelliteRealTimeReader
  from ._q_nmea_satellite_simulation_reader import QNmeaSatelliteSimulationReader
  from ._q_nmea_real_time_reader import QNmeaRealTimeReader
  from ._q_nmea_simulated_reader import QNmeaSimulatedReader
  from ._q_double_vector3_d import PolygonVector
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QPendingGeoPositionInfo': '_q_pending_geo_position_info',
      'SatelliteInfo': '_satellite_info',
      'QGeoAddressPrivate': '_q_geo_address_private',
      'QGeoLocationPrivate': '_q_geo_location_private',
      'QDoubleVector2D': '_q_double_vector2_d',
      'QDoubleVector3D': '_q_double_vector3_d',
      'QClipperUtils': '_q_clipper_utils',
      'QGeoAddress': '_q_geo_address',
      'QDoubleMatrix4x4': '_q_double_matrix4x4',
      'QGeoCoordinate': '_q_geo_coordinate',
      'QGeoCoordinatePrivate': '_q_geo_coordinate_private',
      'QGeoPositionInfoSourceFactory': '_q_geo_position_info_source_factory',
      'QGeoSatelliteInfo': '_q_geo_satellite_info',
      'QGeoSatelliteInfoPrivate': '_q_geo_satellite_info_private',
      'QGeoSatelliteInfoSourcePrivate': '_q_geo_satellite_info_source_private',
      'QGeoCoordinateObject': '_q_geo_coordinate_object',
      'QGeoMercatorCoordinatePrivate': '_q_geo_mercator_coordinate_private',
      'QGeoPositionInfo': '_q_geo_position_info',
      'QGeoPositionInfoPrivate': '_q_geo_position_info_private',
      'QGeoSatelliteInfoSource': '_q_geo_satellite_info_source',
      'QGeoShape': '_q_geo_shape',
      'QGeoShapePrivate': '_q_geo_shape_private',
      'QNmeaSatelliteInfoUpdate': '_q_nmea_satellite_info_update',
      'QWebMercator': '_q_web_mercator',
      'QGeoAreaMonitorInfo': '_q_geo_area_monitor_info',
      'QGeoCircle': '_q_geo_circle',
      'QGeoCirclePrivate': '_q_geo_circle_private',
      'QGeoLocation': '_q_geo_location',
      'QGeoPath': '_q_geo_path',
      'QGeoPathPrivateBase': '_q_geo_path_private_base',
      'QGeoPolygon': '_q_geo_polygon',
      'QGeoPositionInfoSource': '_q_geo_position_info_source',
      'QGeoPositionInfoSourcePrivate': '_q_geo_position_info_source_private',
      'QGeoRectangle': '_q_geo_rectangle',
      'QGeoRectanglePrivate': '_q_geo_rectangle_private',
      'QLocationUtils': '_q_location_utils',
      'QNmeaSatelliteInfoSource': '_q_nmea_satellite_info_source',
      'QGeoAreaMonitorSource': '_q_geo_area_monitor_source',
      'QGeoPathEager': '_q_geo_path_eager',
      'QGeoPathPrivate': '_q_geo_path_private',
      'QGeoPolygonEager': '_q_geo_polygon_eager',
      'QGeoPolygonPrivate': '_q_geo_polygon_private',
      'QNmeaPositionInfoSource': '_q_nmea_position_info_source',
      'QNmeaSatelliteInfoSourcePrivate': '_q_nmea_satellite_info_source_private',
      'QGeoPathPrivateEager': '_q_geo_path_private_eager',
      'QGeoPolygonPrivateEager': '_q_geo_polygon_private_eager',
      'QNmeaPositionInfoSourcePrivate': '_q_nmea_position_info_source_private',
      'QNmeaSatelliteReader': '_q_nmea_satellite_reader',
      'QNmeaReader': '_q_nmea_reader',
      'QNmeaSatelliteRealTimeReader': '_q_nmea_satellite_real_time_reader',
      'QNmeaSatelliteSimulationReader': '_q_nmea_satellite_simulation_reader',
      'QNmeaRealTimeReader': '_q_nmea_real_time_reader',
      'QNmeaSimulatedReader': '_q_nmea_simulated_reader',
      'PolygonVector': '_q_double_vector3_d',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtPositioning import PolygonVector'. Python calls
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
