//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/areachartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/areachartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A AreaBoundItem that Python can take functions over in. Every AreaBoundItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAreaBoundItemCall0)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteAreaBoundItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAreaBoundItemCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall5)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall6)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall7)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall8)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall9)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall10)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void * (*CuteAreaBoundItemCall11)(const void *, int *);
typedef void (*CuteAreaBoundItemCall12)(const void *, int *);
typedef void (*CuteAreaBoundItemCall13)(const void *, int *);
typedef void (*CuteAreaBoundItemCall14)(const void *, int *);
typedef void (*CuteAreaBoundItemCall15)(const void *, int *);
typedef void (*CuteAreaBoundItemCall16)(const void *, ChartPresenter *, int *);
typedef void (*CuteAreaBoundItemCall17)(const void *, ChartThemeManager *, int *);
typedef void (*CuteAreaBoundItemCall18)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall19)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAreaBoundItemCall20)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaBoundItemCall21)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaBoundItemCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaBoundItemCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaBoundItemCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaBoundItemCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall26)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall27)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall28)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall29)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall30)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAreaBoundItemCall31)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteAreaBoundItemCall32)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall33)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaBoundItemCall34)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall35)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall36)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall37)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall38)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall40)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall41)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall42)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall43)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall44)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall45)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaBoundItemCall46)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaBoundItemCall47)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaBoundItemCall48)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaBoundItemCall49)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteAreaBoundItem : public AreaBoundItem {
public:
  using AreaBoundItem::AreaBoundItem;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7XYChart14updateGeometryEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7XYChart19handleSeriesUpdatedEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart13updateGlChartEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart14refreshGlChartEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem7cleanupEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
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

  //  void AreaBoundItem::updateGeometry()
  void updateGeometry() override {
    if (taken[0]) {
      int handled = 0;
      CuteAreaBoundItemCall0 call = reinterpret_cast<CuteAreaBoundItemCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AreaBoundItem::updateGeometry();
  }

#if QT_CONFIG(graphicsview)
  //  QRectF LineChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAreaBoundItemCall1 call = reinterpret_cast<CuteAreaBoundItemCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return LineChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      CuteAreaBoundItemCall2 call = reinterpret_cast<CuteAreaBoundItemCall2>(taken[2]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    LineChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath LineChartItem::shape() const
  QPainterPath shape() const override {
    if (taken[3]) {
      int handled = 0;
      CuteAreaBoundItemCall3 call = reinterpret_cast<CuteAreaBoundItemCall3>(taken[3]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return LineChartItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void LineChartItem::handleSeriesUpdated()
  void handleSeriesUpdated() override {
    if (taken[4]) {
      int handled = 0;
      CuteAreaBoundItemCall4 call = reinterpret_cast<CuteAreaBoundItemCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    LineChartItem::handleSeriesUpdated();
  }

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteAreaBoundItemCall5 call = reinterpret_cast<CuteAreaBoundItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteAreaBoundItemCall6 call = reinterpret_cast<CuteAreaBoundItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteAreaBoundItemCall7 call = reinterpret_cast<CuteAreaBoundItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteAreaBoundItemCall8 call = reinterpret_cast<CuteAreaBoundItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteAreaBoundItemCall9 call = reinterpret_cast<CuteAreaBoundItemCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteAreaBoundItemCall10 call = reinterpret_cast<CuteAreaBoundItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    LineChartItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

  //  ChartAnimation *XYChart::animation() const
  ChartAnimation *animation() const override {
    if (taken[11]) {
      int handled = 0;
      CuteAreaBoundItemCall11 call = reinterpret_cast<CuteAreaBoundItemCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return XYChart::animation();
  }

  //  void XYChart::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[12]) {
      int handled = 0;
      CuteAreaBoundItemCall12 call = reinterpret_cast<CuteAreaBoundItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::handleDomainUpdated();
  }

  //  void XYChart::updateGlChart()
  void updateGlChart() override {
    if (taken[13]) {
      int handled = 0;
      CuteAreaBoundItemCall13 call = reinterpret_cast<CuteAreaBoundItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::updateGlChart();
  }

  //  void XYChart::refreshGlChart()
  void refreshGlChart() override {
    if (taken[14]) {
      int handled = 0;
      CuteAreaBoundItemCall14 call = reinterpret_cast<CuteAreaBoundItemCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::refreshGlChart();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[15]) {
      int handled = 0;
      CuteAreaBoundItemCall15 call = reinterpret_cast<CuteAreaBoundItemCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[16]) {
      int handled = 0;
      CuteAreaBoundItemCall16 call = reinterpret_cast<CuteAreaBoundItemCall16>(taken[16]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[17]) {
      int handled = 0;
      CuteAreaBoundItemCall17 call = reinterpret_cast<CuteAreaBoundItemCall17>(taken[17]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[18]) {
      int handled = 0;
      CuteAreaBoundItemCall18 call = reinterpret_cast<CuteAreaBoundItemCall18>(taken[18]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[19]) {
      int handled = 0;
      CuteAreaBoundItemCall19 call = reinterpret_cast<CuteAreaBoundItemCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteAreaBoundItemCall20 call = reinterpret_cast<CuteAreaBoundItemCall20>(taken[20]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteAreaBoundItemCall21 call = reinterpret_cast<CuteAreaBoundItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteAreaBoundItemCall22 call = reinterpret_cast<CuteAreaBoundItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteAreaBoundItemCall23 call = reinterpret_cast<CuteAreaBoundItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteAreaBoundItemCall24 call = reinterpret_cast<CuteAreaBoundItemCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteAreaBoundItemCall25 call = reinterpret_cast<CuteAreaBoundItemCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[26]) {
      int handled = 0;
      CuteAreaBoundItemCall26 call = reinterpret_cast<CuteAreaBoundItemCall26>(taken[26]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[27]) {
      int handled = 0;
      CuteAreaBoundItemCall27 call = reinterpret_cast<CuteAreaBoundItemCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteAreaBoundItemCall28 call = reinterpret_cast<CuteAreaBoundItemCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteAreaBoundItemCall29 call = reinterpret_cast<CuteAreaBoundItemCall29>(taken[29]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[30]) {
      int handled = 0;
      CuteAreaBoundItemCall30 call = reinterpret_cast<CuteAreaBoundItemCall30>(taken[30]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[31]) {
      int handled = 0;
      CuteAreaBoundItemCall31 call = reinterpret_cast<CuteAreaBoundItemCall31>(taken[31]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[32]) {
      int handled = 0;
      CuteAreaBoundItemCall32 call = reinterpret_cast<CuteAreaBoundItemCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteAreaBoundItemCall33 call = reinterpret_cast<CuteAreaBoundItemCall33>(taken[33]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteAreaBoundItemCall34 call = reinterpret_cast<CuteAreaBoundItemCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteAreaBoundItemCall35 call = reinterpret_cast<CuteAreaBoundItemCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteAreaBoundItemCall36 call = reinterpret_cast<CuteAreaBoundItemCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteAreaBoundItemCall37 call = reinterpret_cast<CuteAreaBoundItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAreaBoundItemCall38 call = reinterpret_cast<CuteAreaBoundItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteAreaBoundItemCall39 call = reinterpret_cast<CuteAreaBoundItemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteAreaBoundItemCall40 call = reinterpret_cast<CuteAreaBoundItemCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteAreaBoundItemCall41 call = reinterpret_cast<CuteAreaBoundItemCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteAreaBoundItemCall42 call = reinterpret_cast<CuteAreaBoundItemCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteAreaBoundItemCall43 call = reinterpret_cast<CuteAreaBoundItemCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteAreaBoundItemCall44 call = reinterpret_cast<CuteAreaBoundItemCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteAreaBoundItemCall45 call = reinterpret_cast<CuteAreaBoundItemCall45>(taken[45]);
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
      CuteAreaBoundItemCall46 call = reinterpret_cast<CuteAreaBoundItemCall46>(taken[46]);
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
      CuteAreaBoundItemCall47 call = reinterpret_cast<CuteAreaBoundItemCall47>(taken[47]);
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
      CuteAreaBoundItemCall48 call = reinterpret_cast<CuteAreaBoundItemCall48>(taken[48]);
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
      CuteAreaBoundItemCall49 call = reinterpret_cast<CuteAreaBoundItemCall49>(taken[49]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  AreaBoundItem::AreaBoundItem(AreaChartItem *area, QLineSeries
//      *lineSeries, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
AreaBoundItem *ritual_ZN13AreaBoundItemC1EP13AreaChartItemP11QLineSeriesP13QGraphicsItem(
    AreaChartItem *area,
    QLineSeries *lineSeries,
    QGraphicsItem *item) {
  return new CuteAreaBoundItem(area, lineSeries, item);
}

//  AreaBoundItem::~AreaBoundItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaBoundItemD1Ev(AreaBoundItem *self) {
  delete self;
}

//  void AreaBoundItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaBoundItem14updateGeometryEv(AreaBoundItem *self) {
  self->updateGeometry();
}

//  a Python function taken by a CuteAreaBoundItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AreaBoundItem(
    AreaBoundItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteAreaBoundItem *>(self)->take(key, call);
}

//  void AreaBoundItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaBoundItem14updateGeometryEv(AreaBoundItem *self) {
  self->AreaBoundItem::updateGeometry();
}
