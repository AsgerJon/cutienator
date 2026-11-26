//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylanddrag.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#include <QtWaylandCompositor/qwaylanddrag.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandDrag that Python can take functions over in. Every QWaylandDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandDragCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandDragCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDragCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDragCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDragCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDragCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDragCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandDrag : public QWaylandDrag {
public:
  using QWaylandDrag::QWaylandDrag;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandDragCall0 call = reinterpret_cast<CuteQWaylandDragCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandDragCall1 call = reinterpret_cast<CuteQWaylandDragCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandDragCall2 call = reinterpret_cast<CuteQWaylandDragCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandDragCall3 call = reinterpret_cast<CuteQWaylandDragCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandDragCall4 call = reinterpret_cast<CuteQWaylandDragCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandDragCall5 call = reinterpret_cast<CuteQWaylandDragCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandDragCall6 call = reinterpret_cast<CuteQWaylandDragCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandDrag::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QWaylandDrag10metaObjectEv(
    const QWaylandDrag *self) {
  return self->metaObject();
}

//  void *QWaylandDrag::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QWaylandDrag11qt_metacastEPKc(
    QWaylandDrag *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandDrag::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QWaylandDrag11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandDrag *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandDrag::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QWaylandDrag2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandDrag::tr(s, c, n));
}

//  QWaylandDragPrivate *QWaylandDrag::d_func()
extern "C" Q_DECL_EXPORT
QWaylandDragPrivate *ritual_ZN12QWaylandDrag6d_funcEv(QWaylandDrag *self) {
  return self->d_func();
}

//  const QWaylandDragPrivate *QWaylandDrag::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandDragPrivate *ritual_ZNK12QWaylandDrag6d_funcEv(
    const QWaylandDrag *self) {
  return self->d_func();
}

//  void QWaylandDrag::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag24qt_qmlMarker_uncreatableEv(
    QWaylandDrag *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandDrag::QWaylandDrag(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
QWaylandDrag *ritual_ZN12QWaylandDragC1EP12QWaylandSeat(QWaylandSeat *seat) {
  return new CuteQWaylandDrag(seat);
}

//  QWaylandSurface *QWaylandDrag::icon() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK12QWaylandDrag4iconEv(const QWaylandDrag *self) {
  return self->icon();
}

//  QWaylandSurface *QWaylandDrag::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK12QWaylandDrag6originEv(
    const QWaylandDrag *self) {
  return self->origin();
}

//  QWaylandSeat *QWaylandDrag::seat() const
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZNK12QWaylandDrag4seatEv(const QWaylandDrag *self) {
  return self->seat();
}

//  bool QWaylandDrag::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandDrag7visibleEv(const QWaylandDrag *self) {
  return self->visible();
}

//  void QWaylandDrag::dragMove(QWaylandSurface *target, const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag8dragMoveEP15QWaylandSurfaceRK7QPointF(
    QWaylandDrag *self,
    QWaylandSurface *target,
    const QPointF *pos) {
  self->dragMove(target, *pos);
}

//  void QWaylandDrag::drop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag4dropEv(QWaylandDrag *self) {
  self->drop();
}

//  void QWaylandDrag::cancelDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag10cancelDragEv(QWaylandDrag *self) {
  self->cancelDrag();
}

//  void QWaylandDrag::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag11iconChangedEv(QWaylandDrag *self) {
  self->iconChanged();
}

//  void QWaylandDrag::dragStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandDrag11dragStartedEv(QWaylandDrag *self) {
  self->dragStarted();
}

//  a Python function taken by a CuteQWaylandDrag, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandDrag(
    QWaylandDrag *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandDrag *>(self)->take(key, call);
}

#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(draganddrop)
