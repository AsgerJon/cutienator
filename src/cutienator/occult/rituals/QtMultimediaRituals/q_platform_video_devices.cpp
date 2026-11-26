//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qcameradevice.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformVideoDevices that Python can take functions over in. Every QPlatformVideoDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoDevicesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoDevicesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoDevicesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoDevicesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoDevicesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoDevicesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformVideoDevices : public QPlatformVideoDevices {
public:
  using QPlatformVideoDevices::QPlatformVideoDevices;
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
      CuteQPlatformVideoDevicesCall0 call = reinterpret_cast<CuteQPlatformVideoDevicesCall0>(taken[0]);
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
      CuteQPlatformVideoDevicesCall1 call = reinterpret_cast<CuteQPlatformVideoDevicesCall1>(taken[1]);
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
      CuteQPlatformVideoDevicesCall2 call = reinterpret_cast<CuteQPlatformVideoDevicesCall2>(taken[2]);
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
      CuteQPlatformVideoDevicesCall3 call = reinterpret_cast<CuteQPlatformVideoDevicesCall3>(taken[3]);
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
      CuteQPlatformVideoDevicesCall4 call = reinterpret_cast<CuteQPlatformVideoDevicesCall4>(taken[4]);
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
      CuteQPlatformVideoDevicesCall5 call = reinterpret_cast<CuteQPlatformVideoDevicesCall5>(taken[5]);
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
      CuteQPlatformVideoDevicesCall6 call = reinterpret_cast<CuteQPlatformVideoDevicesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformVideoDevices::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlatformVideoDevices10metaObjectEv(
    const QPlatformVideoDevices *self) {
  return self->metaObject();
}

//  void *QPlatformVideoDevices::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QPlatformVideoDevices11qt_metacastEPKc(
    QPlatformVideoDevices *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformVideoDevices::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QPlatformVideoDevices11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformVideoDevices *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformVideoDevices::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPlatformVideoDevices2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformVideoDevices::tr(s, c, n));
}

//  QPlatformVideoDevices::~QPlatformVideoDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformVideoDevicesD1Ev(QPlatformVideoDevices *self) {
  delete self;
}

//  QList<QCameraDevice> QPlatformVideoDevices::videoInputs() const
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_ZNK21QPlatformVideoDevices11videoInputsEv(
    const QPlatformVideoDevices *self) {
  return new QList<QCameraDevice>(self->videoInputs());
}

//  QList<QCameraDevice> QPlatformVideoDevices::findVideoInputs() const
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_ZNK21QPlatformVideoDevices15findVideoInputsEv(
    const QPlatformVideoDevices *self) {
  return new QList<QCameraDevice>(self->findVideoInputs());
}

//  void QPlatformVideoDevices::onVideoInputsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformVideoDevices20onVideoInputsChangedEv(
    QPlatformVideoDevices *self) {
  self->onVideoInputsChanged();
}

//  void QPlatformVideoDevices::updateVideoInputsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformVideoDevices22updateVideoInputsCacheEv(
    QPlatformVideoDevices *self) {
  self->updateVideoInputsCache();
}

//  void QPlatformVideoDevices::videoInputsChanged(PrivateTag a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformVideoDevices18videoInputsChangedENS_10PrivateTagE(
    QPlatformVideoDevices *self,
    const QPlatformVideoDevices::PrivateTag *a0) {
  self->videoInputsChanged(*a0);
}

//  a Python function taken by a CuteQPlatformVideoDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformVideoDevices(
    QPlatformVideoDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformVideoDevices *>(self)->take(key, call);
}
