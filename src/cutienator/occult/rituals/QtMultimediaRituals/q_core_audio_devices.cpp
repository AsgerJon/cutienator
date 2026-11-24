//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCoreAudioDevices that Python can take functions over in. Every QCoreAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCoreAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQCoreAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQCoreAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQCoreAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoreAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoreAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoreAudioDevices : public QCoreAudioDevices {
public:
  using QCoreAudioDevices::QCoreAudioDevices;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDevices11backendNameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDevices14hasCallbackApiEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPlatformAudioSource *QCoreAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall0 call = reinterpret_cast<CuteQCoreAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QCoreAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QCoreAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall1 call = reinterpret_cast<CuteQCoreAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QCoreAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QCoreAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall2 call = reinterpret_cast<CuteQCoreAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreAudioDevices::backendName();
  }

  //  bool QCoreAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall3 call = reinterpret_cast<CuteQCoreAudioDevicesCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreAudioDevices::hasCallbackApi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall4 call = reinterpret_cast<CuteQCoreAudioDevicesCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall5 call = reinterpret_cast<CuteQCoreAudioDevicesCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall6 call = reinterpret_cast<CuteQCoreAudioDevicesCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall7 call = reinterpret_cast<CuteQCoreAudioDevicesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall8 call = reinterpret_cast<CuteQCoreAudioDevicesCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall9 call = reinterpret_cast<CuteQCoreAudioDevicesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCoreAudioDevicesCall10 call = reinterpret_cast<CuteQCoreAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QLatin1String QCoreAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK17QCoreAudioDevices11backendNameEv(
    const QCoreAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QCoreAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCoreAudioDevices14hasCallbackApiEv(
    const QCoreAudioDevices *self) {
  return self->hasCallbackApi();
}

//  a Python function taken by a CuteQCoreAudioDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoreAudioDevices(
    QCoreAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoreAudioDevices *>(self)->take(key, call);
}

//  QPlatformAudioSource *QCoreAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_own_ZN17QCoreAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QCoreAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QCoreAudioDevices::createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QCoreAudioDevices::createAudioSink(const QAudioDevice
//      &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_own_ZN17QCoreAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QCoreAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QCoreAudioDevices::createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QCoreAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK17QCoreAudioDevices11backendNameEv(
    const QCoreAudioDevices *self) {
  return new QLatin1String(self->QCoreAudioDevices::backendName());
}

//  bool QCoreAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QCoreAudioDevices14hasCallbackApiEv(
    const QCoreAudioDevices *self) {
  return self->QCoreAudioDevices::hasCallbackApi();
}

#endif  // defined(Q_OS_DARWIN)
