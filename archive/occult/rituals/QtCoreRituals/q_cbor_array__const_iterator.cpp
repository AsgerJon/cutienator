//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborarray.h>
#include <QtCore/qcborvalue.h>

//  QCborArray::ConstIterator::ConstIterator()
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZN10QCborArray13ConstIteratorC1Ev() {
  return new QCborArray::ConstIterator();
}

//  QCborArray::ConstIterator::ConstIterator(const ConstIterator &a0)
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZN10QCborArray13ConstIteratorC1ERKS0_(
    const QCborArray::ConstIterator *a0) {
  return new QCborArray::ConstIterator(*a0);
}

//  QCborValueConstRef QCborArray::ConstIterator::operator*() const
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZNK10QCborArray13ConstIteratordeEv(
    const QCborArray::ConstIterator *self) {
  return new QCborValueConstRef(self->operator*());
}

//  const QCborValueConstRef *QCborArray::ConstIterator::operator->() const
extern "C" Q_DECL_EXPORT
const QCborValueConstRef *ritual_ZNK10QCborArray13ConstIteratorptEv(
    const QCborArray::ConstIterator *self) {
  return self->operator->();
}

//  QCborValueConstRef QCborArray::ConstIterator::operator[](qsizetype j)
//      const
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZNK10QCborArray13ConstIteratorixEx(
    const QCborArray::ConstIterator *self,
    qsizetype j) {
  return new QCborValueConstRef(self->operator[](j));
}

//  ConstIterator QCborArray::ConstIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZN10QCborArray13ConstIteratorppEi(
    QCborArray::ConstIterator *self,
    int a0) {
  return new QCborArray::ConstIterator(self->operator++(a0));
}

//  ConstIterator QCborArray::ConstIterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZN10QCborArray13ConstIteratormmEi(
    QCborArray::ConstIterator *self,
    int a0) {
  return new QCborArray::ConstIterator(self->operator--(a0));
}

//  ConstIterator &QCborArray::ConstIterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray13ConstIteratorpLEx(
    QCborArray::ConstIterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  ConstIterator &QCborArray::ConstIterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray13ConstIteratormIEx(
    QCborArray::ConstIterator *self,
    qsizetype j) {
  self->operator-=(j);
}

//  ConstIterator QCborArray::ConstIterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZNK10QCborArray13ConstIteratorplEx(
    const QCborArray::ConstIterator *self,
    qsizetype j) {
  return new QCborArray::ConstIterator(self->operator+(j));
}

//  ConstIterator QCborArray::ConstIterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborArray::ConstIterator *ritual_ZNK10QCborArray13ConstIteratormiEx(
    const QCborArray::ConstIterator *self,
    qsizetype j) {
  return new QCborArray::ConstIterator(self->operator-(j));
}

//  qsizetype QCborArray::ConstIterator::operator-(ConstIterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QCborArray13ConstIteratormiES0_(
    const QCborArray::ConstIterator *self,
    const QCborArray::ConstIterator *j) {
  return self->operator-(*j);
}

//  bool QCborArray::ConstIterator::comparesEqual_helper(const ConstIterator
//      &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCborArray13ConstIterator20comparesEqual_helperERKS0_S2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return QCborArray::ConstIterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool operator==(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QCborArray13ConstIteratorES2_(
    const QCborArray::ConstIterator *lhs,
    const QCborArray::ConstIterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QCborArray::ConstIterator::~ConstIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray13ConstIteratorD1Ev(
    QCborArray::ConstIterator *self) {
  delete self;
}
