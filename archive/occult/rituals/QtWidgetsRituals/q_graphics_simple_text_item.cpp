//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QGraphicsSimpleTextItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsSimpleTextItem : QGraphicsSimpleTextItem {
  using QGraphicsSimpleTextItem::extension;
};

//  A QGraphicsSimpleTextItem that Python can take functions over in. Every QGraphicsSimpleTextItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQGraphicsSimpleTextItemCall0)(const void *, int *);
typedef const QPainterPath * (*CuteQGraphicsSimpleTextItemCall1)(const void *, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall2)(const void *, const QPointF *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall4)(const void *, const QGraphicsItem *, int *);
typedef const QPainterPath * (*CuteQGraphicsSimpleTextItemCall5)(const void *, int *);
typedef int (*CuteQGraphicsSimpleTextItemCall6)(const void *, int *);
typedef const QVariant * (*CuteQGraphicsSimpleTextItemCall7)(const void *, const QVariant *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall8)(const void *, int, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall9)(const void *, const QGraphicsItem *, int, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall10)(const void *, const QPainterPath *, int, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall11)(const void *, QGraphicsItem *, QEvent *, int *);
typedef bool (*CuteQGraphicsSimpleTextItemCall12)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall13)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall14)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall15)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall16)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall17)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall20)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall21)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall22)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall25)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall26)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall27)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall28)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall29)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef void (*CuteQGraphicsSimpleTextItemCall30)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQGraphicsSimpleTextItemCall31)(const void *, int, int *);
typedef const QVariant * (*CuteQGraphicsSimpleTextItemCall32)(const void *, int, const QVariant *, int *);
class CuteQGraphicsSimpleTextItem : public QGraphicsSimpleTextItem {
public:
  using QGraphicsSimpleTextItem::QGraphicsSimpleTextItem;
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

  //  QRectF QGraphicsSimpleTextItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall0 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsSimpleTextItem::boundingRect();
  }

  //  QPainterPath QGraphicsSimpleTextItem::shape() const
  QPainterPath shape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall1 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall1>(taken[1]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsSimpleTextItem::shape();
  }

  //  bool QGraphicsSimpleTextItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall2 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsSimpleTextItem::contains(point);
  }

  //  void QGraphicsSimpleTextItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall3 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsSimpleTextItem::paint(painter, option, widget);
  }

  //  bool QGraphicsSimpleTextItem::isObscuredBy(const QGraphicsItem *item)
  //      const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall4 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsSimpleTextItem::isObscuredBy(item);
  }

  //  QPainterPath QGraphicsSimpleTextItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall5 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsSimpleTextItem::opaqueArea();
  }

  //  int QGraphicsSimpleTextItem::type() const
  int type() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall6 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsSimpleTextItem::type();
  }

  //  QVariant QGraphicsSimpleTextItem::extension(const QVariant &variant)
  //      const
  QVariant extension(const QVariant &variant) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall7 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall7>(taken[7]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsSimpleTextItem::extension(variant);
  }

  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall8 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall8>(taken[8]);
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
      CuteQGraphicsSimpleTextItemCall9 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall9>(taken[9]);
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
      CuteQGraphicsSimpleTextItemCall10 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall10>(taken[10]);
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
      CuteQGraphicsSimpleTextItemCall11 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }

  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall12 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall12>(taken[12]);
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
      CuteQGraphicsSimpleTextItemCall13 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall13>(taken[13]);
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
      CuteQGraphicsSimpleTextItemCall14 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall14>(taken[14]);
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
      CuteQGraphicsSimpleTextItemCall15 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }

  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall16 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }

  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall17 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }

  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall18 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }

  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall19 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }

  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall20 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }

  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall21 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }

  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall22 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }

  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall23 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }

  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall24 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }

  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall25 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }

  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall26 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall26>(taken[26]);
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
      CuteQGraphicsSimpleTextItemCall27 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall27>(taken[27]);
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
      CuteQGraphicsSimpleTextItemCall28 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall29 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }

  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsSimpleTextItemCall30 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall30>(taken[30]);
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
      CuteQGraphicsSimpleTextItemCall31 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall31>(taken[31]);
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
      CuteQGraphicsSimpleTextItemCall32 call = reinterpret_cast<CuteQGraphicsSimpleTextItemCall32>(taken[32]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
};

//  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN23QGraphicsSimpleTextItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteQGraphicsSimpleTextItem(parent);
}

//  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(const QString &text,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN23QGraphicsSimpleTextItemC1ERK7QStringP13QGraphicsItem(
    const QString *text,
    QGraphicsItem *parent) {
  return new CuteQGraphicsSimpleTextItem(*text, parent);
}

//  QGraphicsSimpleTextItem::~QGraphicsSimpleTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItemD1Ev(QGraphicsSimpleTextItem *self) {
  delete self;
}

//  void QGraphicsSimpleTextItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem7setTextERK7QString(
    QGraphicsSimpleTextItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QGraphicsSimpleTextItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QGraphicsSimpleTextItem4textEv(
    const QGraphicsSimpleTextItem *self) {
  return new QString(self->text());
}

//  void QGraphicsSimpleTextItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem7setFontERK5QFont(
    QGraphicsSimpleTextItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QFont QGraphicsSimpleTextItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QGraphicsSimpleTextItem4fontEv(
    const QGraphicsSimpleTextItem *self) {
  return new QFont(self->font());
}

//  QRectF QGraphicsSimpleTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QGraphicsSimpleTextItem12boundingRectEv(
    const QGraphicsSimpleTextItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsSimpleTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QGraphicsSimpleTextItem5shapeEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsSimpleTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGraphicsSimpleTextItem8containsERK7QPointF(
    const QGraphicsSimpleTextItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsSimpleTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsSimpleTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsSimpleTextItem::isObscuredBy(const QGraphicsItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGraphicsSimpleTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsSimpleTextItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsSimpleTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QGraphicsSimpleTextItem10opaqueAreaEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsSimpleTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGraphicsSimpleTextItem4typeEv(
    const QGraphicsSimpleTextItem *self) {
  return self->type();
}

//  bool QGraphicsSimpleTextItem::supportsExtension(Extension extension)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGraphicsSimpleTextItem17supportsExtensionEN13QGraphicsItem9ExtensionE(
    const QGraphicsSimpleTextItem *self,
    QGraphicsItem::Extension extension) {
  return self->supportsExtension(extension);
}

//  void QGraphicsSimpleTextItem::setExtension(Extension extension, const
//      QVariant &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem12setExtensionEN13QGraphicsItem9ExtensionERK8QVariant(
    QGraphicsSimpleTextItem *self,
    QGraphicsItem::Extension extension,
    const QVariant *variant) {
  self->setExtension(extension, *variant);
}

//  QVariant QGraphicsSimpleTextItem::extension(const QVariant &variant)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QGraphicsSimpleTextItem9extensionERK8QVariant(
    const QGraphicsSimpleTextItem *self,
    const QVariant *variant) {
  return new QVariant(self->extension(*variant));
}

//  a Python function taken by a CuteQGraphicsSimpleTextItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSimpleTextItem(
    QGraphicsSimpleTextItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSimpleTextItem *>(self)->take(key, call);
}

//  QRectF QGraphicsSimpleTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK23QGraphicsSimpleTextItem12boundingRectEv(
    const QGraphicsSimpleTextItem *self) {
  return new QRectF(self->QGraphicsSimpleTextItem::boundingRect());
}

//  QPainterPath QGraphicsSimpleTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK23QGraphicsSimpleTextItem5shapeEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->QGraphicsSimpleTextItem::shape());
}

//  bool QGraphicsSimpleTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QGraphicsSimpleTextItem8containsERK7QPointF(
    const QGraphicsSimpleTextItem *self,
    const QPointF *point) {
  return self->QGraphicsSimpleTextItem::contains(*point);
}

//  void QGraphicsSimpleTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QGraphicsSimpleTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsSimpleTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsSimpleTextItem::paint(painter, option, widget);
}

//  bool QGraphicsSimpleTextItem::isObscuredBy(const QGraphicsItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QGraphicsSimpleTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsSimpleTextItem *self,
    const QGraphicsItem *item) {
  return self->QGraphicsSimpleTextItem::isObscuredBy(item);
}

//  QPainterPath QGraphicsSimpleTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK23QGraphicsSimpleTextItem10opaqueAreaEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->QGraphicsSimpleTextItem::opaqueArea());
}

//  int QGraphicsSimpleTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QGraphicsSimpleTextItem4typeEv(
    const QGraphicsSimpleTextItem *self) {
  return self->QGraphicsSimpleTextItem::type();
}

//  QVariant QGraphicsSimpleTextItem::extension(const QVariant &variant)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QGraphicsSimpleTextItem9extensionERK8QVariant(
    const QGraphicsSimpleTextItem *self,
    const QVariant *variant) {
  return new QVariant(
      static_cast<const OwnQGraphicsSimpleTextItem *>(self)->OwnQGraphicsSimpleTextItem::extension(
          *variant));
}
