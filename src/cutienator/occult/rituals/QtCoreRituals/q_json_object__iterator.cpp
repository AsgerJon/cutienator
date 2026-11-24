//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qcompare.h>

//  QJsonObject::iterator::iterator()
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject8iteratorC1Ev() {
  return new QJsonObject::iterator();
}

//  QJsonObject::iterator::iterator(QJsonObject *obj, qsizetype index)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject8iteratorC1EPS_x(
    QJsonObject *obj,
    qsizetype index) {
  return new QJsonObject::iterator(obj, index);
}

//  QJsonObject::iterator::iterator(const iterator &other)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject8iteratorC1ERKS0_(
    const QJsonObject::iterator *other) {
  return new QJsonObject::iterator(*other);
}

//  QString QJsonObject::iterator::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QJsonObject8iterator3keyEv(
    const QJsonObject::iterator *self) {
  return new QString(self->key());
}

//  QAnyStringView QJsonObject::iterator::keyView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QJsonObject8iterator7keyViewEv(
    const QJsonObject::iterator *self) {
  return new QString(self->keyView().toString());
}

//  QJsonValueRef QJsonObject::iterator::value() const
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZNK11QJsonObject8iterator5valueEv(
    const QJsonObject::iterator *self) {
  return new QJsonValueRef(self->value());
}

//  QJsonValueRef QJsonObject::iterator::operator*() const
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZNK11QJsonObject8iteratordeEv(
    const QJsonObject::iterator *self) {
  return new QJsonValueRef(self->operator*());
}

//  const QJsonValueConstRef *QJsonObject::iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QJsonValueConstRef *ritual_ZNK11QJsonObject8iteratorptEv(
    const QJsonObject::iterator *self) {
  return self->operator->();
}

//  QJsonValueRef *QJsonObject::iterator::operator->()
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN11QJsonObject8iteratorptEv(
    QJsonObject::iterator *self) {
  return self->operator->();
}

//  QJsonValueRef QJsonObject::iterator::operator[](qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZNK11QJsonObject8iteratorixEx(
    const QJsonObject::iterator *self,
    qsizetype j) {
  return new QJsonValueRef(self->operator[](j));
}

//  iterator QJsonObject::iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject8iteratorppEi(
    QJsonObject::iterator *self,
    int a0) {
  return new QJsonObject::iterator(self->operator++(a0));
}

//  iterator QJsonObject::iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject8iteratormmEi(
    QJsonObject::iterator *self,
    int a0) {
  return new QJsonObject::iterator(self->operator--(a0));
}

//  iterator QJsonObject::iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZNK11QJsonObject8iteratorplEx(
    const QJsonObject::iterator *self,
    qsizetype j) {
  return new QJsonObject::iterator(self->operator+(j));
}

//  iterator QJsonObject::iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZNK11QJsonObject8iteratormiEx(
    const QJsonObject::iterator *self,
    qsizetype j) {
  return new QJsonObject::iterator(self->operator-(j));
}

//  iterator &QJsonObject::iterator::operator+=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject8iteratorpLEx(
    QJsonObject::iterator *self,
    qsizetype j) {
  self->operator+=(j);
}

//  iterator &QJsonObject::iterator::operator-=(qsizetype j)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject8iteratormIEx(
    QJsonObject::iterator *self,
    qsizetype j) {
  self->operator-=(j);
}

//  qsizetype QJsonObject::iterator::operator-(iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QJsonObject8iteratormiES0_(
    const QJsonObject::iterator *self,
    const QJsonObject::iterator *j) {
  return self->operator-(*j);
}

//  bool QJsonObject::iterator::comparesEqual_helper(const iterator &lhs,
//      const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QJsonObject8iterator20comparesEqual_helperERKS0_S2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return QJsonObject::iterator::comparesEqual_helper(*lhs, *rhs);
}

//  bool QJsonObject::iterator::comparesEqual_helper(const iterator &lhs,
//      const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QJsonObject8iterator20comparesEqual_helperERKS0_RKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return QJsonObject::iterator::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QJsonObject::iterator::compareThreeWay_helper(const
//      iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN11QJsonObject8iterator22compareThreeWay_helperERKS0_S2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return new Qt::strong_ordering(
      QJsonObject::iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  Qt::strong_ordering QJsonObject::iterator::compareThreeWay_helper(const
//      iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN11QJsonObject8iterator22compareThreeWay_helperERKS0_RKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return new Qt::strong_ordering(
      QJsonObject::iterator::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN11QJsonObject8iteratorES2_(
    const QJsonObject::iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const iterator &lhs, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN11QJsonObject8iteratorERKNS_14const_iteratorE(
    const QJsonObject::iterator *lhs,
    const QJsonObject::const_iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const const_iterator &lhs, const iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN11QJsonObject14const_iteratorERKNS_8iteratorE(
    const QJsonObject::const_iterator *lhs,
    const QJsonObject::iterator *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QJsonObject::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject8iteratorD1Ev(QJsonObject::iterator *self) {
  delete self;
}
