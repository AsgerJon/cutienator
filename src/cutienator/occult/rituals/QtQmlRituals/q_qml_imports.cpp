//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 2. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlimport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#include <QtQml/qqmlerror.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QList>

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

//  bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
//      QHashedStringRef &type, QQmlType *type_return, QTypeRevision
//      *version_return, QQmlImportNamespace **ns_return, QList<QQmlError>
//      *errors, QQmlType::RegistrationType registrationType, bool
//      *typeRecursionDetected) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlImports11resolveTypeEP14QQmlTypeLoaderRK16QHashedStringRefP8QQmlTypeP13QTypeRevisionPP19QQmlImportNamespaceP5QListI9QQmlErrorENS5_16RegistrationTypeEPb(
    const QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QHashedStringRef *type,
    QQmlType *type_return,
    QTypeRevision *version_return,
    QQmlImportNamespace **ns_return,
    QList<QQmlError> *errors,
    QQmlType::RegistrationType registrationType,
    bool *typeRecursionDetected) {
  return self->resolveType(
      typeLoader,
      *type,
      type_return,
      version_return,
      ns_return,
      errors,
      registrationType,
      typeRecursionDetected);
}

//  bool QQmlImports::addInlineComponentImport(QQmlImportInstance *const
//      importInstance, const QString &name, const QUrl &importUrl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlImports24addInlineComponentImportEP18QQmlImportInstanceRK7QStringRK4QUrl(
    QQmlImports *self,
    QQmlImportInstance *const importInstance,
    const QString *name,
    const QUrl *importUrl) {
  return self->addInlineComponentImport(importInstance, *name, *importUrl);
}

//  QTypeRevision QQmlImports::addFileImport(QQmlTypeLoader *typeLoader,
//      const QString &uri, const QString &prefix, QTypeRevision
//      requestedVersion, ImportFlags flags, quint8 precedence, QString
//      *localQmldir, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN11QQmlImports13addFileImportEP14QQmlTypeLoaderRK7QStringS4_13QTypeRevision6QFlagsINS_10ImportFlagEEhPS2_P5QListI9QQmlErrorE(
    QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QString *uri,
    const QString *prefix,
    const QTypeRevision *requestedVersion,
    int flags,
    quint8 precedence,
    QString *localQmldir,
    QList<QQmlError> *errors) {
  return new QTypeRevision(
      self->addFileImport(
          typeLoader,
          *uri,
          *prefix,
          *requestedVersion,
          QFlags<QQmlImports::ImportFlag>::fromInt(flags),
          precedence,
          localQmldir,
          errors));
}

//  QTypeRevision QQmlImports::addLibraryImport(QQmlTypeLoader *typeLoader,
//      const QString &uri, const QString &prefix, QTypeRevision
//      requestedVersion, const QString &qmldirIdentifier, const QString
//      &qmldirUrl, ImportFlags flags, quint8 precedence, QList<QQmlError>
//      *errors)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN11QQmlImports16addLibraryImportEP14QQmlTypeLoaderRK7QStringS4_13QTypeRevisionS4_S4_6QFlagsINS_10ImportFlagEEhP5QListI9QQmlErrorE(
    QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QString *uri,
    const QString *prefix,
    const QTypeRevision *requestedVersion,
    const QString *qmldirIdentifier,
    const QString *qmldirUrl,
    int flags,
    quint8 precedence,
    QList<QQmlError> *errors) {
  return new QTypeRevision(
      self->addLibraryImport(
          typeLoader,
          *uri,
          *prefix,
          *requestedVersion,
          *qmldirIdentifier,
          *qmldirUrl,
          QFlags<QQmlImports::ImportFlag>::fromInt(flags),
          precedence,
          errors));
}

//  QTypeRevision QQmlImports::updateQmldirContent(QQmlTypeLoader
//      *typeLoader, const QString &uri, QTypeRevision version, const QString
//      &prefix, const QString &qmldirIdentifier, const QString &qmldirUrl,
//      QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN11QQmlImports19updateQmldirContentEP14QQmlTypeLoaderRK7QString13QTypeRevisionS4_S4_S4_P5QListI9QQmlErrorE(
    QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QString *uri,
    const QTypeRevision *version,
    const QString *prefix,
    const QString *qmldirIdentifier,
    const QString *qmldirUrl,
    QList<QQmlError> *errors) {
  return new QTypeRevision(
      self->updateQmldirContent(
          typeLoader,
          *uri,
          *version,
          *prefix,
          *qmldirIdentifier,
          *qmldirUrl,
          errors));
}

//  void QQmlImports::populateCache(QQmlTypeNameCache *cache) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlImports13populateCacheEP17QQmlTypeNameCache(
    const QQmlImports *self,
    QQmlTypeNameCache *cache) {
  self->populateCache(cache);
}

//  QList<ScriptReference> QQmlImports::resolvedScripts() const
extern "C" Q_DECL_EXPORT
QList<QQmlImports::ScriptReference> *ritual_ZNK11QQmlImports15resolvedScriptsEv(
    const QQmlImports *self) {
  return new QList<QQmlImports::ScriptReference>(self->resolvedScripts());
}

//  QList<CompositeSingletonReference>
//      QQmlImports::resolvedCompositeSingletons() const
extern "C" Q_DECL_EXPORT
QList<QQmlImports::CompositeSingletonReference> *ritual_ZNK11QQmlImports27resolvedCompositeSingletonsEv(
    const QQmlImports *self) {
  return new QList<QQmlImports::CompositeSingletonReference>(
      self->resolvedCompositeSingletons());
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

//  bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
//      QHashedStringRef &type, QTypeRevision *version_return, QQmlType
//      *type_return, QList<QQmlError> *errors, QQmlType::RegistrationType
//      registrationType, bool *typeRecursionDetected) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlImports11resolveTypeEP14QQmlTypeLoaderRK16QHashedStringRefP13QTypeRevisionP8QQmlTypeP5QListI9QQmlErrorENS7_16RegistrationTypeEPb(
    const QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QHashedStringRef *type,
    QTypeRevision *version_return,
    QQmlType *type_return,
    QList<QQmlError> *errors,
    QQmlType::RegistrationType registrationType,
    bool *typeRecursionDetected) {
  return self->resolveType(
      typeLoader,
      *type,
      version_return,
      type_return,
      errors,
      registrationType,
      typeRecursionDetected);
}

//  QQmlImportNamespace *QQmlImports::findQualifiedNamespace(const
//      QHashedStringRef &a0) const
extern "C" Q_DECL_EXPORT
QQmlImportNamespace *ritual_ZNK11QQmlImports22findQualifiedNamespaceERK16QHashedStringRef(
    const QQmlImports *self,
    const QHashedStringRef *a0) {
  return self->findQualifiedNamespace(*a0);
}

//  QTypeRevision QQmlImports::importExtension(QQmlTypeLoader *typeLoader,
//      const QString &uri, QTypeRevision version, const
//      QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN11QQmlImports15importExtensionEP14QQmlTypeLoaderRK7QString13QTypeRevisionPK27QQmlTypeLoaderQmldirContentP5QListI9QQmlErrorE(
    QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QString *uri,
    const QTypeRevision *version,
    const QQmlTypeLoaderQmldirContent *qmldir,
    QList<QQmlError> *errors) {
  return new QTypeRevision(
      self->importExtension(
          typeLoader,
          *uri,
          *version,
          qmldir,
          errors));
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

//  bool QQmlImports::getQmldirContent(QQmlTypeLoader *typeLoader, const
//      QString &qmldirIdentifier, const QString &uri,
//      QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlImports16getQmldirContentEP14QQmlTypeLoaderRK7QStringS4_P27QQmlTypeLoaderQmldirContentP5QListI9QQmlErrorE(
    QQmlImports *self,
    QQmlTypeLoader *typeLoader,
    const QString *qmldirIdentifier,
    const QString *uri,
    QQmlTypeLoaderQmldirContent *qmldir,
    QList<QQmlError> *errors) {
  return self->getQmldirContent(
      typeLoader,
      *qmldirIdentifier,
      *uri,
      qmldir,
      errors);
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

//  a QList<QQmlImports::ScriptReference> a ritual of QQmlImports gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlImports__QList_QQmlImports_ScriptReference(
    QList<QQmlImports::ScriptReference> *self) {
  delete self;
}

//  a QList<QQmlImports::CompositeSingletonReference> a ritual of QQmlImports
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlImports__QList_QQmlImports_CompositeSingletonReference(
    QList<QQmlImports::CompositeSingletonReference> *self) {
  delete self;
}

//  static QQmlImportInstance *QQmlImports::addImportToNamespace<
//      QQmlImports::IsLibrary::No>(QQmlImportNamespace *nameSpace, const
//      QString &uri, const QString &url, QTypeRevision version, quint8
//      precedence)
extern "C" Q_DECL_EXPORT
QQmlImportInstance * ritual_ZN11QQmlImports20addImportToNamespaceILNS_9IsLibraryE0EEEP18QQmlImportInstanceP19QQmlImportNamespaceRK7QStringS8_13QTypeRevisionh(
    QQmlImportNamespace *nameSpace,
    const QString *uri,
    const QString *url,
    const QTypeRevision *version,
    unsigned char precedence) {
  return QQmlImports::addImportToNamespace<QQmlImports::IsLibrary::No>(
      nameSpace, *uri, *url, *version, precedence);
}

//  static QQmlImportInstance *QQmlImports::addImportToNamespace<
//      QQmlImports::IsLibrary::Yes>(QQmlImportNamespace *nameSpace, const
//      QString &uri, const QString &url, QTypeRevision version, quint8
//      precedence)
extern "C" Q_DECL_EXPORT
QQmlImportInstance * ritual_ZN11QQmlImports20addImportToNamespaceILNS_9IsLibraryE1EEEP18QQmlImportInstanceP19QQmlImportNamespaceRK7QStringS8_13QTypeRevisionh(
    QQmlImportNamespace *nameSpace,
    const QString *uri,
    const QString *url,
    const QTypeRevision *version,
    unsigned char precedence) {
  return QQmlImports::addImportToNamespace<QQmlImports::IsLibrary::Yes>(
      nameSpace, *uri, *url, *version, precedence);
}
