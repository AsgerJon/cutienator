//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomItem::DomItem()
extern "C" Q_DECL_EXPORT
DomItem *ritual_ZN7DomItemC1Ev() {
  return new DomItem();
}

//  DomItem::~DomItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItemD1Ev(DomItem *self) {
  delete self;
}

//  bool DomItem::hasAttributeRow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomItem15hasAttributeRowEv(const DomItem *self) {
  return self->hasAttributeRow();
}

//  int DomItem::attributeRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomItem12attributeRowEv(const DomItem *self) {
  return self->attributeRow();
}

//  void DomItem::setAttributeRow(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem15setAttributeRowEi(DomItem *self, int a) {
  self->setAttributeRow(a);
}

//  void DomItem::clearAttributeRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem17clearAttributeRowEv(DomItem *self) {
  self->clearAttributeRow();
}

//  bool DomItem::hasAttributeColumn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomItem18hasAttributeColumnEv(const DomItem *self) {
  return self->hasAttributeColumn();
}

//  int DomItem::attributeColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomItem15attributeColumnEv(const DomItem *self) {
  return self->attributeColumn();
}

//  void DomItem::setAttributeColumn(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem18setAttributeColumnEi(DomItem *self, int a) {
  self->setAttributeColumn(a);
}

//  void DomItem::clearAttributeColumn()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem20clearAttributeColumnEv(DomItem *self) {
  self->clearAttributeColumn();
}

//  QList<DomProperty *> DomItem::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK7DomItem15elementPropertyEv(
    const DomItem *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomItem::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem18setElementPropertyERK5QListIP11DomPropertyE(
    DomItem *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomItem *> DomItem::elementItem() const
extern "C" Q_DECL_EXPORT
QList<DomItem *> *ritual_ZNK7DomItem11elementItemEv(const DomItem *self) {
  return new QList<DomItem *>(self->elementItem());
}

//  void DomItem::setElementItem(const QList<DomItem *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomItem14setElementItemERK5QListIPS_E(
    DomItem *self,
    const QList<DomItem *> *a) {
  self->setElementItem(*a);
}

//  QList<DomItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomItem *> *ritual_list_make_DomItem_ptr() {
  return new QList<DomItem *>();
}

//  void QList<DomItem *>::append(const DomItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomItem_ptr(QList<DomItem *> *self, DomItem *element) {
  self->append(element);
}

//  qsizetype QList<DomItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomItem_ptr(const QList<DomItem *> *self) {
  return self->size();
}

//  const DomItem * &QList<DomItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomItem *ritual_list_at_DomItem_ptr(
    const QList<DomItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomItem_ptr(QList<DomItem *> *self) {
  delete self;
}
