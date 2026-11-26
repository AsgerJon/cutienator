//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSwipeGesture that Python can take functions over in. Every QSwipeGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSwipeGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSwipeGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSwipeGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSwipeGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSwipeGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSwipeGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSwipeGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSwipeGesture : public QSwipeGesture {
public:
  using QSwipeGesture::QSwipeGesture;
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
      CuteQSwipeGestureCall0 call = reinterpret_cast<CuteQSwipeGestureCall0>(taken[0]);
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
      CuteQSwipeGestureCall1 call = reinterpret_cast<CuteQSwipeGestureCall1>(taken[1]);
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
      CuteQSwipeGestureCall2 call = reinterpret_cast<CuteQSwipeGestureCall2>(taken[2]);
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
      CuteQSwipeGestureCall3 call = reinterpret_cast<CuteQSwipeGestureCall3>(taken[3]);
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
      CuteQSwipeGestureCall4 call = reinterpret_cast<CuteQSwipeGestureCall4>(taken[4]);
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
      CuteQSwipeGestureCall5 call = reinterpret_cast<CuteQSwipeGestureCall5>(taken[5]);
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
      CuteQSwipeGestureCall6 call = reinterpret_cast<CuteQSwipeGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSwipeGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSwipeGesture10metaObjectEv(
    const QSwipeGesture *self) {
  return self->metaObject();
}

//  void *QSwipeGesture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QSwipeGesture11qt_metacastEPKc(
    QSwipeGesture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSwipeGesture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSwipeGesture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSwipeGesture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSwipeGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSwipeGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSwipeGesture::tr(s, c, n));
}

//  QSwipeGesturePrivate *QSwipeGesture::d_func()
extern "C" Q_DECL_EXPORT
QSwipeGesturePrivate *ritual_ZN13QSwipeGesture6d_funcEv(
    QSwipeGesture *self) {
  return self->d_func();
}

//  const QSwipeGesturePrivate *QSwipeGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QSwipeGesturePrivate *ritual_ZNK13QSwipeGesture6d_funcEv(
    const QSwipeGesture *self) {
  return self->d_func();
}

//  QSwipeGesture::QSwipeGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QSwipeGesture *ritual_ZN13QSwipeGestureC1EP7QObject(QObject *parent) {
  return new CuteQSwipeGesture(parent);
}

//  QSwipeGesture::~QSwipeGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSwipeGestureD1Ev(QSwipeGesture *self) {
  delete self;
}

//  SwipeDirection QSwipeGesture::horizontalDirection() const
extern "C" Q_DECL_EXPORT
QSwipeGesture::SwipeDirection ritual_ZNK13QSwipeGesture19horizontalDirectionEv(
    const QSwipeGesture *self) {
  return self->horizontalDirection();
}

//  SwipeDirection QSwipeGesture::verticalDirection() const
extern "C" Q_DECL_EXPORT
QSwipeGesture::SwipeDirection ritual_ZNK13QSwipeGesture17verticalDirectionEv(
    const QSwipeGesture *self) {
  return self->verticalDirection();
}

//  qreal QSwipeGesture::swipeAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QSwipeGesture10swipeAngleEv(const QSwipeGesture *self) {
  return self->swipeAngle();
}

//  void QSwipeGesture::setSwipeAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSwipeGesture13setSwipeAngleEd(
    QSwipeGesture *self,
    qreal value) {
  self->setSwipeAngle(value);
}

//  a Python function taken by a CuteQSwipeGesture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSwipeGesture(
    QSwipeGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSwipeGesture *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
