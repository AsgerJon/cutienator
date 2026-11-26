//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaaddreferenceitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaaddreferenceitem.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>

//  QOpcUaAddReferenceItem::QOpcUaAddReferenceItem()
extern "C" Q_DECL_EXPORT
QOpcUaAddReferenceItem *ritual_ZN22QOpcUaAddReferenceItemC1Ev() {
  return new QOpcUaAddReferenceItem();
}

//  QOpcUaAddReferenceItem::QOpcUaAddReferenceItem(const
//      QOpcUaAddReferenceItem &other)
extern "C" Q_DECL_EXPORT
QOpcUaAddReferenceItem *ritual_ZN22QOpcUaAddReferenceItemC1ERKS_(
    const QOpcUaAddReferenceItem *other) {
  return new QOpcUaAddReferenceItem(*other);
}

//  QOpcUaAddReferenceItem &QOpcUaAddReferenceItem::operator=(const
//      QOpcUaAddReferenceItem &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaAddReferenceItem *ritual_ZN22QOpcUaAddReferenceItemaSERKS_(
    QOpcUaAddReferenceItem *self,
    const QOpcUaAddReferenceItem *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaAddReferenceItem::~QOpcUaAddReferenceItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItemD1Ev(QOpcUaAddReferenceItem *self) {
  delete self;
}

//  QString QOpcUaAddReferenceItem::sourceNodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAddReferenceItem12sourceNodeIdEv(
    const QOpcUaAddReferenceItem *self) {
  return new QString(self->sourceNodeId());
}

//  void QOpcUaAddReferenceItem::setSourceNodeId(const QString &sourceNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem15setSourceNodeIdERK7QString(
    QOpcUaAddReferenceItem *self,
    const QString *sourceNodeId) {
  self->setSourceNodeId(*sourceNodeId);
}

//  QString QOpcUaAddReferenceItem::referenceTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAddReferenceItem15referenceTypeIdEv(
    const QOpcUaAddReferenceItem *self) {
  return new QString(self->referenceTypeId());
}

//  void QOpcUaAddReferenceItem::setReferenceTypeId(const QString
//      &referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem18setReferenceTypeIdERK7QString(
    QOpcUaAddReferenceItem *self,
    const QString *referenceTypeId) {
  self->setReferenceTypeId(*referenceTypeId);
}

//  bool QOpcUaAddReferenceItem::isForwardReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QOpcUaAddReferenceItem18isForwardReferenceEv(
    const QOpcUaAddReferenceItem *self) {
  return self->isForwardReference();
}

//  void QOpcUaAddReferenceItem::setIsForwardReference(bool
//      isForwardReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem21setIsForwardReferenceEb(
    QOpcUaAddReferenceItem *self,
    bool isForwardReference) {
  self->setIsForwardReference(isForwardReference);
}

//  QOpcUaExpandedNodeId QOpcUaAddReferenceItem::targetNodeId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK22QOpcUaAddReferenceItem12targetNodeIdEv(
    const QOpcUaAddReferenceItem *self) {
  return new QOpcUaExpandedNodeId(self->targetNodeId());
}

//  void QOpcUaAddReferenceItem::setTargetNodeId(const QOpcUaExpandedNodeId
//      &targetNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem15setTargetNodeIdERK20QOpcUaExpandedNodeId(
    QOpcUaAddReferenceItem *self,
    const QOpcUaExpandedNodeId *targetNodeId) {
  self->setTargetNodeId(*targetNodeId);
}

//  QOpcUa::NodeClass QOpcUaAddReferenceItem::targetNodeClass() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeClass ritual_ZNK22QOpcUaAddReferenceItem15targetNodeClassEv(
    const QOpcUaAddReferenceItem *self) {
  return self->targetNodeClass();
}

//  void QOpcUaAddReferenceItem::setTargetNodeClass(QOpcUa::NodeClass
//      targetNodeClass)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem18setTargetNodeClassEN6QOpcUa9NodeClassE(
    QOpcUaAddReferenceItem *self,
    QOpcUa::NodeClass targetNodeClass) {
  self->setTargetNodeClass(targetNodeClass);
}

//  QString QOpcUaAddReferenceItem::targetServerUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAddReferenceItem15targetServerUriEv(
    const QOpcUaAddReferenceItem *self) {
  return new QString(self->targetServerUri());
}

//  void QOpcUaAddReferenceItem::setTargetServerUri(const QString
//      &targetServerUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAddReferenceItem18setTargetServerUriERK7QString(
    QOpcUaAddReferenceItem *self,
    const QString *targetServerUri) {
  self->setTargetServerUri(*targetServerUri);
}
