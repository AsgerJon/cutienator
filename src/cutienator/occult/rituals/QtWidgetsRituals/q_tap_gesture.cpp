//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTapGesture that Python can take functions over in. Every QTapGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTapGesture : public QTapGesture {
public:
  using QTapGesture::QTapGesture;
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
      CuteQTapGestureCall0 call = reinterpret_cast<CuteQTapGestureCall0>(taken[0]);
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
      CuteQTapGestureCall1 call = reinterpret_cast<CuteQTapGestureCall1>(taken[1]);
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
      CuteQTapGestureCall2 call = reinterpret_cast<CuteQTapGestureCall2>(taken[2]);
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
      CuteQTapGestureCall3 call = reinterpret_cast<CuteQTapGestureCall3>(taken[3]);
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
      CuteQTapGestureCall4 call = reinterpret_cast<CuteQTapGestureCall4>(taken[4]);
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
      CuteQTapGestureCall5 call = reinterpret_cast<CuteQTapGestureCall5>(taken[5]);
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
      CuteQTapGestureCall6 call = reinterpret_cast<CuteQTapGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTapGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTapGesture10metaObjectEv(
    const QTapGesture *self) {
  return self->metaObject();
}

//  QString QTapGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTapGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapGesture::tr(s, c, n));
}

//  QTapGesturePrivate *QTapGesture::d_func()
extern "C" Q_DECL_EXPORT
QTapGesturePrivate *ritual_ZN11QTapGesture6d_funcEv(QTapGesture *self) {
  return self->d_func();
}

//  const QTapGesturePrivate *QTapGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QTapGesturePrivate *ritual_ZNK11QTapGesture6d_funcEv(
    const QTapGesture *self) {
  return self->d_func();
}

//  QTapGesture::QTapGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapGesture *ritual_ZN11QTapGestureC1EP7QObject(QObject *parent) {
  return new CuteQTapGesture(parent);
}

//  QTapGesture::~QTapGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapGestureD1Ev(QTapGesture *self) {
  delete self;
}

//  QPointF QTapGesture::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QTapGesture8positionEv(const QTapGesture *self) {
  return new QPointF(self->position());
}

//  void QTapGesture::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapGesture11setPositionERK7QPointF(
    QTapGesture *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  a Python function taken by a CuteQTapGesture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapGesture(
    QTapGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTapGesture *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
