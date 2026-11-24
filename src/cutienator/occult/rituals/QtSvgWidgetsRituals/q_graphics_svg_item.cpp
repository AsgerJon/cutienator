//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvgWidgets/qgraphicssvgitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtSvgWidgets/qtsvgwidgetsglobal.h>
#if !defined(QT_NO_GRAPHICSVIEW)
#include <QtSvgWidgets/qgraphicssvgitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QGraphicsSvgItem that Python can take functions over in. Every QGraphicsSvgItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
typedef const QRectF * (*CuteQGraphicsSvgItemCall0)(const void *, int *);
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
typedef void (*CuteQGraphicsSvgItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
typedef int (*CuteQGraphicsSvgItemCall2)(const void *, int *);
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsSvgItemCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSvgItemCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSvgItemCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSvgItemCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSvgItemCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSvgItemCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall10)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsSvgItemCall11)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall12)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall13)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall14)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall15)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsSvgItemCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall17)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSvgItemCall18)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall19)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall20)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall21)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall22)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall23)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall24)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall25)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall27)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall28)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall29)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall30)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall31)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall32)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall33)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall34)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall35)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSvgItemCall36)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsSvgItemCall37)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsSvgItemCall38)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsSvgItemCall39)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsSvgItem : public QGraphicsSvgItem {
public:
  using QGraphicsSvgItem::QGraphicsSvgItem;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
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
#if !defined(QT_NO_GRAPHICSVIEW)
  //  QRectF QGraphicsSvgItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall0 call = reinterpret_cast<CuteQGraphicsSvgItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsSvgItem::boundingRect();
  }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
  //  void QGraphicsSvgItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall1 call = reinterpret_cast<CuteQGraphicsSvgItemCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsSvgItem::paint(painter, option, widget);
  }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_GRAPHICSVIEW)
  //  int QGraphicsSvgItem::type() const
  int type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall2 call = reinterpret_cast<CuteQGraphicsSvgItemCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsSvgItem::type();
  }
#endif  // !defined(QT_NO_GRAPHICSVIEW)
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall3 call = reinterpret_cast<CuteQGraphicsSvgItemCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall4 call = reinterpret_cast<CuteQGraphicsSvgItemCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall5 call = reinterpret_cast<CuteQGraphicsSvgItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall6 call = reinterpret_cast<CuteQGraphicsSvgItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall7 call = reinterpret_cast<CuteQGraphicsSvgItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall8 call = reinterpret_cast<CuteQGraphicsSvgItemCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall9 call = reinterpret_cast<CuteQGraphicsSvgItemCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall10 call = reinterpret_cast<CuteQGraphicsSvgItemCall10>(taken[10]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall11 call = reinterpret_cast<CuteQGraphicsSvgItemCall11>(taken[11]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall12 call = reinterpret_cast<CuteQGraphicsSvgItemCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall13 call = reinterpret_cast<CuteQGraphicsSvgItemCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall14 call = reinterpret_cast<CuteQGraphicsSvgItemCall14>(taken[14]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall15 call = reinterpret_cast<CuteQGraphicsSvgItemCall15>(taken[15]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall16 call = reinterpret_cast<CuteQGraphicsSvgItemCall16>(taken[16]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall17 call = reinterpret_cast<CuteQGraphicsSvgItemCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall18 call = reinterpret_cast<CuteQGraphicsSvgItemCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall19 call = reinterpret_cast<CuteQGraphicsSvgItemCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall20 call = reinterpret_cast<CuteQGraphicsSvgItemCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall21 call = reinterpret_cast<CuteQGraphicsSvgItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall22 call = reinterpret_cast<CuteQGraphicsSvgItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall23 call = reinterpret_cast<CuteQGraphicsSvgItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall24 call = reinterpret_cast<CuteQGraphicsSvgItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall25 call = reinterpret_cast<CuteQGraphicsSvgItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall26 call = reinterpret_cast<CuteQGraphicsSvgItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall27 call = reinterpret_cast<CuteQGraphicsSvgItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall28 call = reinterpret_cast<CuteQGraphicsSvgItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall29 call = reinterpret_cast<CuteQGraphicsSvgItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall30 call = reinterpret_cast<CuteQGraphicsSvgItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall31 call = reinterpret_cast<CuteQGraphicsSvgItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall32 call = reinterpret_cast<CuteQGraphicsSvgItemCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall33 call = reinterpret_cast<CuteQGraphicsSvgItemCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall34 call = reinterpret_cast<CuteQGraphicsSvgItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsSvgItemCall35 call = reinterpret_cast<CuteQGraphicsSvgItemCall35>(taken[35]);
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
      CuteQGraphicsSvgItemCall36 call = reinterpret_cast<CuteQGraphicsSvgItemCall36>(taken[36]);
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
      CuteQGraphicsSvgItemCall37 call = reinterpret_cast<CuteQGraphicsSvgItemCall37>(taken[37]);
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
      CuteQGraphicsSvgItemCall38 call = reinterpret_cast<CuteQGraphicsSvgItemCall38>(taken[38]);
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
      CuteQGraphicsSvgItemCall39 call = reinterpret_cast<CuteQGraphicsSvgItemCall39>(taken[39]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *QGraphicsSvgItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QGraphicsSvgItem10metaObjectEv(
    const QGraphicsSvgItem *self) {
  return self->metaObject();
}

//  QString QGraphicsSvgItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QGraphicsSvgItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsSvgItem::tr(s, c, n));
}

//  QGraphicsSvgItem::QGraphicsSvgItem(QGraphicsItem *parentItem)
extern "C" Q_DECL_EXPORT
QGraphicsSvgItem *ritual_ZN16QGraphicsSvgItemC1EP13QGraphicsItem(
    QGraphicsItem *parentItem) {
  return new CuteQGraphicsSvgItem(parentItem);
}

//  QGraphicsSvgItem::QGraphicsSvgItem(const QString &fileName, QGraphicsItem
//      *parentItem)
extern "C" Q_DECL_EXPORT
QGraphicsSvgItem *ritual_ZN16QGraphicsSvgItemC1ERK7QStringP13QGraphicsItem(
    const QString *fileName,
    QGraphicsItem *parentItem) {
  return new CuteQGraphicsSvgItem(*fileName, parentItem);
}

//  QGraphicsSvgItem::~QGraphicsSvgItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItemD1Ev(QGraphicsSvgItem *self) {
  delete self;
}

//  void QGraphicsSvgItem::setSharedRenderer(QSvgRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItem17setSharedRendererEP12QSvgRenderer(
    QGraphicsSvgItem *self,
    QSvgRenderer *renderer) {
  self->setSharedRenderer(renderer);
}

//  QSvgRenderer *QGraphicsSvgItem::renderer() const
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZNK16QGraphicsSvgItem8rendererEv(
    const QGraphicsSvgItem *self) {
  return self->renderer();
}

//  void QGraphicsSvgItem::setElementId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItem12setElementIdERK7QString(
    QGraphicsSvgItem *self,
    const QString *id) {
  self->setElementId(*id);
}

//  QString QGraphicsSvgItem::elementId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QGraphicsSvgItem9elementIdEv(
    const QGraphicsSvgItem *self) {
  return new QString(self->elementId());
}

//  void QGraphicsSvgItem::setCachingEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItem17setCachingEnabledEb(
    QGraphicsSvgItem *self,
    bool a0) {
  self->setCachingEnabled(a0);
}

//  bool QGraphicsSvgItem::isCachingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGraphicsSvgItem16isCachingEnabledEv(
    const QGraphicsSvgItem *self) {
  return self->isCachingEnabled();
}

//  void QGraphicsSvgItem::setMaximumCacheSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItem19setMaximumCacheSizeERK5QSize(
    QGraphicsSvgItem *self,
    const QSize *size) {
  self->setMaximumCacheSize(*size);
}

//  QSize QGraphicsSvgItem::maximumCacheSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QGraphicsSvgItem16maximumCacheSizeEv(
    const QGraphicsSvgItem *self) {
  return new QSize(self->maximumCacheSize());
}

//  QRectF QGraphicsSvgItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QGraphicsSvgItem12boundingRectEv(
    const QGraphicsSvgItem *self) {
  return new QRectF(self->boundingRect());
}

//  void QGraphicsSvgItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphicsSvgItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsSvgItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  int QGraphicsSvgItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGraphicsSvgItem4typeEv(const QGraphicsSvgItem *self) {
  return self->type();
}

//  a Python function taken by a CuteQGraphicsSvgItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSvgItem(
    QGraphicsSvgItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSvgItem *>(self)->take(key, call);
}

//  QRectF QGraphicsSvgItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK16QGraphicsSvgItem12boundingRectEv(
    const QGraphicsSvgItem *self) {
  return new QRectF(self->QGraphicsSvgItem::boundingRect());
}

//  void QGraphicsSvgItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QGraphicsSvgItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsSvgItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsSvgItem::paint(painter, option, widget);
}

//  int QGraphicsSvgItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QGraphicsSvgItem4typeEv(const QGraphicsSvgItem *self) {
  return self->QGraphicsSvgItem::type();
}

#endif  // !defined(QT_NO_GRAPHICSVIEW)
