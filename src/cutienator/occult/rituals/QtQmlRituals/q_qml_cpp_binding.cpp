//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcppbinding_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcppbinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qproperty.h>

//  QUntypedPropertyBinding QQmlCppBinding::createBindingForBindable(const
//      QV4::ExecutableCompilationUnit *unit, QObject *thisObject, qsizetype
//      functionIndex, QObject *bindingTarget, int metaPropertyIndex, int
//      valueTypePropertyIndex, const QString &propertyName)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN14QQmlCppBinding24createBindingForBindableEPKN3QV425ExecutableCompilationUnitEP7QObjectxS5_iiRK7QString(
    const QV4::ExecutableCompilationUnit *unit,
    QObject *thisObject,
    qsizetype functionIndex,
    QObject *bindingTarget,
    int metaPropertyIndex,
    int valueTypePropertyIndex,
    const QString *propertyName) {
  return new QUntypedPropertyBinding(
      QQmlCppBinding::createBindingForBindable(
          unit,
          thisObject,
          functionIndex,
          bindingTarget,
          metaPropertyIndex,
          valueTypePropertyIndex,
          *propertyName));
}

//  void QQmlCppBinding::createBindingForNonBindable(const
//      QV4::ExecutableCompilationUnit *unit, QObject *thisObject, qsizetype
//      functionIndex, QObject *bindingTarget, int metaPropertyIndex, int
//      valueTypePropertyIndex, const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlCppBinding27createBindingForNonBindableEPKN3QV425ExecutableCompilationUnitEP7QObjectxS5_iiRK7QString(
    const QV4::ExecutableCompilationUnit *unit,
    QObject *thisObject,
    qsizetype functionIndex,
    QObject *bindingTarget,
    int metaPropertyIndex,
    int valueTypePropertyIndex,
    const QString *propertyName) {
  QQmlCppBinding::createBindingForNonBindable(
      unit,
      thisObject,
      functionIndex,
      bindingTarget,
      metaPropertyIndex,
      valueTypePropertyIndex,
      *propertyName);
}

//  QQmlCppBinding::~QQmlCppBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlCppBindingD1Ev(QQmlCppBinding *self) {
  delete self;
}
