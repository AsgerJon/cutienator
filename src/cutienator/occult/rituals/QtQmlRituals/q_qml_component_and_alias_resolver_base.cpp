//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcomponentandaliasresolver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcomponentandaliasresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QString QQmlComponentAndAliasResolverBase::tr(const char *sourceText,
//      const char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QQmlComponentAndAliasResolverBase2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlComponentAndAliasResolverBase::tr(
          sourceText,
          disambiguation,
          n));
}

//  QQmlComponentAndAliasResolverBase::~QQmlComponentAndAliasResolverBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlComponentAndAliasResolverBaseD1Ev(
    QQmlComponentAndAliasResolverBase *self) {
  delete self;
}
