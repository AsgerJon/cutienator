//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>

//  QString QQmlPropertyCacheCreatorBase::tr(const char *sourceText, const
//      char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQmlPropertyCacheCreatorBase2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlPropertyCacheCreatorBase::tr(
          sourceText,
          disambiguation,
          n));
}

//  QV4::CompiledData::CommonType
//      QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(QMetaType
//      metaType)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CommonType ritual_ZN28QQmlPropertyCacheCreatorBase23propertyTypeForMetaTypeE9QMetaType(
    const QMetaType *metaType) {
  return QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(*metaType);
}

//  QString QQmlPropertyCacheCreatorBase::explain(OverrideSemantics::Status
//      reason)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQmlPropertyCacheCreatorBase7explainEN17OverrideSemantics6StatusE(
    OverrideSemantics::Status reason) {
  return new QString(QQmlPropertyCacheCreatorBase::explain(reason));
}

//  QQmlPropertyCacheCreatorBase::~QQmlPropertyCacheCreatorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlPropertyCacheCreatorBaseD1Ev(
    QQmlPropertyCacheCreatorBase *self) {
  delete self;
}
