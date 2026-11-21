//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>

//  QCborMap::Iterator::Iterator()
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZN8QCborMap8IteratorC1Ev() {
  return new QCborMap::Iterator();
}

//  QCborMap::Iterator::Iterator(const Iterator &a0)
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZN8QCborMap8IteratorC1ERKS0_(
    const QCborMap::Iterator *a0) {
  return new QCborMap::Iterator(*a0);
}

//  QCborMap::Iterator::~Iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap8IteratorD1Ev(QCborMap::Iterator *self) {
  delete self;
}

//  QCborValueRef *QCborMap::Iterator::operator->()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN8QCborMap8IteratorptEv(QCborMap::Iterator *self) {
  return self->operator->();
}

//  const QCborValueConstRef *QCborMap::Iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QCborValueConstRef *ritual_ZNK8QCborMap8IteratorptEv(
    const QCborMap::Iterator *self) {
  return self->operator->();
}

//  QCborValue QCborMap::Iterator::key() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap8Iterator3keyEv(
    const QCborMap::Iterator *self) {
  return new QCborValue(self->key());
}

//  QCborValueConstRef QCborMap::Iterator::keyRef() const
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZNK8QCborMap8Iterator6keyRefEv(
    const QCborMap::Iterator *self) {
  return new QCborValueConstRef(self->keyRef());
}

//  QCborValueRef QCborMap::Iterator::value() const
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZNK8QCborMap8Iterator5valueEv(
    const QCborMap::Iterator *self) {
  return new QCborValueRef(self->value());
}

//  Iterator QCborMap::Iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZN8QCborMap8IteratorppEi(
    QCborMap::Iterator *self,
    int a0) {
  return new QCborMap::Iterator(self->operator++(a0));
}

//  Iterator QCborMap::Iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZN8QCborMap8IteratormmEi(
    QCborMap::Iterator *self,
    int a0) {
  return new QCborMap::Iterator(self->operator--(a0));
}

//  Iterator QCborMap::Iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZNK8QCborMap8IteratorplEx(
    const QCborMap::Iterator *self,
    qsizetype j) {
  return new QCborMap::Iterator(self->operator+(j));
}

//  Iterator QCborMap::Iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborMap::Iterator *ritual_ZNK8QCborMap8IteratormiEx(
    const QCborMap::Iterator *self,
    qsizetype j) {
  return new QCborMap::Iterator(self->operator-(j));
}

//  qsizetype QCborMap::Iterator::operator-(Iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK8QCborMap8IteratormiES0_(
    const QCborMap::Iterator *self,
    const QCborMap::Iterator *j) {
  return self->operator-(*j);
}
