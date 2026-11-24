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

//  DomButtonGroup::DomButtonGroup()
extern "C" Q_DECL_EXPORT
DomButtonGroup *ritual_ZN14DomButtonGroupC1Ev() {
  return new DomButtonGroup();
}

//  DomButtonGroup::~DomButtonGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomButtonGroupD1Ev(DomButtonGroup *self) {
  delete self;
}

//  bool DomButtonGroup::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14DomButtonGroup16hasAttributeNameEv(
    const DomButtonGroup *self) {
  return self->hasAttributeName();
}

//  QString DomButtonGroup::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14DomButtonGroup13attributeNameEv(
    const DomButtonGroup *self) {
  return new QString(self->attributeName());
}

//  void DomButtonGroup::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomButtonGroup16setAttributeNameERK7QString(
    DomButtonGroup *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomButtonGroup::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomButtonGroup18clearAttributeNameEv(DomButtonGroup *self) {
  self->clearAttributeName();
}

//  QList<DomProperty *> DomButtonGroup::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK14DomButtonGroup15elementPropertyEv(
    const DomButtonGroup *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomButtonGroup::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomButtonGroup18setElementPropertyERK5QListIP11DomPropertyE(
    DomButtonGroup *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomProperty *> DomButtonGroup::elementAttribute() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK14DomButtonGroup16elementAttributeEv(
    const DomButtonGroup *self) {
  return new QList<DomProperty *>(self->elementAttribute());
}

//  void DomButtonGroup::setElementAttribute(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomButtonGroup19setElementAttributeERK5QListIP11DomPropertyE(
    DomButtonGroup *self,
    const QList<DomProperty *> *a) {
  self->setElementAttribute(*a);
}

//  QList<DomButtonGroup *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomButtonGroup *> *ritual_list_make_DomButtonGroup_ptr() {
  return new QList<DomButtonGroup *>();
}

//  void QList<DomButtonGroup *>::append(const DomButtonGroup * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomButtonGroup_ptr(
    QList<DomButtonGroup *> *self,
    DomButtonGroup *element) {
  self->append(element);
}

//  qsizetype QList<DomButtonGroup *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomButtonGroup_ptr(
    const QList<DomButtonGroup *> *self) {
  return self->size();
}

//  const DomButtonGroup * &QList<DomButtonGroup *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomButtonGroup *ritual_list_at_DomButtonGroup_ptr(
    const QList<DomButtonGroup *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomButtonGroup *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomButtonGroup_ptr(QList<DomButtonGroup *> *self) {
  delete self;
}
