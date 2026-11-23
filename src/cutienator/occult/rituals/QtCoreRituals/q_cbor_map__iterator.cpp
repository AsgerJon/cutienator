//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qcompare.h>

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

//  Iterator &QCborMap::Iterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap8IteratorpLEx(QCborMap::Iterator *self, qsizetype j) {
  self->operator+=(j);
}

//  Iterator &QCborMap::Iterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap8IteratormIEx(QCborMap::Iterator *self, qsizetype j) {
  self->operator-=(j);
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

//  bool QCborMap::Iterator::comparesEqual_helper(const Iterator &lhs, const
//      Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QCborMap8Iterator20comparesEqual_helperERKS0_S2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return QCborMap::Iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool QCborMap::Iterator::comparesEqual_helper(const Iterator &lhs, const
//      ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QCborMap8Iterator20comparesEqual_helperERKS0_RKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return QCborMap::Iterator::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QCborMap::Iterator::compareThreeWay_helper(const
//      Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN8QCborMap8Iterator22compareThreeWay_helperERKS0_S2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return new Qt::strong_ordering(
      QCborMap::Iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  Qt::strong_ordering QCborMap::Iterator::compareThreeWay_helper(const
//      Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN8QCborMap8Iterator22compareThreeWay_helperERKS0_RKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return new Qt::strong_ordering(
      QCborMap::Iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const Iterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN8QCborMap8IteratorES2_(
    const QCborMap::Iterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const Iterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN8QCborMap8IteratorERKNS_13ConstIteratorE(
    const QCborMap::Iterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const ConstIterator &lhs, const Iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN8QCborMap13ConstIteratorERKNS_8IteratorE(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::Iterator *rhs) {
  return operator>=(*lhs, *rhs);
}
