//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qline.h>
#include <QtGui/qpen.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QGraphicsLineItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsLineItem : QGraphicsLineItem {
  using QGraphicsLineItem::extension;
};

//  A QGraphicsLineItem that Python can take functions over in. Every QGraphicsLineItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQGraphicsLineItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsLineItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall2)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall4)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsLineItemCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsLineItemCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsLineItemCall7)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall8)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall9)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall10)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall11)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLineItemCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall13)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall14)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall15)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall16)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall17)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall18)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall20)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall21)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall22)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall23)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall24)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall25)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall26)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall27)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall28)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall29)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLineItemCall30)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsLineItemCall31)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsLineItemCall32)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsLineItem : public QGraphicsLineItem {
public:
  using QGraphicsLineItem::QGraphicsLineItem;
  void *taken[33] = {};

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
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  QRectF QGraphicsLineItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsLineItemCall0 call = reinterpret_cast<CuteQGraphicsLineItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsLineItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsLineItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsLineItemCall1 call = reinterpret_cast<CuteQGraphicsLineItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsLineItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLineItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsLineItemCall2 call = reinterpret_cast<CuteQGraphicsLineItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsLineItem::contains(point);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLineItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsLineItemCall3 call = reinterpret_cast<CuteQGraphicsLineItemCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsLineItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsLineItemCall4 call = reinterpret_cast<CuteQGraphicsLineItemCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsLineItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsLineItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsLineItemCall5 call = reinterpret_cast<CuteQGraphicsLineItemCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsLineItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsLineItem::type() const
  int type() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsLineItemCall6 call = reinterpret_cast<CuteQGraphicsLineItemCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLineItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsLineItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsLineItemCall7 call = reinterpret_cast<CuteQGraphicsLineItemCall7>(taken[7]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsLineItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsLineItemCall8 call = reinterpret_cast<CuteQGraphicsLineItemCall8>(taken[8]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithItem(
      const QGraphicsItem *other,
      Qt::ItemSelectionMode mode) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsLineItemCall9 call = reinterpret_cast<CuteQGraphicsLineItemCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsLineItemCall10 call = reinterpret_cast<CuteQGraphicsLineItemCall10>(taken[10]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsLineItemCall11 call = reinterpret_cast<CuteQGraphicsLineItemCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsLineItemCall12 call = reinterpret_cast<CuteQGraphicsLineItemCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsLineItemCall13 call = reinterpret_cast<CuteQGraphicsLineItemCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsLineItemCall14 call = reinterpret_cast<CuteQGraphicsLineItemCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsLineItemCall15 call = reinterpret_cast<CuteQGraphicsLineItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsLineItemCall16 call = reinterpret_cast<CuteQGraphicsLineItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsLineItemCall17 call = reinterpret_cast<CuteQGraphicsLineItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsLineItemCall18 call = reinterpret_cast<CuteQGraphicsLineItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsLineItemCall19 call = reinterpret_cast<CuteQGraphicsLineItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsLineItemCall20 call = reinterpret_cast<CuteQGraphicsLineItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsLineItemCall21 call = reinterpret_cast<CuteQGraphicsLineItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsLineItemCall22 call = reinterpret_cast<CuteQGraphicsLineItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsLineItemCall23 call = reinterpret_cast<CuteQGraphicsLineItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsLineItemCall24 call = reinterpret_cast<CuteQGraphicsLineItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsLineItemCall25 call = reinterpret_cast<CuteQGraphicsLineItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsLineItemCall26 call = reinterpret_cast<CuteQGraphicsLineItemCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsLineItemCall27 call = reinterpret_cast<CuteQGraphicsLineItemCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsLineItemCall28 call = reinterpret_cast<CuteQGraphicsLineItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsLineItemCall29 call = reinterpret_cast<CuteQGraphicsLineItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsLineItemCall30 call = reinterpret_cast<CuteQGraphicsLineItemCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsLineItemCall31 call = reinterpret_cast<CuteQGraphicsLineItemCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsLineItemCall32 call = reinterpret_cast<CuteQGraphicsLineItemCall32>(taken[32]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsLineItem::QGraphicsLineItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsLineItem(parent);
}

//  QGraphicsLineItem::QGraphicsLineItem(const QLineF &line, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1ERK6QLineFP13QGraphicsItem(
    const QLineF *line,
    QGraphicsItem *parent) {
  return new CuteQGraphicsLineItem(*line, parent);
}

//  QGraphicsLineItem::QGraphicsLineItem(qreal x1, qreal y1, qreal x2, qreal
//      y2, QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1EddddP13QGraphicsItem(
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    QGraphicsItem *parent) {
  return new CuteQGraphicsLineItem(x1, y1, x2, y2, parent);
}

//  QGraphicsLineItem::~QGraphicsLineItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItemD1Ev(QGraphicsLineItem *self) {
  delete self;
}

//  QPen QGraphicsLineItem::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK17QGraphicsLineItem3penEv(const QGraphicsLineItem *self) {
  return new QPen(self->pen());
}

//  void QGraphicsLineItem::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem6setPenERK4QPen(
    QGraphicsLineItem *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QLineF QGraphicsLineItem::line() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK17QGraphicsLineItem4lineEv(const QGraphicsLineItem *self) {
  return new QLineF(self->line());
}

//  void QGraphicsLineItem::setLine(const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem7setLineERK6QLineF(
    QGraphicsLineItem *self,
    const QLineF *line) {
  self->setLine(*line);
}

//  void QGraphicsLineItem::setLine(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem7setLineEdddd(
    QGraphicsLineItem *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  self->setLine(x1, y1, x2, y2);
}

//  QRectF QGraphicsLineItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsLineItem12boundingRectEv(
    const QGraphicsLineItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsLineItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsLineItem5shapeEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsLineItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsLineItem8containsERK7QPointF(
    const QGraphicsLineItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsLineItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsLineItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsLineItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsLineItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsLineItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsLineItem10opaqueAreaEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsLineItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsLineItem4typeEv(const QGraphicsLineItem *self) {
  return self->type();
}

//  bool QGraphicsLineItem::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsLineItem17supportsExtensionEN13QGraphicsItem9ExtensionE(
    const QGraphicsLineItem *self,
    QGraphicsItem::Extension extension) {
  return self->supportsExtension(extension);
}

//  void QGraphicsLineItem::setExtension(Extension extension, const QVariant
//      &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem12setExtensionEN13QGraphicsItem9ExtensionERK8QVariant(
    QGraphicsLineItem *self,
    QGraphicsItem::Extension extension,
    const QVariant *variant) {
  self->setExtension(extension, *variant);
}

//  QVariant QGraphicsLineItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QGraphicsLineItem9extensionERK8QVariant(
    const QGraphicsLineItem *self,
    const QVariant *variant) {
  return new QVariant(self->extension(*variant));
}

//  a Python function taken by a CuteQGraphicsLineItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsLineItem(
    QGraphicsLineItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsLineItem *>(self)->take(key, call);
}

//  QRectF QGraphicsLineItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QGraphicsLineItem12boundingRectEv(
    const QGraphicsLineItem *self) {
  return new QRectF(self->QGraphicsLineItem::boundingRect());
}

//  QPainterPath QGraphicsLineItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsLineItem5shapeEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->QGraphicsLineItem::shape());
}

//  bool QGraphicsLineItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsLineItem8containsERK7QPointF(
    const QGraphicsLineItem *self,
    const QPointF *point) {
  return self->QGraphicsLineItem::contains(*point);
}

//  void QGraphicsLineItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsLineItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsLineItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsLineItem::paint(painter, option, widget);
}

//  bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsLineItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsLineItem *self,
    const QGraphicsItem *item) {
  return self->QGraphicsLineItem::isObscuredBy(item);
}

//  QPainterPath QGraphicsLineItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsLineItem10opaqueAreaEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->QGraphicsLineItem::opaqueArea());
}

//  int QGraphicsLineItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGraphicsLineItem4typeEv(const QGraphicsLineItem *self) {
  return self->QGraphicsLineItem::type();
}

//  QVariant QGraphicsLineItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QGraphicsLineItem9extensionERK8QVariant(
    const QGraphicsLineItem *self,
    const QVariant *variant) {
  return new QVariant(
      static_cast<const OwnQGraphicsLineItem *>(self)->OwnQGraphicsLineItem::extension(
          *variant));
}

#endif  // QT_CONFIG(graphicsview)
