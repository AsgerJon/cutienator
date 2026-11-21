//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborarray.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qjsonarray.h>

//  QCborArray::QCborArray()
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZN10QCborArrayC1Ev() {
  return new QCborArray();
}

//  QCborArray::QCborArray(const QCborArray &other)
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZN10QCborArrayC1ERKS_(const QCborArray *other) {
  return new QCborArray(*other);
}

//  QCborArray::~QCborArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArrayD1Ev(QCborArray *self) {
  delete self;
}

//  QCborValue QCborArray::toCborValue() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborArray11toCborValueEv(const QCborArray *self) {
  return new QCborValue(self->toCborValue());
}

//  qsizetype QCborArray::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QCborArray4sizeEv(const QCborArray *self) {
  return self->size();
}

//  bool QCborArray::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborArray7isEmptyEv(const QCborArray *self) {
  return self->isEmpty();
}

//  void QCborArray::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray5clearEv(QCborArray *self) {
  self->clear();
}

//  QCborValue QCborArray::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborArray2atEx(
    const QCborArray *self,
    qsizetype i) {
  return new QCborValue(self->at(i));
}

//  QCborValue QCborArray::first() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborArray5firstEv(const QCborArray *self) {
  return new QCborValue(self->first());
}

//  QCborValue QCborArray::last() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborArray4lastEv(const QCborArray *self) {
  return new QCborValue(self->last());
}

//  const QCborValue QCborArray::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborArrayixEx(const QCborArray *self, qsizetype i) {
  return new QCborValue(self->operator[](i));
}

//  QCborValueRef QCborArray::first()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborArray5firstEv(QCborArray *self) {
  return new QCborValueRef(self->first());
}

//  QCborValueRef QCborArray::last()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborArray4lastEv(QCborArray *self) {
  return new QCborValueRef(self->last());
}

//  QCborValueRef QCborArray::operator[](qsizetype i)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborArrayixEx(QCborArray *self, qsizetype i) {
  return new QCborValueRef(self->operator[](i));
}

//  void QCborArray::insert(qsizetype i, const QCborValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray6insertExRK10QCborValue(
    QCborArray *self,
    qsizetype i,
    const QCborValue *value) {
  self->insert(i, *value);
}

//  void QCborArray::prepend(const QCborValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray7prependERK10QCborValue(
    QCborArray *self,
    const QCborValue *value) {
  self->prepend(*value);
}

//  void QCborArray::append(const QCborValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray6appendERK10QCborValue(
    QCborArray *self,
    const QCborValue *value) {
  self->append(*value);
}

//  QCborValue QCborArray::extract(ConstIterator it)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborArray7extractENS_13ConstIteratorE(
    QCborArray *self,
    const QCborArray::ConstIterator *it) {
  return new QCborValue(self->extract(*it));
}

//  QCborValue QCborArray::extract(Iterator it)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborArray7extractENS_8IteratorE(
    QCborArray *self,
    const QCborArray::Iterator *it) {
  return new QCborValue(self->extract(*it));
}

//  void QCborArray::removeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8removeAtEx(QCborArray *self, qsizetype i) {
  self->removeAt(i);
}

//  QCborValue QCborArray::takeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborArray6takeAtEx(QCborArray *self, qsizetype i) {
  return new QCborValue(self->takeAt(i));
}

//  void QCborArray::removeFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray11removeFirstEv(QCborArray *self) {
  self->removeFirst();
}

//  void QCborArray::removeLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray10removeLastEv(QCborArray *self) {
  self->removeLast();
}

//  QCborValue QCborArray::takeFirst()
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborArray9takeFirstEv(QCborArray *self) {
  return new QCborValue(self->takeFirst());
}

//  QCborValue QCborArray::takeLast()
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborArray8takeLastEv(QCborArray *self) {
  return new QCborValue(self->takeLast());
}

//  bool QCborArray::contains(const QCborValue &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborArray8containsERK10QCborValue(
    const QCborArray *self,
    const QCborValue *value) {
  return self->contains(*value);
}

//  int QCborArray::compare(const QCborArray &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCborArray7compareERKS_(
    const QCborArray *self,
    const QCborArray *other) {
  return self->compare(*other);
}

//  void QCborArray::push_back(const QCborValue &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray9push_backERK10QCborValue(
    QCborArray *self,
    const QCborValue *t) {
  self->push_back(*t);
}

//  void QCborArray::push_front(const QCborValue &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray10push_frontERK10QCborValue(
    QCborArray *self,
    const QCborValue *t) {
  self->push_front(*t);
}

//  void QCborArray::pop_front()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray9pop_frontEv(QCborArray *self) {
  self->pop_front();
}

//  void QCborArray::pop_back()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborArray8pop_backEv(QCborArray *self) {
  self->pop_back();
}

//  bool QCborArray::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborArray5emptyEv(const QCborArray *self) {
  return self->empty();
}

//  QCborArray QCborArray::operator+(const QCborValue &v) const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK10QCborArrayplERK10QCborValue(
    const QCborArray *self,
    const QCborValue *v) {
  return new QCborArray(self->operator+(*v));
}

//  QCborArray QCborArray::fromJsonArray(const QJsonArray &array)
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZN10QCborArray13fromJsonArrayERK10QJsonArray(
    const QJsonArray *array) {
  return new QCborArray(QCborArray::fromJsonArray(*array));
}

//  QJsonArray QCborArray::toJsonArray() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK10QCborArray11toJsonArrayEv(const QCborArray *self) {
  return new QJsonArray(self->toJsonArray());
}
