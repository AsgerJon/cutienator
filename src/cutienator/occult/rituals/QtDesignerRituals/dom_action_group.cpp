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

//  DomActionGroup::DomActionGroup()
extern "C" Q_DECL_EXPORT
DomActionGroup *ritual_ZN14DomActionGroupC1Ev() {
  return new DomActionGroup();
}

//  DomActionGroup::~DomActionGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroupD1Ev(DomActionGroup *self) {
  delete self;
}

//  bool DomActionGroup::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14DomActionGroup16hasAttributeNameEv(
    const DomActionGroup *self) {
  return self->hasAttributeName();
}

//  QString DomActionGroup::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14DomActionGroup13attributeNameEv(
    const DomActionGroup *self) {
  return new QString(self->attributeName());
}

//  void DomActionGroup::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup16setAttributeNameERK7QString(
    DomActionGroup *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomActionGroup::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup18clearAttributeNameEv(DomActionGroup *self) {
  self->clearAttributeName();
}

//  QList<DomAction *> DomActionGroup::elementAction() const
extern "C" Q_DECL_EXPORT
QList<DomAction *> *ritual_ZNK14DomActionGroup13elementActionEv(
    const DomActionGroup *self) {
  return new QList<DomAction *>(self->elementAction());
}

//  void DomActionGroup::setElementAction(const QList<DomAction *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup16setElementActionERK5QListIP9DomActionE(
    DomActionGroup *self,
    const QList<DomAction *> *a) {
  self->setElementAction(*a);
}

//  QList<DomActionGroup *> DomActionGroup::elementActionGroup() const
extern "C" Q_DECL_EXPORT
QList<DomActionGroup *> *ritual_ZNK14DomActionGroup18elementActionGroupEv(
    const DomActionGroup *self) {
  return new QList<DomActionGroup *>(self->elementActionGroup());
}

//  void DomActionGroup::setElementActionGroup(const QList<DomActionGroup *>
//      &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup21setElementActionGroupERK5QListIPS_E(
    DomActionGroup *self,
    const QList<DomActionGroup *> *a) {
  self->setElementActionGroup(*a);
}

//  QList<DomProperty *> DomActionGroup::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK14DomActionGroup15elementPropertyEv(
    const DomActionGroup *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomActionGroup::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup18setElementPropertyERK5QListIP11DomPropertyE(
    DomActionGroup *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomProperty *> DomActionGroup::elementAttribute() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK14DomActionGroup16elementAttributeEv(
    const DomActionGroup *self) {
  return new QList<DomProperty *>(self->elementAttribute());
}

//  void DomActionGroup::setElementAttribute(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomActionGroup19setElementAttributeERK5QListIP11DomPropertyE(
    DomActionGroup *self,
    const QList<DomProperty *> *a) {
  self->setElementAttribute(*a);
}

//  QList<DomActionGroup *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomActionGroup *> *ritual_list_make_DomActionGroup_ptr() {
  return new QList<DomActionGroup *>();
}

//  void QList<DomActionGroup *>::append(const DomActionGroup * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomActionGroup_ptr(
    QList<DomActionGroup *> *self,
    DomActionGroup *element) {
  self->append(element);
}

//  qsizetype QList<DomActionGroup *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomActionGroup_ptr(
    const QList<DomActionGroup *> *self) {
  return self->size();
}

//  const DomActionGroup * &QList<DomActionGroup *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomActionGroup *ritual_list_at_DomActionGroup_ptr(
    const QList<DomActionGroup *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomActionGroup *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomActionGroup_ptr(QList<DomActionGroup *> *self) {
  delete self;
}
