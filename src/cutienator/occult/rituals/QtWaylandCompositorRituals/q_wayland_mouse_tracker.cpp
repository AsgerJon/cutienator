//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandmousetracker_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandmousetracker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWaylandMouseTracker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandMouseTracker : QWaylandMouseTracker {
  using QWaylandMouseTracker::childMouseEventFilter;
  using QWaylandMouseTracker::mouseMoveEvent;
  using QWaylandMouseTracker::hoverMoveEvent;
  using QWaylandMouseTracker::hoverEnterEvent;
  using QWaylandMouseTracker::hoverLeaveEvent;
};

//  A QWaylandMouseTracker that Python can take functions over in. Every QWaylandMouseTracker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQWaylandMouseTrackerCall0)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall1)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall2)(const void *, QHoverEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall3)(const void *, QHoverEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall4)(const void *, QHoverEvent *, int *);
typedef const QRectF * (*CuteQWaylandMouseTrackerCall5)(const void *, int *);
typedef const QRectF * (*CuteQWaylandMouseTrackerCall6)(const void *, int *);
typedef bool (*CuteQWaylandMouseTrackerCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQWaylandMouseTrackerCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQWaylandMouseTrackerCall9)(const void *, int *);
typedef void * (*CuteQWaylandMouseTrackerCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandMouseTrackerCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall12)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQWaylandMouseTrackerCall13)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQWaylandMouseTrackerCall14)(const void *, int *);
typedef void (*CuteQWaylandMouseTrackerCall15)(const void *, int *);
typedef void (*CuteQWaylandMouseTrackerCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQWaylandMouseTrackerCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQWaylandMouseTrackerCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandMouseTrackerCall24)(const void *, int *);
typedef void (*CuteQWaylandMouseTrackerCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWaylandMouseTrackerCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWaylandMouseTrackerCall27)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandMouseTrackerCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandMouseTrackerCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandMouseTrackerCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandMouseTrackerCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQWaylandMouseTrackerCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQWaylandMouseTrackerCall33)(const void *, int *);
typedef void (*CuteQWaylandMouseTrackerCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandMouseTrackerCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandMouseTrackerCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandMouseTracker : public QWaylandMouseTracker {
public:
  using QWaylandMouseTracker::QWaylandMouseTracker;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QWaylandMouseTracker::childMouseEventFilter(QQuickItem *item,
  //      QEvent *event)
  bool childMouseEventFilter(QQuickItem *item, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall0 call = reinterpret_cast<CuteQWaylandMouseTrackerCall0>(taken[0]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QWaylandMouseTracker::childMouseEventFilter(item, event);
  }

  //  void QWaylandMouseTracker::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall1 call = reinterpret_cast<CuteQWaylandMouseTrackerCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandMouseTracker::mouseMoveEvent(event);
  }

  //  void QWaylandMouseTracker::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall2 call = reinterpret_cast<CuteQWaylandMouseTrackerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandMouseTracker::hoverMoveEvent(event);
  }

  //  void QWaylandMouseTracker::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall3 call = reinterpret_cast<CuteQWaylandMouseTrackerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandMouseTracker::hoverEnterEvent(event);
  }

  //  void QWaylandMouseTracker::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall4 call = reinterpret_cast<CuteQWaylandMouseTrackerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandMouseTracker::hoverLeaveEvent(event);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall5 call = reinterpret_cast<CuteQWaylandMouseTrackerCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall6 call = reinterpret_cast<CuteQWaylandMouseTrackerCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall7 call = reinterpret_cast<CuteQWaylandMouseTrackerCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall8 call = reinterpret_cast<CuteQWaylandMouseTrackerCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall9 call = reinterpret_cast<CuteQWaylandMouseTrackerCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall10 call = reinterpret_cast<CuteQWaylandMouseTrackerCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall11 call = reinterpret_cast<CuteQWaylandMouseTrackerCall11>(taken[11]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall12 call = reinterpret_cast<CuteQWaylandMouseTrackerCall12>(taken[12]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall13 call = reinterpret_cast<CuteQWaylandMouseTrackerCall13>(taken[13]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall14 call = reinterpret_cast<CuteQWaylandMouseTrackerCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[15]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall15 call = reinterpret_cast<CuteQWaylandMouseTrackerCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall16 call = reinterpret_cast<CuteQWaylandMouseTrackerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall17 call = reinterpret_cast<CuteQWaylandMouseTrackerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall18 call = reinterpret_cast<CuteQWaylandMouseTrackerCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall19 call = reinterpret_cast<CuteQWaylandMouseTrackerCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall20 call = reinterpret_cast<CuteQWaylandMouseTrackerCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall21 call = reinterpret_cast<CuteQWaylandMouseTrackerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall22 call = reinterpret_cast<CuteQWaylandMouseTrackerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall23 call = reinterpret_cast<CuteQWaylandMouseTrackerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall24 call = reinterpret_cast<CuteQWaylandMouseTrackerCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall25 call = reinterpret_cast<CuteQWaylandMouseTrackerCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall26 call = reinterpret_cast<CuteQWaylandMouseTrackerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall27 call = reinterpret_cast<CuteQWaylandMouseTrackerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall28 call = reinterpret_cast<CuteQWaylandMouseTrackerCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall29 call = reinterpret_cast<CuteQWaylandMouseTrackerCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall30 call = reinterpret_cast<CuteQWaylandMouseTrackerCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall31 call = reinterpret_cast<CuteQWaylandMouseTrackerCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall32 call = reinterpret_cast<CuteQWaylandMouseTrackerCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall33 call = reinterpret_cast<CuteQWaylandMouseTrackerCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall34 call = reinterpret_cast<CuteQWaylandMouseTrackerCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall35 call = reinterpret_cast<CuteQWaylandMouseTrackerCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall36 call = reinterpret_cast<CuteQWaylandMouseTrackerCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall37 call = reinterpret_cast<CuteQWaylandMouseTrackerCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall38 call = reinterpret_cast<CuteQWaylandMouseTrackerCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall39 call = reinterpret_cast<CuteQWaylandMouseTrackerCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWaylandMouseTrackerCall40 call = reinterpret_cast<CuteQWaylandMouseTrackerCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandMouseTracker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWaylandMouseTracker10metaObjectEv(
    const QWaylandMouseTracker *self) {
  return self->metaObject();
}

//  QString QWaylandMouseTracker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QWaylandMouseTracker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandMouseTracker::tr(s, c, n));
}

//  QWaylandMouseTracker::QWaylandMouseTracker(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QWaylandMouseTracker *ritual_ZN20QWaylandMouseTrackerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQWaylandMouseTracker(parent);
}

//  qreal QWaylandMouseTracker::mouseX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QWaylandMouseTracker6mouseXEv(
    const QWaylandMouseTracker *self) {
  return self->mouseX();
}

//  qreal QWaylandMouseTracker::mouseY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QWaylandMouseTracker6mouseYEv(
    const QWaylandMouseTracker *self) {
  return self->mouseY();
}

//  void QWaylandMouseTracker::setWindowSystemCursorEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandMouseTracker28setWindowSystemCursorEnabledEb(
    QWaylandMouseTracker *self,
    bool enable) {
  self->setWindowSystemCursorEnabled(enable);
}

//  bool QWaylandMouseTracker::windowSystemCursorEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWaylandMouseTracker25windowSystemCursorEnabledEv(
    const QWaylandMouseTracker *self) {
  return self->windowSystemCursorEnabled();
}

//  bool QWaylandMouseTracker::hovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWaylandMouseTracker7hoveredEv(
    const QWaylandMouseTracker *self) {
  return self->hovered();
}

//  bool QWaylandMouseTracker::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QWaylandMouseTracker21childMouseEventFilterEP10QQuickItemP6QEvent(
    QWaylandMouseTracker *self,
    QQuickItem *item,
    QEvent *event) {
  return self->childMouseEventFilter(item, event);
}

//  void QWaylandMouseTracker::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandMouseTracker14mouseMoveEventEP11QMouseEvent(
    QWaylandMouseTracker *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QWaylandMouseTracker::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandMouseTracker14hoverMoveEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QWaylandMouseTracker::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandMouseTracker15hoverEnterEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QWaylandMouseTracker::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandMouseTracker15hoverLeaveEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  a Python function taken by a CuteQWaylandMouseTracker, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandMouseTracker(
    QWaylandMouseTracker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandMouseTracker *>(self)->take(key, call);
}

//  bool QWaylandMouseTracker::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QWaylandMouseTracker21childMouseEventFilterEP10QQuickItemP6QEvent(
    QWaylandMouseTracker *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQWaylandMouseTracker *>(self)->OwnQWaylandMouseTracker::childMouseEventFilter(
      item,
      event);
}

//  void QWaylandMouseTracker::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWaylandMouseTracker14mouseMoveEventEP11QMouseEvent(
    QWaylandMouseTracker *self,
    QMouseEvent *event) {
  static_cast<OwnQWaylandMouseTracker *>(self)->OwnQWaylandMouseTracker::mouseMoveEvent(
      event);
}

//  void QWaylandMouseTracker::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWaylandMouseTracker14hoverMoveEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandMouseTracker *>(self)->OwnQWaylandMouseTracker::hoverMoveEvent(
      event);
}

//  void QWaylandMouseTracker::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWaylandMouseTracker15hoverEnterEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandMouseTracker *>(self)->OwnQWaylandMouseTracker::hoverEnterEvent(
      event);
}

//  void QWaylandMouseTracker::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWaylandMouseTracker15hoverLeaveEventEP11QHoverEvent(
    QWaylandMouseTracker *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandMouseTracker *>(self)->OwnQWaylandMouseTracker::hoverLeaveEvent(
      event);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
