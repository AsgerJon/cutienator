//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qsequentialiterable.h>
#include <QtCore/qvariant.h>

//  QSequentialConstIterator::QSequentialConstIterator(QConstIterator<QMetaSe
//      quence> &&it)
extern "C" Q_DECL_EXPORT
QSequentialConstIterator *ritual_ZN24QSequentialConstIteratorC1EO14QConstIteratorI13QMetaSequenceE(
    QConstIterator<QMetaSequence> *it) {
  return new QSequentialConstIterator(std::move(*it));
}

//  QVariant QSequentialConstIterator::operator*() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QSequentialConstIteratordeEv(
    const QSequentialConstIterator *self) {
  return new QVariant(self->operator*());
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
