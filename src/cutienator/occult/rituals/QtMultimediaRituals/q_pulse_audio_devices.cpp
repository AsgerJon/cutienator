//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qpulseaudiodevices_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands also under
//  '__has_include(<pulse/pulseaudio.h>)', because Qt's header it needs
//  includes the header of PulseAudio, which a machine with Qt's kit but
//  without the development headers of PulseAudio lacks. Kept as it is when
//  the generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(pulseaudio) && __has_include(<pulse/pulseaudio.h>)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qpulseaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qpulseaudiodevices_p.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qcameradevice_p.h>
#include <QtMultimedia/private/qpulseaudiosource_p.h>
#include <QtMultimedia/private/qpulseaudiosink_p.h>
#include <QtMultimedia/private/qpulseaudio_contextmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/pulseaudio/qpulseaudiodevices.cpp, line 26, as _ZN18QPulseAudioDevicesD1Ev
inline QPulseAudioDevices::~QPulseAudioDevices()
{
    delete pulseEngine;
}

//  from ../qtmultimedia/src/multimedia/pulseaudio/qpulseaudiodevices.cpp, line 41, as _ZN18QPulseAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSource *QPulseAudioDevices::createAudioSource(const QAudioDevice &deviceInfo,
                                                            const QAudioFormat &fmt,
                                                            QObject *parent)
{
    return new QPulseAudioInternal::QPulseAudioSource(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/pulseaudio/qpulseaudiodevices.cpp, line 48, as _ZN18QPulseAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSink *QPulseAudioDevices::createAudioSink(const QAudioDevice &deviceInfo,
                                                        const QAudioFormat &fmt,
                                                        QObject *parent)
{
    return new QPulseAudioInternal::QPulseAudioSink(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/pulseaudio/qpulseaudiodevices.cpp, line 31, as _ZNK18QPulseAudioDevices15findAudioInputsEv
inline QList<QAudioDevice> QPulseAudioDevices::findAudioInputs() const
{
    return pulseEngine->availableDevices(QAudioDevice::Input);
}

//  from ../qtmultimedia/src/multimedia/pulseaudio/qpulseaudiodevices.cpp, line 36, as _ZNK18QPulseAudioDevices16findAudioOutputsEv
inline QList<QAudioDevice> QPulseAudioDevices::findAudioOutputs() const
{
    return pulseEngine->availableDevices(QAudioDevice::Output);
}
//  -----------------------------------------------------------------------

//  A QPulseAudioDevices that Python can take functions over in. Every QPulseAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPulseAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQPulseAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQPulseAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQPulseAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPulseAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPulseAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPulseAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPulseAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPulseAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPulseAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPulseAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPulseAudioDevices : public QPulseAudioDevices {
public:
  using QPulseAudioDevices::QPulseAudioDevices;
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

  //  QPlatformAudioSource *QPulseAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPulseAudioDevicesCall0 call = reinterpret_cast<CuteQPulseAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QPulseAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QPulseAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPulseAudioDevicesCall1 call = reinterpret_cast<CuteQPulseAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QPulseAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QPulseAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPulseAudioDevicesCall2 call = reinterpret_cast<CuteQPulseAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPulseAudioDevices::backendName();
  }

  //  bool QPulseAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPulseAudioDevicesCall3 call = reinterpret_cast<CuteQPulseAudioDevicesCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPulseAudioDevices::hasCallbackApi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPulseAudioDevicesCall4 call = reinterpret_cast<CuteQPulseAudioDevicesCall4>(taken[4]);
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
      CuteQPulseAudioDevicesCall5 call = reinterpret_cast<CuteQPulseAudioDevicesCall5>(taken[5]);
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
      CuteQPulseAudioDevicesCall6 call = reinterpret_cast<CuteQPulseAudioDevicesCall6>(taken[6]);
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
      CuteQPulseAudioDevicesCall7 call = reinterpret_cast<CuteQPulseAudioDevicesCall7>(taken[7]);
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
      CuteQPulseAudioDevicesCall8 call = reinterpret_cast<CuteQPulseAudioDevicesCall8>(taken[8]);
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
      CuteQPulseAudioDevicesCall9 call = reinterpret_cast<CuteQPulseAudioDevicesCall9>(taken[9]);
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
      CuteQPulseAudioDevicesCall10 call = reinterpret_cast<CuteQPulseAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QPulseAudioDevices::~QPulseAudioDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPulseAudioDevicesD1Ev(QPulseAudioDevices *self) {
  delete self;
}

//  QPlatformAudioSource *QPulseAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN18QPulseAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPulseAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QPulseAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN18QPulseAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPulseAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QPulseAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK18QPulseAudioDevices11backendNameEv(
    const QPulseAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QPulseAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPulseAudioDevices14hasCallbackApiEv(
    const QPulseAudioDevices *self) {
  return self->hasCallbackApi();
}

//  QList<QAudioDevice> QPulseAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK18QPulseAudioDevices15findAudioInputsEv(
    const QPulseAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QPulseAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK18QPulseAudioDevices16findAudioOutputsEv(
    const QPulseAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

//  a Python function taken by a CuteQPulseAudioDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPulseAudioDevices(
    QPulseAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPulseAudioDevices *>(self)->take(key, call);
}

//  QLatin1String QPulseAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK18QPulseAudioDevices11backendNameEv(
    const QPulseAudioDevices *self) {
  return new QLatin1String(self->QPulseAudioDevices::backendName());
}

//  bool QPulseAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QPulseAudioDevices14hasCallbackApiEv(
    const QPulseAudioDevices *self) {
  return self->QPulseAudioDevices::hasCallbackApi();
}

#endif  // QT_CONFIG(pulseaudio) && __has_include(<pulse/pulseaudio.h>)
