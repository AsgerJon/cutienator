//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTapAndHoldGesture that Python can take functions over in. Every QTapAndHoldGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapAndHoldGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapAndHoldGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapAndHoldGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapAndHoldGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapAndHoldGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapAndHoldGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapAndHoldGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTapAndHoldGesture : public QTapAndHoldGesture {
public:
  using QTapAndHoldGesture::QTapAndHoldGesture;
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
      CuteQTapAndHoldGestureCall0 call = reinterpret_cast<CuteQTapAndHoldGestureCall0>(taken[0]);
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
      CuteQTapAndHoldGestureCall1 call = reinterpret_cast<CuteQTapAndHoldGestureCall1>(taken[1]);
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
      CuteQTapAndHoldGestureCall2 call = reinterpret_cast<CuteQTapAndHoldGestureCall2>(taken[2]);
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
      CuteQTapAndHoldGestureCall3 call = reinterpret_cast<CuteQTapAndHoldGestureCall3>(taken[3]);
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
      CuteQTapAndHoldGestureCall4 call = reinterpret_cast<CuteQTapAndHoldGestureCall4>(taken[4]);
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
      CuteQTapAndHoldGestureCall5 call = reinterpret_cast<CuteQTapAndHoldGestureCall5>(taken[5]);
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
      CuteQTapAndHoldGestureCall6 call = reinterpret_cast<CuteQTapAndHoldGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTapAndHoldGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QTapAndHoldGesture10metaObjectEv(
    const QTapAndHoldGesture *self) {
  return self->metaObject();
}

//  void *QTapAndHoldGesture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QTapAndHoldGesture11qt_metacastEPKc(
    QTapAndHoldGesture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTapAndHoldGesture::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QTapAndHoldGesture11qt_metacallEN11QMetaObject4CallEiPPv(
    QTapAndHoldGesture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTapAndHoldGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QTapAndHoldGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapAndHoldGesture::tr(s, c, n));
}

//  QTapAndHoldGesturePrivate *QTapAndHoldGesture::d_func()
extern "C" Q_DECL_EXPORT
QTapAndHoldGesturePrivate *ritual_ZN18QTapAndHoldGesture6d_funcEv(
    QTapAndHoldGesture *self) {
  return self->d_func();
}

//  const QTapAndHoldGesturePrivate *QTapAndHoldGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QTapAndHoldGesturePrivate *ritual_ZNK18QTapAndHoldGesture6d_funcEv(
    const QTapAndHoldGesture *self) {
  return self->d_func();
}

//  QTapAndHoldGesture::QTapAndHoldGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapAndHoldGesture *ritual_ZN18QTapAndHoldGestureC1EP7QObject(
    QObject *parent) {
  return new CuteQTapAndHoldGesture(parent);
}

//  QTapAndHoldGesture::~QTapAndHoldGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGestureD1Ev(QTapAndHoldGesture *self) {
  delete self;
}

//  QPointF QTapAndHoldGesture::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QTapAndHoldGesture8positionEv(
    const QTapAndHoldGesture *self) {
  return new QPointF(self->position());
}

//  void QTapAndHoldGesture::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGesture11setPositionERK7QPointF(
    QTapAndHoldGesture *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  void QTapAndHoldGesture::setTimeout(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapAndHoldGesture10setTimeoutEi(int msecs) {
  QTapAndHoldGesture::setTimeout(msecs);
}

//  int QTapAndHoldGesture::timeout()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QTapAndHoldGesture7timeoutEv() {
  return QTapAndHoldGesture::timeout();
}

//  a Python function taken by a CuteQTapAndHoldGesture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapAndHoldGesture(
    QTapAndHoldGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTapAndHoldGesture *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
