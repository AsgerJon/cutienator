//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialiterable.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  the ritual of the destructor the compiler writes for the class, which its
//  cute class calls to remove what Python holds, and which the generator no
//  longer writes for it. Kept as it is when the generator runs again.
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

//  QSequentialConstIterator::~QSequentialConstIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSequentialConstIteratorD1Ev(
    QSequentialConstIterator *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
