//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>

//  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError()
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::AnnotatedQmlError *ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1Ev() {
  return new QQmlComponentPrivate::AnnotatedQmlError();
}

//  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
//      error)
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::AnnotatedQmlError *ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1E9QQmlError(
    const QQmlError *error) {
  return new QQmlComponentPrivate::AnnotatedQmlError(*error);
}

//  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
//      error, bool transient)
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::AnnotatedQmlError *ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1E9QQmlErrorb(
    const QQmlError *error,
    bool transient) {
  return new QQmlComponentPrivate::AnnotatedQmlError(*error, transient);
}

//  QQmlComponentPrivate::AnnotatedQmlError::~AnnotatedQmlError()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorD1Ev(
    QQmlComponentPrivate::AnnotatedQmlError *self) {
  delete self;
}
