//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QGraphicsPixmapItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsPixmapItem : QGraphicsPixmapItem {
  using QGraphicsPixmapItem::extension;
};

//  A QGraphicsPixmapItem that Python can take functions over in. Every QGraphicsPixmapItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQGraphicsPixmapItemCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsPixmapItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall2)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall4)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsPixmapItemCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsPixmapItemCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsPixmapItemCall7)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall8)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall9)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall10)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall11)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsPixmapItemCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall13)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall14)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall15)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall16)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall17)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall18)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall20)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall21)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall22)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall23)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall24)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall25)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall26)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall27)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall28)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall29)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsPixmapItemCall30)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsPixmapItemCall31)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsPixmapItemCall32)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsPixmapItem : public QGraphicsPixmapItem {
public:
  using QGraphicsPixmapItem::QGraphicsPixmapItem;
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
  //  QRectF QGraphicsPixmapItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall0 call = reinterpret_cast<CuteQGraphicsPixmapItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsPixmapItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsPixmapItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall1 call = reinterpret_cast<CuteQGraphicsPixmapItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsPixmapItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsPixmapItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall2 call = reinterpret_cast<CuteQGraphicsPixmapItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsPixmapItem::contains(point);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsPixmapItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall3 call = reinterpret_cast<CuteQGraphicsPixmapItemCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsPixmapItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem *item)
  //      const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall4 call = reinterpret_cast<CuteQGraphicsPixmapItemCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsPixmapItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsPixmapItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall5 call = reinterpret_cast<CuteQGraphicsPixmapItemCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsPixmapItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsPixmapItem::type() const
  int type() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall6 call = reinterpret_cast<CuteQGraphicsPixmapItemCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsPixmapItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsPixmapItem::extension(const QVariant &variant)
  //      const
  QVariant extension(const QVariant &variant) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall7 call = reinterpret_cast<CuteQGraphicsPixmapItemCall7>(taken[7]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsPixmapItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsPixmapItemCall8 call = reinterpret_cast<CuteQGraphicsPixmapItemCall8>(taken[8]);
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
      CuteQGraphicsPixmapItemCall9 call = reinterpret_cast<CuteQGraphicsPixmapItemCall9>(taken[9]);
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
      CuteQGraphicsPixmapItemCall10 call = reinterpret_cast<CuteQGraphicsPixmapItemCall10>(taken[10]);
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
      CuteQGraphicsPixmapItemCall11 call = reinterpret_cast<CuteQGraphicsPixmapItemCall11>(taken[11]);
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
      CuteQGraphicsPixmapItemCall12 call = reinterpret_cast<CuteQGraphicsPixmapItemCall12>(taken[12]);
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
      CuteQGraphicsPixmapItemCall13 call = reinterpret_cast<CuteQGraphicsPixmapItemCall13>(taken[13]);
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
      CuteQGraphicsPixmapItemCall14 call = reinterpret_cast<CuteQGraphicsPixmapItemCall14>(taken[14]);
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
      CuteQGraphicsPixmapItemCall15 call = reinterpret_cast<CuteQGraphicsPixmapItemCall15>(taken[15]);
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
      CuteQGraphicsPixmapItemCall16 call = reinterpret_cast<CuteQGraphicsPixmapItemCall16>(taken[16]);
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
      CuteQGraphicsPixmapItemCall17 call = reinterpret_cast<CuteQGraphicsPixmapItemCall17>(taken[17]);
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
      CuteQGraphicsPixmapItemCall18 call = reinterpret_cast<CuteQGraphicsPixmapItemCall18>(taken[18]);
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
      CuteQGraphicsPixmapItemCall19 call = reinterpret_cast<CuteQGraphicsPixmapItemCall19>(taken[19]);
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
      CuteQGraphicsPixmapItemCall20 call = reinterpret_cast<CuteQGraphicsPixmapItemCall20>(taken[20]);
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
      CuteQGraphicsPixmapItemCall21 call = reinterpret_cast<CuteQGraphicsPixmapItemCall21>(taken[21]);
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
      CuteQGraphicsPixmapItemCall22 call = reinterpret_cast<CuteQGraphicsPixmapItemCall22>(taken[22]);
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
      CuteQGraphicsPixmapItemCall23 call = reinterpret_cast<CuteQGraphicsPixmapItemCall23>(taken[23]);
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
      CuteQGraphicsPixmapItemCall24 call = reinterpret_cast<CuteQGraphicsPixmapItemCall24>(taken[24]);
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
      CuteQGraphicsPixmapItemCall25 call = reinterpret_cast<CuteQGraphicsPixmapItemCall25>(taken[25]);
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
      CuteQGraphicsPixmapItemCall26 call = reinterpret_cast<CuteQGraphicsPixmapItemCall26>(taken[26]);
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
      CuteQGraphicsPixmapItemCall27 call = reinterpret_cast<CuteQGraphicsPixmapItemCall27>(taken[27]);
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
      CuteQGraphicsPixmapItemCall28 call = reinterpret_cast<CuteQGraphicsPixmapItemCall28>(taken[28]);
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
      CuteQGraphicsPixmapItemCall29 call = reinterpret_cast<CuteQGraphicsPixmapItemCall29>(taken[29]);
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
      CuteQGraphicsPixmapItemCall30 call = reinterpret_cast<CuteQGraphicsPixmapItemCall30>(taken[30]);
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
      CuteQGraphicsPixmapItemCall31 call = reinterpret_cast<CuteQGraphicsPixmapItemCall31>(taken[31]);
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
      CuteQGraphicsPixmapItemCall32 call = reinterpret_cast<CuteQGraphicsPixmapItemCall32>(taken[32]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsPixmapItem::QGraphicsPixmapItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN19QGraphicsPixmapItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsPixmapItem(parent);
}

//  QGraphicsPixmapItem::QGraphicsPixmapItem(const QPixmap &pixmap,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN19QGraphicsPixmapItemC1ERK7QPixmapP13QGraphicsItem(
    const QPixmap *pixmap,
    QGraphicsItem *parent) {
  return new CuteQGraphicsPixmapItem(*pixmap, parent);
}

//  QGraphicsPixmapItem::~QGraphicsPixmapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItemD1Ev(QGraphicsPixmapItem *self) {
  delete self;
}

//  QPixmap QGraphicsPixmapItem::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK19QGraphicsPixmapItem6pixmapEv(
    const QGraphicsPixmapItem *self) {
  return new QPixmap(self->pixmap());
}

//  void QGraphicsPixmapItem::setPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setPixmapERK7QPixmap(
    QGraphicsPixmapItem *self,
    const QPixmap *pixmap) {
  self->setPixmap(*pixmap);
}

//  Qt::TransformationMode QGraphicsPixmapItem::transformationMode() const
extern "C" Q_DECL_EXPORT
Qt::TransformationMode ritual_ZNK19QGraphicsPixmapItem18transformationModeEv(
    const QGraphicsPixmapItem *self) {
  return self->transformationMode();
}

//  void QGraphicsPixmapItem::setTransformationMode(Qt::TransformationMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem21setTransformationModeEN2Qt18TransformationModeE(
    QGraphicsPixmapItem *self,
    Qt::TransformationMode mode) {
  self->setTransformationMode(mode);
}

//  QPointF QGraphicsPixmapItem::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QGraphicsPixmapItem6offsetEv(
    const QGraphicsPixmapItem *self) {
  return new QPointF(self->offset());
}

//  void QGraphicsPixmapItem::setOffset(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setOffsetERK7QPointF(
    QGraphicsPixmapItem *self,
    const QPointF *offset) {
  self->setOffset(*offset);
}

//  void QGraphicsPixmapItem::setOffset(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setOffsetEdd(
    QGraphicsPixmapItem *self,
    qreal x,
    qreal y) {
  self->setOffset(x, y);
}

//  QRectF QGraphicsPixmapItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsPixmapItem12boundingRectEv(
    const QGraphicsPixmapItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsPixmapItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QGraphicsPixmapItem5shapeEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsPixmapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsPixmapItem8containsERK7QPointF(
    const QGraphicsPixmapItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsPixmapItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsPixmapItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsPixmapItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsPixmapItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsPixmapItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QGraphicsPixmapItem10opaqueAreaEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsPixmapItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsPixmapItem4typeEv(const QGraphicsPixmapItem *self) {
  return self->type();
}

//  ShapeMode QGraphicsPixmapItem::shapeMode() const
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem::ShapeMode ritual_ZNK19QGraphicsPixmapItem9shapeModeEv(
    const QGraphicsPixmapItem *self) {
  return self->shapeMode();
}

//  void QGraphicsPixmapItem::setShapeMode(ShapeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem12setShapeModeENS_9ShapeModeE(
    QGraphicsPixmapItem *self,
    QGraphicsPixmapItem::ShapeMode mode) {
  self->setShapeMode(mode);
}

//  bool QGraphicsPixmapItem::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsPixmapItem17supportsExtensionEN13QGraphicsItem9ExtensionE(
    const QGraphicsPixmapItem *self,
    QGraphicsItem::Extension extension) {
  return self->supportsExtension(extension);
}

//  void QGraphicsPixmapItem::setExtension(Extension extension, const
//      QVariant &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem12setExtensionEN13QGraphicsItem9ExtensionERK8QVariant(
    QGraphicsPixmapItem *self,
    QGraphicsItem::Extension extension,
    const QVariant *variant) {
  self->setExtension(extension, *variant);
}

//  QVariant QGraphicsPixmapItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QGraphicsPixmapItem9extensionERK8QVariant(
    const QGraphicsPixmapItem *self,
    const QVariant *variant) {
  return new QVariant(self->extension(*variant));
}

//  a Python function taken by a CuteQGraphicsPixmapItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsPixmapItem(
    QGraphicsPixmapItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsPixmapItem *>(self)->take(key, call);
}

//  QRectF QGraphicsPixmapItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QGraphicsPixmapItem12boundingRectEv(
    const QGraphicsPixmapItem *self) {
  return new QRectF(self->QGraphicsPixmapItem::boundingRect());
}

//  QPainterPath QGraphicsPixmapItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK19QGraphicsPixmapItem5shapeEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->QGraphicsPixmapItem::shape());
}

//  bool QGraphicsPixmapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGraphicsPixmapItem8containsERK7QPointF(
    const QGraphicsPixmapItem *self,
    const QPointF *point) {
  return self->QGraphicsPixmapItem::contains(*point);
}

//  void QGraphicsPixmapItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsPixmapItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsPixmapItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsPixmapItem::paint(painter, option, widget);
}

//  bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGraphicsPixmapItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsPixmapItem *self,
    const QGraphicsItem *item) {
  return self->QGraphicsPixmapItem::isObscuredBy(item);
}

//  QPainterPath QGraphicsPixmapItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK19QGraphicsPixmapItem10opaqueAreaEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->QGraphicsPixmapItem::opaqueArea());
}

//  int QGraphicsPixmapItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QGraphicsPixmapItem4typeEv(
    const QGraphicsPixmapItem *self) {
  return self->QGraphicsPixmapItem::type();
}

//  QVariant QGraphicsPixmapItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QGraphicsPixmapItem9extensionERK8QVariant(
    const QGraphicsPixmapItem *self,
    const QVariant *variant) {
  return new QVariant(
      static_cast<const OwnQGraphicsPixmapItem *>(self)->OwnQGraphicsPixmapItem::extension(
          *variant));
}

#endif  // QT_CONFIG(graphicsview)
