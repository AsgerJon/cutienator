//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPanGesture that Python can take functions over in. Every QPanGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPanGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPanGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPanGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPanGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPanGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPanGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPanGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPanGesture : public QPanGesture {
public:
  using QPanGesture::QPanGesture;
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
      CuteQPanGestureCall0 call = reinterpret_cast<CuteQPanGestureCall0>(taken[0]);
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
      CuteQPanGestureCall1 call = reinterpret_cast<CuteQPanGestureCall1>(taken[1]);
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
      CuteQPanGestureCall2 call = reinterpret_cast<CuteQPanGestureCall2>(taken[2]);
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
      CuteQPanGestureCall3 call = reinterpret_cast<CuteQPanGestureCall3>(taken[3]);
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
      CuteQPanGestureCall4 call = reinterpret_cast<CuteQPanGestureCall4>(taken[4]);
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
      CuteQPanGestureCall5 call = reinterpret_cast<CuteQPanGestureCall5>(taken[5]);
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
      CuteQPanGestureCall6 call = reinterpret_cast<CuteQPanGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPanGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPanGesture10metaObjectEv(
    const QPanGesture *self) {
  return self->metaObject();
}

//  void *QPanGesture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QPanGesture11qt_metacastEPKc(
    QPanGesture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPanGesture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QPanGesture11qt_metacallEN11QMetaObject4CallEiPPv(
    QPanGesture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPanGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPanGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPanGesture::tr(s, c, n));
}

//  QPanGesturePrivate *QPanGesture::d_func()
extern "C" Q_DECL_EXPORT
QPanGesturePrivate *ritual_ZN11QPanGesture6d_funcEv(QPanGesture *self) {
  return self->d_func();
}

//  const QPanGesturePrivate *QPanGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QPanGesturePrivate *ritual_ZNK11QPanGesture6d_funcEv(
    const QPanGesture *self) {
  return self->d_func();
}

//  QPanGesture::QPanGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QPanGesture *ritual_ZN11QPanGestureC1EP7QObject(QObject *parent) {
  return new CuteQPanGesture(parent);
}

//  QPanGesture::~QPanGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGestureD1Ev(QPanGesture *self) {
  delete self;
}

//  QPointF QPanGesture::lastOffset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture10lastOffsetEv(const QPanGesture *self) {
  return new QPointF(self->lastOffset());
}

//  QPointF QPanGesture::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture6offsetEv(const QPanGesture *self) {
  return new QPointF(self->offset());
}

//  QPointF QPanGesture::delta() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPanGesture5deltaEv(const QPanGesture *self) {
  return new QPointF(self->delta());
}

//  qreal QPanGesture::acceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QPanGesture12accelerationEv(const QPanGesture *self) {
  return self->acceleration();
}

//  void QPanGesture::setLastOffset(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture13setLastOffsetERK7QPointF(
    QPanGesture *self,
    const QPointF *value) {
  self->setLastOffset(*value);
}

//  void QPanGesture::setOffset(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture9setOffsetERK7QPointF(
    QPanGesture *self,
    const QPointF *value) {
  self->setOffset(*value);
}

//  void QPanGesture::setAcceleration(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPanGesture15setAccelerationEd(
    QPanGesture *self,
    qreal value) {
  self->setAcceleration(value);
}

//  a Python function taken by a CuteQPanGesture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPanGesture(
    QPanGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPanGesture *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
