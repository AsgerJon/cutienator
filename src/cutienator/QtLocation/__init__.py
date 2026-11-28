"""
The 'cutienator.QtLocation' package provides the cute classes of the
part of Qt named QtLocation, under the name PySide6 has for it.

  from cutienator.QtLocation import Frustum, QGeoCachedTileDisk

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
    'Frustum',
    'QGeoCachedTileDisk',
    'QGeoCodingManagerEnginePrivate',
    'QGeoCodingManagerPrivate',
    'QGeoMapViewportChangeEvent',
    'QGeoMappingManagerEnginePrivate',
    'QGeoMappingManagerPrivate',
    'QGeoRoutingManagerEnginePrivate',
    'QGeoRoutingManagerPrivate',
    'QGeoTileTexture',
    'QGeoTiledMappingManagerEnginePrivate',
    'QPlaceManagerEnginePrivate',
    'QPlaceReplyPrivate',
    'QGeoRouteRequestPrivate',
    'QPlaceAttributePrivate',
    'QPlaceCategoryPrivate',
    'QPlaceContactDetailPrivate',
    'QPlaceContentRequestPrivate',
    'QPlaceIconPrivate',
    'QPlaceRatingsPrivate',
    'QPlaceSupplierPrivate',
    'QPlaceUserPrivate',
    'QGeoTileSpec',
    'QGeoTileSpecPrivate',
    'QCache3QTileEvictionPolicy',
    'QAbstractGeoTileCache',
    'QDeclarativeMapLineProperties',
    'QDeclarativePluginParameterForeign',
    'QGeoCameraCapabilities',
    'QGeoServiceProviderPrivate',
    'QGeoTileFetcherPrivate',
    'QGeoTiledMapReply',
    'QPlaceAttribute',
    'QPlaceContactDetail',
    'QPlaceRatings',
    'QPlaceReply',
    'QPlaceUser',
    'QDeclarativeContactDetails',
    'QGeoCameraData',
    'QGeoManeuver',
    'QGeoMapType',
    'QGeoTiledMapReplyPrivate',
    'QPlaceIdReply',
    'QPlaceSearchSuggestionReply',
    'QGeoCameraTiles',
    'QGeoFileTileCache',
    'QGeoManeuverDerived',
    'QGeoManeuverPrivate',
    'QGeoMapTypePrivate',
    'QGeoMappingManagerEngine',
    'QGeoProjection',
    'QGeoRouteSegment',
    'QGeoRouteSegmentPrivate',
    'QDeclarativeGeoMapPainterPath',
    'QGeoCameraTilesPrivate',
    'QGeoCodeReply',
    'QGeoMapItemGeometry',
    'QGeoMappingManager',
    'QGeoProjectionWebMercator',
    'QGeoRouteParserOsrmV5Extension',
    'QGeoRouteRequest',
    'QGeoTileFetcher',
    'QPlaceIcon',
    'QPlaceCategory',
    'QPlaceSupplier',
    'QPlaceContent',
    'QPlace',
    'QPlaceContentRequest',
    'QPlaceSearchRequest',
    'QPlaceMatchRequest',
    'QPlaceManagerEngine',
    'QPlaceManager',
    'QPlacePrivate',
    'QPlaceSearchResult',
    'QPlaceSearchResultPrivate',
    'QDeclarativeGeoRouteQuery',
    'QGeoCodeReplyPrivate',
    'QGeoCodingManagerEngine',
    'QGeoRoute',
    'QPlaceContentPrivate',
    'QPlaceContentReply',
    'QPlaceDetailsReply',
    'QPlaceIdReplyUnsupported',
    'QPlaceMatchReply',
    'QPlacePrivateDefault',
    'QPlaceProposedSearchResult',
    'QPlaceProposedSearchResultPrivate',
    'QPlaceReplyUnsupported',
    'QPlaceResult',
    'QPlaceResultPrivate',
    'QPlaceSearchReply',
    'QPlaceSearchRequestPrivate',
    'QPlaceSearchSuggestionReplyUnsupported',
    'QGeoCodingManager',
    'QGeoRouteParserPrivate',
    'QGeoRoutePrivate',
    'QGeoRouteReply',
    'QPlaceContentReplyUnsupported',
    'QPlaceDetailsReplyUnsupported',
    'QPlaceMatchReplyUnsupported',
    'QPlaceSearchReplyUnsupported',
    'QGeoRouteParser',
    'QGeoRouteReplyPrivate',
    'QGeoRoutingManagerEngine',
    'QGeoRouteParserOsrmV5',
    'QGeoRoutingManager',
    'QGeoServiceProvider',
    'QDeclarativeGeoServiceProvider',
    'QDeclarativeGeoServiceProviderRequirements',
    'QGeoServiceProviderFactory',
    'QDeclarativeCategory',
    'QDeclarativeGeoRouteModel',
    'QDeclarativeGeocodeModel',
    'QDeclarativeSearchModelBase',
    'QDeclarativeSupportedCategoriesModel',
    'QGeoTiledMapScene',
    'QMapQuickItemMatrix4x4',
    'QDeclarativeGeoMapItemGroup',
    'QDeclarativeGeoMapItemBase',
    'QDeclarativeGeoMap',
    'QDeclarativeGeoMapItemView',
    'QGeoMap',
    'QGeoMapPrivate',
    'QDeclarativeGeoMapItemTransitionManager',
    'QDeclarativePlace',
    'QDeclarativeSearchSuggestionModel',
    'QDeclarativeCircleMapItem',
    'QDeclarativeGeoJsonData',
    'QDeclarativeGeoMapCopyrightNotice',
    'QDeclarativeGeoMapQuickItem',
    'QDeclarativePlaceContentModel',
    'QDeclarativePolygonMapItem',
    'QDeclarativePolylineMapItem',
    'QDeclarativeRectangleMapItem',
    'QDeclarativeSearchResultModel',
    'QGeoMapPolygonGeometry',
    'QGeoMapPolylineGeometry',
    'QGeoTiledMappingManagerEngine',
    'QGeoTiledMapPrivate',
    'QGeoTiledMap',
    'QDeclarativeCircleMapItemPrivate',
    'QDeclarativePlaceEditorialModel',
    'QDeclarativePlaceImageModel',
    'QDeclarativePlaceReviewModel',
    'QDeclarativePolygonMapItemPrivate',
    'QDeclarativePolylineMapItemPrivate',
    'QDeclarativeRectangleMapItemPrivate',
    'QDeclarativeRouteMapItem',
    'QGeoMapCircleGeometry',
    'QGeoTileRequestManager',
    'QGeoTiledMapScenePrivate',
    'QGeoTiledMapTileContainerNode',
    'QDeclarativeCircleMapItemPrivateCPU',
    'QDeclarativePolygonMapItemPrivateCPU',
    'QDeclarativePolylineMapItemPrivateCPU',
    'QDeclarativeRectangleMapItemPrivateCPU',
    'QGeoTiledMapRootNode',
    'QDeclarativeGeoMapItemUtils',
    'QLocation',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._frustum import Frustum
  from ._q_geo_cached_tile_disk import QGeoCachedTileDisk
  from ._q_geo_coding_manager_engine_private import QGeoCodingManagerEnginePrivate
  from ._q_geo_coding_manager_private import QGeoCodingManagerPrivate
  from ._q_geo_map_viewport_change_event import QGeoMapViewportChangeEvent
  from ._q_geo_mapping_manager_engine_private import QGeoMappingManagerEnginePrivate
  from ._q_geo_mapping_manager_private import QGeoMappingManagerPrivate
  from ._q_geo_routing_manager_engine_private import QGeoRoutingManagerEnginePrivate
  from ._q_geo_routing_manager_private import QGeoRoutingManagerPrivate
  from ._q_geo_tile_texture import QGeoTileTexture
  from ._q_geo_tiled_mapping_manager_engine_private import QGeoTiledMappingManagerEnginePrivate
  from ._q_place_manager_engine_private import QPlaceManagerEnginePrivate
  from ._q_place_reply_private import QPlaceReplyPrivate
  from ._q_geo_route_request_private import QGeoRouteRequestPrivate
  from ._q_place_attribute_private import QPlaceAttributePrivate
  from ._q_place_category_private import QPlaceCategoryPrivate
  from ._q_place_contact_detail_private import QPlaceContactDetailPrivate
  from ._q_place_content_request_private import QPlaceContentRequestPrivate
  from ._q_place_icon_private import QPlaceIconPrivate
  from ._q_place_ratings_private import QPlaceRatingsPrivate
  from ._q_place_supplier_private import QPlaceSupplierPrivate
  from ._q_place_user_private import QPlaceUserPrivate
  from ._q_geo_tile_spec import QGeoTileSpec
  from ._q_geo_tile_spec_private import QGeoTileSpecPrivate
  from ._q_cache3_q_tile_eviction_policy import QCache3QTileEvictionPolicy
  from ._q_abstract_geo_tile_cache import QAbstractGeoTileCache
  from ._q_declarative_map_line_properties import QDeclarativeMapLineProperties
  from ._q_declarative_plugin_parameter_foreign import QDeclarativePluginParameterForeign
  from ._q_geo_camera_capabilities import QGeoCameraCapabilities
  from ._q_geo_service_provider_private import QGeoServiceProviderPrivate
  from ._q_geo_tile_fetcher_private import QGeoTileFetcherPrivate
  from ._q_geo_tiled_map_reply import QGeoTiledMapReply
  from ._q_place_attribute import QPlaceAttribute
  from ._q_place_contact_detail import QPlaceContactDetail
  from ._q_place_ratings import QPlaceRatings
  from ._q_place_reply import QPlaceReply
  from ._q_place_user import QPlaceUser
  from ._q_declarative_contact_details import QDeclarativeContactDetails
  from ._q_geo_camera_data import QGeoCameraData
  from ._q_geo_maneuver import QGeoManeuver
  from ._q_geo_map_type import QGeoMapType
  from ._q_geo_tiled_map_reply_private import QGeoTiledMapReplyPrivate
  from ._q_place_id_reply import QPlaceIdReply
  from ._q_place_search_suggestion_reply import QPlaceSearchSuggestionReply
  from ._q_geo_camera_tiles import QGeoCameraTiles
  from ._q_geo_file_tile_cache import QGeoFileTileCache
  from ._q_geo_maneuver_derived import QGeoManeuverDerived
  from ._q_geo_maneuver_private import QGeoManeuverPrivate
  from ._q_geo_map_type_private import QGeoMapTypePrivate
  from ._q_geo_mapping_manager_engine import QGeoMappingManagerEngine
  from ._q_geo_projection import QGeoProjection
  from ._q_geo_route_segment import QGeoRouteSegment
  from ._q_geo_route_segment_private import QGeoRouteSegmentPrivate
  from ._q_declarative_geo_map_painter_path import QDeclarativeGeoMapPainterPath
  from ._q_geo_camera_tiles_private import QGeoCameraTilesPrivate
  from ._q_geo_code_reply import QGeoCodeReply
  from ._q_geo_map_item_geometry import QGeoMapItemGeometry
  from ._q_geo_mapping_manager import QGeoMappingManager
  from ._q_geo_projection_web_mercator import QGeoProjectionWebMercator
  from ._q_geo_route_parser_osrm_v5_extension import QGeoRouteParserOsrmV5Extension
  from ._q_geo_route_request import QGeoRouteRequest
  from ._q_geo_tile_fetcher import QGeoTileFetcher
  from ._q_place_icon import QPlaceIcon
  from ._q_place_category import QPlaceCategory
  from ._q_place_supplier import QPlaceSupplier
  from ._q_place_content import QPlaceContent
  from ._q_place import QPlace
  from ._q_place_content_request import QPlaceContentRequest
  from ._q_place_search_request import QPlaceSearchRequest
  from ._q_place_match_request import QPlaceMatchRequest
  from ._q_place_manager_engine import QPlaceManagerEngine
  from ._q_place_manager import QPlaceManager
  from ._q_place_private import QPlacePrivate
  from ._q_place_search_result import QPlaceSearchResult
  from ._q_place_search_result_private import QPlaceSearchResultPrivate
  from ._q_declarative_geo_route_query import QDeclarativeGeoRouteQuery
  from ._q_geo_code_reply_private import QGeoCodeReplyPrivate
  from ._q_geo_coding_manager_engine import QGeoCodingManagerEngine
  from ._q_geo_route import QGeoRoute
  from ._q_place_content_private import QPlaceContentPrivate
  from ._q_place_content_reply import QPlaceContentReply
  from ._q_place_details_reply import QPlaceDetailsReply
  from ._q_place_id_reply_unsupported import QPlaceIdReplyUnsupported
  from ._q_place_match_reply import QPlaceMatchReply
  from ._q_place_private_default import QPlacePrivateDefault
  from ._q_place_proposed_search_result import QPlaceProposedSearchResult
  from ._q_place_proposed_search_result_private import QPlaceProposedSearchResultPrivate
  from ._q_place_reply_unsupported import QPlaceReplyUnsupported
  from ._q_place_result import QPlaceResult
  from ._q_place_result_private import QPlaceResultPrivate
  from ._q_place_search_reply import QPlaceSearchReply
  from ._q_place_search_request_private import QPlaceSearchRequestPrivate
  from ._q_place_search_suggestion_reply_unsupported import QPlaceSearchSuggestionReplyUnsupported
  from ._q_geo_coding_manager import QGeoCodingManager
  from ._q_geo_route_parser_private import QGeoRouteParserPrivate
  from ._q_geo_route_private import QGeoRoutePrivate
  from ._q_geo_route_reply import QGeoRouteReply
  from ._q_place_content_reply_unsupported import QPlaceContentReplyUnsupported
  from ._q_place_details_reply_unsupported import QPlaceDetailsReplyUnsupported
  from ._q_place_match_reply_unsupported import QPlaceMatchReplyUnsupported
  from ._q_place_search_reply_unsupported import QPlaceSearchReplyUnsupported
  from ._q_geo_route_parser import QGeoRouteParser
  from ._q_geo_route_reply_private import QGeoRouteReplyPrivate
  from ._q_geo_routing_manager_engine import QGeoRoutingManagerEngine
  from ._q_geo_route_parser_osrm_v5 import QGeoRouteParserOsrmV5
  from ._q_geo_routing_manager import QGeoRoutingManager
  from ._q_geo_service_provider import QGeoServiceProvider
  from ._q_declarative_geo_service_provider import QDeclarativeGeoServiceProvider
  from ._q_declarative_geo_service_provider_requirements import QDeclarativeGeoServiceProviderRequirements
  from ._q_geo_service_provider_factory import QGeoServiceProviderFactory
  from ._q_declarative_category import QDeclarativeCategory
  from ._q_declarative_geo_route_model import QDeclarativeGeoRouteModel
  from ._q_declarative_geocode_model import QDeclarativeGeocodeModel
  from ._q_declarative_search_model_base import QDeclarativeSearchModelBase
  from ._q_declarative_supported_categories_model import QDeclarativeSupportedCategoriesModel
  from ._q_geo_tiled_map_scene import QGeoTiledMapScene
  from ._q_map_quick_item_matrix4x4 import QMapQuickItemMatrix4x4
  from ._q_declarative_geo_map_item_group import QDeclarativeGeoMapItemGroup
  from ._q_declarative_geo_map_item_base import QDeclarativeGeoMapItemBase
  from ._q_declarative_geo_map import QDeclarativeGeoMap
  from ._q_declarative_geo_map_item_view import QDeclarativeGeoMapItemView
  from ._q_geo_map import QGeoMap
  from ._q_geo_map_private import QGeoMapPrivate
  from ._q_declarative_geo_map_item_transition_manager import QDeclarativeGeoMapItemTransitionManager
  from ._q_declarative_place import QDeclarativePlace
  from ._q_declarative_search_suggestion_model import QDeclarativeSearchSuggestionModel
  from ._q_declarative_circle_map_item import QDeclarativeCircleMapItem
  from ._q_declarative_geo_json_data import QDeclarativeGeoJsonData
  from ._q_declarative_geo_map_copyright_notice import QDeclarativeGeoMapCopyrightNotice
  from ._q_declarative_geo_map_quick_item import QDeclarativeGeoMapQuickItem
  from ._q_declarative_place_content_model import QDeclarativePlaceContentModel
  from ._q_declarative_polygon_map_item import QDeclarativePolygonMapItem
  from ._q_declarative_polyline_map_item import QDeclarativePolylineMapItem
  from ._q_declarative_rectangle_map_item import QDeclarativeRectangleMapItem
  from ._q_declarative_search_result_model import QDeclarativeSearchResultModel
  from ._q_geo_map_polygon_geometry import QGeoMapPolygonGeometry
  from ._q_geo_map_polyline_geometry import QGeoMapPolylineGeometry
  from ._q_geo_tiled_mapping_manager_engine import QGeoTiledMappingManagerEngine
  from ._q_geo_tiled_map_private import QGeoTiledMapPrivate
  from ._q_geo_tiled_map import QGeoTiledMap
  from ._q_declarative_circle_map_item_private import QDeclarativeCircleMapItemPrivate
  from ._q_declarative_place_editorial_model import QDeclarativePlaceEditorialModel
  from ._q_declarative_place_image_model import QDeclarativePlaceImageModel
  from ._q_declarative_place_review_model import QDeclarativePlaceReviewModel
  from ._q_declarative_polygon_map_item_private import QDeclarativePolygonMapItemPrivate
  from ._q_declarative_polyline_map_item_private import QDeclarativePolylineMapItemPrivate
  from ._q_declarative_rectangle_map_item_private import QDeclarativeRectangleMapItemPrivate
  from ._q_declarative_route_map_item import QDeclarativeRouteMapItem
  from ._q_geo_map_circle_geometry import QGeoMapCircleGeometry
  from ._q_geo_tile_request_manager import QGeoTileRequestManager
  from ._q_geo_tiled_map_scene_private import QGeoTiledMapScenePrivate
  from ._q_geo_tiled_map_tile_container_node import QGeoTiledMapTileContainerNode
  from ._q_declarative_circle_map_item_private_c_p_u import QDeclarativeCircleMapItemPrivateCPU
  from ._q_declarative_polygon_map_item_private_c_p_u import QDeclarativePolygonMapItemPrivateCPU
  from ._q_declarative_polyline_map_item_private_c_p_u import QDeclarativePolylineMapItemPrivateCPU
  from ._q_declarative_rectangle_map_item_private_c_p_u import QDeclarativeRectangleMapItemPrivateCPU
  from ._q_geo_tiled_map_root_node import QGeoTiledMapRootNode
  from . import QDeclarativeGeoMapItemUtils
  from . import QLocation
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Frustum': '_frustum',
      'QGeoCachedTileDisk': '_q_geo_cached_tile_disk',
      'QGeoCodingManagerEnginePrivate': '_q_geo_coding_manager_engine_private',
      'QGeoCodingManagerPrivate': '_q_geo_coding_manager_private',
      'QGeoMapViewportChangeEvent': '_q_geo_map_viewport_change_event',
      'QGeoMappingManagerEnginePrivate': '_q_geo_mapping_manager_engine_private',
      'QGeoMappingManagerPrivate': '_q_geo_mapping_manager_private',
      'QGeoRoutingManagerEnginePrivate': '_q_geo_routing_manager_engine_private',
      'QGeoRoutingManagerPrivate': '_q_geo_routing_manager_private',
      'QGeoTileTexture': '_q_geo_tile_texture',
      'QGeoTiledMappingManagerEnginePrivate': '_q_geo_tiled_mapping_manager_engine_private',
      'QPlaceManagerEnginePrivate': '_q_place_manager_engine_private',
      'QPlaceReplyPrivate': '_q_place_reply_private',
      'QGeoRouteRequestPrivate': '_q_geo_route_request_private',
      'QPlaceAttributePrivate': '_q_place_attribute_private',
      'QPlaceCategoryPrivate': '_q_place_category_private',
      'QPlaceContactDetailPrivate': '_q_place_contact_detail_private',
      'QPlaceContentRequestPrivate': '_q_place_content_request_private',
      'QPlaceIconPrivate': '_q_place_icon_private',
      'QPlaceRatingsPrivate': '_q_place_ratings_private',
      'QPlaceSupplierPrivate': '_q_place_supplier_private',
      'QPlaceUserPrivate': '_q_place_user_private',
      'QGeoTileSpec': '_q_geo_tile_spec',
      'QGeoTileSpecPrivate': '_q_geo_tile_spec_private',
      'QCache3QTileEvictionPolicy': '_q_cache3_q_tile_eviction_policy',
      'QAbstractGeoTileCache': '_q_abstract_geo_tile_cache',
      'QDeclarativeMapLineProperties': '_q_declarative_map_line_properties',
      'QDeclarativePluginParameterForeign': '_q_declarative_plugin_parameter_foreign',
      'QGeoCameraCapabilities': '_q_geo_camera_capabilities',
      'QGeoServiceProviderPrivate': '_q_geo_service_provider_private',
      'QGeoTileFetcherPrivate': '_q_geo_tile_fetcher_private',
      'QGeoTiledMapReply': '_q_geo_tiled_map_reply',
      'QPlaceAttribute': '_q_place_attribute',
      'QPlaceContactDetail': '_q_place_contact_detail',
      'QPlaceRatings': '_q_place_ratings',
      'QPlaceReply': '_q_place_reply',
      'QPlaceUser': '_q_place_user',
      'QDeclarativeContactDetails': '_q_declarative_contact_details',
      'QGeoCameraData': '_q_geo_camera_data',
      'QGeoManeuver': '_q_geo_maneuver',
      'QGeoMapType': '_q_geo_map_type',
      'QGeoTiledMapReplyPrivate': '_q_geo_tiled_map_reply_private',
      'QPlaceIdReply': '_q_place_id_reply',
      'QPlaceSearchSuggestionReply': '_q_place_search_suggestion_reply',
      'QGeoCameraTiles': '_q_geo_camera_tiles',
      'QGeoFileTileCache': '_q_geo_file_tile_cache',
      'QGeoManeuverDerived': '_q_geo_maneuver_derived',
      'QGeoManeuverPrivate': '_q_geo_maneuver_private',
      'QGeoMapTypePrivate': '_q_geo_map_type_private',
      'QGeoMappingManagerEngine': '_q_geo_mapping_manager_engine',
      'QGeoProjection': '_q_geo_projection',
      'QGeoRouteSegment': '_q_geo_route_segment',
      'QGeoRouteSegmentPrivate': '_q_geo_route_segment_private',
      'QDeclarativeGeoMapPainterPath': '_q_declarative_geo_map_painter_path',
      'QGeoCameraTilesPrivate': '_q_geo_camera_tiles_private',
      'QGeoCodeReply': '_q_geo_code_reply',
      'QGeoMapItemGeometry': '_q_geo_map_item_geometry',
      'QGeoMappingManager': '_q_geo_mapping_manager',
      'QGeoProjectionWebMercator': '_q_geo_projection_web_mercator',
      'QGeoRouteParserOsrmV5Extension': '_q_geo_route_parser_osrm_v5_extension',
      'QGeoRouteRequest': '_q_geo_route_request',
      'QGeoTileFetcher': '_q_geo_tile_fetcher',
      'QPlaceIcon': '_q_place_icon',
      'QPlaceCategory': '_q_place_category',
      'QPlaceSupplier': '_q_place_supplier',
      'QPlaceContent': '_q_place_content',
      'QPlace': '_q_place',
      'QPlaceContentRequest': '_q_place_content_request',
      'QPlaceSearchRequest': '_q_place_search_request',
      'QPlaceMatchRequest': '_q_place_match_request',
      'QPlaceManagerEngine': '_q_place_manager_engine',
      'QPlaceManager': '_q_place_manager',
      'QPlacePrivate': '_q_place_private',
      'QPlaceSearchResult': '_q_place_search_result',
      'QPlaceSearchResultPrivate': '_q_place_search_result_private',
      'QDeclarativeGeoRouteQuery': '_q_declarative_geo_route_query',
      'QGeoCodeReplyPrivate': '_q_geo_code_reply_private',
      'QGeoCodingManagerEngine': '_q_geo_coding_manager_engine',
      'QGeoRoute': '_q_geo_route',
      'QPlaceContentPrivate': '_q_place_content_private',
      'QPlaceContentReply': '_q_place_content_reply',
      'QPlaceDetailsReply': '_q_place_details_reply',
      'QPlaceIdReplyUnsupported': '_q_place_id_reply_unsupported',
      'QPlaceMatchReply': '_q_place_match_reply',
      'QPlacePrivateDefault': '_q_place_private_default',
      'QPlaceProposedSearchResult': '_q_place_proposed_search_result',
      'QPlaceProposedSearchResultPrivate': '_q_place_proposed_search_result_private',
      'QPlaceReplyUnsupported': '_q_place_reply_unsupported',
      'QPlaceResult': '_q_place_result',
      'QPlaceResultPrivate': '_q_place_result_private',
      'QPlaceSearchReply': '_q_place_search_reply',
      'QPlaceSearchRequestPrivate': '_q_place_search_request_private',
      'QPlaceSearchSuggestionReplyUnsupported': '_q_place_search_suggestion_reply_unsupported',
      'QGeoCodingManager': '_q_geo_coding_manager',
      'QGeoRouteParserPrivate': '_q_geo_route_parser_private',
      'QGeoRoutePrivate': '_q_geo_route_private',
      'QGeoRouteReply': '_q_geo_route_reply',
      'QPlaceContentReplyUnsupported': '_q_place_content_reply_unsupported',
      'QPlaceDetailsReplyUnsupported': '_q_place_details_reply_unsupported',
      'QPlaceMatchReplyUnsupported': '_q_place_match_reply_unsupported',
      'QPlaceSearchReplyUnsupported': '_q_place_search_reply_unsupported',
      'QGeoRouteParser': '_q_geo_route_parser',
      'QGeoRouteReplyPrivate': '_q_geo_route_reply_private',
      'QGeoRoutingManagerEngine': '_q_geo_routing_manager_engine',
      'QGeoRouteParserOsrmV5': '_q_geo_route_parser_osrm_v5',
      'QGeoRoutingManager': '_q_geo_routing_manager',
      'QGeoServiceProvider': '_q_geo_service_provider',
      'QDeclarativeGeoServiceProvider': '_q_declarative_geo_service_provider',
      'QDeclarativeGeoServiceProviderRequirements': '_q_declarative_geo_service_provider_requirements',
      'QGeoServiceProviderFactory': '_q_geo_service_provider_factory',
      'QDeclarativeCategory': '_q_declarative_category',
      'QDeclarativeGeoRouteModel': '_q_declarative_geo_route_model',
      'QDeclarativeGeocodeModel': '_q_declarative_geocode_model',
      'QDeclarativeSearchModelBase': '_q_declarative_search_model_base',
      'QDeclarativeSupportedCategoriesModel': '_q_declarative_supported_categories_model',
      'QGeoTiledMapScene': '_q_geo_tiled_map_scene',
      'QMapQuickItemMatrix4x4': '_q_map_quick_item_matrix4x4',
      'QDeclarativeGeoMapItemGroup': '_q_declarative_geo_map_item_group',
      'QDeclarativeGeoMapItemBase': '_q_declarative_geo_map_item_base',
      'QDeclarativeGeoMap': '_q_declarative_geo_map',
      'QDeclarativeGeoMapItemView': '_q_declarative_geo_map_item_view',
      'QGeoMap': '_q_geo_map',
      'QGeoMapPrivate': '_q_geo_map_private',
      'QDeclarativeGeoMapItemTransitionManager': '_q_declarative_geo_map_item_transition_manager',
      'QDeclarativePlace': '_q_declarative_place',
      'QDeclarativeSearchSuggestionModel': '_q_declarative_search_suggestion_model',
      'QDeclarativeCircleMapItem': '_q_declarative_circle_map_item',
      'QDeclarativeGeoJsonData': '_q_declarative_geo_json_data',
      'QDeclarativeGeoMapCopyrightNotice': '_q_declarative_geo_map_copyright_notice',
      'QDeclarativeGeoMapQuickItem': '_q_declarative_geo_map_quick_item',
      'QDeclarativePlaceContentModel': '_q_declarative_place_content_model',
      'QDeclarativePolygonMapItem': '_q_declarative_polygon_map_item',
      'QDeclarativePolylineMapItem': '_q_declarative_polyline_map_item',
      'QDeclarativeRectangleMapItem': '_q_declarative_rectangle_map_item',
      'QDeclarativeSearchResultModel': '_q_declarative_search_result_model',
      'QGeoMapPolygonGeometry': '_q_geo_map_polygon_geometry',
      'QGeoMapPolylineGeometry': '_q_geo_map_polyline_geometry',
      'QGeoTiledMappingManagerEngine': '_q_geo_tiled_mapping_manager_engine',
      'QGeoTiledMapPrivate': '_q_geo_tiled_map_private',
      'QGeoTiledMap': '_q_geo_tiled_map',
      'QDeclarativeCircleMapItemPrivate': '_q_declarative_circle_map_item_private',
      'QDeclarativePlaceEditorialModel': '_q_declarative_place_editorial_model',
      'QDeclarativePlaceImageModel': '_q_declarative_place_image_model',
      'QDeclarativePlaceReviewModel': '_q_declarative_place_review_model',
      'QDeclarativePolygonMapItemPrivate': '_q_declarative_polygon_map_item_private',
      'QDeclarativePolylineMapItemPrivate': '_q_declarative_polyline_map_item_private',
      'QDeclarativeRectangleMapItemPrivate': '_q_declarative_rectangle_map_item_private',
      'QDeclarativeRouteMapItem': '_q_declarative_route_map_item',
      'QGeoMapCircleGeometry': '_q_geo_map_circle_geometry',
      'QGeoTileRequestManager': '_q_geo_tile_request_manager',
      'QGeoTiledMapScenePrivate': '_q_geo_tiled_map_scene_private',
      'QGeoTiledMapTileContainerNode': '_q_geo_tiled_map_tile_container_node',
      'QDeclarativeCircleMapItemPrivateCPU': '_q_declarative_circle_map_item_private_c_p_u',
      'QDeclarativePolygonMapItemPrivateCPU': '_q_declarative_polygon_map_item_private_c_p_u',
      'QDeclarativePolylineMapItemPrivateCPU': '_q_declarative_polyline_map_item_private_c_p_u',
      'QDeclarativeRectangleMapItemPrivateCPU': '_q_declarative_rectangle_map_item_private_c_p_u',
      'QGeoTiledMapRootNode': '_q_geo_tiled_map_root_node',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QDeclarativeGeoMapItemUtils', 'QLocation',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtLocation import QGeoTiledMapRootNode'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
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
