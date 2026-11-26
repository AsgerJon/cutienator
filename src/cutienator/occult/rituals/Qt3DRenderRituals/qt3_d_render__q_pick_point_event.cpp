//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qpickpointevent.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'd_func' gives
//  'Qt3DRender::QPickPointEventPrivate', written in full (the compiler did
//  not know the short name), and 'qt_metacast' is taken out (a Q_OBJECT
//  class gets 'metaObject' only). Kept as it is when the generator runs
//  again.
#include <Qt3DRender/qpickpointevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QPickPointEvent that Python can take functions over in. Every Qt3DRender::QPickPointEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickPointEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickPointEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickPointEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickPointEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickPointEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickPointEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickPointEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QPickPointEvent : public Qt3DRender::QPickPointEvent {
public:
  using Qt3DRender::QPickPointEvent::QPickPointEvent;
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
      CuteQt3DRender_QPickPointEventCall0 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall0>(taken[0]);
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
      CuteQt3DRender_QPickPointEventCall1 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall1>(taken[1]);
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
      CuteQt3DRender_QPickPointEventCall2 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall2>(taken[2]);
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
      CuteQt3DRender_QPickPointEventCall3 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall3>(taken[3]);
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
      CuteQt3DRender_QPickPointEventCall4 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall4>(taken[4]);
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
      CuteQt3DRender_QPickPointEventCall5 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall5>(taken[5]);
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
      CuteQt3DRender_QPickPointEventCall6 call = reinterpret_cast<CuteQt3DRender_QPickPointEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QPickPointEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender15QPickPointEvent10metaObjectEv(
    const Qt3DRender::QPickPointEvent *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QPickPointEvent::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender15QPickPointEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QPickPointEvent::tr(s, c, n));
}

//  Qt3DRender::QPickPointEvent::QPickPointEvent()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickPointEvent *ritual_ZN10Qt3DRender15QPickPointEventC1Ev() {
  return new CuteQt3DRender_QPickPointEvent();
}

//  Qt3DRender::QPickPointEvent::QPickPointEvent(const QPointF &position,
//      const QVector3D &worldIntersection, const QVector3D
//      &localIntersection, float distance, uint pointIndex, Buttons button,
//      int buttons, int modifiers)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickPointEvent *ritual_ZN10Qt3DRender15QPickPointEventC1ERK7QPointFRK9QVector3DS6_fjNS_10QPickEvent7ButtonsEii(
    const QPointF *position,
    const QVector3D *worldIntersection,
    const QVector3D *localIntersection,
    float distance,
    uint pointIndex,
    Qt3DRender::QPickEvent::Buttons button,
    int buttons,
    int modifiers) {
  return new CuteQt3DRender_QPickPointEvent(
      *position,
      *worldIntersection,
      *localIntersection,
      distance,
      pointIndex,
      button,
      buttons,
      modifiers);
}

//  Qt3DRender::QPickPointEventPrivate *
//      Qt3DRender::QPickPointEvent::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickPointEventPrivate *ritual_ZN10Qt3DRender15QPickPointEvent6d_funcEv(
    Qt3DRender::QPickPointEvent *self) {
  return self->d_func();
}

//  const Qt3DRender::QPickPointEventPrivate *
//      Qt3DRender::QPickPointEvent::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPickPointEventPrivate *ritual_ZNK10Qt3DRender15QPickPointEvent6d_funcEv(
    const Qt3DRender::QPickPointEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QPickPointEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPickPointEvent(
    Qt3DRender::QPickPointEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPickPointEvent *>(self)->take(key, call);
}
