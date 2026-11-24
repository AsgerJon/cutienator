//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclient_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaclient.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaapplicationidentity.h>
#include <QtOpcUa/qopcuapkiconfiguration.h>
#include <QtCore/qlist.h>

//  QOpcUaClient *QOpcUaClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpcUaClient *ritual_ZN19QOpcUaClientPrivate6q_funcEv(
    QOpcUaClientPrivate *self) {
  return self->q_func();
}

//  const QOpcUaClient *QOpcUaClientPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaClient *ritual_ZNK19QOpcUaClientPrivate6q_funcEv(
    const QOpcUaClientPrivate *self) {
  return self->q_func();
}

//  QOpcUaClientPrivate::QOpcUaClientPrivate(QOpcUaClientImpl *impl)
extern "C" Q_DECL_EXPORT
QOpcUaClientPrivate *ritual_ZN19QOpcUaClientPrivateC1EP16QOpcUaClientImpl(
    QOpcUaClientImpl *impl) {
  return new QOpcUaClientPrivate(impl);
}

//  QOpcUaClientPrivate::~QOpcUaClientPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivateD1Ev(QOpcUaClientPrivate *self) {
  delete self;
}

//  void QOpcUaClientPrivate::connectToEndpoint(const
//      QOpcUaEndpointDescription &endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate17connectToEndpointERK25QOpcUaEndpointDescription(
    QOpcUaClientPrivate *self,
    const QOpcUaEndpointDescription *endpoint) {
  self->connectToEndpoint(*endpoint);
}

//  void QOpcUaClientPrivate::disconnectFromEndpoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate22disconnectFromEndpointEv(
    QOpcUaClientPrivate *self) {
  self->disconnectFromEndpoint();
}

//  void QOpcUaClientPrivate::setStateAndError(QOpcUaClient::ClientState
//      state, QOpcUaClient::ClientError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate16setStateAndErrorEN12QOpcUaClient11ClientStateENS0_11ClientErrorE(
    QOpcUaClientPrivate *self,
    QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error) {
  self->setStateAndError(state, error);
}

//  bool QOpcUaClientPrivate::updateNamespaceArray()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QOpcUaClientPrivate20updateNamespaceArrayEv(
    QOpcUaClientPrivate *self) {
  return self->updateNamespaceArray();
}

//  QStringList QOpcUaClientPrivate::namespaceArray() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QOpcUaClientPrivate14namespaceArrayEv(
    const QOpcUaClientPrivate *self) {
  return new QList<QString>(self->namespaceArray());
}

//  void QOpcUaClientPrivate::namespaceArrayUpdated(QOpcUa::NodeAttributes
//      attr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate21namespaceArrayUpdatedE6QFlagsIN6QOpcUa13NodeAttributeEE(
    QOpcUaClientPrivate *self,
    int attr) {
  self->namespaceArrayUpdated(QFlags<QOpcUa::NodeAttribute>::fromInt(attr));
}

//  void QOpcUaClientPrivate::setupNamespaceArrayMonitoring()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate29setupNamespaceArrayMonitoringEv(
    QOpcUaClientPrivate *self) {
  self->setupNamespaceArrayMonitoring();
}

//  void QOpcUaClientPrivate::setApplicationIdentity(const
//      QOpcUaApplicationIdentity &identity)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate22setApplicationIdentityERK25QOpcUaApplicationIdentity(
    QOpcUaClientPrivate *self,
    const QOpcUaApplicationIdentity *identity) {
  self->setApplicationIdentity(*identity);
}

//  QOpcUaApplicationIdentity QOpcUaClientPrivate::applicationIdentity()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZNK19QOpcUaClientPrivate19applicationIdentityEv(
    const QOpcUaClientPrivate *self) {
  return new QOpcUaApplicationIdentity(self->applicationIdentity());
}

//  void QOpcUaClientPrivate::setPkiConfiguration(const
//      QOpcUaPkiConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaClientPrivate19setPkiConfigurationERK22QOpcUaPkiConfiguration(
    QOpcUaClientPrivate *self,
    const QOpcUaPkiConfiguration *config) {
  self->setPkiConfiguration(*config);
}

//  QOpcUaPkiConfiguration QOpcUaClientPrivate::pkiConfiguration() const
extern "C" Q_DECL_EXPORT
QOpcUaPkiConfiguration *ritual_ZNK19QOpcUaClientPrivate16pkiConfigurationEv(
    const QOpcUaClientPrivate *self) {
  return new QOpcUaPkiConfiguration(self->pkiConfiguration());
}
