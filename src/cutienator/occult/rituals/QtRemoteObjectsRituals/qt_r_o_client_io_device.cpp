//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtROClientIoDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtROClientIoDevice : QtROClientIoDevice {
  using QtROClientIoDevice::deviceType;
};

//  A QtROClientIoDevice that Python can take functions over in. Every QtROClientIoDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtROClientIoDeviceCall0)(const void *, int *);
typedef void (*CuteQtROClientIoDeviceCall1)(const void *, int *);
typedef QString * (*CuteQtROClientIoDeviceCall2)(const void *, int *);
typedef void (*CuteQtROClientIoDeviceCall3)(const void *, const QByteArray *, int *);
typedef void (*CuteQtROClientIoDeviceCall4)(const void *, const QByteArray *, qint64, int *);
typedef bool (*CuteQtROClientIoDeviceCall5)(const void *, int *);
typedef void (*CuteQtROClientIoDeviceCall6)(const void *, int *);
typedef qint64 (*CuteQtROClientIoDeviceCall7)(const void *, int *);
typedef void * (*CuteQtROClientIoDeviceCall8)(const void *, int *);
typedef void (*CuteQtROClientIoDeviceCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROClientIoDeviceCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROClientIoDeviceCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROClientIoDeviceCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROClientIoDeviceCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROClientIoDeviceCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROClientIoDeviceCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROClientIoDeviceCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtROClientIoDevice : public QtROClientIoDevice {
public:
  using QtROClientIoDevice::QtROClientIoDevice;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QtROClientIoDevice15connectToServerEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QtROClientIoDevice22doDisconnectFromServerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10deviceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArray")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArrayx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase6isOpenEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5closeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase14bytesAvailableEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10connectionEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase7doCloseEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QtROClientIoDevice::connectToServer()
  void connectToServer() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall0 call = reinterpret_cast<CuteQtROClientIoDeviceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QtROClientIoDevice::doDisconnectFromServer()
  void doDisconnectFromServer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall1 call = reinterpret_cast<CuteQtROClientIoDeviceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QString QtROClientIoDevice::deviceType() const
  QString deviceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall2 call = reinterpret_cast<CuteQtROClientIoDeviceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QtROClientIoDevice::deviceType();
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data)
  void write(const QByteArray &data) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall3 call = reinterpret_cast<CuteQtROClientIoDeviceCall3>(taken[3]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data);
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
  void write(const QByteArray &data, qint64 a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall4 call = reinterpret_cast<CuteQtROClientIoDeviceCall4>(taken[4]);
      call(this, &data, a1, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data, a1);
  }

  //  bool QtROIoDeviceBase::isOpen() const
  bool isOpen() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall5 call = reinterpret_cast<CuteQtROClientIoDeviceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::isOpen();
  }

  //  void QtROIoDeviceBase::close()
  void close() override {
    if (taken[6]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall6 call = reinterpret_cast<CuteQtROClientIoDeviceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::close();
  }

  //  qint64 QtROIoDeviceBase::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall7 call = reinterpret_cast<CuteQtROClientIoDeviceCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::bytesAvailable();
  }

  //  QIODevice *QtROIoDeviceBase::connection() const
  QIODevice *connection() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall8 call = reinterpret_cast<CuteQtROClientIoDeviceCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QtROIoDeviceBase::doClose()
  void doClose() override {
    if (taken[9]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall9 call = reinterpret_cast<CuteQtROClientIoDeviceCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall10 call = reinterpret_cast<CuteQtROClientIoDeviceCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall11 call = reinterpret_cast<CuteQtROClientIoDeviceCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall12 call = reinterpret_cast<CuteQtROClientIoDeviceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall13 call = reinterpret_cast<CuteQtROClientIoDeviceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall14 call = reinterpret_cast<CuteQtROClientIoDeviceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall15 call = reinterpret_cast<CuteQtROClientIoDeviceCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtROClientIoDeviceCall16 call = reinterpret_cast<CuteQtROClientIoDeviceCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtROClientIoDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtROClientIoDevice10metaObjectEv(
    const QtROClientIoDevice *self) {
  return self->metaObject();
}

//  QString QtROClientIoDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtROClientIoDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtROClientIoDevice::tr(s, c, n));
}

//  QtROClientIoDevice::~QtROClientIoDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtROClientIoDeviceD1Ev(QtROClientIoDevice *self) {
  delete self;
}

//  void QtROClientIoDevice::disconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtROClientIoDevice20disconnectFromServerEv(
    QtROClientIoDevice *self) {
  self->disconnectFromServer();
}

//  void QtROClientIoDevice::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtROClientIoDevice15connectToServerEv(
    QtROClientIoDevice *self) {
  self->connectToServer();
}

//  QUrl QtROClientIoDevice::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QtROClientIoDevice3urlEv(const QtROClientIoDevice *self) {
  return new QUrl(self->url());
}

//  void QtROClientIoDevice::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtROClientIoDevice22doDisconnectFromServerEv(
    QtROClientIoDevice *self) {
  self->doDisconnectFromServer();
}

//  QString QtROClientIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtROClientIoDevice10deviceTypeEv(
    const QtROClientIoDevice *self) {
  return new QString(self->deviceType());
}

//  void QtROClientIoDevice::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtROClientIoDevice6setUrlERK4QUrl(
    QtROClientIoDevice *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QtROClientIoDevicePrivate *QtROClientIoDevice::d_func()
extern "C" Q_DECL_EXPORT
QtROClientIoDevicePrivate *ritual_ZN18QtROClientIoDevice6d_funcEv(
    QtROClientIoDevice *self) {
  return self->d_func();
}

//  const QtROClientIoDevicePrivate *QtROClientIoDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QtROClientIoDevicePrivate *ritual_ZNK18QtROClientIoDevice6d_funcEv(
    const QtROClientIoDevice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtROClientIoDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtROClientIoDevice(
    QtROClientIoDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtROClientIoDevice *>(self)->take(key, call);
}

//  QString QtROClientIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QtROClientIoDevice10deviceTypeEv(
    const QtROClientIoDevice *self) {
  return new QString(
      static_cast<const OwnQtROClientIoDevice *>(self)->OwnQtROClientIoDevice::deviceType());
}
