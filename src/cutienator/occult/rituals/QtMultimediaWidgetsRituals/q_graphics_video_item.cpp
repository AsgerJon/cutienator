//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaWidgets/qgraphicsvideoitem.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtMultimediaWidgets/qtmultimediawidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtMultimediaWidgets/qgraphicsvideoitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <cstring>

//  Only a class built on QGraphicsVideoItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsVideoItem : QGraphicsVideoItem {
  using QGraphicsVideoItem::timerEvent;
  using QGraphicsVideoItem::itemChange;
};

//  A QGraphicsVideoItem that Python can take functions over in. Every QGraphicsVideoItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQGraphicsVideoItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsVideoItemCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall3)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsVideoItemCall4)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall5)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsVideoItemCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsVideoItemCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsVideoItemCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsVideoItemCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsVideoItemCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall11)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsVideoItemCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall13)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall14)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall15)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall16)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsVideoItemCall17)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall18)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsVideoItemCall19)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall20)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall21)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall22)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall23)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall24)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall25)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall26)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall27)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall28)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall29)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall30)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall31)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall32)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall33)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall34)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall35)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall36)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsVideoItemCall37)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsVideoItemCall38)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsVideoItemCall39)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsVideoItem : public QGraphicsVideoItem {
public:
  using QGraphicsVideoItem::QGraphicsVideoItem;
  void *taken[40] = {};

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
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
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
  //  QRectF QGraphicsVideoItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall0 call = reinterpret_cast<CuteQGraphicsVideoItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsVideoItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsVideoItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall1 call = reinterpret_cast<CuteQGraphicsVideoItemCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsVideoItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsVideoItem::type() const
  int type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall2 call = reinterpret_cast<CuteQGraphicsVideoItemCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsVideoItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsVideoItem::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall3 call = reinterpret_cast<CuteQGraphicsVideoItemCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsVideoItem::timerEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsVideoItem::itemChange(GraphicsItemChange change,
  //      const QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall4 call = reinterpret_cast<CuteQGraphicsVideoItemCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsVideoItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall5 call = reinterpret_cast<CuteQGraphicsVideoItemCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall6 call = reinterpret_cast<CuteQGraphicsVideoItemCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall7 call = reinterpret_cast<CuteQGraphicsVideoItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall8 call = reinterpret_cast<CuteQGraphicsVideoItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall9 call = reinterpret_cast<CuteQGraphicsVideoItemCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall10 call = reinterpret_cast<CuteQGraphicsVideoItemCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall11 call = reinterpret_cast<CuteQGraphicsVideoItemCall11>(taken[11]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall12 call = reinterpret_cast<CuteQGraphicsVideoItemCall12>(taken[12]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall13 call = reinterpret_cast<CuteQGraphicsVideoItemCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall14 call = reinterpret_cast<CuteQGraphicsVideoItemCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall15 call = reinterpret_cast<CuteQGraphicsVideoItemCall15>(taken[15]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall16 call = reinterpret_cast<CuteQGraphicsVideoItemCall16>(taken[16]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall17 call = reinterpret_cast<CuteQGraphicsVideoItemCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall18 call = reinterpret_cast<CuteQGraphicsVideoItemCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall19 call = reinterpret_cast<CuteQGraphicsVideoItemCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall20 call = reinterpret_cast<CuteQGraphicsVideoItemCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall21 call = reinterpret_cast<CuteQGraphicsVideoItemCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall22 call = reinterpret_cast<CuteQGraphicsVideoItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall23 call = reinterpret_cast<CuteQGraphicsVideoItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall24 call = reinterpret_cast<CuteQGraphicsVideoItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall25 call = reinterpret_cast<CuteQGraphicsVideoItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall26 call = reinterpret_cast<CuteQGraphicsVideoItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall27 call = reinterpret_cast<CuteQGraphicsVideoItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall28 call = reinterpret_cast<CuteQGraphicsVideoItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall29 call = reinterpret_cast<CuteQGraphicsVideoItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall30 call = reinterpret_cast<CuteQGraphicsVideoItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall31 call = reinterpret_cast<CuteQGraphicsVideoItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall32 call = reinterpret_cast<CuteQGraphicsVideoItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall33 call = reinterpret_cast<CuteQGraphicsVideoItemCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall34 call = reinterpret_cast<CuteQGraphicsVideoItemCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall35 call = reinterpret_cast<CuteQGraphicsVideoItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall36 call = reinterpret_cast<CuteQGraphicsVideoItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall37 call = reinterpret_cast<CuteQGraphicsVideoItemCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall38 call = reinterpret_cast<CuteQGraphicsVideoItemCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphicsVideoItemCall39 call = reinterpret_cast<CuteQGraphicsVideoItemCall39>(taken[39]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *QGraphicsVideoItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QGraphicsVideoItem10metaObjectEv(
    const QGraphicsVideoItem *self) {
  return self->metaObject();
}

//  void *QGraphicsVideoItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QGraphicsVideoItem11qt_metacastEPKc(
    QGraphicsVideoItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphicsVideoItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGraphicsVideoItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphicsVideoItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGraphicsVideoItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QGraphicsVideoItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsVideoItem::tr(s, c, n));
}

//  QGraphicsVideoItem::QGraphicsVideoItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsVideoItem *ritual_ZN18QGraphicsVideoItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsVideoItem(parent);
}

//  QGraphicsVideoItem::~QGraphicsVideoItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItemD1Ev(QGraphicsVideoItem *self) {
  delete self;
}

//  QVideoSink *QGraphicsVideoItem::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK18QGraphicsVideoItem9videoSinkEv(
    const QGraphicsVideoItem *self) {
  return self->videoSink();
}

//  Qt::AspectRatioMode QGraphicsVideoItem::aspectRatioMode() const
extern "C" Q_DECL_EXPORT
Qt::AspectRatioMode ritual_ZNK18QGraphicsVideoItem15aspectRatioModeEv(
    const QGraphicsVideoItem *self) {
  return self->aspectRatioMode();
}

//  void QGraphicsVideoItem::setAspectRatioMode(Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QGraphicsVideoItem *self,
    Qt::AspectRatioMode mode) {
  self->setAspectRatioMode(mode);
}

//  QPointF QGraphicsVideoItem::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QGraphicsVideoItem6offsetEv(
    const QGraphicsVideoItem *self) {
  return new QPointF(self->offset());
}

//  void QGraphicsVideoItem::setOffset(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem9setOffsetERK7QPointF(
    QGraphicsVideoItem *self,
    const QPointF *offset) {
  self->setOffset(*offset);
}

//  QSizeF QGraphicsVideoItem::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18QGraphicsVideoItem4sizeEv(
    const QGraphicsVideoItem *self) {
  return new QSizeF(self->size());
}

//  void QGraphicsVideoItem::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem7setSizeERK6QSizeF(
    QGraphicsVideoItem *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  QSizeF QGraphicsVideoItem::nativeSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18QGraphicsVideoItem10nativeSizeEv(
    const QGraphicsVideoItem *self) {
  return new QSizeF(self->nativeSize());
}

//  QRectF QGraphicsVideoItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QGraphicsVideoItem12boundingRectEv(
    const QGraphicsVideoItem *self) {
  return new QRectF(self->boundingRect());
}

//  void QGraphicsVideoItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsVideoItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  int QGraphicsVideoItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGraphicsVideoItem4typeEv(const QGraphicsVideoItem *self) {
  return self->type();
}

//  void QGraphicsVideoItem::nativeSizeChanged(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem17nativeSizeChangedERK6QSizeF(
    QGraphicsVideoItem *self,
    const QSizeF *size) {
  self->nativeSizeChanged(*size);
}

//  void QGraphicsVideoItem::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsVideoItem10timerEventEP11QTimerEvent(
    QGraphicsVideoItem *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QVariant QGraphicsVideoItem::itemChange(GraphicsItemChange change, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18QGraphicsVideoItem10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsVideoItem *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(self->itemChange(change, *value));
}

//  QGraphicsVideoItemPrivate *QGraphicsVideoItem::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsVideoItemPrivate *ritual_ZN18QGraphicsVideoItem6d_funcEv(
    QGraphicsVideoItem *self) {
  return self->d_func();
}

//  const QGraphicsVideoItemPrivate *QGraphicsVideoItem::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsVideoItemPrivate *ritual_ZNK18QGraphicsVideoItem6d_funcEv(
    const QGraphicsVideoItem *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsVideoItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsVideoItem(
    QGraphicsVideoItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsVideoItem *>(self)->take(key, call);
}

//  QRectF QGraphicsVideoItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK18QGraphicsVideoItem12boundingRectEv(
    const QGraphicsVideoItem *self) {
  return new QRectF(self->QGraphicsVideoItem::boundingRect());
}

//  void QGraphicsVideoItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGraphicsVideoItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsVideoItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsVideoItem::paint(painter, option, widget);
}

//  int QGraphicsVideoItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QGraphicsVideoItem4typeEv(
    const QGraphicsVideoItem *self) {
  return self->QGraphicsVideoItem::type();
}

//  void QGraphicsVideoItem::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGraphicsVideoItem10timerEventEP11QTimerEvent(
    QGraphicsVideoItem *self,
    QTimerEvent *event) {
  static_cast<OwnQGraphicsVideoItem *>(self)->OwnQGraphicsVideoItem::timerEvent(
      event);
}

//  QVariant QGraphicsVideoItem::itemChange(GraphicsItemChange change, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN18QGraphicsVideoItem10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsVideoItem *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(
      static_cast<OwnQGraphicsVideoItem *>(self)->OwnQGraphicsVideoItem::itemChange(
          change,
          *value));
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
