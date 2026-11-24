//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/linechartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/linechartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on LineChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnLineChartItem : LineChartItem {
  using LineChartItem::updateGeometry;
  using LineChartItem::mousePressEvent;
  using LineChartItem::hoverEnterEvent;
  using LineChartItem::hoverMoveEvent;
  using LineChartItem::hoverLeaveEvent;
  using LineChartItem::mouseReleaseEvent;
  using LineChartItem::mouseDoubleClickEvent;
};

//  A LineChartItem that Python can take functions over in. Every LineChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteLineChartItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteLineChartItemCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall3)(const void *, int *);
typedef void (*CuteLineChartItemCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall5)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall6)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall7)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall8)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall9)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall10)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void * (*CuteLineChartItemCall11)(const void *, int *);
typedef void (*CuteLineChartItemCall12)(const void *, int *);
typedef void (*CuteLineChartItemCall13)(const void *, int *);
typedef void (*CuteLineChartItemCall14)(const void *, int *);
typedef void (*CuteLineChartItemCall15)(const void *, int *);
typedef void (*CuteLineChartItemCall16)(const void *, ChartPresenter *, int *);
typedef void (*CuteLineChartItemCall17)(const void *, ChartThemeManager *, int *);
typedef void (*CuteLineChartItemCall18)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall19)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLineChartItemCall20)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLineChartItemCall21)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLineChartItemCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLineChartItemCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLineChartItemCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLineChartItemCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall26)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall27)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall28)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall29)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall30)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteLineChartItemCall31)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteLineChartItemCall32)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall33)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLineChartItemCall34)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall35)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall36)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall37)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall38)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall40)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall41)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall42)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall43)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall44)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall45)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLineChartItemCall46)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLineChartItemCall47)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLineChartItemCall48)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLineChartItemCall49)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteLineChartItem : public LineChartItem {
public:
  using LineChartItem::LineChartItem;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7XYChart19handleSeriesUpdatedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7XYChart14updateGeometryEv")) {
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

#if QT_CONFIG(graphicsview)
  //  QRectF LineChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteLineChartItemCall0 call = reinterpret_cast<CuteLineChartItemCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteLineChartItemCall1 call = reinterpret_cast<CuteLineChartItemCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    LineChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath LineChartItem::shape() const
  QPainterPath shape() const override {
    if (taken[2]) {
      int handled = 0;
      CuteLineChartItemCall2 call = reinterpret_cast<CuteLineChartItemCall2>(taken[2]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return LineChartItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void LineChartItem::handleSeriesUpdated()
  void handleSeriesUpdated() override {
    if (taken[3]) {
      int handled = 0;
      CuteLineChartItemCall3 call = reinterpret_cast<CuteLineChartItemCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    LineChartItem::handleSeriesUpdated();
  }

  //  void LineChartItem::updateGeometry()
  void updateGeometry() override {
    if (taken[4]) {
      int handled = 0;
      CuteLineChartItemCall4 call = reinterpret_cast<CuteLineChartItemCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    LineChartItem::updateGeometry();
  }

#if QT_CONFIG(graphicsview)
  //  void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteLineChartItemCall5 call = reinterpret_cast<CuteLineChartItemCall5>(taken[5]);
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
      CuteLineChartItemCall6 call = reinterpret_cast<CuteLineChartItemCall6>(taken[6]);
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
      CuteLineChartItemCall7 call = reinterpret_cast<CuteLineChartItemCall7>(taken[7]);
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
      CuteLineChartItemCall8 call = reinterpret_cast<CuteLineChartItemCall8>(taken[8]);
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
      CuteLineChartItemCall9 call = reinterpret_cast<CuteLineChartItemCall9>(taken[9]);
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
      CuteLineChartItemCall10 call = reinterpret_cast<CuteLineChartItemCall10>(taken[10]);
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
      CuteLineChartItemCall11 call = reinterpret_cast<CuteLineChartItemCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return XYChart::animation();
  }

  //  void XYChart::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[12]) {
      int handled = 0;
      CuteLineChartItemCall12 call = reinterpret_cast<CuteLineChartItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::handleDomainUpdated();
  }

  //  void XYChart::updateGlChart()
  void updateGlChart() override {
    if (taken[13]) {
      int handled = 0;
      CuteLineChartItemCall13 call = reinterpret_cast<CuteLineChartItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::updateGlChart();
  }

  //  void XYChart::refreshGlChart()
  void refreshGlChart() override {
    if (taken[14]) {
      int handled = 0;
      CuteLineChartItemCall14 call = reinterpret_cast<CuteLineChartItemCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    XYChart::refreshGlChart();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[15]) {
      int handled = 0;
      CuteLineChartItemCall15 call = reinterpret_cast<CuteLineChartItemCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[16]) {
      int handled = 0;
      CuteLineChartItemCall16 call = reinterpret_cast<CuteLineChartItemCall16>(taken[16]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[17]) {
      int handled = 0;
      CuteLineChartItemCall17 call = reinterpret_cast<CuteLineChartItemCall17>(taken[17]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[18]) {
      int handled = 0;
      CuteLineChartItemCall18 call = reinterpret_cast<CuteLineChartItemCall18>(taken[18]);
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
      CuteLineChartItemCall19 call = reinterpret_cast<CuteLineChartItemCall19>(taken[19]);
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
      CuteLineChartItemCall20 call = reinterpret_cast<CuteLineChartItemCall20>(taken[20]);
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
      CuteLineChartItemCall21 call = reinterpret_cast<CuteLineChartItemCall21>(taken[21]);
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
      CuteLineChartItemCall22 call = reinterpret_cast<CuteLineChartItemCall22>(taken[22]);
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
      CuteLineChartItemCall23 call = reinterpret_cast<CuteLineChartItemCall23>(taken[23]);
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
      CuteLineChartItemCall24 call = reinterpret_cast<CuteLineChartItemCall24>(taken[24]);
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
      CuteLineChartItemCall25 call = reinterpret_cast<CuteLineChartItemCall25>(taken[25]);
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
      CuteLineChartItemCall26 call = reinterpret_cast<CuteLineChartItemCall26>(taken[26]);
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
      CuteLineChartItemCall27 call = reinterpret_cast<CuteLineChartItemCall27>(taken[27]);
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
      CuteLineChartItemCall28 call = reinterpret_cast<CuteLineChartItemCall28>(taken[28]);
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
      CuteLineChartItemCall29 call = reinterpret_cast<CuteLineChartItemCall29>(taken[29]);
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
      CuteLineChartItemCall30 call = reinterpret_cast<CuteLineChartItemCall30>(taken[30]);
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
      CuteLineChartItemCall31 call = reinterpret_cast<CuteLineChartItemCall31>(taken[31]);
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
      CuteLineChartItemCall32 call = reinterpret_cast<CuteLineChartItemCall32>(taken[32]);
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
      CuteLineChartItemCall33 call = reinterpret_cast<CuteLineChartItemCall33>(taken[33]);
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
      CuteLineChartItemCall34 call = reinterpret_cast<CuteLineChartItemCall34>(taken[34]);
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
      CuteLineChartItemCall35 call = reinterpret_cast<CuteLineChartItemCall35>(taken[35]);
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
      CuteLineChartItemCall36 call = reinterpret_cast<CuteLineChartItemCall36>(taken[36]);
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
      CuteLineChartItemCall37 call = reinterpret_cast<CuteLineChartItemCall37>(taken[37]);
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
      CuteLineChartItemCall38 call = reinterpret_cast<CuteLineChartItemCall38>(taken[38]);
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
      CuteLineChartItemCall39 call = reinterpret_cast<CuteLineChartItemCall39>(taken[39]);
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
      CuteLineChartItemCall40 call = reinterpret_cast<CuteLineChartItemCall40>(taken[40]);
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
      CuteLineChartItemCall41 call = reinterpret_cast<CuteLineChartItemCall41>(taken[41]);
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
      CuteLineChartItemCall42 call = reinterpret_cast<CuteLineChartItemCall42>(taken[42]);
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
      CuteLineChartItemCall43 call = reinterpret_cast<CuteLineChartItemCall43>(taken[43]);
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
      CuteLineChartItemCall44 call = reinterpret_cast<CuteLineChartItemCall44>(taken[44]);
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
      CuteLineChartItemCall45 call = reinterpret_cast<CuteLineChartItemCall45>(taken[45]);
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
      CuteLineChartItemCall46 call = reinterpret_cast<CuteLineChartItemCall46>(taken[46]);
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
      CuteLineChartItemCall47 call = reinterpret_cast<CuteLineChartItemCall47>(taken[47]);
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
      CuteLineChartItemCall48 call = reinterpret_cast<CuteLineChartItemCall48>(taken[48]);
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
      CuteLineChartItemCall49 call = reinterpret_cast<CuteLineChartItemCall49>(taken[49]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *LineChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13LineChartItem10metaObjectEv(
    const LineChartItem *self) {
  return self->metaObject();
}

//  QString LineChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13LineChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LineChartItem::tr(s, c, n));
}

//  LineChartItem::LineChartItem(QLineSeries *series, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
LineChartItem *ritual_ZN13LineChartItemC1EP11QLineSeriesP13QGraphicsItem(
    QLineSeries *series,
    QGraphicsItem *item) {
  return new CuteLineChartItem(series, item);
}

//  LineChartItem::~LineChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItemD1Ev(LineChartItem *self) {
  delete self;
}

//  QRectF LineChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13LineChartItem12boundingRectEv(
    const LineChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void LineChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LineChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QPainterPath LineChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13LineChartItem5shapeEv(const LineChartItem *self) {
  return new QPainterPath(self->shape());
}

//  QPainterPath LineChartItem::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13LineChartItem4pathEv(const LineChartItem *self) {
  return new QPainterPath(self->path());
}

//  void LineChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem19handleSeriesUpdatedEv(LineChartItem *self) {
  self->handleSeriesUpdated();
}

//  void LineChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem14updateGeometryEv(LineChartItem *self) {
  self->updateGeometry();
}

//  void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void LineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void LineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void LineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void LineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void LineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void LineChartItem::suppressPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem14suppressPointsEv(LineChartItem *self) {
  self->suppressPoints();
}

//  void LineChartItem::forceChartType(QChart::ChartType chartType)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineChartItem14forceChartTypeEN6QChart9ChartTypeE(
    LineChartItem *self,
    QChart::ChartType chartType) {
  self->forceChartType(chartType);
}

//  a Python function taken by a CuteLineChartItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LineChartItem(
    LineChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteLineChartItem *>(self)->take(key, call);
}

//  QRectF LineChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK13LineChartItem12boundingRectEv(
    const LineChartItem *self) {
  return new QRectF(self->LineChartItem::boundingRect());
}

//  void LineChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LineChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->LineChartItem::paint(painter, option, widget);
}

//  QPainterPath LineChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK13LineChartItem5shapeEv(
    const LineChartItem *self) {
  return new QPainterPath(self->LineChartItem::shape());
}

//  void LineChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem19handleSeriesUpdatedEv(
    LineChartItem *self) {
  self->LineChartItem::handleSeriesUpdated();
}

//  void LineChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem14updateGeometryEv(LineChartItem *self) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::updateGeometry();
}

//  void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::mousePressEvent(
      event);
}

//  void LineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::hoverEnterEvent(
      event);
}

//  void LineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::hoverMoveEvent(
      event);
}

//  void LineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::hoverLeaveEvent(
      event);
}

//  void LineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::mouseReleaseEvent(
      event);
}

//  void LineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    LineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnLineChartItem *>(self)->OwnLineChartItem::mouseDoubleClickEvent(
      event);
}
