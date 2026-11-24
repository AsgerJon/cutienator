//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xychart_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xychart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/xychart_p.h>
#include <QtCharts/QXYSeries>
#include <private/qxyseries_p.h>
#include <private/chartpresenter_p.h>
#include <private/abstractdomain_p.h>
#include <private/chartdataset_p.h>
#include <private/glxyseriesdata_p.h>
#include <QtCharts/QXYModelMapper>
#include <private/qabstractaxis_p.h>
#include <QtGui/QPainter>
#include <QtCore/QAbstractItemModel>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/charts/xychart/xychart.cpp, line 228, as _ZN7XYChart7isEmptyEv
inline bool XYChart::isEmpty()
{
    return domain()->isEmpty() || m_series->points().isEmpty();
}
//  -----------------------------------------------------------------------

//  Only a class built on XYChart may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnXYChart : XYChart {
  using XYChart::updateGlChart;
  using XYChart::refreshGlChart;
};

//  A XYChart that Python can take functions over in. Every XYChart
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteXYChartCall0)(const void *, int *);
typedef void (*CuteXYChartCall1)(const void *, int *);
typedef void (*CuteXYChartCall2)(const void *, int *);
typedef void (*CuteXYChartCall3)(const void *, int *);
typedef void (*CuteXYChartCall4)(const void *, int *);
typedef void (*CuteXYChartCall5)(const void *, int *);
typedef void (*CuteXYChartCall6)(const void *, int *);
typedef void (*CuteXYChartCall7)(const void *, ChartPresenter *, int *);
typedef void (*CuteXYChartCall8)(const void *, ChartThemeManager *, int *);
typedef void (*CuteXYChartCall9)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall10)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYChartCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYChartCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYChartCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYChartCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYChartCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYChartCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall17)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteXYChartCall18)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteXYChartCall19)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall20)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall21)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall22)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall23)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteXYChartCall24)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall25)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteXYChartCall26)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall27)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteXYChartCall28)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall29)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall30)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall31)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall32)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall33)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall34)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall35)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall36)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall37)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall38)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall39)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall40)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall41)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall42)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall43)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall44)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall45)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteXYChartCall46)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteXYChartCall47)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteXYChartCall48)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteXYChartCall49)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteXYChart : public XYChart {
public:
  using XYChart::XYChart;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart14updateGeometryEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart19handleSeriesUpdatedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart13updateGlChartEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart14refreshGlChartEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem7cleanupEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

  //  ChartAnimation *XYChart::animation() const
  ChartAnimation *animation() const override {
    if (taken[0]) {
      int handled = 0;
      CuteXYChartCall0 call = reinterpret_cast<CuteXYChartCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return XYChart::animation();
  }

  //  void XYChart::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteXYChartCall1 call = reinterpret_cast<CuteXYChartCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void XYChart::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[2]) {
      int handled = 0;
      CuteXYChartCall2 call = reinterpret_cast<CuteXYChartCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::handleDomainUpdated();
  }

  //  void XYChart::handleSeriesUpdated()
  void handleSeriesUpdated() override {
    if (taken[3]) {
      int handled = 0;
      CuteXYChartCall3 call = reinterpret_cast<CuteXYChartCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::handleSeriesUpdated();
  }

  //  void XYChart::updateGlChart()
  void updateGlChart() override {
    if (taken[4]) {
      int handled = 0;
      CuteXYChartCall4 call = reinterpret_cast<CuteXYChartCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::updateGlChart();
  }

  //  void XYChart::refreshGlChart()
  void refreshGlChart() override {
    if (taken[5]) {
      int handled = 0;
      CuteXYChartCall5 call = reinterpret_cast<CuteXYChartCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::refreshGlChart();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[6]) {
      int handled = 0;
      CuteXYChartCall6 call = reinterpret_cast<CuteXYChartCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[7]) {
      int handled = 0;
      CuteXYChartCall7 call = reinterpret_cast<CuteXYChartCall7>(taken[7]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[8]) {
      int handled = 0;
      CuteXYChartCall8 call = reinterpret_cast<CuteXYChartCall8>(taken[8]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[9]) {
      int handled = 0;
      CuteXYChartCall9 call = reinterpret_cast<CuteXYChartCall9>(taken[9]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[10]) {
      int handled = 0;
      CuteXYChartCall10 call = reinterpret_cast<CuteXYChartCall10>(taken[10]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QGraphicsObject::event(ev);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteXYChartCall11 call = reinterpret_cast<CuteXYChartCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteXYChartCall12 call = reinterpret_cast<CuteXYChartCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteXYChartCall13 call = reinterpret_cast<CuteXYChartCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteXYChartCall14 call = reinterpret_cast<CuteXYChartCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteXYChartCall15 call = reinterpret_cast<CuteXYChartCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteXYChartCall16 call = reinterpret_cast<CuteXYChartCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[17]) {
      int handled = 0;
      CuteXYChartCall17 call = reinterpret_cast<CuteXYChartCall17>(taken[17]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF QGraphicsItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteXYChartCall18 call = reinterpret_cast<CuteXYChartCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[19]) {
      int handled = 0;
      CuteXYChartCall19 call = reinterpret_cast<CuteXYChartCall19>(taken[19]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteXYChartCall20 call = reinterpret_cast<CuteXYChartCall20>(taken[20]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::contains(point);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithItem(
      const QGraphicsItem *other,
      Qt::ItemSelectionMode mode) const override {
    if (taken[21]) {
      int handled = 0;
      CuteXYChartCall21 call = reinterpret_cast<CuteXYChartCall21>(taken[21]);
      bool given = call(this, other, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithItem(other, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::collidesWithPath(const QPainterPath &path,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithPath(
      const QPainterPath &path,
      Qt::ItemSelectionMode mode) const override {
    if (taken[22]) {
      int handled = 0;
      CuteXYChartCall22 call = reinterpret_cast<CuteXYChartCall22>(taken[22]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[23]) {
      int handled = 0;
      CuteXYChartCall23 call = reinterpret_cast<CuteXYChartCall23>(taken[23]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[24]) {
      int handled = 0;
      CuteXYChartCall24 call = reinterpret_cast<CuteXYChartCall24>(taken[24]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[25]) {
      int handled = 0;
      CuteXYChartCall25 call = reinterpret_cast<CuteXYChartCall25>(taken[25]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[26]) {
      int handled = 0;
      CuteXYChartCall26 call = reinterpret_cast<CuteXYChartCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteXYChartCall27 call = reinterpret_cast<CuteXYChartCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteXYChartCall28 call = reinterpret_cast<CuteXYChartCall28>(taken[28]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteXYChartCall29 call = reinterpret_cast<CuteXYChartCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteXYChartCall30 call = reinterpret_cast<CuteXYChartCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteXYChartCall31 call = reinterpret_cast<CuteXYChartCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteXYChartCall32 call = reinterpret_cast<CuteXYChartCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteXYChartCall33 call = reinterpret_cast<CuteXYChartCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteXYChartCall34 call = reinterpret_cast<CuteXYChartCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteXYChartCall35 call = reinterpret_cast<CuteXYChartCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteXYChartCall36 call = reinterpret_cast<CuteXYChartCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteXYChartCall37 call = reinterpret_cast<CuteXYChartCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteXYChartCall38 call = reinterpret_cast<CuteXYChartCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteXYChartCall39 call = reinterpret_cast<CuteXYChartCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteXYChartCall40 call = reinterpret_cast<CuteXYChartCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteXYChartCall41 call = reinterpret_cast<CuteXYChartCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteXYChartCall42 call = reinterpret_cast<CuteXYChartCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteXYChartCall43 call = reinterpret_cast<CuteXYChartCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteXYChartCall44 call = reinterpret_cast<CuteXYChartCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteXYChartCall45 call = reinterpret_cast<CuteXYChartCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteXYChartCall46 call = reinterpret_cast<CuteXYChartCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[47]) {
      int handled = 0;
      CuteXYChartCall47 call = reinterpret_cast<CuteXYChartCall47>(taken[47]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[48]) {
      int handled = 0;
      CuteXYChartCall48 call = reinterpret_cast<CuteXYChartCall48>(taken[48]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[49]) {
      int handled = 0;
      CuteXYChartCall49 call = reinterpret_cast<CuteXYChartCall49>(taken[49]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *XYChart::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7XYChart10metaObjectEv(const XYChart *self) {
  return self->metaObject();
}

//  QString XYChart::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7XYChart2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(XYChart::tr(s, c, n));
}

//  XYChart::~XYChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChartD1Ev(XYChart *self) {
  delete self;
}

//  void XYChart::setGeometryPoints(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart17setGeometryPointsERK5QListI7QPointFE(
    XYChart *self,
    const QList<QPointF> *points) {
  self->setGeometryPoints(*points);
}

//  QList<QPointF> XYChart::geometryPoints() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK7XYChart14geometryPointsEv(const XYChart *self) {
  return new QList<QPointF>(self->geometryPoints());
}

//  void XYChart::setAnimation(XYAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart12setAnimationEP11XYAnimation(
    XYChart *self,
    XYAnimation *animation) {
  self->setAnimation(animation);
}

//  ChartAnimation *XYChart::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZNK7XYChart9animationEv(const XYChart *self) {
  return self->animation();
}

//  void XYChart::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart14updateGeometryEv(XYChart *self) {
  self->updateGeometry();
}

//  bool XYChart::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7XYChart7isDirtyEv(const XYChart *self) {
  return self->isDirty();
}

//  void XYChart::setDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart8setDirtyEb(XYChart *self, bool dirty) {
  self->setDirty(dirty);
}

//  void XYChart::handlePointAdded(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart16handlePointAddedEi(XYChart *self, int index) {
  self->handlePointAdded(index);
}

//  void XYChart::handlePointRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart18handlePointRemovedEi(XYChart *self, int index) {
  self->handlePointRemoved(index);
}

//  void XYChart::handlePointsRemoved(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart19handlePointsRemovedEii(
    XYChart *self,
    int index,
    int count) {
  self->handlePointsRemoved(index, count);
}

//  void XYChart::handlePointReplaced(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart19handlePointReplacedEi(XYChart *self, int index) {
  self->handlePointReplaced(index);
}

//  void XYChart::handlePointsReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart20handlePointsReplacedEv(XYChart *self) {
  self->handlePointsReplaced();
}

//  void XYChart::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart19handleDomainUpdatedEv(XYChart *self) {
  self->handleDomainUpdated();
}

//  void XYChart::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart19handleSeriesUpdatedEv(XYChart *self) {
  self->handleSeriesUpdated();
}

//  void XYChart::updateChart(const QList<QPointF> &oldPoints, const
//      QList<QPointF> &newPoints, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart11updateChartERK5QListI7QPointFES4_i(
    XYChart *self,
    const QList<QPointF> *oldPoints,
    const QList<QPointF> *newPoints,
    int index) {
  self->updateChart(*oldPoints, *newPoints, index);
}

//  void XYChart::updateGlChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart13updateGlChartEv(XYChart *self) {
  self->updateGlChart();
}

//  void XYChart::refreshGlChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7XYChart14refreshGlChartEv(XYChart *self) {
  self->refreshGlChart();
}

//  QPointF XYChart::matchForLightMarker(const QPointF &eventPos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7XYChart19matchForLightMarkerERK7QPointF(
    const XYChart *self,
    const QPointF *eventPos) {
  return new QPointF(self->matchForLightMarker(*eventPos));
}

//  bool XYChart::isEmpty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7XYChart7isEmptyEv(XYChart *self) {
  return self->isEmpty();
}

//  QPointF XYChart::hoverPoint(const QPointF &eventPos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7XYChart10hoverPointERK7QPointF(
    const XYChart *self,
    const QPointF *eventPos) {
  return new QPointF(self->hoverPoint(*eventPos));
}

//  bool XYChart::fuzzyComparePointF(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7XYChart18fuzzyComparePointFERK7QPointFS2_(
    const QPointF *p1,
    const QPointF *p2) {
  return XYChart::fuzzyComparePointF(*p1, *p2);
}

//  a Python function taken by a CuteXYChart, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_XYChart(XYChart *self, const char *key, void *call) {
  return static_cast<CuteXYChart *>(self)->take(key, call);
}

//  ChartAnimation *XYChart::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_own_ZNK7XYChart9animationEv(const XYChart *self) {
  return self->XYChart::animation();
}

//  void XYChart::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7XYChart19handleDomainUpdatedEv(XYChart *self) {
  self->XYChart::handleDomainUpdated();
}

//  void XYChart::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7XYChart19handleSeriesUpdatedEv(XYChart *self) {
  self->XYChart::handleSeriesUpdated();
}

//  void XYChart::updateGlChart()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7XYChart13updateGlChartEv(XYChart *self) {
  static_cast<OwnXYChart *>(self)->OwnXYChart::updateGlChart();
}

//  void XYChart::refreshGlChart()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7XYChart14refreshGlChartEv(XYChart *self) {
  static_cast<OwnXYChart *>(self)->OwnXYChart::refreshGlChart();
}
