//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltranslation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QQmlTranslationPropertyTranslationDataFunctor::QQmlTranslationPropertyTra
//      nslationDataFunctor(const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QQmlTranslation &translationData)
extern "C" Q_DECL_EXPORT
QQmlTranslationPropertyTranslationDataFunctor *ritual_ZN45QQmlTranslationPropertyTranslationDataFunctorC1ERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK15QQmlTranslation(
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QQmlTranslation *translationData) {
  return new QQmlTranslationPropertyTranslationDataFunctor(
      *compilationUnit,
      *translationData);
}

//  bool QQmlTranslationPropertyTranslationDataFunctor::operator()(QMetaType
//      metaType, void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN45QQmlTranslationPropertyTranslationDataFunctorclE9QMetaTypePv(
    QQmlTranslationPropertyTranslationDataFunctor *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->operator()(*metaType, dataPtr);
}

//  QQmlTranslationPropertyTranslationDataFunctor::~QQmlTranslationPropertyTr
//      anslationDataFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN45QQmlTranslationPropertyTranslationDataFunctorD1Ev(
    QQmlTranslationPropertyTranslationDataFunctor *self) {
  delete self;
}
