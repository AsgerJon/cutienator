//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/QString>
#include <QtNetwork/QDnsLookup>
#include <QtNetwork/QHostAddress>

//  A QDnsLookup that Python can take functions over in. Every QDnsLookup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDnsLookupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDnsLookupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDnsLookupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDnsLookupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDnsLookupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDnsLookupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDnsLookupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDnsLookup : public QDnsLookup {
public:
  using QDnsLookup::QDnsLookup;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDnsLookupCall0 call = reinterpret_cast<CuteQDnsLookupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDnsLookupCall1 call = reinterpret_cast<CuteQDnsLookupCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDnsLookupCall2 call = reinterpret_cast<CuteQDnsLookupCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDnsLookupCall3 call = reinterpret_cast<CuteQDnsLookupCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDnsLookupCall4 call = reinterpret_cast<CuteQDnsLookupCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDnsLookupCall5 call = reinterpret_cast<CuteQDnsLookupCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDnsLookupCall6 call = reinterpret_cast<CuteQDnsLookupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDnsLookup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QDnsLookup10metaObjectEv(
    const QDnsLookup *self) {
  return self->metaObject();
}

//  void *QDnsLookup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QDnsLookup11qt_metacastEPKc(
    QDnsLookup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDnsLookup::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QDnsLookup11qt_metacallEN11QMetaObject4CallEiPPv(
    QDnsLookup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDnsLookup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QDnsLookup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDnsLookup::tr(s, c, n));
}

//  QDnsLookup::QDnsLookup(QObject *parent)
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN10QDnsLookupC1EP7QObject(QObject *parent) {
  return new CuteQDnsLookup(parent);
}

//  QDnsLookup::QDnsLookup(Type type, const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringP7QObject(
    QDnsLookup::Type type,
    const QString *name,
    QObject *parent) {
  return new CuteQDnsLookup(type, *name, parent);
}

//  QDnsLookup::QDnsLookup(Type type, const QString &name, const QHostAddress
//      &nameserver, QObject *parent)
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringRK12QHostAddressP7QObject(
    QDnsLookup::Type type,
    const QString *name,
    const QHostAddress *nameserver,
    QObject *parent) {
  return new CuteQDnsLookup(type, *name, *nameserver, parent);
}

//  QDnsLookup::QDnsLookup(Type type, const QString &name, const QHostAddress
//      &nameserver, quint16 port, QObject *parent)
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringRK12QHostAddresstP7QObject(
    QDnsLookup::Type type,
    const QString *name,
    const QHostAddress *nameserver,
    quint16 port,
    QObject *parent) {
  return new CuteQDnsLookup(type, *name, *nameserver, port, parent);
}

//  QDnsLookup::QDnsLookup(Type type, const QString &name, Protocol protocol,
//      const QHostAddress &nameserver, quint16 port, QObject *parent)
extern "C" Q_DECL_EXPORT
QDnsLookup *ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringNS_8ProtocolERK12QHostAddresstP7QObject(
    QDnsLookup::Type type,
    const QString *name,
    QDnsLookup::Protocol protocol,
    const QHostAddress *nameserver,
    quint16 port,
    QObject *parent) {
  return new CuteQDnsLookup(
      type,
      *name,
      protocol,
      *nameserver,
      port,
      parent);
}

//  QDnsLookup::~QDnsLookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookupD1Ev(QDnsLookup *self) {
  delete self;
}

//  bool QDnsLookup::isAuthenticData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QDnsLookup15isAuthenticDataEv(const QDnsLookup *self) {
  return self->isAuthenticData();
}

//  Error QDnsLookup::error() const
extern "C" Q_DECL_EXPORT
QDnsLookup::Error ritual_ZNK10QDnsLookup5errorEv(const QDnsLookup *self) {
  return self->error();
}

//  QString QDnsLookup::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDnsLookup11errorStringEv(const QDnsLookup *self) {
  return new QString(self->errorString());
}

//  bool QDnsLookup::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QDnsLookup10isFinishedEv(const QDnsLookup *self) {
  return self->isFinished();
}

//  QString QDnsLookup::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDnsLookup4nameEv(const QDnsLookup *self) {
  return new QString(self->name());
}

//  void QDnsLookup::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup7setNameERK7QString(
    QDnsLookup *self,
    const QString *name) {
  self->setName(*name);
}

//  QBindable<QString> QDnsLookup::bindableName()
extern "C" Q_DECL_EXPORT
QBindable<QString> *ritual_ZN10QDnsLookup12bindableNameEv(QDnsLookup *self) {
  return new QBindable<QString>(self->bindableName());
}

//  Type QDnsLookup::type() const
extern "C" Q_DECL_EXPORT
QDnsLookup::Type ritual_ZNK10QDnsLookup4typeEv(const QDnsLookup *self) {
  return self->type();
}

//  void QDnsLookup::setType(QDnsLookup::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup7setTypeENS_4TypeE(
    QDnsLookup *self,
    QDnsLookup::Type a0) {
  self->setType(a0);
}

//  QBindable<Type> QDnsLookup::bindableType()
extern "C" Q_DECL_EXPORT
QBindable<QDnsLookup::Type> *ritual_ZN10QDnsLookup12bindableTypeEv(
    QDnsLookup *self) {
  return new QBindable<QDnsLookup::Type>(self->bindableType());
}

//  QHostAddress QDnsLookup::nameserver() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK10QDnsLookup10nameserverEv(const QDnsLookup *self) {
  return new QHostAddress(self->nameserver());
}

//  void QDnsLookup::setNameserver(const QHostAddress &nameserver)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup13setNameserverERK12QHostAddress(
    QDnsLookup *self,
    const QHostAddress *nameserver) {
  self->setNameserver(*nameserver);
}

//  QBindable<QHostAddress> QDnsLookup::bindableNameserver()
extern "C" Q_DECL_EXPORT
QBindable<QHostAddress> *ritual_ZN10QDnsLookup18bindableNameserverEv(
    QDnsLookup *self) {
  return new QBindable<QHostAddress>(self->bindableNameserver());
}

//  quint16 QDnsLookup::nameserverPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK10QDnsLookup14nameserverPortEv(const QDnsLookup *self) {
  return self->nameserverPort();
}

//  void QDnsLookup::setNameserverPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup17setNameserverPortEt(
    QDnsLookup *self,
    quint16 port) {
  self->setNameserverPort(port);
}

//  QBindable<quint16> QDnsLookup::bindableNameserverPort()
extern "C" Q_DECL_EXPORT
QBindable<quint16> *ritual_ZN10QDnsLookup22bindableNameserverPortEv(
    QDnsLookup *self) {
  return new QBindable<quint16>(self->bindableNameserverPort());
}

//  Protocol QDnsLookup::nameserverProtocol() const
extern "C" Q_DECL_EXPORT
QDnsLookup::Protocol ritual_ZNK10QDnsLookup18nameserverProtocolEv(
    const QDnsLookup *self) {
  return self->nameserverProtocol();
}

//  void QDnsLookup::setNameserverProtocol(Protocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup21setNameserverProtocolENS_8ProtocolE(
    QDnsLookup *self,
    QDnsLookup::Protocol protocol) {
  self->setNameserverProtocol(protocol);
}

//  QBindable<Protocol> QDnsLookup::bindableNameserverProtocol()
extern "C" Q_DECL_EXPORT
QBindable<QDnsLookup::Protocol> *ritual_ZN10QDnsLookup26bindableNameserverProtocolEv(
    QDnsLookup *self) {
  return new QBindable<QDnsLookup::Protocol>(
      self->bindableNameserverProtocol());
}

//  void QDnsLookup::setNameserver(Protocol protocol, const QHostAddress
//      &nameserver, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup13setNameserverENS_8ProtocolERK12QHostAddresst(
    QDnsLookup *self,
    QDnsLookup::Protocol protocol,
    const QHostAddress *nameserver,
    quint16 port) {
  self->setNameserver(protocol, *nameserver, port);
}

//  void QDnsLookup::setNameserver(const QHostAddress &nameserver, quint16
//      port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup13setNameserverERK12QHostAddresst(
    QDnsLookup *self,
    const QHostAddress *nameserver,
    quint16 port) {
  self->setNameserver(*nameserver, port);
}

//  QList<QDnsDomainNameRecord> QDnsLookup::canonicalNameRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsDomainNameRecord> *ritual_ZNK10QDnsLookup20canonicalNameRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsDomainNameRecord>(self->canonicalNameRecords());
}

//  QList<QDnsHostAddressRecord> QDnsLookup::hostAddressRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsHostAddressRecord> *ritual_ZNK10QDnsLookup18hostAddressRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsHostAddressRecord>(self->hostAddressRecords());
}

//  QList<QDnsMailExchangeRecord> QDnsLookup::mailExchangeRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsMailExchangeRecord> *ritual_ZNK10QDnsLookup19mailExchangeRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsMailExchangeRecord>(self->mailExchangeRecords());
}

//  QList<QDnsDomainNameRecord> QDnsLookup::nameServerRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsDomainNameRecord> *ritual_ZNK10QDnsLookup17nameServerRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsDomainNameRecord>(self->nameServerRecords());
}

//  QList<QDnsDomainNameRecord> QDnsLookup::pointerRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsDomainNameRecord> *ritual_ZNK10QDnsLookup14pointerRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsDomainNameRecord>(self->pointerRecords());
}

//  QList<QDnsServiceRecord> QDnsLookup::serviceRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsServiceRecord> *ritual_ZNK10QDnsLookup14serviceRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsServiceRecord>(self->serviceRecords());
}

//  QList<QDnsTextRecord> QDnsLookup::textRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsTextRecord> *ritual_ZNK10QDnsLookup11textRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsTextRecord>(self->textRecords());
}

//  QList<QDnsTlsAssociationRecord> QDnsLookup::tlsAssociationRecords() const
extern "C" Q_DECL_EXPORT
QList<QDnsTlsAssociationRecord> *ritual_ZNK10QDnsLookup21tlsAssociationRecordsEv(
    const QDnsLookup *self) {
  return new QList<QDnsTlsAssociationRecord>(self->tlsAssociationRecords());
}

#if QT_CONFIG(ssl)
//  void QDnsLookup::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup19setSslConfigurationERK17QSslConfiguration(
    QDnsLookup *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QSslConfiguration QDnsLookup::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK10QDnsLookup16sslConfigurationEv(
    const QDnsLookup *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

//  bool QDnsLookup::isProtocolSupported(Protocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QDnsLookup19isProtocolSupportedENS_8ProtocolE(
    QDnsLookup::Protocol protocol) {
  return QDnsLookup::isProtocolSupported(protocol);
}

//  quint16 QDnsLookup::defaultPortForProtocol(Protocol protocol)
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN10QDnsLookup22defaultPortForProtocolENS_8ProtocolE(
    QDnsLookup::Protocol protocol) {
  return QDnsLookup::defaultPortForProtocol(protocol);
}

//  void QDnsLookup::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup5abortEv(QDnsLookup *self) {
  self->abort();
}

//  void QDnsLookup::lookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup6lookupEv(QDnsLookup *self) {
  self->lookup();
}

//  void QDnsLookup::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup8finishedEv(QDnsLookup *self) {
  self->finished();
}

//  void QDnsLookup::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup11nameChangedERK7QString(
    QDnsLookup *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void QDnsLookup::typeChanged(QDnsLookup::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup11typeChangedENS_4TypeE(
    QDnsLookup *self,
    QDnsLookup::Type type) {
  self->typeChanged(type);
}

//  void QDnsLookup::nameserverChanged(const QHostAddress &nameserver)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup17nameserverChangedERK12QHostAddress(
    QDnsLookup *self,
    const QHostAddress *nameserver) {
  self->nameserverChanged(*nameserver);
}

//  void QDnsLookup::nameserverPortChanged(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup21nameserverPortChangedEt(
    QDnsLookup *self,
    quint16 port) {
  self->nameserverPortChanged(port);
}

//  void QDnsLookup::nameserverProtocolChanged(QDnsLookup::Protocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDnsLookup25nameserverProtocolChangedENS_8ProtocolE(
    QDnsLookup *self,
    QDnsLookup::Protocol protocol) {
  self->nameserverProtocolChanged(protocol);
}

//  QDnsLookupPrivate *QDnsLookup::d_func()
extern "C" Q_DECL_EXPORT
QDnsLookupPrivate *ritual_ZN10QDnsLookup6d_funcEv(QDnsLookup *self) {
  return self->d_func();
}

//  const QDnsLookupPrivate *QDnsLookup::d_func() const
extern "C" Q_DECL_EXPORT
const QDnsLookupPrivate *ritual_ZNK10QDnsLookup6d_funcEv(
    const QDnsLookup *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDnsLookup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDnsLookup(QDnsLookup *self, const char *key, void *call) {
  return static_cast<CuteQDnsLookup *>(self)->take(key, call);
}

//  a QBindable<QString> a ritual of QDnsLookup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDnsLookup__QBindable_QString(QBindable<QString> *self) {
  delete self;
}

//  a QBindable<QDnsLookup::Type> a ritual of QDnsLookup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDnsLookup__QBindable_QDnsLookup_Type(
    QBindable<QDnsLookup::Type> *self) {
  delete self;
}

//  a QBindable<QHostAddress> a ritual of QDnsLookup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDnsLookup__QBindable_QHostAddress(
    QBindable<QHostAddress> *self) {
  delete self;
}

//  a QBindable<quint16> a ritual of QDnsLookup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDnsLookup__QBindable_quint16(QBindable<quint16> *self) {
  delete self;
}

//  a QBindable<QDnsLookup::Protocol> a ritual of QDnsLookup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDnsLookup__QBindable_QDnsLookup_Protocol(
    QBindable<QDnsLookup::Protocol> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
