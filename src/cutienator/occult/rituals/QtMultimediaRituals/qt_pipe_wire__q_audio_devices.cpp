//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qpipewire_audiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(pipewire)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qpipewire_audiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QtPipeWire::QAudioDevices that Python can take functions over in. Every QtPipeWire::QAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQtPipeWire_QAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQtPipeWire_QAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQtPipeWire_QAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQtPipeWire_QAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPipeWire_QAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPipeWire_QAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtPipeWire_QAudioDevices : public QtPipeWire::QAudioDevices {
public:
  using QtPipeWire::QAudioDevices::QAudioDevices;
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

  //  QPlatformAudioSource
  //      *QtPipeWire::QAudioDevices::createAudioSource(const QAudioDevice
  //      &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtPipeWire_QAudioDevicesCall0 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QtPipeWire::QAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QtPipeWire::QAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtPipeWire_QAudioDevicesCall1 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QtPipeWire::QAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QtPipeWire::QAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtPipeWire_QAudioDevicesCall2 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QtPipeWire::QAudioDevices::backendName();
  }

  //  bool QtPipeWire::QAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtPipeWire_QAudioDevicesCall3 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtPipeWire::QAudioDevices::hasCallbackApi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtPipeWire_QAudioDevicesCall4 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall4>(taken[4]);
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
      CuteQtPipeWire_QAudioDevicesCall5 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall5>(taken[5]);
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
      CuteQtPipeWire_QAudioDevicesCall6 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall6>(taken[6]);
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
      CuteQtPipeWire_QAudioDevicesCall7 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall7>(taken[7]);
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
      CuteQtPipeWire_QAudioDevicesCall8 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall8>(taken[8]);
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
      CuteQtPipeWire_QAudioDevicesCall9 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall9>(taken[9]);
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
      CuteQtPipeWire_QAudioDevicesCall10 call = reinterpret_cast<CuteQtPipeWire_QAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QtPipeWire::QAudioDevices::~QAudioDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtPipeWire13QAudioDevicesD1Ev(
    QtPipeWire::QAudioDevices *self) {
  delete self;
}

//  QList<QAudioDevice> QtPipeWire::QAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK10QtPipeWire13QAudioDevices15findAudioInputsEv(
    const QtPipeWire::QAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QtPipeWire::QAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK10QtPipeWire13QAudioDevices16findAudioOutputsEv(
    const QtPipeWire::QAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

//  QPlatformAudioSource *QtPipeWire::QAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN10QtPipeWire13QAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QtPipeWire::QAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QtPipeWire::QAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN10QtPipeWire13QAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QtPipeWire::QAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QtPipeWire::QAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK10QtPipeWire13QAudioDevices11backendNameEv(
    const QtPipeWire::QAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QtPipeWire::QAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QtPipeWire13QAudioDevices14hasCallbackApiEv(
    const QtPipeWire::QAudioDevices *self) {
  return self->hasCallbackApi();
}

//  a Python function taken by a CuteQtPipeWire_QAudioDevices, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtPipeWire_QAudioDevices(
    QtPipeWire::QAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtPipeWire_QAudioDevices *>(self)->take(key, call);
}

//  QLatin1String QtPipeWire::QAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK10QtPipeWire13QAudioDevices11backendNameEv(
    const QtPipeWire::QAudioDevices *self) {
  return new QLatin1String(self->QtPipeWire::QAudioDevices::backendName());
}

//  bool QtPipeWire::QAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QtPipeWire13QAudioDevices14hasCallbackApiEv(
    const QtPipeWire::QAudioDevices *self) {
  return self->QtPipeWire::QAudioDevices::hasCallbackApi();
}

#endif  // QT_CONFIG(pipewire)
