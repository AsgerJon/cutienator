//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qvariant.h>

//  QtMetaContainerPrivate::Association::Association()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC1Ev() {
  return new QtMetaContainerPrivate::Association();
}

//  bool QtMetaContainerPrivate::Association::containsKey(const QVariant
//      &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QtMetaContainerPrivate11Association11containsKeyERK8QVariant(
    const QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  return self->containsKey(*key);
}

//  void QtMetaContainerPrivate::Association::insertKey(const QVariant &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate11Association9insertKeyERK8QVariant(
    QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  self->insertKey(*key);
}

//  void QtMetaContainerPrivate::Association::removeKey(const QVariant &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate11Association9removeKeyERK8QVariant(
    QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  self->removeKey(*key);
}

//  QVariant QtMetaContainerPrivate::Association::value(const QVariant &key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate11Association5valueERK8QVariant(
    const QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  return new QVariant(self->value(*key));
}

//  void QtMetaContainerPrivate::Association::setValue(const QVariant &key,
//      const QVariant &mapped)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate11Association8setValueERK8QVariantS3_(
    QtMetaContainerPrivate::Association *self,
    const QVariant *key,
    const QVariant *mapped) {
  self->setValue(*key, *mapped);
}

//  QtMetaContainerPrivate::Association::~Association()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate11AssociationD1Ev(
    QtMetaContainerPrivate::Association *self) {
  delete self;
}
