//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuasimpleattributeoperand.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuasimpleattributeoperand.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtCore/qlist.h>

//  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand()
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_ZN28QOpcUaSimpleAttributeOperandC1Ev() {
  return new QOpcUaSimpleAttributeOperand();
}

//  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const
//      QOpcUaSimpleAttributeOperand &a0)
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_ZN28QOpcUaSimpleAttributeOperandC1ERKS_(
    const QOpcUaSimpleAttributeOperand *a0) {
  return new QOpcUaSimpleAttributeOperand(*a0);
}

//  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(const QString
//      &name, quint16 namespaceIndex, const QString &typeId,
//      QOpcUa::NodeAttribute attributeId)
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_ZN28QOpcUaSimpleAttributeOperandC1ERK7QStringtS2_N6QOpcUa13NodeAttributeE(
    const QString *name,
    quint16 namespaceIndex,
    const QString *typeId,
    QOpcUa::NodeAttribute attributeId) {
  return new QOpcUaSimpleAttributeOperand(
      *name,
      namespaceIndex,
      *typeId,
      attributeId);
}

//  QOpcUaSimpleAttributeOperand::QOpcUaSimpleAttributeOperand(QOpcUa::NodeAt
//      tribute attributeId, const QString &typeId)
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_ZN28QOpcUaSimpleAttributeOperandC1EN6QOpcUa13NodeAttributeERK7QString(
    QOpcUa::NodeAttribute attributeId,
    const QString *typeId) {
  return new QOpcUaSimpleAttributeOperand(attributeId, *typeId);
}

//  QOpcUaSimpleAttributeOperand
//      &QOpcUaSimpleAttributeOperand::operator=(const
//      QOpcUaSimpleAttributeOperand &a0)
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_ZN28QOpcUaSimpleAttributeOperandaSERKS_(
    QOpcUaSimpleAttributeOperand *self,
    const QOpcUaSimpleAttributeOperand *a0) {
  return &(self->operator=(*a0));
}

//  QVariant QOpcUaSimpleAttributeOperand::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QOpcUaSimpleAttributeOperandcv8QVariantEv(
    const QOpcUaSimpleAttributeOperand *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaSimpleAttributeOperand::~QOpcUaSimpleAttributeOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaSimpleAttributeOperandD1Ev(
    QOpcUaSimpleAttributeOperand *self) {
  delete self;
}

//  QString QOpcUaSimpleAttributeOperand::typeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaSimpleAttributeOperand6typeIdEv(
    const QOpcUaSimpleAttributeOperand *self) {
  return new QString(self->typeId());
}

//  void QOpcUaSimpleAttributeOperand::setTypeId(const QString &typeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaSimpleAttributeOperand9setTypeIdERK7QString(
    QOpcUaSimpleAttributeOperand *self,
    const QString *typeId) {
  self->setTypeId(*typeId);
}

//  QList<QOpcUaQualifiedName> QOpcUaSimpleAttributeOperand::browsePath()
//      const
extern "C" Q_DECL_EXPORT
QList<QOpcUaQualifiedName> *ritual_ZNK28QOpcUaSimpleAttributeOperand10browsePathEv(
    const QOpcUaSimpleAttributeOperand *self) {
  return new QList<QOpcUaQualifiedName>(self->browsePath());
}

//  QList<QOpcUaQualifiedName> &QOpcUaSimpleAttributeOperand::browsePathRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUaQualifiedName> *ritual_ZN28QOpcUaSimpleAttributeOperand13browsePathRefEv(
    QOpcUaSimpleAttributeOperand *self) {
  return &(self->browsePathRef());
}

//  void QOpcUaSimpleAttributeOperand::setBrowsePath(const
//      QList<QOpcUaQualifiedName> &browsePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaSimpleAttributeOperand13setBrowsePathERK5QListI19QOpcUaQualifiedNameE(
    QOpcUaSimpleAttributeOperand *self,
    const QList<QOpcUaQualifiedName> *browsePath) {
  self->setBrowsePath(*browsePath);
}

//  QOpcUa::NodeAttribute QOpcUaSimpleAttributeOperand::attributeId() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK28QOpcUaSimpleAttributeOperand11attributeIdEv(
    const QOpcUaSimpleAttributeOperand *self) {
  return self->attributeId();
}

//  void QOpcUaSimpleAttributeOperand::setAttributeId(QOpcUa::NodeAttribute
//      attributeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaSimpleAttributeOperand14setAttributeIdEN6QOpcUa13NodeAttributeE(
    QOpcUaSimpleAttributeOperand *self,
    QOpcUa::NodeAttribute attributeId) {
  self->setAttributeId(attributeId);
}

//  QString QOpcUaSimpleAttributeOperand::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaSimpleAttributeOperand10indexRangeEv(
    const QOpcUaSimpleAttributeOperand *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaSimpleAttributeOperand::setIndexRange(const QString
//      &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaSimpleAttributeOperand13setIndexRangeERK7QString(
    QOpcUaSimpleAttributeOperand *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  bool operator==(const QOpcUaSimpleAttributeOperand &lhs, const
//      QOpcUaSimpleAttributeOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK28QOpcUaSimpleAttributeOperandS1_(
    const QOpcUaSimpleAttributeOperand *lhs,
    const QOpcUaSimpleAttributeOperand *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaSimpleAttributeOperand &lhs, const
//      QOpcUaSimpleAttributeOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK28QOpcUaSimpleAttributeOperandS1_(
    const QOpcUaSimpleAttributeOperand *lhs,
    const QOpcUaSimpleAttributeOperand *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaSimpleAttributeOperand>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaSimpleAttributeOperand> *ritual_list_make_QOpcUaSimpleAttributeOperand() {
  return new QList<QOpcUaSimpleAttributeOperand>();
}

//  void QList<QOpcUaSimpleAttributeOperand>::append(const
//      QOpcUaSimpleAttributeOperand &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaSimpleAttributeOperand(
    QList<QOpcUaSimpleAttributeOperand> *self,
    const QOpcUaSimpleAttributeOperand *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaSimpleAttributeOperand>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaSimpleAttributeOperand(
    const QList<QOpcUaSimpleAttributeOperand> *self) {
  return self->size();
}

//  const QOpcUaSimpleAttributeOperand
//      &QList<QOpcUaSimpleAttributeOperand>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaSimpleAttributeOperand *ritual_list_at_QOpcUaSimpleAttributeOperand(
    const QList<QOpcUaSimpleAttributeOperand> *self,
    long long index) {
  return new QOpcUaSimpleAttributeOperand(self->at(index));
}

//  QList<QOpcUaSimpleAttributeOperand>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaSimpleAttributeOperand(
    QList<QOpcUaSimpleAttributeOperand> *self) {
  delete self;
}
