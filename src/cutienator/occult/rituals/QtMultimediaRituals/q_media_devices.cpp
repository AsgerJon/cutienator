//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediadevices.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediadevices.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qcameradevice.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMediaDevices may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMediaDevices : QMediaDevices {
  using QMediaDevices::connectNotify;
};

//  A QMediaDevices that Python can take functions over in. Every QMediaDevices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaDevicesCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaDevicesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaDevicesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaDevicesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaDevicesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaDevicesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaDevicesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMediaDevices : public QMediaDevices {
public:
  using QMediaDevices::QMediaDevices;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
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
  //  void QMediaDevices::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMediaDevicesCall0 call = reinterpret_cast<CuteQMediaDevicesCall0>(taken[0]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QMediaDevices::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMediaDevicesCall1 call = reinterpret_cast<CuteQMediaDevicesCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMediaDevicesCall2 call = reinterpret_cast<CuteQMediaDevicesCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMediaDevicesCall3 call = reinterpret_cast<CuteQMediaDevicesCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMediaDevicesCall4 call = reinterpret_cast<CuteQMediaDevicesCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMediaDevicesCall5 call = reinterpret_cast<CuteQMediaDevicesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMediaDevicesCall6 call = reinterpret_cast<CuteQMediaDevicesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMediaDevices::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QMediaDevices10metaObjectEv(
    const QMediaDevices *self) {
  return self->metaObject();
}

//  QString QMediaDevices::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QMediaDevices2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMediaDevices::tr(s, c, n));
}

//  QMediaDevices::QMediaDevices(QObject *parent)
extern "C" Q_DECL_EXPORT
QMediaDevices *ritual_ZN13QMediaDevicesC1EP7QObject(QObject *parent) {
  return new CuteQMediaDevices(parent);
}

//  QMediaDevices::~QMediaDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMediaDevicesD1Ev(QMediaDevices *self) {
  delete self;
}

//  QList<QAudioDevice> QMediaDevices::audioInputs()
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZN13QMediaDevices11audioInputsEv() {
  return new QList<QAudioDevice>(QMediaDevices::audioInputs());
}

//  QList<QAudioDevice> QMediaDevices::audioOutputs()
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_ZN13QMediaDevices12audioOutputsEv() {
  return new QList<QAudioDevice>(QMediaDevices::audioOutputs());
}

//  QList<QCameraDevice> QMediaDevices::videoInputs()
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_ZN13QMediaDevices11videoInputsEv() {
  return new QList<QCameraDevice>(QMediaDevices::videoInputs());
}

//  QAudioDevice QMediaDevices::defaultAudioInput()
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN13QMediaDevices17defaultAudioInputEv() {
  return new QAudioDevice(QMediaDevices::defaultAudioInput());
}

//  QAudioDevice QMediaDevices::defaultAudioOutput()
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN13QMediaDevices18defaultAudioOutputEv() {
  return new QAudioDevice(QMediaDevices::defaultAudioOutput());
}

//  QCameraDevice QMediaDevices::defaultVideoInput()
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZN13QMediaDevices17defaultVideoInputEv() {
  return new QCameraDevice(QMediaDevices::defaultVideoInput());
}

//  void QMediaDevices::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMediaDevices13connectNotifyERK11QMetaMethod(
    QMediaDevices *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  a Python function taken by a CuteQMediaDevices, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMediaDevices(
    QMediaDevices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMediaDevices *>(self)->take(key, call);
}

//  void QMediaDevices::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QMediaDevices13connectNotifyERK11QMetaMethod(
    QMediaDevices *self,
    const QMetaMethod *signal) {
  static_cast<OwnQMediaDevices *>(self)->OwnQMediaDevices::connectNotify(
      *signal);
}
