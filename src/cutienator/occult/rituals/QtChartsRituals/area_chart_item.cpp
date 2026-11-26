//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/areachartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/areachartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on AreaChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAreaChartItem : AreaChartItem {
  using AreaChartItem::mousePressEvent;
  using AreaChartItem::hoverEnterEvent;
  using AreaChartItem::hoverLeaveEvent;
  using AreaChartItem::mouseReleaseEvent;
  using AreaChartItem::mouseDoubleClickEvent;
};

//  A AreaChartItem that Python can take functions over in. Every AreaChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteAreaChartItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAreaChartItemCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall3)(const void *, ChartPresenter *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall4)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall5)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall6)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall7)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall8)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall9)(const void *, int *);
typedef void (*CuteAreaChartItemCall10)(const void *, int *);
typedef void * (*CuteAreaChartItemCall11)(const void *, int *);
typedef void (*CuteAreaChartItemCall12)(const void *, ChartThemeManager *, int *);
typedef void (*CuteAreaChartItemCall13)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall14)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAreaChartItemCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaChartItemCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaChartItemCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaChartItemCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaChartItemCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaChartItemCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall21)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall22)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall23)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall24)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall25)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAreaChartItemCall26)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteAreaChartItemCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall28)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAreaChartItemCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall30)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall31)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall32)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall33)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall34)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall35)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall36)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall37)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall38)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall39)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall40)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAreaChartItemCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaChartItemCall43)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaChartItemCall44)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAreaChartItemCall45)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteAreaChartItem : public AreaChartItem {
public:
  using AreaChartItem::AreaChartItem;
  void *taken[46] = {};

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
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem7cleanupEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
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
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  QRectF AreaChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteAreaChartItemCall0 call = reinterpret_cast<CuteAreaChartItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return AreaChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteAreaChartItemCall1 call = reinterpret_cast<CuteAreaChartItemCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    AreaChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath AreaChartItem::shape() const
  QPainterPath shape() const override {
    if (taken[2]) {
      int handled = 0;
      CuteAreaChartItemCall2 call = reinterpret_cast<CuteAreaChartItemCall2>(taken[2]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return AreaChartItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void AreaChartItem::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[3]) {
      int handled = 0;
      CuteAreaChartItemCall3 call = reinterpret_cast<CuteAreaChartItemCall3>(taken[3]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    AreaChartItem::setPresenter(presenter);
  }

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteAreaChartItemCall4 call = reinterpret_cast<CuteAreaChartItemCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    AreaChartItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteAreaChartItemCall5 call = reinterpret_cast<CuteAreaChartItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    AreaChartItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteAreaChartItemCall6 call = reinterpret_cast<CuteAreaChartItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    AreaChartItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteAreaChartItemCall7 call = reinterpret_cast<CuteAreaChartItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    AreaChartItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AreaChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteAreaChartItemCall8 call = reinterpret_cast<CuteAreaChartItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    AreaChartItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void AreaChartItem::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[9]) {
      int handled = 0;
      CuteAreaChartItemCall9 call = reinterpret_cast<CuteAreaChartItemCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    AreaChartItem::handleDomainUpdated();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[10]) {
      int handled = 0;
      CuteAreaChartItemCall10 call = reinterpret_cast<CuteAreaChartItemCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  ChartAnimation *ChartElement::animation() const
  ChartAnimation *animation() const override {
    if (taken[11]) {
      int handled = 0;
      CuteAreaChartItemCall11 call = reinterpret_cast<CuteAreaChartItemCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return ChartElement::animation();
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[12]) {
      int handled = 0;
      CuteAreaChartItemCall12 call = reinterpret_cast<CuteAreaChartItemCall12>(taken[12]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[13]) {
      int handled = 0;
      CuteAreaChartItemCall13 call = reinterpret_cast<CuteAreaChartItemCall13>(taken[13]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[14]) {
      int handled = 0;
      CuteAreaChartItemCall14 call = reinterpret_cast<CuteAreaChartItemCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteAreaChartItemCall15 call = reinterpret_cast<CuteAreaChartItemCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteAreaChartItemCall16 call = reinterpret_cast<CuteAreaChartItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAreaChartItemCall17 call = reinterpret_cast<CuteAreaChartItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAreaChartItemCall18 call = reinterpret_cast<CuteAreaChartItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteAreaChartItemCall19 call = reinterpret_cast<CuteAreaChartItemCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteAreaChartItemCall20 call = reinterpret_cast<CuteAreaChartItemCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[21]) {
      int handled = 0;
      CuteAreaChartItemCall21 call = reinterpret_cast<CuteAreaChartItemCall21>(taken[21]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CuteAreaChartItemCall22 call = reinterpret_cast<CuteAreaChartItemCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteAreaChartItemCall23 call = reinterpret_cast<CuteAreaChartItemCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteAreaChartItemCall24 call = reinterpret_cast<CuteAreaChartItemCall24>(taken[24]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[25]) {
      int handled = 0;
      CuteAreaChartItemCall25 call = reinterpret_cast<CuteAreaChartItemCall25>(taken[25]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[26]) {
      int handled = 0;
      CuteAreaChartItemCall26 call = reinterpret_cast<CuteAreaChartItemCall26>(taken[26]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[27]) {
      int handled = 0;
      CuteAreaChartItemCall27 call = reinterpret_cast<CuteAreaChartItemCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteAreaChartItemCall28 call = reinterpret_cast<CuteAreaChartItemCall28>(taken[28]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteAreaChartItemCall29 call = reinterpret_cast<CuteAreaChartItemCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteAreaChartItemCall30 call = reinterpret_cast<CuteAreaChartItemCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteAreaChartItemCall31 call = reinterpret_cast<CuteAreaChartItemCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteAreaChartItemCall32 call = reinterpret_cast<CuteAreaChartItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteAreaChartItemCall33 call = reinterpret_cast<CuteAreaChartItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteAreaChartItemCall34 call = reinterpret_cast<CuteAreaChartItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteAreaChartItemCall35 call = reinterpret_cast<CuteAreaChartItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteAreaChartItemCall36 call = reinterpret_cast<CuteAreaChartItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteAreaChartItemCall37 call = reinterpret_cast<CuteAreaChartItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAreaChartItemCall38 call = reinterpret_cast<CuteAreaChartItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteAreaChartItemCall39 call = reinterpret_cast<CuteAreaChartItemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteAreaChartItemCall40 call = reinterpret_cast<CuteAreaChartItemCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteAreaChartItemCall41 call = reinterpret_cast<CuteAreaChartItemCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteAreaChartItemCall42 call = reinterpret_cast<CuteAreaChartItemCall42>(taken[42]);
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
    if (taken[43]) {
      int handled = 0;
      CuteAreaChartItemCall43 call = reinterpret_cast<CuteAreaChartItemCall43>(taken[43]);
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
    if (taken[44]) {
      int handled = 0;
      CuteAreaChartItemCall44 call = reinterpret_cast<CuteAreaChartItemCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[45]) {
      int handled = 0;
      CuteAreaChartItemCall45 call = reinterpret_cast<CuteAreaChartItemCall45>(taken[45]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *AreaChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13AreaChartItem10metaObjectEv(
    const AreaChartItem *self) {
  return self->metaObject();
}

//  void *AreaChartItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13AreaChartItem11qt_metacastEPKc(
    AreaChartItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AreaChartItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13AreaChartItem11qt_metacallEN11QMetaObject4CallEiPPv(
    AreaChartItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AreaChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13AreaChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AreaChartItem::tr(s, c, n));
}

//  AreaChartItem::AreaChartItem(QAreaSeries *areaSeries, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
AreaChartItem *ritual_ZN13AreaChartItemC1EP11QAreaSeriesP13QGraphicsItem(
    QAreaSeries *areaSeries,
    QGraphicsItem *item) {
  return new CuteAreaChartItem(areaSeries, item);
}

//  AreaChartItem::~AreaChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItemD1Ev(AreaChartItem *self) {
  delete self;
}

//  QRectF AreaChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13AreaChartItem12boundingRectEv(
    const AreaChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void AreaChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    AreaChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QPainterPath AreaChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13AreaChartItem5shapeEv(const AreaChartItem *self) {
  return new QPainterPath(self->shape());
}

//  LineChartItem *AreaChartItem::upperLineItem() const
extern "C" Q_DECL_EXPORT
LineChartItem *ritual_ZNK13AreaChartItem13upperLineItemEv(
    const AreaChartItem *self) {
  return self->upperLineItem();
}

//  LineChartItem *AreaChartItem::lowerLineItem() const
extern "C" Q_DECL_EXPORT
LineChartItem *ritual_ZNK13AreaChartItem13lowerLineItemEv(
    const AreaChartItem *self) {
  return self->lowerLineItem();
}

//  void AreaChartItem::updatePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem10updatePathEv(AreaChartItem *self) {
  self->updatePath();
}

//  void AreaChartItem::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem12setPresenterEP14ChartPresenter(
    AreaChartItem *self,
    ChartPresenter *presenter) {
  self->setPresenter(presenter);
}

//  QAreaSeries *AreaChartItem::series() const
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZNK13AreaChartItem6seriesEv(const AreaChartItem *self) {
  return self->series();
}

//  void AreaChartItem::setUpperSeries(QLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem14setUpperSeriesEP11QLineSeries(
    AreaChartItem *self,
    QLineSeries *series) {
  self->setUpperSeries(series);
}

//  void AreaChartItem::setLowerSeries(QLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem14setLowerSeriesEP11QLineSeries(
    AreaChartItem *self,
    QLineSeries *series) {
  self->setLowerSeries(series);
}

//  void AreaChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void AreaChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    AreaChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void AreaChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    AreaChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void AreaChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void AreaChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void AreaChartItem::clicked(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem7clickedERK7QPointF(
    AreaChartItem *self,
    const QPointF *point) {
  self->clicked(*point);
}

//  void AreaChartItem::hovered(const QPointF &point, bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem7hoveredERK7QPointFb(
    AreaChartItem *self,
    const QPointF *point,
    bool state) {
  self->hovered(*point, state);
}

//  void AreaChartItem::pressed(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem7pressedERK7QPointF(
    AreaChartItem *self,
    const QPointF *point) {
  self->pressed(*point);
}

//  void AreaChartItem::released(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem8releasedERK7QPointF(
    AreaChartItem *self,
    const QPointF *point) {
  self->released(*point);
}

//  void AreaChartItem::doubleClicked(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem13doubleClickedERK7QPointF(
    AreaChartItem *self,
    const QPointF *point) {
  self->doubleClicked(*point);
}

//  void AreaChartItem::handleUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem13handleUpdatedEv(AreaChartItem *self) {
  self->handleUpdated();
}

//  void AreaChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem19handleDomainUpdatedEv(AreaChartItem *self) {
  self->handleDomainUpdated();
}

//  void AreaChartItem::fixEdgeSeriesDomain(LineChartItem *edgeSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AreaChartItem19fixEdgeSeriesDomainEP13LineChartItem(
    AreaChartItem *self,
    LineChartItem *edgeSeries) {
  self->fixEdgeSeriesDomain(edgeSeries);
}

//  a Python function taken by a CuteAreaChartItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AreaChartItem(
    AreaChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteAreaChartItem *>(self)->take(key, call);
}

//  QRectF AreaChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK13AreaChartItem12boundingRectEv(
    const AreaChartItem *self) {
  return new QRectF(self->AreaChartItem::boundingRect());
}

//  void AreaChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    AreaChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->AreaChartItem::paint(painter, option, widget);
}

//  QPainterPath AreaChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK13AreaChartItem5shapeEv(
    const AreaChartItem *self) {
  return new QPainterPath(self->AreaChartItem::shape());
}

//  void AreaChartItem::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem12setPresenterEP14ChartPresenter(
    AreaChartItem *self,
    ChartPresenter *presenter) {
  self->AreaChartItem::setPresenter(presenter);
}

//  void AreaChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnAreaChartItem *>(self)->OwnAreaChartItem::mousePressEvent(
      event);
}

//  void AreaChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    AreaChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnAreaChartItem *>(self)->OwnAreaChartItem::hoverEnterEvent(
      event);
}

//  void AreaChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    AreaChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnAreaChartItem *>(self)->OwnAreaChartItem::hoverLeaveEvent(
      event);
}

//  void AreaChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnAreaChartItem *>(self)->OwnAreaChartItem::mouseReleaseEvent(
      event);
}

//  void AreaChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    AreaChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnAreaChartItem *>(self)->OwnAreaChartItem::mouseDoubleClickEvent(
      event);
}

//  void AreaChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AreaChartItem19handleDomainUpdatedEv(
    AreaChartItem *self) {
  self->AreaChartItem::handleDomainUpdated();
}

#endif  // QT_CONFIG(charts_area_chart)
