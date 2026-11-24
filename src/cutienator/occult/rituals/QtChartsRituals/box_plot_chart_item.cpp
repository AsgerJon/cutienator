//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/boxplotchartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxplotchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCharts/qboxset.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A BoxPlotChartItem that Python can take functions over in. Every BoxPlotChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall0)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteBoxPlotChartItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall2)(const void *, int *);
typedef void (*CuteBoxPlotChartItemCall3)(const void *, int *);
typedef void * (*CuteBoxPlotChartItemCall4)(const void *, int *);
typedef void (*CuteBoxPlotChartItemCall5)(const void *, ChartPresenter *, int *);
typedef void (*CuteBoxPlotChartItemCall6)(const void *, ChartThemeManager *, int *);
typedef void (*CuteBoxPlotChartItemCall7)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBoxPlotChartItemCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotChartItemCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotChartItemCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotChartItemCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotChartItemCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotChartItemCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall15)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteBoxPlotChartItemCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall17)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall18)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall19)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall20)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteBoxPlotChartItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteBoxPlotChartItemCall22)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall23)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxPlotChartItemCall24)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall25)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall26)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall27)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall28)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall29)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall30)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall31)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall32)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall33)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall34)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall35)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall36)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall37)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall38)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall39)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall40)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxPlotChartItemCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxPlotChartItemCall43)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxPlotChartItemCall44)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxPlotChartItemCall45)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteBoxPlotChartItem : public BoxPlotChartItem {
public:
  using BoxPlotChartItem::BoxPlotChartItem;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
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
  //  void BoxPlotChartItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[0]) {
      int handled = 0;
      CuteBoxPlotChartItemCall0 call = reinterpret_cast<CuteBoxPlotChartItemCall0>(taken[0]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    BoxPlotChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF BoxPlotChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteBoxPlotChartItemCall1 call = reinterpret_cast<CuteBoxPlotChartItemCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return BoxPlotChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void BoxPlotChartItem::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[2]) {
      int handled = 0;
      CuteBoxPlotChartItemCall2 call = reinterpret_cast<CuteBoxPlotChartItemCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    BoxPlotChartItem::handleDomainUpdated();
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[3]) {
      int handled = 0;
      CuteBoxPlotChartItemCall3 call = reinterpret_cast<CuteBoxPlotChartItemCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  ChartAnimation *ChartElement::animation() const
  ChartAnimation *animation() const override {
    if (taken[4]) {
      int handled = 0;
      CuteBoxPlotChartItemCall4 call = reinterpret_cast<CuteBoxPlotChartItemCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return ChartElement::animation();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[5]) {
      int handled = 0;
      CuteBoxPlotChartItemCall5 call = reinterpret_cast<CuteBoxPlotChartItemCall5>(taken[5]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[6]) {
      int handled = 0;
      CuteBoxPlotChartItemCall6 call = reinterpret_cast<CuteBoxPlotChartItemCall6>(taken[6]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[7]) {
      int handled = 0;
      CuteBoxPlotChartItemCall7 call = reinterpret_cast<CuteBoxPlotChartItemCall7>(taken[7]);
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
      CuteBoxPlotChartItemCall8 call = reinterpret_cast<CuteBoxPlotChartItemCall8>(taken[8]);
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
      CuteBoxPlotChartItemCall9 call = reinterpret_cast<CuteBoxPlotChartItemCall9>(taken[9]);
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
      CuteBoxPlotChartItemCall10 call = reinterpret_cast<CuteBoxPlotChartItemCall10>(taken[10]);
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
      CuteBoxPlotChartItemCall11 call = reinterpret_cast<CuteBoxPlotChartItemCall11>(taken[11]);
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
      CuteBoxPlotChartItemCall12 call = reinterpret_cast<CuteBoxPlotChartItemCall12>(taken[12]);
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
      CuteBoxPlotChartItemCall13 call = reinterpret_cast<CuteBoxPlotChartItemCall13>(taken[13]);
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
      CuteBoxPlotChartItemCall14 call = reinterpret_cast<CuteBoxPlotChartItemCall14>(taken[14]);
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
      CuteBoxPlotChartItemCall15 call = reinterpret_cast<CuteBoxPlotChartItemCall15>(taken[15]);
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
      CuteBoxPlotChartItemCall16 call = reinterpret_cast<CuteBoxPlotChartItemCall16>(taken[16]);
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
      CuteBoxPlotChartItemCall17 call = reinterpret_cast<CuteBoxPlotChartItemCall17>(taken[17]);
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
      CuteBoxPlotChartItemCall18 call = reinterpret_cast<CuteBoxPlotChartItemCall18>(taken[18]);
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
      CuteBoxPlotChartItemCall19 call = reinterpret_cast<CuteBoxPlotChartItemCall19>(taken[19]);
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
      CuteBoxPlotChartItemCall20 call = reinterpret_cast<CuteBoxPlotChartItemCall20>(taken[20]);
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
      CuteBoxPlotChartItemCall21 call = reinterpret_cast<CuteBoxPlotChartItemCall21>(taken[21]);
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
      CuteBoxPlotChartItemCall22 call = reinterpret_cast<CuteBoxPlotChartItemCall22>(taken[22]);
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
      CuteBoxPlotChartItemCall23 call = reinterpret_cast<CuteBoxPlotChartItemCall23>(taken[23]);
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
      CuteBoxPlotChartItemCall24 call = reinterpret_cast<CuteBoxPlotChartItemCall24>(taken[24]);
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
      CuteBoxPlotChartItemCall25 call = reinterpret_cast<CuteBoxPlotChartItemCall25>(taken[25]);
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
      CuteBoxPlotChartItemCall26 call = reinterpret_cast<CuteBoxPlotChartItemCall26>(taken[26]);
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
      CuteBoxPlotChartItemCall27 call = reinterpret_cast<CuteBoxPlotChartItemCall27>(taken[27]);
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
      CuteBoxPlotChartItemCall28 call = reinterpret_cast<CuteBoxPlotChartItemCall28>(taken[28]);
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
      CuteBoxPlotChartItemCall29 call = reinterpret_cast<CuteBoxPlotChartItemCall29>(taken[29]);
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
      CuteBoxPlotChartItemCall30 call = reinterpret_cast<CuteBoxPlotChartItemCall30>(taken[30]);
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
      CuteBoxPlotChartItemCall31 call = reinterpret_cast<CuteBoxPlotChartItemCall31>(taken[31]);
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
      CuteBoxPlotChartItemCall32 call = reinterpret_cast<CuteBoxPlotChartItemCall32>(taken[32]);
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
      CuteBoxPlotChartItemCall33 call = reinterpret_cast<CuteBoxPlotChartItemCall33>(taken[33]);
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
      CuteBoxPlotChartItemCall34 call = reinterpret_cast<CuteBoxPlotChartItemCall34>(taken[34]);
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
      CuteBoxPlotChartItemCall35 call = reinterpret_cast<CuteBoxPlotChartItemCall35>(taken[35]);
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
      CuteBoxPlotChartItemCall36 call = reinterpret_cast<CuteBoxPlotChartItemCall36>(taken[36]);
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
      CuteBoxPlotChartItemCall37 call = reinterpret_cast<CuteBoxPlotChartItemCall37>(taken[37]);
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
      CuteBoxPlotChartItemCall38 call = reinterpret_cast<CuteBoxPlotChartItemCall38>(taken[38]);
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
      CuteBoxPlotChartItemCall39 call = reinterpret_cast<CuteBoxPlotChartItemCall39>(taken[39]);
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
      CuteBoxPlotChartItemCall40 call = reinterpret_cast<CuteBoxPlotChartItemCall40>(taken[40]);
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
      CuteBoxPlotChartItemCall41 call = reinterpret_cast<CuteBoxPlotChartItemCall41>(taken[41]);
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
      CuteBoxPlotChartItemCall42 call = reinterpret_cast<CuteBoxPlotChartItemCall42>(taken[42]);
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
      CuteBoxPlotChartItemCall43 call = reinterpret_cast<CuteBoxPlotChartItemCall43>(taken[43]);
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
      CuteBoxPlotChartItemCall44 call = reinterpret_cast<CuteBoxPlotChartItemCall44>(taken[44]);
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
      CuteBoxPlotChartItemCall45 call = reinterpret_cast<CuteBoxPlotChartItemCall45>(taken[45]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *BoxPlotChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16BoxPlotChartItem10metaObjectEv(
    const BoxPlotChartItem *self) {
  return self->metaObject();
}

//  QString BoxPlotChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16BoxPlotChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BoxPlotChartItem::tr(s, c, n));
}

//  BoxPlotChartItem::BoxPlotChartItem(QBoxPlotSeries *series, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
BoxPlotChartItem *ritual_ZN16BoxPlotChartItemC1EP14QBoxPlotSeriesP13QGraphicsItem(
    QBoxPlotSeries *series,
    QGraphicsItem *item) {
  return new CuteBoxPlotChartItem(series, item);
}

//  BoxPlotChartItem::~BoxPlotChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItemD1Ev(BoxPlotChartItem *self) {
  delete self;
}

//  void BoxPlotChartItem::setAnimation(BoxPlotAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem12setAnimationEP16BoxPlotAnimation(
    BoxPlotChartItem *self,
    BoxPlotAnimation *animation) {
  self->setAnimation(animation);
}

//  void BoxPlotChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    BoxPlotChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QRectF BoxPlotChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16BoxPlotChartItem12boundingRectEv(
    const BoxPlotChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void BoxPlotChartItem::handleSeriesVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem26handleSeriesVisibleChangedEv(
    BoxPlotChartItem *self) {
  self->handleSeriesVisibleChanged();
}

//  void BoxPlotChartItem::handleOpacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem20handleOpacityChangedEv(
    BoxPlotChartItem *self) {
  self->handleOpacityChanged();
}

//  void BoxPlotChartItem::handleDataStructureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem26handleDataStructureChangedEv(
    BoxPlotChartItem *self) {
  self->handleDataStructureChanged();
}

//  void BoxPlotChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem19handleDomainUpdatedEv(
    BoxPlotChartItem *self) {
  self->handleDomainUpdated();
}

//  void BoxPlotChartItem::handleLayoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem19handleLayoutChangedEv(
    BoxPlotChartItem *self) {
  self->handleLayoutChanged();
}

//  void BoxPlotChartItem::handleUpdatedBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem17handleUpdatedBarsEv(
    BoxPlotChartItem *self) {
  self->handleUpdatedBars();
}

//  void BoxPlotChartItem::handleBoxsetRemove(const QList<QBoxSet *>
//      &barSets)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem18handleBoxsetRemoveERK5QListIP7QBoxSetE(
    BoxPlotChartItem *self,
    const QList<QBoxSet *> *barSets) {
  self->handleBoxsetRemove(*barSets);
}

//  QList<QRectF> BoxPlotChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN16BoxPlotChartItem15calculateLayoutEv(
    BoxPlotChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void BoxPlotChartItem::initializeLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotChartItem16initializeLayoutEv(
    BoxPlotChartItem *self) {
  self->initializeLayout();
}

//  bool BoxPlotChartItem::updateBoxGeometry(BoxWhiskers *box, int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16BoxPlotChartItem17updateBoxGeometryEP11BoxWhiskersi(
    BoxPlotChartItem *self,
    BoxWhiskers *box,
    int index) {
  return self->updateBoxGeometry(box, index);
}

//  a Python function taken by a CuteBoxPlotChartItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BoxPlotChartItem(
    BoxPlotChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteBoxPlotChartItem *>(self)->take(key, call);
}

//  void BoxPlotChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16BoxPlotChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    BoxPlotChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->BoxPlotChartItem::paint(painter, option, widget);
}

//  QRectF BoxPlotChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK16BoxPlotChartItem12boundingRectEv(
    const BoxPlotChartItem *self) {
  return new QRectF(self->BoxPlotChartItem::boundingRect());
}

//  void BoxPlotChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16BoxPlotChartItem19handleDomainUpdatedEv(
    BoxPlotChartItem *self) {
  self->BoxPlotChartItem::handleDomainUpdated();
}
