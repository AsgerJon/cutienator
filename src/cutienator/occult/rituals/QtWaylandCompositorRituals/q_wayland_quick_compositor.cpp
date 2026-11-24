//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickcompositor.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickcompositor.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWaylandQuickCompositor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandQuickCompositor : QWaylandQuickCompositor {
  using QWaylandQuickCompositor::classBegin;
  using QWaylandQuickCompositor::componentComplete;
};

//  A QWaylandQuickCompositor that Python can take functions over in. Every QWaylandQuickCompositor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickCompositorCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickCompositorCall1)(const void *, QWaylandSurfaceGrabber *, const QWaylandBufferRef *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickCompositorCall2)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickCompositorCall3)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickCompositorCall4)(const void *, QMimeData *, int *);
typedef void * (*CuteQWaylandQuickCompositorCall5)(const void *, int *);
typedef void * (*CuteQWaylandQuickCompositorCall6)(const void *, QWaylandSeat *, int *);
typedef void * (*CuteQWaylandQuickCompositorCall7)(const void *, QWaylandSeat *, int *);
typedef void * (*CuteQWaylandQuickCompositorCall8)(const void *, QWaylandSeat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickCompositorCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickCompositorCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickCompositorCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickCompositorCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickCompositorCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickCompositorCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickCompositorCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickCompositor : public QWaylandQuickCompositor {
public:
  using QWaylandQuickCompositor::QWaylandQuickCompositor;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN18QWaylandCompositor6createEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeData")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor10createSeatEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSeat")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickCompositor::create()
  void create() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall0 call = reinterpret_cast<CuteQWaylandQuickCompositorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickCompositor::create();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickCompositor::grabSurface(QWaylandSurfaceGrabber
  //      *grabber, const QWaylandBufferRef &buffer)
  void grabSurface(
      QWaylandSurfaceGrabber *grabber,
      const QWaylandBufferRef &buffer) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall1 call = reinterpret_cast<CuteQWaylandQuickCompositorCall1>(taken[1]);
      call(this, grabber, &buffer, &handled);
      if (handled) return;
    }
    QWaylandQuickCompositor::grabSurface(grabber, buffer);
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickCompositor::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall2 call = reinterpret_cast<CuteQWaylandQuickCompositorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickCompositor::classBegin();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickCompositor::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall3 call = reinterpret_cast<CuteQWaylandQuickCompositorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickCompositor::componentComplete();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

  //  void QWaylandCompositor::retainedSelectionReceived(QMimeData
  //      *mimeData)
  void retainedSelectionReceived(QMimeData *mimeData) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall4 call = reinterpret_cast<CuteQWaylandQuickCompositorCall4>(taken[4]);
      call(this, mimeData, &handled);
      if (handled) return;
    }
    QWaylandCompositor::retainedSelectionReceived(mimeData);
  }

  //  QWaylandSeat *QWaylandCompositor::createSeat()
  QWaylandSeat *createSeat() override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall5 call = reinterpret_cast<CuteQWaylandQuickCompositorCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWaylandSeat *>(given);
    }
    return QWaylandCompositor::createSeat();
  }

  //  QWaylandPointer *QWaylandCompositor::createPointerDevice(QWaylandSeat
  //      *seat)
  QWaylandPointer *createPointerDevice(QWaylandSeat *seat) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall6 call = reinterpret_cast<CuteQWaylandQuickCompositorCall6>(taken[6]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandPointer *>(given);
    }
    return QWaylandCompositor::createPointerDevice(seat);
  }

  //  QWaylandKeyboard
  //      *QWaylandCompositor::createKeyboardDevice(QWaylandSeat *seat)
  QWaylandKeyboard *createKeyboardDevice(QWaylandSeat *seat) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall7 call = reinterpret_cast<CuteQWaylandQuickCompositorCall7>(taken[7]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandKeyboard *>(given);
    }
    return QWaylandCompositor::createKeyboardDevice(seat);
  }

  //  QWaylandTouch *QWaylandCompositor::createTouchDevice(QWaylandSeat
  //      *seat)
  QWaylandTouch *createTouchDevice(QWaylandSeat *seat) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall8 call = reinterpret_cast<CuteQWaylandQuickCompositorCall8>(taken[8]);
      void * given = call(this, seat, &handled);
      if (handled) return static_cast<QWaylandTouch *>(given);
    }
    return QWaylandCompositor::createTouchDevice(seat);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall9 call = reinterpret_cast<CuteQWaylandQuickCompositorCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall10 call = reinterpret_cast<CuteQWaylandQuickCompositorCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall11 call = reinterpret_cast<CuteQWaylandQuickCompositorCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall12 call = reinterpret_cast<CuteQWaylandQuickCompositorCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall13 call = reinterpret_cast<CuteQWaylandQuickCompositorCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall14 call = reinterpret_cast<CuteQWaylandQuickCompositorCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWaylandQuickCompositorCall15 call = reinterpret_cast<CuteQWaylandQuickCompositorCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickCompositor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWaylandQuickCompositor10metaObjectEv(
    const QWaylandQuickCompositor *self) {
  return self->metaObject();
}

//  QString QWaylandQuickCompositor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QWaylandQuickCompositor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickCompositor::tr(s, c, n));
}

//  QWaylandQuickCompositor::QWaylandQuickCompositor(QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickCompositor *ritual_ZN23QWaylandQuickCompositorC1EP7QObject(
    QObject *parent) {
  return new CuteQWaylandQuickCompositor(parent);
}

//  void QWaylandQuickCompositor::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQuickCompositor6createEv(
    QWaylandQuickCompositor *self) {
  self->create();
}

//  void QWaylandQuickCompositor::grabSurface(QWaylandSurfaceGrabber
//      *grabber, const QWaylandBufferRef &buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQuickCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef(
    QWaylandQuickCompositor *self,
    QWaylandSurfaceGrabber *grabber,
    const QWaylandBufferRef *buffer) {
  self->grabSurface(grabber, *buffer);
}

//  void QWaylandQuickCompositor::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQuickCompositor10classBeginEv(
    QWaylandQuickCompositor *self) {
  self->classBegin();
}

//  void QWaylandQuickCompositor::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQuickCompositor17componentCompleteEv(
    QWaylandQuickCompositor *self) {
  self->componentComplete();
}

//  QWaylandQuickCompositor as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQuickCompositor_QQmlParserStatus(
    QWaylandQuickCompositor *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQWaylandQuickCompositor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickCompositor(
    QWaylandQuickCompositor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickCompositor *>(self)->take(key, call);
}

//  void QWaylandQuickCompositor::create()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QWaylandQuickCompositor6createEv(
    QWaylandQuickCompositor *self) {
  self->QWaylandQuickCompositor::create();
}

//  void QWaylandQuickCompositor::grabSurface(QWaylandSurfaceGrabber
//      *grabber, const QWaylandBufferRef &buffer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QWaylandQuickCompositor11grabSurfaceEP22QWaylandSurfaceGrabberRK17QWaylandBufferRef(
    QWaylandQuickCompositor *self,
    QWaylandSurfaceGrabber *grabber,
    const QWaylandBufferRef *buffer) {
  self->QWaylandQuickCompositor::grabSurface(grabber, *buffer);
}

//  void QWaylandQuickCompositor::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QWaylandQuickCompositor10classBeginEv(
    QWaylandQuickCompositor *self) {
  static_cast<OwnQWaylandQuickCompositor *>(self)->OwnQWaylandQuickCompositor::classBegin();
}

//  void QWaylandQuickCompositor::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QWaylandQuickCompositor17componentCompleteEv(
    QWaylandQuickCompositor *self) {
  static_cast<OwnQWaylandQuickCompositor *>(self)->OwnQWaylandQuickCompositor::componentComplete();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
