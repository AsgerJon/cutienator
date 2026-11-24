//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtROServerIoDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtROServerIoDevice : QtROServerIoDevice {
  using QtROServerIoDevice::deviceType;
};

//  A QtROServerIoDevice that Python can take functions over in. Every QtROServerIoDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQtROServerIoDeviceCall0)(const void *, int *);
typedef void (*CuteQtROServerIoDeviceCall1)(const void *, const QByteArray *, int *);
typedef void (*CuteQtROServerIoDeviceCall2)(const void *, const QByteArray *, qint64, int *);
typedef bool (*CuteQtROServerIoDeviceCall3)(const void *, int *);
typedef void (*CuteQtROServerIoDeviceCall4)(const void *, int *);
typedef qint64 (*CuteQtROServerIoDeviceCall5)(const void *, int *);
typedef void * (*CuteQtROServerIoDeviceCall6)(const void *, int *);
typedef void (*CuteQtROServerIoDeviceCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROServerIoDeviceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROServerIoDeviceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROServerIoDeviceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROServerIoDeviceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROServerIoDeviceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROServerIoDeviceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROServerIoDeviceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtROServerIoDevice : public QtROServerIoDevice {
public:
  using QtROServerIoDevice::QtROServerIoDevice;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10deviceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArray")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArrayx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase6isOpenEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5closeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase14bytesAvailableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10connectionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase7doCloseEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QtROServerIoDevice::deviceType() const
  QString deviceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall0 call = reinterpret_cast<CuteQtROServerIoDeviceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QtROServerIoDevice::deviceType();
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data)
  void write(const QByteArray &data) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall1 call = reinterpret_cast<CuteQtROServerIoDeviceCall1>(taken[1]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data);
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
  void write(const QByteArray &data, qint64 a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall2 call = reinterpret_cast<CuteQtROServerIoDeviceCall2>(taken[2]);
      call(this, &data, a1, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data, a1);
  }

  //  bool QtROIoDeviceBase::isOpen() const
  bool isOpen() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall3 call = reinterpret_cast<CuteQtROServerIoDeviceCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::isOpen();
  }

  //  void QtROIoDeviceBase::close()
  void close() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall4 call = reinterpret_cast<CuteQtROServerIoDeviceCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::close();
  }

  //  qint64 QtROIoDeviceBase::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall5 call = reinterpret_cast<CuteQtROServerIoDeviceCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::bytesAvailable();
  }

  //  QIODevice *QtROIoDeviceBase::connection() const
  QIODevice *connection() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall6 call = reinterpret_cast<CuteQtROServerIoDeviceCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QtROIoDeviceBase::doClose()
  void doClose() override {
    if (taken[7]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall7 call = reinterpret_cast<CuteQtROServerIoDeviceCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall8 call = reinterpret_cast<CuteQtROServerIoDeviceCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall9 call = reinterpret_cast<CuteQtROServerIoDeviceCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall10 call = reinterpret_cast<CuteQtROServerIoDeviceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall11 call = reinterpret_cast<CuteQtROServerIoDeviceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall12 call = reinterpret_cast<CuteQtROServerIoDeviceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall13 call = reinterpret_cast<CuteQtROServerIoDeviceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtROServerIoDeviceCall14 call = reinterpret_cast<CuteQtROServerIoDeviceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtROServerIoDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtROServerIoDevice10metaObjectEv(
    const QtROServerIoDevice *self) {
  return self->metaObject();
}

//  QString QtROServerIoDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtROServerIoDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtROServerIoDevice::tr(s, c, n));
}

//  QString QtROServerIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtROServerIoDevice10deviceTypeEv(
    const QtROServerIoDevice *self) {
  return new QString(self->deviceType());
}

//  a Python function taken by a CuteQtROServerIoDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtROServerIoDevice(
    QtROServerIoDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtROServerIoDevice *>(self)->take(key, call);
}

//  QString QtROServerIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QtROServerIoDevice10deviceTypeEv(
    const QtROServerIoDevice *self) {
  return new QString(
      static_cast<const OwnQtROServerIoDevice *>(self)->OwnQtROServerIoDevice::deviceType());
}
