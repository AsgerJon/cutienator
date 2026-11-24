//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qvariant.h>

//  QVariant QAssociativeIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAssociativeIterator3keyEv(
    const QAssociativeIterator *self) {
  return new QVariant(self->key());
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
