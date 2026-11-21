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

//  QJsonArray::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonArray8iteratorD1Ev(QJsonArray::iterator *self) {
  delete self;
}
