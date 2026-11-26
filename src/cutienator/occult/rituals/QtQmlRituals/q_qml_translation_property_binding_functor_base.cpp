//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      &QQmlTranslationPropertyBindingFunctorBase::compilationUnit() const
extern "C" Q_DECL_EXPORT
const QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZNK41QQmlTranslationPropertyBindingFunctorBase15compilationUnitEv(
    const QQmlTranslationPropertyBindingFunctorBase *self) {
  return &(self->compilationUnit());
}

//  QQmlTranslationPropertyBindingFunctorBase::QQmlTranslationPropertyBinding
//      FunctorBase(const QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      &compilationUnit)
extern "C" Q_DECL_EXPORT
QQmlTranslationPropertyBindingFunctorBase *ritual_ZN41QQmlTranslationPropertyBindingFunctorBaseC1ERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEE(
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit) {
  return new QQmlTranslationPropertyBindingFunctorBase(*compilationUnit);
}

//  QQmlTranslationPropertyBindingFunctorBase::~QQmlTranslationPropertyBindin
//      gFunctorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQmlTranslationPropertyBindingFunctorBaseD1Ev(
    QQmlTranslationPropertyBindingFunctorBase *self) {
  delete self;
}
