//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_ANDROID)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qandroidaudiodevices_p.h>
#include <QtMultimedia/private/qandroidaudiodevice_p.h>
#include <QtMultimedia/private/qandroidaudiojnitypes_p.h>
#include <QtMultimedia/private/qandroidaudiosink_p.h>
#include <QtMultimedia/private/qandroidaudiosource_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtCore/qjniobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 80, as _ZN20QAndroidAudioDevicesC1Ev
inline QAndroidAudioDevices::QAndroidAudioDevices() : QPlatformAudioDevices()
{
    QtAudioDeviceManager::callStaticMethod<void>(
        "qAndroidAudioDevicesConstructed",
        static_cast<jlong>(reinterpret_cast<size_t>(this)));
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 87, as _ZN20QAndroidAudioDevicesD1Ev
inline QAndroidAudioDevices::~QAndroidAudioDevices()
{
    // Performs a blocking call to unregister QAndroidAudioDevices from receiving
    // any more callbacks, and flushes remaining callbacks.
    QtAudioDeviceManager::callStaticMethod<void>("qAndroidAudioDevicesDestroyed");
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 107, as _ZN20QAndroidAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSource *QAndroidAudioDevices::createAudioSource(const QAudioDevice &deviceInfo,
                                                              const QAudioFormat &fmt,
                                                              QObject *parent)
{
    return new QtAAudio::QAndroidAudioSource(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 115, as _ZN20QAndroidAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject
inline QPlatformAudioSink *QAndroidAudioDevices::createAudioSink(const QAudioDevice &deviceInfo,
                                                          const QAudioFormat &fmt, QObject *parent)
{
    return new QtAAudio::QAndroidAudioSink(deviceInfo, fmt, parent);
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 145, as _ZN20QAndroidAudioDevices21registerNativeMethodsEv
inline bool QAndroidAudioDevices::registerNativeMethods()
{
    static const bool registered = []{
        const auto context = QNativeInterface::QAndroidApplication::context();
        QtAudioDeviceManager::callStaticMethod<void>("setContext", context);

        return QtJniTypes::QtAudioDeviceManager::registerNativeMethods({
            Q_JNI_NATIVE_METHOD(onAudioInputDevicesUpdated),
            Q_JNI_NATIVE_METHOD(onAudioOutputDevicesUpdated),
        });
    }();
    return registered;
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 95, as _ZNK20QAndroidAudioDevices15findAudioInputsEv
inline QList<QAudioDevice> QAndroidAudioDevices::findAudioInputs() const
{
    return availableDevices(QAudioDevice::Input);
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevices.cpp, line 101, as _ZNK20QAndroidAudioDevices16findAudioOutputsEv
inline QList<QAudioDevice> QAndroidAudioDevices::findAudioOutputs() const
{
    return availableDevices(QAudioDevice::Output);
}
//  -----------------------------------------------------------------------

//  A QAndroidAudioDevices that Python can take functions over in. Every QAndroidAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAndroidAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQAndroidAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQAndroidAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQAndroidAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAndroidAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAndroidAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAndroidAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAndroidAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAndroidAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAndroidAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAndroidAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAndroidAudioDevices : public QAndroidAudioDevices {
public:
  using QAndroidAudioDevices::QAndroidAudioDevices;
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

  //  QPlatformAudioSource *QAndroidAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAndroidAudioDevicesCall0 call = reinterpret_cast<CuteQAndroidAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QAndroidAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QAndroidAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAndroidAudioDevicesCall1 call = reinterpret_cast<CuteQAndroidAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QAndroidAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QAndroidAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAndroidAudioDevicesCall2 call = reinterpret_cast<CuteQAndroidAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAndroidAudioDevices::backendName();
  }

  //  bool QAndroidAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAndroidAudioDevicesCall3 call = reinterpret_cast<CuteQAndroidAudioDevicesCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAndroidAudioDevices::hasCallbackApi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAndroidAudioDevicesCall4 call = reinterpret_cast<CuteQAndroidAudioDevicesCall4>(taken[4]);
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
      CuteQAndroidAudioDevicesCall5 call = reinterpret_cast<CuteQAndroidAudioDevicesCall5>(taken[5]);
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
      CuteQAndroidAudioDevicesCall6 call = reinterpret_cast<CuteQAndroidAudioDevicesCall6>(taken[6]);
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
      CuteQAndroidAudioDevicesCall7 call = reinterpret_cast<CuteQAndroidAudioDevicesCall7>(taken[7]);
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
      CuteQAndroidAudioDevicesCall8 call = reinterpret_cast<CuteQAndroidAudioDevicesCall8>(taken[8]);
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
      CuteQAndroidAudioDevicesCall9 call = reinterpret_cast<CuteQAndroidAudioDevicesCall9>(taken[9]);
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
      CuteQAndroidAudioDevicesCall10 call = reinterpret_cast<CuteQAndroidAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAndroidAudioDevices::QAndroidAudioDevices()
extern "C" Q_DECL_EXPORT
QAndroidAudioDevices *ritual_ZN20QAndroidAudioDevicesC1Ev() {
  return new CuteQAndroidAudioDevices();
}

//  QAndroidAudioDevices::~QAndroidAudioDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAndroidAudioDevicesD1Ev(QAndroidAudioDevices *self) {
  delete self;
}

//  QPlatformAudioSource *QAndroidAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN20QAndroidAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAndroidAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QAndroidAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN20QAndroidAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAndroidAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QAndroidAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK20QAndroidAudioDevices11backendNameEv(
    const QAndroidAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QAndroidAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAndroidAudioDevices14hasCallbackApiEv(
    const QAndroidAudioDevices *self) {
  return self->hasCallbackApi();
}

//  bool QAndroidAudioDevices::registerNativeMethods()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAndroidAudioDevices21registerNativeMethodsEv() {
  return QAndroidAudioDevices::registerNativeMethods();
}

//  QList<QAudioDevice> QAndroidAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK20QAndroidAudioDevices15findAudioInputsEv(
    const QAndroidAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QAndroidAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK20QAndroidAudioDevices16findAudioOutputsEv(
    const QAndroidAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

//  a Python function taken by a CuteQAndroidAudioDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAndroidAudioDevices(
    QAndroidAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAndroidAudioDevices *>(self)->take(key, call);
}

//  QPlatformAudioSource *QAndroidAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_own_ZN20QAndroidAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAndroidAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QAndroidAudioDevices::createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QAndroidAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_own_ZN20QAndroidAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QAndroidAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QAndroidAudioDevices::createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QAndroidAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK20QAndroidAudioDevices11backendNameEv(
    const QAndroidAudioDevices *self) {
  return new QLatin1String(self->QAndroidAudioDevices::backendName());
}

//  bool QAndroidAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QAndroidAudioDevices14hasCallbackApiEv(
    const QAndroidAudioDevices *self) {
  return self->QAndroidAudioDevices::hasCallbackApi();
}

#endif  // defined(Q_OS_ANDROID)
