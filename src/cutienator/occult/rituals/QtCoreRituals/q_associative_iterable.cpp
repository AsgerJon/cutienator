//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Edited by hand on 2026-11-25,
//  mended on 2026-11-26: added by hand, instances of templates of the class:
//  4. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/QAssociativeIterable>
#include <QtCore/QVariant>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>

//  QAssociativeIterable::QAssociativeIterable()
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableC1Ev() {
  return new QAssociativeIterable();
}

//  QAssociativeIterable::QAssociativeIterable(const QMetaAssociation
//      &metaAssociation, const QMetaType &metaType, void *iterable)
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableC1ERK16QMetaAssociationRK9QMetaTypePv(
    const QMetaAssociation *metaAssociation,
    const QMetaType *metaType,
    void *iterable) {
  return new QAssociativeIterable(*metaAssociation, *metaType, iterable);
}

//  QAssociativeIterable::QAssociativeIterable(const QMetaAssociation
//      &metaAssociation, const QMetaType &metaType, const void *iterable)
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableC1ERK16QMetaAssociationRK9QMetaTypePKv(
    const QMetaAssociation *metaAssociation,
    const QMetaType *metaType,
    const void *iterable) {
  return new QAssociativeIterable(*metaAssociation, *metaType, iterable);
}

//  QAssociativeIterable::QAssociativeIterable(QIterable<QMetaAssociation>
//      &&other)
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableC1EO9QIterableI16QMetaAssociationE(
    QIterable<QMetaAssociation> *other) {
  return new QAssociativeIterable(std::move(*other));
}

//  QAssociativeIterable
//      &QAssociativeIterable::operator=(QIterable<QMetaAssociation> &&other)
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableaSEO9QIterableI16QMetaAssociationE(
    QAssociativeIterable *self,
    QIterable<QMetaAssociation> *other) {
  return &(self->operator=(std::move(*other)));
}

//  const_iterator QAssociativeIterable::begin() const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable5beginEv(
    const QAssociativeIterable *self) {
  return new QAssociativeIterable::const_iterator(self->begin());
}

//  const_iterator QAssociativeIterable::end() const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable3endEv(
    const QAssociativeIterable *self) {
  return new QAssociativeIterable::const_iterator(self->end());
}

//  const_iterator QAssociativeIterable::constBegin() const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable10constBeginEv(
    const QAssociativeIterable *self) {
  return new QAssociativeIterable::const_iterator(self->constBegin());
}

//  const_iterator QAssociativeIterable::constEnd() const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable8constEndEv(
    const QAssociativeIterable *self) {
  return new QAssociativeIterable::const_iterator(self->constEnd());
}

//  iterator QAssociativeIterable::mutableBegin()
extern "C" Q_DECL_EXPORT
QAssociativeIterable::iterator *ritual_ZN20QAssociativeIterable12mutableBeginEv(
    QAssociativeIterable *self) {
  return new QAssociativeIterable::iterator(self->mutableBegin());
}

//  iterator QAssociativeIterable::mutableEnd()
extern "C" Q_DECL_EXPORT
QAssociativeIterable::iterator *ritual_ZN20QAssociativeIterable10mutableEndEv(
    QAssociativeIterable *self) {
  return new QAssociativeIterable::iterator(self->mutableEnd());
}

//  const_iterator QAssociativeIterable::find(const QVariant &key) const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable4findERK8QVariant(
    const QAssociativeIterable *self,
    const QVariant *key) {
  return new QAssociativeIterable::const_iterator(self->find(*key));
}

//  const_iterator QAssociativeIterable::constFind(const QVariant &key) const
extern "C" Q_DECL_EXPORT
QAssociativeIterable::const_iterator *ritual_ZNK20QAssociativeIterable9constFindERK8QVariant(
    const QAssociativeIterable *self,
    const QVariant *key) {
  return new QAssociativeIterable::const_iterator(self->constFind(*key));
}

//  iterator QAssociativeIterable::mutableFind(const QVariant &key)
extern "C" Q_DECL_EXPORT
QAssociativeIterable::iterator *ritual_ZN20QAssociativeIterable11mutableFindERK8QVariant(
    QAssociativeIterable *self,
    const QVariant *key) {
  return new QAssociativeIterable::iterator(self->mutableFind(*key));
}

//  bool QAssociativeIterable::containsKey(const QVariant &key)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAssociativeIterable11containsKeyERK8QVariant(
    QAssociativeIterable *self,
    const QVariant *key) {
  return self->containsKey(*key);
}

//  void QAssociativeIterable::insertKey(const QVariant &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAssociativeIterable9insertKeyERK8QVariant(
    QAssociativeIterable *self,
    const QVariant *key) {
  self->insertKey(*key);
}

//  void QAssociativeIterable::removeKey(const QVariant &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAssociativeIterable9removeKeyERK8QVariant(
    QAssociativeIterable *self,
    const QVariant *key) {
  self->removeKey(*key);
}

//  QVariant QAssociativeIterable::value(const QVariant &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAssociativeIterable5valueERK8QVariant(
    const QAssociativeIterable *self,
    const QVariant *key) {
  return new QVariant(self->value(*key));
}

//  void QAssociativeIterable::setValue(const QVariant &key, const QVariant
//      &mapped)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAssociativeIterable8setValueERK8QVariantS2_(
    QAssociativeIterable *self,
    const QVariant *key,
    const QVariant *mapped) {
  self->setValue(*key, *mapped);
}

//  bool QAssociativeIterable::canRandomAccessIterate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAssociativeIterable22canRandomAccessIterateEv(
    const QAssociativeIterable *self) {
  return self->canRandomAccessIterate();
}

//  a QAssociativeIterable::const_iterator a ritual of QAssociativeIterable
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAssociativeIterable__QAssociativeIterable_const_iterator(
    QAssociativeIterable::const_iterator *self) {
  delete self;
}

//  a QAssociativeIterable::iterator a ritual of QAssociativeIterable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAssociativeIterable__QAssociativeIterable_iterator(
    QAssociativeIterable::iterator *self) {
  delete self;
}

//  QAssociativeIterable::QAssociativeIterable<QMap<QString, QVariant>>(const
//      QMap<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QAssociativeIterable * ritual_ZN20QAssociativeIterableC1I4QMapI7QString8QVariantEEEPKT_(
    const QMap<QString, QVariant> *p) {
  return new QAssociativeIterable(p);
}

//  QAssociativeIterable::QAssociativeIterable<QMap<QString,
//      QVariant>>(QMap<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QAssociativeIterable * ritual_ZN20QAssociativeIterableC1I4QMapI7QString8QVariantEEEPT_(
    QMap<QString, QVariant> *p) {
  return new QAssociativeIterable(p);
}

//  QAssociativeIterable::QAssociativeIterable<QHash<QString,
//      QVariant>>(const QHash<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QAssociativeIterable * ritual_ZN20QAssociativeIterableC1I5QHashI7QString8QVariantEEEPKT_(
    const QHash<QString, QVariant> *p) {
  return new QAssociativeIterable(p);
}

//  QAssociativeIterable::QAssociativeIterable<QHash<QString,
//      QVariant>>(QHash<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QAssociativeIterable * ritual_ZN20QAssociativeIterableC1I5QHashI7QString8QVariantEEEPT_(
    QHash<QString, QVariant> *p) {
  return new QAssociativeIterable(p);
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
