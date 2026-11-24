//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qjson_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcborvalue.h>
#include <QtCore/qjsonvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcborvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qint64 QJsonPrivate::Value::valueHelper(const QCborValue &v)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QJsonPrivate5Value11valueHelperERK10QCborValue(
    const QCborValue *v) {
  return QJsonPrivate::Value::valueHelper(*v);
}

//  QCborContainerPrivate *QJsonPrivate::Value::container(const QCborValue
//      &v)
extern "C" Q_DECL_EXPORT
QCborContainerPrivate *ritual_ZN12QJsonPrivate5Value9containerERK10QCborValue(
    const QCborValue *v) {
  return QJsonPrivate::Value::container(*v);
}

//  const QCborContainerPrivate
//      *QJsonPrivate::Value::container(QJsonValueConstRef r)
extern "C" Q_DECL_EXPORT
const QCborContainerPrivate *ritual_ZN12QJsonPrivate5Value9containerE18QJsonValueConstRef(
    const QJsonValueConstRef *r) {
  return QJsonPrivate::Value::container(*r);
}

//  QCborContainerPrivate *QJsonPrivate::Value::container(QJsonValueRef r)
extern "C" Q_DECL_EXPORT
QCborContainerPrivate *ritual_ZN12QJsonPrivate5Value9containerE13QJsonValueRef(
    const QJsonValueRef *r) {
  return QJsonPrivate::Value::container(*r);
}

//  qsizetype QJsonPrivate::Value::indexHelper(QJsonValueConstRef r)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN12QJsonPrivate5Value11indexHelperE18QJsonValueConstRef(
    const QJsonValueConstRef *r) {
  return QJsonPrivate::Value::indexHelper(*r);
}

//  const QtCbor::Element
//      &QJsonPrivate::Value::elementHelper(QJsonValueConstRef r)
extern "C" Q_DECL_EXPORT
QtCbor::Element *ritual_ZN12QJsonPrivate5Value13elementHelperE18QJsonValueConstRef(
    const QJsonValueConstRef *r) {
  return new QtCbor::Element(QJsonPrivate::Value::elementHelper(*r));
}

//  QJsonValue QJsonPrivate::Value::fromTrustedCbor(const QCborValue &v)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN12QJsonPrivate5Value15fromTrustedCborERK10QCborValue(
    const QCborValue *v) {
  return new QJsonValue(QJsonPrivate::Value::fromTrustedCbor(*v));
}

//  QJsonPrivate::Value::~Value()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QJsonPrivate5ValueD1Ev(QJsonPrivate::Value *self) {
  delete self;
}
