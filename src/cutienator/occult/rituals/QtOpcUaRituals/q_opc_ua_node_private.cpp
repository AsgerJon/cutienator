//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanode_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuanode.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuanode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/qopcuareadresult.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtCore/qlist.h>

//  QOpcUaNode *QOpcUaNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpcUaNode *ritual_ZN17QOpcUaNodePrivate6q_funcEv(QOpcUaNodePrivate *self) {
  return self->q_func();
}

//  const QOpcUaNode *QOpcUaNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaNode *ritual_ZNK17QOpcUaNodePrivate6q_funcEv(
    const QOpcUaNodePrivate *self) {
  return self->q_func();
}

//  QOpcUaNodePrivate::QOpcUaNodePrivate(QOpcUaNodeImpl *impl, QOpcUaClient
//      *client)
extern "C" Q_DECL_EXPORT
QOpcUaNodePrivate *ritual_ZN17QOpcUaNodePrivateC1EP14QOpcUaNodeImplP12QOpcUaClient(
    QOpcUaNodeImpl *impl,
    QOpcUaClient *client) {
  return new QOpcUaNodePrivate(impl, client);
}

//  void QOpcUaNodePrivate::createConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivate17createConnectionsEv(
    QOpcUaNodePrivate *self) {
  self->createConnections();
}

//  QOpcUaNodePrivate::~QOpcUaNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivateD1Ev(QOpcUaNodePrivate *self) {
  delete self;
}

//  void QOpcUaNodePrivate::handleAttributesRead(const
//      QList<QOpcUaReadResult> &attr, QOpcUa::UaStatusCode serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivate20handleAttributesReadERK5QListI16QOpcUaReadResultEN6QOpcUa12UaStatusCodeE(
    QOpcUaNodePrivate *self,
    const QList<QOpcUaReadResult> *attr,
    QOpcUa::UaStatusCode serviceResult) {
  self->handleAttributesRead(*attr, serviceResult);
}

//  void QOpcUaNodePrivate::handleAttributesWritten(QOpcUa::NodeAttribute
//      attr, const QVariant &value, QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivate23handleAttributesWrittenEN6QOpcUa13NodeAttributeERK8QVariantNS0_12UaStatusCodeE(
    QOpcUaNodePrivate *self,
    QOpcUa::NodeAttribute attr,
    const QVariant *value,
    QOpcUa::UaStatusCode statusCode) {
  self->handleAttributesWritten(attr, *value, statusCode);
}

//  void
//      QOpcUaNodePrivate::handleMonitoringEnableDisable(QOpcUa::NodeAttribut
//      e attr, bool subscribe, const QOpcUaMonitoringParameters &status)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivate29handleMonitoringEnableDisableEN6QOpcUa13NodeAttributeEbRK26QOpcUaMonitoringParameters(
    QOpcUaNodePrivate *self,
    QOpcUa::NodeAttribute attr,
    bool subscribe,
    const QOpcUaMonitoringParameters *status) {
  self->handleMonitoringEnableDisable(attr, subscribe, *status);
}

//  void
//      QOpcUaNodePrivate::handleMonitoringStatusChange(QOpcUa::NodeAttribute
//      attr, QOpcUaMonitoringParameters::Parameters items, const
//      QOpcUaMonitoringParameters &param)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaNodePrivate28handleMonitoringStatusChangeEN6QOpcUa13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEERKS3_(
    QOpcUaNodePrivate *self,
    QOpcUa::NodeAttribute attr,
    int items,
    const QOpcUaMonitoringParameters *param) {
  self->handleMonitoringStatusChange(
      attr,
      QFlags<QOpcUaMonitoringParameters::Parameter>::fromInt(items),
      *param);
}
