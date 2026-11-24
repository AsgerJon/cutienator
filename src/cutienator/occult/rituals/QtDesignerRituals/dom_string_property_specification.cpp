//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomStringPropertySpecification::DomStringPropertySpecification()
extern "C" Q_DECL_EXPORT
DomStringPropertySpecification *ritual_ZN30DomStringPropertySpecificationC1Ev() {
  return new DomStringPropertySpecification();
}

//  DomStringPropertySpecification::~DomStringPropertySpecification()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecificationD1Ev(
    DomStringPropertySpecification *self) {
  delete self;
}

//  bool DomStringPropertySpecification::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30DomStringPropertySpecification16hasAttributeNameEv(
    const DomStringPropertySpecification *self) {
  return self->hasAttributeName();
}

//  QString DomStringPropertySpecification::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30DomStringPropertySpecification13attributeNameEv(
    const DomStringPropertySpecification *self) {
  return new QString(self->attributeName());
}

//  void DomStringPropertySpecification::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification16setAttributeNameERK7QString(
    DomStringPropertySpecification *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomStringPropertySpecification::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification18clearAttributeNameEv(
    DomStringPropertySpecification *self) {
  self->clearAttributeName();
}

//  bool DomStringPropertySpecification::hasAttributeType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30DomStringPropertySpecification16hasAttributeTypeEv(
    const DomStringPropertySpecification *self) {
  return self->hasAttributeType();
}

//  QString DomStringPropertySpecification::attributeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30DomStringPropertySpecification13attributeTypeEv(
    const DomStringPropertySpecification *self) {
  return new QString(self->attributeType());
}

//  void DomStringPropertySpecification::setAttributeType(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification16setAttributeTypeERK7QString(
    DomStringPropertySpecification *self,
    const QString *a) {
  self->setAttributeType(*a);
}

//  void DomStringPropertySpecification::clearAttributeType()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification18clearAttributeTypeEv(
    DomStringPropertySpecification *self) {
  self->clearAttributeType();
}

//  bool DomStringPropertySpecification::hasAttributeNotr() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30DomStringPropertySpecification16hasAttributeNotrEv(
    const DomStringPropertySpecification *self) {
  return self->hasAttributeNotr();
}

//  QString DomStringPropertySpecification::attributeNotr() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30DomStringPropertySpecification13attributeNotrEv(
    const DomStringPropertySpecification *self) {
  return new QString(self->attributeNotr());
}

//  void DomStringPropertySpecification::setAttributeNotr(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification16setAttributeNotrERK7QString(
    DomStringPropertySpecification *self,
    const QString *a) {
  self->setAttributeNotr(*a);
}

//  void DomStringPropertySpecification::clearAttributeNotr()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DomStringPropertySpecification18clearAttributeNotrEv(
    DomStringPropertySpecification *self) {
  self->clearAttributeNotr();
}

//  QList<DomStringPropertySpecification *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomStringPropertySpecification *> *ritual_list_make_DomStringPropertySpecification_ptr() {
  return new QList<DomStringPropertySpecification *>();
}

//  void QList<DomStringPropertySpecification *>::append(const
//      DomStringPropertySpecification * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomStringPropertySpecification_ptr(
    QList<DomStringPropertySpecification *> *self,
    DomStringPropertySpecification *element) {
  self->append(element);
}

//  qsizetype QList<DomStringPropertySpecification *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomStringPropertySpecification_ptr(
    const QList<DomStringPropertySpecification *> *self) {
  return self->size();
}

//  const DomStringPropertySpecification *
//      &QList<DomStringPropertySpecification *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomStringPropertySpecification *ritual_list_at_DomStringPropertySpecification_ptr(
    const QList<DomStringPropertySpecification *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomStringPropertySpecification *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomStringPropertySpecification_ptr(
    QList<DomStringPropertySpecification *> *self) {
  delete self;
}
