//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemerror_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemerror_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSystemError::QSystemError(int error, ErrorScope scope)
extern "C" Q_DECL_EXPORT
QSystemError *ritual_ZN12QSystemErrorC1EiNS_10ErrorScopeE(
    int error,
    QSystemError::ErrorScope scope) {
  return new QSystemError(error, scope);
}

//  QSystemError::QSystemError()
extern "C" Q_DECL_EXPORT
QSystemError *ritual_ZN12QSystemErrorC1Ev() {
  return new QSystemError();
}

//  QString QSystemError::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSystemError8toStringEv(const QSystemError *self) {
  return new QString(self->toString());
}

//  ErrorScope QSystemError::scope() const
extern "C" Q_DECL_EXPORT
QSystemError::ErrorScope ritual_ZNK12QSystemError5scopeEv(
    const QSystemError *self) {
  return self->scope();
}

//  int QSystemError::error() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSystemError5errorEv(const QSystemError *self) {
  return self->error();
}

//  bool QSystemError::ok() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSystemError2okEv(const QSystemError *self) {
  return self->ok();
}

//  QSystemError QSystemError::stdError(int error)
extern "C" Q_DECL_EXPORT
QSystemError *ritual_ZN12QSystemError8stdErrorEi(int error) {
  return new QSystemError(QSystemError::stdError(error));
}

//  QString QSystemError::string(ErrorScope errorScope, int errorCode)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QSystemError6stringENS_10ErrorScopeEi(
    QSystemError::ErrorScope errorScope,
    int errorCode) {
  return new QString(QSystemError::string(errorScope, errorCode));
}

//  QString QSystemError::stdString(int errorCode)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QSystemError9stdStringEi(int errorCode) {
  return new QString(QSystemError::stdString(errorCode));
}

//  QSystemError::~QSystemError()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSystemErrorD1Ev(QSystemError *self) {
  delete self;
}
