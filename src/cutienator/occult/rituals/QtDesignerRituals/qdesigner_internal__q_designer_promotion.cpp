//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotion_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotion_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtCore/qlist.h>
#include <QtDesigner/QDesignerPromotionInterface>
#include <QtCore/QSet>
#include <QtCore/QString>

//  qdesigner_internal::QDesignerPromotion::QDesignerPromotion(QDesignerFormE
//      ditorInterface *core)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerPromotion *ritual_ZN18qdesigner_internal18QDesignerPromotionC1EP28QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *core) {
  return new qdesigner_internal::QDesignerPromotion(core);
}

//  PromotedClasses qdesigner_internal::QDesignerPromotion::promotedClasses()
//      const
extern "C" Q_DECL_EXPORT
QDesignerPromotionInterface::PromotedClasses *ritual_ZNK18qdesigner_internal18QDesignerPromotion15promotedClassesEv(
    const qdesigner_internal::QDesignerPromotion *self) {
  return new QDesignerPromotionInterface::PromotedClasses(
      self->promotedClasses());
}

//  QSet<QString>
//      qdesigner_internal::QDesignerPromotion::referencedPromotedClassNames(
//      ) const
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZNK18qdesigner_internal18QDesignerPromotion28referencedPromotedClassNamesEv(
    const qdesigner_internal::QDesignerPromotion *self) {
  return new QSet<QString>(self->referencedPromotedClassNames());
}

//  bool qdesigner_internal::QDesignerPromotion::addPromotedClass(const
//      QString &baseClass, const QString &className, const QString
//      &includeFile, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerPromotion16addPromotedClassERK7QStringS3_S3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *baseClass,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->addPromotedClass(
      *baseClass,
      *className,
      *includeFile,
      errorMessage);
}

//  bool qdesigner_internal::QDesignerPromotion::removePromotedClass(const
//      QString &className, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerPromotion19removePromotedClassERK7QStringPS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *className,
    QString *errorMessage) {
  return self->removePromotedClass(*className, errorMessage);
}

//  bool
//      qdesigner_internal::QDesignerPromotion::changePromotedClassName(const
//      QString &oldclassName, const QString &newClassName, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerPromotion23changePromotedClassNameERK7QStringS3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *oldclassName,
    const QString *newClassName,
    QString *errorMessage) {
  return self->changePromotedClassName(
      *oldclassName,
      *newClassName,
      errorMessage);
}

//  bool
//      qdesigner_internal::QDesignerPromotion::setPromotedClassIncludeFile(c
//      onst QString &className, const QString &includeFile, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerPromotion27setPromotedClassIncludeFileERK7QStringS3_PS1_(
    qdesigner_internal::QDesignerPromotion *self,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->setPromotedClassIncludeFile(
      *className,
      *includeFile,
      errorMessage);
}

//  QList<QDesignerWidgetDataBaseItemInterface *>
//      qdesigner_internal::QDesignerPromotion::promotionBaseClasses() const
extern "C" Q_DECL_EXPORT
QList<QDesignerWidgetDataBaseItemInterface *> *ritual_ZNK18qdesigner_internal18QDesignerPromotion20promotionBaseClassesEv(
    const qdesigner_internal::QDesignerPromotion *self) {
  return new QList<QDesignerWidgetDataBaseItemInterface *>(
      self->promotionBaseClasses());
}

//  bool qdesigner_internal::QDesignerPromotion::canBePromoted(const
//      QDesignerWidgetDataBaseItemInterface *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18QDesignerPromotion13canBePromotedEPK36QDesignerWidgetDataBaseItemInterface(
    const qdesigner_internal::QDesignerPromotion *self,
    const QDesignerWidgetDataBaseItemInterface *a0) {
  return self->canBePromoted(a0);
}

//  void qdesigner_internal::QDesignerPromotion::refreshObjectInspector()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18QDesignerPromotion22refreshObjectInspectorEv(
    qdesigner_internal::QDesignerPromotion *self) {
  self->refreshObjectInspector();
}

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

//  a QDesignerPromotionInterface::PromotedClasses a ritual of
//      qdesigner_internal::QDesignerPromotion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_QDesignerPromotion__QDesignerPromotionInterface_PromotedClasses(
    QDesignerPromotionInterface::PromotedClasses *self) {
  delete self;
}

//  a QSet<QString> a ritual of qdesigner_internal::QDesignerPromotion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_QDesignerPromotion__QSet_QString(
    QSet<QString> *self) {
  delete self;
}
