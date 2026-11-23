//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonvalue.h>

//  QJsonArray::const_iterator::const_iterator()
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratorC1Ev() {
  return new QJsonArray::const_iterator();
}

//  QJsonArray::const_iterator::const_iterator(const QJsonArray *array,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratorC1EPKS_x(
    const QJsonArray *array,
    qsizetype index) {
  return new QJsonArray::const_iterator(array, index);
}

//  QJsonArray::const_iterator::const_iterator(const iterator &o)
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratorC1ERKNS_8iteratorE(
    const QJsonArray::iterator *o) {
  return new QJsonArray::const_iterator(*o);
}

//  QJsonArray::const_iterator::const_iterator(const const_iterator &other)
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratorC1ERKS0_(
    const QJsonArray::const_iterator *other) {
  return new QJsonArray::const_iterator(*other);
}

//  const QJsonValueConstRef QJsonArray::const_iterator::operator*() const
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZNK10QJsonArray14const_iteratordeEv(
    const QJsonArray::const_iterator *self) {
  return new QJsonValueConstRef(self->operator*());
}

//  const QJsonValueConstRef *QJsonArray::const_iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QJsonValueConstRef *ritual_ZNK10QJsonArray14const_iteratorptEv(
    const QJsonArray::const_iterator *self) {
  return self->operator->();
}

//  QJsonValueConstRef QJsonArray::const_iterator::operator[](qsizetype j)
//      const
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZNK10QJsonArray14const_iteratorixEx(
    const QJsonArray::const_iterator *self,
    qsizetype j) {
  return new QJsonValueConstRef(self->operator[](j));
}

//  const_iterator QJsonArray::const_iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratorppEi(
    QJsonArray::const_iterator *self,
    int a0) {
  return new QJsonArray::const_iterator(self->operator++(a0));
}

//  const_iterator QJsonArray::const_iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZN10QJsonArray14const_iteratormmEi(
    QJsonArray::const_iterator *self,
    int a0) {
  return new QJsonArray::const_iterator(self->operator--(a0));
}

//  const_iterator &QJsonArray::const_iterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray14const_iteratorpLEx(
    QJsonArray::const_iterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  const_iterator &QJsonArray::const_iterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray14const_iteratormIEx(
    QJsonArray::const_iterator *self,
    qsizetype j) {
  self->operator-=(j);
}

//  const_iterator QJsonArray::const_iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray14const_iteratorplEx(
    const QJsonArray::const_iterator *self,
    qsizetype j) {
  return new QJsonArray::const_iterator(self->operator+(j));
}

//  const_iterator QJsonArray::const_iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray14const_iteratormiEx(
    const QJsonArray::const_iterator *self,
    qsizetype j) {
  return new QJsonArray::const_iterator(self->operator-(j));
}

//  qsizetype QJsonArray::const_iterator::operator-(const_iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QJsonArray14const_iteratormiES0_(
    const QJsonArray::const_iterator *self,
    const QJsonArray::const_iterator *j) {
  return self->operator-(*j);
}

//  bool QJsonArray::const_iterator::comparesEqual_helper(const
//      const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QJsonArray14const_iterator20comparesEqual_helperERKS0_S2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return QJsonArray::const_iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool operator==(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const const_iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QJsonArray14const_iteratorES2_(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QJsonArray::const_iterator::~const_iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray14const_iteratorD1Ev(
    QJsonArray::const_iterator *self) {
  delete self;
}
