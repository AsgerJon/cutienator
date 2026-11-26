//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuadeletereferenceitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuadeletereferenceitem.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>

//  QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem()
extern "C" Q_DECL_EXPORT
QOpcUaDeleteReferenceItem *ritual_ZN25QOpcUaDeleteReferenceItemC1Ev() {
  return new QOpcUaDeleteReferenceItem();
}

//  QOpcUaDeleteReferenceItem::QOpcUaDeleteReferenceItem(const
//      QOpcUaDeleteReferenceItem &other)
extern "C" Q_DECL_EXPORT
QOpcUaDeleteReferenceItem *ritual_ZN25QOpcUaDeleteReferenceItemC1ERKS_(
    const QOpcUaDeleteReferenceItem *other) {
  return new QOpcUaDeleteReferenceItem(*other);
}

//  QOpcUaDeleteReferenceItem &QOpcUaDeleteReferenceItem::operator=(const
//      QOpcUaDeleteReferenceItem &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaDeleteReferenceItem *ritual_ZN25QOpcUaDeleteReferenceItemaSERKS_(
    QOpcUaDeleteReferenceItem *self,
    const QOpcUaDeleteReferenceItem *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaDeleteReferenceItem::~QOpcUaDeleteReferenceItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItemD1Ev(
    QOpcUaDeleteReferenceItem *self) {
  delete self;
}

//  QString QOpcUaDeleteReferenceItem::sourceNodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaDeleteReferenceItem12sourceNodeIdEv(
    const QOpcUaDeleteReferenceItem *self) {
  return new QString(self->sourceNodeId());
}

//  void QOpcUaDeleteReferenceItem::setSourceNodeId(const QString
//      &sourceNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItem15setSourceNodeIdERK7QString(
    QOpcUaDeleteReferenceItem *self,
    const QString *sourceNodeId) {
  self->setSourceNodeId(*sourceNodeId);
}

//  QString QOpcUaDeleteReferenceItem::referenceTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaDeleteReferenceItem15referenceTypeIdEv(
    const QOpcUaDeleteReferenceItem *self) {
  return new QString(self->referenceTypeId());
}

//  void QOpcUaDeleteReferenceItem::setReferenceTypeId(const QString
//      &referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItem18setReferenceTypeIdERK7QString(
    QOpcUaDeleteReferenceItem *self,
    const QString *referenceTypeId) {
  self->setReferenceTypeId(*referenceTypeId);
}

//  bool QOpcUaDeleteReferenceItem::isForwardReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaDeleteReferenceItem18isForwardReferenceEv(
    const QOpcUaDeleteReferenceItem *self) {
  return self->isForwardReference();
}

//  void QOpcUaDeleteReferenceItem::setIsForwardReference(bool
//      isForwardReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItem21setIsForwardReferenceEb(
    QOpcUaDeleteReferenceItem *self,
    bool isForwardReference) {
  self->setIsForwardReference(isForwardReference);
}

//  QOpcUaExpandedNodeId QOpcUaDeleteReferenceItem::targetNodeId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK25QOpcUaDeleteReferenceItem12targetNodeIdEv(
    const QOpcUaDeleteReferenceItem *self) {
  return new QOpcUaExpandedNodeId(self->targetNodeId());
}

//  void QOpcUaDeleteReferenceItem::setTargetNodeId(const
//      QOpcUaExpandedNodeId &targetNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItem15setTargetNodeIdERK20QOpcUaExpandedNodeId(
    QOpcUaDeleteReferenceItem *self,
    const QOpcUaExpandedNodeId *targetNodeId) {
  self->setTargetNodeId(*targetNodeId);
}

//  bool QOpcUaDeleteReferenceItem::deleteBidirectional() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaDeleteReferenceItem19deleteBidirectionalEv(
    const QOpcUaDeleteReferenceItem *self) {
  return self->deleteBidirectional();
}

//  void QOpcUaDeleteReferenceItem::setDeleteBidirectional(bool
//      deleteBidirectional)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDeleteReferenceItem22setDeleteBidirectionalEb(
    QOpcUaDeleteReferenceItem *self,
    bool deleteBidirectional) {
  self->setDeleteBidirectional(deleteBidirectional);
}
