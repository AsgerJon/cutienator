//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonvalue_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsonvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QJsonValue>

//  QBinaryJsonValue::QBinaryJsonValue(QJsonValue::Type type)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1EN10QJsonValue4TypeE(
    QJsonValue::Type type) {
  return new QBinaryJsonValue(type);
}

//  QBinaryJsonValue::QBinaryJsonValue(bool b)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1Eb(bool b) {
  return new QBinaryJsonValue(b);
}

//  QBinaryJsonValue::QBinaryJsonValue(double n)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1Ed(double n) {
  return new QBinaryJsonValue(n);
}

//  QBinaryJsonValue::QBinaryJsonValue(QString s)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1E7QString(const QString *s) {
  return new QBinaryJsonValue(*s);
}

//  QBinaryJsonValue::QBinaryJsonValue(const QBinaryJsonArray &a)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1ERK16QBinaryJsonArray(
    const QBinaryJsonArray *a) {
  return new QBinaryJsonValue(*a);
}

//  QBinaryJsonValue::QBinaryJsonValue(const QBinaryJsonObject &o)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1ERK17QBinaryJsonObject(
    const QBinaryJsonObject *o) {
  return new QBinaryJsonValue(*o);
}

//  QBinaryJsonValue::~QBinaryJsonValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBinaryJsonValueD1Ev(QBinaryJsonValue *self) {
  delete self;
}

//  QBinaryJsonValue::QBinaryJsonValue(QBinaryJsonValue &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1EOS_(
    QBinaryJsonValue *other) {
  return new QBinaryJsonValue(std::move(*other));
}

//  QBinaryJsonValue &QBinaryJsonValue::operator=(QBinaryJsonValue &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueaSEOS_(
    QBinaryJsonValue *self,
    QBinaryJsonValue *other) {
  return &(self->operator=(std::move(*other)));
}

//  QBinaryJsonValue QBinaryJsonValue::fromJsonValue(const QJsonValue &json)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValue13fromJsonValueERK10QJsonValue(
    const QJsonValue *json) {
  return new QBinaryJsonValue(QBinaryJsonValue::fromJsonValue(*json));
}

//  QJsonValue::Type QBinaryJsonValue::type() const
extern "C" Q_DECL_EXPORT
QJsonValue::Type ritual_ZNK16QBinaryJsonValue4typeEv(
    const QBinaryJsonValue *self) {
  return self->type();
}

//  bool QBinaryJsonValue::toBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QBinaryJsonValue6toBoolEv(const QBinaryJsonValue *self) {
  return self->toBool();
}

//  double QBinaryJsonValue::toDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QBinaryJsonValue8toDoubleEv(
    const QBinaryJsonValue *self) {
  return self->toDouble();
}

//  QString QBinaryJsonValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBinaryJsonValue8toStringEv(
    const QBinaryJsonValue *self) {
  return new QString(self->toString());
}

//  QBinaryJsonValue::QBinaryJsonValue(QBinaryJsonPrivate::MutableData *d,
//      QBinaryJsonPrivate::Base *parent, const QBinaryJsonPrivate::Value &v)
extern "C" Q_DECL_EXPORT
QBinaryJsonValue *ritual_ZN16QBinaryJsonValueC1EPN18QBinaryJsonPrivate11MutableDataEPNS0_4BaseERKNS0_5ValueE(
    QBinaryJsonPrivate::MutableData *d,
    QBinaryJsonPrivate::Base *parent,
    const QBinaryJsonPrivate::Value *v) {
  return new QBinaryJsonValue(d, parent, *v);
}

//  a QBinaryJsonValue a ritual of QBinaryJsonValue gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBinaryJsonValue__QBinaryJsonValue(QBinaryJsonValue *self) {
  delete self;
}
