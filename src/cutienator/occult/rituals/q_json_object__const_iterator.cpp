//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qjsonvalue.h>

//  QJsonObject::const_iterator::const_iterator()
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratorC1Ev() {
  return new QJsonObject::const_iterator();
}

//  QJsonObject::const_iterator::const_iterator(const QJsonObject *obj,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratorC1EPKS_x(
    const QJsonObject *obj,
    qsizetype index) {
  return new QJsonObject::const_iterator(obj, index);
}

//  QJsonObject::const_iterator::const_iterator(const iterator &other)
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratorC1ERKNS_8iteratorE(
    const QJsonObject::iterator *other) {
  return new QJsonObject::const_iterator(*other);
}

//  QJsonObject::const_iterator::const_iterator(const const_iterator &other)
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratorC1ERKS0_(
    const QJsonObject::const_iterator *other) {
  return new QJsonObject::const_iterator(*other);
}

//  QString QJsonObject::const_iterator::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QJsonObject14const_iterator3keyEv(
    const QJsonObject::const_iterator *self) {
  return new QString(self->key());
}

//  QAnyStringView QJsonObject::const_iterator::keyView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QJsonObject14const_iterator7keyViewEv(
    const QJsonObject::const_iterator *self) {
  return new QString(self->keyView().toString());
}

//  QJsonValueConstRef QJsonObject::const_iterator::value() const
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZNK11QJsonObject14const_iterator5valueEv(
    const QJsonObject::const_iterator *self) {
  return new QJsonValueConstRef(self->value());
}

//  const QJsonValueConstRef QJsonObject::const_iterator::operator*() const
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZNK11QJsonObject14const_iteratordeEv(
    const QJsonObject::const_iterator *self) {
  return new QJsonValueConstRef(self->operator*());
}

//  const QJsonValueConstRef *QJsonObject::const_iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QJsonValueConstRef *ritual_ZNK11QJsonObject14const_iteratorptEv(
    const QJsonObject::const_iterator *self) {
  return self->operator->();
}

//  QJsonValueConstRef QJsonObject::const_iterator::operator[](qsizetype j)
//      const
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZNK11QJsonObject14const_iteratorixEx(
    const QJsonObject::const_iterator *self,
    qsizetype j) {
  return new QJsonValueConstRef(self->operator[](j));
}

//  const_iterator QJsonObject::const_iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratorppEi(
    QJsonObject::const_iterator *self,
    int a0) {
  return new QJsonObject::const_iterator(self->operator++(a0));
}

//  const_iterator QJsonObject::const_iterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZN11QJsonObject14const_iteratormmEi(
    QJsonObject::const_iterator *self,
    int a0) {
  return new QJsonObject::const_iterator(self->operator--(a0));
}

//  const_iterator QJsonObject::const_iterator::operator+(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject14const_iteratorplEx(
    const QJsonObject::const_iterator *self,
    qsizetype j) {
  return new QJsonObject::const_iterator(self->operator+(j));
}

//  const_iterator QJsonObject::const_iterator::operator-(qsizetype j) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject14const_iteratormiEx(
    const QJsonObject::const_iterator *self,
    qsizetype j) {
  return new QJsonObject::const_iterator(self->operator-(j));
}

//  qsizetype QJsonObject::const_iterator::operator-(const_iterator j) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QJsonObject14const_iteratormiES0_(
    const QJsonObject::const_iterator *self,
    const QJsonObject::const_iterator *j) {
  return self->operator-(*j);
}

//  QJsonObject::const_iterator::~const_iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject14const_iteratorD1Ev(
    QJsonObject::const_iterator *self) {
  delete self;
}
