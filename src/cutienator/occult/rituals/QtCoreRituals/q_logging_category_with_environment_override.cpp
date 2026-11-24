//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLoggingCategoryWithEnvironmentOverride::QLoggingCategoryWithEnvironmentO
//      verride(const char *category, const char *env)
extern "C" Q_DECL_EXPORT
QLoggingCategoryWithEnvironmentOverride *ritual_ZN39QLoggingCategoryWithEnvironmentOverrideC1EPKcS1_(
    const char *category,
    const char *env) {
  return new QLoggingCategoryWithEnvironmentOverride(category, env);
}

//  const char
//      *QLoggingCategoryWithEnvironmentOverride::registerOverride(const char
//      *categoryName, const char *environment)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN39QLoggingCategoryWithEnvironmentOverride16registerOverrideEPKcS1_(
    const char *categoryName,
    const char *environment) {
  return QLoggingCategoryWithEnvironmentOverride::registerOverride(
      categoryName,
      environment);
}
