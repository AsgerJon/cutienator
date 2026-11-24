//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaclient.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaclient.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaapplicationidentity.h>
#include <QtOpcUa/qopcuapkiconfiguration.h>
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtCore/qurl.h>
#include <QtOpcUa/qopcuareaditem.h>
#include <QtOpcUa/qopcuawriteitem.h>
#include <QtOpcUa/qopcuaaddnodeitem.h>
#include <QtOpcUa/qopcuaaddreferenceitem.h>
#include <QtOpcUa/qopcuadeletereferenceitem.h>
#include <QtOpcUa/qopcuaauthenticationinformation.h>
#include <QtOpcUa/qopcuaconnectionsettings.h>
#include <QtOpcUa/qopcuahistoryreadrawrequest.h>
#include <QtOpcUa/qopcuahistoryreadeventrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaClient that Python can take functions over in. Every QOpcUaClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaClientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaClientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaClient : public QOpcUaClient {
public:
  using QOpcUaClient::QOpcUaClient;
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
      CuteQOpcUaClientCall0 call = reinterpret_cast<CuteQOpcUaClientCall0>(taken[0]);
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
      CuteQOpcUaClientCall1 call = reinterpret_cast<CuteQOpcUaClientCall1>(taken[1]);
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
      CuteQOpcUaClientCall2 call = reinterpret_cast<CuteQOpcUaClientCall2>(taken[2]);
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
      CuteQOpcUaClientCall3 call = reinterpret_cast<CuteQOpcUaClientCall3>(taken[3]);
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
      CuteQOpcUaClientCall4 call = reinterpret_cast<CuteQOpcUaClientCall4>(taken[4]);
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
      CuteQOpcUaClientCall5 call = reinterpret_cast<CuteQOpcUaClientCall5>(taken[5]);
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
      CuteQOpcUaClientCall6 call = reinterpret_cast<CuteQOpcUaClientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QOpcUaClient10metaObjectEv(
    const QOpcUaClient *self) {
  return self->metaObject();
}

//  QString QOpcUaClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QOpcUaClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaClient::tr(s, c, n));
}

//  QOpcUaClientPrivate *QOpcUaClient::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaClientPrivate *ritual_ZN12QOpcUaClient6d_funcEv(QOpcUaClient *self) {
  return self->d_func();
}

//  const QOpcUaClientPrivate *QOpcUaClient::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaClientPrivate *ritual_ZNK12QOpcUaClient6d_funcEv(
    const QOpcUaClient *self) {
  return self->d_func();
}

//  QOpcUaClient::QOpcUaClient(QOpcUaClientImpl *impl, QObject *parent)
extern "C" Q_DECL_EXPORT
QOpcUaClient *ritual_ZN12QOpcUaClientC1EP16QOpcUaClientImplP7QObject(
    QOpcUaClientImpl *impl,
    QObject *parent) {
  return new CuteQOpcUaClient(impl, parent);
}

//  QOpcUaClient::~QOpcUaClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClientD1Ev(QOpcUaClient *self) {
  delete self;
}

//  void QOpcUaClient::setApplicationIdentity(const QOpcUaApplicationIdentity
//      &identity)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient22setApplicationIdentityERK25QOpcUaApplicationIdentity(
    QOpcUaClient *self,
    const QOpcUaApplicationIdentity *identity) {
  self->setApplicationIdentity(*identity);
}

//  QOpcUaApplicationIdentity QOpcUaClient::applicationIdentity() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZNK12QOpcUaClient19applicationIdentityEv(
    const QOpcUaClient *self) {
  return new QOpcUaApplicationIdentity(self->applicationIdentity());
}

//  void QOpcUaClient::setPkiConfiguration(const QOpcUaPkiConfiguration
//      &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient19setPkiConfigurationERK22QOpcUaPkiConfiguration(
    QOpcUaClient *self,
    const QOpcUaPkiConfiguration *config) {
  self->setPkiConfiguration(*config);
}

//  QOpcUaPkiConfiguration QOpcUaClient::pkiConfiguration() const
extern "C" Q_DECL_EXPORT
QOpcUaPkiConfiguration *ritual_ZNK12QOpcUaClient16pkiConfigurationEv(
    const QOpcUaClient *self) {
  return new QOpcUaPkiConfiguration(self->pkiConfiguration());
}

//  void QOpcUaClient::connectToEndpoint(const QOpcUaEndpointDescription
//      &endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient17connectToEndpointERK25QOpcUaEndpointDescription(
    QOpcUaClient *self,
    const QOpcUaEndpointDescription *endpoint) {
  self->connectToEndpoint(*endpoint);
}

//  void QOpcUaClient::disconnectFromEndpoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient22disconnectFromEndpointEv(QOpcUaClient *self) {
  self->disconnectFromEndpoint();
}

//  QOpcUaNode *QOpcUaClient::node(const QString &nodeId)
extern "C" Q_DECL_EXPORT
QOpcUaNode *ritual_ZN12QOpcUaClient4nodeERK7QString(
    QOpcUaClient *self,
    const QString *nodeId) {
  return self->node(*nodeId);
}

//  QOpcUaNode *QOpcUaClient::node(const QOpcUaExpandedNodeId
//      &expandedNodeId)
extern "C" Q_DECL_EXPORT
QOpcUaNode *ritual_ZN12QOpcUaClient4nodeERK20QOpcUaExpandedNodeId(
    QOpcUaClient *self,
    const QOpcUaExpandedNodeId *expandedNodeId) {
  return self->node(*expandedNodeId);
}

//  bool QOpcUaClient::updateNamespaceArray()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient20updateNamespaceArrayEv(QOpcUaClient *self) {
  return self->updateNamespaceArray();
}

//  QStringList QOpcUaClient::namespaceArray() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QOpcUaClient14namespaceArrayEv(
    const QOpcUaClient *self) {
  return new QList<QString>(self->namespaceArray());
}

//  QString QOpcUaClient::resolveExpandedNodeId(const QOpcUaExpandedNodeId
//      &expandedNodeId, bool *ok) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QOpcUaClient21resolveExpandedNodeIdERK20QOpcUaExpandedNodeIdPb(
    const QOpcUaClient *self,
    const QOpcUaExpandedNodeId *expandedNodeId,
    bool *ok) {
  return new QString(self->resolveExpandedNodeId(*expandedNodeId, ok));
}

//  QOpcUaQualifiedName QOpcUaClient::qualifiedNameFromNamespaceUri(const
//      QString &namespaceUri, const QString &name, bool *ok) const
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZNK12QOpcUaClient29qualifiedNameFromNamespaceUriERK7QStringS2_Pb(
    const QOpcUaClient *self,
    const QString *namespaceUri,
    const QString *name,
    bool *ok) {
  return new QOpcUaQualifiedName(
      self->qualifiedNameFromNamespaceUri(
          *namespaceUri,
          *name,
          ok));
}

//  bool QOpcUaClient::requestEndpoints(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient16requestEndpointsERK4QUrl(
    QOpcUaClient *self,
    const QUrl *url) {
  return self->requestEndpoints(*url);
}

//  bool QOpcUaClient::findServers(const QUrl &url, const QStringList
//      &localeIds, const QStringList &serverUris)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient11findServersERK4QUrlRK5QListI7QStringES7_(
    QOpcUaClient *self,
    const QUrl *url,
    const QList<QString> *localeIds,
    const QList<QString> *serverUris) {
  return self->findServers(*url, *localeIds, *serverUris);
}

//  bool QOpcUaClient::readNodeAttributes(const QList<QOpcUaReadItem>
//      &nodesToRead)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient18readNodeAttributesERK5QListI14QOpcUaReadItemE(
    QOpcUaClient *self,
    const QList<QOpcUaReadItem> *nodesToRead) {
  return self->readNodeAttributes(*nodesToRead);
}

//  bool QOpcUaClient::writeNodeAttributes(const QList<QOpcUaWriteItem>
//      &nodesToWrite)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient19writeNodeAttributesERK5QListI15QOpcUaWriteItemE(
    QOpcUaClient *self,
    const QList<QOpcUaWriteItem> *nodesToWrite) {
  return self->writeNodeAttributes(*nodesToWrite);
}

//  bool QOpcUaClient::addNode(const QOpcUaAddNodeItem &nodeToAdd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient7addNodeERK17QOpcUaAddNodeItem(
    QOpcUaClient *self,
    const QOpcUaAddNodeItem *nodeToAdd) {
  return self->addNode(*nodeToAdd);
}

//  bool QOpcUaClient::deleteNode(const QString &nodeId, bool
//      deleteTargetReferences)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient10deleteNodeERK7QStringb(
    QOpcUaClient *self,
    const QString *nodeId,
    bool deleteTargetReferences) {
  return self->deleteNode(*nodeId, deleteTargetReferences);
}

//  bool QOpcUaClient::addReference(const QOpcUaAddReferenceItem
//      &referenceToAdd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient12addReferenceERK22QOpcUaAddReferenceItem(
    QOpcUaClient *self,
    const QOpcUaAddReferenceItem *referenceToAdd) {
  return self->addReference(*referenceToAdd);
}

//  bool QOpcUaClient::deleteReference(const QOpcUaDeleteReferenceItem
//      &referenceToDelete)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient15deleteReferenceERK25QOpcUaDeleteReferenceItem(
    QOpcUaClient *self,
    const QOpcUaDeleteReferenceItem *referenceToDelete) {
  return self->deleteReference(*referenceToDelete);
}

//  QOpcUaEndpointDescription QOpcUaClient::endpoint() const
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_ZNK12QOpcUaClient8endpointEv(
    const QOpcUaClient *self) {
  return new QOpcUaEndpointDescription(self->endpoint());
}

//  ClientState QOpcUaClient::state() const
extern "C" Q_DECL_EXPORT
QOpcUaClient::ClientState ritual_ZNK12QOpcUaClient5stateEv(
    const QOpcUaClient *self) {
  return self->state();
}

//  ClientError QOpcUaClient::error() const
extern "C" Q_DECL_EXPORT
QOpcUaClient::ClientError ritual_ZNK12QOpcUaClient5errorEv(
    const QOpcUaClient *self) {
  return self->error();
}

//  QString QOpcUaClient::backend() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QOpcUaClient7backendEv(const QOpcUaClient *self) {
  return new QString(self->backend());
}

//  void QOpcUaClient::setNamespaceAutoupdate(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient22setNamespaceAutoupdateEb(
    QOpcUaClient *self,
    bool isEnabled) {
  self->setNamespaceAutoupdate(isEnabled);
}

//  bool QOpcUaClient::isNamespaceAutoupdateEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QOpcUaClient28isNamespaceAutoupdateEnabledEv(
    const QOpcUaClient *self) {
  return self->isNamespaceAutoupdateEnabled();
}

//  void QOpcUaClient::setNamespaceAutoupdateInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient30setNamespaceAutoupdateIntervalEi(
    QOpcUaClient *self,
    int interval) {
  self->setNamespaceAutoupdateInterval(interval);
}

//  int QOpcUaClient::namespaceAutoupdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QOpcUaClient27namespaceAutoupdateIntervalEv(
    const QOpcUaClient *self) {
  return self->namespaceAutoupdateInterval();
}

//  void QOpcUaClient::setAuthenticationInformation(const
//      QOpcUaAuthenticationInformation &authenticationInformation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient28setAuthenticationInformationERK31QOpcUaAuthenticationInformation(
    QOpcUaClient *self,
    const QOpcUaAuthenticationInformation *authenticationInformation) {
  self->setAuthenticationInformation(*authenticationInformation);
}

//  const QOpcUaAuthenticationInformation
//      &QOpcUaClient::authenticationInformation() const
extern "C" Q_DECL_EXPORT
QOpcUaAuthenticationInformation *ritual_ZNK12QOpcUaClient25authenticationInformationEv(
    const QOpcUaClient *self) {
  return new QOpcUaAuthenticationInformation(
      self->authenticationInformation());
}

//  void QOpcUaClient::setConnectionSettings(const QOpcUaConnectionSettings
//      &connectionSettings)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaClient21setConnectionSettingsERK24QOpcUaConnectionSettings(
    QOpcUaClient *self,
    const QOpcUaConnectionSettings *connectionSettings) {
  self->setConnectionSettings(*connectionSettings);
}

//  QOpcUaConnectionSettings QOpcUaClient::connectionSettings() const
extern "C" Q_DECL_EXPORT
QOpcUaConnectionSettings *ritual_ZNK12QOpcUaClient18connectionSettingsEv(
    const QOpcUaClient *self) {
  return new QOpcUaConnectionSettings(self->connectionSettings());
}

//  QStringList QOpcUaClient::supportedSecurityPolicies() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QOpcUaClient25supportedSecurityPoliciesEv(
    const QOpcUaClient *self) {
  return new QList<QString>(self->supportedSecurityPolicies());
}

//  QOpcUaHistoryReadResponse *QOpcUaClient::readHistoryData(const
//      QOpcUaHistoryReadRawRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN12QOpcUaClient15readHistoryDataERK27QOpcUaHistoryReadRawRequest(
    QOpcUaClient *self,
    const QOpcUaHistoryReadRawRequest *request) {
  return self->readHistoryData(*request);
}

//  QOpcUaHistoryReadResponse *QOpcUaClient::readHistoryEvents(const
//      QOpcUaHistoryReadEventRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN12QOpcUaClient17readHistoryEventsERK29QOpcUaHistoryReadEventRequest(
    QOpcUaClient *self,
    const QOpcUaHistoryReadEventRequest *request) {
  return self->readHistoryEvents(*request);
}

//  bool QOpcUaClient::registerNodes(const QStringList &nodesToRegister)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient13registerNodesERK5QListI7QStringE(
    QOpcUaClient *self,
    const QList<QString> *nodesToRegister) {
  return self->registerNodes(*nodesToRegister);
}

//  bool QOpcUaClient::unregisterNodes(const QStringList &nodesToUnregister)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QOpcUaClient15unregisterNodesERK5QListI7QStringE(
    QOpcUaClient *self,
    const QList<QString> *nodesToUnregister) {
  return self->unregisterNodes(*nodesToUnregister);
}

//  a Python function taken by a CuteQOpcUaClient, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaClient(
    QOpcUaClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaClient *>(self)->take(key, call);
}
