//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/QVariant>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <QtCore/qstring.h>

//  QtMetaContainerPrivate::Association::Association()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC1Ev() {
  return new QtMetaContainerPrivate::Association();
}

//  QtMetaContainerPrivate::Association::Association(const QMetaAssociation
//      &metaAssociation, QMetaType metaType, void *iterable)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC1ERK16QMetaAssociation9QMetaTypePv(
    const QMetaAssociation *metaAssociation,
    const QMetaType *metaType,
    void *iterable) {
  return new QtMetaContainerPrivate::Association(
      *metaAssociation,
      *metaType,
      iterable);
}

//  QtMetaContainerPrivate::Association::Association(const QMetaAssociation
//      &metaAssociation, QMetaType metaType, const void *iterable)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC1ERK16QMetaAssociation9QMetaTypePKv(
    const QMetaAssociation *metaAssociation,
    const QMetaType *metaType,
    const void *iterable) {
  return new QtMetaContainerPrivate::Association(
      *metaAssociation,
      *metaType,
      iterable);
}

//  QtMetaContainerPrivate::Association::Association(QIterable<QMetaAssociati
//      on> &&other)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC1EO9QIterableI16QMetaAssociationE(
    QIterable<QMetaAssociation> *other) {
  return new QtMetaContainerPrivate::Association(std::move(*other));
}

//  Association &QtMetaContainerPrivate::Association::operator=(QIterable<QMe
//      taAssociation> &&other)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationaSEO9QIterableI16QMetaAssociationE(
    QtMetaContainerPrivate::Association *self,
    QIterable<QMetaAssociation> *other) {
  return &(self->operator=(std::move(*other)));
}

//  ConstIterator QtMetaContainerPrivate::Association::begin() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association5beginEv(
    const QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::ConstIterator(
      self->begin());
}

//  ConstIterator QtMetaContainerPrivate::Association::end() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association3endEv(
    const QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::ConstIterator(self->end());
}

//  ConstIterator QtMetaContainerPrivate::Association::constBegin() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association10constBeginEv(
    const QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::ConstIterator(
      self->constBegin());
}

//  ConstIterator QtMetaContainerPrivate::Association::constEnd() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association8constEndEv(
    const QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::ConstIterator(
      self->constEnd());
}

//  Iterator QtMetaContainerPrivate::Association::mutableBegin()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::Iterator *ritual_ZN22QtMetaContainerPrivate11Association12mutableBeginEv(
    QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::Iterator(
      self->mutableBegin());
}

//  Iterator QtMetaContainerPrivate::Association::mutableEnd()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::Iterator *ritual_ZN22QtMetaContainerPrivate11Association10mutableEndEv(
    QtMetaContainerPrivate::Association *self) {
  return new QtMetaContainerPrivate::Association::Iterator(
      self->mutableEnd());
}

//  ConstIterator QtMetaContainerPrivate::Association::find(const QVariant
//      &key) const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association4findERK8QVariant(
    const QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  return new QtMetaContainerPrivate::Association::ConstIterator(
      self->find(
          *key));
}

//  ConstIterator QtMetaContainerPrivate::Association::constFind(const
//      QVariant &key) const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::ConstIterator *ritual_ZNK22QtMetaContainerPrivate11Association9constFindERK8QVariant(
    const QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  return new QtMetaContainerPrivate::Association::ConstIterator(
      self->constFind(
          *key));
}

//  Iterator QtMetaContainerPrivate::Association::mutableFind(const QVariant
//      &key)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association::Iterator *ritual_ZN22QtMetaContainerPrivate11Association11mutableFindERK8QVariant(
    QtMetaContainerPrivate::Association *self,
    const QVariant *key) {
  return new QtMetaContainerPrivate::Association::Iterator(
      self->mutableFind(
          *key));
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

//  a QtMetaContainerPrivate::Association::ConstIterator a ritual of
//      QtMetaContainerPrivate::Association gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_Association__QtMetaContainerPrivate_Association_ConstIterator(
    QtMetaContainerPrivate::Association::ConstIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::Association::Iterator a ritual of
//      QtMetaContainerPrivate::Association gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_Association__QtMetaContainerPrivate_Association_Iterator(
    QtMetaContainerPrivate::Association::Iterator *self) {
  delete self;
}

//  QtMetaContainerPrivate::Association::Association<
//      QMap<QString, QVariant>>(
//      QMap<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC2I4QMapI7QString8QVariantEEEPT_(
    QMap<QString, QVariant> *p) {
  return new QtMetaContainerPrivate::Association(p);
}

//  QtMetaContainerPrivate::Association::Association<
//      QMap<QString, QVariant>>(
//      const QMap<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC2I4QMapI7QString8QVariantEEEPKT_(
    const QMap<QString, QVariant> *p) {
  return new QtMetaContainerPrivate::Association(p);
}

//  QtMetaContainerPrivate::Association::Association<
//      QHash<QString, QVariant>>(
//      QHash<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC2I5QHashI7QString8QVariantEEEPT_(
    QHash<QString, QVariant> *p) {
  return new QtMetaContainerPrivate::Association(p);
}

//  QtMetaContainerPrivate::Association::Association<
//      QHash<QString, QVariant>>(
//      const QHash<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Association *ritual_ZN22QtMetaContainerPrivate11AssociationC2I5QHashI7QString8QVariantEEEPKT_(
    const QHash<QString, QVariant> *p) {
  return new QtMetaContainerPrivate::Association(p);
}
