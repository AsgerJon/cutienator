//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborarray.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qcompare.h>

//  QCborArray::Iterator::Iterator(QCborContainerPrivate *dd, qsizetype ii)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorC1EP21QCborContainerPrivatex(
    QCborContainerPrivate *dd,
    qsizetype ii) {
  return new QCborArray::Iterator(dd, ii);
}

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

//  Iterator &QCborArray::Iterator::operator=(const Iterator &other)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratoraSERKS0_(
    QCborArray::Iterator *self,
    const QCborArray::Iterator *other) {
  return &(self->operator=(*other));
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

//  Iterator &QCborArray::Iterator::operator++()
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorppEv(
    QCborArray::Iterator *self) {
  return &(self->operator++());
}

//  Iterator QCborArray::Iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratorppEi(
    QCborArray::Iterator *self,
    int a0) {
  return new QCborArray::Iterator(self->operator++(a0));
}

//  Iterator &QCborArray::Iterator::operator--()
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratormmEv(
    QCborArray::Iterator *self) {
  return &(self->operator--());
}

//  Iterator QCborArray::Iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::Iterator *ritual_ZN10QCborArray8IteratormmEi(
    QCborArray::Iterator *self,
    int a0) {
  return new QCborArray::Iterator(self->operator--(a0));
}

//  Iterator &QCborArray::Iterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8IteratorpLEx(
    QCborArray::Iterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  Iterator &QCborArray::Iterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8IteratormIEx(
    QCborArray::Iterator *self,
    qsizetype j) {
  self->operator-=(j);
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

//  bool QCborArray::Iterator::comparesEqual_helper(const Iterator &lhs,
//      const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCborArray8Iterator20comparesEqual_helperERKS0_S2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return QCborArray::Iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool QCborArray::Iterator::comparesEqual_helper(const Iterator &lhs,
//      const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCborArray8Iterator20comparesEqual_helperERKS0_RKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return QCborArray::Iterator::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QCborArray::Iterator::compareThreeWay_helper(const
//      Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN10QCborArray8Iterator22compareThreeWay_helperERKS0_S2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return new Qt::strong_ordering(
      QCborArray::Iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  Qt::strong_ordering QCborArray::Iterator::compareThreeWay_helper(const
//      Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN10QCborArray8Iterator22compareThreeWay_helperERKS0_RKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return new Qt::strong_ordering(
      QCborArray::Iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QCborArray8IteratorES2_(
    const QCborArray::Iterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QCborArray8IteratorERKNS_13ConstIteratorE(
    const QCborArray::Iterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QCborArray13ConstIteratorERKNS_8IteratorE(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::Iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QCborArray::Iterator::~Iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8IteratorD1Ev(QCborArray::Iterator *self) {
  delete self;
}
