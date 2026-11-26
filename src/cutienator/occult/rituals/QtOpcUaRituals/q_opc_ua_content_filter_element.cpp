//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuacontentfilterelement.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuacontentfilterelement.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuasimpleattributeoperand.h>
#include <QtOpcUa/qopcuaattributeoperand.h>
#include <QtOpcUa/qopcualiteraloperand.h>
#include <QtOpcUa/qopcuaelementoperand.h>
#include <QtCore/qlist.h>

//  QOpcUaContentFilterElement::QOpcUaContentFilterElement()
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementC1Ev() {
  return new QOpcUaContentFilterElement();
}

//  QOpcUaContentFilterElement::QOpcUaContentFilterElement(const
//      QOpcUaContentFilterElement &a0)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementC1ERKS_(
    const QOpcUaContentFilterElement *a0) {
  return new QOpcUaContentFilterElement(*a0);
}

//  QOpcUaContentFilterElement &QOpcUaContentFilterElement::operator=(const
//      QOpcUaContentFilterElement &a0)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementaSERKS_(
    QOpcUaContentFilterElement *self,
    const QOpcUaContentFilterElement *a0) {
  return &(self->operator=(*a0));
}

//  QVariant QOpcUaContentFilterElement::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QOpcUaContentFilterElementcv8QVariantEv(
    const QOpcUaContentFilterElement *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaContentFilterElement::~QOpcUaContentFilterElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaContentFilterElementD1Ev(
    QOpcUaContentFilterElement *self) {
  delete self;
}

//  QOpcUaContentFilterElement
//      &QOpcUaContentFilterElement::operator<<(FilterOperator op)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementlsENS_14FilterOperatorE(
    QOpcUaContentFilterElement *self,
    QOpcUaContentFilterElement::FilterOperator op) {
  return &(self->operator<<(op));
}

//  QOpcUaContentFilterElement &QOpcUaContentFilterElement::operator<<(const
//      QOpcUaSimpleAttributeOperand &op)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementlsERK28QOpcUaSimpleAttributeOperand(
    QOpcUaContentFilterElement *self,
    const QOpcUaSimpleAttributeOperand *op) {
  return &(self->operator<<(*op));
}

//  QOpcUaContentFilterElement &QOpcUaContentFilterElement::operator<<(const
//      QOpcUaAttributeOperand &op)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementlsERK22QOpcUaAttributeOperand(
    QOpcUaContentFilterElement *self,
    const QOpcUaAttributeOperand *op) {
  return &(self->operator<<(*op));
}

//  QOpcUaContentFilterElement &QOpcUaContentFilterElement::operator<<(const
//      QOpcUaLiteralOperand &op)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementlsERK20QOpcUaLiteralOperand(
    QOpcUaContentFilterElement *self,
    const QOpcUaLiteralOperand *op) {
  return &(self->operator<<(*op));
}

//  QOpcUaContentFilterElement &QOpcUaContentFilterElement::operator<<(const
//      QOpcUaElementOperand &op)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_ZN26QOpcUaContentFilterElementlsERK20QOpcUaElementOperand(
    QOpcUaContentFilterElement *self,
    const QOpcUaElementOperand *op) {
  return &(self->operator<<(*op));
}

//  QOpcUaContentFilterElement::FilterOperator
//      QOpcUaContentFilterElement::filterOperator() const
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement::FilterOperator ritual_ZNK26QOpcUaContentFilterElement14filterOperatorEv(
    const QOpcUaContentFilterElement *self) {
  return self->filterOperator();
}

//  void QOpcUaContentFilterElement::setFilterOperator(QOpcUaContentFilterEle
//      ment::FilterOperator filterOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaContentFilterElement17setFilterOperatorENS_14FilterOperatorE(
    QOpcUaContentFilterElement *self,
    QOpcUaContentFilterElement::FilterOperator filterOperator) {
  self->setFilterOperator(filterOperator);
}

//  QList<QVariant> QOpcUaContentFilterElement::filterOperands() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK26QOpcUaContentFilterElement14filterOperandsEv(
    const QOpcUaContentFilterElement *self) {
  return new QList<QVariant>(self->filterOperands());
}

//  QList<QVariant> &QOpcUaContentFilterElement::filterOperandsRef()
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN26QOpcUaContentFilterElement17filterOperandsRefEv(
    QOpcUaContentFilterElement *self) {
  return &(self->filterOperandsRef());
}

//  void QOpcUaContentFilterElement::setFilterOperands(const QList<QVariant>
//      &filterOperands)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaContentFilterElement17setFilterOperandsERK5QListI8QVariantE(
    QOpcUaContentFilterElement *self,
    const QList<QVariant> *filterOperands) {
  self->setFilterOperands(*filterOperands);
}

//  bool operator==(const QOpcUaContentFilterElement &lhs, const
//      QOpcUaContentFilterElement &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QOpcUaContentFilterElementS1_(
    const QOpcUaContentFilterElement *lhs,
    const QOpcUaContentFilterElement *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaContentFilterElement &lhs, const
//      QOpcUaContentFilterElement &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QOpcUaContentFilterElementS1_(
    const QOpcUaContentFilterElement *lhs,
    const QOpcUaContentFilterElement *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaContentFilterElement>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElement> *ritual_list_make_QOpcUaContentFilterElement() {
  return new QList<QOpcUaContentFilterElement>();
}

//  void QList<QOpcUaContentFilterElement>::append(const
//      QOpcUaContentFilterElement &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaContentFilterElement(
    QList<QOpcUaContentFilterElement> *self,
    const QOpcUaContentFilterElement *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaContentFilterElement>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaContentFilterElement(
    const QList<QOpcUaContentFilterElement> *self) {
  return self->size();
}

//  const QOpcUaContentFilterElement
//      &QList<QOpcUaContentFilterElement>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElement *ritual_list_at_QOpcUaContentFilterElement(
    const QList<QOpcUaContentFilterElement> *self,
    long long index) {
  return new QOpcUaContentFilterElement(self->at(index));
}

//  QList<QOpcUaContentFilterElement>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaContentFilterElement(
    QList<QOpcUaContentFilterElement> *self) {
  delete self;
}
