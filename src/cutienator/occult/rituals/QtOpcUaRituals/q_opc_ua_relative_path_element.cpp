//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuarelativepathelement.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuarelativepathelement.h>
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOpcUaRelativePathElement::QOpcUaRelativePathElement()
extern "C" Q_DECL_EXPORT
QOpcUaRelativePathElement *ritual_ZN25QOpcUaRelativePathElementC1Ev() {
  return new QOpcUaRelativePathElement();
}

//  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
//      QOpcUaQualifiedName &target, const QString &refType)
extern "C" Q_DECL_EXPORT
QOpcUaRelativePathElement *ritual_ZN25QOpcUaRelativePathElementC1ERK19QOpcUaQualifiedNameRK7QString(
    const QOpcUaQualifiedName *target,
    const QString *refType) {
  return new QOpcUaRelativePathElement(*target, *refType);
}

//  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
//      QOpcUaQualifiedName &target, QOpcUa::ReferenceTypeId refType)
extern "C" Q_DECL_EXPORT
QOpcUaRelativePathElement *ritual_ZN25QOpcUaRelativePathElementC1ERK19QOpcUaQualifiedNameN6QOpcUa15ReferenceTypeIdE(
    const QOpcUaQualifiedName *target,
    QOpcUa::ReferenceTypeId refType) {
  return new QOpcUaRelativePathElement(*target, refType);
}

//  QOpcUaRelativePathElement::QOpcUaRelativePathElement(const
//      QOpcUaRelativePathElement &a0)
extern "C" Q_DECL_EXPORT
QOpcUaRelativePathElement *ritual_ZN25QOpcUaRelativePathElementC1ERKS_(
    const QOpcUaRelativePathElement *a0) {
  return new QOpcUaRelativePathElement(*a0);
}

//  QOpcUaRelativePathElement::~QOpcUaRelativePathElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElementD1Ev(
    QOpcUaRelativePathElement *self) {
  delete self;
}

//  QString QOpcUaRelativePathElement::referenceTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaRelativePathElement15referenceTypeIdEv(
    const QOpcUaRelativePathElement *self) {
  return new QString(self->referenceTypeId());
}

//  void QOpcUaRelativePathElement::setReferenceTypeId(const QString
//      &referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElement18setReferenceTypeIdERK7QString(
    QOpcUaRelativePathElement *self,
    const QString *referenceTypeId) {
  self->setReferenceTypeId(*referenceTypeId);
}

//  void
//      QOpcUaRelativePathElement::setReferenceTypeId(QOpcUa::ReferenceTypeId
//      referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElement18setReferenceTypeIdEN6QOpcUa15ReferenceTypeIdE(
    QOpcUaRelativePathElement *self,
    QOpcUa::ReferenceTypeId referenceTypeId) {
  self->setReferenceTypeId(referenceTypeId);
}

//  bool QOpcUaRelativePathElement::isInverse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaRelativePathElement9isInverseEv(
    const QOpcUaRelativePathElement *self) {
  return self->isInverse();
}

//  void QOpcUaRelativePathElement::setIsInverse(bool isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElement12setIsInverseEb(
    QOpcUaRelativePathElement *self,
    bool isInverse) {
  self->setIsInverse(isInverse);
}

//  bool QOpcUaRelativePathElement::includeSubtypes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaRelativePathElement15includeSubtypesEv(
    const QOpcUaRelativePathElement *self) {
  return self->includeSubtypes();
}

//  void QOpcUaRelativePathElement::setIncludeSubtypes(bool includeSubtypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElement18setIncludeSubtypesEb(
    QOpcUaRelativePathElement *self,
    bool includeSubtypes) {
  self->setIncludeSubtypes(includeSubtypes);
}

//  QVariant QOpcUaRelativePathElement::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QOpcUaRelativePathElementcv8QVariantEv(
    const QOpcUaRelativePathElement *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaQualifiedName QOpcUaRelativePathElement::targetName() const
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZNK25QOpcUaRelativePathElement10targetNameEv(
    const QOpcUaRelativePathElement *self) {
  return new QOpcUaQualifiedName(self->targetName());
}

//  void QOpcUaRelativePathElement::setTargetName(const QOpcUaQualifiedName
//      &targetName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaRelativePathElement13setTargetNameERK19QOpcUaQualifiedName(
    QOpcUaRelativePathElement *self,
    const QOpcUaQualifiedName *targetName) {
  self->setTargetName(*targetName);
}

//  bool operator==(const QOpcUaRelativePathElement &lhs, const
//      QOpcUaRelativePathElement &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK25QOpcUaRelativePathElementS1_(
    const QOpcUaRelativePathElement *lhs,
    const QOpcUaRelativePathElement *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaRelativePathElement &lhs, const
//      QOpcUaRelativePathElement &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK25QOpcUaRelativePathElementS1_(
    const QOpcUaRelativePathElement *lhs,
    const QOpcUaRelativePathElement *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaRelativePathElement>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaRelativePathElement> *ritual_list_make_QOpcUaRelativePathElement() {
  return new QList<QOpcUaRelativePathElement>();
}

//  void QList<QOpcUaRelativePathElement>::append(const
//      QOpcUaRelativePathElement &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaRelativePathElement(
    QList<QOpcUaRelativePathElement> *self,
    const QOpcUaRelativePathElement *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaRelativePathElement>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaRelativePathElement(
    const QList<QOpcUaRelativePathElement> *self) {
  return self->size();
}

//  const QOpcUaRelativePathElement
//      &QList<QOpcUaRelativePathElement>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaRelativePathElement *ritual_list_at_QOpcUaRelativePathElement(
    const QList<QOpcUaRelativePathElement> *self,
    long long index) {
  return new QOpcUaRelativePathElement(self->at(index));
}

//  QList<QOpcUaRelativePathElement>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaRelativePathElement(
    QList<QOpcUaRelativePathElement> *self) {
  delete self;
}
