//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qpicktriangleevent.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qpicktriangleevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QPickTriangleEvent that Python can take functions over in. Every Qt3DRender::QPickTriangleEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickTriangleEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickTriangleEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickTriangleEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickTriangleEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickTriangleEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickTriangleEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickTriangleEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QPickTriangleEvent : public Qt3DRender::QPickTriangleEvent {
public:
  using Qt3DRender::QPickTriangleEvent::QPickTriangleEvent;
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
      CuteQt3DRender_QPickTriangleEventCall0 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall0>(taken[0]);
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
      CuteQt3DRender_QPickTriangleEventCall1 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall1>(taken[1]);
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
      CuteQt3DRender_QPickTriangleEventCall2 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall2>(taken[2]);
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
      CuteQt3DRender_QPickTriangleEventCall3 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall3>(taken[3]);
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
      CuteQt3DRender_QPickTriangleEventCall4 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall4>(taken[4]);
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
      CuteQt3DRender_QPickTriangleEventCall5 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall5>(taken[5]);
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
      CuteQt3DRender_QPickTriangleEventCall6 call = reinterpret_cast<CuteQt3DRender_QPickTriangleEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QPickTriangleEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender18QPickTriangleEvent10metaObjectEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QPickTriangleEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender18QPickTriangleEvent11qt_metacastEPKc(
    Qt3DRender::QPickTriangleEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QPickTriangleEvent::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender18QPickTriangleEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QPickTriangleEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QPickTriangleEvent::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender18QPickTriangleEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QPickTriangleEvent::tr(s, c, n));
}

//  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEvent *ritual_ZN10Qt3DRender18QPickTriangleEventC1Ev() {
  return new CuteQt3DRender_QPickTriangleEvent();
}

//  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
//      &position, const QVector3D &worldIntersection, const QVector3D
//      &localIntersection, float distance, uint triangleIndex, uint
//      vertex1Index, uint vertex2Index, uint vertex3Index)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEvent *ritual_ZN10Qt3DRender18QPickTriangleEventC1ERK7QPointFRK9QVector3DS6_fjjjj(
    const QPointF *position,
    const QVector3D *worldIntersection,
    const QVector3D *localIntersection,
    float distance,
    uint triangleIndex,
    uint vertex1Index,
    uint vertex2Index,
    uint vertex3Index) {
  return new CuteQt3DRender_QPickTriangleEvent(
      *position,
      *worldIntersection,
      *localIntersection,
      distance,
      triangleIndex,
      vertex1Index,
      vertex2Index,
      vertex3Index);
}

//  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
//      &position, const QVector3D &worldIntersection, const QVector3D
//      &localIntersection, float distance, uint triangleIndex, uint
//      vertex1Index, uint vertex2Index, uint vertex3Index, Buttons button,
//      int buttons, int modifiers, const QVector3D &uvw)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEvent *ritual_ZN10Qt3DRender18QPickTriangleEventC1ERK7QPointFRK9QVector3DS6_fjjjjNS_10QPickEvent7ButtonsEiiS6_(
    const QPointF *position,
    const QVector3D *worldIntersection,
    const QVector3D *localIntersection,
    float distance,
    uint triangleIndex,
    uint vertex1Index,
    uint vertex2Index,
    uint vertex3Index,
    Qt3DRender::QPickEvent::Buttons button,
    int buttons,
    int modifiers,
    const QVector3D *uvw) {
  return new CuteQt3DRender_QPickTriangleEvent(
      *position,
      *worldIntersection,
      *localIntersection,
      distance,
      triangleIndex,
      vertex1Index,
      vertex2Index,
      vertex3Index,
      button,
      buttons,
      modifiers,
      *uvw);
}

//  Qt3DRender::QPickTriangleEvent::~QPickTriangleEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QPickTriangleEventD1Ev(
    Qt3DRender::QPickTriangleEvent *self) {
  delete self;
}

//  uint Qt3DRender::QPickTriangleEvent::triangleIndex() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender18QPickTriangleEvent13triangleIndexEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->triangleIndex();
}

//  uint Qt3DRender::QPickTriangleEvent::vertex1Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex1IndexEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->vertex1Index();
}

//  uint Qt3DRender::QPickTriangleEvent::vertex2Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex2IndexEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->vertex2Index();
}

//  uint Qt3DRender::QPickTriangleEvent::vertex3Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex3IndexEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->vertex3Index();
}

//  QVector3D Qt3DRender::QPickTriangleEvent::uvw() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender18QPickTriangleEvent3uvwEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return new QVector3D(self->uvw());
}

//  QPickTriangleEventPrivate *Qt3DRender::QPickTriangleEvent::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickTriangleEventPrivate *ritual_ZN10Qt3DRender18QPickTriangleEvent6d_funcEv(
    Qt3DRender::QPickTriangleEvent *self) {
  return self->d_func();
}

//  const QPickTriangleEventPrivate *Qt3DRender::QPickTriangleEvent::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPickTriangleEventPrivate *ritual_ZNK10Qt3DRender18QPickTriangleEvent6d_funcEv(
    const Qt3DRender::QPickTriangleEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QPickTriangleEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPickTriangleEvent(
    Qt3DRender::QPickTriangleEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPickTriangleEvent *>(self)->take(key, call);
}
