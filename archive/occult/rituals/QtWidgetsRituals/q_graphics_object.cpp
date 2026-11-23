//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QGraphicsObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsObject : QGraphicsObject {
  using QGraphicsObject::event;
};

//  A QGraphicsObject that Python can take functions over in. Every QGraphicsObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGraphicsObjectCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsObjectCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsObjectCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsObjectCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsObjectCall4)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsObjectCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsObjectCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsObjectCall7)(const void *, int, int *);
typedef const QRectF * (*CuteQGraphicsObjectCall8)(const void *, int *);
typedef const QPainterPath * (*CuteQGraphicsObjectCall9)(const void *, int *);
typedef bool (*CuteQGraphicsObjectCall10)(const void *, const QPointF *, int *);
typedef bool (*CuteQGraphicsObjectCall11)(const void *, const QGraphicsItem *, int, int *);
typedef bool (*CuteQGraphicsObjectCall12)(const void *, const QPainterPath *, int, int *);
typedef bool (*CuteQGraphicsObjectCall13)(const void *, const QGraphicsItem *, int *);
typedef const QPainterPath * (*CuteQGraphicsObjectCall14)(const void *, int *);
typedef void (*CuteQGraphicsObjectCall15)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef int (*CuteQGraphicsObjectCall16)(const void *, int *);
typedef bool (*CuteQGraphicsObjectCall17)(const void *, QGraphicsItem *, QEvent *, int *);
typedef bool (*CuteQGraphicsObjectCall18)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsObjectCall19)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsObjectCall20)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsObjectCall21)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsObjectCall22)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsObjectCall23)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsObjectCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsObjectCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsObjectCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsObjectCall27)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsObjectCall28)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsObjectCall29)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsObjectCall30)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsObjectCall31)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsObjectCall32)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsObjectCall33)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsObjectCall34)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsObjectCall35)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef void (*CuteQGraphicsObjectCall36)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQGraphicsObjectCall37)(const void *, int, int *);
typedef const QVariant * (*CuteQGraphicsObjectCall38)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQGraphicsObjectCall39)(const void *, const QVariant *, int *);
class CuteQGraphicsObject : public QGraphicsObject {
public:
  using QGraphicsObject::QGraphicsObject;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[39] = call;
      return true;
    }
    return false;
  }

  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsObjectCall0 call = reinterpret_cast<CuteQGraphicsObjectCall0>(taken[0]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QGraphicsObject::event(ev);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsObjectCall1 call = reinterpret_cast<CuteQGraphicsObjectCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsObjectCall2 call = reinterpret_cast<CuteQGraphicsObjectCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsObjectCall3 call = reinterpret_cast<CuteQGraphicsObjectCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsObjectCall4 call = reinterpret_cast<CuteQGraphicsObjectCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsObjectCall5 call = reinterpret_cast<CuteQGraphicsObjectCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsObjectCall6 call = reinterpret_cast<CuteQGraphicsObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsObjectCall7 call = reinterpret_cast<CuteQGraphicsObjectCall7>(taken[7]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }

  //  QRectF QGraphicsItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsObjectCall8 call = reinterpret_cast<CuteQGraphicsObjectCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsObjectCall9 call = reinterpret_cast<CuteQGraphicsObjectCall9>(taken[9]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }

  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsObjectCall10 call = reinterpret_cast<CuteQGraphicsObjectCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::contains(point);
  }

  //  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithItem(
      const QGraphicsItem *other,
      Qt::ItemSelectionMode mode) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsObjectCall11 call = reinterpret_cast<CuteQGraphicsObjectCall11>(taken[11]);
      bool given = call(this, other, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithItem(other, mode);
  }

  //  bool QGraphicsItem::collidesWithPath(const QPainterPath &path,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithPath(
      const QPainterPath &path,
      Qt::ItemSelectionMode mode) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsObjectCall12 call = reinterpret_cast<CuteQGraphicsObjectCall12>(taken[12]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }

  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsObjectCall13 call = reinterpret_cast<CuteQGraphicsObjectCall13>(taken[13]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }

  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsObjectCall14 call = reinterpret_cast<CuteQGraphicsObjectCall14>(taken[14]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }

  //  void QGraphicsItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsObjectCall15 call = reinterpret_cast<CuteQGraphicsObjectCall15>(taken[15]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
  }

  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsObjectCall16 call = reinterpret_cast<CuteQGraphicsObjectCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::type();
  }

  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsObjectCall17 call = reinterpret_cast<CuteQGraphicsObjectCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }

  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsObjectCall18 call = reinterpret_cast<CuteQGraphicsObjectCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEvent(event);
  }

  //  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsObjectCall19 call = reinterpret_cast<CuteQGraphicsObjectCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::contextMenuEvent(event);
  }

  //  void QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsObjectCall20 call = reinterpret_cast<CuteQGraphicsObjectCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragEnterEvent(event);
  }

  //  void QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsObjectCall21 call = reinterpret_cast<CuteQGraphicsObjectCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }

  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsObjectCall22 call = reinterpret_cast<CuteQGraphicsObjectCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }

  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsObjectCall23 call = reinterpret_cast<CuteQGraphicsObjectCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }

  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsObjectCall24 call = reinterpret_cast<CuteQGraphicsObjectCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }

  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsObjectCall25 call = reinterpret_cast<CuteQGraphicsObjectCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }

  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsObjectCall26 call = reinterpret_cast<CuteQGraphicsObjectCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }

  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsObjectCall27 call = reinterpret_cast<CuteQGraphicsObjectCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }

  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsObjectCall28 call = reinterpret_cast<CuteQGraphicsObjectCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }

  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsObjectCall29 call = reinterpret_cast<CuteQGraphicsObjectCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }

  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsObjectCall30 call = reinterpret_cast<CuteQGraphicsObjectCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }

  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsObjectCall31 call = reinterpret_cast<CuteQGraphicsObjectCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }

  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsObjectCall32 call = reinterpret_cast<CuteQGraphicsObjectCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }

  //  void QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsObjectCall33 call = reinterpret_cast<CuteQGraphicsObjectCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseReleaseEvent(event);
  }

  //  void QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsObjectCall34 call = reinterpret_cast<CuteQGraphicsObjectCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsObjectCall35 call = reinterpret_cast<CuteQGraphicsObjectCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }

  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQGraphicsObjectCall36 call = reinterpret_cast<CuteQGraphicsObjectCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::inputMethodEvent(event);
  }

  //  QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphicsObjectCall37 call = reinterpret_cast<CuteQGraphicsObjectCall37>(taken[37]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::inputMethodQuery(query);
  }

  //  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[38]) {
      int handled = 0;
      CuteQGraphicsObjectCall38 call = reinterpret_cast<CuteQGraphicsObjectCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }

  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphicsObjectCall39 call = reinterpret_cast<CuteQGraphicsObjectCall39>(taken[39]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
};

//  const QMetaObject *QGraphicsObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsObject10metaObjectEv(
    const QGraphicsObject *self) {
  return self->metaObject();
}

//  QString QGraphicsObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsObject::tr(s, c, n));
}

//  QGraphicsObject::~QGraphicsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObjectD1Ev(QGraphicsObject *self) {
  delete self;
}

//  void QGraphicsObject::grabGesture(Qt::GestureType type, Qt::GestureFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObject11grabGestureEN2Qt11GestureTypeE6QFlagsINS0_11GestureFlagEE(
    QGraphicsObject *self,
    Qt::GestureType type,
    int flags) {
  self->grabGesture(type, QFlags<Qt::GestureFlag>::fromInt(flags));
}

//  void QGraphicsObject::ungrabGesture(Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObject13ungrabGestureEN2Qt11GestureTypeE(
    QGraphicsObject *self,
    Qt::GestureType type) {
  self->ungrabGesture(type);
}

//  void QGraphicsObject::updateMicroFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsObject16updateMicroFocusEv(QGraphicsObject *self) {
  self->updateMicroFocus();
}

//  bool QGraphicsObject::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsObject5eventEP6QEvent(
    QGraphicsObject *self,
    QEvent *ev) {
  return self->event(ev);
}

//  QGraphicsObject as the QGraphicsItem it is built on
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_cast_QGraphicsObject_QGraphicsItem(
    QGraphicsObject *self) {
  return static_cast<QGraphicsItem *>(self);
}

//  a Python function taken by a CuteQGraphicsObject, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsObject(
    QGraphicsObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsObject *>(self)->take(key, call);
}

//  bool QGraphicsObject::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGraphicsObject5eventEP6QEvent(
    QGraphicsObject *self,
    QEvent *ev) {
  return static_cast<OwnQGraphicsObject *>(self)->OwnQGraphicsObject::event(
      ev);
}
