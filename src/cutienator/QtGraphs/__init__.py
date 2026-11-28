"""
The 'cutienator.QtGraphs' package provides the cute classes of the part
of Qt named QtGraphs, under the name PySide6 has for it.

  from cutienator.QtGraphs import Abstract3DChangeBitField, BarItemHolder

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
    'BarItemHolder',
    'Bars3DChangeBitField',
    'CommonUtils',
    'DataItemHolder',
    'GradientHolder',
    'Q3DSceneChangeBitField',
    'QAbstract3DSeriesChangeBitField',
    'QAbstract3DSeriesThemeOverrideBitField',
    'QBarDataItem',
    'QCustomItemDirtyBitField',
    'QCustomVolumeDirtyBitField',
    'QGraphsThemeDirtyBitField',
    'Scatter3DChangeBitField',
    'Surface3DChangeBitField',
    'QGraphsLinePrivate',
    'AbstractItemModelHandler',
    'Q3DScene',
    'Q3DScenePrivate',
    'QAbstract3DAxis',
    'QAbstract3DAxisPrivate',
    'QBarSet',
    'QBarSetPrivate',
    'QCustomSeriesData',
    'QGraphsThemePrivate',
    'QLegendData',
    'QQuickGraphsColor',
    'QXYModelMapperPrivate',
    'QXYPoint',
    'QBarModelMapperPrivate',
    'QCategory3DAxis',
    'QCategory3DAxisPrivate',
    'QValue3DAxisPrivate',
    'QGraphAnimation',
    'QPieSlice',
    'QValue3DAxis',
    'QValue3DAxisFormatter',
    'QCustom3DItemPrivate',
    'QGraphTransition',
    'QLogValue3DAxisFormatter',
    'QPieModelMapperPrivate',
    'QScatterDataItem',
    'QSurfaceDataItem',
    'QCustom3DItem',
    'QCustom3DLabelPrivate',
    'QCustom3DVolumePrivate',
    'QXYSeriesAnimation',
    'QCustom3DLabel',
    'QCustom3DVolume',
    'QGraphPointAnimation',
    'QSplineControlAnimation',
    'QGraphsLine',
    'QGraphsTheme',
    'AxisGrid',
    'AxisLine',
    'AxisTicker',
    'BarInstancing',
    'QQuickGraphsTextureData',
    'ScatterInstancing',
    'QAbstract3DSeries',
    'QAbstractDataProxy',
    'QQuickGraphsItem',
    'QAbstract3DSeriesPrivate',
    'QAbstractDataProxyPrivate',
    'QBarDataProxyPrivate',
    'QGraphsInputHandler',
    'QQuickGraphsNode',
    'QScatter3DSeriesPrivate',
    'QScatterDataProxyPrivate',
    'QSurfaceDataProxyPrivate',
    'QBar3DSeries',
    'QBarDataProxy',
    'QHeightMapSurfaceDataProxyPrivate',
    'QScatter3DSeries',
    'QScatterDataProxy',
    'QSpline3DSeriesPrivate',
    'QSurface3DSeries',
    'QSurface3DSeriesPrivate',
    'QSurfaceDataProxy',
    'QBar3DSeriesPrivate',
    'QHeightMapSurfaceDataProxy',
    'QItemModelBarDataProxy',
    'QItemModelScatterDataProxy',
    'QItemModelSurfaceDataProxy',
    'QQuickGraphsBars',
    'QQuickGraphsBarsNode',
    'QQuickGraphsScatter',
    'QQuickGraphsScatterNode',
    'QQuickGraphsSurface',
    'QQuickGraphsSurfaceNode',
    'QSpline3DSeries',
    'BarItemModelHandler',
    'QItemModelBarDataProxyPrivate',
    'QItemModelScatterDataProxyPrivate',
    'QItemModelSurfaceDataProxyPrivate',
    'ScatterItemModelHandler',
    'SurfaceItemModelHandler',
    'QAbstractAxis',
    'QAbstractSeries',
    'QCustomSeries',
    'QGraphsView',
    'QAbstractAxisPrivate',
    'QCustomSeriesCanvasRenderer',
    'AxisRenderer',
    'QBarCategoryAxisPrivate',
    'QDateTimeAxisPrivate',
    'QLogValueAxisPrivate',
    'QValueAxisPrivate',
    'QXYSeries',
    'CustomRenderer',
    'QBarCategoryAxis',
    'QDateTimeAxis',
    'QLineSeries',
    'QLogValueAxis',
    'QPieSeries',
    'QValueAxis',
    'QXYModelMapper',
    'QPieModelMapper',
    'QPieSlicePrivate',
    'QScatterSeries',
    'QAreaSeries',
    'QBarSeries',
    'QSplineSeries',
    'AreaRenderer',
    'BarsRenderer',
    'PointRenderer',
    'QBarModelMapper',
    'QBarDataRow',
    'QScatterDataArray',
    'QSurfaceDataRow',
    'QtGraphs3D',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._abstract3_d_change_bit_field import Abstract3DChangeBitField
  from ._bar_item_holder import BarItemHolder
  from ._bars3_d_change_bit_field import Bars3DChangeBitField
  from ._common_utils import CommonUtils
  from ._data_item_holder import DataItemHolder
  from ._gradient_holder import GradientHolder
  from ._q3_d_scene_change_bit_field import Q3DSceneChangeBitField
  from ._q_abstract3_d_series_change_bit_field import QAbstract3DSeriesChangeBitField
  from ._q_abstract3_d_series_theme_override_bit_field import QAbstract3DSeriesThemeOverrideBitField
  from ._q_bar_data_item import QBarDataItem
  from ._q_custom_item_dirty_bit_field import QCustomItemDirtyBitField
  from ._q_custom_volume_dirty_bit_field import QCustomVolumeDirtyBitField
  from ._q_graphs_theme_dirty_bit_field import QGraphsThemeDirtyBitField
  from ._scatter3_d_change_bit_field import Scatter3DChangeBitField
  from ._surface3_d_change_bit_field import Surface3DChangeBitField
  from ._q_graphs_line_private import QGraphsLinePrivate
  from ._abstract_item_model_handler import AbstractItemModelHandler
  from ._q3_d_scene import Q3DScene
  from ._q3_d_scene_private import Q3DScenePrivate
  from ._q_abstract3_d_axis import QAbstract3DAxis
  from ._q_abstract3_d_axis_private import QAbstract3DAxisPrivate
  from ._q_bar_set import QBarSet
  from ._q_bar_set_private import QBarSetPrivate
  from ._q_custom_series_data import QCustomSeriesData
  from ._q_graphs_theme_private import QGraphsThemePrivate
  from ._q_legend_data import QLegendData
  from ._q_quick_graphs_color import QQuickGraphsColor
  from ._q_x_y_model_mapper_private import QXYModelMapperPrivate
  from ._q_x_y_point import QXYPoint
  from ._q_bar_model_mapper_private import QBarModelMapperPrivate
  from ._q_category3_d_axis import QCategory3DAxis
  from ._q_category3_d_axis_private import QCategory3DAxisPrivate
  from ._q_value3_d_axis_private import QValue3DAxisPrivate
  from ._q_graph_animation import QGraphAnimation
  from ._q_pie_slice import QPieSlice
  from ._q_value3_d_axis import QValue3DAxis
  from ._q_value3_d_axis_formatter import QValue3DAxisFormatter
  from ._q_custom3_d_item_private import QCustom3DItemPrivate
  from ._q_graph_transition import QGraphTransition
  from ._q_log_value3_d_axis_formatter import QLogValue3DAxisFormatter
  from ._q_pie_model_mapper_private import QPieModelMapperPrivate
  from ._q_scatter_data_item import QScatterDataItem
  from ._q_surface_data_item import QSurfaceDataItem
  from ._q_custom3_d_item import QCustom3DItem
  from ._q_custom3_d_label_private import QCustom3DLabelPrivate
  from ._q_custom3_d_volume_private import QCustom3DVolumePrivate
  from ._q_x_y_series_animation import QXYSeriesAnimation
  from ._q_custom3_d_label import QCustom3DLabel
  from ._q_custom3_d_volume import QCustom3DVolume
  from ._q_graph_point_animation import QGraphPointAnimation
  from ._q_spline_control_animation import QSplineControlAnimation
  from ._q_graphs_line import QGraphsLine
  from ._q_graphs_theme import QGraphsTheme
  from ._axis_grid import AxisGrid
  from ._axis_line import AxisLine
  from ._axis_ticker import AxisTicker
  from ._bar_instancing import BarInstancing
  from ._q_quick_graphs_texture_data import QQuickGraphsTextureData
  from ._scatter_instancing import ScatterInstancing
  from ._q_abstract3_d_series import QAbstract3DSeries
  from ._q_abstract_data_proxy import QAbstractDataProxy
  from ._q_quick_graphs_item import QQuickGraphsItem
  from ._q_abstract3_d_series_private import QAbstract3DSeriesPrivate
  from ._q_abstract_data_proxy_private import QAbstractDataProxyPrivate
  from ._q_bar_data_proxy_private import QBarDataProxyPrivate
  from ._q_graphs_input_handler import QGraphsInputHandler
  from ._q_quick_graphs_node import QQuickGraphsNode
  from ._q_scatter3_d_series_private import QScatter3DSeriesPrivate
  from ._q_scatter_data_proxy_private import QScatterDataProxyPrivate
  from ._q_surface_data_proxy_private import QSurfaceDataProxyPrivate
  from ._q_bar3_d_series import QBar3DSeries
  from ._q_bar_data_proxy import QBarDataProxy
  from ._q_height_map_surface_data_proxy_private import QHeightMapSurfaceDataProxyPrivate
  from ._q_scatter3_d_series import QScatter3DSeries
  from ._q_scatter_data_proxy import QScatterDataProxy
  from ._q_spline3_d_series_private import QSpline3DSeriesPrivate
  from ._q_surface3_d_series import QSurface3DSeries
  from ._q_surface3_d_series_private import QSurface3DSeriesPrivate
  from ._q_surface_data_proxy import QSurfaceDataProxy
  from ._q_bar3_d_series_private import QBar3DSeriesPrivate
  from ._q_height_map_surface_data_proxy import QHeightMapSurfaceDataProxy
  from ._q_item_model_bar_data_proxy import QItemModelBarDataProxy
  from ._q_item_model_scatter_data_proxy import QItemModelScatterDataProxy
  from ._q_item_model_surface_data_proxy import QItemModelSurfaceDataProxy
  from ._q_quick_graphs_bars import QQuickGraphsBars
  from ._q_quick_graphs_bars_node import QQuickGraphsBarsNode
  from ._q_quick_graphs_scatter import QQuickGraphsScatter
  from ._q_quick_graphs_scatter_node import QQuickGraphsScatterNode
  from ._q_quick_graphs_surface import QQuickGraphsSurface
  from ._q_quick_graphs_surface_node import QQuickGraphsSurfaceNode
  from ._q_spline3_d_series import QSpline3DSeries
  from ._bar_item_model_handler import BarItemModelHandler
  from ._q_item_model_bar_data_proxy_private import QItemModelBarDataProxyPrivate
  from ._q_item_model_scatter_data_proxy_private import QItemModelScatterDataProxyPrivate
  from ._q_item_model_surface_data_proxy_private import QItemModelSurfaceDataProxyPrivate
  from ._scatter_item_model_handler import ScatterItemModelHandler
  from ._surface_item_model_handler import SurfaceItemModelHandler
  from ._q_abstract_axis import QAbstractAxis
  from ._q_abstract_series import QAbstractSeries
  from ._q_custom_series import QCustomSeries
  from ._q_graphs_view import QGraphsView
  from ._q_abstract_axis_private import QAbstractAxisPrivate
  from ._q_custom_series_canvas_renderer import QCustomSeriesCanvasRenderer
  from ._axis_renderer import AxisRenderer
  from ._q_bar_category_axis_private import QBarCategoryAxisPrivate
  from ._q_date_time_axis_private import QDateTimeAxisPrivate
  from ._q_log_value_axis_private import QLogValueAxisPrivate
  from ._q_value_axis_private import QValueAxisPrivate
  from ._q_x_y_series import QXYSeries
  from ._custom_renderer import CustomRenderer
  from ._q_bar_category_axis import QBarCategoryAxis
  from ._q_date_time_axis import QDateTimeAxis
  from ._q_line_series import QLineSeries
  from ._q_log_value_axis import QLogValueAxis
  from ._q_pie_series import QPieSeries
  from ._q_value_axis import QValueAxis
  from ._q_x_y_model_mapper import QXYModelMapper
  from ._q_pie_model_mapper import QPieModelMapper
  from ._q_pie_slice_private import QPieSlicePrivate
  from ._q_scatter_series import QScatterSeries
  from ._q_area_series import QAreaSeries
  from ._q_bar_series import QBarSeries
  from ._q_spline_series import QSplineSeries
  from ._area_renderer import AreaRenderer
  from ._bars_renderer import BarsRenderer
  from ._point_renderer import PointRenderer
  from ._q_bar_model_mapper import QBarModelMapper
  from ._q_bar_data_item import QBarDataRow
  from ._q_scatter_data_item import QScatterDataArray
  from ._q_surface_data_item import QSurfaceDataRow
  from . import QtGraphs3D
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Abstract3DChangeBitField': '_abstract3_d_change_bit_field',
      'BarItemHolder': '_bar_item_holder',
      'Bars3DChangeBitField': '_bars3_d_change_bit_field',
      'CommonUtils': '_common_utils',
      'DataItemHolder': '_data_item_holder',
      'GradientHolder': '_gradient_holder',
      'Q3DSceneChangeBitField': '_q3_d_scene_change_bit_field',
      'QAbstract3DSeriesChangeBitField': '_q_abstract3_d_series_change_bit_field',
      'QAbstract3DSeriesThemeOverrideBitField': '_q_abstract3_d_series_theme_override_bit_field',
      'QBarDataItem': '_q_bar_data_item',
      'QCustomItemDirtyBitField': '_q_custom_item_dirty_bit_field',
      'QCustomVolumeDirtyBitField': '_q_custom_volume_dirty_bit_field',
      'QGraphsThemeDirtyBitField': '_q_graphs_theme_dirty_bit_field',
      'Scatter3DChangeBitField': '_scatter3_d_change_bit_field',
      'Surface3DChangeBitField': '_surface3_d_change_bit_field',
      'QGraphsLinePrivate': '_q_graphs_line_private',
      'AbstractItemModelHandler': '_abstract_item_model_handler',
      'Q3DScene': '_q3_d_scene',
      'Q3DScenePrivate': '_q3_d_scene_private',
      'QAbstract3DAxis': '_q_abstract3_d_axis',
      'QAbstract3DAxisPrivate': '_q_abstract3_d_axis_private',
      'QBarSet': '_q_bar_set',
      'QBarSetPrivate': '_q_bar_set_private',
      'QCustomSeriesData': '_q_custom_series_data',
      'QGraphsThemePrivate': '_q_graphs_theme_private',
      'QLegendData': '_q_legend_data',
      'QQuickGraphsColor': '_q_quick_graphs_color',
      'QXYModelMapperPrivate': '_q_x_y_model_mapper_private',
      'QXYPoint': '_q_x_y_point',
      'QBarModelMapperPrivate': '_q_bar_model_mapper_private',
      'QCategory3DAxis': '_q_category3_d_axis',
      'QCategory3DAxisPrivate': '_q_category3_d_axis_private',
      'QValue3DAxisPrivate': '_q_value3_d_axis_private',
      'QGraphAnimation': '_q_graph_animation',
      'QPieSlice': '_q_pie_slice',
      'QValue3DAxis': '_q_value3_d_axis',
      'QValue3DAxisFormatter': '_q_value3_d_axis_formatter',
      'QCustom3DItemPrivate': '_q_custom3_d_item_private',
      'QGraphTransition': '_q_graph_transition',
      'QLogValue3DAxisFormatter': '_q_log_value3_d_axis_formatter',
      'QPieModelMapperPrivate': '_q_pie_model_mapper_private',
      'QScatterDataItem': '_q_scatter_data_item',
      'QSurfaceDataItem': '_q_surface_data_item',
      'QCustom3DItem': '_q_custom3_d_item',
      'QCustom3DLabelPrivate': '_q_custom3_d_label_private',
      'QCustom3DVolumePrivate': '_q_custom3_d_volume_private',
      'QXYSeriesAnimation': '_q_x_y_series_animation',
      'QCustom3DLabel': '_q_custom3_d_label',
      'QCustom3DVolume': '_q_custom3_d_volume',
      'QGraphPointAnimation': '_q_graph_point_animation',
      'QSplineControlAnimation': '_q_spline_control_animation',
      'QGraphsLine': '_q_graphs_line',
      'QGraphsTheme': '_q_graphs_theme',
      'AxisGrid': '_axis_grid',
      'AxisLine': '_axis_line',
      'AxisTicker': '_axis_ticker',
      'BarInstancing': '_bar_instancing',
      'QQuickGraphsTextureData': '_q_quick_graphs_texture_data',
      'ScatterInstancing': '_scatter_instancing',
      'QAbstract3DSeries': '_q_abstract3_d_series',
      'QAbstractDataProxy': '_q_abstract_data_proxy',
      'QQuickGraphsItem': '_q_quick_graphs_item',
      'QAbstract3DSeriesPrivate': '_q_abstract3_d_series_private',
      'QAbstractDataProxyPrivate': '_q_abstract_data_proxy_private',
      'QBarDataProxyPrivate': '_q_bar_data_proxy_private',
      'QGraphsInputHandler': '_q_graphs_input_handler',
      'QQuickGraphsNode': '_q_quick_graphs_node',
      'QScatter3DSeriesPrivate': '_q_scatter3_d_series_private',
      'QScatterDataProxyPrivate': '_q_scatter_data_proxy_private',
      'QSurfaceDataProxyPrivate': '_q_surface_data_proxy_private',
      'QBar3DSeries': '_q_bar3_d_series',
      'QBarDataProxy': '_q_bar_data_proxy',
      'QHeightMapSurfaceDataProxyPrivate': '_q_height_map_surface_data_proxy_private',
      'QScatter3DSeries': '_q_scatter3_d_series',
      'QScatterDataProxy': '_q_scatter_data_proxy',
      'QSpline3DSeriesPrivate': '_q_spline3_d_series_private',
      'QSurface3DSeries': '_q_surface3_d_series',
      'QSurface3DSeriesPrivate': '_q_surface3_d_series_private',
      'QSurfaceDataProxy': '_q_surface_data_proxy',
      'QBar3DSeriesPrivate': '_q_bar3_d_series_private',
      'QHeightMapSurfaceDataProxy': '_q_height_map_surface_data_proxy',
      'QItemModelBarDataProxy': '_q_item_model_bar_data_proxy',
      'QItemModelScatterDataProxy': '_q_item_model_scatter_data_proxy',
      'QItemModelSurfaceDataProxy': '_q_item_model_surface_data_proxy',
      'QQuickGraphsBars': '_q_quick_graphs_bars',
      'QQuickGraphsBarsNode': '_q_quick_graphs_bars_node',
      'QQuickGraphsScatter': '_q_quick_graphs_scatter',
      'QQuickGraphsScatterNode': '_q_quick_graphs_scatter_node',
      'QQuickGraphsSurface': '_q_quick_graphs_surface',
      'QQuickGraphsSurfaceNode': '_q_quick_graphs_surface_node',
      'QSpline3DSeries': '_q_spline3_d_series',
      'BarItemModelHandler': '_bar_item_model_handler',
      'QItemModelBarDataProxyPrivate': '_q_item_model_bar_data_proxy_private',
      'QItemModelScatterDataProxyPrivate': '_q_item_model_scatter_data_proxy_private',
      'QItemModelSurfaceDataProxyPrivate': '_q_item_model_surface_data_proxy_private',
      'ScatterItemModelHandler': '_scatter_item_model_handler',
      'SurfaceItemModelHandler': '_surface_item_model_handler',
      'QAbstractAxis': '_q_abstract_axis',
      'QAbstractSeries': '_q_abstract_series',
      'QCustomSeries': '_q_custom_series',
      'QGraphsView': '_q_graphs_view',
      'QAbstractAxisPrivate': '_q_abstract_axis_private',
      'QCustomSeriesCanvasRenderer': '_q_custom_series_canvas_renderer',
      'AxisRenderer': '_axis_renderer',
      'QBarCategoryAxisPrivate': '_q_bar_category_axis_private',
      'QDateTimeAxisPrivate': '_q_date_time_axis_private',
      'QLogValueAxisPrivate': '_q_log_value_axis_private',
      'QValueAxisPrivate': '_q_value_axis_private',
      'QXYSeries': '_q_x_y_series',
      'CustomRenderer': '_custom_renderer',
      'QBarCategoryAxis': '_q_bar_category_axis',
      'QDateTimeAxis': '_q_date_time_axis',
      'QLineSeries': '_q_line_series',
      'QLogValueAxis': '_q_log_value_axis',
      'QPieSeries': '_q_pie_series',
      'QValueAxis': '_q_value_axis',
      'QXYModelMapper': '_q_x_y_model_mapper',
      'QPieModelMapper': '_q_pie_model_mapper',
      'QPieSlicePrivate': '_q_pie_slice_private',
      'QScatterSeries': '_q_scatter_series',
      'QAreaSeries': '_q_area_series',
      'QBarSeries': '_q_bar_series',
      'QSplineSeries': '_q_spline_series',
      'AreaRenderer': '_area_renderer',
      'BarsRenderer': '_bars_renderer',
      'PointRenderer': '_point_renderer',
      'QBarModelMapper': '_q_bar_model_mapper',
      'QBarDataRow': '_q_bar_data_item',
      'QScatterDataArray': '_q_scatter_data_item',
      'QSurfaceDataRow': '_q_surface_data_item',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtGraphs3D',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGraphs import QSurfaceDataRow'. Python calls
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
