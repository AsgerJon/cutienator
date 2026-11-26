//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltranslation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QUntypedPropertyBinding QQmlTranslationPropertyBinding::create(const
//      QQmlPropertyData *pd, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN30QQmlTranslationPropertyBinding6createEPK16QQmlPropertyDataRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEEPKNS4_12CompiledData7BindingE(
    const QQmlPropertyData *pd,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QV4::CompiledData::Binding *binding) {
  return new QUntypedPropertyBinding(
      QQmlTranslationPropertyBinding::create(
          pd,
          *compilationUnit,
          binding));
}

//  QUntypedPropertyBinding QQmlTranslationPropertyBinding::create(const
//      QMetaType &propertyType, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QQmlTranslation &translationData)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN30QQmlTranslationPropertyBinding6createERK9QMetaTypeRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK15QQmlTranslation(
    const QMetaType *propertyType,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QQmlTranslation *translationData) {
  return new QUntypedPropertyBinding(
      QQmlTranslationPropertyBinding::create(
          *propertyType,
          *compilationUnit,
          *translationData));
}

//  QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      QQmlTranslationPropertyBinding::compilationUnit(const
//      QPropertyBindingPrivate *priv)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZN30QQmlTranslationPropertyBinding15compilationUnitEPK23QPropertyBindingPrivate(
    const QPropertyBindingPrivate *priv) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      QQmlTranslationPropertyBinding::compilationUnit(
          priv));
}

//  QQmlTranslationPropertyBinding::~QQmlTranslationPropertyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQmlTranslationPropertyBindingD1Ev(
    QQmlTranslationPropertyBinding *self) {
  delete self;
}

//  a QQmlRefPointer<QV4::ExecutableCompilationUnit> a ritual of
//      QQmlTranslationPropertyBinding gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlTranslationPropertyBinding__QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QQmlRefPointer<QV4::ExecutableCompilationUnit> *self) {
  delete self;
}
