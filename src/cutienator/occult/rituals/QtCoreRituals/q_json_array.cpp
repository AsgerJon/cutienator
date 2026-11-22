//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonarray.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QJsonArray::QJsonArray()
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN10QJsonArrayC1Ev() {
  return new QJsonArray();
}

//  QJsonArray::~QJsonArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArrayD1Ev(QJsonArray *self) {
  delete self;
}

//  QJsonArray::QJsonArray(const QJsonArray &other)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN10QJsonArrayC1ERKS_(const QJsonArray *other) {
  return new QJsonArray(*other);
}

//  QJsonArray QJsonArray::fromStringList(const QStringList &list)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN10QJsonArray14fromStringListERK5QListI7QStringE(
    const QList<QString> *list) {
  return new QJsonArray(QJsonArray::fromStringList(*list));
}

//  QJsonArray QJsonArray::fromVariantList(const QVariantList &list)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN10QJsonArray15fromVariantListERK5QListI8QVariantE(
    const QList<QVariant> *list) {
  return new QJsonArray(QJsonArray::fromVariantList(*list));
}

//  QVariantList QJsonArray::toVariantList() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK10QJsonArray13toVariantListEv(
    const QJsonArray *self) {
  return new QList<QVariant>(self->toVariantList());
}

//  qsizetype QJsonArray::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QJsonArray4sizeEv(const QJsonArray *self) {
  return self->size();
}

//  qsizetype QJsonArray::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QJsonArray5countEv(const QJsonArray *self) {
  return self->count();
}

//  bool QJsonArray::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonArray7isEmptyEv(const QJsonArray *self) {
  return self->isEmpty();
}

//  QJsonValue QJsonArray::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonArray2atEx(
    const QJsonArray *self,
    qsizetype i) {
  return new QJsonValue(self->at(i));
}

//  QJsonValue QJsonArray::first() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonArray5firstEv(const QJsonArray *self) {
  return new QJsonValue(self->first());
}

//  QJsonValue QJsonArray::last() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonArray4lastEv(const QJsonArray *self) {
  return new QJsonValue(self->last());
}

//  void QJsonArray::prepend(const QJsonValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray7prependERK10QJsonValue(
    QJsonArray *self,
    const QJsonValue *value) {
  self->prepend(*value);
}

//  void QJsonArray::append(const QJsonValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray6appendERK10QJsonValue(
    QJsonArray *self,
    const QJsonValue *value) {
  self->append(*value);
}

//  void QJsonArray::removeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8removeAtEx(QJsonArray *self, qsizetype i) {
  self->removeAt(i);
}

//  QJsonValue QJsonArray::takeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonArray6takeAtEx(QJsonArray *self, qsizetype i) {
  return new QJsonValue(self->takeAt(i));
}

//  void QJsonArray::removeFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray11removeFirstEv(QJsonArray *self) {
  self->removeFirst();
}

//  void QJsonArray::removeLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray10removeLastEv(QJsonArray *self) {
  self->removeLast();
}

//  void QJsonArray::insert(qsizetype i, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray6insertExRK10QJsonValue(
    QJsonArray *self,
    qsizetype i,
    const QJsonValue *value) {
  self->insert(i, *value);
}

//  void QJsonArray::replace(qsizetype i, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray7replaceExRK10QJsonValue(
    QJsonArray *self,
    qsizetype i,
    const QJsonValue *value) {
  self->replace(i, *value);
}

//  bool QJsonArray::contains(const QJsonValue &element) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonArray8containsERK10QJsonValue(
    const QJsonArray *self,
    const QJsonValue *element) {
  return self->contains(*element);
}

//  QJsonValueRef QJsonArray::operator[](qsizetype i)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN10QJsonArrayixEx(QJsonArray *self, qsizetype i) {
  return new QJsonValueRef(self->operator[](i));
}

//  QJsonValue QJsonArray::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonArrayixEx(const QJsonArray *self, qsizetype i) {
  return new QJsonValue(self->operator[](i));
}

//  iterator QJsonArray::begin()
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray5beginEv(QJsonArray *self) {
  return new QJsonArray::iterator(self->begin());
}

//  const_iterator QJsonArray::begin() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray5beginEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->begin());
}

//  const_iterator QJsonArray::constBegin() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray10constBeginEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->constBegin());
}

//  const_iterator QJsonArray::cbegin() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray6cbeginEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->cbegin());
}

//  iterator QJsonArray::end()
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray3endEv(QJsonArray *self) {
  return new QJsonArray::iterator(self->end());
}

//  const_iterator QJsonArray::end() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray3endEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->end());
}

//  const_iterator QJsonArray::constEnd() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray8constEndEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->constEnd());
}

//  const_iterator QJsonArray::cend() const
extern "C" Q_DECL_EXPORT
QJsonArray::const_iterator *ritual_ZNK10QJsonArray4cendEv(
    const QJsonArray *self) {
  return new QJsonArray::const_iterator(self->cend());
}

//  iterator QJsonArray::insert(iterator before, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray6insertENS_8iteratorERK10QJsonValue(
    QJsonArray *self,
    const QJsonArray::iterator *before,
    const QJsonValue *value) {
  return new QJsonArray::iterator(self->insert(*before, *value));
}

//  iterator QJsonArray::erase(iterator it)
extern "C" Q_DECL_EXPORT
QJsonArray::iterator *ritual_ZN10QJsonArray5eraseENS_8iteratorE(
    QJsonArray *self,
    const QJsonArray::iterator *it) {
  return new QJsonArray::iterator(self->erase(*it));
}

//  QJsonArray QJsonArray::operator+(const QJsonValue &v) const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK10QJsonArrayplERK10QJsonValue(
    const QJsonArray *self,
    const QJsonValue *v) {
  return new QJsonArray(self->operator+(*v));
}

//  QJsonArray &QJsonArray::operator+=(const QJsonValue &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArraypLERK10QJsonValue(
    QJsonArray *self,
    const QJsonValue *v) {
  self->operator+=(*v);
}

//  void QJsonArray::push_back(const QJsonValue &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray9push_backERK10QJsonValue(
    QJsonArray *self,
    const QJsonValue *t) {
  self->push_back(*t);
}

//  void QJsonArray::push_front(const QJsonValue &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray10push_frontERK10QJsonValue(
    QJsonArray *self,
    const QJsonValue *t) {
  self->push_front(*t);
}

//  void QJsonArray::pop_front()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray9pop_frontEv(QJsonArray *self) {
  self->pop_front();
}

//  void QJsonArray::pop_back()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8pop_backEv(QJsonArray *self) {
  self->pop_back();
}

//  bool QJsonArray::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonArray5emptyEv(const QJsonArray *self) {
  return self->empty();
}

//  QDebug operator<<(QDebug a0, const QJsonArray &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK10QJsonArray(
    const QDebug *a0,
    const QJsonArray *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  bool operator==(const QJsonArray &lhs, const QJsonArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonArrayS1_(
    const QJsonArray *lhs,
    const QJsonArray *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonArray &lhs, const QJsonArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonArrayS1_(
    const QJsonArray *lhs,
    const QJsonArray *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonArray &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonArrayRK10QJsonValue(
    const QJsonArray *lhs,
    const QJsonValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonArray &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonArrayRK10QJsonValue(
    const QJsonArray *lhs,
    const QJsonValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonValue &lhs, const QJsonArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonValueRK10QJsonArray(
    const QJsonValue *lhs,
    const QJsonArray *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValue &lhs, const QJsonArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonValueRK10QJsonArray(
    const QJsonValue *lhs,
    const QJsonArray *rhs) {
  return operator!=(*lhs, *rhs);
}
