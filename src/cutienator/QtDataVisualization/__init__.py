"""
The 'cutienator.QtDataVisualization' package provides the cute classes
of the part of Qt named QtDataVisualization, under the name PySide6 has
for it.

  from cutienator.QtDataVisualization import Abstract3DChangeBitField, AbstractDeclarativeInterface

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
    'Abstract3DChangeBitField',
    'AbstractDeclarativeInterface',
    'Bars3DChangeBitField',
    'Q3DSceneChangeBitField',
    'Q3DThemeDirtyBitField',
    'QAbstract3DSeriesChangeBitField',
    'QAbstract3DSeriesThemeOverrideBitField',
    'QBarDataItem',
    'QBarDataItemPrivate',
    'QCustomItemDirtyBitField',
    'QCustomVolumeDirtyBitField',
    'QScatterDataItemPrivate',
    'QSurfaceDataItemPrivate',
    'Scatter3DChangeBitField',
    'Surface3DChangeBitField',
    'LabelItem',
    'AbstractItemModelHandler',
    'QAbstract3DAxis',
    'QAbstract3DAxisPrivate',
    'QCategory3DAxis',
    'QValue3DAxisFormatter',
    'QValue3DAxis',
    'QValue3DAxisFormatterPrivate',
    'Q3DTheme',
    'Q3DThemePrivate',
    'QCategory3DAxisPrivate',
    'QLogValue3DAxisFormatter',
    'QLogValue3DAxisFormatterPrivate',
    'QValue3DAxisPrivate',
    'AbstractRenderItem',
    'MeshLoader',
    'Q3DObject',
    'QCustom3DItem',
    'QCustom3DItemPrivate',
    'QScatterDataItem',
    'QSurfaceDataItem',
    'ShaderHelper',
    'Utils',
    'VertexIndexer',
    'BarRenderItem',
    'Q3DCamera',
    'Q3DLight',
    'Q3DObjectPrivate',
    'QCustom3DLabel',
    'QCustom3DVolume',
    'ScatterRenderItem',
    'BarRenderSliceItem',
    'CameraHelper',
    'Q3DCameraPrivate',
    'Q3DLightPrivate',
    'Q3DScene',
    'QCustom3DLabelPrivate',
    'QCustom3DVolumePrivate',
    'Q3DScenePrivate',
    'QAbstract3DInputHandler',
    'Q3DInputHandler',
    'QAbstract3DInputHandlerPrivate',
    'Q3DInputHandlerPrivate',
    'QTouch3DInputHandler',
    'QTouch3DInputHandlerPrivate',
    'AbstractObjectHelper',
    'TextureHelper',
    'QAbstract3DSeries',
    'QAbstract3DGraph',
    'Abstract3DController',
    'QAbstractDataProxy',
    'Abstract3DRenderer',
    'CustomRenderItem',
    'QAbstract3DGraphPrivate',
    'QAbstract3DSeriesPrivate',
    'QAbstractDataProxyPrivate',
    'SeriesRenderCache',
    'BarSeriesRenderCache',
    'ObjectHelper',
    'QBar3DSeries',
    'QBarDataProxy',
    'QBarDataProxyPrivate',
    'QScatter3DSeries',
    'QScatter3DSeriesPrivate',
    'QScatterDataProxy',
    'QScatterDataProxyPrivate',
    'QSurface3DSeries',
    'QSurface3DSeriesPrivate',
    'QSurfaceDataProxy',
    'QSurfaceDataProxyPrivate',
    'ScatterObjectBufferHelper',
    'ScatterPointBufferHelper',
    'ScatterSeriesRenderCache',
    'ThemeManager',
    'Bars3DController',
    'Q3DBars',
    'Q3DScatter',
    'Q3DSurface',
    'QBar3DSeriesPrivate',
    'QHeightMapSurfaceDataProxy',
    'QHeightMapSurfaceDataProxyPrivate',
    'QItemModelBarDataProxy',
    'QItemModelScatterDataProxy',
    'QItemModelSurfaceDataProxy',
    'Scatter3DController',
    'Surface3DController',
    'BarItemModelHandler',
    'Bars3DRenderer',
    'Surface3DRenderer',
    'SurfaceObject',
    'Drawer',
    'SelectionPointer',
    'SurfaceSeriesRenderCache',
    'Q3DBarsPrivate',
    'Q3DScatterPrivate',
    'Q3DSurfacePrivate',
    'QItemModelBarDataProxyPrivate',
    'QItemModelScatterDataProxyPrivate',
    'QItemModelSurfaceDataProxyPrivate',
    'Scatter3DRenderer',
    'ScatterItemModelHandler',
    'SurfaceItemModelHandler',
    'AxisRenderCache',
    'QScatterDataArray',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._abstract3_d_change_bit_field import Abstract3DChangeBitField
  from ._abstract_declarative_interface import AbstractDeclarativeInterface
  from ._bars3_d_change_bit_field import Bars3DChangeBitField
  from ._q3_d_scene_change_bit_field import Q3DSceneChangeBitField
  from ._q3_d_theme_dirty_bit_field import Q3DThemeDirtyBitField
  from ._q_abstract3_d_series_change_bit_field import QAbstract3DSeriesChangeBitField
  from ._q_abstract3_d_series_theme_override_bit_field import QAbstract3DSeriesThemeOverrideBitField
  from ._q_bar_data_item import QBarDataItem
  from ._q_bar_data_item_private import QBarDataItemPrivate
  from ._q_custom_item_dirty_bit_field import QCustomItemDirtyBitField
  from ._q_custom_volume_dirty_bit_field import QCustomVolumeDirtyBitField
  from ._q_scatter_data_item_private import QScatterDataItemPrivate
  from ._q_surface_data_item_private import QSurfaceDataItemPrivate
  from ._scatter3_d_change_bit_field import Scatter3DChangeBitField
  from ._surface3_d_change_bit_field import Surface3DChangeBitField
  from ._label_item import LabelItem
  from ._abstract_item_model_handler import AbstractItemModelHandler
  from ._q_abstract3_d_axis import QAbstract3DAxis
  from ._q_abstract3_d_axis_private import QAbstract3DAxisPrivate
  from ._q_category3_d_axis import QCategory3DAxis
  from ._q_value3_d_axis_formatter import QValue3DAxisFormatter
  from ._q_value3_d_axis import QValue3DAxis
  from ._q_value3_d_axis_formatter_private import QValue3DAxisFormatterPrivate
  from ._q3_d_theme import Q3DTheme
  from ._q3_d_theme_private import Q3DThemePrivate
  from ._q_category3_d_axis_private import QCategory3DAxisPrivate
  from ._q_log_value3_d_axis_formatter import QLogValue3DAxisFormatter
  from ._q_log_value3_d_axis_formatter_private import QLogValue3DAxisFormatterPrivate
  from ._q_value3_d_axis_private import QValue3DAxisPrivate
  from ._abstract_render_item import AbstractRenderItem
  from ._mesh_loader import MeshLoader
  from ._q3_d_object import Q3DObject
  from ._q_custom3_d_item import QCustom3DItem
  from ._q_custom3_d_item_private import QCustom3DItemPrivate
  from ._q_scatter_data_item import QScatterDataItem
  from ._q_surface_data_item import QSurfaceDataItem
  from ._shader_helper import ShaderHelper
  from ._utils import Utils
  from ._vertex_indexer import VertexIndexer
  from ._bar_render_item import BarRenderItem
  from ._q3_d_camera import Q3DCamera
  from ._q3_d_light import Q3DLight
  from ._q3_d_object_private import Q3DObjectPrivate
  from ._q_custom3_d_label import QCustom3DLabel
  from ._q_custom3_d_volume import QCustom3DVolume
  from ._scatter_render_item import ScatterRenderItem
  from ._bar_render_slice_item import BarRenderSliceItem
  from ._camera_helper import CameraHelper
  from ._q3_d_camera_private import Q3DCameraPrivate
  from ._q3_d_light_private import Q3DLightPrivate
  from ._q3_d_scene import Q3DScene
  from ._q_custom3_d_label_private import QCustom3DLabelPrivate
  from ._q_custom3_d_volume_private import QCustom3DVolumePrivate
  from ._q3_d_scene_private import Q3DScenePrivate
  from ._q_abstract3_d_input_handler import QAbstract3DInputHandler
  from ._q3_d_input_handler import Q3DInputHandler
  from ._q_abstract3_d_input_handler_private import QAbstract3DInputHandlerPrivate
  from ._q3_d_input_handler_private import Q3DInputHandlerPrivate
  from ._q_touch3_d_input_handler import QTouch3DInputHandler
  from ._q_touch3_d_input_handler_private import QTouch3DInputHandlerPrivate
  from ._abstract_object_helper import AbstractObjectHelper
  from ._texture_helper import TextureHelper
  from ._q_abstract3_d_series import QAbstract3DSeries
  from ._q_abstract3_d_graph import QAbstract3DGraph
  from ._abstract3_d_controller import Abstract3DController
  from ._q_abstract_data_proxy import QAbstractDataProxy
  from ._abstract3_d_renderer import Abstract3DRenderer
  from ._custom_render_item import CustomRenderItem
  from ._q_abstract3_d_graph_private import QAbstract3DGraphPrivate
  from ._q_abstract3_d_series_private import QAbstract3DSeriesPrivate
  from ._q_abstract_data_proxy_private import QAbstractDataProxyPrivate
  from ._series_render_cache import SeriesRenderCache
  from ._bar_series_render_cache import BarSeriesRenderCache
  from ._object_helper import ObjectHelper
  from ._q_bar3_d_series import QBar3DSeries
  from ._q_bar_data_proxy import QBarDataProxy
  from ._q_bar_data_proxy_private import QBarDataProxyPrivate
  from ._q_scatter3_d_series import QScatter3DSeries
  from ._q_scatter3_d_series_private import QScatter3DSeriesPrivate
  from ._q_scatter_data_proxy import QScatterDataProxy
  from ._q_scatter_data_proxy_private import QScatterDataProxyPrivate
  from ._q_surface3_d_series import QSurface3DSeries
  from ._q_surface3_d_series_private import QSurface3DSeriesPrivate
  from ._q_surface_data_proxy import QSurfaceDataProxy
  from ._q_surface_data_proxy_private import QSurfaceDataProxyPrivate
  from ._scatter_object_buffer_helper import ScatterObjectBufferHelper
  from ._scatter_point_buffer_helper import ScatterPointBufferHelper
  from ._scatter_series_render_cache import ScatterSeriesRenderCache
  from ._theme_manager import ThemeManager
  from ._bars3_d_controller import Bars3DController
  from ._q3_d_bars import Q3DBars
  from ._q3_d_scatter import Q3DScatter
  from ._q3_d_surface import Q3DSurface
  from ._q_bar3_d_series_private import QBar3DSeriesPrivate
  from ._q_height_map_surface_data_proxy import QHeightMapSurfaceDataProxy
  from ._q_height_map_surface_data_proxy_private import QHeightMapSurfaceDataProxyPrivate
  from ._q_item_model_bar_data_proxy import QItemModelBarDataProxy
  from ._q_item_model_scatter_data_proxy import QItemModelScatterDataProxy
  from ._q_item_model_surface_data_proxy import QItemModelSurfaceDataProxy
  from ._scatter3_d_controller import Scatter3DController
  from ._surface3_d_controller import Surface3DController
  from ._bar_item_model_handler import BarItemModelHandler
  from ._bars3_d_renderer import Bars3DRenderer
  from ._surface3_d_renderer import Surface3DRenderer
  from ._surface_object import SurfaceObject
  from ._drawer import Drawer
  from ._selection_pointer import SelectionPointer
  from ._surface_series_render_cache import SurfaceSeriesRenderCache
  from ._q3_d_bars_private import Q3DBarsPrivate
  from ._q3_d_scatter_private import Q3DScatterPrivate
  from ._q3_d_surface_private import Q3DSurfacePrivate
  from ._q_item_model_bar_data_proxy_private import QItemModelBarDataProxyPrivate
  from ._q_item_model_scatter_data_proxy_private import QItemModelScatterDataProxyPrivate
  from ._q_item_model_surface_data_proxy_private import QItemModelSurfaceDataProxyPrivate
  from ._scatter3_d_renderer import Scatter3DRenderer
  from ._scatter_item_model_handler import ScatterItemModelHandler
  from ._surface_item_model_handler import SurfaceItemModelHandler
  from ._axis_render_cache import AxisRenderCache
  from ._q_scatter_data_item import QScatterDataArray
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Abstract3DChangeBitField': '_abstract3_d_change_bit_field',
      'AbstractDeclarativeInterface': '_abstract_declarative_interface',
      'Bars3DChangeBitField': '_bars3_d_change_bit_field',
      'Q3DSceneChangeBitField': '_q3_d_scene_change_bit_field',
      'Q3DThemeDirtyBitField': '_q3_d_theme_dirty_bit_field',
      'QAbstract3DSeriesChangeBitField': '_q_abstract3_d_series_change_bit_field',
      'QAbstract3DSeriesThemeOverrideBitField': '_q_abstract3_d_series_theme_override_bit_field',
      'QBarDataItem': '_q_bar_data_item',
      'QBarDataItemPrivate': '_q_bar_data_item_private',
      'QCustomItemDirtyBitField': '_q_custom_item_dirty_bit_field',
      'QCustomVolumeDirtyBitField': '_q_custom_volume_dirty_bit_field',
      'QScatterDataItemPrivate': '_q_scatter_data_item_private',
      'QSurfaceDataItemPrivate': '_q_surface_data_item_private',
      'Scatter3DChangeBitField': '_scatter3_d_change_bit_field',
      'Surface3DChangeBitField': '_surface3_d_change_bit_field',
      'LabelItem': '_label_item',
      'AbstractItemModelHandler': '_abstract_item_model_handler',
      'QAbstract3DAxis': '_q_abstract3_d_axis',
      'QAbstract3DAxisPrivate': '_q_abstract3_d_axis_private',
      'QCategory3DAxis': '_q_category3_d_axis',
      'QValue3DAxisFormatter': '_q_value3_d_axis_formatter',
      'QValue3DAxis': '_q_value3_d_axis',
      'QValue3DAxisFormatterPrivate': '_q_value3_d_axis_formatter_private',
      'Q3DTheme': '_q3_d_theme',
      'Q3DThemePrivate': '_q3_d_theme_private',
      'QCategory3DAxisPrivate': '_q_category3_d_axis_private',
      'QLogValue3DAxisFormatter': '_q_log_value3_d_axis_formatter',
      'QLogValue3DAxisFormatterPrivate': '_q_log_value3_d_axis_formatter_private',
      'QValue3DAxisPrivate': '_q_value3_d_axis_private',
      'AbstractRenderItem': '_abstract_render_item',
      'MeshLoader': '_mesh_loader',
      'Q3DObject': '_q3_d_object',
      'QCustom3DItem': '_q_custom3_d_item',
      'QCustom3DItemPrivate': '_q_custom3_d_item_private',
      'QScatterDataItem': '_q_scatter_data_item',
      'QSurfaceDataItem': '_q_surface_data_item',
      'ShaderHelper': '_shader_helper',
      'Utils': '_utils',
      'VertexIndexer': '_vertex_indexer',
      'BarRenderItem': '_bar_render_item',
      'Q3DCamera': '_q3_d_camera',
      'Q3DLight': '_q3_d_light',
      'Q3DObjectPrivate': '_q3_d_object_private',
      'QCustom3DLabel': '_q_custom3_d_label',
      'QCustom3DVolume': '_q_custom3_d_volume',
      'ScatterRenderItem': '_scatter_render_item',
      'BarRenderSliceItem': '_bar_render_slice_item',
      'CameraHelper': '_camera_helper',
      'Q3DCameraPrivate': '_q3_d_camera_private',
      'Q3DLightPrivate': '_q3_d_light_private',
      'Q3DScene': '_q3_d_scene',
      'QCustom3DLabelPrivate': '_q_custom3_d_label_private',
      'QCustom3DVolumePrivate': '_q_custom3_d_volume_private',
      'Q3DScenePrivate': '_q3_d_scene_private',
      'QAbstract3DInputHandler': '_q_abstract3_d_input_handler',
      'Q3DInputHandler': '_q3_d_input_handler',
      'QAbstract3DInputHandlerPrivate': '_q_abstract3_d_input_handler_private',
      'Q3DInputHandlerPrivate': '_q3_d_input_handler_private',
      'QTouch3DInputHandler': '_q_touch3_d_input_handler',
      'QTouch3DInputHandlerPrivate': '_q_touch3_d_input_handler_private',
      'AbstractObjectHelper': '_abstract_object_helper',
      'TextureHelper': '_texture_helper',
      'QAbstract3DSeries': '_q_abstract3_d_series',
      'QAbstract3DGraph': '_q_abstract3_d_graph',
      'Abstract3DController': '_abstract3_d_controller',
      'QAbstractDataProxy': '_q_abstract_data_proxy',
      'Abstract3DRenderer': '_abstract3_d_renderer',
      'CustomRenderItem': '_custom_render_item',
      'QAbstract3DGraphPrivate': '_q_abstract3_d_graph_private',
      'QAbstract3DSeriesPrivate': '_q_abstract3_d_series_private',
      'QAbstractDataProxyPrivate': '_q_abstract_data_proxy_private',
      'SeriesRenderCache': '_series_render_cache',
      'BarSeriesRenderCache': '_bar_series_render_cache',
      'ObjectHelper': '_object_helper',
      'QBar3DSeries': '_q_bar3_d_series',
      'QBarDataProxy': '_q_bar_data_proxy',
      'QBarDataProxyPrivate': '_q_bar_data_proxy_private',
      'QScatter3DSeries': '_q_scatter3_d_series',
      'QScatter3DSeriesPrivate': '_q_scatter3_d_series_private',
      'QScatterDataProxy': '_q_scatter_data_proxy',
      'QScatterDataProxyPrivate': '_q_scatter_data_proxy_private',
      'QSurface3DSeries': '_q_surface3_d_series',
      'QSurface3DSeriesPrivate': '_q_surface3_d_series_private',
      'QSurfaceDataProxy': '_q_surface_data_proxy',
      'QSurfaceDataProxyPrivate': '_q_surface_data_proxy_private',
      'ScatterObjectBufferHelper': '_scatter_object_buffer_helper',
      'ScatterPointBufferHelper': '_scatter_point_buffer_helper',
      'ScatterSeriesRenderCache': '_scatter_series_render_cache',
      'ThemeManager': '_theme_manager',
      'Bars3DController': '_bars3_d_controller',
      'Q3DBars': '_q3_d_bars',
      'Q3DScatter': '_q3_d_scatter',
      'Q3DSurface': '_q3_d_surface',
      'QBar3DSeriesPrivate': '_q_bar3_d_series_private',
      'QHeightMapSurfaceDataProxy': '_q_height_map_surface_data_proxy',
      'QHeightMapSurfaceDataProxyPrivate': '_q_height_map_surface_data_proxy_private',
      'QItemModelBarDataProxy': '_q_item_model_bar_data_proxy',
      'QItemModelScatterDataProxy': '_q_item_model_scatter_data_proxy',
      'QItemModelSurfaceDataProxy': '_q_item_model_surface_data_proxy',
      'Scatter3DController': '_scatter3_d_controller',
      'Surface3DController': '_surface3_d_controller',
      'BarItemModelHandler': '_bar_item_model_handler',
      'Bars3DRenderer': '_bars3_d_renderer',
      'Surface3DRenderer': '_surface3_d_renderer',
      'SurfaceObject': '_surface_object',
      'Drawer': '_drawer',
      'SelectionPointer': '_selection_pointer',
      'SurfaceSeriesRenderCache': '_surface_series_render_cache',
      'Q3DBarsPrivate': '_q3_d_bars_private',
      'Q3DScatterPrivate': '_q3_d_scatter_private',
      'Q3DSurfacePrivate': '_q3_d_surface_private',
      'QItemModelBarDataProxyPrivate': '_q_item_model_bar_data_proxy_private',
      'QItemModelScatterDataProxyPrivate': '_q_item_model_scatter_data_proxy_private',
      'QItemModelSurfaceDataProxyPrivate': '_q_item_model_surface_data_proxy_private',
      'Scatter3DRenderer': '_scatter3_d_renderer',
      'ScatterItemModelHandler': '_scatter_item_model_handler',
      'SurfaceItemModelHandler': '_surface_item_model_handler',
      'AxisRenderCache': '_axis_render_cache',
      'QScatterDataArray': '_q_scatter_data_item',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtDataVisualization import QScatterDataArray'. Python calls
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
