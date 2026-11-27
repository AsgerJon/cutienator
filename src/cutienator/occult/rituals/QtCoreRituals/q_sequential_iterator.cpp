//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialiterable.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  the ritual of the destructor the compiler writes for the class, which its
//  cute class calls to remove what Python holds, and which the generator no
//  longer writes for it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qsequentialiterable.h>
#include <QtCore/QSequentialIterator>

//  QSequentialIterator::QSequentialIterator(QIterator<QMetaSequence> &&it)
extern "C" Q_DECL_EXPORT
QSequentialIterator *ritual_ZN19QSequentialIteratorC1EO9QIteratorI13QMetaSequenceE(
    QIterator<QMetaSequence> *it) {
  return new QSequentialIterator(std::move(*it));
}

//  QVariantRef<QSequentialIterator> QSequentialIterator::operator*() const
extern "C" Q_DECL_EXPORT
QVariantRef<QSequentialIterator> *ritual_ZNK19QSequentialIteratordeEv(
    const QSequentialIterator *self) {
  return new QVariantRef<QSequentialIterator>(self->operator*());
}

//  QVariantPointer<QSequentialIterator> QSequentialIterator::operator->()
//      const
extern "C" Q_DECL_EXPORT
QVariantPointer<QSequentialIterator> *ritual_ZNK19QSequentialIteratorptEv(
    const QSequentialIterator *self) {
  return new QVariantPointer<QSequentialIterator>(self->operator->());
}

//  a QVariantRef<QSequentialIterator> a ritual of QSequentialIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSequentialIterator__QVariantRef_QSequentialIterator(
    QVariantRef<QSequentialIterator> *self) {
  delete self;
}

//  a QVariantPointer<QSequentialIterator> a ritual of QSequentialIterator
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSequentialIterator__QVariantPointer_QSequentialIterator(
    QVariantPointer<QSequentialIterator> *self) {
  delete self;
}

//  QSequentialIterator::~QSequentialIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIteratorD1Ev(QSequentialIterator *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
