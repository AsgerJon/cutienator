//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QGraphicsRectItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsRectItem : QGraphicsRectItem {
  using QGraphicsRectItem::extension;
};

//  A QGraphicsRectItem that Python can take functions over in. Every QGraphicsRectItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQGraphicsRectItemCall0)(const void *, int *);
typedef const QPainterPath * (*CuteQGraphicsRectItemCall1)(const void *, int *);
typedef bool (*CuteQGraphicsRectItemCall2)(const void *, const QPointF *, int *);
typedef void (*CuteQGraphicsRectItemCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef bool (*CuteQGraphicsRectItemCall4)(const void *, const QGraphicsItem *, int *);
typedef const QPainterPath * (*CuteQGraphicsRectItemCall5)(const void *, int *);
typedef int (*CuteQGraphicsRectItemCall6)(const void *, int *);
typedef const QVariant * (*CuteQGraphicsRectItemCall7)(const void *, const QVariant *, int *);
typedef void (*CuteQGraphicsRectItemCall8)(const void *, int, int *);
typedef bool (*CuteQGraphicsRectItemCall9)(const void *, const QGraphicsItem *, int, int *);
typedef bool (*CuteQGraphicsRectItemCall10)(const void *, const QPainterPath *, int, int *);
typedef bool (*CuteQGraphicsRectItemCall11)(const void *, QGraphicsItem *, QEvent *, int *);
typedef bool (*CuteQGraphicsRectItemCall12)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall13)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall14)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall15)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall16)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall17)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall20)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall21)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall22)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall25)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall26)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall27)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall28)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall29)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef void (*CuteQGraphicsRectItemCall30)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQGraphicsRectItemCall31)(const void *, int, int *);
typedef const QVariant * (*CuteQGraphicsRectItemCall32)(const void *, int, const QVariant *, int *);
class CuteQGraphicsRectItem : public QGraphicsRectItem {
public:
  using QGraphicsRectItem::QGraphicsRectItem;
  void *taken[33] = {};

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
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[32] = call;
      return true;
    }
    return false;
  }

  //  QRectF QGraphicsRectItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsRectItemCall0 call = reinterpret_cast<CuteQGraphicsRectItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsRectItem::boundingRect();
  }

  //  QPainterPath QGraphicsRectItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsRectItemCall1 call = reinterpret_cast<CuteQGraphicsRectItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsRectItem::shape();
  }

  //  bool QGraphicsRectItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsRectItemCall2 call = reinterpret_cast<CuteQGraphicsRectItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsRectItem::contains(point);
  }

  //  void QGraphicsRectItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsRectItemCall3 call = reinterpret_cast<CuteQGraphicsRectItemCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsRectItem::paint(painter, option, widget);
  }

  //  bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsRectItemCall4 call = reinterpret_cast<CuteQGraphicsRectItemCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsRectItem::isObscuredBy(item);
  }

  //  QPainterPath QGraphicsRectItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsRectItemCall5 call = reinterpret_cast<CuteQGraphicsRectItemCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsRectItem::opaqueArea();
  }

  //  int QGraphicsRectItem::type() const
  int type() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsRectItemCall6 call = reinterpret_cast<CuteQGraphicsRectItemCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsRectItem::type();
  }

  //  QVariant QGraphicsRectItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsRectItemCall7 call = reinterpret_cast<CuteQGraphicsRectItemCall7>(taken[7]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsRectItem::extension(variant);
  }

  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsRectItemCall8 call = reinterpret_cast<CuteQGraphicsRectItemCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsRectItemCall9 call = reinterpret_cast<CuteQGraphicsRectItemCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsRectItemCall10 call = reinterpret_cast<CuteQGraphicsRectItemCall10>(taken[10]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }

  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsRectItemCall11 call = reinterpret_cast<CuteQGraphicsRectItemCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }

  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsRectItemCall12 call = reinterpret_cast<CuteQGraphicsRectItemCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEvent(event);
  }

  //  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsRectItemCall13 call = reinterpret_cast<CuteQGraphicsRectItemCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::contextMenuEvent(event);
  }

  //  void QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsRectItemCall14 call = reinterpret_cast<CuteQGraphicsRectItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragEnterEvent(event);
  }

  //  void QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsRectItemCall15 call = reinterpret_cast<CuteQGraphicsRectItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }

  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsRectItemCall16 call = reinterpret_cast<CuteQGraphicsRectItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }

  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsRectItemCall17 call = reinterpret_cast<CuteQGraphicsRectItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }

  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsRectItemCall18 call = reinterpret_cast<CuteQGraphicsRectItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }

  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsRectItemCall19 call = reinterpret_cast<CuteQGraphicsRectItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }

  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsRectItemCall20 call = reinterpret_cast<CuteQGraphicsRectItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }

  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsRectItemCall21 call = reinterpret_cast<CuteQGraphicsRectItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }

  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsRectItemCall22 call = reinterpret_cast<CuteQGraphicsRectItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }

  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsRectItemCall23 call = reinterpret_cast<CuteQGraphicsRectItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }

  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsRectItemCall24 call = reinterpret_cast<CuteQGraphicsRectItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }

  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsRectItemCall25 call = reinterpret_cast<CuteQGraphicsRectItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }

  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsRectItemCall26 call = reinterpret_cast<CuteQGraphicsRectItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }

  //  void QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsRectItemCall27 call = reinterpret_cast<CuteQGraphicsRectItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseReleaseEvent(event);
  }

  //  void QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsRectItemCall28 call = reinterpret_cast<CuteQGraphicsRectItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsRectItemCall29 call = reinterpret_cast<CuteQGraphicsRectItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }

  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsRectItemCall30 call = reinterpret_cast<CuteQGraphicsRectItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::inputMethodEvent(event);
  }

  //  QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsRectItemCall31 call = reinterpret_cast<CuteQGraphicsRectItemCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsRectItemCall32 call = reinterpret_cast<CuteQGraphicsRectItemCall32>(taken[32]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
};

//  QGraphicsRectItem::QGraphicsRectItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsRectItem(parent);
}

//  QGraphicsRectItem::QGraphicsRectItem(const QRectF &rect, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1ERK6QRectFP13QGraphicsItem(
    const QRectF *rect,
    QGraphicsItem *parent) {
  return new CuteQGraphicsRectItem(*rect, parent);
}

//  QGraphicsRectItem::QGraphicsRectItem(qreal x, qreal y, qreal w, qreal h,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1EddddP13QGraphicsItem(
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    QGraphicsItem *parent) {
  return new CuteQGraphicsRectItem(x, y, w, h, parent);
}

//  QGraphicsRectItem::~QGraphicsRectItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItemD1Ev(QGraphicsRectItem *self) {
  delete self;
}

//  QRectF QGraphicsRectItem::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsRectItem4rectEv(const QGraphicsRectItem *self) {
  return new QRectF(self->rect());
}

//  void QGraphicsRectItem::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem7setRectERK6QRectF(
    QGraphicsRectItem *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QGraphicsRectItem::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem7setRectEdddd(
    QGraphicsRectItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QGraphicsRectItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsRectItem12boundingRectEv(
    const QGraphicsRectItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsRectItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsRectItem5shapeEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsRectItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsRectItem8containsERK7QPointF(
    const QGraphicsRectItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsRectItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsRectItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsRectItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsRectItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsRectItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsRectItem10opaqueAreaEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsRectItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsRectItem4typeEv(const QGraphicsRectItem *self) {
  return self->type();
}

//  bool QGraphicsRectItem::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsRectItem17supportsExtensionEN13QGraphicsItem9ExtensionE(
    const QGraphicsRectItem *self,
    QGraphicsItem::Extension extension) {
  return self->supportsExtension(extension);
}

//  void QGraphicsRectItem::setExtension(Extension extension, const QVariant
//      &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem12setExtensionEN13QGraphicsItem9ExtensionERK8QVariant(
    QGraphicsRectItem *self,
    QGraphicsItem::Extension extension,
    const QVariant *variant) {
  self->setExtension(extension, *variant);
}

//  QVariant QGraphicsRectItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QGraphicsRectItem9extensionERK8QVariant(
    const QGraphicsRectItem *self,
    const QVariant *variant) {
  return new QVariant(self->extension(*variant));
}

//  a Python function taken by a CuteQGraphicsRectItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsRectItem(
    QGraphicsRectItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsRectItem *>(self)->take(key, call);
}

//  QRectF QGraphicsRectItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QGraphicsRectItem12boundingRectEv(
    const QGraphicsRectItem *self) {
  return new QRectF(self->QGraphicsRectItem::boundingRect());
}

//  QPainterPath QGraphicsRectItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsRectItem5shapeEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->QGraphicsRectItem::shape());
}

//  bool QGraphicsRectItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsRectItem8containsERK7QPointF(
    const QGraphicsRectItem *self,
    const QPointF *point) {
  return self->QGraphicsRectItem::contains(*point);
}

//  void QGraphicsRectItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGraphicsRectItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsRectItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsRectItem::paint(painter, option, widget);
}

//  bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGraphicsRectItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsRectItem *self,
    const QGraphicsItem *item) {
  return self->QGraphicsRectItem::isObscuredBy(item);
}

//  QPainterPath QGraphicsRectItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK17QGraphicsRectItem10opaqueAreaEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->QGraphicsRectItem::opaqueArea());
}

//  int QGraphicsRectItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGraphicsRectItem4typeEv(const QGraphicsRectItem *self) {
  return self->QGraphicsRectItem::type();
}

//  QVariant QGraphicsRectItem::extension(const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QGraphicsRectItem9extensionERK8QVariant(
    const QGraphicsRectItem *self,
    const QVariant *variant) {
  return new QVariant(
      static_cast<const OwnQGraphicsRectItem *>(self)->OwnQGraphicsRectItem::extension(
          *variant));
}
