//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclientimpl_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclientimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtCore/qurl.h>
#include <QtOpcUa/qopcuareaditem.h>
#include <QtOpcUa/qopcuawriteitem.h>
#include <QtOpcUa/qopcuahistoryreadrawrequest.h>
#include <QtOpcUa/qopcuahistoryreadeventrequest.h>
#include <QtOpcUa/qopcuaaddnodeitem.h>
#include <QtOpcUa/qopcuaaddreferenceitem.h>
#include <QtOpcUa/qopcuadeletereferenceitem.h>
#include <QtOpcUa/qopcuareadresult.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtOpcUa/qopcuareferencedescription.h>
#include <QtOpcUa/qopcuabrowsepathtarget.h>
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtOpcUa/qopcuaapplicationdescription.h>
#include <QtOpcUa/qopcuawriteresult.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtOpcUa/qopcuaconnectionsettings.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QPointer>
#include <QtCore/QList>
#include <QtOpcUa/QOpcUaUserTokenPolicy>

//  A QOpcUaClientImpl that Python can take functions over in. Every QOpcUaClientImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpcUaClientImplCall0)(const void *, const QOpcUaEndpointDescription *, int *);
typedef void (*CuteQOpcUaClientImplCall1)(const void *, int *);
typedef void * (*CuteQOpcUaClientImplCall2)(const void *, const QString *, int *);
typedef QString * (*CuteQOpcUaClientImplCall3)(const void *, int *);
typedef bool (*CuteQOpcUaClientImplCall4)(const void *, const QUrl *, int *);
typedef void * (*CuteQOpcUaClientImplCall5)(const void *, const QOpcUaHistoryReadRawRequest *, int *);
typedef void * (*CuteQOpcUaClientImplCall6)(const void *, const QOpcUaHistoryReadEventRequest *, int *);
typedef bool (*CuteQOpcUaClientImplCall7)(const void *, const QOpcUaAddNodeItem *, int *);
typedef bool (*CuteQOpcUaClientImplCall8)(const void *, const QString *, bool, int *);
typedef bool (*CuteQOpcUaClientImplCall9)(const void *, const QOpcUaAddReferenceItem *, int *);
typedef bool (*CuteQOpcUaClientImplCall10)(const void *, const QOpcUaDeleteReferenceItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaClientImplCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaClientImplCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientImplCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientImplCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientImplCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientImplCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaClientImplCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaClientImpl : public QOpcUaClientImpl {
public:
  using QOpcUaClientImpl::QOpcUaClientImpl;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl17connectToEndpointERK25QOpcUaEndpointDescription")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl22disconnectFromEndpointEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl4nodeERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QOpcUaClientImpl7backendEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl16requestEndpointsERK4QUrl")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl15readHistoryDataERK27QOpcUaHistoryReadRawRequest")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl17readHistoryEventsERK29QOpcUaHistoryReadEventRequest")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl7addNodeERK17QOpcUaAddNodeItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl10deleteNodeERK7QStringb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl12addReferenceERK22QOpcUaAddReferenceItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QOpcUaClientImpl15deleteReferenceERK25QOpcUaDeleteReferenceItem")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QOpcUaClientImpl::connectToEndpoint(const
  //      QOpcUaEndpointDescription &endpoint)
  void connectToEndpoint(
      const QOpcUaEndpointDescription &endpoint) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpcUaClientImplCall0 call = reinterpret_cast<CuteQOpcUaClientImplCall0>(taken[0]);
      call(this, &endpoint, &handled);
      if (handled) return;
    }
  }

  //  void QOpcUaClientImpl::disconnectFromEndpoint()
  void disconnectFromEndpoint() override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpcUaClientImplCall1 call = reinterpret_cast<CuteQOpcUaClientImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QOpcUaNode *QOpcUaClientImpl::node(const QString &nodeId)
  QOpcUaNode *node(const QString &nodeId) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpcUaClientImplCall2 call = reinterpret_cast<CuteQOpcUaClientImplCall2>(taken[2]);
      void * given = call(this, &nodeId, &handled);
      if (handled) return static_cast<QOpcUaNode *>(given);
    }
    return {};
  }

  //  QString QOpcUaClientImpl::backend() const
  QString backend() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpcUaClientImplCall3 call = reinterpret_cast<CuteQOpcUaClientImplCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QOpcUaClientImpl::requestEndpoints(const QUrl &url)
  bool requestEndpoints(const QUrl &url) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpcUaClientImplCall4 call = reinterpret_cast<CuteQOpcUaClientImplCall4>(taken[4]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryData(const
  //      QOpcUaHistoryReadRawRequest &request)
  QOpcUaHistoryReadResponse *readHistoryData(
      const QOpcUaHistoryReadRawRequest &request) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpcUaClientImplCall5 call = reinterpret_cast<CuteQOpcUaClientImplCall5>(taken[5]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QOpcUaHistoryReadResponse *>(given);
    }
    return {};
  }

  //  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryEvents(const
  //      QOpcUaHistoryReadEventRequest &request)
  QOpcUaHistoryReadResponse *readHistoryEvents(
      const QOpcUaHistoryReadEventRequest &request) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpcUaClientImplCall6 call = reinterpret_cast<CuteQOpcUaClientImplCall6>(taken[6]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QOpcUaHistoryReadResponse *>(given);
    }
    return {};
  }

  //  bool QOpcUaClientImpl::addNode(const QOpcUaAddNodeItem &nodeToAdd)
  bool addNode(const QOpcUaAddNodeItem &nodeToAdd) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpcUaClientImplCall7 call = reinterpret_cast<CuteQOpcUaClientImplCall7>(taken[7]);
      bool given = call(this, &nodeToAdd, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaClientImpl::deleteNode(const QString &nodeId, bool
  //      deleteTargetReferences)
  bool deleteNode(
      const QString &nodeId,
      bool deleteTargetReferences) override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpcUaClientImplCall8 call = reinterpret_cast<CuteQOpcUaClientImplCall8>(taken[8]);
      bool given = call(this, &nodeId, deleteTargetReferences, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaClientImpl::addReference(const QOpcUaAddReferenceItem
  //      &referenceToAdd)
  bool addReference(const QOpcUaAddReferenceItem &referenceToAdd) override {
    if (taken[9]) {
      int handled = 0;
      CuteQOpcUaClientImplCall9 call = reinterpret_cast<CuteQOpcUaClientImplCall9>(taken[9]);
      bool given = call(this, &referenceToAdd, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QOpcUaClientImpl::deleteReference(const
  //      QOpcUaDeleteReferenceItem &referenceToDelete)
  bool deleteReference(
      const QOpcUaDeleteReferenceItem &referenceToDelete) override {
    if (taken[10]) {
      int handled = 0;
      CuteQOpcUaClientImplCall10 call = reinterpret_cast<CuteQOpcUaClientImplCall10>(taken[10]);
      bool given = call(this, &referenceToDelete, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQOpcUaClientImplCall11 call = reinterpret_cast<CuteQOpcUaClientImplCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQOpcUaClientImplCall12 call = reinterpret_cast<CuteQOpcUaClientImplCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQOpcUaClientImplCall13 call = reinterpret_cast<CuteQOpcUaClientImplCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQOpcUaClientImplCall14 call = reinterpret_cast<CuteQOpcUaClientImplCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQOpcUaClientImplCall15 call = reinterpret_cast<CuteQOpcUaClientImplCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQOpcUaClientImplCall16 call = reinterpret_cast<CuteQOpcUaClientImplCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQOpcUaClientImplCall17 call = reinterpret_cast<CuteQOpcUaClientImplCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaClientImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QOpcUaClientImpl10metaObjectEv(
    const QOpcUaClientImpl *self) {
  return self->metaObject();
}

//  void *QOpcUaClientImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QOpcUaClientImpl11qt_metacastEPKc(
    QOpcUaClientImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaClientImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QOpcUaClientImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaClientImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaClientImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QOpcUaClientImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaClientImpl::tr(s, c, n));
}

//  QOpcUaClientImpl::~QOpcUaClientImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImplD1Ev(QOpcUaClientImpl *self) {
  delete self;
}

//  void QOpcUaClientImpl::connectToEndpoint(const QOpcUaEndpointDescription
//      &endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl17connectToEndpointERK25QOpcUaEndpointDescription(
    QOpcUaClientImpl *self,
    const QOpcUaEndpointDescription *endpoint) {
  self->connectToEndpoint(*endpoint);
}

//  void QOpcUaClientImpl::disconnectFromEndpoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl22disconnectFromEndpointEv(
    QOpcUaClientImpl *self) {
  self->disconnectFromEndpoint();
}

//  QOpcUaNode *QOpcUaClientImpl::node(const QString &nodeId)
extern "C" Q_DECL_EXPORT
QOpcUaNode *ritual_ZN16QOpcUaClientImpl4nodeERK7QString(
    QOpcUaClientImpl *self,
    const QString *nodeId) {
  return self->node(*nodeId);
}

//  QString QOpcUaClientImpl::backend() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QOpcUaClientImpl7backendEv(
    const QOpcUaClientImpl *self) {
  return new QString(self->backend());
}

//  bool QOpcUaClientImpl::requestEndpoints(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl16requestEndpointsERK4QUrl(
    QOpcUaClientImpl *self,
    const QUrl *url) {
  return self->requestEndpoints(*url);
}

//  bool QOpcUaClientImpl::findServers(const QUrl &url, const QStringList
//      &localeIds, const QStringList &serverUris)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl11findServersERK4QUrlRK5QListI7QStringES7_(
    QOpcUaClientImpl *self,
    const QUrl *url,
    const QList<QString> *localeIds,
    const QList<QString> *serverUris) {
  return self->findServers(*url, *localeIds, *serverUris);
}

//  bool QOpcUaClientImpl::readNodeAttributes(const QList<QOpcUaReadItem>
//      &nodesToRead)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl18readNodeAttributesERK5QListI14QOpcUaReadItemE(
    QOpcUaClientImpl *self,
    const QList<QOpcUaReadItem> *nodesToRead) {
  return self->readNodeAttributes(*nodesToRead);
}

//  bool QOpcUaClientImpl::writeNodeAttributes(const QList<QOpcUaWriteItem>
//      &nodesToWrite)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl19writeNodeAttributesERK5QListI15QOpcUaWriteItemE(
    QOpcUaClientImpl *self,
    const QList<QOpcUaWriteItem> *nodesToWrite) {
  return self->writeNodeAttributes(*nodesToWrite);
}

//  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryData(const
//      QOpcUaHistoryReadRawRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN16QOpcUaClientImpl15readHistoryDataERK27QOpcUaHistoryReadRawRequest(
    QOpcUaClientImpl *self,
    const QOpcUaHistoryReadRawRequest *request) {
  return self->readHistoryData(*request);
}

//  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryEvents(const
//      QOpcUaHistoryReadEventRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN16QOpcUaClientImpl17readHistoryEventsERK29QOpcUaHistoryReadEventRequest(
    QOpcUaClientImpl *self,
    const QOpcUaHistoryReadEventRequest *request) {
  return self->readHistoryEvents(*request);
}

//  bool QOpcUaClientImpl::registerNode(QPointer<QOpcUaNodeImpl> obj)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl12registerNodeE8QPointerI14QOpcUaNodeImplE(
    QOpcUaClientImpl *self,
    const QPointer<QOpcUaNodeImpl> *obj) {
  return self->registerNode(*obj);
}

//  void QOpcUaClientImpl::unregisterNode(QPointer<QOpcUaNodeImpl> obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl14unregisterNodeE8QPointerI14QOpcUaNodeImplE(
    QOpcUaClientImpl *self,
    const QPointer<QOpcUaNodeImpl> *obj) {
  self->unregisterNode(*obj);
}

//  bool QOpcUaClientImpl::addNode(const QOpcUaAddNodeItem &nodeToAdd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl7addNodeERK17QOpcUaAddNodeItem(
    QOpcUaClientImpl *self,
    const QOpcUaAddNodeItem *nodeToAdd) {
  return self->addNode(*nodeToAdd);
}

//  bool QOpcUaClientImpl::deleteNode(const QString &nodeId, bool
//      deleteTargetReferences)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl10deleteNodeERK7QStringb(
    QOpcUaClientImpl *self,
    const QString *nodeId,
    bool deleteTargetReferences) {
  return self->deleteNode(*nodeId, deleteTargetReferences);
}

//  bool QOpcUaClientImpl::addReference(const QOpcUaAddReferenceItem
//      &referenceToAdd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl12addReferenceERK22QOpcUaAddReferenceItem(
    QOpcUaClientImpl *self,
    const QOpcUaAddReferenceItem *referenceToAdd) {
  return self->addReference(*referenceToAdd);
}

//  bool QOpcUaClientImpl::deleteReference(const QOpcUaDeleteReferenceItem
//      &referenceToDelete)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl15deleteReferenceERK25QOpcUaDeleteReferenceItem(
    QOpcUaClientImpl *self,
    const QOpcUaDeleteReferenceItem *referenceToDelete) {
  return self->deleteReference(*referenceToDelete);
}

//  void QOpcUaClientImpl::connectBackendWithClient(QOpcUaBackend *backend)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl24connectBackendWithClientEP13QOpcUaBackend(
    QOpcUaClientImpl *self,
    QOpcUaBackend *backend) {
  self->connectBackendWithClient(backend);
}

//  QStringList QOpcUaClientImpl::supportedSecurityPolicies() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QOpcUaClientImpl25supportedSecurityPoliciesEv(
    const QOpcUaClientImpl *self) {
  return new QList<QString>(self->supportedSecurityPolicies());
}

//  QList<QOpcUaUserTokenPolicy::TokenType>
//      QOpcUaClientImpl::supportedUserTokenTypes() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaUserTokenPolicy::TokenType> *ritual_ZNK16QOpcUaClientImpl23supportedUserTokenTypesEv(
    const QOpcUaClientImpl *self) {
  return new QList<QOpcUaUserTokenPolicy::TokenType>(
      self->supportedUserTokenTypes());
}

//  bool QOpcUaClientImpl::registerNodes(const QStringList &nodesToRegister)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl13registerNodesERK5QListI7QStringE(
    QOpcUaClientImpl *self,
    const QList<QString> *nodesToRegister) {
  return self->registerNodes(*nodesToRegister);
}

//  bool QOpcUaClientImpl::unregisterNodes(const QStringList
//      &nodesToUnregister)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QOpcUaClientImpl15unregisterNodesERK5QListI7QStringE(
    QOpcUaClientImpl *self,
    const QList<QString> *nodesToUnregister) {
  return self->unregisterNodes(*nodesToUnregister);
}

//  void QOpcUaClientImpl::handleAttributesRead(quint64 handle,
//      QList<QOpcUaReadResult> attr, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl20handleAttributesReadEy5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QList<QOpcUaReadResult> *attr,
    QOpcUa::UaStatusCode serviceResult) {
  self->handleAttributesRead(handle, *attr, serviceResult);
}

//  void QOpcUaClientImpl::handleAttributeWritten(quint64 handle,
//      QOpcUa::NodeAttribute attr, const QVariant &value,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl22handleAttributeWrittenEyN6QOpcUa13NodeAttributeERK8QVariantNS0_12UaStatusCodeE(
    QOpcUaClientImpl *self,
    quint64 handle,
    QOpcUa::NodeAttribute attr,
    const QVariant *value,
    QOpcUa::UaStatusCode statusCode) {
  self->handleAttributeWritten(handle, attr, *value, statusCode);
}

//  void QOpcUaClientImpl::handleDataChangeOccurred(quint64 handle, const
//      QOpcUaReadResult &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl24handleDataChangeOccurredEyRK16QOpcUaReadResult(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QOpcUaReadResult *value) {
  self->handleDataChangeOccurred(handle, *value);
}

//  void QOpcUaClientImpl::handleMonitoringEnableDisable(quint64 handle,
//      QOpcUa::NodeAttribute attr, bool subscribe,
//      QOpcUaMonitoringParameters status)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl29handleMonitoringEnableDisableEyN6QOpcUa13NodeAttributeEb26QOpcUaMonitoringParameters(
    QOpcUaClientImpl *self,
    quint64 handle,
    QOpcUa::NodeAttribute attr,
    bool subscribe,
    const QOpcUaMonitoringParameters *status) {
  self->handleMonitoringEnableDisable(handle, attr, subscribe, *status);
}

//  void QOpcUaClientImpl::handleMonitoringStatusChanged(quint64 handle,
//      QOpcUa::NodeAttribute attr, QOpcUaMonitoringParameters::Parameters
//      items, QOpcUaMonitoringParameters param)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl29handleMonitoringStatusChangedEyN6QOpcUa13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEES3_(
    QOpcUaClientImpl *self,
    quint64 handle,
    QOpcUa::NodeAttribute attr,
    int items,
    const QOpcUaMonitoringParameters *param) {
  self->handleMonitoringStatusChanged(
      handle,
      attr,
      QFlags<QOpcUaMonitoringParameters::Parameter>::fromInt(items),
      *param);
}

//  void QOpcUaClientImpl::handleMethodCallFinished(quint64 handle, QString
//      methodNodeId, QVariant result, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl24handleMethodCallFinishedEy7QString8QVariantN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QString *methodNodeId,
    const QVariant *result,
    QOpcUa::UaStatusCode statusCode) {
  self->handleMethodCallFinished(handle, *methodNodeId, *result, statusCode);
}

//  void QOpcUaClientImpl::handleBrowseFinished(quint64 handle, const
//      QList<QOpcUaReferenceDescription> &children, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl20handleBrowseFinishedEyRK5QListI26QOpcUaReferenceDescriptionEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QList<QOpcUaReferenceDescription> *children,
    QOpcUa::UaStatusCode statusCode) {
  self->handleBrowseFinished(handle, *children, statusCode);
}

//  void QOpcUaClientImpl::handleResolveBrowsePathFinished(quint64 handle,
//      QList<QOpcUaBrowsePathTarget> targets,
//      QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl31handleResolveBrowsePathFinishedEy5QListI22QOpcUaBrowsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QList<QOpcUaBrowsePathTarget> *targets,
    const QList<QOpcUaRelativePathElement> *path,
    QOpcUa::UaStatusCode status) {
  self->handleResolveBrowsePathFinished(handle, *targets, *path, status);
}

//  void QOpcUaClientImpl::handleNewEvent(quint64 handle, QVariantList
//      eventFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl14handleNewEventEy5QListI8QVariantE(
    QOpcUaClientImpl *self,
    quint64 handle,
    const QList<QVariant> *eventFields) {
  self->handleNewEvent(handle, *eventFields);
}

//  void QOpcUaClientImpl::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl9connectedEv(QOpcUaClientImpl *self) {
  self->connected();
}

//  void QOpcUaClientImpl::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl12disconnectedEv(QOpcUaClientImpl *self) {
  self->disconnected();
}

//  void QOpcUaClientImpl::stateAndOrErrorChanged(QOpcUaClient::ClientState
//      state, QOpcUaClient::ClientError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl22stateAndOrErrorChangedEN12QOpcUaClient11ClientStateENS0_11ClientErrorE(
    QOpcUaClientImpl *self,
    QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error) {
  self->stateAndOrErrorChanged(state, error);
}

//  void QOpcUaClientImpl::endpointsRequestFinished(QList<QOpcUaEndpointDescr
//      iption> endpoints, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl24endpointsRequestFinishedE5QListI25QOpcUaEndpointDescriptionEN6QOpcUa12UaStatusCodeE4QUrl(
    QOpcUaClientImpl *self,
    const QList<QOpcUaEndpointDescription> *endpoints,
    QOpcUa::UaStatusCode statusCode,
    const QUrl *requestUrl) {
  self->endpointsRequestFinished(*endpoints, statusCode, *requestUrl);
}

//  void
//      QOpcUaClientImpl::findServersFinished(QList<QOpcUaApplicationDescript
//      ion> servers, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl19findServersFinishedE5QListI28QOpcUaApplicationDescriptionEN6QOpcUa12UaStatusCodeE4QUrl(
    QOpcUaClientImpl *self,
    const QList<QOpcUaApplicationDescription> *servers,
    QOpcUa::UaStatusCode statusCode,
    const QUrl *requestUrl) {
  self->findServersFinished(*servers, statusCode, *requestUrl);
}

//  void QOpcUaClientImpl::readNodeAttributesFinished(QList<QOpcUaReadResult>
//      results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl26readNodeAttributesFinishedE5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QList<QOpcUaReadResult> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readNodeAttributesFinished(*results, serviceResult);
}

//  void
//      QOpcUaClientImpl::writeNodeAttributesFinished(QList<QOpcUaWriteResult
//      > results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl27writeNodeAttributesFinishedE5QListI17QOpcUaWriteResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QList<QOpcUaWriteResult> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->writeNodeAttributesFinished(*results, serviceResult);
}

//  void QOpcUaClientImpl::addNodeFinished(QOpcUaExpandedNodeId
//      requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl15addNodeFinishedE20QOpcUaExpandedNodeId7QStringN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QOpcUaExpandedNodeId *requestedNodeId,
    const QString *assignedNodeId,
    QOpcUa::UaStatusCode statusCode) {
  self->addNodeFinished(*requestedNodeId, *assignedNodeId, statusCode);
}

//  void QOpcUaClientImpl::deleteNodeFinished(QString nodeId,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl18deleteNodeFinishedE7QStringN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QString *nodeId,
    QOpcUa::UaStatusCode statusCode) {
  self->deleteNodeFinished(*nodeId, statusCode);
}

//  void QOpcUaClientImpl::addReferenceFinished(QString sourceNodeId, QString
//      referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
//      isForwardReference, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl20addReferenceFinishedE7QStringS0_20QOpcUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QString *sourceNodeId,
    const QString *referenceTypeId,
    const QOpcUaExpandedNodeId *targetNodeId,
    bool isForwardReference,
    QOpcUa::UaStatusCode statusCode) {
  self->addReferenceFinished(
      *sourceNodeId,
      *referenceTypeId,
      *targetNodeId,
      isForwardReference,
      statusCode);
}

//  void QOpcUaClientImpl::deleteReferenceFinished(QString sourceNodeId,
//      QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
//      isForwardReference, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl23deleteReferenceFinishedE7QStringS0_20QOpcUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QString *sourceNodeId,
    const QString *referenceTypeId,
    const QOpcUaExpandedNodeId *targetNodeId,
    bool isForwardReference,
    QOpcUa::UaStatusCode statusCode) {
  self->deleteReferenceFinished(
      *sourceNodeId,
      *referenceTypeId,
      *targetNodeId,
      isForwardReference,
      statusCode);
}

//  void QOpcUaClientImpl::connectError(QOpcUaErrorState *errorState)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl12connectErrorEP16QOpcUaErrorState(
    QOpcUaClientImpl *self,
    QOpcUaErrorState *errorState) {
  self->connectError(errorState);
}

//  void QOpcUaClientImpl::passwordForPrivateKeyRequired(const QString
//      keyFilePath, QString *password, bool previousTryWasInvalid)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl29passwordForPrivateKeyRequiredE7QStringPS0_b(
    QOpcUaClientImpl *self,
    const QString *keyFilePath,
    QString *password,
    bool previousTryWasInvalid) {
  self->passwordForPrivateKeyRequired(
      *keyFilePath,
      password,
      previousTryWasInvalid);
}

//  void QOpcUaClientImpl::registerNodesFinished(QStringList nodesToRegister,
//      QStringList registeredNodeIds, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl21registerNodesFinishedE5QListI7QStringES2_N6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QList<QString> *nodesToRegister,
    const QList<QString> *registeredNodeIds,
    QOpcUa::UaStatusCode statusCode) {
  self->registerNodesFinished(
      *nodesToRegister,
      *registeredNodeIds,
      statusCode);
}

//  void QOpcUaClientImpl::unregisterNodesFinished(QStringList
//      nodesToUnregister, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl23unregisterNodesFinishedE5QListI7QStringEN6QOpcUa12UaStatusCodeE(
    QOpcUaClientImpl *self,
    const QList<QString> *nodesToUnregister,
    QOpcUa::UaStatusCode statusCode) {
  self->unregisterNodesFinished(*nodesToUnregister, statusCode);
}

//  void QOpcUaClientImpl::connectionSettingsChanged(QOpcUaConnectionSettings
//      settings)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaClientImpl25connectionSettingsChangedE24QOpcUaConnectionSettings(
    QOpcUaClientImpl *self,
    const QOpcUaConnectionSettings *settings) {
  self->connectionSettingsChanged(*settings);
}

//  a Python function taken by a CuteQOpcUaClientImpl, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaClientImpl(
    QOpcUaClientImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaClientImpl *>(self)->take(key, call);
}

//  a QList<QOpcUaUserTokenPolicy::TokenType> a ritual of QOpcUaClientImpl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaClientImpl__QList_QOpcUaUserTokenPolicy_TokenType(
    QList<QOpcUaUserTokenPolicy::TokenType> *self) {
  delete self;
}
