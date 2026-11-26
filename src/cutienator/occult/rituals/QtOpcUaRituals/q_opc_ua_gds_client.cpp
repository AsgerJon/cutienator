//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuagdsclient.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtOpcUa/qtopcua-config.h> before the #if, as it defines
//  QT_CONFIG(gds); the long #if line split in two.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/qopcuagdsclient.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtOpcUa/qopcuapkiconfiguration.h>
#include <QtOpcUa/qopcuaapplicationidentity.h>
#include <QtOpcUa/qopcuaapplicationrecorddatatype.h>
#include <QtOpcUa/qopcuax509distinguishedname.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaGdsClient that Python can take functions over in. Every QOpcUaGdsClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaGdsClientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaGdsClientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGdsClientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGdsClientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGdsClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGdsClientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGdsClientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaGdsClient : public QOpcUaGdsClient {
public:
  using QOpcUaGdsClient::QOpcUaGdsClient;
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
      CuteQOpcUaGdsClientCall0 call = reinterpret_cast<CuteQOpcUaGdsClientCall0>(taken[0]);
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
      CuteQOpcUaGdsClientCall1 call = reinterpret_cast<CuteQOpcUaGdsClientCall1>(taken[1]);
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
      CuteQOpcUaGdsClientCall2 call = reinterpret_cast<CuteQOpcUaGdsClientCall2>(taken[2]);
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
      CuteQOpcUaGdsClientCall3 call = reinterpret_cast<CuteQOpcUaGdsClientCall3>(taken[3]);
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
      CuteQOpcUaGdsClientCall4 call = reinterpret_cast<CuteQOpcUaGdsClientCall4>(taken[4]);
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
      CuteQOpcUaGdsClientCall5 call = reinterpret_cast<CuteQOpcUaGdsClientCall5>(taken[5]);
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
      CuteQOpcUaGdsClientCall6 call = reinterpret_cast<CuteQOpcUaGdsClientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaGdsClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QOpcUaGdsClient10metaObjectEv(
    const QOpcUaGdsClient *self) {
  return self->metaObject();
}

//  void *QOpcUaGdsClient::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QOpcUaGdsClient11qt_metacastEPKc(
    QOpcUaGdsClient *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QOpcUaGdsClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QOpcUaGdsClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaGdsClient::tr(s, c, n));
}

//  QOpcUaGdsClientPrivate *QOpcUaGdsClient::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaGdsClientPrivate *ritual_ZN15QOpcUaGdsClient6d_funcEv(
    QOpcUaGdsClient *self) {
  return self->d_func();
}

//  const QOpcUaGdsClientPrivate *QOpcUaGdsClient::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaGdsClientPrivate *ritual_ZNK15QOpcUaGdsClient6d_funcEv(
    const QOpcUaGdsClient *self) {
  return self->d_func();
}

//  QOpcUaGdsClient::QOpcUaGdsClient(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpcUaGdsClient *ritual_ZN15QOpcUaGdsClientC1EP7QObject(QObject *parent) {
  return new CuteQOpcUaGdsClient(parent);
}

//  QOpcUaGdsClient::~QOpcUaGdsClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClientD1Ev(QOpcUaGdsClient *self) {
  delete self;
}

//  void QOpcUaGdsClient::setBackend(const QString &backend)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient10setBackendERK7QString(
    QOpcUaGdsClient *self,
    const QString *backend) {
  self->setBackend(*backend);
}

//  const QString &QOpcUaGdsClient::backend() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaGdsClient7backendEv(const QOpcUaGdsClient *self) {
  return new QString(self->backend());
}

//  void QOpcUaGdsClient::setEndpoint(const QOpcUaEndpointDescription
//      &endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient11setEndpointERK25QOpcUaEndpointDescription(
    QOpcUaGdsClient *self,
    const QOpcUaEndpointDescription *endpoint) {
  self->setEndpoint(*endpoint);
}

//  const QOpcUaEndpointDescription &QOpcUaGdsClient::endpoint() const
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_ZNK15QOpcUaGdsClient8endpointEv(
    const QOpcUaGdsClient *self) {
  return new QOpcUaEndpointDescription(self->endpoint());
}

//  void QOpcUaGdsClient::setPkiConfiguration(const QOpcUaPkiConfiguration
//      &pkiConfig)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient19setPkiConfigurationERK22QOpcUaPkiConfiguration(
    QOpcUaGdsClient *self,
    const QOpcUaPkiConfiguration *pkiConfig) {
  self->setPkiConfiguration(*pkiConfig);
}

//  const QOpcUaPkiConfiguration &QOpcUaGdsClient::pkiConfiguration() const
extern "C" Q_DECL_EXPORT
QOpcUaPkiConfiguration *ritual_ZNK15QOpcUaGdsClient16pkiConfigurationEv(
    const QOpcUaGdsClient *self) {
  return new QOpcUaPkiConfiguration(self->pkiConfiguration());
}

//  void QOpcUaGdsClient::setApplicationIdentity(const
//      QOpcUaApplicationIdentity &appIdentity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient22setApplicationIdentityERK25QOpcUaApplicationIdentity(
    QOpcUaGdsClient *self,
    const QOpcUaApplicationIdentity *appIdentity) {
  self->setApplicationIdentity(*appIdentity);
}

//  const QOpcUaApplicationIdentity &QOpcUaGdsClient::applicationIdentity()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZNK15QOpcUaGdsClient19applicationIdentityEv(
    const QOpcUaGdsClient *self) {
  return new QOpcUaApplicationIdentity(self->applicationIdentity());
}

//  void QOpcUaGdsClient::setApplicationRecord(const
//      QOpcUaApplicationRecordDataType &appRecord)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient20setApplicationRecordERK31QOpcUaApplicationRecordDataType(
    QOpcUaGdsClient *self,
    const QOpcUaApplicationRecordDataType *appRecord) {
  self->setApplicationRecord(*appRecord);
}

//  const QOpcUaApplicationRecordDataType
//      &QOpcUaGdsClient::applicationRecord() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationRecordDataType *ritual_ZNK15QOpcUaGdsClient17applicationRecordEv(
    const QOpcUaGdsClient *self) {
  return new QOpcUaApplicationRecordDataType(self->applicationRecord());
}

//  QString QOpcUaGdsClient::applicationId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaGdsClient13applicationIdEv(
    const QOpcUaGdsClient *self) {
  return new QString(self->applicationId());
}

//  void QOpcUaGdsClient::setCertificateSigningRequestPresets(const
//      QOpcUaX509DistinguishedName &dn, const QString &dns)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient35setCertificateSigningRequestPresetsERK27QOpcUaX509DistinguishedNameRK7QString(
    QOpcUaGdsClient *self,
    const QOpcUaX509DistinguishedName *dn,
    const QString *dns) {
  self->setCertificateSigningRequestPresets(*dn, *dns);
}

//  const QOpcUaX509DistinguishedName
//      &QOpcUaGdsClient::distinguishedNameCertificateSigningRequestPreset()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaX509DistinguishedName *ritual_ZNK15QOpcUaGdsClient48distinguishedNameCertificateSigningRequestPresetEv(
    const QOpcUaGdsClient *self) {
  return new QOpcUaX509DistinguishedName(
      self->distinguishedNameCertificateSigningRequestPreset());
}

//  const QString &QOpcUaGdsClient::dnsCertificateSigningRequestPreset()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaGdsClient34dnsCertificateSigningRequestPresetEv(
    const QOpcUaGdsClient *self) {
  return new QString(self->dnsCertificateSigningRequestPreset());
}

//  void QOpcUaGdsClient::setCertificateCheckInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient27setCertificateCheckIntervalEi(
    QOpcUaGdsClient *self,
    int interval) {
  self->setCertificateCheckInterval(interval);
}

//  int QOpcUaGdsClient::certificateCheckInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QOpcUaGdsClient24certificateCheckIntervalEv(
    const QOpcUaGdsClient *self) {
  return self->certificateCheckInterval();
}

//  void QOpcUaGdsClient::setTrustListUpdateInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient26setTrustListUpdateIntervalEi(
    QOpcUaGdsClient *self,
    int interval) {
  self->setTrustListUpdateInterval(interval);
}

//  int QOpcUaGdsClient::trustListUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QOpcUaGdsClient23trustListUpdateIntervalEv(
    const QOpcUaGdsClient *self) {
  return self->trustListUpdateInterval();
}

//  Error QOpcUaGdsClient::error() const
extern "C" Q_DECL_EXPORT
QOpcUaGdsClient::Error ritual_ZNK15QOpcUaGdsClient5errorEv(
    const QOpcUaGdsClient *self) {
  return self->error();
}

//  State QOpcUaGdsClient::state() const
extern "C" Q_DECL_EXPORT
QOpcUaGdsClient::State ritual_ZNK15QOpcUaGdsClient5stateEv(
    const QOpcUaGdsClient *self) {
  return self->state();
}

//  void QOpcUaGdsClient::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient5startEv(QOpcUaGdsClient *self) {
  self->start();
}

//  void QOpcUaGdsClient::unregisterApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient21unregisterApplicationEv(
    QOpcUaGdsClient *self) {
  self->unregisterApplication();
}

//  void QOpcUaGdsClient::stateChanged(State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient12stateChangedENS_5StateE(
    QOpcUaGdsClient *self,
    QOpcUaGdsClient::State state) {
  self->stateChanged(state);
}

//  void QOpcUaGdsClient::errorChanged(Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient12errorChangedENS_5ErrorE(
    QOpcUaGdsClient *self,
    QOpcUaGdsClient::Error error) {
  self->errorChanged(error);
}

//  void QOpcUaGdsClient::applicationRegistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient21applicationRegisteredEv(
    QOpcUaGdsClient *self) {
  self->applicationRegistered();
}

//  void QOpcUaGdsClient::certificateGroupsReceived(QStringList
//      certificateGroups)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient25certificateGroupsReceivedE5QListI7QStringE(
    QOpcUaGdsClient *self,
    const QList<QString> *certificateGroups) {
  self->certificateGroupsReceived(*certificateGroups);
}

//  void QOpcUaGdsClient::certificateUpdateRequired()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient25certificateUpdateRequiredEv(
    QOpcUaGdsClient *self) {
  self->certificateUpdateRequired();
}

//  void QOpcUaGdsClient::certificateUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient18certificateUpdatedEv(
    QOpcUaGdsClient *self) {
  self->certificateUpdated();
}

//  void QOpcUaGdsClient::unregistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient12unregisteredEv(QOpcUaGdsClient *self) {
  self->unregistered();
}

//  void QOpcUaGdsClient::trustListUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient16trustListUpdatedEv(QOpcUaGdsClient *self) {
  self->trustListUpdated();
}

//  void
//      QOpcUaGdsClient::authenticationRequired(QOpcUaAuthenticationInformati
//      on &authInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaGdsClient22authenticationRequiredER31QOpcUaAuthenticationInformation(
    QOpcUaGdsClient *self,
    QOpcUaAuthenticationInformation *authInfo) {
  self->authenticationRequired(*authInfo);
}

//  a Python function taken by a CuteQOpcUaGdsClient, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaGdsClient(
    QOpcUaGdsClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaGdsClient *>(self)->take(key, call);
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
