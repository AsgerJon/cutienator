//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/editableaxislabel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/editableaxislabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A EditableAxisLabel that Python can take functions over in. Every EditableAxisLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall0)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall1)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteEditableAxisLabelCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall4)(const void *, int *);
typedef void (*CuteEditableAxisLabelCall5)(const void *, int *);
typedef void (*CuteEditableAxisLabelCall6)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteEditableAxisLabelCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall8)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall9)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall10)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteEditableAxisLabelCall11)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteEditableAxisLabelCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall13)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall14)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall15)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall16)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall17)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall18)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall19)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall20)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall21)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall22)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall23)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall24)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall25)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall27)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteEditableAxisLabelCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteEditableAxisLabelCall29)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall30)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteEditableAxisLabelCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteEditableAxisLabelCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteEditableAxisLabelCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteEditableAxisLabelCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteEditableAxisLabelCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteEditableAxisLabelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall37)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall38)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall39)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteEditableAxisLabelCall40)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteEditableAxisLabelCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteEditableAxisLabelCall42)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteEditableAxisLabel : public EditableAxisLabel {
public:
  using EditableAxisLabel::EditableAxisLabel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN17EditableAxisLabel19setInitialEditValueEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17EditableAxisLabel13finishEditingEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17EditableAxisLabel20resetBeforeEditValueEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
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
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void EditableAxisLabel::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteEditableAxisLabelCall0 call = reinterpret_cast<CuteEditableAxisLabelCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    EditableAxisLabel::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void EditableAxisLabel::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteEditableAxisLabelCall1 call = reinterpret_cast<CuteEditableAxisLabelCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    EditableAxisLabel::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool EditableAxisLabel::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteEditableAxisLabelCall2 call = reinterpret_cast<CuteEditableAxisLabelCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return EditableAxisLabel::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF EditableAxisLabel::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteEditableAxisLabelCall3 call = reinterpret_cast<CuteEditableAxisLabelCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return EditableAxisLabel::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void EditableAxisLabel::setInitialEditValue()
  void setInitialEditValue() override {
    if (taken[4]) {
      int handled = 0;
      CuteEditableAxisLabelCall4 call = reinterpret_cast<CuteEditableAxisLabelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void EditableAxisLabel::finishEditing()
  void finishEditing() override {
    if (taken[5]) {
      int handled = 0;
      CuteEditableAxisLabelCall5 call = reinterpret_cast<CuteEditableAxisLabelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void EditableAxisLabel::resetBeforeEditValue()
  void resetBeforeEditValue() override {
    if (taken[6]) {
      int handled = 0;
      CuteEditableAxisLabelCall6 call = reinterpret_cast<CuteEditableAxisLabelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsTextItem::shape() const
  QPainterPath shape() const override {
    if (taken[7]) {
      int handled = 0;
      CuteEditableAxisLabelCall7 call = reinterpret_cast<CuteEditableAxisLabelCall7>(taken[7]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsTextItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteEditableAxisLabelCall8 call = reinterpret_cast<CuteEditableAxisLabelCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::contains(point);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[9]) {
      int handled = 0;
      CuteEditableAxisLabelCall9 call = reinterpret_cast<CuteEditableAxisLabelCall9>(taken[9]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[10]) {
      int handled = 0;
      CuteEditableAxisLabelCall10 call = reinterpret_cast<CuteEditableAxisLabelCall10>(taken[10]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsTextItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[11]) {
      int handled = 0;
      CuteEditableAxisLabelCall11 call = reinterpret_cast<CuteEditableAxisLabelCall11>(taken[11]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsTextItem::type() const
  int type() const override {
    if (taken[12]) {
      int handled = 0;
      CuteEditableAxisLabelCall12 call = reinterpret_cast<CuteEditableAxisLabelCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::mousePressEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteEditableAxisLabelCall13 call = reinterpret_cast<CuteEditableAxisLabelCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::mouseMoveEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteEditableAxisLabelCall14 call = reinterpret_cast<CuteEditableAxisLabelCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteEditableAxisLabelCall15 call = reinterpret_cast<CuteEditableAxisLabelCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void
  //      QGraphicsTextItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteEditableAxisLabelCall16 call = reinterpret_cast<CuteEditableAxisLabelCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void
  //      QGraphicsTextItem::contextMenuEvent(QGraphicsSceneContextMenuEven
  //      t *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteEditableAxisLabelCall17 call = reinterpret_cast<CuteEditableAxisLabelCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteEditableAxisLabelCall18 call = reinterpret_cast<CuteEditableAxisLabelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteEditableAxisLabelCall19 call = reinterpret_cast<CuteEditableAxisLabelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteEditableAxisLabelCall20 call = reinterpret_cast<CuteEditableAxisLabelCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteEditableAxisLabelCall21 call = reinterpret_cast<CuteEditableAxisLabelCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::dragMoveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteEditableAxisLabelCall22 call = reinterpret_cast<CuteEditableAxisLabelCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteEditableAxisLabelCall23 call = reinterpret_cast<CuteEditableAxisLabelCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteEditableAxisLabelCall24 call = reinterpret_cast<CuteEditableAxisLabelCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::hoverEnterEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteEditableAxisLabelCall25 call = reinterpret_cast<CuteEditableAxisLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::hoverMoveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteEditableAxisLabelCall26 call = reinterpret_cast<CuteEditableAxisLabelCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteEditableAxisLabelCall27 call = reinterpret_cast<CuteEditableAxisLabelCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsTextItem::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[28]) {
      int handled = 0;
      CuteEditableAxisLabelCall28 call = reinterpret_cast<CuteEditableAxisLabelCall28>(taken[28]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsTextItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[29]) {
      int handled = 0;
      CuteEditableAxisLabelCall29 call = reinterpret_cast<CuteEditableAxisLabelCall29>(taken[29]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[30]) {
      int handled = 0;
      CuteEditableAxisLabelCall30 call = reinterpret_cast<CuteEditableAxisLabelCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteEditableAxisLabelCall31 call = reinterpret_cast<CuteEditableAxisLabelCall31>(taken[31]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteEditableAxisLabelCall32 call = reinterpret_cast<CuteEditableAxisLabelCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteEditableAxisLabelCall33 call = reinterpret_cast<CuteEditableAxisLabelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteEditableAxisLabelCall34 call = reinterpret_cast<CuteEditableAxisLabelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[35]) {
      int handled = 0;
      CuteEditableAxisLabelCall35 call = reinterpret_cast<CuteEditableAxisLabelCall35>(taken[35]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteEditableAxisLabelCall36 call = reinterpret_cast<CuteEditableAxisLabelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[37]) {
      int handled = 0;
      CuteEditableAxisLabelCall37 call = reinterpret_cast<CuteEditableAxisLabelCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteEditableAxisLabelCall38 call = reinterpret_cast<CuteEditableAxisLabelCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteEditableAxisLabelCall39 call = reinterpret_cast<CuteEditableAxisLabelCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteEditableAxisLabelCall40 call = reinterpret_cast<CuteEditableAxisLabelCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteEditableAxisLabelCall41 call = reinterpret_cast<CuteEditableAxisLabelCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[42]) {
      int handled = 0;
      CuteEditableAxisLabelCall42 call = reinterpret_cast<CuteEditableAxisLabelCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *EditableAxisLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17EditableAxisLabel10metaObjectEv(
    const EditableAxisLabel *self) {
  return self->metaObject();
}

//  QString EditableAxisLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17EditableAxisLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(EditableAxisLabel::tr(s, c, n));
}

//  void EditableAxisLabel::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel12focusInEventEP11QFocusEvent(
    EditableAxisLabel *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void EditableAxisLabel::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel13focusOutEventEP11QFocusEvent(
    EditableAxisLabel *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  bool EditableAxisLabel::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17EditableAxisLabel10sceneEventEP6QEvent(
    EditableAxisLabel *self,
    QEvent *event) {
  return self->sceneEvent(event);
}

//  void EditableAxisLabel::setEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel11setEditableEb(
    EditableAxisLabel *self,
    bool editable) {
  self->setEditable(editable);
}

//  void EditableAxisLabel::reloadBeforeEditContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel23reloadBeforeEditContentEv(
    EditableAxisLabel *self) {
  self->reloadBeforeEditContent();
}

//  QRectF EditableAxisLabel::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17EditableAxisLabel12boundingRectEv(
    const EditableAxisLabel *self) {
  return new QRectF(self->boundingRect());
}

//  void EditableAxisLabel::setInitialEditValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel19setInitialEditValueEv(
    EditableAxisLabel *self) {
  self->setInitialEditValue();
}

//  void EditableAxisLabel::finishEditing()
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel13finishEditingEv(EditableAxisLabel *self) {
  self->finishEditing();
}

//  void EditableAxisLabel::resetBeforeEditValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17EditableAxisLabel20resetBeforeEditValueEv(
    EditableAxisLabel *self) {
  self->resetBeforeEditValue();
}

//  bool EditableAxisLabel::isEditEndingKeyPress(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17EditableAxisLabel20isEditEndingKeyPressEP9QKeyEvent(
    EditableAxisLabel *self,
    QKeyEvent *event) {
  return self->isEditEndingKeyPress(event);
}

//  a Python function taken by a CuteEditableAxisLabel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_EditableAxisLabel(
    EditableAxisLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteEditableAxisLabel *>(self)->take(key, call);
}

//  void EditableAxisLabel::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17EditableAxisLabel12focusInEventEP11QFocusEvent(
    EditableAxisLabel *self,
    QFocusEvent *event) {
  self->EditableAxisLabel::focusInEvent(event);
}

//  void EditableAxisLabel::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17EditableAxisLabel13focusOutEventEP11QFocusEvent(
    EditableAxisLabel *self,
    QFocusEvent *event) {
  self->EditableAxisLabel::focusOutEvent(event);
}

//  bool EditableAxisLabel::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17EditableAxisLabel10sceneEventEP6QEvent(
    EditableAxisLabel *self,
    QEvent *event) {
  return self->EditableAxisLabel::sceneEvent(event);
}

//  QRectF EditableAxisLabel::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17EditableAxisLabel12boundingRectEv(
    const EditableAxisLabel *self) {
  return new QRectF(self->EditableAxisLabel::boundingRect());
}
