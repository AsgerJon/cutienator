//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlimport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qtyperevision.h>
#include <QtQml/qqmlerror.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QString QQmlImports::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlImports2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlImports::tr(sourceText, disambiguation, n));
}

//  QQmlImports::QQmlImports()
extern "C" Q_DECL_EXPORT
QQmlImports *ritual_ZN11QQmlImportsC1Ev() {
  return new QQmlImports();
}

//  QQmlImports::~QQmlImports()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlImportsD1Ev(QQmlImports *self) {
  delete self;
}

//  void QQmlImports::setBaseUrl(const QUrl &url, const QString &urlString)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlImports10setBaseUrlERK4QUrlRK7QString(
    QQmlImports *self,
    const QUrl *url,
    const QString *urlString) {
  self->setBaseUrl(*url, *urlString);
}

//  QUrl QQmlImports::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK11QQmlImports7baseUrlEv(const QQmlImports *self) {
  return new QUrl(self->baseUrl());
}

//  void QQmlImports::populateCache(QQmlTypeNameCache *cache) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlImports13populateCacheEP17QQmlTypeNameCache(
    const QQmlImports *self,
    QQmlTypeNameCache *cache) {
  self->populateCache(cache);
}

//  QStringList QQmlImports::completeQmldirPaths(const QString &uri, const
//      QStringList &basePaths, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QQmlImports19completeQmldirPathsERK7QStringRK5QListIS0_E13QTypeRevision(
    const QString *uri,
    const QList<QString> *basePaths,
    const QTypeRevision *version) {
  return new QList<QString>(
      QQmlImports::completeQmldirPaths(
          *uri,
          *basePaths,
          *version));
}

//  QString QQmlImports::versionString(QTypeRevision version, ImportVersion
//      importVersion)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlImports13versionStringE13QTypeRevisionNS_13ImportVersionE(
    const QTypeRevision *version,
    QQmlImports::ImportVersion importVersion) {
  return new QString(QQmlImports::versionString(*version, importVersion));
}

//  bool QQmlImports::isLocal(const QString &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlImports7isLocalERK7QString(const QString *url) {
  return QQmlImports::isLocal(*url);
}

//  bool QQmlImports::isLocal(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlImports7isLocalERK4QUrl(const QUrl *url) {
  return QQmlImports::isLocal(*url);
}

//  QUrl QQmlImports::urlFromLocalFileOrQrcOrUrl(const QString &a0)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN11QQmlImports26urlFromLocalFileOrQrcOrUrlERK7QString(
    const QString *a0) {
  return new QUrl(QQmlImports::urlFromLocalFileOrQrcOrUrl(*a0));
}

//  void QQmlImports::setDesignerSupportRequired(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlImports26setDesignerSupportRequiredEb(bool b) {
  QQmlImports::setDesignerSupportRequired(b);
}

//  QTypeRevision QQmlImports::validVersion(QTypeRevision version)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN11QQmlImports12validVersionE13QTypeRevision(
    const QTypeRevision *version) {
  return new QTypeRevision(QQmlImports::validVersion(*version));
}

//  QQmlError QQmlImports::moduleNotFoundError(const QString &uri,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN11QQmlImports19moduleNotFoundErrorERK7QString13QTypeRevision(
    const QString *uri,
    const QTypeRevision *version) {
  return new QQmlError(QQmlImports::moduleNotFoundError(*uri, *version));
}

//  QString QQmlImports::redirectQmldirContent(QQmlTypeLoader *typeLoader,
//      QQmlTypeLoaderQmldirContent *qmldir)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlImports21redirectQmldirContentEP14QQmlTypeLoaderP27QQmlTypeLoaderQmldirContent(
    QQmlTypeLoader *typeLoader,
    QQmlTypeLoaderQmldirContent *qmldir) {
  return new QString(QQmlImports::redirectQmldirContent(typeLoader, qmldir));
}

//  void QQmlImports::insertImport(QQmlImportNamespace *nameSpace,
//      QQmlImportInstance *import)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlImports12insertImportEP19QQmlImportNamespaceP18QQmlImportInstance(
    QQmlImportNamespace *nameSpace,
    QQmlImportInstance *import) {
  QQmlImports::insertImport(nameSpace, import);
}

//  QQmlImportNamespace *QQmlImports::importNamespace(const QString &prefix)
extern "C" Q_DECL_EXPORT
QQmlImportNamespace *ritual_ZN11QQmlImports15importNamespaceERK7QString(
    QQmlImports *self,
    const QString *prefix) {
  return self->importNamespace(*prefix);
}

//  QQmlImportNamespace *QQmlImports::findQualifiedNamespace(const
//      QHashedStringRef &a0) const
extern "C" Q_DECL_EXPORT
QQmlImportNamespace *ritual_ZNK11QQmlImports22findQualifiedNamespaceERK16QHashedStringRef(
    const QQmlImports *self,
    const QHashedStringRef *a0) {
  return self->findQualifiedNamespace(*a0);
}

//  void QQmlImports::registerBuiltinModuleTypes(const
//      QQmlTypeLoaderQmldirContent &qmldir, QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlImports26registerBuiltinModuleTypesERK27QQmlTypeLoaderQmldirContent13QTypeRevision(
    QQmlImports *self,
    const QQmlTypeLoaderQmldirContent *qmldir,
    const QTypeRevision *version) {
  self->registerBuiltinModuleTypes(*qmldir, *version);
}

//  QString QQmlImports::resolvedUri(const QString &dir_arg, QQmlTypeLoader
//      *typeLoader)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlImports11resolvedUriERK7QStringP14QQmlTypeLoader(
    QQmlImports *self,
    const QString *dir_arg,
    QQmlTypeLoader *typeLoader) {
  return new QString(self->resolvedUri(*dir_arg, typeLoader));
}
