//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/datetimeaxislabel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_datetime_axis)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/datetimeaxislabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A DateTimeAxisLabel that Python can take functions over in. Every DateTimeAxisLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall0)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall1)(const void *, int *);
typedef void (*CuteDateTimeAxisLabelCall2)(const void *, int *);
typedef void (*CuteDateTimeAxisLabelCall3)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall4)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall5)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteDateTimeAxisLabelCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteDateTimeAxisLabelCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall9)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall10)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall11)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteDateTimeAxisLabelCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteDateTimeAxisLabelCall13)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall14)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall15)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall16)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall17)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall18)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall19)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall20)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall21)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall22)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall23)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall24)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall25)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall27)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteDateTimeAxisLabelCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteDateTimeAxisLabelCall29)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall30)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDateTimeAxisLabelCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDateTimeAxisLabelCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDateTimeAxisLabelCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDateTimeAxisLabelCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDateTimeAxisLabelCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDateTimeAxisLabelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall37)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall38)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall39)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteDateTimeAxisLabelCall40)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteDateTimeAxisLabelCall41)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteDateTimeAxisLabelCall42)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteDateTimeAxisLabel : public DateTimeAxisLabel {
public:
  using DateTimeAxisLabel::DateTimeAxisLabel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN17EditableAxisLabel19setInitialEditValueEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17EditableAxisLabel13finishEditingEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17EditableAxisLabel20resetBeforeEditValueEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
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
  //  void DateTimeAxisLabel::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall0 call = reinterpret_cast<CuteDateTimeAxisLabelCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    DateTimeAxisLabel::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void DateTimeAxisLabel::setInitialEditValue()
  void setInitialEditValue() override {
    if (taken[1]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall1 call = reinterpret_cast<CuteDateTimeAxisLabelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DateTimeAxisLabel::setInitialEditValue();
  }

  //  void DateTimeAxisLabel::finishEditing()
  void finishEditing() override {
    if (taken[2]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall2 call = reinterpret_cast<CuteDateTimeAxisLabelCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    DateTimeAxisLabel::finishEditing();
  }

  //  void DateTimeAxisLabel::resetBeforeEditValue()
  void resetBeforeEditValue() override {
    if (taken[3]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall3 call = reinterpret_cast<CuteDateTimeAxisLabelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    DateTimeAxisLabel::resetBeforeEditValue();
  }

#if QT_CONFIG(graphicsview)
  //  void EditableAxisLabel::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall4 call = reinterpret_cast<CuteDateTimeAxisLabelCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    EditableAxisLabel::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void EditableAxisLabel::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall5 call = reinterpret_cast<CuteDateTimeAxisLabelCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    EditableAxisLabel::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool EditableAxisLabel::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall6 call = reinterpret_cast<CuteDateTimeAxisLabelCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return EditableAxisLabel::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF EditableAxisLabel::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall7 call = reinterpret_cast<CuteDateTimeAxisLabelCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return EditableAxisLabel::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsTextItem::shape() const
  QPainterPath shape() const override {
    if (taken[8]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall8 call = reinterpret_cast<CuteDateTimeAxisLabelCall8>(taken[8]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsTextItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall9 call = reinterpret_cast<CuteDateTimeAxisLabelCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall10 call = reinterpret_cast<CuteDateTimeAxisLabelCall10>(taken[10]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[11]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall11 call = reinterpret_cast<CuteDateTimeAxisLabelCall11>(taken[11]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsTextItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsTextItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[12]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall12 call = reinterpret_cast<CuteDateTimeAxisLabelCall12>(taken[12]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsTextItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsTextItem::type() const
  int type() const override {
    if (taken[13]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall13 call = reinterpret_cast<CuteDateTimeAxisLabelCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall14 call = reinterpret_cast<CuteDateTimeAxisLabelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall15 call = reinterpret_cast<CuteDateTimeAxisLabelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall16 call = reinterpret_cast<CuteDateTimeAxisLabelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall17 call = reinterpret_cast<CuteDateTimeAxisLabelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall18 call = reinterpret_cast<CuteDateTimeAxisLabelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsTextItem::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTextItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteDateTimeAxisLabelCall19 call = reinterpret_cast<CuteDateTimeAxisLabelCall19>(taken[19]);
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
      CuteDateTimeAxisLabelCall20 call = reinterpret_cast<CuteDateTimeAxisLabelCall20>(taken[20]);
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
      CuteDateTimeAxisLabelCall21 call = reinterpret_cast<CuteDateTimeAxisLabelCall21>(taken[21]);
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
      CuteDateTimeAxisLabelCall22 call = reinterpret_cast<CuteDateTimeAxisLabelCall22>(taken[22]);
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
      CuteDateTimeAxisLabelCall23 call = reinterpret_cast<CuteDateTimeAxisLabelCall23>(taken[23]);
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
      CuteDateTimeAxisLabelCall24 call = reinterpret_cast<CuteDateTimeAxisLabelCall24>(taken[24]);
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
      CuteDateTimeAxisLabelCall25 call = reinterpret_cast<CuteDateTimeAxisLabelCall25>(taken[25]);
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
      CuteDateTimeAxisLabelCall26 call = reinterpret_cast<CuteDateTimeAxisLabelCall26>(taken[26]);
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
      CuteDateTimeAxisLabelCall27 call = reinterpret_cast<CuteDateTimeAxisLabelCall27>(taken[27]);
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
      CuteDateTimeAxisLabelCall28 call = reinterpret_cast<CuteDateTimeAxisLabelCall28>(taken[28]);
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
      CuteDateTimeAxisLabelCall29 call = reinterpret_cast<CuteDateTimeAxisLabelCall29>(taken[29]);
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
      CuteDateTimeAxisLabelCall30 call = reinterpret_cast<CuteDateTimeAxisLabelCall30>(taken[30]);
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
      CuteDateTimeAxisLabelCall31 call = reinterpret_cast<CuteDateTimeAxisLabelCall31>(taken[31]);
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
      CuteDateTimeAxisLabelCall32 call = reinterpret_cast<CuteDateTimeAxisLabelCall32>(taken[32]);
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
      CuteDateTimeAxisLabelCall33 call = reinterpret_cast<CuteDateTimeAxisLabelCall33>(taken[33]);
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
      CuteDateTimeAxisLabelCall34 call = reinterpret_cast<CuteDateTimeAxisLabelCall34>(taken[34]);
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
      CuteDateTimeAxisLabelCall35 call = reinterpret_cast<CuteDateTimeAxisLabelCall35>(taken[35]);
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
      CuteDateTimeAxisLabelCall36 call = reinterpret_cast<CuteDateTimeAxisLabelCall36>(taken[36]);
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
      CuteDateTimeAxisLabelCall37 call = reinterpret_cast<CuteDateTimeAxisLabelCall37>(taken[37]);
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
      CuteDateTimeAxisLabelCall38 call = reinterpret_cast<CuteDateTimeAxisLabelCall38>(taken[38]);
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
      CuteDateTimeAxisLabelCall39 call = reinterpret_cast<CuteDateTimeAxisLabelCall39>(taken[39]);
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
      CuteDateTimeAxisLabelCall40 call = reinterpret_cast<CuteDateTimeAxisLabelCall40>(taken[40]);
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
      CuteDateTimeAxisLabelCall41 call = reinterpret_cast<CuteDateTimeAxisLabelCall41>(taken[41]);
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
      CuteDateTimeAxisLabelCall42 call = reinterpret_cast<CuteDateTimeAxisLabelCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *DateTimeAxisLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17DateTimeAxisLabel10metaObjectEv(
    const DateTimeAxisLabel *self) {
  return self->metaObject();
}

//  QString DateTimeAxisLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17DateTimeAxisLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DateTimeAxisLabel::tr(s, c, n));
}

//  DateTimeAxisLabel::DateTimeAxisLabel(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
DateTimeAxisLabel *ritual_ZN17DateTimeAxisLabelC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new CuteDateTimeAxisLabel(parent);
}

//  void DateTimeAxisLabel::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel13keyPressEventEP9QKeyEvent(
    DateTimeAxisLabel *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  QDateTime DateTimeAxisLabel::value() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK17DateTimeAxisLabel5valueEv(
    const DateTimeAxisLabel *self) {
  return new QDateTime(self->value());
}

//  void DateTimeAxisLabel::setValue(const QDateTime &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel8setValueERK9QDateTime(
    DateTimeAxisLabel *self,
    const QDateTime *value) {
  self->setValue(*value);
}

//  void DateTimeAxisLabel::setFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel9setFormatERK7QString(
    DateTimeAxisLabel *self,
    const QString *format) {
  self->setFormat(*format);
}

//  void DateTimeAxisLabel::setInitialEditValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel19setInitialEditValueEv(
    DateTimeAxisLabel *self) {
  self->setInitialEditValue();
}

//  void DateTimeAxisLabel::finishEditing()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel13finishEditingEv(DateTimeAxisLabel *self) {
  self->finishEditing();
}

//  void DateTimeAxisLabel::resetBeforeEditValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DateTimeAxisLabel20resetBeforeEditValueEv(
    DateTimeAxisLabel *self) {
  self->resetBeforeEditValue();
}

//  a Python function taken by a CuteDateTimeAxisLabel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DateTimeAxisLabel(
    DateTimeAxisLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteDateTimeAxisLabel *>(self)->take(key, call);
}

//  void DateTimeAxisLabel::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17DateTimeAxisLabel13keyPressEventEP9QKeyEvent(
    DateTimeAxisLabel *self,
    QKeyEvent *event) {
  self->DateTimeAxisLabel::keyPressEvent(event);
}

//  void DateTimeAxisLabel::setInitialEditValue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17DateTimeAxisLabel19setInitialEditValueEv(
    DateTimeAxisLabel *self) {
  self->DateTimeAxisLabel::setInitialEditValue();
}

//  void DateTimeAxisLabel::finishEditing()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17DateTimeAxisLabel13finishEditingEv(
    DateTimeAxisLabel *self) {
  self->DateTimeAxisLabel::finishEditing();
}

//  void DateTimeAxisLabel::resetBeforeEditValue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17DateTimeAxisLabel20resetBeforeEditValueEv(
    DateTimeAxisLabel *self) {
  self->DateTimeAxisLabel::resetBeforeEditValue();
}

#endif  // QT_CONFIG(charts_datetime_axis)
