//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotion_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotion_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  bool qdesigner_internal::QDesignerPromotion::addPromotedClass(const
//      QString &baseClass, const QString &className, const QString
//      &includeFile, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal18QDesignerPromotion16addPromotedClassERK7QStringS3_S3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *baseClass,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->qdesigner_internal::QDesignerPromotion::addPromotedClass(
      *baseClass,
      *className,
      *includeFile,
      errorMessage);
}

//  bool qdesigner_internal::QDesignerPromotion::removePromotedClass(const
//      QString &className, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal18QDesignerPromotion19removePromotedClassERK7QStringPS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *className,
    QString *errorMessage) {
  return self->qdesigner_internal::QDesignerPromotion::removePromotedClass(
      *className,
      errorMessage);
}

//  bool
//      qdesigner_internal::QDesignerPromotion::changePromotedClassName(const
//      QString &oldclassName, const QString &newClassName, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal18QDesignerPromotion23changePromotedClassNameERK7QStringS3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *oldclassName,
    const QString *newClassName,
    QString *errorMessage) {
  return self->qdesigner_internal::QDesignerPromotion::changePromotedClassName(
      *oldclassName,
      *newClassName,
      errorMessage);
}

//  bool
//      qdesigner_internal::QDesignerPromotion::setPromotedClassIncludeFile(c
//      onst QString &className, const QString &includeFile, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal18QDesignerPromotion27setPromotedClassIncludeFileERK7QStringS3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->qdesigner_internal::QDesignerPromotion::setPromotedClassIncludeFile(
      *className,
      *includeFile,
      errorMessage);
}
