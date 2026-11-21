//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborarray.h>
#include <QtCore/qcborvalue.h>

//  QCborArray::Iterator::Iterator()
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorC1Ev() {
  return new QCborArray::Iterator();
}

//  QCborArray::Iterator::Iterator(const Iterator &a0)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorC1ERKS0_(
    const QCborArray::Iterator *a0) {
  return new QCborArray::Iterator(*a0);
}

//  QCborValueRef QCborArray::Iterator::operator*() const
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZNK10QCborArray8IteratordeEv(
    const QCborArray::Iterator *self) {
  return new QCborValueRef(self->operator*());
}

//  QCborValueRef *QCborArray::Iterator::operator->()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborArray8IteratorptEv(
    QCborArray::Iterator *self) {
  return self->operator->();
}

//  const QCborValueConstRef *QCborArray::Iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QCborValueConstRef *ritual_ZNK10QCborArray8IteratorptEv(
    const QCborArray::Iterator *self) {
  return self->operator->();
}

//  QCborValueRef QCborArray::Iterator::operator[](qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZNK10QCborArray8IteratorixEx(
    const QCborArray::Iterator *self,
    qsizetype j) {
  return new QCborValueRef(self->operator[](j));
}

//  Iterator QCborArray::Iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorppEi(
    QCborArray::Iterator *self,
    int a0) {
  return new QCborArray::Iterator(self->operator++(a0));
}

//  Iterator QCborArray::Iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratormmEi(
    QCborArray::Iterator *self,
    int a0) {
  return new QCborArray::Iterator(self->operator--(a0));
}

//  Iterator QCborArray::Iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZNK10QCborArray8IteratorplEx(
    const QCborArray::Iterator *self,
    qsizetype j) {
  return new QCborArray::Iterator(self->operator+(j));
}

//  Iterator QCborArray::Iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZNK10QCborArray8IteratormiEx(
    const QCborArray::Iterator *self,
    qsizetype j) {
  return new QCborArray::Iterator(self->operator-(j));
}

//  qsizetype QCborArray::Iterator::operator-(Iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QCborArray8IteratormiES0_(
    const QCborArray::Iterator *self,
    const QCborArray::Iterator *j) {
  return self->operator-(*j);
}

//  QCborArray::Iterator::~Iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8IteratorD1Ev(QCborArray::Iterator *self) {
  delete self;
}
