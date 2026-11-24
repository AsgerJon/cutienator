//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcpponassignment_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcpponassignment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>

//  void QQmlCppOnAssignmentHelper::set(QQmlPropertyValueInterceptor
//      *interceptor, const QQmlProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlCppOnAssignmentHelper3setEP28QQmlPropertyValueInterceptorRK12QQmlProperty(
    QQmlPropertyValueInterceptor *interceptor,
    const QQmlProperty *property) {
  QQmlCppOnAssignmentHelper::set(interceptor, *property);
}

//  void QQmlCppOnAssignmentHelper::set(QQmlPropertyValueSource *valueSource,
//      const QQmlProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlCppOnAssignmentHelper3setEP23QQmlPropertyValueSourceRK12QQmlProperty(
    QQmlPropertyValueSource *valueSource,
    const QQmlProperty *property) {
  QQmlCppOnAssignmentHelper::set(valueSource, *property);
}

//  QQmlCppOnAssignmentHelper::~QQmlCppOnAssignmentHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlCppOnAssignmentHelperD1Ev(
    QQmlCppOnAssignmentHelper *self) {
  delete self;
}
