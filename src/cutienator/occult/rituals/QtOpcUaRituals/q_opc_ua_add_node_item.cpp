//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaaddnodeitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaaddnodeitem.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtOpcUa/qopcuanodecreationattributes.h>

//  QOpcUaAddNodeItem::QOpcUaAddNodeItem()
extern "C" Q_DECL_EXPORT
QOpcUaAddNodeItem *ritual_ZN17QOpcUaAddNodeItemC1Ev() {
  return new QOpcUaAddNodeItem();
}

//  QOpcUaAddNodeItem::QOpcUaAddNodeItem(const QOpcUaAddNodeItem &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAddNodeItem *ritual_ZN17QOpcUaAddNodeItemC1ERKS_(
    const QOpcUaAddNodeItem *a0) {
  return new QOpcUaAddNodeItem(*a0);
}

//  QOpcUaAddNodeItem &QOpcUaAddNodeItem::operator=(const QOpcUaAddNodeItem
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAddNodeItem *ritual_ZN17QOpcUaAddNodeItemaSERKS_(
    QOpcUaAddNodeItem *self,
    const QOpcUaAddNodeItem *a0) {
  return &(self->operator=(*a0));
}

//  QOpcUaAddNodeItem::~QOpcUaAddNodeItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItemD1Ev(QOpcUaAddNodeItem *self) {
  delete self;
}

//  QOpcUaExpandedNodeId QOpcUaAddNodeItem::parentNodeId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK17QOpcUaAddNodeItem12parentNodeIdEv(
    const QOpcUaAddNodeItem *self) {
  return new QOpcUaExpandedNodeId(self->parentNodeId());
}

//  void QOpcUaAddNodeItem::setParentNodeId(const QOpcUaExpandedNodeId
//      &parentNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem15setParentNodeIdERK20QOpcUaExpandedNodeId(
    QOpcUaAddNodeItem *self,
    const QOpcUaExpandedNodeId *parentNodeId) {
  self->setParentNodeId(*parentNodeId);
}

//  QString QOpcUaAddNodeItem::referenceTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QOpcUaAddNodeItem15referenceTypeIdEv(
    const QOpcUaAddNodeItem *self) {
  return new QString(self->referenceTypeId());
}

//  void QOpcUaAddNodeItem::setReferenceTypeId(const QString
//      &referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem18setReferenceTypeIdERK7QString(
    QOpcUaAddNodeItem *self,
    const QString *referenceTypeId) {
  self->setReferenceTypeId(*referenceTypeId);
}

//  QOpcUaExpandedNodeId QOpcUaAddNodeItem::requestedNewNodeId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK17QOpcUaAddNodeItem18requestedNewNodeIdEv(
    const QOpcUaAddNodeItem *self) {
  return new QOpcUaExpandedNodeId(self->requestedNewNodeId());
}

//  void QOpcUaAddNodeItem::setRequestedNewNodeId(const QOpcUaExpandedNodeId
//      &requestedNewNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem21setRequestedNewNodeIdERK20QOpcUaExpandedNodeId(
    QOpcUaAddNodeItem *self,
    const QOpcUaExpandedNodeId *requestedNewNodeId) {
  self->setRequestedNewNodeId(*requestedNewNodeId);
}

//  QOpcUaQualifiedName QOpcUaAddNodeItem::browseName() const
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZNK17QOpcUaAddNodeItem10browseNameEv(
    const QOpcUaAddNodeItem *self) {
  return new QOpcUaQualifiedName(self->browseName());
}

//  void QOpcUaAddNodeItem::setBrowseName(const QOpcUaQualifiedName
//      &browseName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem13setBrowseNameERK19QOpcUaQualifiedName(
    QOpcUaAddNodeItem *self,
    const QOpcUaQualifiedName *browseName) {
  self->setBrowseName(*browseName);
}

//  QOpcUa::NodeClass QOpcUaAddNodeItem::nodeClass() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeClass ritual_ZNK17QOpcUaAddNodeItem9nodeClassEv(
    const QOpcUaAddNodeItem *self) {
  return self->nodeClass();
}

//  void QOpcUaAddNodeItem::setNodeClass(const QOpcUa::NodeClass &nodeClass)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem12setNodeClassERKN6QOpcUa9NodeClassE(
    QOpcUaAddNodeItem *self,
    const QOpcUa::NodeClass *nodeClass) {
  self->setNodeClass(*nodeClass);
}

//  QOpcUaNodeCreationAttributes QOpcUaAddNodeItem::nodeAttributes() const
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributes *ritual_ZNK17QOpcUaAddNodeItem14nodeAttributesEv(
    const QOpcUaAddNodeItem *self) {
  return new QOpcUaNodeCreationAttributes(self->nodeAttributes());
}

//  QOpcUaNodeCreationAttributes &QOpcUaAddNodeItem::nodeAttributesRef()
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributes *ritual_ZN17QOpcUaAddNodeItem17nodeAttributesRefEv(
    QOpcUaAddNodeItem *self) {
  return &(self->nodeAttributesRef());
}

//  void QOpcUaAddNodeItem::setNodeAttributes(const
//      QOpcUaNodeCreationAttributes &nodeAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem17setNodeAttributesERK28QOpcUaNodeCreationAttributes(
    QOpcUaAddNodeItem *self,
    const QOpcUaNodeCreationAttributes *nodeAttributes) {
  self->setNodeAttributes(*nodeAttributes);
}

//  QOpcUaExpandedNodeId QOpcUaAddNodeItem::typeDefinition() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK17QOpcUaAddNodeItem14typeDefinitionEv(
    const QOpcUaAddNodeItem *self) {
  return new QOpcUaExpandedNodeId(self->typeDefinition());
}

//  void QOpcUaAddNodeItem::setTypeDefinition(const QOpcUaExpandedNodeId
//      &typeDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaAddNodeItem17setTypeDefinitionERK20QOpcUaExpandedNodeId(
    QOpcUaAddNodeItem *self,
    const QOpcUaExpandedNodeId *typeDefinition) {
  self->setTypeDefinition(*typeDefinition);
}
