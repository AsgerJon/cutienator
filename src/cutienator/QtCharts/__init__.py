"""
The 'cutienator.QtCharts' package provides the cute classes of the part
of Qt named QtCharts, under the name PySide6 has for it.

  from cutienator.QtCharts import BoxWhiskersData, CandlestickData

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
    'BoxWhiskersData',
    'CandlestickData',
    'ChartConfig',
    'GLXYSeriesData',
    'PieSliceData',
    'ChartAnimation',
    'QBarSet',
    'QBoxSet',
    'QCandlestickSet',
    'QPieSlice',
    'QBarSetPrivate',
    'QBoxSetPrivate',
    'QCandlestickSetPrivate',
    'QPieSlicePrivate',
    'Scroller',
    'ScrollTicker',
    'PieSliceItem',
    'Bar',
    'ChartBackground',
    'ChartTitle',
    'EditableAxisLabel',
    'PieSliceAnimation',
    'DateTimeAxisLabel',
    'ValueAxisLabel',
    'QAbstractAxis',
    'QChart',
    'AbstractDomain',
    'ChartTheme',
    'QAbstractSeries',
    'ChartPresenter',
    'QLegend',
    'QAbstractAxisPrivate',
    'QAbstractSeriesPrivate',
    'BoxWhiskers',
    'Candlestick',
    'ChartDataSet',
    'ChartThemeBlueCerulean',
    'ChartThemeBlueIcy',
    'ChartThemeBlueNcs',
    'ChartThemeBrownSand',
    'ChartThemeDark',
    'ChartThemeHighContrast',
    'ChartThemeLight',
    'ChartThemeManager',
    'ChartThemeQt',
    'ChartThemeSystem',
    'LegendLayout',
    'LegendMoveResizeHandler',
    'LegendScroller',
    'LogXLogYDomain',
    'LogXYDomain',
    'PolarDomain',
    'QBarCategoryAxis',
    'QBarCategoryAxisPrivate',
    'QBoxPlotSeries',
    'QCandlestickSeries',
    'QChartPrivate',
    'QChartView',
    'QColorAxis',
    'QColorAxisPrivate',
    'QDateTimeAxis',
    'QDateTimeAxisPrivate',
    'QLegendMarker',
    'QLegendMarkerPrivate',
    'QLogValueAxis',
    'QLogValueAxisPrivate',
    'QPieSeries',
    'QPolarChart',
    'QValueAxis',
    'QValueAxisPrivate',
    'QXYSeries',
    'QXYSeriesPrivate',
    'XLogYDomain',
    'XYDomain',
    'ChartElement',
    'GLXYSeriesDataManager',
    'LegendMarkerItem',
    'LogXLogYPolarDomain',
    'LogXYPolarDomain',
    'QAbstractBarSeries',
    'QAbstractBarSeriesPrivate',
    'QBoxPlotLegendMarker',
    'QBoxPlotLegendMarkerPrivate',
    'QBoxPlotModelMapper',
    'QBoxPlotSeriesPrivate',
    'QCandlestickLegendMarker',
    'QCandlestickModelMapper',
    'QCandlestickSeriesPrivate',
    'QCategoryAxis',
    'QCategoryAxisPrivate',
    'QChartViewPrivate',
    'QLegendPrivate',
    'QLineSeries',
    'QLineSeriesPrivate',
    'QPieLegendMarker',
    'QPieLegendMarkerPrivate',
    'QPieModelMapper',
    'QPieSeriesPrivate',
    'QScatterSeries',
    'QXYLegendMarker',
    'QXYLegendMarkerPrivate',
    'QXYModelMapper',
    'XLogYPolarDomain',
    'XYPolarDomain',
    'AxisAnimation',
    'ChartAxisElement',
    'ChartItem',
    'GLWidget',
    'QAreaSeries',
    'QBarLegendMarker',
    'QBarLegendMarkerPrivate',
    'QBarModelMapper',
    'QBarSeries',
    'QBoxPlotModelMapperPrivate',
    'QCandlestickLegendMarkerPrivate',
    'QCandlestickModelMapperPrivate',
    'QHBoxPlotModelMapper',
    'QHCandlestickModelMapper',
    'QHPieModelMapper',
    'QHXYModelMapper',
    'QHorizontalBarSeries',
    'QHorizontalPercentBarSeries',
    'QHorizontalStackedBarSeries',
    'QPercentBarSeries',
    'QPieModelMapperPrivate',
    'QScatterSeriesPrivate',
    'QSplineSeries',
    'QStackedBarSeries',
    'QVBoxPlotModelMapper',
    'QVCandlestickModelMapper',
    'QVPieModelMapper',
    'QVXYModelMapper',
    'QXYModelMapperPrivate',
    'AbstractBarChartItem',
    'BarAnimation',
    'AbstractChartLayout',
    'BoxPlotAnimation',
    'BoxPlotChartItem',
    'CandlestickAnimation',
    'CandlestickChartItem',
    'CartesianChartAxis',
    'LineArrowItem',
    'PieAnimation',
    'PieChartItem',
    'PolarChartAxis',
    'QAreaLegendMarker',
    'QAreaLegendMarkerPrivate',
    'QAreaSeriesPrivate',
    'QBarModelMapperPrivate',
    'QBarSeriesPrivate',
    'QHBarModelMapper',
    'QHorizontalBarSeriesPrivate',
    'QHorizontalPercentBarSeriesPrivate',
    'QHorizontalStackedBarSeriesPrivate',
    'QPercentBarSeriesPrivate',
    'QSplineSeriesPrivate',
    'QStackedBarSeriesPrivate',
    'QVBarModelMapper',
    'XYAnimation',
    'XYChart',
    'BarChartItem',
    'BoxWhiskersAnimation',
    'CandlestickBodyWicksAnimation',
    'CartesianChartLayout',
    'HorizontalAxis',
    'HorizontalBarChartItem',
    'HorizontalPercentBarChartItem',
    'HorizontalStackedBarChartItem',
    'LineChartItem',
    'PercentBarChartItem',
    'PolarChartAxisAngular',
    'PolarChartAxisRadial',
    'PolarChartLayout',
    'ScatterChartItem',
    'SplineAnimation',
    'SplineChartItem',
    'StackedBarChartItem',
    'VerticalAxis',
    'AreaChartItem',
    'ChartBarCategoryAxisX',
    'ChartBarCategoryAxisY',
    'ChartCategoryAxisX',
    'ChartCategoryAxisY',
    'ChartColorAxisX',
    'ChartColorAxisY',
    'ChartDateTimeAxisX',
    'ChartDateTimeAxisY',
    'ChartLogValueAxisX',
    'ChartLogValueAxisY',
    'ChartValueAxisX',
    'ChartValueAxisY',
    'PentagonMarker',
    'PolarChartCategoryAxisAngular',
    'PolarChartCategoryAxisRadial',
    'PolarChartDateTimeAxisAngular',
    'PolarChartDateTimeAxisRadial',
    'PolarChartLogValueAxisAngular',
    'PolarChartLogValueAxisRadial',
    'PolarChartValueAxisAngular',
    'PolarChartValueAxisRadial',
    'RotatedRectangleMarker',
    'ScatterAnimation',
    'StarMarker',
    'TriangleMarker',
    'AreaBoundItem',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._box_whiskers_data import BoxWhiskersData
  from ._candlestick_data import CandlestickData
  from ._chart_config import ChartConfig
  from ._g_l_x_y_series_data import GLXYSeriesData
  from ._pie_slice_data import PieSliceData
  from ._chart_animation import ChartAnimation
  from ._q_bar_set import QBarSet
  from ._q_box_set import QBoxSet
  from ._q_candlestick_set import QCandlestickSet
  from ._q_pie_slice import QPieSlice
  from ._q_bar_set_private import QBarSetPrivate
  from ._q_box_set_private import QBoxSetPrivate
  from ._q_candlestick_set_private import QCandlestickSetPrivate
  from ._q_pie_slice_private import QPieSlicePrivate
  from ._scroller import Scroller
  from ._scroll_ticker import ScrollTicker
  from ._pie_slice_item import PieSliceItem
  from ._bar import Bar
  from ._chart_background import ChartBackground
  from ._chart_title import ChartTitle
  from ._editable_axis_label import EditableAxisLabel
  from ._pie_slice_animation import PieSliceAnimation
  from ._date_time_axis_label import DateTimeAxisLabel
  from ._value_axis_label import ValueAxisLabel
  from ._q_abstract_axis import QAbstractAxis
  from ._q_chart import QChart
  from ._abstract_domain import AbstractDomain
  from ._chart_theme import ChartTheme
  from ._q_abstract_series import QAbstractSeries
  from ._chart_presenter import ChartPresenter
  from ._q_legend import QLegend
  from ._q_abstract_axis_private import QAbstractAxisPrivate
  from ._q_abstract_series_private import QAbstractSeriesPrivate
  from ._box_whiskers import BoxWhiskers
  from ._candlestick import Candlestick
  from ._chart_data_set import ChartDataSet
  from ._chart_theme_blue_cerulean import ChartThemeBlueCerulean
  from ._chart_theme_blue_icy import ChartThemeBlueIcy
  from ._chart_theme_blue_ncs import ChartThemeBlueNcs
  from ._chart_theme_brown_sand import ChartThemeBrownSand
  from ._chart_theme_dark import ChartThemeDark
  from ._chart_theme_high_contrast import ChartThemeHighContrast
  from ._chart_theme_light import ChartThemeLight
  from ._chart_theme_manager import ChartThemeManager
  from ._chart_theme_qt import ChartThemeQt
  from ._chart_theme_system import ChartThemeSystem
  from ._legend_layout import LegendLayout
  from ._legend_move_resize_handler import LegendMoveResizeHandler
  from ._legend_scroller import LegendScroller
  from ._log_x_log_y_domain import LogXLogYDomain
  from ._log_x_y_domain import LogXYDomain
  from ._polar_domain import PolarDomain
  from ._q_bar_category_axis import QBarCategoryAxis
  from ._q_bar_category_axis_private import QBarCategoryAxisPrivate
  from ._q_box_plot_series import QBoxPlotSeries
  from ._q_candlestick_series import QCandlestickSeries
  from ._q_chart_private import QChartPrivate
  from ._q_chart_view import QChartView
  from ._q_color_axis import QColorAxis
  from ._q_color_axis_private import QColorAxisPrivate
  from ._q_date_time_axis import QDateTimeAxis
  from ._q_date_time_axis_private import QDateTimeAxisPrivate
  from ._q_legend_marker import QLegendMarker
  from ._q_legend_marker_private import QLegendMarkerPrivate
  from ._q_log_value_axis import QLogValueAxis
  from ._q_log_value_axis_private import QLogValueAxisPrivate
  from ._q_pie_series import QPieSeries
  from ._q_polar_chart import QPolarChart
  from ._q_value_axis import QValueAxis
  from ._q_value_axis_private import QValueAxisPrivate
  from ._q_x_y_series import QXYSeries
  from ._q_x_y_series_private import QXYSeriesPrivate
  from ._x_log_y_domain import XLogYDomain
  from ._x_y_domain import XYDomain
  from ._chart_element import ChartElement
  from ._g_l_x_y_series_data_manager import GLXYSeriesDataManager
  from ._legend_marker_item import LegendMarkerItem
  from ._log_x_log_y_polar_domain import LogXLogYPolarDomain
  from ._log_x_y_polar_domain import LogXYPolarDomain
  from ._q_abstract_bar_series import QAbstractBarSeries
  from ._q_abstract_bar_series_private import QAbstractBarSeriesPrivate
  from ._q_box_plot_legend_marker import QBoxPlotLegendMarker
  from ._q_box_plot_legend_marker_private import QBoxPlotLegendMarkerPrivate
  from ._q_box_plot_model_mapper import QBoxPlotModelMapper
  from ._q_box_plot_series_private import QBoxPlotSeriesPrivate
  from ._q_candlestick_legend_marker import QCandlestickLegendMarker
  from ._q_candlestick_model_mapper import QCandlestickModelMapper
  from ._q_candlestick_series_private import QCandlestickSeriesPrivate
  from ._q_category_axis import QCategoryAxis
  from ._q_category_axis_private import QCategoryAxisPrivate
  from ._q_chart_view_private import QChartViewPrivate
  from ._q_legend_private import QLegendPrivate
  from ._q_line_series import QLineSeries
  from ._q_line_series_private import QLineSeriesPrivate
  from ._q_pie_legend_marker import QPieLegendMarker
  from ._q_pie_legend_marker_private import QPieLegendMarkerPrivate
  from ._q_pie_model_mapper import QPieModelMapper
  from ._q_pie_series_private import QPieSeriesPrivate
  from ._q_scatter_series import QScatterSeries
  from ._q_x_y_legend_marker import QXYLegendMarker
  from ._q_x_y_legend_marker_private import QXYLegendMarkerPrivate
  from ._q_x_y_model_mapper import QXYModelMapper
  from ._x_log_y_polar_domain import XLogYPolarDomain
  from ._x_y_polar_domain import XYPolarDomain
  from ._axis_animation import AxisAnimation
  from ._chart_axis_element import ChartAxisElement
  from ._chart_item import ChartItem
  from ._g_l_widget import GLWidget
  from ._q_area_series import QAreaSeries
  from ._q_bar_legend_marker import QBarLegendMarker
  from ._q_bar_legend_marker_private import QBarLegendMarkerPrivate
  from ._q_bar_model_mapper import QBarModelMapper
  from ._q_bar_series import QBarSeries
  from ._q_box_plot_model_mapper_private import QBoxPlotModelMapperPrivate
  from ._q_candlestick_legend_marker_private import QCandlestickLegendMarkerPrivate
  from ._q_candlestick_model_mapper_private import QCandlestickModelMapperPrivate
  from ._q_h_box_plot_model_mapper import QHBoxPlotModelMapper
  from ._q_h_candlestick_model_mapper import QHCandlestickModelMapper
  from ._q_h_pie_model_mapper import QHPieModelMapper
  from ._q_h_x_y_model_mapper import QHXYModelMapper
  from ._q_horizontal_bar_series import QHorizontalBarSeries
  from ._q_horizontal_percent_bar_series import QHorizontalPercentBarSeries
  from ._q_horizontal_stacked_bar_series import QHorizontalStackedBarSeries
  from ._q_percent_bar_series import QPercentBarSeries
  from ._q_pie_model_mapper_private import QPieModelMapperPrivate
  from ._q_scatter_series_private import QScatterSeriesPrivate
  from ._q_spline_series import QSplineSeries
  from ._q_stacked_bar_series import QStackedBarSeries
  from ._q_v_box_plot_model_mapper import QVBoxPlotModelMapper
  from ._q_v_candlestick_model_mapper import QVCandlestickModelMapper
  from ._q_v_pie_model_mapper import QVPieModelMapper
  from ._q_v_x_y_model_mapper import QVXYModelMapper
  from ._q_x_y_model_mapper_private import QXYModelMapperPrivate
  from ._abstract_bar_chart_item import AbstractBarChartItem
  from ._bar_animation import BarAnimation
  from ._abstract_chart_layout import AbstractChartLayout
  from ._box_plot_animation import BoxPlotAnimation
  from ._box_plot_chart_item import BoxPlotChartItem
  from ._candlestick_animation import CandlestickAnimation
  from ._candlestick_chart_item import CandlestickChartItem
  from ._cartesian_chart_axis import CartesianChartAxis
  from ._line_arrow_item import LineArrowItem
  from ._pie_animation import PieAnimation
  from ._pie_chart_item import PieChartItem
  from ._polar_chart_axis import PolarChartAxis
  from ._q_area_legend_marker import QAreaLegendMarker
  from ._q_area_legend_marker_private import QAreaLegendMarkerPrivate
  from ._q_area_series_private import QAreaSeriesPrivate
  from ._q_bar_model_mapper_private import QBarModelMapperPrivate
  from ._q_bar_series_private import QBarSeriesPrivate
  from ._q_h_bar_model_mapper import QHBarModelMapper
  from ._q_horizontal_bar_series_private import QHorizontalBarSeriesPrivate
  from ._q_horizontal_percent_bar_series_private import QHorizontalPercentBarSeriesPrivate
  from ._q_horizontal_stacked_bar_series_private import QHorizontalStackedBarSeriesPrivate
  from ._q_percent_bar_series_private import QPercentBarSeriesPrivate
  from ._q_spline_series_private import QSplineSeriesPrivate
  from ._q_stacked_bar_series_private import QStackedBarSeriesPrivate
  from ._q_v_bar_model_mapper import QVBarModelMapper
  from ._x_y_animation import XYAnimation
  from ._x_y_chart import XYChart
  from ._bar_chart_item import BarChartItem
  from ._box_whiskers_animation import BoxWhiskersAnimation
  from ._candlestick_body_wicks_animation import CandlestickBodyWicksAnimation
  from ._cartesian_chart_layout import CartesianChartLayout
  from ._horizontal_axis import HorizontalAxis
  from ._horizontal_bar_chart_item import HorizontalBarChartItem
  from ._horizontal_percent_bar_chart_item import HorizontalPercentBarChartItem
  from ._horizontal_stacked_bar_chart_item import HorizontalStackedBarChartItem
  from ._line_chart_item import LineChartItem
  from ._percent_bar_chart_item import PercentBarChartItem
  from ._polar_chart_axis_angular import PolarChartAxisAngular
  from ._polar_chart_axis_radial import PolarChartAxisRadial
  from ._polar_chart_layout import PolarChartLayout
  from ._scatter_chart_item import ScatterChartItem
  from ._spline_animation import SplineAnimation
  from ._spline_chart_item import SplineChartItem
  from ._stacked_bar_chart_item import StackedBarChartItem
  from ._vertical_axis import VerticalAxis
  from ._area_chart_item import AreaChartItem
  from ._chart_bar_category_axis_x import ChartBarCategoryAxisX
  from ._chart_bar_category_axis_y import ChartBarCategoryAxisY
  from ._chart_category_axis_x import ChartCategoryAxisX
  from ._chart_category_axis_y import ChartCategoryAxisY
  from ._chart_color_axis_x import ChartColorAxisX
  from ._chart_color_axis_y import ChartColorAxisY
  from ._chart_date_time_axis_x import ChartDateTimeAxisX
  from ._chart_date_time_axis_y import ChartDateTimeAxisY
  from ._chart_log_value_axis_x import ChartLogValueAxisX
  from ._chart_log_value_axis_y import ChartLogValueAxisY
  from ._chart_value_axis_x import ChartValueAxisX
  from ._chart_value_axis_y import ChartValueAxisY
  from ._pentagon_marker import PentagonMarker
  from ._polar_chart_category_axis_angular import PolarChartCategoryAxisAngular
  from ._polar_chart_category_axis_radial import PolarChartCategoryAxisRadial
  from ._polar_chart_date_time_axis_angular import PolarChartDateTimeAxisAngular
  from ._polar_chart_date_time_axis_radial import PolarChartDateTimeAxisRadial
  from ._polar_chart_log_value_axis_angular import PolarChartLogValueAxisAngular
  from ._polar_chart_log_value_axis_radial import PolarChartLogValueAxisRadial
  from ._polar_chart_value_axis_angular import PolarChartValueAxisAngular
  from ._polar_chart_value_axis_radial import PolarChartValueAxisRadial
  from ._rotated_rectangle_marker import RotatedRectangleMarker
  from ._scatter_animation import ScatterAnimation
  from ._star_marker import StarMarker
  from ._triangle_marker import TriangleMarker
  from ._area_bound_item import AreaBoundItem
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'BoxWhiskersData': '_box_whiskers_data',
      'CandlestickData': '_candlestick_data',
      'ChartConfig': '_chart_config',
      'GLXYSeriesData': '_g_l_x_y_series_data',
      'PieSliceData': '_pie_slice_data',
      'ChartAnimation': '_chart_animation',
      'QBarSet': '_q_bar_set',
      'QBoxSet': '_q_box_set',
      'QCandlestickSet': '_q_candlestick_set',
      'QPieSlice': '_q_pie_slice',
      'QBarSetPrivate': '_q_bar_set_private',
      'QBoxSetPrivate': '_q_box_set_private',
      'QCandlestickSetPrivate': '_q_candlestick_set_private',
      'QPieSlicePrivate': '_q_pie_slice_private',
      'Scroller': '_scroller',
      'ScrollTicker': '_scroll_ticker',
      'PieSliceItem': '_pie_slice_item',
      'Bar': '_bar',
      'ChartBackground': '_chart_background',
      'ChartTitle': '_chart_title',
      'EditableAxisLabel': '_editable_axis_label',
      'PieSliceAnimation': '_pie_slice_animation',
      'DateTimeAxisLabel': '_date_time_axis_label',
      'ValueAxisLabel': '_value_axis_label',
      'QAbstractAxis': '_q_abstract_axis',
      'QChart': '_q_chart',
      'AbstractDomain': '_abstract_domain',
      'ChartTheme': '_chart_theme',
      'QAbstractSeries': '_q_abstract_series',
      'ChartPresenter': '_chart_presenter',
      'QLegend': '_q_legend',
      'QAbstractAxisPrivate': '_q_abstract_axis_private',
      'QAbstractSeriesPrivate': '_q_abstract_series_private',
      'BoxWhiskers': '_box_whiskers',
      'Candlestick': '_candlestick',
      'ChartDataSet': '_chart_data_set',
      'ChartThemeBlueCerulean': '_chart_theme_blue_cerulean',
      'ChartThemeBlueIcy': '_chart_theme_blue_icy',
      'ChartThemeBlueNcs': '_chart_theme_blue_ncs',
      'ChartThemeBrownSand': '_chart_theme_brown_sand',
      'ChartThemeDark': '_chart_theme_dark',
      'ChartThemeHighContrast': '_chart_theme_high_contrast',
      'ChartThemeLight': '_chart_theme_light',
      'ChartThemeManager': '_chart_theme_manager',
      'ChartThemeQt': '_chart_theme_qt',
      'ChartThemeSystem': '_chart_theme_system',
      'LegendLayout': '_legend_layout',
      'LegendMoveResizeHandler': '_legend_move_resize_handler',
      'LegendScroller': '_legend_scroller',
      'LogXLogYDomain': '_log_x_log_y_domain',
      'LogXYDomain': '_log_x_y_domain',
      'PolarDomain': '_polar_domain',
      'QBarCategoryAxis': '_q_bar_category_axis',
      'QBarCategoryAxisPrivate': '_q_bar_category_axis_private',
      'QBoxPlotSeries': '_q_box_plot_series',
      'QCandlestickSeries': '_q_candlestick_series',
      'QChartPrivate': '_q_chart_private',
      'QChartView': '_q_chart_view',
      'QColorAxis': '_q_color_axis',
      'QColorAxisPrivate': '_q_color_axis_private',
      'QDateTimeAxis': '_q_date_time_axis',
      'QDateTimeAxisPrivate': '_q_date_time_axis_private',
      'QLegendMarker': '_q_legend_marker',
      'QLegendMarkerPrivate': '_q_legend_marker_private',
      'QLogValueAxis': '_q_log_value_axis',
      'QLogValueAxisPrivate': '_q_log_value_axis_private',
      'QPieSeries': '_q_pie_series',
      'QPolarChart': '_q_polar_chart',
      'QValueAxis': '_q_value_axis',
      'QValueAxisPrivate': '_q_value_axis_private',
      'QXYSeries': '_q_x_y_series',
      'QXYSeriesPrivate': '_q_x_y_series_private',
      'XLogYDomain': '_x_log_y_domain',
      'XYDomain': '_x_y_domain',
      'ChartElement': '_chart_element',
      'GLXYSeriesDataManager': '_g_l_x_y_series_data_manager',
      'LegendMarkerItem': '_legend_marker_item',
      'LogXLogYPolarDomain': '_log_x_log_y_polar_domain',
      'LogXYPolarDomain': '_log_x_y_polar_domain',
      'QAbstractBarSeries': '_q_abstract_bar_series',
      'QAbstractBarSeriesPrivate': '_q_abstract_bar_series_private',
      'QBoxPlotLegendMarker': '_q_box_plot_legend_marker',
      'QBoxPlotLegendMarkerPrivate': '_q_box_plot_legend_marker_private',
      'QBoxPlotModelMapper': '_q_box_plot_model_mapper',
      'QBoxPlotSeriesPrivate': '_q_box_plot_series_private',
      'QCandlestickLegendMarker': '_q_candlestick_legend_marker',
      'QCandlestickModelMapper': '_q_candlestick_model_mapper',
      'QCandlestickSeriesPrivate': '_q_candlestick_series_private',
      'QCategoryAxis': '_q_category_axis',
      'QCategoryAxisPrivate': '_q_category_axis_private',
      'QChartViewPrivate': '_q_chart_view_private',
      'QLegendPrivate': '_q_legend_private',
      'QLineSeries': '_q_line_series',
      'QLineSeriesPrivate': '_q_line_series_private',
      'QPieLegendMarker': '_q_pie_legend_marker',
      'QPieLegendMarkerPrivate': '_q_pie_legend_marker_private',
      'QPieModelMapper': '_q_pie_model_mapper',
      'QPieSeriesPrivate': '_q_pie_series_private',
      'QScatterSeries': '_q_scatter_series',
      'QXYLegendMarker': '_q_x_y_legend_marker',
      'QXYLegendMarkerPrivate': '_q_x_y_legend_marker_private',
      'QXYModelMapper': '_q_x_y_model_mapper',
      'XLogYPolarDomain': '_x_log_y_polar_domain',
      'XYPolarDomain': '_x_y_polar_domain',
      'AxisAnimation': '_axis_animation',
      'ChartAxisElement': '_chart_axis_element',
      'ChartItem': '_chart_item',
      'GLWidget': '_g_l_widget',
      'QAreaSeries': '_q_area_series',
      'QBarLegendMarker': '_q_bar_legend_marker',
      'QBarLegendMarkerPrivate': '_q_bar_legend_marker_private',
      'QBarModelMapper': '_q_bar_model_mapper',
      'QBarSeries': '_q_bar_series',
      'QBoxPlotModelMapperPrivate': '_q_box_plot_model_mapper_private',
      'QCandlestickLegendMarkerPrivate': '_q_candlestick_legend_marker_private',
      'QCandlestickModelMapperPrivate': '_q_candlestick_model_mapper_private',
      'QHBoxPlotModelMapper': '_q_h_box_plot_model_mapper',
      'QHCandlestickModelMapper': '_q_h_candlestick_model_mapper',
      'QHPieModelMapper': '_q_h_pie_model_mapper',
      'QHXYModelMapper': '_q_h_x_y_model_mapper',
      'QHorizontalBarSeries': '_q_horizontal_bar_series',
      'QHorizontalPercentBarSeries': '_q_horizontal_percent_bar_series',
      'QHorizontalStackedBarSeries': '_q_horizontal_stacked_bar_series',
      'QPercentBarSeries': '_q_percent_bar_series',
      'QPieModelMapperPrivate': '_q_pie_model_mapper_private',
      'QScatterSeriesPrivate': '_q_scatter_series_private',
      'QSplineSeries': '_q_spline_series',
      'QStackedBarSeries': '_q_stacked_bar_series',
      'QVBoxPlotModelMapper': '_q_v_box_plot_model_mapper',
      'QVCandlestickModelMapper': '_q_v_candlestick_model_mapper',
      'QVPieModelMapper': '_q_v_pie_model_mapper',
      'QVXYModelMapper': '_q_v_x_y_model_mapper',
      'QXYModelMapperPrivate': '_q_x_y_model_mapper_private',
      'AbstractBarChartItem': '_abstract_bar_chart_item',
      'BarAnimation': '_bar_animation',
      'AbstractChartLayout': '_abstract_chart_layout',
      'BoxPlotAnimation': '_box_plot_animation',
      'BoxPlotChartItem': '_box_plot_chart_item',
      'CandlestickAnimation': '_candlestick_animation',
      'CandlestickChartItem': '_candlestick_chart_item',
      'CartesianChartAxis': '_cartesian_chart_axis',
      'LineArrowItem': '_line_arrow_item',
      'PieAnimation': '_pie_animation',
      'PieChartItem': '_pie_chart_item',
      'PolarChartAxis': '_polar_chart_axis',
      'QAreaLegendMarker': '_q_area_legend_marker',
      'QAreaLegendMarkerPrivate': '_q_area_legend_marker_private',
      'QAreaSeriesPrivate': '_q_area_series_private',
      'QBarModelMapperPrivate': '_q_bar_model_mapper_private',
      'QBarSeriesPrivate': '_q_bar_series_private',
      'QHBarModelMapper': '_q_h_bar_model_mapper',
      'QHorizontalBarSeriesPrivate': '_q_horizontal_bar_series_private',
      'QHorizontalPercentBarSeriesPrivate': '_q_horizontal_percent_bar_series_private',
      'QHorizontalStackedBarSeriesPrivate': '_q_horizontal_stacked_bar_series_private',
      'QPercentBarSeriesPrivate': '_q_percent_bar_series_private',
      'QSplineSeriesPrivate': '_q_spline_series_private',
      'QStackedBarSeriesPrivate': '_q_stacked_bar_series_private',
      'QVBarModelMapper': '_q_v_bar_model_mapper',
      'XYAnimation': '_x_y_animation',
      'XYChart': '_x_y_chart',
      'BarChartItem': '_bar_chart_item',
      'BoxWhiskersAnimation': '_box_whiskers_animation',
      'CandlestickBodyWicksAnimation': '_candlestick_body_wicks_animation',
      'CartesianChartLayout': '_cartesian_chart_layout',
      'HorizontalAxis': '_horizontal_axis',
      'HorizontalBarChartItem': '_horizontal_bar_chart_item',
      'HorizontalPercentBarChartItem': '_horizontal_percent_bar_chart_item',
      'HorizontalStackedBarChartItem': '_horizontal_stacked_bar_chart_item',
      'LineChartItem': '_line_chart_item',
      'PercentBarChartItem': '_percent_bar_chart_item',
      'PolarChartAxisAngular': '_polar_chart_axis_angular',
      'PolarChartAxisRadial': '_polar_chart_axis_radial',
      'PolarChartLayout': '_polar_chart_layout',
      'ScatterChartItem': '_scatter_chart_item',
      'SplineAnimation': '_spline_animation',
      'SplineChartItem': '_spline_chart_item',
      'StackedBarChartItem': '_stacked_bar_chart_item',
      'VerticalAxis': '_vertical_axis',
      'AreaChartItem': '_area_chart_item',
      'ChartBarCategoryAxisX': '_chart_bar_category_axis_x',
      'ChartBarCategoryAxisY': '_chart_bar_category_axis_y',
      'ChartCategoryAxisX': '_chart_category_axis_x',
      'ChartCategoryAxisY': '_chart_category_axis_y',
      'ChartColorAxisX': '_chart_color_axis_x',
      'ChartColorAxisY': '_chart_color_axis_y',
      'ChartDateTimeAxisX': '_chart_date_time_axis_x',
      'ChartDateTimeAxisY': '_chart_date_time_axis_y',
      'ChartLogValueAxisX': '_chart_log_value_axis_x',
      'ChartLogValueAxisY': '_chart_log_value_axis_y',
      'ChartValueAxisX': '_chart_value_axis_x',
      'ChartValueAxisY': '_chart_value_axis_y',
      'PentagonMarker': '_pentagon_marker',
      'PolarChartCategoryAxisAngular': '_polar_chart_category_axis_angular',
      'PolarChartCategoryAxisRadial': '_polar_chart_category_axis_radial',
      'PolarChartDateTimeAxisAngular': '_polar_chart_date_time_axis_angular',
      'PolarChartDateTimeAxisRadial': '_polar_chart_date_time_axis_radial',
      'PolarChartLogValueAxisAngular': '_polar_chart_log_value_axis_angular',
      'PolarChartLogValueAxisRadial': '_polar_chart_log_value_axis_radial',
      'PolarChartValueAxisAngular': '_polar_chart_value_axis_angular',
      'PolarChartValueAxisRadial': '_polar_chart_value_axis_radial',
      'RotatedRectangleMarker': '_rotated_rectangle_marker',
      'ScatterAnimation': '_scatter_animation',
      'StarMarker': '_star_marker',
      'TriangleMarker': '_triangle_marker',
      'AreaBoundItem': '_area_bound_item',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCharts import AreaBoundItem'. Python calls
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
