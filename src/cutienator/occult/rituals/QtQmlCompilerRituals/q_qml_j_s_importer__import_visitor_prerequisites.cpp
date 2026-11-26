//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QString>
#include <QtCore/QList>

//  QQmlJSImporter::ImportVisitorPrerequisites::ImportVisitorPrerequisites(QQ
//      mlJSScope::Ptr target, QQmlJSLogger *logger, const QString
//      &implicitImportDirectory, const QStringList &qmldirFiles)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportVisitorPrerequisites *ritual_ZN14QQmlJSImporter26ImportVisitorPrerequisitesC1E22QDeferredSharedPointerI11QQmlJSScopeEP12QQmlJSLoggerRK7QStringRK5QListIS6_E(
    const QQmlJSScope::Ptr *target,
    QQmlJSLogger *logger,
    const QString *implicitImportDirectory,
    const QList<QString> *qmldirFiles) {
  return new QQmlJSImporter::ImportVisitorPrerequisites(
      *target,
      logger,
      *implicitImportDirectory,
      *qmldirFiles);
}

//  QQmlJSImporter::ImportVisitorPrerequisites::~ImportVisitorPrerequisites()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter26ImportVisitorPrerequisitesD1Ev(
    QQmlJSImporter::ImportVisitorPrerequisites *self) {
  delete self;
}
