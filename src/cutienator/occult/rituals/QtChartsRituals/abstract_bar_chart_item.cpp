//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/abstractbarchartitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/abstractbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on AbstractBarChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAbstractBarChartItem : AbstractBarChartItem {
  using AbstractBarChartItem::generateLabelText;
  using AbstractBarChartItem::markLabelsDirty;
};

//  A AbstractBarChartItem that Python can take functions over in. Every AbstractBarChartItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall0)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteAbstractBarChartItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall2)(const void *, int, int, int, bool, int *);
typedef void (*CuteAbstractBarChartItemCall3)(const void *, BarAnimation *, int *);
typedef void * (*CuteAbstractBarChartItemCall4)(const void *, int *);
typedef void (*CuteAbstractBarChartItemCall5)(const void *, int *);
typedef void (*CuteAbstractBarChartItemCall6)(const void *, int *);
typedef QString * (*CuteAbstractBarChartItemCall7)(const void *, int, int, qreal, int *);
typedef void (*CuteAbstractBarChartItemCall8)(const void *, QBarSet *, int, int, int *);
typedef void (*CuteAbstractBarChartItemCall9)(const void *, int *);
typedef void (*CuteAbstractBarChartItemCall10)(const void *, ChartPresenter *, int *);
typedef void (*CuteAbstractBarChartItemCall11)(const void *, ChartThemeManager *, int *);
typedef void (*CuteAbstractBarChartItemCall12)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstractBarChartItemCall14)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractBarChartItemCall15)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractBarChartItemCall16)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractBarChartItemCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractBarChartItemCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractBarChartItemCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall20)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAbstractBarChartItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall22)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall23)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall24)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall25)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteAbstractBarChartItemCall26)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteAbstractBarChartItemCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall28)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractBarChartItemCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall30)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall31)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall32)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall33)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall34)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall35)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall36)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall37)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall38)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall39)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall40)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall41)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall42)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall43)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall44)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall45)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall46)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractBarChartItemCall47)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAbstractBarChartItemCall48)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAbstractBarChartItemCall49)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteAbstractBarChartItemCall50)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteAbstractBarChartItem : public AbstractBarChartItem {
public:
  using AbstractBarChartItem::AbstractBarChartItem;
  void *taken[51] = {};

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
    if (!std::strcmp(key, "_ZN20AbstractBarChartItem16initializeLayoutEiiib")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20AbstractBarChartItem12setAnimationEP12BarAnimation")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9ChartItem19handleDomainUpdatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20AbstractBarChartItem14positionLabelsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20AbstractBarChartItem17generateLabelTextEiid")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii")) {
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
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void AbstractBarChartItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[0]) {
      int handled = 0;
      CuteAbstractBarChartItemCall0 call = reinterpret_cast<CuteAbstractBarChartItemCall0>(taken[0]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    AbstractBarChartItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF AbstractBarChartItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAbstractBarChartItemCall1 call = reinterpret_cast<CuteAbstractBarChartItemCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return AbstractBarChartItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void AbstractBarChartItem::initializeLayout(int set, int category,
  //      int layoutIndex, bool resetAnimation)
  void initializeLayout(
      int set,
      int category,
      int layoutIndex,
      bool resetAnimation) override {
    if (taken[2]) {
      int handled = 0;
      CuteAbstractBarChartItemCall2 call = reinterpret_cast<CuteAbstractBarChartItemCall2>(taken[2]);
      call(this, set, category, layoutIndex, resetAnimation, &handled);
      if (handled) return;
    }
  }

  //  void AbstractBarChartItem::setAnimation(BarAnimation *animation)
  void setAnimation(BarAnimation *animation) override {
    if (taken[3]) {
      int handled = 0;
      CuteAbstractBarChartItemCall3 call = reinterpret_cast<CuteAbstractBarChartItemCall3>(taken[3]);
      call(this, animation, &handled);
      if (handled) return;
    }
    AbstractBarChartItem::setAnimation(animation);
  }

  //  ChartAnimation *AbstractBarChartItem::animation() const
  ChartAnimation *animation() const override {
    if (taken[4]) {
      int handled = 0;
      CuteAbstractBarChartItemCall4 call = reinterpret_cast<CuteAbstractBarChartItemCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<ChartAnimation *>(given);
    }
    return AbstractBarChartItem::animation();
  }

  //  void AbstractBarChartItem::handleDomainUpdated()
  void handleDomainUpdated() override {
    if (taken[5]) {
      int handled = 0;
      CuteAbstractBarChartItemCall5 call = reinterpret_cast<CuteAbstractBarChartItemCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractBarChartItem::handleDomainUpdated();
  }

  //  void AbstractBarChartItem::positionLabels()
  void positionLabels() override {
    if (taken[6]) {
      int handled = 0;
      CuteAbstractBarChartItemCall6 call = reinterpret_cast<CuteAbstractBarChartItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractBarChartItem::positionLabels();
  }

  //  QString AbstractBarChartItem::generateLabelText(int set, int
  //      category, qreal value)
  QString generateLabelText(int set, int category, qreal value) override {
    if (taken[7]) {
      int handled = 0;
      CuteAbstractBarChartItemCall7 call = reinterpret_cast<CuteAbstractBarChartItemCall7>(taken[7]);
      QString * given = call(this, set, category, value, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return AbstractBarChartItem::generateLabelText(set, category, value);
  }

  //  void AbstractBarChartItem::markLabelsDirty(QBarSet *barset, int
  //      index, int count)
  void markLabelsDirty(QBarSet *barset, int index, int count) override {
    if (taken[8]) {
      int handled = 0;
      CuteAbstractBarChartItemCall8 call = reinterpret_cast<CuteAbstractBarChartItemCall8>(taken[8]);
      call(this, barset, index, count, &handled);
      if (handled) return;
    }
    AbstractBarChartItem::markLabelsDirty(barset, index, count);
  }

  //  void ChartItem::cleanup()
  void cleanup() override {
    if (taken[9]) {
      int handled = 0;
      CuteAbstractBarChartItemCall9 call = reinterpret_cast<CuteAbstractBarChartItemCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    ChartItem::cleanup();
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[10]) {
      int handled = 0;
      CuteAbstractBarChartItemCall10 call = reinterpret_cast<CuteAbstractBarChartItemCall10>(taken[10]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[11]) {
      int handled = 0;
      CuteAbstractBarChartItemCall11 call = reinterpret_cast<CuteAbstractBarChartItemCall11>(taken[11]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[12]) {
      int handled = 0;
      CuteAbstractBarChartItemCall12 call = reinterpret_cast<CuteAbstractBarChartItemCall12>(taken[12]);
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
      CuteAbstractBarChartItemCall13 call = reinterpret_cast<CuteAbstractBarChartItemCall13>(taken[13]);
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
      CuteAbstractBarChartItemCall14 call = reinterpret_cast<CuteAbstractBarChartItemCall14>(taken[14]);
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
      CuteAbstractBarChartItemCall15 call = reinterpret_cast<CuteAbstractBarChartItemCall15>(taken[15]);
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
      CuteAbstractBarChartItemCall16 call = reinterpret_cast<CuteAbstractBarChartItemCall16>(taken[16]);
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
      CuteAbstractBarChartItemCall17 call = reinterpret_cast<CuteAbstractBarChartItemCall17>(taken[17]);
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
      CuteAbstractBarChartItemCall18 call = reinterpret_cast<CuteAbstractBarChartItemCall18>(taken[18]);
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
      CuteAbstractBarChartItemCall19 call = reinterpret_cast<CuteAbstractBarChartItemCall19>(taken[19]);
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
      CuteAbstractBarChartItemCall20 call = reinterpret_cast<CuteAbstractBarChartItemCall20>(taken[20]);
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
      CuteAbstractBarChartItemCall21 call = reinterpret_cast<CuteAbstractBarChartItemCall21>(taken[21]);
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
      CuteAbstractBarChartItemCall22 call = reinterpret_cast<CuteAbstractBarChartItemCall22>(taken[22]);
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
      CuteAbstractBarChartItemCall23 call = reinterpret_cast<CuteAbstractBarChartItemCall23>(taken[23]);
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
      CuteAbstractBarChartItemCall24 call = reinterpret_cast<CuteAbstractBarChartItemCall24>(taken[24]);
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
      CuteAbstractBarChartItemCall25 call = reinterpret_cast<CuteAbstractBarChartItemCall25>(taken[25]);
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
      CuteAbstractBarChartItemCall26 call = reinterpret_cast<CuteAbstractBarChartItemCall26>(taken[26]);
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
      CuteAbstractBarChartItemCall27 call = reinterpret_cast<CuteAbstractBarChartItemCall27>(taken[27]);
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
      CuteAbstractBarChartItemCall28 call = reinterpret_cast<CuteAbstractBarChartItemCall28>(taken[28]);
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
      CuteAbstractBarChartItemCall29 call = reinterpret_cast<CuteAbstractBarChartItemCall29>(taken[29]);
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
      CuteAbstractBarChartItemCall30 call = reinterpret_cast<CuteAbstractBarChartItemCall30>(taken[30]);
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
      CuteAbstractBarChartItemCall31 call = reinterpret_cast<CuteAbstractBarChartItemCall31>(taken[31]);
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
      CuteAbstractBarChartItemCall32 call = reinterpret_cast<CuteAbstractBarChartItemCall32>(taken[32]);
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
      CuteAbstractBarChartItemCall33 call = reinterpret_cast<CuteAbstractBarChartItemCall33>(taken[33]);
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
      CuteAbstractBarChartItemCall34 call = reinterpret_cast<CuteAbstractBarChartItemCall34>(taken[34]);
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
      CuteAbstractBarChartItemCall35 call = reinterpret_cast<CuteAbstractBarChartItemCall35>(taken[35]);
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
      CuteAbstractBarChartItemCall36 call = reinterpret_cast<CuteAbstractBarChartItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteAbstractBarChartItemCall37 call = reinterpret_cast<CuteAbstractBarChartItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAbstractBarChartItemCall38 call = reinterpret_cast<CuteAbstractBarChartItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteAbstractBarChartItemCall39 call = reinterpret_cast<CuteAbstractBarChartItemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteAbstractBarChartItemCall40 call = reinterpret_cast<CuteAbstractBarChartItemCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteAbstractBarChartItemCall41 call = reinterpret_cast<CuteAbstractBarChartItemCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteAbstractBarChartItemCall42 call = reinterpret_cast<CuteAbstractBarChartItemCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteAbstractBarChartItemCall43 call = reinterpret_cast<CuteAbstractBarChartItemCall43>(taken[43]);
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
    if (taken[44]) {
      int handled = 0;
      CuteAbstractBarChartItemCall44 call = reinterpret_cast<CuteAbstractBarChartItemCall44>(taken[44]);
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
    if (taken[45]) {
      int handled = 0;
      CuteAbstractBarChartItemCall45 call = reinterpret_cast<CuteAbstractBarChartItemCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteAbstractBarChartItemCall46 call = reinterpret_cast<CuteAbstractBarChartItemCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteAbstractBarChartItemCall47 call = reinterpret_cast<CuteAbstractBarChartItemCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteAbstractBarChartItemCall48 call = reinterpret_cast<CuteAbstractBarChartItemCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteAbstractBarChartItemCall49 call = reinterpret_cast<CuteAbstractBarChartItemCall49>(taken[49]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[50]) {
      int handled = 0;
      CuteAbstractBarChartItemCall50 call = reinterpret_cast<CuteAbstractBarChartItemCall50>(taken[50]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *AbstractBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20AbstractBarChartItem10metaObjectEv(
    const AbstractBarChartItem *self) {
  return self->metaObject();
}

//  QString AbstractBarChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20AbstractBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AbstractBarChartItem::tr(s, c, n));
}

//  AbstractBarChartItem::~AbstractBarChartItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItemD1Ev(AbstractBarChartItem *self) {
  delete self;
}

//  void AbstractBarChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    AbstractBarChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QRectF AbstractBarChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20AbstractBarChartItem12boundingRectEv(
    const AbstractBarChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  QList<QRectF> AbstractBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN20AbstractBarChartItem15calculateLayoutEv(
    AbstractBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void AbstractBarChartItem::initializeFullLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem20initializeFullLayoutEv(
    AbstractBarChartItem *self) {
  self->initializeFullLayout();
}

//  void AbstractBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem16initializeLayoutEiiib(
    AbstractBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  void AbstractBarChartItem::applyLayout(const QList<QRectF> &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem11applyLayoutERK5QListI6QRectFE(
    AbstractBarChartItem *self,
    const QList<QRectF> *layout) {
  self->applyLayout(*layout);
}

//  void AbstractBarChartItem::setAnimation(BarAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem12setAnimationEP12BarAnimation(
    AbstractBarChartItem *self,
    BarAnimation *animation) {
  self->setAnimation(animation);
}

//  ChartAnimation *AbstractBarChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZNK20AbstractBarChartItem9animationEv(
    const AbstractBarChartItem *self) {
  return self->animation();
}

//  void AbstractBarChartItem::setLayout(const QList<QRectF> &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem9setLayoutERK5QListI6QRectFE(
    AbstractBarChartItem *self,
    const QList<QRectF> *layout) {
  self->setLayout(*layout);
}

//  QRectF AbstractBarChartItem::geometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20AbstractBarChartItem8geometryEv(
    const AbstractBarChartItem *self) {
  return new QRectF(self->geometry());
}

//  void AbstractBarChartItem::resetAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem14resetAnimationEv(
    AbstractBarChartItem *self) {
  self->resetAnimation();
}

//  void AbstractBarChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem19handleDomainUpdatedEv(
    AbstractBarChartItem *self) {
  self->handleDomainUpdated();
}

//  void AbstractBarChartItem::handleLayoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem19handleLayoutChangedEv(
    AbstractBarChartItem *self) {
  self->handleLayoutChanged();
}

//  void AbstractBarChartItem::handleLabelsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem26handleLabelsVisibleChangedEb(
    AbstractBarChartItem *self,
    bool visible) {
  self->handleLabelsVisibleChanged(visible);
}

//  void AbstractBarChartItem::handleDataStructureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem26handleDataStructureChangedEv(
    AbstractBarChartItem *self) {
  self->handleDataStructureChanged();
}

//  void AbstractBarChartItem::handleVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem20handleVisibleChangedEv(
    AbstractBarChartItem *self) {
  self->handleVisibleChanged();
}

//  void AbstractBarChartItem::handleOpacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem20handleOpacityChangedEv(
    AbstractBarChartItem *self) {
  self->handleOpacityChanged();
}

//  void AbstractBarChartItem::handleUpdatedBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem17handleUpdatedBarsEv(
    AbstractBarChartItem *self) {
  self->handleUpdatedBars();
}

//  void AbstractBarChartItem::handleLabelsPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem27handleLabelsPositionChangedEv(
    AbstractBarChartItem *self) {
  self->handleLabelsPositionChanged();
}

//  void AbstractBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem14positionLabelsEv(
    AbstractBarChartItem *self) {
  self->positionLabels();
}

//  void AbstractBarChartItem::handleBarValueChange(int index, QBarSet
//      *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem20handleBarValueChangeEiP7QBarSet(
    AbstractBarChartItem *self,
    int index,
    QBarSet *barset) {
  self->handleBarValueChange(index, barset);
}

//  void AbstractBarChartItem::handleBarValueAdd(int index, int count,
//      QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem17handleBarValueAddEiiP7QBarSet(
    AbstractBarChartItem *self,
    int index,
    int count,
    QBarSet *barset) {
  self->handleBarValueAdd(index, count, barset);
}

//  void AbstractBarChartItem::handleBarValueRemove(int index, int count,
//      QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem20handleBarValueRemoveEiiP7QBarSet(
    AbstractBarChartItem *self,
    int index,
    int count,
    QBarSet *barset) {
  self->handleBarValueRemove(index, count, barset);
}

//  void AbstractBarChartItem::handleSeriesAdded(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem17handleSeriesAddedEP15QAbstractSeries(
    AbstractBarChartItem *self,
    QAbstractSeries *series) {
  self->handleSeriesAdded(series);
}

//  void AbstractBarChartItem::handleSeriesRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem19handleSeriesRemovedEP15QAbstractSeries(
    AbstractBarChartItem *self,
    QAbstractSeries *series) {
  self->handleSeriesRemoved(series);
}

//  void AbstractBarChartItem::positionLabelsVertical()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem22positionLabelsVerticalEv(
    AbstractBarChartItem *self) {
  self->positionLabelsVertical();
}

//  void AbstractBarChartItem::createLabelItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem16createLabelItemsEv(
    AbstractBarChartItem *self) {
  self->createLabelItems();
}

//  void AbstractBarChartItem::handleSetStructureChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem24handleSetStructureChangeEv(
    AbstractBarChartItem *self) {
  self->handleSetStructureChange();
}

//  QString AbstractBarChartItem::generateLabelText(int set, int category,
//      qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20AbstractBarChartItem17generateLabelTextEiid(
    AbstractBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(self->generateLabelText(set, category, value));
}

//  void AbstractBarChartItem::updateBarItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem14updateBarItemsEv(
    AbstractBarChartItem *self) {
  self->updateBarItems();
}

//  void AbstractBarChartItem::markLabelsDirty(QBarSet *barset, int index,
//      int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii(
    AbstractBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  self->markLabelsDirty(barset, index, count);
}

//  void AbstractBarChartItem::calculateSeriesPositionAdjustmentAndWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractBarChartItem41calculateSeriesPositionAdjustmentAndWidthEv(
    AbstractBarChartItem *self) {
  self->calculateSeriesPositionAdjustmentAndWidth();
}

//  a Python function taken by a CuteAbstractBarChartItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractBarChartItem(
    AbstractBarChartItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractBarChartItem *>(self)->take(key, call);
}

//  void AbstractBarChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20AbstractBarChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    AbstractBarChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->AbstractBarChartItem::paint(painter, option, widget);
}

//  QRectF AbstractBarChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK20AbstractBarChartItem12boundingRectEv(
    const AbstractBarChartItem *self) {
  return new QRectF(self->AbstractBarChartItem::boundingRect());
}

//  void AbstractBarChartItem::setAnimation(BarAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20AbstractBarChartItem12setAnimationEP12BarAnimation(
    AbstractBarChartItem *self,
    BarAnimation *animation) {
  self->AbstractBarChartItem::setAnimation(animation);
}

//  ChartAnimation *AbstractBarChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_own_ZNK20AbstractBarChartItem9animationEv(
    const AbstractBarChartItem *self) {
  return self->AbstractBarChartItem::animation();
}

//  void AbstractBarChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20AbstractBarChartItem19handleDomainUpdatedEv(
    AbstractBarChartItem *self) {
  self->AbstractBarChartItem::handleDomainUpdated();
}

//  void AbstractBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20AbstractBarChartItem14positionLabelsEv(
    AbstractBarChartItem *self) {
  self->AbstractBarChartItem::positionLabels();
}

//  QString AbstractBarChartItem::generateLabelText(int set, int category,
//      qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN20AbstractBarChartItem17generateLabelTextEiid(
    AbstractBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(
      static_cast<OwnAbstractBarChartItem *>(self)->OwnAbstractBarChartItem::generateLabelText(
          set,
          category,
          value));
}

//  void AbstractBarChartItem::markLabelsDirty(QBarSet *barset, int index,
//      int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii(
    AbstractBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  static_cast<OwnAbstractBarChartItem *>(self)->OwnAbstractBarChartItem::markLabelsDirty(
      barset,
      index,
      count);
}

#endif  // QT_CONFIG(charts_bar_chart)
