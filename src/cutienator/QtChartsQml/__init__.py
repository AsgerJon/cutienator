"""
The 'cutienator.QtChartsQml' package provides the cute classes of the
part of Qt named QtChartsQml, under the name PySide6 has for it.

  from cutienator.QtChartsQml import DeclarativeXySeries, CppQAbstractAxis

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
    'DeclarativeXySeries',
    'CppQAbstractAxis',
    'CppQAbstractBarSeries',
    'CppQAbstractSeries',
    'CppQBarCategoryAxis',
    'CppQBarModelMapper',
    'CppQBoxPlotModelMapper',
    'CppQBrush',
    'CppQCandlestickModelMapper',
    'CppQDateTimeAxis',
    'CppQGraphicsLayout',
    'CppQHBarModelMapper',
    'CppQHBoxPlotModelMapper',
    'CppQHCandlestickModelMapper',
    'CppQHPieModelMapper',
    'CppQHXYModelMapper',
    'CppQHashPointConfiguration',
    'CppQLegend',
    'CppQListBarSet',
    'CppQListBoxSet',
    'CppQListCandlestickSet',
    'CppQListPieSlice',
    'CppQLogValueAxis',
    'CppQPen',
    'CppQPieModelMapper',
    'CppQVBarModelMapper',
    'CppQVBoxPlotModelMapper',
    'CppQVCandlestickModelMapper',
    'CppQVPieModelMapper',
    'CppQVXYModelMapper',
    'CppQValueAxis',
    'CppQXYModelMapper',
    'CppQXYSeries',
    'DeclarativeCategoryRange',
    'DeclarativeMargins',
    'DeclarativeXYPoint',
    'DeclarativeBarSet',
    'DeclarativeBoxSet',
    'DeclarativeCandlestickSet',
    'DeclarativePieSlice',
    'DeclarativeChartNode',
    'DeclarativeAxes',
    'DeclarativeBoxPlotSeries',
    'DeclarativeCandlestickSeries',
    'DeclarativeChart',
    'DeclarativePieSeries',
    'MouseEventResponse',
    'DeclarativeAbstractRenderNode',
    'DeclarativeCategoryAxis',
    'DeclarativeLineSeries',
    'DeclarativePolarChart',
    'DeclarativeScatterSeries',
    'DeclarativeAreaSeries',
    'DeclarativeBarSeries',
    'DeclarativeHorizontalBarSeries',
    'DeclarativeHorizontalPercentBarSeries',
    'DeclarativeHorizontalStackedBarSeries',
    'DeclarativeOpenGLRenderNode',
    'DeclarativePercentBarSeries',
    'DeclarativeSplineSeries',
    'DeclarativeStackedBarSeries',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._declarative_xy_series import DeclarativeXySeries
  from ._cpp_q_abstract_axis import CppQAbstractAxis
  from ._cpp_q_abstract_bar_series import CppQAbstractBarSeries
  from ._cpp_q_abstract_series import CppQAbstractSeries
  from ._cpp_q_bar_category_axis import CppQBarCategoryAxis
  from ._cpp_q_bar_model_mapper import CppQBarModelMapper
  from ._cpp_q_box_plot_model_mapper import CppQBoxPlotModelMapper
  from ._cpp_q_brush import CppQBrush
  from ._cpp_q_candlestick_model_mapper import CppQCandlestickModelMapper
  from ._cpp_q_date_time_axis import CppQDateTimeAxis
  from ._cpp_q_graphics_layout import CppQGraphicsLayout
  from ._cpp_q_h_bar_model_mapper import CppQHBarModelMapper
  from ._cpp_q_h_box_plot_model_mapper import CppQHBoxPlotModelMapper
  from ._cpp_q_h_candlestick_model_mapper import CppQHCandlestickModelMapper
  from ._cpp_q_h_pie_model_mapper import CppQHPieModelMapper
  from ._cpp_q_h_x_y_model_mapper import CppQHXYModelMapper
  from ._cpp_q_hash_point_configuration import CppQHashPointConfiguration
  from ._cpp_q_legend import CppQLegend
  from ._cpp_q_list_bar_set import CppQListBarSet
  from ._cpp_q_list_box_set import CppQListBoxSet
  from ._cpp_q_list_candlestick_set import CppQListCandlestickSet
  from ._cpp_q_list_pie_slice import CppQListPieSlice
  from ._cpp_q_log_value_axis import CppQLogValueAxis
  from ._cpp_q_pen import CppQPen
  from ._cpp_q_pie_model_mapper import CppQPieModelMapper
  from ._cpp_q_v_bar_model_mapper import CppQVBarModelMapper
  from ._cpp_q_v_box_plot_model_mapper import CppQVBoxPlotModelMapper
  from ._cpp_q_v_candlestick_model_mapper import CppQVCandlestickModelMapper
  from ._cpp_q_v_pie_model_mapper import CppQVPieModelMapper
  from ._cpp_q_v_x_y_model_mapper import CppQVXYModelMapper
  from ._cpp_q_value_axis import CppQValueAxis
  from ._cpp_q_x_y_model_mapper import CppQXYModelMapper
  from ._cpp_q_x_y_series import CppQXYSeries
  from ._declarative_category_range import DeclarativeCategoryRange
  from ._declarative_margins import DeclarativeMargins
  from ._declarative_x_y_point import DeclarativeXYPoint
  from ._declarative_bar_set import DeclarativeBarSet
  from ._declarative_box_set import DeclarativeBoxSet
  from ._declarative_candlestick_set import DeclarativeCandlestickSet
  from ._declarative_pie_slice import DeclarativePieSlice
  from ._declarative_chart_node import DeclarativeChartNode
  from ._declarative_axes import DeclarativeAxes
  from ._declarative_box_plot_series import DeclarativeBoxPlotSeries
  from ._declarative_candlestick_series import DeclarativeCandlestickSeries
  from ._declarative_chart import DeclarativeChart
  from ._declarative_pie_series import DeclarativePieSeries
  from ._mouse_event_response import MouseEventResponse
  from ._declarative_abstract_render_node import DeclarativeAbstractRenderNode
  from ._declarative_category_axis import DeclarativeCategoryAxis
  from ._declarative_line_series import DeclarativeLineSeries
  from ._declarative_polar_chart import DeclarativePolarChart
  from ._declarative_scatter_series import DeclarativeScatterSeries
  from ._declarative_area_series import DeclarativeAreaSeries
  from ._declarative_bar_series import DeclarativeBarSeries
  from ._declarative_horizontal_bar_series import DeclarativeHorizontalBarSeries
  from ._declarative_horizontal_percent_bar_series import DeclarativeHorizontalPercentBarSeries
  from ._declarative_horizontal_stacked_bar_series import DeclarativeHorizontalStackedBarSeries
  from ._declarative_open_g_l_render_node import DeclarativeOpenGLRenderNode
  from ._declarative_percent_bar_series import DeclarativePercentBarSeries
  from ._declarative_spline_series import DeclarativeSplineSeries
  from ._declarative_stacked_bar_series import DeclarativeStackedBarSeries
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'DeclarativeXySeries': '_declarative_xy_series',
      'CppQAbstractAxis': '_cpp_q_abstract_axis',
      'CppQAbstractBarSeries': '_cpp_q_abstract_bar_series',
      'CppQAbstractSeries': '_cpp_q_abstract_series',
      'CppQBarCategoryAxis': '_cpp_q_bar_category_axis',
      'CppQBarModelMapper': '_cpp_q_bar_model_mapper',
      'CppQBoxPlotModelMapper': '_cpp_q_box_plot_model_mapper',
      'CppQBrush': '_cpp_q_brush',
      'CppQCandlestickModelMapper': '_cpp_q_candlestick_model_mapper',
      'CppQDateTimeAxis': '_cpp_q_date_time_axis',
      'CppQGraphicsLayout': '_cpp_q_graphics_layout',
      'CppQHBarModelMapper': '_cpp_q_h_bar_model_mapper',
      'CppQHBoxPlotModelMapper': '_cpp_q_h_box_plot_model_mapper',
      'CppQHCandlestickModelMapper': '_cpp_q_h_candlestick_model_mapper',
      'CppQHPieModelMapper': '_cpp_q_h_pie_model_mapper',
      'CppQHXYModelMapper': '_cpp_q_h_x_y_model_mapper',
      'CppQHashPointConfiguration': '_cpp_q_hash_point_configuration',
      'CppQLegend': '_cpp_q_legend',
      'CppQListBarSet': '_cpp_q_list_bar_set',
      'CppQListBoxSet': '_cpp_q_list_box_set',
      'CppQListCandlestickSet': '_cpp_q_list_candlestick_set',
      'CppQListPieSlice': '_cpp_q_list_pie_slice',
      'CppQLogValueAxis': '_cpp_q_log_value_axis',
      'CppQPen': '_cpp_q_pen',
      'CppQPieModelMapper': '_cpp_q_pie_model_mapper',
      'CppQVBarModelMapper': '_cpp_q_v_bar_model_mapper',
      'CppQVBoxPlotModelMapper': '_cpp_q_v_box_plot_model_mapper',
      'CppQVCandlestickModelMapper': '_cpp_q_v_candlestick_model_mapper',
      'CppQVPieModelMapper': '_cpp_q_v_pie_model_mapper',
      'CppQVXYModelMapper': '_cpp_q_v_x_y_model_mapper',
      'CppQValueAxis': '_cpp_q_value_axis',
      'CppQXYModelMapper': '_cpp_q_x_y_model_mapper',
      'CppQXYSeries': '_cpp_q_x_y_series',
      'DeclarativeCategoryRange': '_declarative_category_range',
      'DeclarativeMargins': '_declarative_margins',
      'DeclarativeXYPoint': '_declarative_x_y_point',
      'DeclarativeBarSet': '_declarative_bar_set',
      'DeclarativeBoxSet': '_declarative_box_set',
      'DeclarativeCandlestickSet': '_declarative_candlestick_set',
      'DeclarativePieSlice': '_declarative_pie_slice',
      'DeclarativeChartNode': '_declarative_chart_node',
      'DeclarativeAxes': '_declarative_axes',
      'DeclarativeBoxPlotSeries': '_declarative_box_plot_series',
      'DeclarativeCandlestickSeries': '_declarative_candlestick_series',
      'DeclarativeChart': '_declarative_chart',
      'DeclarativePieSeries': '_declarative_pie_series',
      'MouseEventResponse': '_mouse_event_response',
      'DeclarativeAbstractRenderNode': '_declarative_abstract_render_node',
      'DeclarativeCategoryAxis': '_declarative_category_axis',
      'DeclarativeLineSeries': '_declarative_line_series',
      'DeclarativePolarChart': '_declarative_polar_chart',
      'DeclarativeScatterSeries': '_declarative_scatter_series',
      'DeclarativeAreaSeries': '_declarative_area_series',
      'DeclarativeBarSeries': '_declarative_bar_series',
      'DeclarativeHorizontalBarSeries': '_declarative_horizontal_bar_series',
      'DeclarativeHorizontalPercentBarSeries': '_declarative_horizontal_percent_bar_series',
      'DeclarativeHorizontalStackedBarSeries': '_declarative_horizontal_stacked_bar_series',
      'DeclarativeOpenGLRenderNode': '_declarative_open_g_l_render_node',
      'DeclarativePercentBarSeries': '_declarative_percent_bar_series',
      'DeclarativeSplineSeries': '_declarative_spline_series',
      'DeclarativeStackedBarSeries': '_declarative_stacked_bar_series',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtChartsQml import DeclarativeStackedBarSeries'. Python calls
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
