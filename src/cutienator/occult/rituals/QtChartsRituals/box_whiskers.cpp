//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/boxwhiskers_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxwhiskers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxwhiskersdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A BoxWhiskers that Python can take functions over in. Every BoxWhiskers
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall0)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall1)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall2)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall3)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall4)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteBoxWhiskersCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall6)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBoxWhiskersCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall14)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteBoxWhiskersCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall16)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall17)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall18)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall19)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteBoxWhiskersCall20)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteBoxWhiskersCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall22)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteBoxWhiskersCall23)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall24)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall25)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall26)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall27)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall28)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall29)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall30)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall31)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall32)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall33)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall34)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall35)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteBoxWhiskersCall36)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxWhiskersCall37)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxWhiskersCall38)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteBoxWhiskersCall39)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteBoxWhiskers : public BoxWhiskers {
public:
  using BoxWhiskers::BoxWhiskers;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteBoxWhiskersCall0 call = reinterpret_cast<CuteBoxWhiskersCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    BoxWhiskers::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteBoxWhiskersCall1 call = reinterpret_cast<CuteBoxWhiskersCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    BoxWhiskers::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteBoxWhiskersCall2 call = reinterpret_cast<CuteBoxWhiskersCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    BoxWhiskers::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteBoxWhiskersCall3 call = reinterpret_cast<CuteBoxWhiskersCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    BoxWhiskers::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteBoxWhiskersCall4 call = reinterpret_cast<CuteBoxWhiskersCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    BoxWhiskers::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF BoxWhiskers::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteBoxWhiskersCall5 call = reinterpret_cast<CuteBoxWhiskersCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return BoxWhiskers::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void BoxWhiskers::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[6]) {
      int handled = 0;
      CuteBoxWhiskersCall6 call = reinterpret_cast<CuteBoxWhiskersCall6>(taken[6]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    BoxWhiskers::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[7]) {
      int handled = 0;
      CuteBoxWhiskersCall7 call = reinterpret_cast<CuteBoxWhiskersCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteBoxWhiskersCall8 call = reinterpret_cast<CuteBoxWhiskersCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteBoxWhiskersCall9 call = reinterpret_cast<CuteBoxWhiskersCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteBoxWhiskersCall10 call = reinterpret_cast<CuteBoxWhiskersCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteBoxWhiskersCall11 call = reinterpret_cast<CuteBoxWhiskersCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteBoxWhiskersCall12 call = reinterpret_cast<CuteBoxWhiskersCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteBoxWhiskersCall13 call = reinterpret_cast<CuteBoxWhiskersCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[14]) {
      int handled = 0;
      CuteBoxWhiskersCall14 call = reinterpret_cast<CuteBoxWhiskersCall14>(taken[14]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[15]) {
      int handled = 0;
      CuteBoxWhiskersCall15 call = reinterpret_cast<CuteBoxWhiskersCall15>(taken[15]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[16]) {
      int handled = 0;
      CuteBoxWhiskersCall16 call = reinterpret_cast<CuteBoxWhiskersCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteBoxWhiskersCall17 call = reinterpret_cast<CuteBoxWhiskersCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteBoxWhiskersCall18 call = reinterpret_cast<CuteBoxWhiskersCall18>(taken[18]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[19]) {
      int handled = 0;
      CuteBoxWhiskersCall19 call = reinterpret_cast<CuteBoxWhiskersCall19>(taken[19]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[20]) {
      int handled = 0;
      CuteBoxWhiskersCall20 call = reinterpret_cast<CuteBoxWhiskersCall20>(taken[20]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[21]) {
      int handled = 0;
      CuteBoxWhiskersCall21 call = reinterpret_cast<CuteBoxWhiskersCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteBoxWhiskersCall22 call = reinterpret_cast<CuteBoxWhiskersCall22>(taken[22]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteBoxWhiskersCall23 call = reinterpret_cast<CuteBoxWhiskersCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteBoxWhiskersCall24 call = reinterpret_cast<CuteBoxWhiskersCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteBoxWhiskersCall25 call = reinterpret_cast<CuteBoxWhiskersCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteBoxWhiskersCall26 call = reinterpret_cast<CuteBoxWhiskersCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteBoxWhiskersCall27 call = reinterpret_cast<CuteBoxWhiskersCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteBoxWhiskersCall28 call = reinterpret_cast<CuteBoxWhiskersCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteBoxWhiskersCall29 call = reinterpret_cast<CuteBoxWhiskersCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteBoxWhiskersCall30 call = reinterpret_cast<CuteBoxWhiskersCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteBoxWhiskersCall31 call = reinterpret_cast<CuteBoxWhiskersCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteBoxWhiskersCall32 call = reinterpret_cast<CuteBoxWhiskersCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteBoxWhiskersCall33 call = reinterpret_cast<CuteBoxWhiskersCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteBoxWhiskersCall34 call = reinterpret_cast<CuteBoxWhiskersCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteBoxWhiskersCall35 call = reinterpret_cast<CuteBoxWhiskersCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteBoxWhiskersCall36 call = reinterpret_cast<CuteBoxWhiskersCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteBoxWhiskersCall37 call = reinterpret_cast<CuteBoxWhiskersCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteBoxWhiskersCall38 call = reinterpret_cast<CuteBoxWhiskersCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[39]) {
      int handled = 0;
      CuteBoxWhiskersCall39 call = reinterpret_cast<CuteBoxWhiskersCall39>(taken[39]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *BoxWhiskers::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11BoxWhiskers10metaObjectEv(
    const BoxWhiskers *self) {
  return self->metaObject();
}

//  void *BoxWhiskers::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11BoxWhiskers11qt_metacastEPKc(
    BoxWhiskers *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int BoxWhiskers::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11BoxWhiskers11qt_metacallEN11QMetaObject4CallEiPPv(
    BoxWhiskers *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString BoxWhiskers::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11BoxWhiskers2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BoxWhiskers::tr(s, c, n));
}

//  BoxWhiskers::BoxWhiskers(QBoxSet *set, AbstractDomain *domain,
//      QGraphicsObject *parent)
extern "C" Q_DECL_EXPORT
BoxWhiskers *ritual_ZN11BoxWhiskersC1EP7QBoxSetP14AbstractDomainP15QGraphicsObject(
    QBoxSet *set,
    AbstractDomain *domain,
    QGraphicsObject *parent) {
  return new CuteBoxWhiskers(set, domain, parent);
}

//  BoxWhiskers::~BoxWhiskers()
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskersD1Ev(BoxWhiskers *self) {
  delete self;
}

//  void BoxWhiskers::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers8setBrushERK6QBrush(
    BoxWhiskers *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  void BoxWhiskers::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers6setPenERK4QPen(
    BoxWhiskers *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  void BoxWhiskers::setLayout(const BoxWhiskersData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers9setLayoutERK15BoxWhiskersData(
    BoxWhiskers *self,
    const BoxWhiskersData *data) {
  self->setLayout(*data);
}

//  void BoxWhiskers::setBoxOutlined(const bool outlined)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers14setBoxOutlinedEb(
    BoxWhiskers *self,
    bool outlined) {
  self->setBoxOutlined(outlined);
}

//  void BoxWhiskers::setBoxWidth(const qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers11setBoxWidthEd(BoxWhiskers *self, qreal width) {
  self->setBoxWidth(width);
}

//  void BoxWhiskers::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers15mousePressEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void BoxWhiskers::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    BoxWhiskers *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void BoxWhiskers::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    BoxWhiskers *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void BoxWhiskers::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void BoxWhiskers::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  QRectF BoxWhiskers::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11BoxWhiskers12boundingRectEv(const BoxWhiskers *self) {
  return new QRectF(self->boundingRect());
}

//  void BoxWhiskers::paint(QPainter *painter, const QStyleOptionGraphicsItem
//      *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    BoxWhiskers *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void BoxWhiskers::updateGeometry(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers14updateGeometryEP14AbstractDomain(
    BoxWhiskers *self,
    AbstractDomain *domain) {
  self->updateGeometry(domain);
}

//  QSizeF BoxWhiskers::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK11BoxWhiskers8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const BoxWhiskers *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void BoxWhiskers::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers11setGeometryERK6QRectF(
    BoxWhiskers *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void BoxWhiskers::clicked(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers7clickedEP7QBoxSet(
    BoxWhiskers *self,
    QBoxSet *boxset) {
  self->clicked(boxset);
}

//  void BoxWhiskers::hovered(bool status, QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers7hoveredEbP7QBoxSet(
    BoxWhiskers *self,
    bool status,
    QBoxSet *boxset) {
  self->hovered(status, boxset);
}

//  void BoxWhiskers::pressed(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers7pressedEP7QBoxSet(
    BoxWhiskers *self,
    QBoxSet *boxset) {
  self->pressed(boxset);
}

//  void BoxWhiskers::released(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers8releasedEP7QBoxSet(
    BoxWhiskers *self,
    QBoxSet *boxset) {
  self->released(boxset);
}

//  void BoxWhiskers::doubleClicked(QBoxSet *boxset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11BoxWhiskers13doubleClickedEP7QBoxSet(
    BoxWhiskers *self,
    QBoxSet *boxset) {
  self->doubleClicked(boxset);
}

//  a Python function taken by a CuteBoxWhiskers, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BoxWhiskers(
    BoxWhiskers *self,
    const char *key,
    void *call) {
  return static_cast<CuteBoxWhiskers *>(self)->take(key, call);
}

//  void BoxWhiskers::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers15mousePressEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->BoxWhiskers::mousePressEvent(event);
}

//  void BoxWhiskers::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    BoxWhiskers *self,
    QGraphicsSceneHoverEvent *event) {
  self->BoxWhiskers::hoverEnterEvent(event);
}

//  void BoxWhiskers::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    BoxWhiskers *self,
    QGraphicsSceneHoverEvent *event) {
  self->BoxWhiskers::hoverLeaveEvent(event);
}

//  void BoxWhiskers::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->BoxWhiskers::mouseReleaseEvent(event);
}

//  void BoxWhiskers::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    BoxWhiskers *self,
    QGraphicsSceneMouseEvent *event) {
  self->BoxWhiskers::mouseDoubleClickEvent(event);
}

//  QRectF BoxWhiskers::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK11BoxWhiskers12boundingRectEv(
    const BoxWhiskers *self) {
  return new QRectF(self->BoxWhiskers::boundingRect());
}

//  void BoxWhiskers::paint(QPainter *painter, const QStyleOptionGraphicsItem
//      *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11BoxWhiskers5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    BoxWhiskers *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->BoxWhiskers::paint(painter, option, widget);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
