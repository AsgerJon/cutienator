//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsproxywidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsProxyWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsProxyWidget : QGraphicsProxyWidget {
  using QGraphicsProxyWidget::itemChange;
  using QGraphicsProxyWidget::event;
  using QGraphicsProxyWidget::eventFilter;
  using QGraphicsProxyWidget::showEvent;
  using QGraphicsProxyWidget::hideEvent;
  using QGraphicsProxyWidget::contextMenuEvent;
  using QGraphicsProxyWidget::dragEnterEvent;
  using QGraphicsProxyWidget::dragLeaveEvent;
  using QGraphicsProxyWidget::dragMoveEvent;
  using QGraphicsProxyWidget::dropEvent;
  using QGraphicsProxyWidget::hoverEnterEvent;
  using QGraphicsProxyWidget::hoverLeaveEvent;
  using QGraphicsProxyWidget::hoverMoveEvent;
  using QGraphicsProxyWidget::grabMouseEvent;
  using QGraphicsProxyWidget::ungrabMouseEvent;
  using QGraphicsProxyWidget::mouseMoveEvent;
  using QGraphicsProxyWidget::mousePressEvent;
  using QGraphicsProxyWidget::mouseReleaseEvent;
  using QGraphicsProxyWidget::mouseDoubleClickEvent;
  using QGraphicsProxyWidget::wheelEvent;
  using QGraphicsProxyWidget::keyPressEvent;
  using QGraphicsProxyWidget::keyReleaseEvent;
  using QGraphicsProxyWidget::focusInEvent;
  using QGraphicsProxyWidget::focusOutEvent;
  using QGraphicsProxyWidget::focusNextPrevChild;
  using QGraphicsProxyWidget::inputMethodQuery;
  using QGraphicsProxyWidget::inputMethodEvent;
  using QGraphicsProxyWidget::sizeHint;
  using QGraphicsProxyWidget::resizeEvent;
};

//  A QGraphicsProxyWidget that Python can take functions over in. Every QGraphicsProxyWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsProxyWidgetCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall1)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef int (*CuteQGraphicsProxyWidgetCall2)(const void *, int *);
typedef const QVariant * (*CuteQGraphicsProxyWidgetCall3)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall4)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall5)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall6)(const void *, QShowEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall7)(const void *, QHideEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall8)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall9)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall10)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall11)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall12)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall13)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall14)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall15)(const void *, QGraphicsSceneHoverEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall16)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall17)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall18)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall19)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall20)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall21)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall22)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall23)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall26)(const void *, QFocusEvent *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall27)(const void *, bool, int *);
typedef const QVariant * (*CuteQGraphicsProxyWidgetCall28)(const void *, int, int *);
typedef void (*CuteQGraphicsProxyWidgetCall29)(const void *, QInputMethodEvent *, int *);
typedef const QSizeF * (*CuteQGraphicsProxyWidgetCall30)(const void *, int, const QSizeF *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall31)(const void *, QGraphicsSceneResizeEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall32)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
typedef const QRectF * (*CuteQGraphicsProxyWidgetCall33)(const void *, int *);
typedef const QPainterPath * (*CuteQGraphicsProxyWidgetCall34)(const void *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall35)(const void *, QStyleOption *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall36)(const void *, int *);
typedef const QVariant * (*CuteQGraphicsProxyWidgetCall37)(const void *, const QString *, const QVariant *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall38)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall39)(const void *, QEvent *, int *);
typedef int (*CuteQGraphicsProxyWidgetCall40)(const void *, const QPointF *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall41)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall42)(const void *, QCloseEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall43)(const void *, QGraphicsSceneMoveEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall44)(const void *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall45)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall46)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall47)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall48)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall49)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall50)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall51)(const void *, const QMetaMethod *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall52)(const void *, int *);
typedef void (*CuteQGraphicsProxyWidgetCall53)(const void *, int, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall54)(const void *, const QPointF *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall55)(const void *, const QGraphicsItem *, int, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall56)(const void *, const QPainterPath *, int, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall57)(const void *, const QGraphicsItem *, int *);
typedef const QPainterPath * (*CuteQGraphicsProxyWidgetCall58)(const void *, int *);
typedef bool (*CuteQGraphicsProxyWidgetCall59)(const void *, QGraphicsItem *, QEvent *, int *);
typedef const QVariant * (*CuteQGraphicsProxyWidgetCall60)(const void *, const QVariant *, int *);
class CuteQGraphicsProxyWidget : public QGraphicsProxyWidget {
public:
  using QGraphicsProxyWidget::QGraphicsProxyWidget;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9showEventEP10QShowEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9hideEventEP10QHideEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14grabMouseEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
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
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget18focusNextPrevChildEb")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16windowFrameEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11changeEventEP6QEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget10closeEventEP11QCloseEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11polishEventEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[60] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall0 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::setGeometry(rect);
  }

  //  void QGraphicsProxyWidget::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall1 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall1>(taken[1]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::paint(painter, option, widget);
  }

  //  int QGraphicsProxyWidget::type() const
  int type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall2 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::type();
  }

  //  QVariant QGraphicsProxyWidget::itemChange(GraphicsItemChange change,
  //      const QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall3 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsProxyWidget::itemChange(change, value);
  }

  //  bool QGraphicsProxyWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall4 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::event(event);
  }

  //  bool QGraphicsProxyWidget::eventFilter(QObject *object, QEvent
  //      *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall5 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall5>(taken[5]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::eventFilter(object, event);
  }

  //  void QGraphicsProxyWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall6 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::showEvent(event);
  }

  //  void QGraphicsProxyWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall7 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hideEvent(event);
  }

  //  void
  //      QGraphicsProxyWidget::contextMenuEvent(QGraphicsSceneContextMenuE
  //      vent *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall8 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::contextMenuEvent(event);
  }

  //  void QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall9 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragEnterEvent(event);
  }

  //  void QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall10 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragLeaveEvent(event);
  }

  //  void QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall11 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragMoveEvent(event);
  }

  //  void QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall12 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dropEvent(event);
  }

  //  void QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall13 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverEnterEvent(event);
  }

  //  void QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall14 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverLeaveEvent(event);
  }

  //  void QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall15 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverMoveEvent(event);
  }

  //  void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)
  void grabMouseEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall16 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::grabMouseEvent(event);
  }

  //  void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)
  void ungrabMouseEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall17 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::ungrabMouseEvent(event);
  }

  //  void QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall18 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseMoveEvent(event);
  }

  //  void QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall19 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mousePressEvent(event);
  }

  //  void QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall20 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseReleaseEvent(event);
  }

  //  void
  //      QGraphicsProxyWidget::mouseDoubleClickEvent(QGraphicsSceneMouseEv
  //      ent *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall21 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent
  //      *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall22 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::wheelEvent(event);
  }

  //  void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall23 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::keyPressEvent(event);
  }

  //  void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall24 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::keyReleaseEvent(event);
  }

  //  void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall25 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::focusInEvent(event);
  }

  //  void QGraphicsProxyWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall26 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::focusOutEvent(event);
  }

  //  bool QGraphicsProxyWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall27 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall27>(taken[27]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::focusNextPrevChild(next);
  }

  //  QVariant QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall28 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall28>(taken[28]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsProxyWidget::inputMethodQuery(query);
  }

  //  void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall29 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::inputMethodEvent(event);
  }

  //  QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which, const
  //      QSizeF &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall30 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall30>(taken[30]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsProxyWidget::sizeHint(which, constraint);
  }

  //  void QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent
  //      *event)
  void resizeEvent(QGraphicsSceneResizeEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall31 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::resizeEvent(event);
  }

  //  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paintWindowFrame(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall32 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall32>(taken[32]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsWidget::paintWindowFrame(painter, option, widget);
  }

  //  QRectF QGraphicsWidget::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall33 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::boundingRect();
  }

  //  QPainterPath QGraphicsWidget::shape() const
  QPainterPath shape() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall34 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall34>(taken[34]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::shape();
  }

  //  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
  void initStyleOption(QStyleOption *option) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall35 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall35>(taken[35]);
      call(this, option, &handled);
      if (handled) return;
    }
    QGraphicsWidget::initStyleOption(option);
  }

  //  void QGraphicsWidget::updateGeometry()
  void updateGeometry() override {
    if (taken[36]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall36 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::updateGeometry();
  }

  //  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
  //      const QVariant &value)
  QVariant propertyChange(
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall37 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall37>(taken[37]);
      const QVariant * given = call(this, &propertyName, &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::propertyChange(propertyName, value);
  }

  //  bool QGraphicsWidget::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall38 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::sceneEvent(event);
  }

  //  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
  bool windowFrameEvent(QEvent *e) override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall39 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall39>(taken[39]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::windowFrameEvent(e);
  }

  //  Qt::WindowFrameSection QGraphicsWidget::windowFrameSectionAt(const
  //      QPointF &pos) const
  Qt::WindowFrameSection windowFrameSectionAt(
      const QPointF &pos) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall40 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall40>(taken[40]);
      int given = call(this, &pos, &handled);
      if (handled) return static_cast<Qt::WindowFrameSection>(given);
    }
    return QGraphicsWidget::windowFrameSectionAt(pos);
  }

  //  void QGraphicsWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall41 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::changeEvent(event);
  }

  //  void QGraphicsWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall42 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::closeEvent(event);
  }

  //  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
  void moveEvent(QGraphicsSceneMoveEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall43 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::moveEvent(event);
  }

  //  void QGraphicsWidget::polishEvent()
  void polishEvent() override {
    if (taken[44]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall44 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::polishEvent();
  }

  //  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
  void grabKeyboardEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall45 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::grabKeyboardEvent(event);
  }

  //  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
  void ungrabKeyboardEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall46 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::ungrabKeyboardEvent(event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall47 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall48 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall49 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall50 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall51 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }

  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[52]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall52 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall52>(taken[52]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }

  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[53]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall53 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall53>(taken[53]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }

  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[54]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall54 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall54>(taken[54]);
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
    if (taken[55]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall55 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall55>(taken[55]);
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
    if (taken[56]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall56 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall56>(taken[56]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }

  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[57]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall57 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall57>(taken[57]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }

  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall58 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall58>(taken[58]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }

  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall59 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall59>(taken[59]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }

  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[60]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetCall60 call = reinterpret_cast<CuteQGraphicsProxyWidgetCall60>(taken[60]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
};

//  const QMetaObject *QGraphicsProxyWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QGraphicsProxyWidget10metaObjectEv(
    const QGraphicsProxyWidget *self) {
  return self->metaObject();
}

//  QString QGraphicsProxyWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QGraphicsProxyWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsProxyWidget::tr(s, c, n));
}

//  QGraphicsProxyWidget::QGraphicsProxyWidget(QGraphicsItem *parent,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN20QGraphicsProxyWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new CuteQGraphicsProxyWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsProxyWidget::~QGraphicsProxyWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidgetD1Ev(QGraphicsProxyWidget *self) {
  delete self;
}

//  void QGraphicsProxyWidget::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget9setWidgetEP7QWidget(
    QGraphicsProxyWidget *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QGraphicsProxyWidget::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK20QGraphicsProxyWidget6widgetEv(
    const QGraphicsProxyWidget *self) {
  return self->widget();
}

//  QRectF QGraphicsProxyWidget::subWidgetRect(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsProxyWidget13subWidgetRectEPK7QWidget(
    const QGraphicsProxyWidget *self,
    const QWidget *widget) {
  return new QRectF(self->subWidgetRect(widget));
}

//  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF(
    QGraphicsProxyWidget *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void QGraphicsProxyWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsProxyWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  int QGraphicsProxyWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsProxyWidget4typeEv(
    const QGraphicsProxyWidget *self) {
  return self->type();
}

//  QGraphicsProxyWidget
//      *QGraphicsProxyWidget::createProxyForChildWidget(QWidget *child)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN20QGraphicsProxyWidget25createProxyForChildWidgetEP7QWidget(
    QGraphicsProxyWidget *self,
    QWidget *child) {
  return self->createProxyForChildWidget(child);
}

//  QVariant QGraphicsProxyWidget::itemChange(GraphicsItemChange change,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QGraphicsProxyWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsProxyWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(self->itemChange(change, *value));
}

//  bool QGraphicsProxyWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsProxyWidget5eventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  return self->event(event);
}

//  bool QGraphicsProxyWidget::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsProxyWidget11eventFilterEP7QObjectP6QEvent(
    QGraphicsProxyWidget *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QGraphicsProxyWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget9showEventEP10QShowEvent(
    QGraphicsProxyWidget *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QGraphicsProxyWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget9hideEventEP10QHideEvent(
    QGraphicsProxyWidget *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void
//      QGraphicsProxyWidget::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragEnterEvent(event);
}

//  void QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragMoveEvent(event);
}

//  void QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dropEvent(event);
}

//  void QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget14grabMouseEventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  self->grabMouseEvent(event);
}

//  void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget16ungrabMouseEventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  self->ungrabMouseEvent(event);
}

//  void QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QGraphicsProxyWidget::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget10wheelEventEP24QGraphicsSceneWheelEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneWheelEvent *event) {
  self->wheelEvent(event);
}

//  void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget13keyPressEventEP9QKeyEvent(
    QGraphicsProxyWidget *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget15keyReleaseEventEP9QKeyEvent(
    QGraphicsProxyWidget *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget12focusInEventEP11QFocusEvent(
    QGraphicsProxyWidget *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QGraphicsProxyWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget13focusOutEventEP11QFocusEvent(
    QGraphicsProxyWidget *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  bool QGraphicsProxyWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsProxyWidget18focusNextPrevChildEb(
    QGraphicsProxyWidget *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  QVariant QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery
//      query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QGraphicsProxyWidget16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsProxyWidget *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget16inputMethodEventEP17QInputMethodEvent(
    QGraphicsProxyWidget *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}

//  QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK20QGraphicsProxyWidget8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsProxyWidget *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget11resizeEventEP25QGraphicsSceneResizeEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneResizeEvent *event) {
  self->resizeEvent(event);
}

//  QGraphicsProxyWidget *QGraphicsProxyWidget::newProxyWidget(const QWidget
//      *a0)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN20QGraphicsProxyWidget14newProxyWidgetEPK7QWidget(
    QGraphicsProxyWidget *self,
    const QWidget *a0) {
  return self->newProxyWidget(a0);
}

//  QGraphicsProxyWidgetPrivate *QGraphicsProxyWidget::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidgetPrivate *ritual_ZN20QGraphicsProxyWidget6d_funcEv(
    QGraphicsProxyWidget *self) {
  return self->d_func();
}

//  const QGraphicsProxyWidgetPrivate *QGraphicsProxyWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsProxyWidgetPrivate *ritual_ZNK20QGraphicsProxyWidget6d_funcEv(
    const QGraphicsProxyWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsProxyWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsProxyWidget(
    QGraphicsProxyWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsProxyWidget *>(self)->take(key, call);
}

//  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF(
    QGraphicsProxyWidget *self,
    const QRectF *rect) {
  self->QGraphicsProxyWidget::setGeometry(*rect);
}

//  void QGraphicsProxyWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsProxyWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsProxyWidget::paint(painter, option, widget);
}

//  int QGraphicsProxyWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QGraphicsProxyWidget4typeEv(
    const QGraphicsProxyWidget *self) {
  return self->QGraphicsProxyWidget::type();
}

//  QVariant QGraphicsProxyWidget::itemChange(GraphicsItemChange change,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN20QGraphicsProxyWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsProxyWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(
      static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::itemChange(
          change,
          *value));
}

//  bool QGraphicsProxyWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QGraphicsProxyWidget5eventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::event(
      event);
}

//  bool QGraphicsProxyWidget::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QGraphicsProxyWidget11eventFilterEP7QObjectP6QEvent(
    QGraphicsProxyWidget *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::eventFilter(
      object,
      event);
}

//  void QGraphicsProxyWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget9showEventEP10QShowEvent(
    QGraphicsProxyWidget *self,
    QShowEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::showEvent(
      event);
}

//  void QGraphicsProxyWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget9hideEventEP10QHideEvent(
    QGraphicsProxyWidget *self,
    QHideEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::hideEvent(
      event);
}

//  void
//      QGraphicsProxyWidget::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneContextMenuEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::contextMenuEvent(
      event);
}

//  void QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::dragEnterEvent(
      event);
}

//  void QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::dragLeaveEvent(
      event);
}

//  void QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::dragMoveEvent(
      event);
}

//  void QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::dropEvent(
      event);
}

//  void QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::hoverEnterEvent(
      event);
}

//  void QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::hoverLeaveEvent(
      event);
}

//  void QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::hoverMoveEvent(
      event);
}

//  void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget14grabMouseEventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::grabMouseEvent(
      event);
}

//  void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget16ungrabMouseEventEP6QEvent(
    QGraphicsProxyWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::ungrabMouseEvent(
      event);
}

//  void QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::mouseMoveEvent(
      event);
}

//  void QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::mousePressEvent(
      event);
}

//  void QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::mouseReleaseEvent(
      event);
}

//  void QGraphicsProxyWidget::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::mouseDoubleClickEvent(
      event);
}

//  void QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget10wheelEventEP24QGraphicsSceneWheelEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneWheelEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::wheelEvent(
      event);
}

//  void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget13keyPressEventEP9QKeyEvent(
    QGraphicsProxyWidget *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::keyPressEvent(
      event);
}

//  void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget15keyReleaseEventEP9QKeyEvent(
    QGraphicsProxyWidget *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::keyReleaseEvent(
      event);
}

//  void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget12focusInEventEP11QFocusEvent(
    QGraphicsProxyWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::focusInEvent(
      event);
}

//  void QGraphicsProxyWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget13focusOutEventEP11QFocusEvent(
    QGraphicsProxyWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::focusOutEvent(
      event);
}

//  bool QGraphicsProxyWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QGraphicsProxyWidget18focusNextPrevChildEb(
    QGraphicsProxyWidget *self,
    bool next) {
  return static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::focusNextPrevChild(
      next);
}

//  QVariant QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery
//      query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QGraphicsProxyWidget16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsProxyWidget *self,
    Qt::InputMethodQuery query) {
  return new QVariant(
      static_cast<const OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::inputMethodQuery(
          query));
}

//  void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget16inputMethodEventEP17QInputMethodEvent(
    QGraphicsProxyWidget *self,
    QInputMethodEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::inputMethodEvent(
      event);
}

//  QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK20QGraphicsProxyWidget8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsProxyWidget *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      static_cast<const OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::sizeHint(
          which,
          *constraint));
}

//  void QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsProxyWidget11resizeEventEP25QGraphicsSceneResizeEvent(
    QGraphicsProxyWidget *self,
    QGraphicsSceneResizeEvent *event) {
  static_cast<OwnQGraphicsProxyWidget *>(self)->OwnQGraphicsProxyWidget::resizeEvent(
      event);
}
