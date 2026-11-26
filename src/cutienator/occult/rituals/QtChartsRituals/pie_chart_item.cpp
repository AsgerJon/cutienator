//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/piechartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/piechartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/qpieslice.h>
#endif
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/pieslicedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on PieChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnPieChartItem : PieChartItem {
  using PieChartItem::hoverEnterEvent;
  using PieChartItem::hoverLeaveEvent;
  using PieChartItem::mousePressEvent;
  using PieChartItem::mouseReleaseEvent;
  using PieChartItem::mouseDoubleClickEvent;
};

//  A PieChartItem that Python can take functions over in. Every PieChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CutePieChartItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void * (*CutePieChartItemCall2)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall3)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall4)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall5)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall6)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall7)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall8)(const void *, int *);
typedef void (*CutePieChartItemCall9)(const void *, int *);
typedef void (*CutePieChartItemCall10)(const void *, ChartPresenter *, int *);
typedef void (*CutePieChartItemCall11)(const void *, ChartThemeManager *, int *);
typedef void (*CutePieChartItemCall12)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePieChartItemCall14)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieChartItemCall15)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieChartItemCall16)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieChartItemCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieChartItemCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieChartItemCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall20)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePieChartItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall22)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall23)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall24)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall25)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePieChartItemCall26)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CutePieChartItemCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall28)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieChartItemCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall30)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall31)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall32)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall33)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall34)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall35)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall36)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall37)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall38)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall39)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall40)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieChartItemCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieChartItemCall43)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieChartItemCall44)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieChartItemCall45)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CutePieChartItem : public PieChartItem {
public:
  using PieChartItem::PieChartItem;
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
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem7cleanupEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
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
  //  QRectF PieChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CutePieChartItemCall0 call = reinterpret_cast<CutePieChartItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return PieChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::paint(QPainter *a0, const QStyleOptionGraphicsItem
  //      *a1, QWidget *a2)
  void paint(
      QPainter *a0,
      const QStyleOptionGraphicsItem *a1,
      QWidget *a2) override {
    if (taken[1]) {
      int handled = 0;
      CutePieChartItemCall1 call = reinterpret_cast<CutePieChartItemCall1>(taken[1]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    PieChartItem::paint(a0, a1, a2);
  }
#endif  // QT_CONFIG(graphicsview)

  //  ChartAnimation *PieChartItem::animation() const
  ChartAnimation *animation() const override {
    if (taken[2]) {
      int handled = 0;
      CutePieChartItemCall2 call = reinterpret_cast<CutePieChartItemCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return PieChartItem::animation();
  }

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CutePieChartItemCall3 call = reinterpret_cast<CutePieChartItemCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieChartItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CutePieChartItemCall4 call = reinterpret_cast<CutePieChartItemCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieChartItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CutePieChartItemCall5 call = reinterpret_cast<CutePieChartItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieChartItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CutePieChartItemCall6 call = reinterpret_cast<CutePieChartItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieChartItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CutePieChartItemCall7 call = reinterpret_cast<CutePieChartItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieChartItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void PieChartItem::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[8]) {
      int handled = 0;
      CutePieChartItemCall8 call = reinterpret_cast<CutePieChartItemCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    PieChartItem::handleDomainUpdated();
  }

  //  void PieChartItem::cleanup()
  void cleanup() override {
    if (taken[9]) {
      int handled = 0;
      CutePieChartItemCall9 call = reinterpret_cast<CutePieChartItemCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    PieChartItem::cleanup();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[10]) {
      int handled = 0;
      CutePieChartItemCall10 call = reinterpret_cast<CutePieChartItemCall10>(taken[10]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[11]) {
      int handled = 0;
      CutePieChartItemCall11 call = reinterpret_cast<CutePieChartItemCall11>(taken[11]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[12]) {
      int handled = 0;
      CutePieChartItemCall12 call = reinterpret_cast<CutePieChartItemCall12>(taken[12]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[13]) {
      int handled = 0;
      CutePieChartItemCall13 call = reinterpret_cast<CutePieChartItemCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CutePieChartItemCall14 call = reinterpret_cast<CutePieChartItemCall14>(taken[14]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CutePieChartItemCall15 call = reinterpret_cast<CutePieChartItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CutePieChartItemCall16 call = reinterpret_cast<CutePieChartItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CutePieChartItemCall17 call = reinterpret_cast<CutePieChartItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CutePieChartItemCall18 call = reinterpret_cast<CutePieChartItemCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CutePieChartItemCall19 call = reinterpret_cast<CutePieChartItemCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[20]) {
      int handled = 0;
      CutePieChartItemCall20 call = reinterpret_cast<CutePieChartItemCall20>(taken[20]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[21]) {
      int handled = 0;
      CutePieChartItemCall21 call = reinterpret_cast<CutePieChartItemCall21>(taken[21]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CutePieChartItemCall22 call = reinterpret_cast<CutePieChartItemCall22>(taken[22]);
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
      CutePieChartItemCall23 call = reinterpret_cast<CutePieChartItemCall23>(taken[23]);
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
      CutePieChartItemCall24 call = reinterpret_cast<CutePieChartItemCall24>(taken[24]);
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
      CutePieChartItemCall25 call = reinterpret_cast<CutePieChartItemCall25>(taken[25]);
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
      CutePieChartItemCall26 call = reinterpret_cast<CutePieChartItemCall26>(taken[26]);
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
      CutePieChartItemCall27 call = reinterpret_cast<CutePieChartItemCall27>(taken[27]);
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
      CutePieChartItemCall28 call = reinterpret_cast<CutePieChartItemCall28>(taken[28]);
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
      CutePieChartItemCall29 call = reinterpret_cast<CutePieChartItemCall29>(taken[29]);
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
      CutePieChartItemCall30 call = reinterpret_cast<CutePieChartItemCall30>(taken[30]);
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
      CutePieChartItemCall31 call = reinterpret_cast<CutePieChartItemCall31>(taken[31]);
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
      CutePieChartItemCall32 call = reinterpret_cast<CutePieChartItemCall32>(taken[32]);
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
      CutePieChartItemCall33 call = reinterpret_cast<CutePieChartItemCall33>(taken[33]);
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
      CutePieChartItemCall34 call = reinterpret_cast<CutePieChartItemCall34>(taken[34]);
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
      CutePieChartItemCall35 call = reinterpret_cast<CutePieChartItemCall35>(taken[35]);
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
      CutePieChartItemCall36 call = reinterpret_cast<CutePieChartItemCall36>(taken[36]);
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
      CutePieChartItemCall37 call = reinterpret_cast<CutePieChartItemCall37>(taken[37]);
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
      CutePieChartItemCall38 call = reinterpret_cast<CutePieChartItemCall38>(taken[38]);
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
      CutePieChartItemCall39 call = reinterpret_cast<CutePieChartItemCall39>(taken[39]);
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
      CutePieChartItemCall40 call = reinterpret_cast<CutePieChartItemCall40>(taken[40]);
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
      CutePieChartItemCall41 call = reinterpret_cast<CutePieChartItemCall41>(taken[41]);
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
      CutePieChartItemCall42 call = reinterpret_cast<CutePieChartItemCall42>(taken[42]);
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
      CutePieChartItemCall43 call = reinterpret_cast<CutePieChartItemCall43>(taken[43]);
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
      CutePieChartItemCall44 call = reinterpret_cast<CutePieChartItemCall44>(taken[44]);
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
      CutePieChartItemCall45 call = reinterpret_cast<CutePieChartItemCall45>(taken[45]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *PieChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12PieChartItem10metaObjectEv(
    const PieChartItem *self) {
  return self->metaObject();
}

//  void *PieChartItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12PieChartItem11qt_metacastEPKc(
    PieChartItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int PieChartItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12PieChartItem11qt_metacallEN11QMetaObject4CallEiPPv(
    PieChartItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString PieChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12PieChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PieChartItem::tr(s, c, n));
}

//  PieChartItem::PieChartItem(QPieSeries *series, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
PieChartItem *ritual_ZN12PieChartItemC1EP10QPieSeriesP13QGraphicsItem(
    QPieSeries *series,
    QGraphicsItem *item) {
  return new CutePieChartItem(series, item);
}

//  PieChartItem::~PieChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItemD1Ev(PieChartItem *self) {
  delete self;
}

//  QRectF PieChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12PieChartItem12boundingRectEv(const PieChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void PieChartItem::paint(QPainter *a0, const QStyleOptionGraphicsItem
//      *a1, QWidget *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    PieChartItem *self,
    QPainter *a0,
    const QStyleOptionGraphicsItem *a1,
    QWidget *a2) {
  self->paint(a0, a1, a2);
}

//  ChartAnimation *PieChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZNK12PieChartItem9animationEv(
    const PieChartItem *self) {
  return self->animation();
}

//  void PieChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    PieChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void PieChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    PieChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void PieChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void PieChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void PieChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void PieChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem19handleDomainUpdatedEv(PieChartItem *self) {
  self->handleDomainUpdated();
}

//  void PieChartItem::updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem12updateLayoutEv(PieChartItem *self) {
  self->updateLayout();
}

//  void PieChartItem::handleSlicesAdded(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem17handleSlicesAddedERK5QListIP9QPieSliceE(
    PieChartItem *self,
    const QList<QPieSlice *> *slices) {
  self->handleSlicesAdded(*slices);
}

//  void PieChartItem::handleSlicesRemoved(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem19handleSlicesRemovedERK5QListIP9QPieSliceE(
    PieChartItem *self,
    const QList<QPieSlice *> *slices) {
  self->handleSlicesRemoved(*slices);
}

//  void PieChartItem::handleSliceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem18handleSliceChangedEv(PieChartItem *self) {
  self->handleSliceChanged();
}

//  void PieChartItem::handleSeriesVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem26handleSeriesVisibleChangedEv(
    PieChartItem *self) {
  self->handleSeriesVisibleChanged();
}

//  void PieChartItem::handleOpacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem20handleOpacityChangedEv(PieChartItem *self) {
  self->handleOpacityChanged();
}

//  void PieChartItem::setAnimation(PieAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem12setAnimationEP12PieAnimation(
    PieChartItem *self,
    PieAnimation *animation) {
  self->setAnimation(animation);
}

//  void PieChartItem::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieChartItem7cleanupEv(PieChartItem *self) {
  self->cleanup();
}

//  PieSliceData PieChartItem::updateSliceGeometry(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
PieSliceData *ritual_ZN12PieChartItem19updateSliceGeometryEP9QPieSlice(
    PieChartItem *self,
    QPieSlice *slice) {
  return new PieSliceData(self->updateSliceGeometry(slice));
}

//  a Python function taken by a CutePieChartItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PieChartItem(
    PieChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CutePieChartItem *>(self)->take(key, call);
}

//  QRectF PieChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK12PieChartItem12boundingRectEv(
    const PieChartItem *self) {
  return new QRectF(self->PieChartItem::boundingRect());
}

//  void PieChartItem::paint(QPainter *a0, const QStyleOptionGraphicsItem
//      *a1, QWidget *a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    PieChartItem *self,
    QPainter *a0,
    const QStyleOptionGraphicsItem *a1,
    QWidget *a2) {
  self->PieChartItem::paint(a0, a1, a2);
}

//  ChartAnimation *PieChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_own_ZNK12PieChartItem9animationEv(
    const PieChartItem *self) {
  return self->PieChartItem::animation();
}

//  void PieChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    PieChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnPieChartItem *>(self)->OwnPieChartItem::hoverEnterEvent(
      event);
}

//  void PieChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    PieChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnPieChartItem *>(self)->OwnPieChartItem::hoverLeaveEvent(
      event);
}

//  void PieChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnPieChartItem *>(self)->OwnPieChartItem::mousePressEvent(
      event);
}

//  void PieChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnPieChartItem *>(self)->OwnPieChartItem::mouseReleaseEvent(
      event);
}

//  void PieChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    PieChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnPieChartItem *>(self)->OwnPieChartItem::mouseDoubleClickEvent(
      event);
}

//  void PieChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem19handleDomainUpdatedEv(PieChartItem *self) {
  self->PieChartItem::handleDomainUpdated();
}

//  void PieChartItem::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieChartItem7cleanupEv(PieChartItem *self) {
  self->PieChartItem::cleanup();
}

#endif  // QT_CONFIG(charts_pie_chart)
