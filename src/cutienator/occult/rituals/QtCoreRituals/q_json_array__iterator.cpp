//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonvalue.h>

//  QJsonArray::iterator::iterator()
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray8iteratorC1Ev() {
  return new QJsonArray::iterator();
}

//  QJsonArray::iterator::iterator(QJsonArray *array, qsizetype index)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray8iteratorC1EPS_x(
    QJsonArray *array,
    qsizetype index) {
  return new QJsonArray::iterator(array, index);
}

//  QJsonArray::iterator::iterator(const iterator &other)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray8iteratorC1ERKS0_(
    const QJsonArray::iterator *other) {
  return new QJsonArray::iterator(*other);
}

//  QJsonValueRef QJsonArray::iterator::operator*() const
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZNK10QJsonArray8iteratordeEv(
    const QJsonArray::iterator *self) {
  return new QJsonValueRef(self->operator*());
}

//  const QJsonValueConstRef *QJsonArray::iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QJsonValueConstRef *ritual_ZNK10QJsonArray8iteratorptEv(
    const QJsonArray::iterator *self) {
  return self->operator->();
}

//  QJsonValueRef *QJsonArray::iterator::operator->()
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN10QJsonArray8iteratorptEv(
    QJsonArray::iterator *self) {
  return self->operator->();
}

//  QJsonValueRef QJsonArray::iterator::operator[](qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZNK10QJsonArray8iteratorixEx(
    const QJsonArray::iterator *self,
    qsizetype j) {
  return new QJsonValueRef(self->operator[](j));
}

//  iterator QJsonArray::iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray8iteratorppEi(
    QJsonArray::iterator *self,
    int a0) {
  return new QJsonArray::iterator(self->operator++(a0));
}

//  iterator QJsonArray::iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray8iteratormmEi(
    QJsonArray::iterator *self,
    int a0) {
  return new QJsonArray::iterator(self->operator--(a0));
}

//  iterator &QJsonArray::iterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8iteratorpLEx(
    QJsonArray::iterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  iterator &QJsonArray::iterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8iteratormIEx(
    QJsonArray::iterator *self,
    qsizetype j) {
  self->operator-=(j);
}

//  iterator QJsonArray::iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZNK10QJsonArray8iteratorplEx(
    const QJsonArray::iterator *self,
    qsizetype j) {
  return new QJsonArray::iterator(self->operator+(j));
}

//  iterator QJsonArray::iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZNK10QJsonArray8iteratormiEx(
    const QJsonArray::iterator *self,
    qsizetype j) {
  return new QJsonArray::iterator(self->operator-(j));
}

//  qsizetype QJsonArray::iterator::operator-(iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QJsonArray8iteratormiES0_(
    const QJsonArray::iterator *self,
    const QJsonArray::iterator *j) {
  return self->operator-(*j);
}

//  bool QJsonArray::iterator::comparesEqual_helper(const iterator &lhs,
//      const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QJsonArray8iterator20comparesEqual_helperERKS0_S2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return QJsonArray::iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool QJsonArray::iterator::comparesEqual_helper(const iterator &lhs,
//      const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QJsonArray8iterator20comparesEqual_helperERKS0_RKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return QJsonArray::iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool operator==(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QJsonArray8iteratorES2_(
    const QJsonArray::iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QJsonArray8iteratorERKNS_14const_iteratorE(
    const QJsonArray::iterator *lhs,
    const QJsonArray::const_iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN10QJsonArray14const_iteratorERKNS_8iteratorE(
    const QJsonArray::const_iterator *lhs,
    const QJsonArray::iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QJsonArray::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8iteratorD1Ev(QJsonArray::iterator *self) {
  delete self;
}
