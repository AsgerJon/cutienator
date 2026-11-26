//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuabackend_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuabackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtOpcUa/qopcuareadresult.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtOpcUa/qopcuareferencedescription.h>
#include <QtOpcUa/qopcuabrowsepathtarget.h>
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtCore/qurl.h>
#include <QtOpcUa/qopcuaapplicationdescription.h>
#include <QtOpcUa/qopcuawriteresult.h>
#include <QtOpcUa/qopcuahistoryreadrawrequest.h>
#include <QtOpcUa/qopcuahistorydata.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtCore/qbytearray.h>
#include <QtOpcUa/qopcuahistoryevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaBackend that Python can take functions over in. Every QOpcUaBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaBackendCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaBackendCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaBackend : public QOpcUaBackend {
public:
  using QOpcUaBackend::QOpcUaBackend;
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
      CuteQOpcUaBackendCall0 call = reinterpret_cast<CuteQOpcUaBackendCall0>(taken[0]);
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
      CuteQOpcUaBackendCall1 call = reinterpret_cast<CuteQOpcUaBackendCall1>(taken[1]);
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
      CuteQOpcUaBackendCall2 call = reinterpret_cast<CuteQOpcUaBackendCall2>(taken[2]);
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
      CuteQOpcUaBackendCall3 call = reinterpret_cast<CuteQOpcUaBackendCall3>(taken[3]);
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
      CuteQOpcUaBackendCall4 call = reinterpret_cast<CuteQOpcUaBackendCall4>(taken[4]);
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
      CuteQOpcUaBackendCall5 call = reinterpret_cast<CuteQOpcUaBackendCall5>(taken[5]);
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
      CuteQOpcUaBackendCall6 call = reinterpret_cast<CuteQOpcUaBackendCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpcUaBackend10metaObjectEv(
    const QOpcUaBackend *self) {
  return self->metaObject();
}

//  void *QOpcUaBackend::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QOpcUaBackend11qt_metacastEPKc(
    QOpcUaBackend *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaBackend::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QOpcUaBackend11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaBackend *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaBackend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpcUaBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaBackend::tr(s, c, n));
}

//  QOpcUaBackend::QOpcUaBackend()
extern "C" Q_DECL_EXPORT
QOpcUaBackend *ritual_ZN13QOpcUaBackendC1Ev() {
  return new CuteQOpcUaBackend();
}

//  QOpcUaBackend::~QOpcUaBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackendD1Ev(QOpcUaBackend *self) {
  delete self;
}

//  size_t QOpcUaBackend::nodeAttributeEnumBits()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QOpcUaBackend21nodeAttributeEnumBitsEv() {
  return QOpcUaBackend::nodeAttributeEnumBits();
}

//  QOpcUa::Types QOpcUaBackend::attributeIdToTypeId(QOpcUa::NodeAttribute
//      attr)
extern "C" Q_DECL_EXPORT
QOpcUa::Types ritual_ZN13QOpcUaBackend19attributeIdToTypeIdEN6QOpcUa13NodeAttributeE(
    QOpcUaBackend *self,
    QOpcUa::NodeAttribute attr) {
  return self->attributeIdToTypeId(attr);
}

//  double QOpcUaBackend::revisePublishingInterval(double requestedValue,
//      double minimumValue)
extern "C" Q_DECL_EXPORT
double ritual_ZN13QOpcUaBackend24revisePublishingIntervalEdd(
    QOpcUaBackend *self,
    double requestedValue,
    double minimumValue) {
  return self->revisePublishingInterval(requestedValue, minimumValue);
}

//  QOpcUaClient::ClientError QOpcUaBackend::verifyEndpointDescription(const
//      QOpcUaEndpointDescription &endpoint, QString *message)
extern "C" Q_DECL_EXPORT
QOpcUaClient::ClientError ritual_ZN13QOpcUaBackend25verifyEndpointDescriptionERK25QOpcUaEndpointDescriptionP7QString(
    const QOpcUaEndpointDescription *endpoint,
    QString *message) {
  return QOpcUaBackend::verifyEndpointDescription(*endpoint, message);
}

//  void QOpcUaBackend::stateAndOrErrorChanged(QOpcUaClient::ClientState
//      state, QOpcUaClient::ClientError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend22stateAndOrErrorChangedEN12QOpcUaClient11ClientStateENS0_11ClientErrorE(
    QOpcUaBackend *self,
    QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error) {
  self->stateAndOrErrorChanged(state, error);
}

//  void QOpcUaBackend::attributesRead(quint64 handle,
//      QList<QOpcUaReadResult> attributes, QOpcUa::UaStatusCode
//      serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend14attributesReadEy5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    const QList<QOpcUaReadResult> *attributes,
    QOpcUa::UaStatusCode serviceResult) {
  self->attributesRead(handle, *attributes, serviceResult);
}

//  void QOpcUaBackend::attributeWritten(quint64 handle,
//      QOpcUa::NodeAttribute attribute, QVariant value, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend16attributeWrittenEyN6QOpcUa13NodeAttributeE8QVariantNS0_12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    QOpcUa::NodeAttribute attribute,
    const QVariant *value,
    QOpcUa::UaStatusCode statusCode) {
  self->attributeWritten(handle, attribute, *value, statusCode);
}

//  void QOpcUaBackend::methodCallFinished(quint64 handle, QString
//      methodNodeId, QVariant result, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend18methodCallFinishedEy7QString8QVariantN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    const QString *methodNodeId,
    const QVariant *result,
    QOpcUa::UaStatusCode statusCode) {
  self->methodCallFinished(handle, *methodNodeId, *result, statusCode);
}

//  void QOpcUaBackend::dataChangeOccurred(quint64 handle, QOpcUaReadResult
//      res)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend18dataChangeOccurredEy16QOpcUaReadResult(
    QOpcUaBackend *self,
    quint64 handle,
    const QOpcUaReadResult *res) {
  self->dataChangeOccurred(handle, *res);
}

//  void QOpcUaBackend::eventOccurred(quint64 handle, QVariantList fields)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend13eventOccurredEy5QListI8QVariantE(
    QOpcUaBackend *self,
    quint64 handle,
    const QList<QVariant> *fields) {
  self->eventOccurred(handle, *fields);
}

//  void QOpcUaBackend::monitoringEnableDisable(quint64 handle,
//      QOpcUa::NodeAttribute attr, bool subscribe,
//      QOpcUaMonitoringParameters status)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend23monitoringEnableDisableEyN6QOpcUa13NodeAttributeEb26QOpcUaMonitoringParameters(
    QOpcUaBackend *self,
    quint64 handle,
    QOpcUa::NodeAttribute attr,
    bool subscribe,
    const QOpcUaMonitoringParameters *status) {
  self->monitoringEnableDisable(handle, attr, subscribe, *status);
}

//  void QOpcUaBackend::monitoringStatusChanged(quint64 handle,
//      QOpcUa::NodeAttribute attr, QOpcUaMonitoringParameters::Parameters
//      items, QOpcUaMonitoringParameters param)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend23monitoringStatusChangedEyN6QOpcUa13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEES3_(
    QOpcUaBackend *self,
    quint64 handle,
    QOpcUa::NodeAttribute attr,
    int items,
    const QOpcUaMonitoringParameters *param) {
  self->monitoringStatusChanged(
      handle,
      attr,
      QFlags<QOpcUaMonitoringParameters::Parameter>::fromInt(items),
      *param);
}

//  void QOpcUaBackend::browseFinished(quint64 handle,
//      QList<QOpcUaReferenceDescription> children, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend14browseFinishedEy5QListI26QOpcUaReferenceDescriptionEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    const QList<QOpcUaReferenceDescription> *children,
    QOpcUa::UaStatusCode statusCode) {
  self->browseFinished(handle, *children, statusCode);
}

//  void QOpcUaBackend::resolveBrowsePathFinished(quint64 handle, const
//      QList<QOpcUaBrowsePathTarget> &targets, const
//      QList<QOpcUaRelativePathElement> &path, QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend25resolveBrowsePathFinishedEyRK5QListI22QOpcUaBrowsePathTargetERKS0_I25QOpcUaRelativePathElementEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    const QList<QOpcUaBrowsePathTarget> *targets,
    const QList<QOpcUaRelativePathElement> *path,
    QOpcUa::UaStatusCode statusCode) {
  self->resolveBrowsePathFinished(handle, *targets, *path, statusCode);
}

//  void
//      QOpcUaBackend::endpointsRequestFinished(QList<QOpcUaEndpointDescripti
//      on> endpoints, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend24endpointsRequestFinishedE5QListI25QOpcUaEndpointDescriptionEN6QOpcUa12UaStatusCodeE4QUrl(
    QOpcUaBackend *self,
    const QList<QOpcUaEndpointDescription> *endpoints,
    QOpcUa::UaStatusCode statusCode,
    const QUrl *requestUrl) {
  self->endpointsRequestFinished(*endpoints, statusCode, *requestUrl);
}

//  void
//      QOpcUaBackend::findServersFinished(QList<QOpcUaApplicationDescription
//      > servers, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend19findServersFinishedE5QListI28QOpcUaApplicationDescriptionEN6QOpcUa12UaStatusCodeE4QUrl(
    QOpcUaBackend *self,
    const QList<QOpcUaApplicationDescription> *servers,
    QOpcUa::UaStatusCode statusCode,
    const QUrl *requestUrl) {
  self->findServersFinished(*servers, statusCode, *requestUrl);
}

//  void QOpcUaBackend::readNodeAttributesFinished(QList<QOpcUaReadResult>
//      results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend26readNodeAttributesFinishedE5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QList<QOpcUaReadResult> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readNodeAttributesFinished(*results, serviceResult);
}

//  void QOpcUaBackend::writeNodeAttributesFinished(QList<QOpcUaWriteResult>
//      results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend27writeNodeAttributesFinishedE5QListI17QOpcUaWriteResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QList<QOpcUaWriteResult> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->writeNodeAttributesFinished(*results, serviceResult);
}

//  void QOpcUaBackend::readHistoryDataFinished(quint64 handle, bool
//      isHandleValid, QOpcUaHistoryReadRawRequest request,
//      QList<QOpcUaHistoryData> results, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend23readHistoryDataFinishedEyb27QOpcUaHistoryReadRawRequest5QListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    quint64 handle,
    bool isHandleValid,
    const QOpcUaHistoryReadRawRequest *request,
    const QList<QOpcUaHistoryData> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readHistoryDataFinished(
      handle,
      isHandleValid,
      *request,
      *results,
      serviceResult);
}

//  void QOpcUaBackend::addNodeFinished(QOpcUaExpandedNodeId requestedNodeId,
//      QString assignedNodeId, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend15addNodeFinishedE20QOpcUaExpandedNodeId7QStringN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QOpcUaExpandedNodeId *requestedNodeId,
    const QString *assignedNodeId,
    QOpcUa::UaStatusCode statusCode) {
  self->addNodeFinished(*requestedNodeId, *assignedNodeId, statusCode);
}

//  void QOpcUaBackend::deleteNodeFinished(QString nodeId,
//      QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend18deleteNodeFinishedE7QStringN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QString *nodeId,
    QOpcUa::UaStatusCode statusCode) {
  self->deleteNodeFinished(*nodeId, statusCode);
}

//  void QOpcUaBackend::addReferenceFinished(QString sourceNodeId, QString
//      referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
//      isForwardReference, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend20addReferenceFinishedE7QStringS0_20QOpcUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
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

//  void QOpcUaBackend::deleteReferenceFinished(QString sourceNodeId, QString
//      referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
//      isForwardReference, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend23deleteReferenceFinishedE7QStringS0_20QOpcUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
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

//  void QOpcUaBackend::connectError(QOpcUaErrorState *errorState)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend12connectErrorEP16QOpcUaErrorState(
    QOpcUaBackend *self,
    QOpcUaErrorState *errorState) {
  self->connectError(errorState);
}

//  void QOpcUaBackend::passwordForPrivateKeyRequired(QString keyFilePath,
//      QString *password, bool previousTryWasInvalid)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend29passwordForPrivateKeyRequiredE7QStringPS0_b(
    QOpcUaBackend *self,
    const QString *keyFilePath,
    QString *password,
    bool previousTryWasInvalid) {
  self->passwordForPrivateKeyRequired(
      *keyFilePath,
      password,
      previousTryWasInvalid);
}

//  void QOpcUaBackend::historyDataAvailable(QList<QOpcUaHistoryData> data,
//      QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode
//      serviceResult, uintptr_t handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend20historyDataAvailableE5QListI17QOpcUaHistoryDataES0_I10QByteArrayEN6QOpcUa12UaStatusCodeEm(
    QOpcUaBackend *self,
    const QList<QOpcUaHistoryData> *data,
    const QList<QByteArray> *continuationPoints,
    QOpcUa::UaStatusCode serviceResult,
    unsigned long long handle) {
  self->historyDataAvailable(
      *data,
      *continuationPoints,
      serviceResult,
      handle);
}

//  void QOpcUaBackend::historyEventsAvailable(QList<QOpcUaHistoryEvent>
//      data, QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode
//      serviceResult, uintptr_t handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend22historyEventsAvailableE5QListI18QOpcUaHistoryEventES0_I10QByteArrayEN6QOpcUa12UaStatusCodeEm(
    QOpcUaBackend *self,
    const QList<QOpcUaHistoryEvent> *data,
    const QList<QByteArray> *continuationPoints,
    QOpcUa::UaStatusCode serviceResult,
    unsigned long long handle) {
  self->historyEventsAvailable(
      *data,
      *continuationPoints,
      serviceResult,
      handle);
}

//  void QOpcUaBackend::registerNodesFinished(QStringList nodesToRegister,
//      QStringList registeredNodeIds, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend21registerNodesFinishedE5QListI7QStringES2_N6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QList<QString> *nodesToRegister,
    const QList<QString> *registeredNodeIds,
    QOpcUa::UaStatusCode statusCode) {
  self->registerNodesFinished(
      *nodesToRegister,
      *registeredNodeIds,
      statusCode);
}

//  void QOpcUaBackend::unregisterNodesFinished(QStringList
//      nodesToUnregister, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackend23unregisterNodesFinishedE5QListI7QStringEN6QOpcUa12UaStatusCodeE(
    QOpcUaBackend *self,
    const QList<QString> *nodesToUnregister,
    QOpcUa::UaStatusCode statusCode) {
  self->unregisterNodesFinished(*nodesToUnregister, statusCode);
}

//  a Python function taken by a CuteQOpcUaBackend, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaBackend(
    QOpcUaBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaBackend *>(self)->take(key, call);
}
