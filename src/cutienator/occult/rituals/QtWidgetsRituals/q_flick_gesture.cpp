//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFlickGesture that Python can take functions over in. Every QFlickGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQFlickGestureCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQFlickGestureCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQFlickGestureCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQFlickGestureCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQFlickGestureCall4)(const void *, QEvent *, int *);
typedef void (*CuteQFlickGestureCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQFlickGestureCall6)(const void *, const QMetaMethod *, int *);
class CuteQFlickGesture : public QFlickGesture {
public:
  using QFlickGesture::QFlickGesture;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFlickGestureCall0 call = reinterpret_cast<CuteQFlickGestureCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFlickGestureCall1 call = reinterpret_cast<CuteQFlickGestureCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFlickGestureCall2 call = reinterpret_cast<CuteQFlickGestureCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFlickGestureCall3 call = reinterpret_cast<CuteQFlickGestureCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFlickGestureCall4 call = reinterpret_cast<CuteQFlickGestureCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFlickGestureCall5 call = reinterpret_cast<CuteQFlickGestureCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFlickGestureCall6 call = reinterpret_cast<CuteQFlickGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QFlickGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QFlickGesture10metaObjectEv(
    const QFlickGesture *self) {
  return self->metaObject();
}

//  QString QFlickGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFlickGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFlickGesture::tr(s, c, n));
}

//  QFlickGesture::QFlickGesture(QObject *receiver, Qt::MouseButton button,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QFlickGesture *ritual_ZN13QFlickGestureC1EP7QObjectN2Qt11MouseButtonES1_(
    QObject *receiver,
    Qt::MouseButton button,
    QObject *parent) {
  return new CuteQFlickGesture(receiver, button, parent);
}

//  QFlickGesture::~QFlickGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFlickGestureD1Ev(QFlickGesture *self) {
  delete self;
}

//  a Python function taken by a CuteQFlickGesture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFlickGesture(
    QFlickGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFlickGesture *>(self)->take(key, call);
}
