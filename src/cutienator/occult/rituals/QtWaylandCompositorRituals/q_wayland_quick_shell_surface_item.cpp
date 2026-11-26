//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickshellsurfaceitem.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickshellsurfaceitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandQuickShellSurfaceItem that Python can take functions over in. Every QWaylandQuickShellSurfaceItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland_compositor_quick)
typedef bool (*CuteQWaylandQuickShellSurfaceItemCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandQuickShellSurfaceItemCall1)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef const QVariant * (*CuteQWaylandQuickShellSurfaceItemCall2)(const void *, int, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall6)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall7)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall8)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall11)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall12)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall13)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall15)(const void *, QWaylandSurface *, QWaylandSurface *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall16)(const void *, QWaylandSeat *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void * (*CuteQWaylandQuickShellSurfaceItemCall17)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
typedef const QRectF * (*CuteQWaylandQuickShellSurfaceItemCall18)(const void *, int *);
typedef const QRectF * (*CuteQWaylandQuickShellSurfaceItemCall19)(const void *, int *);
typedef bool (*CuteQWaylandQuickShellSurfaceItemCall20)(const void *, const QPointF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickShellSurfaceItemCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall22)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall23)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall24)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall25)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall29)(const void *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQWaylandQuickShellSurfaceItemCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall35)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickShellSurfaceItemCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellSurfaceItemCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickShellSurfaceItem : public QWaylandQuickShellSurfaceItem {
public:
  using QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem;
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
      CuteQWaylandQuickShellSurfaceItemCall0 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall0>(taken[0]);
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
      CuteQWaylandQuickShellSurfaceItemCall1 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall1>(taken[1]);
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
      CuteQWaylandQuickShellSurfaceItemCall2 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall2>(taken[2]);
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
      CuteQWaylandQuickShellSurfaceItemCall3 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall3>(taken[3]);
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
      CuteQWaylandQuickShellSurfaceItemCall4 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall4>(taken[4]);
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
      CuteQWaylandQuickShellSurfaceItemCall5 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall5>(taken[5]);
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
      CuteQWaylandQuickShellSurfaceItemCall6 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall6>(taken[6]);
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
      CuteQWaylandQuickShellSurfaceItemCall7 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall7>(taken[7]);
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
      CuteQWaylandQuickShellSurfaceItemCall8 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall8>(taken[8]);
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
      CuteQWaylandQuickShellSurfaceItemCall9 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall9>(taken[9]);
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
      CuteQWaylandQuickShellSurfaceItemCall10 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall10>(taken[10]);
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
      CuteQWaylandQuickShellSurfaceItemCall11 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall11>(taken[11]);
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
      CuteQWaylandQuickShellSurfaceItemCall12 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall12>(taken[12]);
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
      CuteQWaylandQuickShellSurfaceItemCall13 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall13>(taken[13]);
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
      CuteQWaylandQuickShellSurfaceItemCall14 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall14>(taken[14]);
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
      CuteQWaylandQuickShellSurfaceItemCall15 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall15>(taken[15]);
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
      CuteQWaylandQuickShellSurfaceItemCall16 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall16>(taken[16]);
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
      CuteQWaylandQuickShellSurfaceItemCall17 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall17>(taken[17]);
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
      CuteQWaylandQuickShellSurfaceItemCall18 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall19 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall19>(taken[19]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall20 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall20>(taken[20]);
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
      CuteQWaylandQuickShellSurfaceItemCall21 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall21>(taken[21]);
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
      CuteQWaylandQuickShellSurfaceItemCall22 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall22>(taken[22]);
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
      CuteQWaylandQuickShellSurfaceItemCall23 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall23>(taken[23]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[24]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall24 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[25]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall25 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall26 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall27 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall28 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall29 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall29>(taken[29]);
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
      CuteQWaylandQuickShellSurfaceItemCall30 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall30>(taken[30]);
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
      CuteQWaylandQuickShellSurfaceItemCall31 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall31>(taken[31]);
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
      CuteQWaylandQuickShellSurfaceItemCall32 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall32>(taken[32]);
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
      CuteQWaylandQuickShellSurfaceItemCall33 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall33>(taken[33]);
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
      CuteQWaylandQuickShellSurfaceItemCall34 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall35 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[36]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemCall36 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall36>(taken[36]);
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
      CuteQWaylandQuickShellSurfaceItemCall37 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall37>(taken[37]);
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
      CuteQWaylandQuickShellSurfaceItemCall38 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall38>(taken[38]);
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
      CuteQWaylandQuickShellSurfaceItemCall39 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall39>(taken[39]);
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
      CuteQWaylandQuickShellSurfaceItemCall40 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall40>(taken[40]);
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
      CuteQWaylandQuickShellSurfaceItemCall41 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall41>(taken[41]);
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
      CuteQWaylandQuickShellSurfaceItemCall42 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickShellSurfaceItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QWaylandQuickShellSurfaceItem10metaObjectEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->metaObject();
}

//  void *QWaylandQuickShellSurfaceItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QWaylandQuickShellSurfaceItem11qt_metacastEPKc(
    QWaylandQuickShellSurfaceItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickShellSurfaceItem::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QWaylandQuickShellSurfaceItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickShellSurfaceItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickShellSurfaceItem::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QWaylandQuickShellSurfaceItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickShellSurfaceItem::tr(s, c, n));
}

//  QWaylandQuickShellSurfaceItemPrivate
//      *QWaylandQuickShellSurfaceItem::d_func()
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItemPrivate *ritual_ZN29QWaylandQuickShellSurfaceItem6d_funcEv(
    QWaylandQuickShellSurfaceItem *self) {
  return self->d_func();
}

//  const QWaylandQuickShellSurfaceItemPrivate
//      *QWaylandQuickShellSurfaceItem::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQuickShellSurfaceItemPrivate *ritual_ZNK29QWaylandQuickShellSurfaceItem6d_funcEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->d_func();
}

//  QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItem *ritual_ZN29QWaylandQuickShellSurfaceItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQWaylandQuickShellSurfaceItem(parent);
}

//  QWaylandQuickShellSurfaceItem::~QWaylandQuickShellSurfaceItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItemD1Ev(
    QWaylandQuickShellSurfaceItem *self) {
  delete self;
}

//  QWaylandShellSurface *QWaylandQuickShellSurfaceItem::shellSurface() const
extern "C" Q_DECL_EXPORT
QWaylandShellSurface *ritual_ZNK29QWaylandQuickShellSurfaceItem12shellSurfaceEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->shellSurface();
}

//  void QWaylandQuickShellSurfaceItem::setShellSurface(QWaylandShellSurface
//      *shellSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem15setShellSurfaceEP20QWaylandShellSurface(
    QWaylandQuickShellSurfaceItem *self,
    QWaylandShellSurface *shellSurface) {
  self->setShellSurface(shellSurface);
}

//  QQuickItem *QWaylandQuickShellSurfaceItem::moveItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK29QWaylandQuickShellSurfaceItem8moveItemEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->moveItem();
}

//  void QWaylandQuickShellSurfaceItem::setMoveItem(QQuickItem *moveItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem11setMoveItemEP10QQuickItem(
    QWaylandQuickShellSurfaceItem *self,
    QQuickItem *moveItem) {
  self->setMoveItem(moveItem);
}

//  bool QWaylandQuickShellSurfaceItem::autoCreatePopupItems()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QWaylandQuickShellSurfaceItem20autoCreatePopupItemsEv(
    QWaylandQuickShellSurfaceItem *self) {
  return self->autoCreatePopupItems();
}

//  void QWaylandQuickShellSurfaceItem::setAutoCreatePopupItems(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem23setAutoCreatePopupItemsEb(
    QWaylandQuickShellSurfaceItem *self,
    bool enabled) {
  self->setAutoCreatePopupItems(enabled);
}

//  bool QWaylandQuickShellSurfaceItem::staysOnTop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWaylandQuickShellSurfaceItem10staysOnTopEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->staysOnTop();
}

//  void QWaylandQuickShellSurfaceItem::setStaysOnTop(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem13setStaysOnTopEb(
    QWaylandQuickShellSurfaceItem *self,
    bool on) {
  self->setStaysOnTop(on);
}

//  bool QWaylandQuickShellSurfaceItem::staysOnBottom() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWaylandQuickShellSurfaceItem13staysOnBottomEv(
    const QWaylandQuickShellSurfaceItem *self) {
  return self->staysOnBottom();
}

//  void QWaylandQuickShellSurfaceItem::setStaysOnBottom(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem16setStaysOnBottomEb(
    QWaylandQuickShellSurfaceItem *self,
    bool on) {
  self->setStaysOnBottom(on);
}

//  void QWaylandQuickShellSurfaceItem::shellSurfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem19shellSurfaceChangedEv(
    QWaylandQuickShellSurfaceItem *self) {
  self->shellSurfaceChanged();
}

//  void QWaylandQuickShellSurfaceItem::moveItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem15moveItemChangedEv(
    QWaylandQuickShellSurfaceItem *self) {
  self->moveItemChanged();
}

//  void QWaylandQuickShellSurfaceItem::autoCreatePopupItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem27autoCreatePopupItemsChangedEv(
    QWaylandQuickShellSurfaceItem *self) {
  self->autoCreatePopupItemsChanged();
}

//  void QWaylandQuickShellSurfaceItem::staysOnTopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem17staysOnTopChangedEv(
    QWaylandQuickShellSurfaceItem *self) {
  self->staysOnTopChanged();
}

//  void QWaylandQuickShellSurfaceItem::staysOnBottomChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellSurfaceItem20staysOnBottomChangedEv(
    QWaylandQuickShellSurfaceItem *self) {
  self->staysOnBottomChanged();
}

//  QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem(QWaylandQuic
//      kShellSurfaceItemPrivate &dd, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItem *ritual_ZN29QWaylandQuickShellSurfaceItemC1ER36QWaylandQuickShellSurfaceItemPrivateP10QQuickItem(
    QWaylandQuickShellSurfaceItemPrivate *dd,
    QQuickItem *parent) {
  return new CuteQWaylandQuickShellSurfaceItem(*dd, parent);
}

//  a Python function taken by a CuteQWaylandQuickShellSurfaceItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickShellSurfaceItem *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
