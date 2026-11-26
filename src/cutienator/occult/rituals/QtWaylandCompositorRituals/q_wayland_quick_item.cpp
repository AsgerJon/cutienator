//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWaylandQuickItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandQuickItem : QWaylandQuickItem {
  using QWaylandQuickItem::mousePressEvent;
  using QWaylandQuickItem::mouseMoveEvent;
  using QWaylandQuickItem::mouseReleaseEvent;
  using QWaylandQuickItem::hoverEnterEvent;
  using QWaylandQuickItem::hoverMoveEvent;
  using QWaylandQuickItem::hoverLeaveEvent;
  using QWaylandQuickItem::wheelEvent;
  using QWaylandQuickItem::keyPressEvent;
  using QWaylandQuickItem::keyReleaseEvent;
  using QWaylandQuickItem::touchEvent;
  using QWaylandQuickItem::touchUngrabEvent;
  using QWaylandQuickItem::inputMethodEvent;
  using QWaylandQuickItem::surfaceChangedEvent;
  using QWaylandQuickItem::updatePaintNode;
};

//  A QWaylandQuickItem that Python can take functions over in. Every QWaylandQuickItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland_compositor_quick)
typedef bool (*CuteQWaylandQuickItemCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandQuickItemCall1)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef const QVariant * (*CuteQWaylandQuickItemCall2)(const void *, int, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall6)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall7)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall8)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall11)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall12)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall13)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall15)(const void *, QWaylandSurface *, QWaylandSurface *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickItemCall16)(const void *, QWaylandSeat *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandQuickItemCall17)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
typedef const QRectF * (*CuteQWaylandQuickItemCall18)(const void *, int *);
typedef const QRectF * (*CuteQWaylandQuickItemCall19)(const void *, int *);
typedef bool (*CuteQWaylandQuickItemCall20)(const void *, const QPointF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickItemCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall22)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQWaylandQuickItemCall23)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQWaylandQuickItemCall24)(const void *, int *);
typedef void (*CuteQWaylandQuickItemCall25)(const void *, int *);
typedef void (*CuteQWaylandQuickItemCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandQuickItemCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandQuickItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandQuickItemCall29)(const void *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQWaylandQuickItemCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQWaylandQuickItemCall35)(const void *, int *);
typedef void (*CuteQWaylandQuickItemCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickItemCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickItemCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickItem : public QWaylandQuickItem {
public:
  using QWaylandQuickItem::QWaylandQuickItem;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylandSurfaceS1_")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[20] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[36] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wayland_compositor_quick)
  //  bool QWaylandQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickItemCall0 call = reinterpret_cast<CuteQWaylandQuickItemCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWaylandQuickItem::isTextureProvider();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  QSGTextureProvider *QWaylandQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickItemCall1 call = reinterpret_cast<CuteQWaylandQuickItemCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QWaylandQuickItem::textureProvider();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
  //  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickItemCall2 call = reinterpret_cast<CuteQWaylandQuickItemCall2>(taken[2]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QWaylandQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickItemCall3 call = reinterpret_cast<CuteQWaylandQuickItemCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandQuickItemCall4 call = reinterpret_cast<CuteQWaylandQuickItemCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandQuickItemCall5 call = reinterpret_cast<CuteQWaylandQuickItemCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandQuickItemCall6 call = reinterpret_cast<CuteQWaylandQuickItemCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickItemCall7 call = reinterpret_cast<CuteQWaylandQuickItemCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickItemCall8 call = reinterpret_cast<CuteQWaylandQuickItemCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandQuickItemCall9 call = reinterpret_cast<CuteQWaylandQuickItemCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandQuickItemCall10 call = reinterpret_cast<CuteQWaylandQuickItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandQuickItemCall11 call = reinterpret_cast<CuteQWaylandQuickItemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaylandQuickItemCall12 call = reinterpret_cast<CuteQWaylandQuickItemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::touchEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaylandQuickItemCall13 call = reinterpret_cast<CuteQWaylandQuickItemCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::touchUngrabEvent();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWaylandQuickItemCall14 call = reinterpret_cast<CuteQWaylandQuickItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::surfaceChangedEvent(QWaylandSurface
  //      *newSurface, QWaylandSurface *oldSurface)
  void surfaceChangedEvent(
      QWaylandSurface *newSurface,
      QWaylandSurface *oldSurface) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWaylandQuickItemCall15 call = reinterpret_cast<CuteQWaylandQuickItemCall15>(taken[15]);
      call(this, newSurface, oldSurface, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::surfaceChangedEvent(newSurface, oldSurface);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickItem::takeFocus(QWaylandSeat *device)
  void takeFocus(QWaylandSeat *device) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWaylandQuickItemCall16 call = reinterpret_cast<CuteQWaylandQuickItemCall16>(taken[16]);
      call(this, device, &handled);
      if (handled) return;
    }
    QWaylandQuickItem::takeFocus(device);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  QSGNode *QWaylandQuickItem::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *data)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWaylandQuickItemCall17 call = reinterpret_cast<CuteQWaylandQuickItemCall17>(taken[17]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QWaylandQuickItem::updatePaintNode(oldNode, data);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQWaylandQuickItemCall18 call = reinterpret_cast<CuteQWaylandQuickItemCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaylandQuickItemCall19 call = reinterpret_cast<CuteQWaylandQuickItemCall19>(taken[19]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQWaylandQuickItemCall20 call = reinterpret_cast<CuteQWaylandQuickItemCall20>(taken[20]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWaylandQuickItemCall21 call = reinterpret_cast<CuteQWaylandQuickItemCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQWaylandQuickItemCall22 call = reinterpret_cast<CuteQWaylandQuickItemCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQWaylandQuickItemCall23 call = reinterpret_cast<CuteQWaylandQuickItemCall23>(taken[23]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[24]) {
      int handled = 0;
      CuteQWaylandQuickItemCall24 call = reinterpret_cast<CuteQWaylandQuickItemCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[25]) {
      int handled = 0;
      CuteQWaylandQuickItemCall25 call = reinterpret_cast<CuteQWaylandQuickItemCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWaylandQuickItemCall26 call = reinterpret_cast<CuteQWaylandQuickItemCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWaylandQuickItemCall27 call = reinterpret_cast<CuteQWaylandQuickItemCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWaylandQuickItemCall28 call = reinterpret_cast<CuteQWaylandQuickItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQWaylandQuickItemCall29 call = reinterpret_cast<CuteQWaylandQuickItemCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWaylandQuickItemCall30 call = reinterpret_cast<CuteQWaylandQuickItemCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWaylandQuickItemCall31 call = reinterpret_cast<CuteQWaylandQuickItemCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWaylandQuickItemCall32 call = reinterpret_cast<CuteQWaylandQuickItemCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWaylandQuickItemCall33 call = reinterpret_cast<CuteQWaylandQuickItemCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQWaylandQuickItemCall34 call = reinterpret_cast<CuteQWaylandQuickItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQWaylandQuickItemCall35 call = reinterpret_cast<CuteQWaylandQuickItemCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[36]) {
      int handled = 0;
      CuteQWaylandQuickItemCall36 call = reinterpret_cast<CuteQWaylandQuickItemCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQWaylandQuickItemCall37 call = reinterpret_cast<CuteQWaylandQuickItemCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQWaylandQuickItemCall38 call = reinterpret_cast<CuteQWaylandQuickItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQWaylandQuickItemCall39 call = reinterpret_cast<CuteQWaylandQuickItemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWaylandQuickItemCall40 call = reinterpret_cast<CuteQWaylandQuickItemCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQWaylandQuickItemCall41 call = reinterpret_cast<CuteQWaylandQuickItemCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQWaylandQuickItemCall42 call = reinterpret_cast<CuteQWaylandQuickItemCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QWaylandQuickItem10metaObjectEv(
    const QWaylandQuickItem *self) {
  return self->metaObject();
}

//  void *QWaylandQuickItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QWaylandQuickItem11qt_metacastEPKc(
    QWaylandQuickItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QWaylandQuickItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QWaylandQuickItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickItem::tr(s, c, n));
}

//  QWaylandQuickItemPrivate *QWaylandQuickItem::d_func()
extern "C" Q_DECL_EXPORT
QWaylandQuickItemPrivate *ritual_ZN17QWaylandQuickItem6d_funcEv(
    QWaylandQuickItem *self) {
  return self->d_func();
}

//  const QWaylandQuickItemPrivate *QWaylandQuickItem::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQuickItemPrivate *ritual_ZNK17QWaylandQuickItem6d_funcEv(
    const QWaylandQuickItem *self) {
  return self->d_func();
}

//  QWaylandQuickItem::QWaylandQuickItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickItem *ritual_ZN17QWaylandQuickItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQWaylandQuickItem(parent);
}

//  QWaylandQuickItem::~QWaylandQuickItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItemD1Ev(QWaylandQuickItem *self) {
  delete self;
}

//  QWaylandCompositor *QWaylandQuickItem::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK17QWaylandQuickItem10compositorEv(
    const QWaylandQuickItem *self) {
  return self->compositor();
}

//  QWaylandView *QWaylandQuickItem::view() const
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZNK17QWaylandQuickItem4viewEv(
    const QWaylandQuickItem *self) {
  return self->view();
}

//  QWaylandSurface *QWaylandQuickItem::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK17QWaylandQuickItem7surfaceEv(
    const QWaylandQuickItem *self) {
  return self->surface();
}

//  void QWaylandQuickItem::setSurface(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10setSurfaceEP15QWaylandSurface(
    QWaylandQuickItem *self,
    QWaylandSurface *surface) {
  self->setSurface(surface);
}

//  QWaylandSurface::Origin QWaylandQuickItem::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface::Origin ritual_ZNK17QWaylandQuickItem6originEv(
    const QWaylandQuickItem *self) {
  return self->origin();
}

//  bool QWaylandQuickItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem17isTextureProviderEv(
    const QWaylandQuickItem *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QWaylandQuickItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK17QWaylandQuickItem15textureProviderEv(
    const QWaylandQuickItem *self) {
  return self->textureProvider();
}

//  bool QWaylandQuickItem::isPaintEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem14isPaintEnabledEv(
    const QWaylandQuickItem *self) {
  return self->isPaintEnabled();
}

//  bool QWaylandQuickItem::touchEventsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem18touchEventsEnabledEv(
    const QWaylandQuickItem *self) {
  return self->touchEventsEnabled();
}

//  void QWaylandQuickItem::setTouchEventsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem21setTouchEventsEnabledEb(
    QWaylandQuickItem *self,
    bool enabled) {
  self->setTouchEventsEnabled(enabled);
}

//  bool QWaylandQuickItem::inputEventsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem18inputEventsEnabledEv(
    const QWaylandQuickItem *self) {
  return self->inputEventsEnabled();
}

//  void QWaylandQuickItem::setInputEventsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem21setInputEventsEnabledEb(
    QWaylandQuickItem *self,
    bool enabled) {
  self->setInputEventsEnabled(enabled);
}

//  bool QWaylandQuickItem::focusOnClick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem12focusOnClickEv(
    const QWaylandQuickItem *self) {
  return self->focusOnClick();
}

//  void QWaylandQuickItem::setFocusOnClick(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15setFocusOnClickEb(
    QWaylandQuickItem *self,
    bool focus) {
  self->setFocusOnClick(focus);
}

//  bool QWaylandQuickItem::inputRegionContains(const QPointF &localPosition)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem19inputRegionContainsERK7QPointF(
    const QWaylandQuickItem *self,
    const QPointF *localPosition) {
  return self->inputRegionContains(*localPosition);
}

//  QPointF QWaylandQuickItem::mapToSurface(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QWaylandQuickItem12mapToSurfaceERK7QPointF(
    const QWaylandQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapToSurface(*point));
}

//  QPointF QWaylandQuickItem::mapFromSurface(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QWaylandQuickItem14mapFromSurfaceERK7QPointF(
    const QWaylandQuickItem *self,
    const QPointF *point) {
  return new QPointF(self->mapFromSurface(*point));
}

#if QT_CONFIG(im)
//  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QWaylandQuickItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery query,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QWaylandQuickItem *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}
#endif  // QT_CONFIG(im)

//  QObject *QWaylandQuickItem::subsurfaceHandler() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QWaylandQuickItem17subsurfaceHandlerEv(
    const QWaylandQuickItem *self) {
  return self->subsurfaceHandler();
}

//  void QWaylandQuickItem::setSubsurfaceHandler(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem20setSubsurfaceHandlerEP7QObject(
    QWaylandQuickItem *self,
    QObject *a0) {
  self->setSubsurfaceHandler(a0);
}

//  QWaylandOutput *QWaylandQuickItem::output() const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK17QWaylandQuickItem6outputEv(
    const QWaylandQuickItem *self) {
  return self->output();
}

//  void QWaylandQuickItem::setOutput(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem9setOutputEP14QWaylandOutput(
    QWaylandQuickItem *self,
    QWaylandOutput *output) {
  self->setOutput(output);
}

//  bool QWaylandQuickItem::isBufferLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem14isBufferLockedEv(
    const QWaylandQuickItem *self) {
  return self->isBufferLocked();
}

//  void QWaylandQuickItem::setBufferLocked(bool locked)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15setBufferLockedEb(
    QWaylandQuickItem *self,
    bool locked) {
  self->setBufferLocked(locked);
}

//  bool QWaylandQuickItem::allowDiscardFrontBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandQuickItem23allowDiscardFrontBufferEv(
    const QWaylandQuickItem *self) {
  return self->allowDiscardFrontBuffer();
}

//  void QWaylandQuickItem::setAllowDiscardFrontBuffer(bool discard)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem26setAllowDiscardFrontBufferEb(
    QWaylandQuickItem *self,
    bool discard) {
  self->setAllowDiscardFrontBuffer(discard);
}

//  void QWaylandQuickItem::setPrimary()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10setPrimaryEv(QWaylandQuickItem *self) {
  self->setPrimary();
}

//  void QWaylandQuickItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15mousePressEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QWaylandQuickItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem14mouseMoveEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QWaylandQuickItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem17mouseReleaseEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QWaylandQuickItem::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15hoverEnterEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QWaylandQuickItem::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem14hoverMoveEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QWaylandQuickItem::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15hoverLeaveEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QWaylandQuickItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10wheelEventEP11QWheelEvent(
    QWaylandQuickItem *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QWaylandQuickItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem13keyPressEventEP9QKeyEvent(
    QWaylandQuickItem *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QWaylandQuickItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15keyReleaseEventEP9QKeyEvent(
    QWaylandQuickItem *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QWaylandQuickItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10touchEventEP11QTouchEvent(
    QWaylandQuickItem *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QWaylandQuickItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem16touchUngrabEventEv(
    QWaylandQuickItem *self) {
  self->touchUngrabEvent();
}

#if QT_CONFIG(im)
//  void QWaylandQuickItem::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem16inputMethodEventEP17QInputMethodEvent(
    QWaylandQuickItem *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}
#endif  // QT_CONFIG(im)

//  void QWaylandQuickItem::surfaceChangedEvent(QWaylandSurface *newSurface,
//      QWaylandSurface *oldSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylandSurfaceS1_(
    QWaylandQuickItem *self,
    QWaylandSurface *newSurface,
    QWaylandSurface *oldSurface) {
  self->surfaceChangedEvent(newSurface, oldSurface);
}

//  void QWaylandQuickItem::takeFocus(QWaylandSeat *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat(
    QWaylandQuickItem *self,
    QWaylandSeat *device) {
  self->takeFocus(device);
}

//  void QWaylandQuickItem::setPaintEnabled(bool paintEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem15setPaintEnabledEb(
    QWaylandQuickItem *self,
    bool paintEnabled) {
  self->setPaintEnabled(paintEnabled);
}

//  void QWaylandQuickItem::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem5raiseEv(QWaylandQuickItem *self) {
  self->raise();
}

//  void QWaylandQuickItem::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem5lowerEv(QWaylandQuickItem *self) {
  self->lower();
}

//  void QWaylandQuickItem::sendMouseMoveEvent(const QPointF &position,
//      QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem18sendMouseMoveEventERK7QPointFP12QWaylandSeat(
    QWaylandQuickItem *self,
    const QPointF *position,
    QWaylandSeat *seat) {
  self->sendMouseMoveEvent(*position, seat);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QWaylandQuickItem::surfaceMappedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem20surfaceMappedChangedEv(
    QWaylandQuickItem *self) {
  self->surfaceMappedChanged();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QWaylandQuickItem::handleSurfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem20handleSurfaceChangedEv(
    QWaylandQuickItem *self) {
  self->handleSurfaceChanged();
}

//  void QWaylandQuickItem::handleBufferLockedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem25handleBufferLockedChangedEv(
    QWaylandQuickItem *self) {
  self->handleBufferLockedChanged();
}

//  void QWaylandQuickItem::parentChanged(QWaylandSurface *newParent,
//      QWaylandSurface *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem13parentChangedEP15QWaylandSurfaceS1_(
    QWaylandQuickItem *self,
    QWaylandSurface *newParent,
    QWaylandSurface *oldParent) {
  self->parentChanged(newParent, oldParent);
}

//  void QWaylandQuickItem::updateSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10updateSizeEv(QWaylandQuickItem *self) {
  self->updateSize();
}

//  void QWaylandQuickItem::updateBuffer(bool hasBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem12updateBufferEb(
    QWaylandQuickItem *self,
    bool hasBuffer) {
  self->updateBuffer(hasBuffer);
}

//  void QWaylandQuickItem::updateWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem12updateWindowEv(QWaylandQuickItem *self) {
  self->updateWindow();
}

//  void QWaylandQuickItem::updateOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem12updateOutputEv(QWaylandQuickItem *self) {
  self->updateOutput();
}

//  void QWaylandQuickItem::beforeSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem10beforeSyncEv(QWaylandQuickItem *self) {
  self->beforeSync();
}

//  void QWaylandQuickItem::handleSubsurfaceAdded(QWaylandSurface
//      *childSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem21handleSubsurfaceAddedEP15QWaylandSurface(
    QWaylandQuickItem *self,
    QWaylandSurface *childSurface) {
  self->handleSubsurfaceAdded(childSurface);
}

//  void QWaylandQuickItem::handleSubsurfacePosition(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem24handleSubsurfacePositionERK6QPoint(
    QWaylandQuickItem *self,
    const QPoint *pos) {
  self->handleSubsurfacePosition(*pos);
}

//  void QWaylandQuickItem::handlePlaceAbove(QWaylandSurface
//      *referenceSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem16handlePlaceAboveEP15QWaylandSurface(
    QWaylandQuickItem *self,
    QWaylandSurface *referenceSurface) {
  self->handlePlaceAbove(referenceSurface);
}

//  void QWaylandQuickItem::handlePlaceBelow(QWaylandSurface
//      *referenceSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem16handlePlaceBelowEP15QWaylandSurface(
    QWaylandQuickItem *self,
    QWaylandSurface *referenceSurface) {
  self->handlePlaceBelow(referenceSurface);
}

#if QT_CONFIG(draganddrop)
//  void QWaylandQuickItem::handleDragStarted(QWaylandDrag *drag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem17handleDragStartedEP12QWaylandDrag(
    QWaylandQuickItem *self,
    QWaylandDrag *drag) {
  self->handleDragStarted(drag);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(im)
//  void QWaylandQuickItem::updateInputMethod(Qt::InputMethodQueries queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem17updateInputMethodE6QFlagsIN2Qt16InputMethodQueryEE(
    QWaylandQuickItem *self,
    int queries) {
  self->updateInputMethod(QFlags<Qt::InputMethodQuery>::fromInt(queries));
}
#endif  // QT_CONFIG(im)

//  void QWaylandQuickItem::updateFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem11updateFocusEv(QWaylandQuickItem *self) {
  self->updateFocus();
}

//  void QWaylandQuickItem::surfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem14surfaceChangedEv(
    QWaylandQuickItem *self) {
  self->surfaceChanged();
}

//  void QWaylandQuickItem::compositorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem17compositorChangedEv(
    QWaylandQuickItem *self) {
  self->compositorChanged();
}

//  void QWaylandQuickItem::paintEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem19paintEnabledChangedEv(
    QWaylandQuickItem *self) {
  self->paintEnabledChanged();
}

//  void QWaylandQuickItem::touchEventsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem25touchEventsEnabledChangedEv(
    QWaylandQuickItem *self) {
  self->touchEventsEnabledChanged();
}

//  void QWaylandQuickItem::originChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem13originChangedEv(QWaylandQuickItem *self) {
  self->originChanged();
}

//  void QWaylandQuickItem::surfaceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem16surfaceDestroyedEv(
    QWaylandQuickItem *self) {
  self->surfaceDestroyed();
}

//  void QWaylandQuickItem::inputEventsEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem25inputEventsEnabledChangedEv(
    QWaylandQuickItem *self) {
  self->inputEventsEnabledChanged();
}

//  void QWaylandQuickItem::focusOnClickChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem19focusOnClickChangedEv(
    QWaylandQuickItem *self) {
  self->focusOnClickChanged();
}

//  void QWaylandQuickItem::mouseMove(const QPointF &windowPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem9mouseMoveERK7QPointF(
    QWaylandQuickItem *self,
    const QPointF *windowPosition) {
  self->mouseMove(*windowPosition);
}

//  void QWaylandQuickItem::mouseRelease()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem12mouseReleaseEv(QWaylandQuickItem *self) {
  self->mouseRelease();
}

//  void QWaylandQuickItem::subsurfaceHandlerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem24subsurfaceHandlerChangedEv(
    QWaylandQuickItem *self) {
  self->subsurfaceHandlerChanged();
}

//  void QWaylandQuickItem::outputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem13outputChangedEv(QWaylandQuickItem *self) {
  self->outputChanged();
}

//  void QWaylandQuickItem::bufferLockedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem19bufferLockedChangedEv(
    QWaylandQuickItem *self) {
  self->bufferLockedChanged();
}

//  void QWaylandQuickItem::allowDiscardFrontBufferChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandQuickItem30allowDiscardFrontBufferChangedEv(
    QWaylandQuickItem *self) {
  self->allowDiscardFrontBufferChanged();
}

//  QSGNode *QWaylandQuickItem::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QWaylandQuickItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QWaylandQuickItem *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updatePaintNode(oldNode, data);
}

//  QWaylandQuickItem::QWaylandQuickItem(QWaylandQuickItemPrivate &dd,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickItem *ritual_ZN17QWaylandQuickItemC1ER24QWaylandQuickItemPrivateP10QQuickItem(
    QWaylandQuickItemPrivate *dd,
    QQuickItem *parent) {
  return new CuteQWaylandQuickItem(*dd, parent);
}

//  a Python function taken by a CuteQWaylandQuickItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickItem(
    QWaylandQuickItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickItem *>(self)->take(key, call);
}

//  bool QWaylandQuickItem::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QWaylandQuickItem17isTextureProviderEv(
    const QWaylandQuickItem *self) {
  return self->QWaylandQuickItem::isTextureProvider();
}

//  QSGTextureProvider *QWaylandQuickItem::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK17QWaylandQuickItem15textureProviderEv(
    const QWaylandQuickItem *self) {
  return self->QWaylandQuickItem::textureProvider();
}

#if QT_CONFIG(im)
//  QVariant QWaylandQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QWaylandQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QWaylandQuickItem *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QWaylandQuickItem::inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  void QWaylandQuickItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem15mousePressEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::mousePressEvent(
      event);
}

//  void QWaylandQuickItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem14mouseMoveEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::mouseMoveEvent(
      event);
}

//  void QWaylandQuickItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem17mouseReleaseEventEP11QMouseEvent(
    QWaylandQuickItem *self,
    QMouseEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::mouseReleaseEvent(
      event);
}

//  void QWaylandQuickItem::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem15hoverEnterEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::hoverEnterEvent(
      event);
}

//  void QWaylandQuickItem::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem14hoverMoveEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::hoverMoveEvent(
      event);
}

//  void QWaylandQuickItem::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem15hoverLeaveEventEP11QHoverEvent(
    QWaylandQuickItem *self,
    QHoverEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::hoverLeaveEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QWaylandQuickItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem10wheelEventEP11QWheelEvent(
    QWaylandQuickItem *self,
    QWheelEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QWaylandQuickItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem13keyPressEventEP9QKeyEvent(
    QWaylandQuickItem *self,
    QKeyEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::keyPressEvent(
      event);
}

//  void QWaylandQuickItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem15keyReleaseEventEP9QKeyEvent(
    QWaylandQuickItem *self,
    QKeyEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::keyReleaseEvent(
      event);
}

//  void QWaylandQuickItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem10touchEventEP11QTouchEvent(
    QWaylandQuickItem *self,
    QTouchEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::touchEvent(
      event);
}

//  void QWaylandQuickItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem16touchUngrabEventEv(
    QWaylandQuickItem *self) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::touchUngrabEvent();
}

#if QT_CONFIG(im)
//  void QWaylandQuickItem::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem16inputMethodEventEP17QInputMethodEvent(
    QWaylandQuickItem *self,
    QInputMethodEvent *event) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::inputMethodEvent(
      event);
}
#endif  // QT_CONFIG(im)

//  void QWaylandQuickItem::surfaceChangedEvent(QWaylandSurface *newSurface,
//      QWaylandSurface *oldSurface)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem19surfaceChangedEventEP15QWaylandSurfaceS1_(
    QWaylandQuickItem *self,
    QWaylandSurface *newSurface,
    QWaylandSurface *oldSurface) {
  static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::surfaceChangedEvent(
      newSurface,
      oldSurface);
}

//  void QWaylandQuickItem::takeFocus(QWaylandSeat *device)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWaylandQuickItem9takeFocusEP12QWaylandSeat(
    QWaylandQuickItem *self,
    QWaylandSeat *device) {
  self->QWaylandQuickItem::takeFocus(device);
}

//  QSGNode *QWaylandQuickItem::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN17QWaylandQuickItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QWaylandQuickItem *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return static_cast<OwnQWaylandQuickItem *>(self)->OwnQWaylandQuickItem::updatePaintNode(
      oldNode,
      data);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
