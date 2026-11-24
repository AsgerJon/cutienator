//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaexpandednodeid.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId()
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZN20QOpcUaExpandedNodeIdC1Ev() {
  return new QOpcUaExpandedNodeId();
}

//  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QOpcUaExpandedNodeId
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZN20QOpcUaExpandedNodeIdC1ERKS_(
    const QOpcUaExpandedNodeId *a0) {
  return new QOpcUaExpandedNodeId(*a0);
}

//  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZN20QOpcUaExpandedNodeIdC1ERK7QString(
    const QString *nodeId) {
  return new QOpcUaExpandedNodeId(*nodeId);
}

//  QOpcUaExpandedNodeId::QOpcUaExpandedNodeId(const QString &namespaceUri,
//      const QString &nodeId, quint32 serverIndex)
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZN20QOpcUaExpandedNodeIdC1ERK7QStringS2_j(
    const QString *namespaceUri,
    const QString *nodeId,
    quint32 serverIndex) {
  return new QOpcUaExpandedNodeId(*namespaceUri, *nodeId, serverIndex);
}

//  bool QOpcUaExpandedNodeId::operator==(const QOpcUaExpandedNodeId &a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaExpandedNodeIdeqERKS_(
    const QOpcUaExpandedNodeId *self,
    const QOpcUaExpandedNodeId *a0) {
  return self->operator==(*a0);
}

//  QVariant QOpcUaExpandedNodeId::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaExpandedNodeIdcv8QVariantEv(
    const QOpcUaExpandedNodeId *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaExpandedNodeId::~QOpcUaExpandedNodeId()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaExpandedNodeIdD1Ev(QOpcUaExpandedNodeId *self) {
  delete self;
}

//  quint32 QOpcUaExpandedNodeId::serverIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QOpcUaExpandedNodeId11serverIndexEv(
    const QOpcUaExpandedNodeId *self) {
  return self->serverIndex();
}

//  void QOpcUaExpandedNodeId::setServerIndex(quint32 serverIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaExpandedNodeId14setServerIndexEj(
    QOpcUaExpandedNodeId *self,
    quint32 serverIndex) {
  self->setServerIndex(serverIndex);
}

//  QString QOpcUaExpandedNodeId::namespaceUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpcUaExpandedNodeId12namespaceUriEv(
    const QOpcUaExpandedNodeId *self) {
  return new QString(self->namespaceUri());
}

//  void QOpcUaExpandedNodeId::setNamespaceUri(const QString &namespaceUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaExpandedNodeId15setNamespaceUriERK7QString(
    QOpcUaExpandedNodeId *self,
    const QString *namespaceUri) {
  self->setNamespaceUri(*namespaceUri);
}

//  QString QOpcUaExpandedNodeId::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpcUaExpandedNodeId6nodeIdEv(
    const QOpcUaExpandedNodeId *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaExpandedNodeId::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaExpandedNodeId9setNodeIdERK7QString(
    QOpcUaExpandedNodeId *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}
