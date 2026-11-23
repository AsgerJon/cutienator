//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsTextItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsTextItem : QGraphicsTextItem {
  using QGraphicsTextItem::sceneEvent;
  using QGraphicsTextItem::mousePressEvent;
  using QGraphicsTextItem::mouseMoveEvent;
  using QGraphicsTextItem::mouseReleaseEvent;
  using QGraphicsTextItem::mouseDoubleClickEvent;
  using QGraphicsTextItem::contextMenuEvent;
  using QGraphicsTextItem::keyPressEvent;
  using QGraphicsTextItem::keyReleaseEvent;
  using QGraphicsTextItem::focusInEvent;
  using QGraphicsTextItem::focusOutEvent;
  using QGraphicsTextItem::dragEnterEvent;
  using QGraphicsTextItem::dragLeaveEvent;
  using QGraphicsTextItem::dragMoveEvent;
  using QGraphicsTextItem::dropEvent;
  using QGraphicsTextItem::inputMethodEvent;
  using QGraphicsTextItem::hoverEnterEvent;
  using QGraphicsTextItem::hoverMoveEvent;
  using QGraphicsTextItem::hoverLeaveEvent;
  using QGraphicsTextItem::inputMethodQuery;
  using QGraphicsTextItem::extension;
};

//  A QGraphicsTextItem that Python can take functions over in. Every QGraphicsTextItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQGraphicsTextItemCall0)(const void *, int *);
typedef const QPainterPath * (*CuteQGraphicsTextItemCall1)(const void *, int *);
typedef bool (*CuteQGraphicsTextItemCall2)(const void *, const QPointF *, int *);
typedef void (*CuteQGraphicsTextItemCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef bool (*CuteQGraphicsTextItemCall4)(const void *, const QGraphicsItem *, int *);
typedef const QPainterPath * (*CuteQGraphicsTextItemCall5)(const void *, int *);
typedef int (*CuteQGraphicsTextItemCall6)(const void *, int *);
typedef bool (*CuteQGraphicsTextItemCall7)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall8)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall9)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall10)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall11)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall12)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall17)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall18)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall19)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall20)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall21)(const void *, QInputMethodEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall22)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall23)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall24)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef const QVariant * (*CuteQGraphicsTextItemCall25)(const void *, int, int *);
typedef const QVariant * (*CuteQGraphicsTextItemCall26)(const void *, const QVariant *, int *);
typedef bool (*CuteQGraphicsTextItemCall27)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsTextItemCall28)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall29)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall30)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall31)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall32)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsTextItemCall33)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsTextItemCall34)(const void *, int, int *);
typedef bool (*CuteQGraphicsTextItemCall35)(const void *, const QGraphicsItem *, int, int *);
typedef bool (*CuteQGraphicsTextItemCall36)(const void *, const QPainterPath *, int, int *);
typedef bool (*CuteQGraphicsTextItemCall37)(const void *, QGraphicsItem *, QEvent *, int *);
typedef void (*CuteQGraphicsTextItemCall38)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef const QVariant * (*CuteQGraphicsTextItemCall39)(const void *, int, const QVariant *, int *);
class CuteQGraphicsTextItem : public QGraphicsTextItem {
public:
  using QGraphicsTextItem::QGraphicsTextItem;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[39] = call;
      return true;
    }
    return false;
  }

  //  QRectF QGraphicsTextItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsTextItemCall0 call = reinterpret_cast<CuteQGraphicsTextItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::boundingRect();
  }

  //  QPainterPath QGraphicsTextItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsTextItemCall1 call = reinterpret_cast<CuteQGraphicsTextItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::shape();
  }

  //  bool QGraphicsTextItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsTextItemCall2 call = reinterpret_cast<CuteQGraphicsTextItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::contains(point);
  }

  //  void QGraphicsTextItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsTextItemCall3 call = reinterpret_cast<CuteQGraphicsTextItemCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::paint(painter, option, widget);
  }

  //  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsTextItemCall4 call = reinterpret_cast<CuteQGraphicsTextItemCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::isObscuredBy(item);
  }

  //  QPainterPath QGraphicsTextItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsTextItemCall5 call = reinterpret_cast<CuteQGraphicsTextItemCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::opaqueArea();
  }

  //  int QGraphicsTextItem::type() const
  int type() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsTextItemCall6 call = reinterpret_cast<CuteQGraphicsTextItemCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::type();
  }

  //  bool QGraphicsTextItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsTextItemCall7 call = reinterpret_cast<CuteQGraphicsTextItemCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::sceneEvent(event);
  }

  //  void QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsTextItemCall8 call = reinterpret_cast<CuteQGraphicsTextItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mousePressEvent(event);
  }

  //  void QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsTextItemCall9 call = reinterpret_cast<CuteQGraphicsTextItemCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseMoveEvent(event);
  }

  //  void QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsTextItemCall10 call = reinterpret_cast<CuteQGraphicsTextItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseReleaseEvent(event);
  }

  //  void
  //      QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsTextItemCall11 call = reinterpret_cast<CuteQGraphicsTextItemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseDoubleClickEvent(event);
  }

  //  void
  //      QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEven
  //      t *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsTextItemCall12 call = reinterpret_cast<CuteQGraphicsTextItemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::contextMenuEvent(event);
  }

  //  void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsTextItemCall13 call = reinterpret_cast<CuteQGraphicsTextItemCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::keyPressEvent(event);
  }

  //  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsTextItemCall14 call = reinterpret_cast<CuteQGraphicsTextItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::keyReleaseEvent(event);
  }

  //  void QGraphicsTextItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsTextItemCall15 call = reinterpret_cast<CuteQGraphicsTextItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::focusInEvent(event);
  }

  //  void QGraphicsTextItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsTextItemCall16 call = reinterpret_cast<CuteQGraphicsTextItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::focusOutEvent(event);
  }

  //  void QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsTextItemCall17 call = reinterpret_cast<CuteQGraphicsTextItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragEnterEvent(event);
  }

  //  void QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsTextItemCall18 call = reinterpret_cast<CuteQGraphicsTextItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragLeaveEvent(event);
  }

  //  void QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsTextItemCall19 call = reinterpret_cast<CuteQGraphicsTextItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragMoveEvent(event);
  }

  //  void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsTextItemCall20 call = reinterpret_cast<CuteQGraphicsTextItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dropEvent(event);
  }

  //  void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsTextItemCall21 call = reinterpret_cast<CuteQGraphicsTextItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::inputMethodEvent(event);
  }

  //  void QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsTextItemCall22 call = reinterpret_cast<CuteQGraphicsTextItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverEnterEvent(event);
  }

  //  void QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsTextItemCall23 call = reinterpret_cast<CuteQGraphicsTextItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverMoveEvent(event);
  }

  //  void QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsTextItemCall24 call = reinterpret_cast<CuteQGraphicsTextItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverLeaveEvent(event);
  }

  //  QVariant QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsTextItemCall25 call = reinterpret_cast<CuteQGraphicsTextItemCall25>(taken[25]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::inputMethodQuery(query);
  }

  //  QVariant QGraphicsTextItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsTextItemCall26 call = reinterpret_cast<CuteQGraphicsTextItemCall26>(taken[26]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::extension(variant);
  }

  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsTextItemCall27 call = reinterpret_cast<CuteQGraphicsTextItemCall27>(taken[27]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QGraphicsObject::event(ev);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsTextItemCall28 call = reinterpret_cast<CuteQGraphicsTextItemCall28>(taken[28]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsTextItemCall29 call = reinterpret_cast<CuteQGraphicsTextItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsTextItemCall30 call = reinterpret_cast<CuteQGraphicsTextItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsTextItemCall31 call = reinterpret_cast<CuteQGraphicsTextItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsTextItemCall32 call = reinterpret_cast<CuteQGraphicsTextItemCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsTextItemCall33 call = reinterpret_cast<CuteQGraphicsTextItemCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsTextItemCall34 call = reinterpret_cast<CuteQGraphicsTextItemCall34>(taken[34]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }

  //  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithItem(
      const QGraphicsItem *other,
      Qt::ItemSelectionMode mode) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsTextItemCall35 call = reinterpret_cast<CuteQGraphicsTextItemCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQGraphicsTextItemCall36 call = reinterpret_cast<CuteQGraphicsTextItemCall36>(taken[36]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }

  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphicsTextItemCall37 call = reinterpret_cast<CuteQGraphicsTextItemCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }

  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQGraphicsTextItemCall38 call = reinterpret_cast<CuteQGraphicsTextItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }

  //  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphicsTextItemCall39 call = reinterpret_cast<CuteQGraphicsTextItemCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
};

//  const QMetaObject *QGraphicsTextItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGraphicsTextItem10metaObjectEv(
    const QGraphicsTextItem *self) {
  return self->metaObject();
}

//  QString QGraphicsTextItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGraphicsTextItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsTextItem::tr(s, c, n));
}

//  QGraphicsTextItem::QGraphicsTextItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN17QGraphicsTextItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsTextItem(parent);
}

//  QGraphicsTextItem::QGraphicsTextItem(const QString &text, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN17QGraphicsTextItemC1ERK7QStringP13QGraphicsItem(
    const QString *text,
    QGraphicsItem *parent) {
  return new CuteQGraphicsTextItem(*text, parent);
}

//  QGraphicsTextItem::~QGraphicsTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItemD1Ev(QGraphicsTextItem *self) {
  delete self;
}

//  QString QGraphicsTextItem::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGraphicsTextItem6toHtmlEv(
    const QGraphicsTextItem *self) {
  return new QString(self->toHtml());
}

//  void QGraphicsTextItem::setHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem7setHtmlERK7QString(
    QGraphicsTextItem *self,
    const QString *html) {
  self->setHtml(*html);
}

//  QString QGraphicsTextItem::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGraphicsTextItem11toPlainTextEv(
    const QGraphicsTextItem *self) {
  return new QString(self->toPlainText());
}

//  void QGraphicsTextItem::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12setPlainTextERK7QString(
    QGraphicsTextItem *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  QFont QGraphicsTextItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QGraphicsTextItem4fontEv(const QGraphicsTextItem *self) {
  return new QFont(self->font());
}

//  void QGraphicsTextItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem7setFontERK5QFont(
    QGraphicsTextItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QGraphicsTextItem::setDefaultTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem19setDefaultTextColorERK6QColor(
    QGraphicsTextItem *self,
    const QColor *c) {
  self->setDefaultTextColor(*c);
}

//  QColor QGraphicsTextItem::defaultTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QGraphicsTextItem16defaultTextColorEv(
    const QGraphicsTextItem *self) {
  return new QColor(self->defaultTextColor());
}

//  QRectF QGraphicsTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsTextItem12boundingRectEv(
    const QGraphicsTextItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsTextItem5shapeEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem8containsERK7QPointF(
    const QGraphicsTextItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsTextItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsTextItem10opaqueAreaEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsTextItem4typeEv(const QGraphicsTextItem *self) {
  return self->type();
}

//  void QGraphicsTextItem::setTextWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12setTextWidthEd(
    QGraphicsTextItem *self,
    qreal width) {
  self->setTextWidth(width);
}

//  qreal QGraphicsTextItem::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGraphicsTextItem9textWidthEv(
    const QGraphicsTextItem *self) {
  return self->textWidth();
}

//  void QGraphicsTextItem::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem10adjustSizeEv(QGraphicsTextItem *self) {
  self->adjustSize();
}

//  void QGraphicsTextItem::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem11setDocumentEP13QTextDocument(
    QGraphicsTextItem *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QGraphicsTextItem::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK17QGraphicsTextItem8documentEv(
    const QGraphicsTextItem *self) {
  return self->document();
}

//  void QGraphicsTextItem::setTextInteractionFlags(Qt::TextInteractionFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QGraphicsTextItem *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QGraphicsTextItem::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsTextItem20textInteractionFlagsEv(
    const QGraphicsTextItem *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QGraphicsTextItem::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem18setTabChangesFocusEb(
    QGraphicsTextItem *self,
    bool b) {
  self->setTabChangesFocus(b);
}

//  bool QGraphicsTextItem::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem15tabChangesFocusEv(
    const QGraphicsTextItem *self) {
  return self->tabChangesFocus();
}

//  void QGraphicsTextItem::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem20setOpenExternalLinksEb(
    QGraphicsTextItem *self,
    bool open) {
  self->setOpenExternalLinks(open);
}

//  bool QGraphicsTextItem::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem17openExternalLinksEv(
    const QGraphicsTextItem *self) {
  return self->openExternalLinks();
}

//  void QGraphicsTextItem::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem13setTextCursorERK11QTextCursor(
    QGraphicsTextItem *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QGraphicsTextItem::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK17QGraphicsTextItem10textCursorEv(
    const QGraphicsTextItem *self) {
  return new QTextCursor(self->textCursor());
}

//  bool QGraphicsTextItem::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGraphicsTextItem10sceneEventEP6QEvent(
    QGraphicsTextItem *self,
    QEvent *event) {
  return self->sceneEvent(event);
}

//  void QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem13keyPressEventEP9QKeyEvent(
    QGraphicsTextItem *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem15keyReleaseEventEP9QKeyEvent(
    QGraphicsTextItem *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QGraphicsTextItem::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12focusInEventEP11QFocusEvent(
    QGraphicsTextItem *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QGraphicsTextItem::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem13focusOutEventEP11QFocusEvent(
    QGraphicsTextItem *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragEnterEvent(event);
}

//  void QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragMoveEvent(event);
}

//  void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dropEvent(event);
}

//  void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem16inputMethodEventEP17QInputMethodEvent(
    QGraphicsTextItem *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}

//  void QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  QVariant QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QGraphicsTextItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsTextItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  bool QGraphicsTextItem::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem17supportsExtensionEN13QGraphicsItem9ExtensionE(
    const QGraphicsTextItem *self,
    QGraphicsItem::Extension extension) {
  return self->supportsExtension(extension);
}

//  void QGraphicsTextItem::setExtension(Extension extension, const QVariant
//      &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12setExtensionEN13QGraphicsItem9ExtensionERK8QVariant(
    QGraphicsTextItem *self,
    QGraphicsItem::Extension extension,
    const QVariant *variant) {
  self->setExtension(extension, *variant);
}

//  QVariant QGraphicsTextItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QGraphicsTextItem9extensionERK8QVariant(
    const QGraphicsTextItem *self,
    const QVariant *variant) {
  return new QVariant(self->extension(*variant));
}

//  a Python function taken by a CuteQGraphicsTextItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsTextItem(
    QGraphicsTextItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsTextItem *>(self)->take(key, call);
}

//  QRectF QGraphicsTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QGraphicsTextItem12boundingRectEv(
    const QGraphicsTextItem *self) {
  return new QRectF(self->QGraphicsTextItem::boundingRect());
}

//  QPainterPath QGraphicsTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsTextItem5shapeEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->QGraphicsTextItem::shape());
}

//  bool QGraphicsTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsTextItem8containsERK7QPointF(
    const QGraphicsTextItem *self,
    const QPointF *point) {
  return self->QGraphicsTextItem::contains(*point);
}

//  void QGraphicsTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsTextItem::paint(painter, option, widget);
}

//  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsTextItem *self,
    const QGraphicsItem *item) {
  return self->QGraphicsTextItem::isObscuredBy(item);
}

//  QPainterPath QGraphicsTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsTextItem10opaqueAreaEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->QGraphicsTextItem::opaqueArea());
}

//  int QGraphicsTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGraphicsTextItem4typeEv(const QGraphicsTextItem *self) {
  return self->QGraphicsTextItem::type();
}

//  bool QGraphicsTextItem::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QGraphicsTextItem10sceneEventEP6QEvent(
    QGraphicsTextItem *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::sceneEvent(
      event);
}

//  void QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::mousePressEvent(
      event);
}

//  void QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::mouseMoveEvent(
      event);
}

//  void QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::mouseReleaseEvent(
      event);
}

//  void QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::mouseDoubleClickEvent(
      event);
}

//  void QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneContextMenuEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::contextMenuEvent(
      event);
}

//  void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem13keyPressEventEP9QKeyEvent(
    QGraphicsTextItem *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::keyPressEvent(
      event);
}

//  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem15keyReleaseEventEP9QKeyEvent(
    QGraphicsTextItem *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::keyReleaseEvent(
      event);
}

//  void QGraphicsTextItem::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem12focusInEventEP11QFocusEvent(
    QGraphicsTextItem *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::focusInEvent(
      event);
}

//  void QGraphicsTextItem::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem13focusOutEventEP11QFocusEvent(
    QGraphicsTextItem *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::focusOutEvent(
      event);
}

//  void QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::dragEnterEvent(
      event);
}

//  void QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::dragLeaveEvent(
      event);
}

//  void QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::dragMoveEvent(
      event);
}

//  void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::dropEvent(
      event);
}

//  void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem16inputMethodEventEP17QInputMethodEvent(
    QGraphicsTextItem *self,
    QInputMethodEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::inputMethodEvent(
      event);
}

//  void QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::hoverEnterEvent(
      event);
}

//  void QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::hoverMoveEvent(
      event);
}

//  void QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsTextItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsTextItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::hoverLeaveEvent(
      event);
}

//  QVariant QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QGraphicsTextItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsTextItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(
      static_cast<const OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::inputMethodQuery(
          query));
}

//  QVariant QGraphicsTextItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QGraphicsTextItem9extensionERK8QVariant(
    const QGraphicsTextItem *self,
    const QVariant *variant) {
  return new QVariant(
      static_cast<const OwnQGraphicsTextItem *>(self)->OwnQGraphicsTextItem::extension(
          *variant));
}
