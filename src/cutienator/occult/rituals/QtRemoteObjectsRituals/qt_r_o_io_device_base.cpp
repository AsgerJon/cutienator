//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSet>
#include <QtCore/QString>

//  A QtROIoDeviceBase that Python can take functions over in. Every QtROIoDeviceBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtROIoDeviceBaseCall0)(const void *, const QByteArray *, int *);
typedef void (*CuteQtROIoDeviceBaseCall1)(const void *, const QByteArray *, qint64, int *);
typedef bool (*CuteQtROIoDeviceBaseCall2)(const void *, int *);
typedef void (*CuteQtROIoDeviceBaseCall3)(const void *, int *);
typedef qint64 (*CuteQtROIoDeviceBaseCall4)(const void *, int *);
typedef void * (*CuteQtROIoDeviceBaseCall5)(const void *, int *);
typedef QString * (*CuteQtROIoDeviceBaseCall6)(const void *, int *);
typedef void (*CuteQtROIoDeviceBaseCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROIoDeviceBaseCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtROIoDeviceBaseCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROIoDeviceBaseCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROIoDeviceBaseCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROIoDeviceBaseCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROIoDeviceBaseCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtROIoDeviceBaseCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtROIoDeviceBase : public QtROIoDeviceBase {
public:
  using QtROIoDeviceBase::QtROIoDeviceBase;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArray")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArrayx")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase6isOpenEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5closeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase14bytesAvailableEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10connectionEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10deviceTypeEv")) {
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

  //  void QtROIoDeviceBase::write(const QByteArray &data)
  void write(const QByteArray &data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall0 call = reinterpret_cast<CuteQtROIoDeviceBaseCall0>(taken[0]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data);
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
  void write(const QByteArray &data, qint64 a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall1 call = reinterpret_cast<CuteQtROIoDeviceBaseCall1>(taken[1]);
      call(this, &data, a1, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data, a1);
  }

  //  bool QtROIoDeviceBase::isOpen() const
  bool isOpen() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall2 call = reinterpret_cast<CuteQtROIoDeviceBaseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::isOpen();
  }

  //  void QtROIoDeviceBase::close()
  void close() override {
    if (taken[3]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall3 call = reinterpret_cast<CuteQtROIoDeviceBaseCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::close();
  }

  //  qint64 QtROIoDeviceBase::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall4 call = reinterpret_cast<CuteQtROIoDeviceBaseCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::bytesAvailable();
  }

  //  QIODevice *QtROIoDeviceBase::connection() const
  QIODevice *connection() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall5 call = reinterpret_cast<CuteQtROIoDeviceBaseCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  QString QtROIoDeviceBase::deviceType() const
  QString deviceType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall6 call = reinterpret_cast<CuteQtROIoDeviceBaseCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QtROIoDeviceBase::doClose()
  void doClose() override {
    if (taken[7]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall7 call = reinterpret_cast<CuteQtROIoDeviceBaseCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtROIoDeviceBaseCall8 call = reinterpret_cast<CuteQtROIoDeviceBaseCall8>(taken[8]);
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
      CuteQtROIoDeviceBaseCall9 call = reinterpret_cast<CuteQtROIoDeviceBaseCall9>(taken[9]);
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
      CuteQtROIoDeviceBaseCall10 call = reinterpret_cast<CuteQtROIoDeviceBaseCall10>(taken[10]);
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
      CuteQtROIoDeviceBaseCall11 call = reinterpret_cast<CuteQtROIoDeviceBaseCall11>(taken[11]);
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
      CuteQtROIoDeviceBaseCall12 call = reinterpret_cast<CuteQtROIoDeviceBaseCall12>(taken[12]);
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
      CuteQtROIoDeviceBaseCall13 call = reinterpret_cast<CuteQtROIoDeviceBaseCall13>(taken[13]);
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
      CuteQtROIoDeviceBaseCall14 call = reinterpret_cast<CuteQtROIoDeviceBaseCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtROIoDeviceBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QtROIoDeviceBase10metaObjectEv(
    const QtROIoDeviceBase *self) {
  return self->metaObject();
}

//  void *QtROIoDeviceBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QtROIoDeviceBase11qt_metacastEPKc(
    QtROIoDeviceBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtROIoDeviceBase::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QtROIoDeviceBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QtROIoDeviceBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtROIoDeviceBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QtROIoDeviceBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtROIoDeviceBase::tr(s, c, n));
}

//  QtROIoDeviceBase::QtROIoDeviceBase(QObject *parent)
extern "C" Q_DECL_EXPORT
QtROIoDeviceBase *ritual_ZN16QtROIoDeviceBaseC1EP7QObject(QObject *parent) {
  return new CuteQtROIoDeviceBase(parent);
}

//  QtROIoDeviceBase::~QtROIoDeviceBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBaseD1Ev(QtROIoDeviceBase *self) {
  delete self;
}

//  bool QtROIoDeviceBase::read(QtRemoteObjects::QRemoteObjectPacketTypeEnum
//      &a0, QString &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QtROIoDeviceBase4readERN15QtRemoteObjects27QRemoteObjectPacketTypeEnumER7QString(
    QtROIoDeviceBase *self,
    QtRemoteObjects::QRemoteObjectPacketTypeEnum *a0,
    QString *a1) {
  return self->read(*a0, *a1);
}

//  void QtROIoDeviceBase::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase5writeERK10QByteArray(
    QtROIoDeviceBase *self,
    const QByteArray *data) {
  self->write(*data);
}

//  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase5writeERK10QByteArrayx(
    QtROIoDeviceBase *self,
    const QByteArray *data,
    qint64 a1) {
  self->write(*data, a1);
}

//  bool QtROIoDeviceBase::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QtROIoDeviceBase6isOpenEv(const QtROIoDeviceBase *self) {
  return self->isOpen();
}

//  void QtROIoDeviceBase::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase5closeEv(QtROIoDeviceBase *self) {
  self->close();
}

//  qint64 QtROIoDeviceBase::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QtROIoDeviceBase14bytesAvailableEv(
    const QtROIoDeviceBase *self) {
  return self->bytesAvailable();
}

//  QIODevice *QtROIoDeviceBase::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK16QtROIoDeviceBase10connectionEv(
    const QtROIoDeviceBase *self) {
  return self->connection();
}

//  void QtROIoDeviceBase::initializeDataStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase20initializeDataStreamEv(
    QtROIoDeviceBase *self) {
  self->initializeDataStream();
}

//  bool QtROIoDeviceBase::isClosing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QtROIoDeviceBase9isClosingEv(const QtROIoDeviceBase *self) {
  return self->isClosing();
}

//  void QtROIoDeviceBase::addSource(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase9addSourceERK7QString(
    QtROIoDeviceBase *self,
    const QString *a0) {
  self->addSource(*a0);
}

//  void QtROIoDeviceBase::removeSource(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase12removeSourceERK7QString(
    QtROIoDeviceBase *self,
    const QString *a0) {
  self->removeSource(*a0);
}

//  QSet<QString> QtROIoDeviceBase::remoteObjects() const
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZNK16QtROIoDeviceBase13remoteObjectsEv(
    const QtROIoDeviceBase *self) {
  return new QSet<QString>(self->remoteObjects());
}

//  void QtROIoDeviceBase::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase9readyReadEv(QtROIoDeviceBase *self) {
  self->readyRead();
}

//  void QtROIoDeviceBase::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase12disconnectedEv(QtROIoDeviceBase *self) {
  self->disconnected();
}

//  QtROIoDeviceBase::QtROIoDeviceBase(QtROIoDeviceBasePrivate &a0, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtROIoDeviceBase *ritual_ZN16QtROIoDeviceBaseC1ER23QtROIoDeviceBasePrivateP7QObject(
    QtROIoDeviceBasePrivate *a0,
    QObject *parent) {
  return new CuteQtROIoDeviceBase(*a0, parent);
}

//  QString QtROIoDeviceBase::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QtROIoDeviceBase10deviceTypeEv(
    const QtROIoDeviceBase *self) {
  return new QString(self->deviceType());
}

//  void QtROIoDeviceBase::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QtROIoDeviceBase7doCloseEv(QtROIoDeviceBase *self) {
  self->doClose();
}

//  QtROIoDeviceBasePrivate *QtROIoDeviceBase::d_func()
extern "C" Q_DECL_EXPORT
QtROIoDeviceBasePrivate *ritual_ZN16QtROIoDeviceBase6d_funcEv(
    QtROIoDeviceBase *self) {
  return self->d_func();
}

//  const QtROIoDeviceBasePrivate *QtROIoDeviceBase::d_func() const
extern "C" Q_DECL_EXPORT
const QtROIoDeviceBasePrivate *ritual_ZNK16QtROIoDeviceBase6d_funcEv(
    const QtROIoDeviceBase *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtROIoDeviceBase, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtROIoDeviceBase(
    QtROIoDeviceBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtROIoDeviceBase *>(self)->take(key, call);
}

//  void QtROIoDeviceBase::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QtROIoDeviceBase5writeERK10QByteArray(
    QtROIoDeviceBase *self,
    const QByteArray *data) {
  self->QtROIoDeviceBase::write(*data);
}

//  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QtROIoDeviceBase5writeERK10QByteArrayx(
    QtROIoDeviceBase *self,
    const QByteArray *data,
    qint64 a1) {
  self->QtROIoDeviceBase::write(*data, a1);
}

//  bool QtROIoDeviceBase::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QtROIoDeviceBase6isOpenEv(
    const QtROIoDeviceBase *self) {
  return self->QtROIoDeviceBase::isOpen();
}

//  void QtROIoDeviceBase::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QtROIoDeviceBase5closeEv(QtROIoDeviceBase *self) {
  self->QtROIoDeviceBase::close();
}

//  qint64 QtROIoDeviceBase::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QtROIoDeviceBase14bytesAvailableEv(
    const QtROIoDeviceBase *self) {
  return self->QtROIoDeviceBase::bytesAvailable();
}

//  a QSet<QString> a ritual of QtROIoDeviceBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtROIoDeviceBase__QSet_QString(QSet<QString> *self) {
  delete self;
}
