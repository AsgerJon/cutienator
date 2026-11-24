//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qvariant.h>

//  QAssociativeIterable::QAssociativeIterable()
extern "C" Q_DECL_EXPORT
QAssociativeIterable *ritual_ZN20QAssociativeIterableC1Ev() {
  return new QAssociativeIterable();
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

#endif  // QT_DEPRECATED_SINCE(6, 15)
