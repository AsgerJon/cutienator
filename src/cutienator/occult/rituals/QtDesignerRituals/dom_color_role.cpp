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

//  DomColorRole::DomColorRole()
extern "C" Q_DECL_EXPORT
DomColorRole *ritual_ZN12DomColorRoleC1Ev() {
  return new DomColorRole();
}

//  DomColorRole::~DomColorRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomColorRoleD1Ev(DomColorRole *self) {
  delete self;
}

//  bool DomColorRole::hasAttributeRole() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12DomColorRole16hasAttributeRoleEv(const DomColorRole *self) {
  return self->hasAttributeRole();
}

//  QString DomColorRole::attributeRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12DomColorRole13attributeRoleEv(
    const DomColorRole *self) {
  return new QString(self->attributeRole());
}

//  void DomColorRole::setAttributeRole(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomColorRole16setAttributeRoleERK7QString(
    DomColorRole *self,
    const QString *a) {
  self->setAttributeRole(*a);
}

//  void DomColorRole::clearAttributeRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomColorRole18clearAttributeRoleEv(DomColorRole *self) {
  self->clearAttributeRole();
}

//  DomBrush *DomColorRole::elementBrush() const
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZNK12DomColorRole12elementBrushEv(
    const DomColorRole *self) {
  return self->elementBrush();
}

//  DomBrush *DomColorRole::takeElementBrush()
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZN12DomColorRole16takeElementBrushEv(DomColorRole *self) {
  return self->takeElementBrush();
}

//  void DomColorRole::setElementBrush(DomBrush *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomColorRole15setElementBrushEP8DomBrush(
    DomColorRole *self,
    DomBrush *a) {
  self->setElementBrush(a);
}

//  bool DomColorRole::hasElementBrush() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12DomColorRole15hasElementBrushEv(const DomColorRole *self) {
  return self->hasElementBrush();
}

//  void DomColorRole::clearElementBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomColorRole17clearElementBrushEv(DomColorRole *self) {
  self->clearElementBrush();
}

//  QList<DomColorRole *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomColorRole *> *ritual_list_make_DomColorRole_ptr() {
  return new QList<DomColorRole *>();
}

//  void QList<DomColorRole *>::append(const DomColorRole * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomColorRole_ptr(
    QList<DomColorRole *> *self,
    DomColorRole *element) {
  self->append(element);
}

//  qsizetype QList<DomColorRole *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomColorRole_ptr(
    const QList<DomColorRole *> *self) {
  return self->size();
}

//  const DomColorRole * &QList<DomColorRole *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomColorRole *ritual_list_at_DomColorRole_ptr(
    const QList<DomColorRole *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomColorRole *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomColorRole_ptr(QList<DomColorRole *> *self) {
  delete self;
}
