//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(alsa)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qalsaaudiodevices_p.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qalsaaudiosource_p.h>
#include <QtMultimedia/private/qalsaaudiosink_p.h>
#include <QtMultimedia/private/qalsaaudiodevice_p.h>
#include <alsa/asoundlib.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qvarlengtharray.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qalsaaudiosource_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qvarlengtharray.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qalsaaudiosink_p.h>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiodevices.cpp, line 17, as local:qalsaaudiodevices.cpp:free_char
namespace {
struct free_char
{
    void operator()(char *c) const { ::free(c); }
};
}  // namespace

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiodevices.cpp, line 22, as local:qalsaaudiodevices.cpp:unique_str
namespace {
using unique_str = std::unique_ptr<char, free_char>;
}  // namespace

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiodevices.cpp, line 121, as _ZN17QAlsaAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSink *QAlsaAudioDevices::createAudioSink(const QAudioDevice &deviceInfo,
                                                       const QAudioFormat &fmt,
                                                       QObject *parent)
{
    return new QAlsaAudioSink(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiodevices.cpp, line 114, as _ZN17QAlsaAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSource *QAlsaAudioDevices::createAudioSource(const QAudioDevice &deviceInfo,
                                                           const QAudioFormat &fmt,
                                                           QObject *parent)
{
    return new QAlsaAudioSource(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 13, as _ZN16QAlsaAudioSourceC1E12QAudioDeviceRK12QAudioFormatP7QObject
inline QAlsaAudioSource::QAlsaAudioSource(QAudioDevice device, const QAudioFormat &fmt, QObject *parent)
    : QPlatformAudioSource(std::move(device), fmt, parent)
{
    bytesAvailable = 0;
    handle = 0;
    access = SND_PCM_ACCESS_RW_INTERLEAVED;
    pcmformat = SND_PCM_FORMAT_S16;
    buffer_size = 0;
    period_size = 0;
    buffer_time = 100000;
    period_time = 20000;
    totalTimeValue = 0;
    deviceState = QAudio::StoppedState;
    audioSource = 0;
    pullMode = true;
    resuming = false;

    timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, &QAlsaAudioSource::userFeed);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 15, as _ZN14QAlsaAudioSinkC1E12QAudioDeviceRK12QAudioFormatP7QObject
inline QAlsaAudioSink::QAlsaAudioSink(QAudioDevice device, const QAudioFormat &format, QObject *parent)
    : QPlatformAudioSink(std::move(device), format, parent)
{
    timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, &QAlsaAudioSink::userFeed);
}
//  -----------------------------------------------------------------------

//  A QAlsaAudioDevices that Python can take functions over in. Every QAlsaAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAlsaAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQAlsaAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQAlsaAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQAlsaAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAlsaAudioDevices : public QAlsaAudioDevices {
public:
  using QAlsaAudioDevices::QAlsaAudioDevices;
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

  //  QPlatformAudioSource *QAlsaAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAlsaAudioDevicesCall0 call = reinterpret_cast<CuteQAlsaAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QAlsaAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QAlsaAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAlsaAudioDevicesCall1 call = reinterpret_cast<CuteQAlsaAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QAlsaAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QAlsaAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAlsaAudioDevicesCall2 call = reinterpret_cast<CuteQAlsaAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAlsaAudioDevices::backendName();
  }

  //  bool QPlatformAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAlsaAudioDevicesCall3 call = reinterpret_cast<CuteQAlsaAudioDevicesCall3>(taken[3]);
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
      CuteQAlsaAudioDevicesCall4 call = reinterpret_cast<CuteQAlsaAudioDevicesCall4>(taken[4]);
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
      CuteQAlsaAudioDevicesCall5 call = reinterpret_cast<CuteQAlsaAudioDevicesCall5>(taken[5]);
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
      CuteQAlsaAudioDevicesCall6 call = reinterpret_cast<CuteQAlsaAudioDevicesCall6>(taken[6]);
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
      CuteQAlsaAudioDevicesCall7 call = reinterpret_cast<CuteQAlsaAudioDevicesCall7>(taken[7]);
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
      CuteQAlsaAudioDevicesCall8 call = reinterpret_cast<CuteQAlsaAudioDevicesCall8>(taken[8]);
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
      CuteQAlsaAudioDevicesCall9 call = reinterpret_cast<CuteQAlsaAudioDevicesCall9>(taken[9]);
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
      CuteQAlsaAudioDevicesCall10 call = reinterpret_cast<CuteQAlsaAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QPlatformAudioSource *QAlsaAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN17QAlsaAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAlsaAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QAlsaAudioDevices::createAudioSink(const QAudioDevice
//      &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN17QAlsaAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAlsaAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QAlsaAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK17QAlsaAudioDevices11backendNameEv(
    const QAlsaAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  QList<QAudioDevice> QAlsaAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK17QAlsaAudioDevices15findAudioInputsEv(
    const QAlsaAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QAlsaAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK17QAlsaAudioDevices16findAudioOutputsEv(
    const QAlsaAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

//  a Python function taken by a CuteQAlsaAudioDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAlsaAudioDevices(
    QAlsaAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAlsaAudioDevices *>(self)->take(key, call);
}

//  QLatin1String QAlsaAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK17QAlsaAudioDevices11backendNameEv(
    const QAlsaAudioDevices *self) {
  return new QLatin1String(self->QAlsaAudioDevices::backendName());
}

#endif  // QT_CONFIG(alsa)
