//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxaudiodevices_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_audio)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQnxAudioDevices that Python can take functions over in. Every QQnxAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQnxAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQQnxAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQQnxAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQQnxAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQnxAudioDevices : public QQnxAudioDevices {
public:
  using QQnxAudioDevices::QQnxAudioDevices;
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

  //  QPlatformAudioSource *QQnxAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQnxAudioDevicesCall0 call = reinterpret_cast<CuteQQnxAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QQnxAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QQnxAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQnxAudioDevicesCall1 call = reinterpret_cast<CuteQQnxAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QQnxAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QQnxAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQnxAudioDevicesCall2 call = reinterpret_cast<CuteQQnxAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQnxAudioDevices::backendName();
  }

  //  bool QPlatformAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQnxAudioDevicesCall3 call = reinterpret_cast<CuteQQnxAudioDevicesCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioDevices::hasCallbackApi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQnxAudioDevicesCall4 call = reinterpret_cast<CuteQQnxAudioDevicesCall4>(taken[4]);
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
      CuteQQnxAudioDevicesCall5 call = reinterpret_cast<CuteQQnxAudioDevicesCall5>(taken[5]);
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
      CuteQQnxAudioDevicesCall6 call = reinterpret_cast<CuteQQnxAudioDevicesCall6>(taken[6]);
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
      CuteQQnxAudioDevicesCall7 call = reinterpret_cast<CuteQQnxAudioDevicesCall7>(taken[7]);
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
      CuteQQnxAudioDevicesCall8 call = reinterpret_cast<CuteQQnxAudioDevicesCall8>(taken[8]);
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
      CuteQQnxAudioDevicesCall9 call = reinterpret_cast<CuteQQnxAudioDevicesCall9>(taken[9]);
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
      CuteQQnxAudioDevicesCall10 call = reinterpret_cast<CuteQQnxAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QLatin1String QQnxAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK16QQnxAudioDevices11backendNameEv(
    const QQnxAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  a Python function taken by a CuteQQnxAudioDevices, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQnxAudioDevices(
    QQnxAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQnxAudioDevices *>(self)->take(key, call);
}

//  QLatin1String QQnxAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK16QQnxAudioDevices11backendNameEv(
    const QQnxAudioDevices *self) {
  return new QLatin1String(self->QQnxAudioDevices::backendName());
}

#endif  // QT_CONFIG(qnx_io_audio)
