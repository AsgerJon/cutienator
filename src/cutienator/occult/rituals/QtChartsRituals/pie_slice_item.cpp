//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/piesliceitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/piesliceitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/pieslicedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A PieSliceItem that Python can take functions over in. Every PieSliceItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CutePieSliceItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePieSliceItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall3)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall4)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall5)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall6)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall7)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePieSliceItemCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceItemCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceItemCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceItemCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceItemCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceItemCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall15)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall16)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall17)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall18)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall19)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePieSliceItemCall20)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CutePieSliceItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall22)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePieSliceItemCall23)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall24)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall25)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall26)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall27)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall28)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall29)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall30)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall31)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall32)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall33)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall34)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall35)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePieSliceItemCall36)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieSliceItemCall37)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieSliceItemCall38)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePieSliceItemCall39)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CutePieSliceItem : public PieSliceItem {
public:
  using PieSliceItem::PieSliceItem;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
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
  //  QRectF PieSliceItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CutePieSliceItemCall0 call = reinterpret_cast<CutePieSliceItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return PieSliceItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath PieSliceItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CutePieSliceItemCall1 call = reinterpret_cast<CutePieSliceItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return PieSliceItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      CutePieSliceItemCall2 call = reinterpret_cast<CutePieSliceItemCall2>(taken[2]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    PieSliceItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CutePieSliceItemCall3 call = reinterpret_cast<CutePieSliceItemCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieSliceItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CutePieSliceItemCall4 call = reinterpret_cast<CutePieSliceItemCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieSliceItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CutePieSliceItemCall5 call = reinterpret_cast<CutePieSliceItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieSliceItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CutePieSliceItemCall6 call = reinterpret_cast<CutePieSliceItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieSliceItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void PieSliceItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CutePieSliceItemCall7 call = reinterpret_cast<CutePieSliceItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    PieSliceItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[8]) {
      int handled = 0;
      CutePieSliceItemCall8 call = reinterpret_cast<CutePieSliceItemCall8>(taken[8]);
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
      CutePieSliceItemCall9 call = reinterpret_cast<CutePieSliceItemCall9>(taken[9]);
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
      CutePieSliceItemCall10 call = reinterpret_cast<CutePieSliceItemCall10>(taken[10]);
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
      CutePieSliceItemCall11 call = reinterpret_cast<CutePieSliceItemCall11>(taken[11]);
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
      CutePieSliceItemCall12 call = reinterpret_cast<CutePieSliceItemCall12>(taken[12]);
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
      CutePieSliceItemCall13 call = reinterpret_cast<CutePieSliceItemCall13>(taken[13]);
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
      CutePieSliceItemCall14 call = reinterpret_cast<CutePieSliceItemCall14>(taken[14]);
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
      CutePieSliceItemCall15 call = reinterpret_cast<CutePieSliceItemCall15>(taken[15]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[16]) {
      int handled = 0;
      CutePieSliceItemCall16 call = reinterpret_cast<CutePieSliceItemCall16>(taken[16]);
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
      CutePieSliceItemCall17 call = reinterpret_cast<CutePieSliceItemCall17>(taken[17]);
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
      CutePieSliceItemCall18 call = reinterpret_cast<CutePieSliceItemCall18>(taken[18]);
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
      CutePieSliceItemCall19 call = reinterpret_cast<CutePieSliceItemCall19>(taken[19]);
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
      CutePieSliceItemCall20 call = reinterpret_cast<CutePieSliceItemCall20>(taken[20]);
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
      CutePieSliceItemCall21 call = reinterpret_cast<CutePieSliceItemCall21>(taken[21]);
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
      CutePieSliceItemCall22 call = reinterpret_cast<CutePieSliceItemCall22>(taken[22]);
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
      CutePieSliceItemCall23 call = reinterpret_cast<CutePieSliceItemCall23>(taken[23]);
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
      CutePieSliceItemCall24 call = reinterpret_cast<CutePieSliceItemCall24>(taken[24]);
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
      CutePieSliceItemCall25 call = reinterpret_cast<CutePieSliceItemCall25>(taken[25]);
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
      CutePieSliceItemCall26 call = reinterpret_cast<CutePieSliceItemCall26>(taken[26]);
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
      CutePieSliceItemCall27 call = reinterpret_cast<CutePieSliceItemCall27>(taken[27]);
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
      CutePieSliceItemCall28 call = reinterpret_cast<CutePieSliceItemCall28>(taken[28]);
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
      CutePieSliceItemCall29 call = reinterpret_cast<CutePieSliceItemCall29>(taken[29]);
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
      CutePieSliceItemCall30 call = reinterpret_cast<CutePieSliceItemCall30>(taken[30]);
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
      CutePieSliceItemCall31 call = reinterpret_cast<CutePieSliceItemCall31>(taken[31]);
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
      CutePieSliceItemCall32 call = reinterpret_cast<CutePieSliceItemCall32>(taken[32]);
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
      CutePieSliceItemCall33 call = reinterpret_cast<CutePieSliceItemCall33>(taken[33]);
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
      CutePieSliceItemCall34 call = reinterpret_cast<CutePieSliceItemCall34>(taken[34]);
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
      CutePieSliceItemCall35 call = reinterpret_cast<CutePieSliceItemCall35>(taken[35]);
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
      CutePieSliceItemCall36 call = reinterpret_cast<CutePieSliceItemCall36>(taken[36]);
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
      CutePieSliceItemCall37 call = reinterpret_cast<CutePieSliceItemCall37>(taken[37]);
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
      CutePieSliceItemCall38 call = reinterpret_cast<CutePieSliceItemCall38>(taken[38]);
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
      CutePieSliceItemCall39 call = reinterpret_cast<CutePieSliceItemCall39>(taken[39]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *PieSliceItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12PieSliceItem10metaObjectEv(
    const PieSliceItem *self) {
  return self->metaObject();
}

//  QString PieSliceItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12PieSliceItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PieSliceItem::tr(s, c, n));
}

//  PieSliceItem::PieSliceItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
PieSliceItem *ritual_ZN12PieSliceItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CutePieSliceItem(parent);
}

//  PieSliceItem::~PieSliceItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItemD1Ev(PieSliceItem *self) {
  delete self;
}

//  QRectF PieSliceItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12PieSliceItem12boundingRectEv(const PieSliceItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath PieSliceItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12PieSliceItem5shapeEv(const PieSliceItem *self) {
  return new QPainterPath(self->shape());
}

//  void PieSliceItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    PieSliceItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void PieSliceItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    PieSliceItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void PieSliceItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    PieSliceItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void PieSliceItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void PieSliceItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void PieSliceItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void PieSliceItem::setLayout(const PieSliceData &sliceData)
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem9setLayoutERK12PieSliceData(
    PieSliceItem *self,
    const PieSliceData *sliceData) {
  self->setLayout(*sliceData);
}

//  QPointF PieSliceItem::sliceCenter(QPointF point, qreal radius, QPieSlice
//      *slice)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12PieSliceItem11sliceCenterE7QPointFdP9QPieSlice(
    const QPointF *point,
    qreal radius,
    QPieSlice *slice) {
  return new QPointF(PieSliceItem::sliceCenter(*point, radius, slice));
}

//  void PieSliceItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceItem14updateGeometryEv(PieSliceItem *self) {
  self->updateGeometry();
}

//  QPainterPath PieSliceItem::slicePath(QPointF center, qreal radius, qreal
//      startAngle, qreal angleSpan, qreal *centerAngle, QPointF *armStart)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12PieSliceItem9slicePathE7QPointFdddPdPS0_(
    PieSliceItem *self,
    const QPointF *center,
    qreal radius,
    qreal startAngle,
    qreal angleSpan,
    qreal *centerAngle,
    QPointF *armStart) {
  return new QPainterPath(
      self->slicePath(
          *center,
          radius,
          startAngle,
          angleSpan,
          centerAngle,
          armStart));
}

//  QPainterPath PieSliceItem::labelArmPath(QPointF start, qreal angle, qreal
//      length, qreal textWidth, QPointF *textStart)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12PieSliceItem12labelArmPathE7QPointFdddPS0_(
    PieSliceItem *self,
    const QPointF *start,
    qreal angle,
    qreal length,
    qreal textWidth,
    QPointF *textStart) {
  return new QPainterPath(
      self->labelArmPath(
          *start,
          angle,
          length,
          textWidth,
          textStart));
}

//  a Python function taken by a CutePieSliceItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PieSliceItem(
    PieSliceItem *self,
    const char *key,
    void *call) {
  return static_cast<CutePieSliceItem *>(self)->take(key, call);
}

//  QRectF PieSliceItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK12PieSliceItem12boundingRectEv(
    const PieSliceItem *self) {
  return new QRectF(self->PieSliceItem::boundingRect());
}

//  QPainterPath PieSliceItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK12PieSliceItem5shapeEv(
    const PieSliceItem *self) {
  return new QPainterPath(self->PieSliceItem::shape());
}

//  void PieSliceItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    PieSliceItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->PieSliceItem::paint(painter, option, widget);
}

//  void PieSliceItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    PieSliceItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->PieSliceItem::hoverEnterEvent(event);
}

//  void PieSliceItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    PieSliceItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->PieSliceItem::hoverLeaveEvent(event);
}

//  void PieSliceItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->PieSliceItem::mousePressEvent(event);
}

//  void PieSliceItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->PieSliceItem::mouseReleaseEvent(event);
}

//  void PieSliceItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12PieSliceItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    PieSliceItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->PieSliceItem::mouseDoubleClickEvent(event);
}
