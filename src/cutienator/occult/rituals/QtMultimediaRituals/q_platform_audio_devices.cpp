//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <memory>

//  A QPlatformAudioDevices that Python can take functions over in. Every QPlatformAudioDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformAudioDevicesCall0)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef void * (*CuteQPlatformAudioDevicesCall1)(const void *, const QAudioDevice *, const QAudioFormat *, QObject *, int *);
typedef const QLatin1String * (*CuteQPlatformAudioDevicesCall2)(const void *, int *);
typedef bool (*CuteQPlatformAudioDevicesCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioDevicesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioDevicesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDevicesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDevicesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDevicesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDevicesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDevicesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformAudioDevices : public QPlatformAudioDevices {
public:
  using QPlatformAudioDevices::QPlatformAudioDevices;
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

  //  QPlatformAudioSource *QPlatformAudioDevices::createAudioSource(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSource *createAudioSource(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioDevicesCall0 call = reinterpret_cast<CuteQPlatformAudioDevicesCall0>(taken[0]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSource *>(given);
    }
    return QPlatformAudioDevices::createAudioSource(a0, a1, parent);
  }

  //  QPlatformAudioSink *QPlatformAudioDevices::createAudioSink(const
  //      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
  QPlatformAudioSink *createAudioSink(
      const QAudioDevice &a0,
      const QAudioFormat &a1,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioDevicesCall1 call = reinterpret_cast<CuteQPlatformAudioDevicesCall1>(taken[1]);
      void * given = call(this, &a0, &a1, parent, &handled);
      if (handled) return static_cast<QPlatformAudioSink *>(given);
    }
    return QPlatformAudioDevices::createAudioSink(a0, a1, parent);
  }

  //  QLatin1String QPlatformAudioDevices::backendName() const
  QLatin1String backendName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioDevicesCall2 call = reinterpret_cast<CuteQPlatformAudioDevicesCall2>(taken[2]);
      const QLatin1String * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformAudioDevices::backendName();
  }

  //  bool QPlatformAudioDevices::hasCallbackApi() const
  bool hasCallbackApi() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAudioDevicesCall3 call = reinterpret_cast<CuteQPlatformAudioDevicesCall3>(taken[3]);
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
      CuteQPlatformAudioDevicesCall4 call = reinterpret_cast<CuteQPlatformAudioDevicesCall4>(taken[4]);
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
      CuteQPlatformAudioDevicesCall5 call = reinterpret_cast<CuteQPlatformAudioDevicesCall5>(taken[5]);
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
      CuteQPlatformAudioDevicesCall6 call = reinterpret_cast<CuteQPlatformAudioDevicesCall6>(taken[6]);
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
      CuteQPlatformAudioDevicesCall7 call = reinterpret_cast<CuteQPlatformAudioDevicesCall7>(taken[7]);
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
      CuteQPlatformAudioDevicesCall8 call = reinterpret_cast<CuteQPlatformAudioDevicesCall8>(taken[8]);
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
      CuteQPlatformAudioDevicesCall9 call = reinterpret_cast<CuteQPlatformAudioDevicesCall9>(taken[9]);
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
      CuteQPlatformAudioDevicesCall10 call = reinterpret_cast<CuteQPlatformAudioDevicesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformAudioDevices::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlatformAudioDevices10metaObjectEv(
    const QPlatformAudioDevices *self) {
  return self->metaObject();
}

//  void *QPlatformAudioDevices::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QPlatformAudioDevices11qt_metacastEPKc(
    QPlatformAudioDevices *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformAudioDevices::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QPlatformAudioDevices11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformAudioDevices *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformAudioDevices::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPlatformAudioDevices2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioDevices::tr(s, c, n));
}

//  QPlatformAudioDevices::QPlatformAudioDevices()
extern "C" Q_DECL_EXPORT
QPlatformAudioDevices *ritual_ZN21QPlatformAudioDevicesC1Ev() {
  return new CuteQPlatformAudioDevices();
}

//  QPlatformAudioDevices::~QPlatformAudioDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevicesD1Ev(QPlatformAudioDevices *self) {
  delete self;
}

//  std::unique_ptr<QPlatformAudioDevices> QPlatformAudioDevices::create()
extern "C" Q_DECL_EXPORT
std::unique_ptr<QPlatformAudioDevices> *ritual_ZN21QPlatformAudioDevices6createEv() {
  return new std::unique_ptr<QPlatformAudioDevices>(
      QPlatformAudioDevices::create());
}

//  QList<QAudioDevice> QPlatformAudioDevices::audioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK21QPlatformAudioDevices11audioInputsEv(
    const QPlatformAudioDevices *self) {
  return new QList<QAudioDevice>(self->audioInputs());
}

//  QList<QAudioDevice> QPlatformAudioDevices::audioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK21QPlatformAudioDevices12audioOutputsEv(
    const QPlatformAudioDevices *self) {
  return new QList<QAudioDevice>(self->audioOutputs());
}

//  QPlatformAudioSource *QPlatformAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN21QPlatformAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPlatformAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QPlatformAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPlatformAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->createAudioSink(*a0, *a1, parent);
}

//  QPlatformAudioSource
//      *QPlatformAudioDevices::audioInputDevice(QAudioFormat a0, const
//      QAudioDevice &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN21QPlatformAudioDevices16audioInputDeviceE12QAudioFormatRK12QAudioDeviceP7QObject(
    QPlatformAudioDevices *self,
    const QAudioFormat *a0,
    const QAudioDevice *a1,
    QObject *parent) {
  return self->audioInputDevice(*a0, *a1, parent);
}

//  QPlatformAudioSink *QPlatformAudioDevices::audioOutputDevice(QAudioFormat
//      a0, const QAudioDevice &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_ZN21QPlatformAudioDevices17audioOutputDeviceE12QAudioFormatRK12QAudioDeviceP7QObject(
    QPlatformAudioDevices *self,
    const QAudioFormat *a0,
    const QAudioDevice *a1,
    QObject *parent) {
  return self->audioOutputDevice(*a0, *a1, parent);
}

//  QLatin1String QPlatformAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK21QPlatformAudioDevices11backendNameEv(
    const QPlatformAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QPlatformAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformAudioDevices14hasCallbackApiEv(
    const QPlatformAudioDevices *self) {
  return self->hasCallbackApi();
}

//  QList<QAudioDevice> QPlatformAudioDevices::findAudioInputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK21QPlatformAudioDevices15findAudioInputsEv(
    const QPlatformAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioInputs());
}

//  QList<QAudioDevice> QPlatformAudioDevices::findAudioOutputs() const
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZNK21QPlatformAudioDevices16findAudioOutputsEv(
    const QPlatformAudioDevices *self) {
  return new QList<QAudioDevice>(self->findAudioOutputs());
}

//  void QPlatformAudioDevices::onAudioInputsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices20onAudioInputsChangedEv(
    QPlatformAudioDevices *self) {
  self->onAudioInputsChanged();
}

//  void QPlatformAudioDevices::onAudioOutputsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices21onAudioOutputsChangedEv(
    QPlatformAudioDevices *self) {
  self->onAudioOutputsChanged();
}

//  void QPlatformAudioDevices::updateAudioInputsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices22updateAudioInputsCacheEv(
    QPlatformAudioDevices *self) {
  self->updateAudioInputsCache();
}

//  void QPlatformAudioDevices::updateAudioOutputsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices23updateAudioOutputsCacheEv(
    QPlatformAudioDevices *self) {
  self->updateAudioOutputsCache();
}

//  void QPlatformAudioDevices::audioInputsChanged(PrivateTag a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices18audioInputsChangedENS_10PrivateTagE(
    QPlatformAudioDevices *self,
    const QPlatformAudioDevices::PrivateTag *a0) {
  self->audioInputsChanged(*a0);
}

//  void QPlatformAudioDevices::audioOutputsChanged(PrivateTag a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDevices19audioOutputsChangedENS_10PrivateTagE(
    QPlatformAudioDevices *self,
    const QPlatformAudioDevices::PrivateTag *a0) {
  self->audioOutputsChanged(*a0);
}

//  a Python function taken by a CuteQPlatformAudioDevices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioDevices(
    QPlatformAudioDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioDevices *>(self)->take(key, call);
}

//  QPlatformAudioSource *QPlatformAudioDevices::createAudioSource(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_own_ZN21QPlatformAudioDevices17createAudioSourceERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPlatformAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QPlatformAudioDevices::createAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSink *QPlatformAudioDevices::createAudioSink(const
//      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSink *ritual_own_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudioDeviceRK12QAudioFormatP7QObject(
    QPlatformAudioDevices *self,
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return self->QPlatformAudioDevices::createAudioSink(*a0, *a1, parent);
}

//  QLatin1String QPlatformAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_own_ZNK21QPlatformAudioDevices11backendNameEv(
    const QPlatformAudioDevices *self) {
  return new QLatin1String(self->QPlatformAudioDevices::backendName());
}

//  bool QPlatformAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformAudioDevices14hasCallbackApiEv(
    const QPlatformAudioDevices *self) {
  return self->QPlatformAudioDevices::hasCallbackApi();
}

//  a std::unique_ptr<QPlatformAudioDevices> a ritual of
//      QPlatformAudioDevices gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformAudioDevices__std_unique_ptr_QPlatformAudioDevices(
    std::unique_ptr<QPlatformAudioDevices> *self) {
  delete self;
}
