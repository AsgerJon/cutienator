//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qcompare.h>
#include <QtCore/QCborMap>

//  QCborMap::ConstIterator::ConstIterator(QCborValueConstRef it)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorC1E18QCborValueConstRef(
    const QCborValueConstRef *it) {
  return new QCborMap::ConstIterator(*it);
}

//  QCborMap::ConstIterator::ConstIterator(QCborContainerPrivate *dd,
//      qsizetype ii)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorC1EP21QCborContainerPrivatex(
    QCborContainerPrivate *dd,
    qsizetype ii) {
  return new QCborMap::ConstIterator(dd, ii);
}

//  QCborMap::ConstIterator::ConstIterator()
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorC1Ev() {
  return new QCborMap::ConstIterator();
}

//  QCborMap::ConstIterator::ConstIterator(const ConstIterator &a0)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorC1ERKS0_(
    const QCborMap::ConstIterator *a0) {
  return new QCborMap::ConstIterator(*a0);
}

//  QCborMap::ConstIterator::~ConstIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap13ConstIteratorD1Ev(QCborMap::ConstIterator *self) {
  delete self;
}

//  ConstIterator &QCborMap::ConstIterator::operator=(const ConstIterator
//      &other)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratoraSERKS0_(
    QCborMap::ConstIterator *self,
    const QCborMap::ConstIterator *other) {
  return &(self->operator=(*other));
}

//  value_type QCborMap::ConstIterator::operator*() const
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator::value_type *ritual_ZNK8QCborMap13ConstIteratordeEv(
    const QCborMap::ConstIterator *self) {
  return new QCborMap::ConstIterator::value_type(self->operator*());
}

//  value_type QCborMap::ConstIterator::operator[](qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator::value_type *ritual_ZNK8QCborMap13ConstIteratorixEx(
    const QCborMap::ConstIterator *self,
    qsizetype j) {
  return new QCborMap::ConstIterator::value_type(self->operator[](j));
}

//  const QCborValueConstRef *QCborMap::ConstIterator::operator->() const
extern "C" Q_DECL_EXPORT
const QCborValueConstRef *ritual_ZNK8QCborMap13ConstIteratorptEv(
    const QCborMap::ConstIterator *self) {
  return self->operator->();
}

//  QCborValue QCborMap::ConstIterator::key() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap13ConstIterator3keyEv(
    const QCborMap::ConstIterator *self) {
  return new QCborValue(self->key());
}

//  QCborValueConstRef QCborMap::ConstIterator::keyRef() const
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZNK8QCborMap13ConstIterator6keyRefEv(
    const QCborMap::ConstIterator *self) {
  return new QCborValueConstRef(self->keyRef());
}

//  QCborValueConstRef QCborMap::ConstIterator::value() const
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZNK8QCborMap13ConstIterator5valueEv(
    const QCborMap::ConstIterator *self) {
  return new QCborValueConstRef(self->value());
}

//  ConstIterator &QCborMap::ConstIterator::operator++()
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorppEv(
    QCborMap::ConstIterator *self) {
  return &(self->operator++());
}

//  ConstIterator QCborMap::ConstIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratorppEi(
    QCborMap::ConstIterator *self,
    int a0) {
  return new QCborMap::ConstIterator(self->operator++(a0));
}

//  ConstIterator &QCborMap::ConstIterator::operator--()
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratormmEv(
    QCborMap::ConstIterator *self) {
  return &(self->operator--());
}

//  ConstIterator QCborMap::ConstIterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZN8QCborMap13ConstIteratormmEi(
    QCborMap::ConstIterator *self,
    int a0) {
  return new QCborMap::ConstIterator(self->operator--(a0));
}

//  ConstIterator &QCborMap::ConstIterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap13ConstIteratorpLEx(
    QCborMap::ConstIterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  ConstIterator &QCborMap::ConstIterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap13ConstIteratormIEx(
    QCborMap::ConstIterator *self,
    qsizetype j) {
  self->operator-=(j);
}

//  ConstIterator QCborMap::ConstIterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZNK8QCborMap13ConstIteratorplEx(
    const QCborMap::ConstIterator *self,
    qsizetype j) {
  return new QCborMap::ConstIterator(self->operator+(j));
}

//  ConstIterator QCborMap::ConstIterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QCborMap::ConstIterator *ritual_ZNK8QCborMap13ConstIteratormiEx(
    const QCborMap::ConstIterator *self,
    qsizetype j) {
  return new QCborMap::ConstIterator(self->operator-(j));
}

//  qsizetype QCborMap::ConstIterator::operator-(ConstIterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK8QCborMap13ConstIteratormiES0_(
    const QCborMap::ConstIterator *self,
    const QCborMap::ConstIterator *j) {
  return self->operator-(*j);
}

//  bool QCborMap::ConstIterator::comparesEqual_helper(const ConstIterator
//      &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QCborMap13ConstIterator20comparesEqual_helperERKS0_S2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return QCborMap::ConstIterator::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QCborMap::ConstIterator::compareThreeWay_helper(const
//      ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN8QCborMap13ConstIterator22compareThreeWay_helperERKS0_S2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return new Qt::strong_ordering(
      QCborMap::ConstIterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const ConstIterator &lhs, const ConstIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN8QCborMap13ConstIteratorES2_(
    const QCborMap::ConstIterator *lhs,
    const QCborMap::ConstIterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  a QCborMap::ConstIterator::value_type a ritual of QCborMap::ConstIterator
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCborMap_ConstIterator__QCborMap_ConstIterator_value_type(
    QCborMap::ConstIterator::value_type *self) {
  delete self;
}
