//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if !(defined(Q_OS_WIN))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QProcEnvValue::QProcEnvValue()
extern "C" Q_DECL_EXPORT
QProcEnvValue *ritual_ZN13QProcEnvValueC1Ev() {
  return new QProcEnvValue();
}

//  QProcEnvValue::QProcEnvValue(const QString &value)
extern "C" Q_DECL_EXPORT
QProcEnvValue *ritual_ZN13QProcEnvValueC1ERK7QString(const QString *value) {
  return new QProcEnvValue(*value);
}

//  QProcEnvValue::QProcEnvValue(const QByteArray &value)
extern "C" Q_DECL_EXPORT
QProcEnvValue *ritual_ZN13QProcEnvValueC1ERK10QByteArray(
    const QByteArray *value) {
  return new QProcEnvValue(*value);
}

//  bool QProcEnvValue::operator==(const QProcEnvValue &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QProcEnvValueeqERKS_(
    const QProcEnvValue *self,
    const QProcEnvValue *other) {
  return self->operator==(*other);
}

//  QByteArray QProcEnvValue::bytes() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QProcEnvValue5bytesEv(const QProcEnvValue *self) {
  return new QByteArray(self->bytes());
}

//  QString QProcEnvValue::string() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QProcEnvValue6stringEv(const QProcEnvValue *self) {
  return new QString(self->string());
}

//  QProcEnvValue::~QProcEnvValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QProcEnvValueD1Ev(QProcEnvValue *self) {
  delete self;
}

#endif  // !(defined(Q_OS_WIN))
#endif  // QT_CONFIG(processenvironment)
#endif  // QT_CONFIG(processenvironment)
