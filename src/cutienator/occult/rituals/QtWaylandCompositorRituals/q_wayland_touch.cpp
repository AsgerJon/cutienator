//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtouch.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandtouch.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandTouch that Python can take functions over in. Every QWaylandTouch
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef uint (*CuteQWaylandTouchCall0)(const void *, QWaylandSurface *, int, const QPointF *, int, int *);
typedef void (*CuteQWaylandTouchCall1)(const void *, QWaylandClient *, int *);
typedef void (*CuteQWaylandTouchCall2)(const void *, QWaylandClient *, int *);
typedef void (*CuteQWaylandTouchCall3)(const void *, QWaylandSurface *, QTouchEvent *, int *);
typedef void (*CuteQWaylandTouchCall4)(const void *, QWaylandClient *, uint32_t, uint32_t, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandTouchCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandTouchCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandTouchCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandTouchCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandTouchCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandTouchCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandTouchCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandTouch : public QWaylandTouch {
public:
  using QWaylandTouch::QWaylandTouch;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSurfaceiRK7QPointFN2Qt15TouchPointStateE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurfaceP11QTouchEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWaylandTouch9addClientEP14QWaylandClientjj")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  uint QWaylandTouch::sendTouchPointEvent(QWaylandSurface *surface, int
  //      id, const QPointF &position, Qt::TouchPointState state)
  uint sendTouchPointEvent(
      QWaylandSurface *surface,
      int id,
      const QPointF &position,
      Qt::TouchPointState state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandTouchCall0 call = reinterpret_cast<CuteQWaylandTouchCall0>(taken[0]);
      uint given = call(this, surface, id, &position, static_cast<int>(state), &handled);
      if (handled) return given;
    }
    return QWaylandTouch::sendTouchPointEvent(surface, id, position, state);
  }

  //  void QWaylandTouch::sendFrameEvent(QWaylandClient *client)
  void sendFrameEvent(QWaylandClient *client) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandTouchCall1 call = reinterpret_cast<CuteQWaylandTouchCall1>(taken[1]);
      call(this, client, &handled);
      if (handled) return;
    }
    QWaylandTouch::sendFrameEvent(client);
  }

  //  void QWaylandTouch::sendCancelEvent(QWaylandClient *client)
  void sendCancelEvent(QWaylandClient *client) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandTouchCall2 call = reinterpret_cast<CuteQWaylandTouchCall2>(taken[2]);
      call(this, client, &handled);
      if (handled) return;
    }
    QWaylandTouch::sendCancelEvent(client);
  }

  //  void QWaylandTouch::sendFullTouchEvent(QWaylandSurface *surface,
  //      QTouchEvent *event)
  void sendFullTouchEvent(
      QWaylandSurface *surface,
      QTouchEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandTouchCall3 call = reinterpret_cast<CuteQWaylandTouchCall3>(taken[3]);
      call(this, surface, event, &handled);
      if (handled) return;
    }
    QWaylandTouch::sendFullTouchEvent(surface, event);
  }

  //  void QWaylandTouch::addClient(QWaylandClient *client, uint32_t id,
  //      uint32_t version)
  void addClient(
      QWaylandClient *client,
      uint32_t id,
      uint32_t version) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandTouchCall4 call = reinterpret_cast<CuteQWaylandTouchCall4>(taken[4]);
      call(this, client, id, version, &handled);
      if (handled) return;
    }
    QWaylandTouch::addClient(client, id, version);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandTouchCall5 call = reinterpret_cast<CuteQWaylandTouchCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandTouchCall6 call = reinterpret_cast<CuteQWaylandTouchCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandTouchCall7 call = reinterpret_cast<CuteQWaylandTouchCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandTouchCall8 call = reinterpret_cast<CuteQWaylandTouchCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandTouchCall9 call = reinterpret_cast<CuteQWaylandTouchCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandTouchCall10 call = reinterpret_cast<CuteQWaylandTouchCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandTouchCall11 call = reinterpret_cast<CuteQWaylandTouchCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandTouch::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWaylandTouch10metaObjectEv(
    const QWaylandTouch *self) {
  return self->metaObject();
}

//  void *QWaylandTouch::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QWaylandTouch11qt_metacastEPKc(
    QWaylandTouch *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandTouch::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QWaylandTouch11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandTouch *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandTouch::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QWaylandTouch2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandTouch::tr(s, c, n));
}

//  QWaylandTouchPrivate *QWaylandTouch::d_func()
extern "C" Q_DECL_EXPORT
QWaylandTouchPrivate *ritual_ZN13QWaylandTouch6d_funcEv(
    QWaylandTouch *self) {
  return self->d_func();
}

//  const QWaylandTouchPrivate *QWaylandTouch::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandTouchPrivate *ritual_ZNK13QWaylandTouch6d_funcEv(
    const QWaylandTouch *self) {
  return self->d_func();
}

//  QWaylandTouch::QWaylandTouch(QWaylandSeat *seat, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandTouch *ritual_ZN13QWaylandTouchC1EP12QWaylandSeatP7QObject(
    QWaylandSeat *seat,
    QObject *parent) {
  return new CuteQWaylandTouch(seat, parent);
}

//  QWaylandSeat *QWaylandTouch::seat() const
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZNK13QWaylandTouch4seatEv(const QWaylandTouch *self) {
  return self->seat();
}

//  QWaylandCompositor *QWaylandTouch::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK13QWaylandTouch10compositorEv(
    const QWaylandTouch *self) {
  return self->compositor();
}

//  uint QWaylandTouch::sendTouchPointEvent(QWaylandSurface *surface, int id,
//      const QPointF &position, Qt::TouchPointState state)
extern "C" Q_DECL_EXPORT
uint ritual_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSurfaceiRK7QPointFN2Qt15TouchPointStateE(
    QWaylandTouch *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *position,
    Qt::TouchPointState state) {
  return self->sendTouchPointEvent(surface, id, *position, state);
}

//  void QWaylandTouch::sendFrameEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient(
    QWaylandTouch *self,
    QWaylandClient *client) {
  self->sendFrameEvent(client);
}

//  void QWaylandTouch::sendCancelEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient(
    QWaylandTouch *self,
    QWaylandClient *client) {
  self->sendCancelEvent(client);
}

//  void QWaylandTouch::sendFullTouchEvent(QWaylandSurface *surface,
//      QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurfaceP11QTouchEvent(
    QWaylandTouch *self,
    QWaylandSurface *surface,
    QTouchEvent *event) {
  self->sendFullTouchEvent(surface, event);
}

//  void QWaylandTouch::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWaylandTouch9addClientEP14QWaylandClientjj(
    QWaylandTouch *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->addClient(client, id, version);
}

//  a Python function taken by a CuteQWaylandTouch, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandTouch(
    QWaylandTouch *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandTouch *>(self)->take(key, call);
}

//  uint QWaylandTouch::sendTouchPointEvent(QWaylandSurface *surface, int id,
//      const QPointF &position, Qt::TouchPointState state)
extern "C" Q_DECL_EXPORT
uint ritual_own_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSurfaceiRK7QPointFN2Qt15TouchPointStateE(
    QWaylandTouch *self,
    QWaylandSurface *surface,
    int id,
    const QPointF *position,
    Qt::TouchPointState state) {
  return self->QWaylandTouch::sendTouchPointEvent(
      surface,
      id,
      *position,
      state);
}

//  void QWaylandTouch::sendFrameEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient(
    QWaylandTouch *self,
    QWaylandClient *client) {
  self->QWaylandTouch::sendFrameEvent(client);
}

//  void QWaylandTouch::sendCancelEvent(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient(
    QWaylandTouch *self,
    QWaylandClient *client) {
  self->QWaylandTouch::sendCancelEvent(client);
}

//  void QWaylandTouch::sendFullTouchEvent(QWaylandSurface *surface,
//      QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurfaceP11QTouchEvent(
    QWaylandTouch *self,
    QWaylandSurface *surface,
    QTouchEvent *event) {
  self->QWaylandTouch::sendFullTouchEvent(surface, event);
}

//  void QWaylandTouch::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWaylandTouch9addClientEP14QWaylandClientjj(
    QWaylandTouch *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->QWaylandTouch::addClient(client, id, version);
}
