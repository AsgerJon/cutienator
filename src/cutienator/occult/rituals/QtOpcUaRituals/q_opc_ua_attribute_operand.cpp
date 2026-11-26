//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaattributeoperand.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaattributeoperand.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtCore/qlist.h>

//  QOpcUaAttributeOperand::QOpcUaAttributeOperand()
extern "C" Q_DECL_EXPORT
QOpcUaAttributeOperand *ritual_ZN22QOpcUaAttributeOperandC1Ev() {
  return new QOpcUaAttributeOperand();
}

//  QOpcUaAttributeOperand::QOpcUaAttributeOperand(const
//      QOpcUaAttributeOperand &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAttributeOperand *ritual_ZN22QOpcUaAttributeOperandC1ERKS_(
    const QOpcUaAttributeOperand *a0) {
  return new QOpcUaAttributeOperand(*a0);
}

//  QOpcUaAttributeOperand &QOpcUaAttributeOperand::operator=(const
//      QOpcUaAttributeOperand &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAttributeOperand *ritual_ZN22QOpcUaAttributeOperandaSERKS_(
    QOpcUaAttributeOperand *self,
    const QOpcUaAttributeOperand *a0) {
  return &(self->operator=(*a0));
}

//  QVariant QOpcUaAttributeOperand::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QOpcUaAttributeOperandcv8QVariantEv(
    const QOpcUaAttributeOperand *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaAttributeOperand::~QOpcUaAttributeOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperandD1Ev(QOpcUaAttributeOperand *self) {
  delete self;
}

//  QString QOpcUaAttributeOperand::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAttributeOperand6nodeIdEv(
    const QOpcUaAttributeOperand *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaAttributeOperand::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperand9setNodeIdERK7QString(
    QOpcUaAttributeOperand *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QString QOpcUaAttributeOperand::alias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAttributeOperand5aliasEv(
    const QOpcUaAttributeOperand *self) {
  return new QString(self->alias());
}

//  void QOpcUaAttributeOperand::setAlias(const QString &alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperand8setAliasERK7QString(
    QOpcUaAttributeOperand *self,
    const QString *alias) {
  self->setAlias(*alias);
}

//  QList<QOpcUaRelativePathElement> QOpcUaAttributeOperand::browsePath()
//      const
extern "C" Q_DECL_EXPORT
QList<QOpcUaRelativePathElement> *ritual_ZNK22QOpcUaAttributeOperand10browsePathEv(
    const QOpcUaAttributeOperand *self) {
  return new QList<QOpcUaRelativePathElement>(self->browsePath());
}

//  QList<QOpcUaRelativePathElement> &QOpcUaAttributeOperand::browsePathRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUaRelativePathElement> *ritual_ZN22QOpcUaAttributeOperand13browsePathRefEv(
    QOpcUaAttributeOperand *self) {
  return &(self->browsePathRef());
}

//  void QOpcUaAttributeOperand::setBrowsePath(const
//      QList<QOpcUaRelativePathElement> &browsePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperand13setBrowsePathERK5QListI25QOpcUaRelativePathElementE(
    QOpcUaAttributeOperand *self,
    const QList<QOpcUaRelativePathElement> *browsePath) {
  self->setBrowsePath(*browsePath);
}

//  QOpcUa::NodeAttribute QOpcUaAttributeOperand::attributeId() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK22QOpcUaAttributeOperand11attributeIdEv(
    const QOpcUaAttributeOperand *self) {
  return self->attributeId();
}

//  void QOpcUaAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
//      attributeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperand14setAttributeIdEN6QOpcUa13NodeAttributeE(
    QOpcUaAttributeOperand *self,
    QOpcUa::NodeAttribute attributeId) {
  self->setAttributeId(attributeId);
}

//  QString QOpcUaAttributeOperand::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaAttributeOperand10indexRangeEv(
    const QOpcUaAttributeOperand *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaAttributeOperand::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaAttributeOperand13setIndexRangeERK7QString(
    QOpcUaAttributeOperand *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  bool operator==(const QOpcUaAttributeOperand &lhs, const
//      QOpcUaAttributeOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK22QOpcUaAttributeOperandS1_(
    const QOpcUaAttributeOperand *lhs,
    const QOpcUaAttributeOperand *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaAttributeOperand &lhs, const
//      QOpcUaAttributeOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK22QOpcUaAttributeOperandS1_(
    const QOpcUaAttributeOperand *lhs,
    const QOpcUaAttributeOperand *rhs) {
  return operator!=(*lhs, *rhs);
}
