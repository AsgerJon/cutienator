//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/legendmarkeritem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/legendmarkeritem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qimage.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A LegendMarkerItem that Python can take functions over in. Every LegendMarkerItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteLegendMarkerItemCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteLegendMarkerItemCall3)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall4)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall5)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLegendMarkerItemCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLegendMarkerItemCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLegendMarkerItemCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLegendMarkerItemCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLegendMarkerItemCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLegendMarkerItemCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall13)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall14)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall15)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteLegendMarkerItemCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall17)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall18)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall19)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall20)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteLegendMarkerItemCall21)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteLegendMarkerItemCall22)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall23)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendMarkerItemCall24)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall25)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall26)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall27)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall28)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall29)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall30)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall31)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall32)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall33)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall34)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall35)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall36)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall37)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall38)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall39)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendMarkerItemCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLegendMarkerItemCall41)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLegendMarkerItemCall42)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteLegendMarkerItemCall43)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteLegendMarkerItem : public LegendMarkerItem {
public:
  using LegendMarkerItem::LegendMarkerItem;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
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
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void LegendMarkerItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteLegendMarkerItemCall0 call = reinterpret_cast<CuteLegendMarkerItemCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LegendMarkerItem::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF LegendMarkerItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteLegendMarkerItemCall1 call = reinterpret_cast<CuteLegendMarkerItemCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return LegendMarkerItem::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LegendMarkerItem::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      CuteLegendMarkerItemCall2 call = reinterpret_cast<CuteLegendMarkerItemCall2>(taken[2]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    LegendMarkerItem::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF LegendMarkerItem::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[3]) {
      int handled = 0;
      CuteLegendMarkerItemCall3 call = reinterpret_cast<CuteLegendMarkerItemCall3>(taken[3]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return LegendMarkerItem::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LegendMarkerItem::hoverEnterEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteLegendMarkerItemCall4 call = reinterpret_cast<CuteLegendMarkerItemCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    LegendMarkerItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LegendMarkerItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteLegendMarkerItemCall5 call = reinterpret_cast<CuteLegendMarkerItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    LegendMarkerItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[6]) {
      int handled = 0;
      CuteLegendMarkerItemCall6 call = reinterpret_cast<CuteLegendMarkerItemCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteLegendMarkerItemCall7 call = reinterpret_cast<CuteLegendMarkerItemCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteLegendMarkerItemCall8 call = reinterpret_cast<CuteLegendMarkerItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteLegendMarkerItemCall9 call = reinterpret_cast<CuteLegendMarkerItemCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteLegendMarkerItemCall10 call = reinterpret_cast<CuteLegendMarkerItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteLegendMarkerItemCall11 call = reinterpret_cast<CuteLegendMarkerItemCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteLegendMarkerItemCall12 call = reinterpret_cast<CuteLegendMarkerItemCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutItem::updateGeometry()
  void updateGeometry() override {
    if (taken[13]) {
      int handled = 0;
      CuteLegendMarkerItemCall13 call = reinterpret_cast<CuteLegendMarkerItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[14]) {
      int handled = 0;
      CuteLegendMarkerItemCall14 call = reinterpret_cast<CuteLegendMarkerItemCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[15]) {
      int handled = 0;
      CuteLegendMarkerItemCall15 call = reinterpret_cast<CuteLegendMarkerItemCall15>(taken[15]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[16]) {
      int handled = 0;
      CuteLegendMarkerItemCall16 call = reinterpret_cast<CuteLegendMarkerItemCall16>(taken[16]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[17]) {
      int handled = 0;
      CuteLegendMarkerItemCall17 call = reinterpret_cast<CuteLegendMarkerItemCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteLegendMarkerItemCall18 call = reinterpret_cast<CuteLegendMarkerItemCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteLegendMarkerItemCall19 call = reinterpret_cast<CuteLegendMarkerItemCall19>(taken[19]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[20]) {
      int handled = 0;
      CuteLegendMarkerItemCall20 call = reinterpret_cast<CuteLegendMarkerItemCall20>(taken[20]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[21]) {
      int handled = 0;
      CuteLegendMarkerItemCall21 call = reinterpret_cast<CuteLegendMarkerItemCall21>(taken[21]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[22]) {
      int handled = 0;
      CuteLegendMarkerItemCall22 call = reinterpret_cast<CuteLegendMarkerItemCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteLegendMarkerItemCall23 call = reinterpret_cast<CuteLegendMarkerItemCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteLegendMarkerItemCall24 call = reinterpret_cast<CuteLegendMarkerItemCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteLegendMarkerItemCall25 call = reinterpret_cast<CuteLegendMarkerItemCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteLegendMarkerItemCall26 call = reinterpret_cast<CuteLegendMarkerItemCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteLegendMarkerItemCall27 call = reinterpret_cast<CuteLegendMarkerItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteLegendMarkerItemCall28 call = reinterpret_cast<CuteLegendMarkerItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteLegendMarkerItemCall29 call = reinterpret_cast<CuteLegendMarkerItemCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteLegendMarkerItemCall30 call = reinterpret_cast<CuteLegendMarkerItemCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteLegendMarkerItemCall31 call = reinterpret_cast<CuteLegendMarkerItemCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteLegendMarkerItemCall32 call = reinterpret_cast<CuteLegendMarkerItemCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteLegendMarkerItemCall33 call = reinterpret_cast<CuteLegendMarkerItemCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteLegendMarkerItemCall34 call = reinterpret_cast<CuteLegendMarkerItemCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteLegendMarkerItemCall35 call = reinterpret_cast<CuteLegendMarkerItemCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteLegendMarkerItemCall36 call = reinterpret_cast<CuteLegendMarkerItemCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteLegendMarkerItemCall37 call = reinterpret_cast<CuteLegendMarkerItemCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteLegendMarkerItemCall38 call = reinterpret_cast<CuteLegendMarkerItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteLegendMarkerItemCall39 call = reinterpret_cast<CuteLegendMarkerItemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteLegendMarkerItemCall40 call = reinterpret_cast<CuteLegendMarkerItemCall40>(taken[40]);
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
    if (taken[41]) {
      int handled = 0;
      CuteLegendMarkerItemCall41 call = reinterpret_cast<CuteLegendMarkerItemCall41>(taken[41]);
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
    if (taken[42]) {
      int handled = 0;
      CuteLegendMarkerItemCall42 call = reinterpret_cast<CuteLegendMarkerItemCall42>(taken[42]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[43]) {
      int handled = 0;
      CuteLegendMarkerItemCall43 call = reinterpret_cast<CuteLegendMarkerItemCall43>(taken[43]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *LegendMarkerItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16LegendMarkerItem10metaObjectEv(
    const LegendMarkerItem *self) {
  return self->metaObject();
}

//  QString LegendMarkerItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16LegendMarkerItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LegendMarkerItem::tr(s, c, n));
}

//  LegendMarkerItem::LegendMarkerItem(QLegendMarkerPrivate *marker,
//      QGraphicsObject *parent)
extern "C" Q_DECL_EXPORT
LegendMarkerItem *ritual_ZN16LegendMarkerItemC1EP20QLegendMarkerPrivateP15QGraphicsObject(
    QLegendMarkerPrivate *marker,
    QGraphicsObject *parent) {
  return new CuteLegendMarkerItem(marker, parent);
}

//  LegendMarkerItem::~LegendMarkerItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItemD1Ev(LegendMarkerItem *self) {
  delete self;
}

//  void LegendMarkerItem::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem6setPenERK4QPen(
    LegendMarkerItem *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QPen LegendMarkerItem::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK16LegendMarkerItem3penEv(const LegendMarkerItem *self) {
  return new QPen(self->pen());
}

//  void LegendMarkerItem::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem8setBrushERK6QBrush(
    LegendMarkerItem *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush LegendMarkerItem::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK16LegendMarkerItem5brushEv(const LegendMarkerItem *self) {
  return new QBrush(self->brush());
}

//  void LegendMarkerItem::setSeriesPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem12setSeriesPenERK4QPen(
    LegendMarkerItem *self,
    const QPen *pen) {
  self->setSeriesPen(*pen);
}

//  void LegendMarkerItem::setSeriesBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem14setSeriesBrushERK6QBrush(
    LegendMarkerItem *self,
    const QBrush *brush) {
  self->setSeriesBrush(*brush);
}

//  void LegendMarkerItem::setSeriesLightMarker(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem20setSeriesLightMarkerERK6QImage(
    LegendMarkerItem *self,
    const QImage *image) {
  self->setSeriesLightMarker(*image);
}

//  void LegendMarkerItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem7setFontERK5QFont(
    LegendMarkerItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QFont LegendMarkerItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16LegendMarkerItem4fontEv(const LegendMarkerItem *self) {
  return new QFont(self->font());
}

//  void LegendMarkerItem::setLabel(const QString label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem8setLabelE7QString(
    LegendMarkerItem *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString LegendMarkerItem::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16LegendMarkerItem5labelEv(const LegendMarkerItem *self) {
  return new QString(self->label());
}

//  void LegendMarkerItem::setLabelBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem13setLabelBrushERK6QBrush(
    LegendMarkerItem *self,
    const QBrush *brush) {
  self->setLabelBrush(*brush);
}

//  QBrush LegendMarkerItem::labelBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK16LegendMarkerItem10labelBrushEv(
    const LegendMarkerItem *self) {
  return new QBrush(self->labelBrush());
}

//  void LegendMarkerItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem11setGeometryERK6QRectF(
    LegendMarkerItem *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QRectF LegendMarkerItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16LegendMarkerItem12boundingRectEv(
    const LegendMarkerItem *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF LegendMarkerItem::markerRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16LegendMarkerItem10markerRectEv(
    const LegendMarkerItem *self) {
  return new QRectF(self->markerRect());
}

//  void LegendMarkerItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LegendMarkerItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QSizeF LegendMarkerItem::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK16LegendMarkerItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const LegendMarkerItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void LegendMarkerItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LegendMarkerItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void LegendMarkerItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LegendMarkerItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  QString LegendMarkerItem::displayedLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16LegendMarkerItem14displayedLabelEv(
    const LegendMarkerItem *self) {
  return new QString(self->displayedLabel());
}

//  void LegendMarkerItem::setToolTip(const QString &tooltip)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem10setToolTipERK7QString(
    LegendMarkerItem *self,
    const QString *tooltip) {
  self->setToolTip(*tooltip);
}

//  QLegend::MarkerShape LegendMarkerItem::markerShape() const
extern "C" Q_DECL_EXPORT
QLegend::MarkerShape ritual_ZNK16LegendMarkerItem11markerShapeEv(
    const LegendMarkerItem *self) {
  return self->markerShape();
}

//  void LegendMarkerItem::setMarkerShape(QLegend::MarkerShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem14setMarkerShapeEN7QLegend11MarkerShapeE(
    LegendMarkerItem *self,
    QLegend::MarkerShape shape) {
  self->setMarkerShape(shape);
}

//  void LegendMarkerItem::updateMarkerShapeAndSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem24updateMarkerShapeAndSizeEv(
    LegendMarkerItem *self) {
  self->updateMarkerShapeAndSize();
}

//  QLegend::MarkerShape LegendMarkerItem::effectiveMarkerShape() const
extern "C" Q_DECL_EXPORT
QLegend::MarkerShape ritual_ZNK16LegendMarkerItem20effectiveMarkerShapeEv(
    const LegendMarkerItem *self) {
  return self->effectiveMarkerShape();
}

//  qreal LegendMarkerItem::effectiveMarkerWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16LegendMarkerItem20effectiveMarkerWidthEv(
    const LegendMarkerItem *self) {
  return self->effectiveMarkerWidth();
}

//  ItemType LegendMarkerItem::itemType() const
extern "C" Q_DECL_EXPORT
LegendMarkerItem::ItemType ritual_ZNK16LegendMarkerItem8itemTypeEv(
    const LegendMarkerItem *self) {
  return self->itemType();
}

//  void LegendMarkerItem::setItemBrushAndPen()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem18setItemBrushAndPenEv(
    LegendMarkerItem *self) {
  self->setItemBrushAndPen();
}

//  void LegendMarkerItem::setItemRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LegendMarkerItem11setItemRectEv(LegendMarkerItem *self) {
  self->setItemRect();
}

//  bool LegendMarkerItem::useMaxWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16LegendMarkerItem11useMaxWidthEv(
    const LegendMarkerItem *self) {
  return self->useMaxWidth();
}

//  LegendMarkerItem as the QGraphicsLayoutItem it is built on
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_cast_LegendMarkerItem_QGraphicsLayoutItem(
    LegendMarkerItem *self) {
  return static_cast<QGraphicsLayoutItem *>(self);
}

//  a Python function taken by a CuteLegendMarkerItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LegendMarkerItem(
    LegendMarkerItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteLegendMarkerItem *>(self)->take(key, call);
}

//  void LegendMarkerItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LegendMarkerItem11setGeometryERK6QRectF(
    LegendMarkerItem *self,
    const QRectF *rect) {
  self->LegendMarkerItem::setGeometry(*rect);
}

//  QRectF LegendMarkerItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK16LegendMarkerItem12boundingRectEv(
    const LegendMarkerItem *self) {
  return new QRectF(self->LegendMarkerItem::boundingRect());
}

//  void LegendMarkerItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LegendMarkerItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LegendMarkerItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->LegendMarkerItem::paint(painter, option, widget);
}

//  QSizeF LegendMarkerItem::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK16LegendMarkerItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const LegendMarkerItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->LegendMarkerItem::sizeHint(which, *constraint));
}

//  void LegendMarkerItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LegendMarkerItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LegendMarkerItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->LegendMarkerItem::hoverEnterEvent(event);
}

//  void LegendMarkerItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LegendMarkerItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LegendMarkerItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->LegendMarkerItem::hoverLeaveEvent(event);
}
