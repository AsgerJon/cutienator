//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/candlestickchartitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/candlestickchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCharts/qcandlestickset.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A CandlestickChartItem that Python can take functions over in. Every CandlestickChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteCandlestickChartItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall2)(const void *, int *);
typedef void (*CuteCandlestickChartItemCall3)(const void *, int *);
typedef void * (*CuteCandlestickChartItemCall4)(const void *, int *);
typedef void (*CuteCandlestickChartItemCall5)(const void *, ChartPresenter *, int *);
typedef void (*CuteCandlestickChartItemCall6)(const void *, ChartThemeManager *, int *);
typedef void (*CuteCandlestickChartItemCall7)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCandlestickChartItemCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickChartItemCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickChartItemCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickChartItemCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickChartItemCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickChartItemCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall15)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteCandlestickChartItemCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall17)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall18)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall19)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall20)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteCandlestickChartItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteCandlestickChartItemCall22)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall23)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteCandlestickChartItemCall24)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall25)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall26)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall27)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall28)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall29)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall30)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall31)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall32)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall33)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall34)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall35)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall36)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall37)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall38)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall39)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall40)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteCandlestickChartItemCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteCandlestickChartItemCall43)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteCandlestickChartItemCall44)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteCandlestickChartItemCall45)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteCandlestickChartItem : public CandlestickChartItem {
public:
  using CandlestickChartItem::CandlestickChartItem;
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
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem7cleanupEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
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
  //  QRectF CandlestickChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteCandlestickChartItemCall0 call = reinterpret_cast<CuteCandlestickChartItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return CandlestickChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void CandlestickChartItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteCandlestickChartItemCall1 call = reinterpret_cast<CuteCandlestickChartItemCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    CandlestickChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CandlestickChartItem::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[2]) {
      int handled = 0;
      CuteCandlestickChartItemCall2 call = reinterpret_cast<CuteCandlestickChartItemCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    CandlestickChartItem::handleDomainUpdated();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[3]) {
      int handled = 0;
      CuteCandlestickChartItemCall3 call = reinterpret_cast<CuteCandlestickChartItemCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  ChartAnimation *ChartElement::animation() const
  ChartAnimation *animation() const override {
    if (taken[4]) {
      int handled = 0;
      CuteCandlestickChartItemCall4 call = reinterpret_cast<CuteCandlestickChartItemCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return ChartElement::animation();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[5]) {
      int handled = 0;
      CuteCandlestickChartItemCall5 call = reinterpret_cast<CuteCandlestickChartItemCall5>(taken[5]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[6]) {
      int handled = 0;
      CuteCandlestickChartItemCall6 call = reinterpret_cast<CuteCandlestickChartItemCall6>(taken[6]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[7]) {
      int handled = 0;
      CuteCandlestickChartItemCall7 call = reinterpret_cast<CuteCandlestickChartItemCall7>(taken[7]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[8]) {
      int handled = 0;
      CuteCandlestickChartItemCall8 call = reinterpret_cast<CuteCandlestickChartItemCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteCandlestickChartItemCall9 call = reinterpret_cast<CuteCandlestickChartItemCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteCandlestickChartItemCall10 call = reinterpret_cast<CuteCandlestickChartItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteCandlestickChartItemCall11 call = reinterpret_cast<CuteCandlestickChartItemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteCandlestickChartItemCall12 call = reinterpret_cast<CuteCandlestickChartItemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteCandlestickChartItemCall13 call = reinterpret_cast<CuteCandlestickChartItemCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteCandlestickChartItemCall14 call = reinterpret_cast<CuteCandlestickChartItemCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[15]) {
      int handled = 0;
      CuteCandlestickChartItemCall15 call = reinterpret_cast<CuteCandlestickChartItemCall15>(taken[15]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[16]) {
      int handled = 0;
      CuteCandlestickChartItemCall16 call = reinterpret_cast<CuteCandlestickChartItemCall16>(taken[16]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[17]) {
      int handled = 0;
      CuteCandlestickChartItemCall17 call = reinterpret_cast<CuteCandlestickChartItemCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteCandlestickChartItemCall18 call = reinterpret_cast<CuteCandlestickChartItemCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteCandlestickChartItemCall19 call = reinterpret_cast<CuteCandlestickChartItemCall19>(taken[19]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[20]) {
      int handled = 0;
      CuteCandlestickChartItemCall20 call = reinterpret_cast<CuteCandlestickChartItemCall20>(taken[20]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[21]) {
      int handled = 0;
      CuteCandlestickChartItemCall21 call = reinterpret_cast<CuteCandlestickChartItemCall21>(taken[21]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[22]) {
      int handled = 0;
      CuteCandlestickChartItemCall22 call = reinterpret_cast<CuteCandlestickChartItemCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteCandlestickChartItemCall23 call = reinterpret_cast<CuteCandlestickChartItemCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteCandlestickChartItemCall24 call = reinterpret_cast<CuteCandlestickChartItemCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteCandlestickChartItemCall25 call = reinterpret_cast<CuteCandlestickChartItemCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteCandlestickChartItemCall26 call = reinterpret_cast<CuteCandlestickChartItemCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteCandlestickChartItemCall27 call = reinterpret_cast<CuteCandlestickChartItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteCandlestickChartItemCall28 call = reinterpret_cast<CuteCandlestickChartItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteCandlestickChartItemCall29 call = reinterpret_cast<CuteCandlestickChartItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteCandlestickChartItemCall30 call = reinterpret_cast<CuteCandlestickChartItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteCandlestickChartItemCall31 call = reinterpret_cast<CuteCandlestickChartItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteCandlestickChartItemCall32 call = reinterpret_cast<CuteCandlestickChartItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteCandlestickChartItemCall33 call = reinterpret_cast<CuteCandlestickChartItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteCandlestickChartItemCall34 call = reinterpret_cast<CuteCandlestickChartItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteCandlestickChartItemCall35 call = reinterpret_cast<CuteCandlestickChartItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteCandlestickChartItemCall36 call = reinterpret_cast<CuteCandlestickChartItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteCandlestickChartItemCall37 call = reinterpret_cast<CuteCandlestickChartItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteCandlestickChartItemCall38 call = reinterpret_cast<CuteCandlestickChartItemCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteCandlestickChartItemCall39 call = reinterpret_cast<CuteCandlestickChartItemCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteCandlestickChartItemCall40 call = reinterpret_cast<CuteCandlestickChartItemCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteCandlestickChartItemCall41 call = reinterpret_cast<CuteCandlestickChartItemCall41>(taken[41]);
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
      CuteCandlestickChartItemCall42 call = reinterpret_cast<CuteCandlestickChartItemCall42>(taken[42]);
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
      CuteCandlestickChartItemCall43 call = reinterpret_cast<CuteCandlestickChartItemCall43>(taken[43]);
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
      CuteCandlestickChartItemCall44 call = reinterpret_cast<CuteCandlestickChartItemCall44>(taken[44]);
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
      CuteCandlestickChartItemCall45 call = reinterpret_cast<CuteCandlestickChartItemCall45>(taken[45]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *CandlestickChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20CandlestickChartItem10metaObjectEv(
    const CandlestickChartItem *self) {
  return self->metaObject();
}

//  QString CandlestickChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20CandlestickChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CandlestickChartItem::tr(s, c, n));
}

//  CandlestickChartItem::CandlestickChartItem(QCandlestickSeries *series,
//      QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
CandlestickChartItem *ritual_ZN20CandlestickChartItemC1EP18QCandlestickSeriesP13QGraphicsItem(
    QCandlestickSeries *series,
    QGraphicsItem *item) {
  return new CuteCandlestickChartItem(series, item);
}

//  CandlestickChartItem::~CandlestickChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItemD1Ev(CandlestickChartItem *self) {
  delete self;
}

//  void CandlestickChartItem::setAnimation(CandlestickAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem12setAnimationEP20CandlestickAnimation(
    CandlestickChartItem *self,
    CandlestickAnimation *animation) {
  self->setAnimation(animation);
}

//  QRectF CandlestickChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20CandlestickChartItem12boundingRectEv(
    const CandlestickChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void CandlestickChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    CandlestickChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void CandlestickChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem19handleDomainUpdatedEv(
    CandlestickChartItem *self) {
  self->handleDomainUpdated();
}

//  void CandlestickChartItem::handleLayoutUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem19handleLayoutUpdatedEv(
    CandlestickChartItem *self) {
  self->handleLayoutUpdated();
}

//  void CandlestickChartItem::handleCandlesticksUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem25handleCandlesticksUpdatedEv(
    CandlestickChartItem *self) {
  self->handleCandlesticksUpdated();
}

//  void CandlestickChartItem::handleCandlestickSeriesChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem29handleCandlestickSeriesChangeEv(
    CandlestickChartItem *self) {
  self->handleCandlestickSeriesChange();
}

//  void CandlestickChartItem::handleCandlestickSetsAdd(const
//      QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem24handleCandlestickSetsAddERK5QListIP15QCandlestickSetE(
    CandlestickChartItem *self,
    const QList<QCandlestickSet *> *sets) {
  self->handleCandlestickSetsAdd(*sets);
}

//  void CandlestickChartItem::handleCandlestickSetsRemove(const
//      QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem27handleCandlestickSetsRemoveERK5QListIP15QCandlestickSetE(
    CandlestickChartItem *self,
    const QList<QCandlestickSet *> *sets) {
  self->handleCandlestickSetsRemove(*sets);
}

//  void CandlestickChartItem::handleDataStructureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem26handleDataStructureChangedEv(
    CandlestickChartItem *self) {
  self->handleDataStructureChanged();
}

//  bool CandlestickChartItem::updateCandlestickGeometry(Candlestick *item,
//      int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20CandlestickChartItem25updateCandlestickGeometryEP11Candlesticki(
    CandlestickChartItem *self,
    Candlestick *item,
    int index) {
  return self->updateCandlestickGeometry(item, index);
}

//  void CandlestickChartItem::updateCandlestickAppearance(Candlestick *item,
//      QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem27updateCandlestickAppearanceEP11CandlestickP15QCandlestickSet(
    CandlestickChartItem *self,
    Candlestick *item,
    QCandlestickSet *set) {
  self->updateCandlestickAppearance(item, set);
}

//  void CandlestickChartItem::addTimestamp(qreal timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem12addTimestampEd(
    CandlestickChartItem *self,
    qreal timestamp) {
  self->addTimestamp(timestamp);
}

//  void CandlestickChartItem::removeTimestamp(qreal timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem15removeTimestampEd(
    CandlestickChartItem *self,
    qreal timestamp) {
  self->removeTimestamp(timestamp);
}

//  void CandlestickChartItem::updateTimePeriod()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickChartItem16updateTimePeriodEv(
    CandlestickChartItem *self) {
  self->updateTimePeriod();
}

//  a Python function taken by a CuteCandlestickChartItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CandlestickChartItem(
    CandlestickChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteCandlestickChartItem *>(self)->take(key, call);
}

//  QRectF CandlestickChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK20CandlestickChartItem12boundingRectEv(
    const CandlestickChartItem *self) {
  return new QRectF(self->CandlestickChartItem::boundingRect());
}

//  void CandlestickChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20CandlestickChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    CandlestickChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->CandlestickChartItem::paint(painter, option, widget);
}

//  void CandlestickChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20CandlestickChartItem19handleDomainUpdatedEv(
    CandlestickChartItem *self) {
  self->CandlestickChartItem::handleDomainUpdated();
}
