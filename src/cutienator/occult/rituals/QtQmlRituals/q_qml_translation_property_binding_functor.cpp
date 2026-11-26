//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QQmlTranslationPropertyBindingFunctor::QQmlTranslationPropertyBindingFunc
//      tor(const QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      &compilationUnit, const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
QQmlTranslationPropertyBindingFunctor *ritual_ZN37QQmlTranslationPropertyBindingFunctorC1ERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEEPKNS1_12CompiledData7BindingE(
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QV4::CompiledData::Binding *binding) {
  return new QQmlTranslationPropertyBindingFunctor(
      *compilationUnit,
      binding);
}

//  bool QQmlTranslationPropertyBindingFunctor::operator()(QMetaType
//      metaType, void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN37QQmlTranslationPropertyBindingFunctorclE9QMetaTypePv(
    QQmlTranslationPropertyBindingFunctor *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->operator()(*metaType, dataPtr);
}

//  QQmlTranslationPropertyBindingFunctor::~QQmlTranslationPropertyBindingFun
//      ctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QQmlTranslationPropertyBindingFunctorD1Ev(
    QQmlTranslationPropertyBindingFunctor *self) {
  delete self;
}
