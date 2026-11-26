//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 4.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtQml/qqmlabstracturlinterceptor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QUrl>
#include <QtQml/6.12.0/QtQml/private/qqmltypedata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmldirdata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlengine_p.h>

//  QString QQmlTypeLoader::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlTypeLoader2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlTypeLoader::tr(sourceText, disambiguation, n));
}

//  QQmlTypeLoader::QQmlTypeLoader(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZN14QQmlTypeLoaderC1EPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QQmlTypeLoader(engine);
}

//  QQmlTypeLoader::~QQmlTypeLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoaderD1Ev(QQmlTypeLoader *self) {
  delete self;
}

//  void QQmlTypeLoader::sanitizeUNCPath(QString *path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader15sanitizeUNCPathEP7QString(QString *path) {
  QQmlTypeLoader::sanitizeUNCPath(path);
}

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QQmlTypeLoader::injectModule(const QUrl &relativeUrl, const
//      QV4::CompiledData::Unit *unit)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZN14QQmlTypeLoader12injectModuleERK4QUrlPKN3QV412CompiledData4UnitE(
    QQmlTypeLoader *self,
    const QUrl *relativeUrl,
    const QV4::CompiledData::Unit *unit) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      self->injectModule(
          *relativeUrl,
          unit));
}

//  QString QQmlTypeLoader::cleanFilePath(const QString &path) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlTypeLoader13cleanFilePathERK7QString(
    const QQmlTypeLoader *self,
    const QString *path) {
  return new QString(self->cleanFilePath(*path));
}

//  bool QQmlTypeLoader::fileExists(const QString &filePath) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTypeLoader10fileExistsERK7QString(
    const QQmlTypeLoader *self,
    const QString *filePath) {
  return self->fileExists(*filePath);
}

//  bool QQmlTypeLoader::fileExists(const QString &dirPath, const QString
//      &file) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTypeLoader10fileExistsERK7QStringS2_(
    const QQmlTypeLoader *self,
    const QString *dirPath,
    const QString *file) {
  return self->fileExists(*dirPath, *file);
}

//  bool QQmlTypeLoader::directoryExists(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader15directoryExistsERK7QString(
    QQmlTypeLoader *self,
    const QString *path) {
  return self->directoryExists(*path);
}

//  const QQmlTypeLoaderQmldirContent QQmlTypeLoader::qmldirContent(const
//      QString &filePath)
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderQmldirContent *ritual_ZN14QQmlTypeLoader13qmldirContentERK7QString(
    QQmlTypeLoader *self,
    const QString *filePath) {
  return new QQmlTypeLoaderQmldirContent(self->qmldirContent(*filePath));
}

//  void QQmlTypeLoader::setQmldirContent(const QString &filePath, const
//      QString &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader16setQmldirContentERK7QStringS2_(
    QQmlTypeLoader *self,
    const QString *filePath,
    const QString *content) {
  self->setQmldirContent(*filePath, *content);
}

//  void QQmlTypeLoader::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader10clearCacheEv(QQmlTypeLoader *self) {
  self->clearCache();
}

//  void QQmlTypeLoader::trimCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader9trimCacheEv(QQmlTypeLoader *self) {
  self->trimCache();
}

//  bool QQmlTypeLoader::removeFromCache(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader15removeFromCacheERK4QUrl(
    QQmlTypeLoader *self,
    const QUrl *url) {
  return self->removeFromCache(*url);
}

//  bool QQmlTypeLoader::isTypeLoaded(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTypeLoader12isTypeLoadedERK4QUrl(
    const QQmlTypeLoader *self,
    const QUrl *url) {
  return self->isTypeLoaded(*url);
}

//  bool QQmlTypeLoader::isScriptLoaded(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTypeLoader14isScriptLoadedERK4QUrl(
    const QQmlTypeLoader *self,
    const QUrl *url) {
  return self->isScriptLoaded(*url);
}

//  void QQmlTypeLoader::loadWithStaticData(const QQmlDataBlob::Ptr &blob,
//      const QByteArray &data, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader18loadWithStaticDataERK14QQmlRefPointerI12QQmlDataBlobERK10QByteArrayNS_4ModeE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob,
    const QByteArray *data,
    QQmlTypeLoader::Mode mode) {
  self->loadWithStaticData(*blob, *data, mode);
}

//  void QQmlTypeLoader::drop(const QQmlDataBlob::Ptr &blob)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4dropERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob) {
  self->drop(*blob);
}

//  void QQmlTypeLoader::initializeEngine(QQmlEngineExtensionInterface *a0,
//      const char *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader16initializeEngineEP28QQmlEngineExtensionInterfacePKc(
    QQmlTypeLoader *self,
    QQmlEngineExtensionInterface *a0,
    const char *a1) {
  self->initializeEngine(a0, a1);
}

//  void QQmlTypeLoader::initializeEngine(QQmlExtensionInterface *a0, const
//      char *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader16initializeEngineEP22QQmlExtensionInterfacePKc(
    QQmlTypeLoader *self,
    QQmlExtensionInterface *a0,
    const char *a1) {
  self->initializeEngine(a0, a1);
}

//  void QQmlTypeLoader::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader10invalidateEv(QQmlTypeLoader *self) {
  self->invalidate();
}

//  void QQmlTypeLoader::addUrlInterceptor(QQmlAbstractUrlInterceptor
//      *urlInterceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader17addUrlInterceptorEP26QQmlAbstractUrlInterceptor(
    QQmlTypeLoader *self,
    QQmlAbstractUrlInterceptor *urlInterceptor) {
  self->addUrlInterceptor(urlInterceptor);
}

//  void QQmlTypeLoader::removeUrlInterceptor(QQmlAbstractUrlInterceptor
//      *urlInterceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader20removeUrlInterceptorEP26QQmlAbstractUrlInterceptor(
    QQmlTypeLoader *self,
    QQmlAbstractUrlInterceptor *urlInterceptor) {
  self->removeUrlInterceptor(urlInterceptor);
}

//  QList<QQmlAbstractUrlInterceptor *> QQmlTypeLoader::urlInterceptors()
//      const
extern "C" Q_DECL_EXPORT
QList<QQmlAbstractUrlInterceptor *> *ritual_ZNK14QQmlTypeLoader15urlInterceptorsEv(
    const QQmlTypeLoader *self) {
  return new QList<QQmlAbstractUrlInterceptor *>(self->urlInterceptors());
}

//  QUrl QQmlTypeLoader::interceptUrl(const QUrl &url,
//      QQmlAbstractUrlInterceptor::DataType type) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QQmlTypeLoader12interceptUrlERK4QUrlN26QQmlAbstractUrlInterceptor8DataTypeE(
    const QQmlTypeLoader *self,
    const QUrl *url,
    QQmlAbstractUrlInterceptor::DataType type) {
  return new QUrl(self->interceptUrl(*url, type));
}

//  bool QQmlTypeLoader::hasUrlInterceptors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTypeLoader18hasUrlInterceptorsEv(
    const QQmlTypeLoader *self) {
  return self->hasUrlInterceptors();
}

#if !(!QT_CONFIG(qml_debug))
//  QQmlProfiler *QQmlTypeLoader::profiler() const
extern "C" Q_DECL_EXPORT
QQmlProfiler *ritual_ZNK14QQmlTypeLoader8profilerEv(
    const QQmlTypeLoader *self) {
  return self->profiler();
}
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
//  void QQmlTypeLoader::setProfiler(QQmlProfiler *profiler)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader11setProfilerEP12QQmlProfiler(
    QQmlTypeLoader *self,
    QQmlProfiler *profiler) {
  self->setProfiler(profiler);
}
#endif  // !(!QT_CONFIG(qml_debug))

//  QStringList QQmlTypeLoader::importPathList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlTypeLoader14importPathListEv(
    const QQmlTypeLoader *self) {
  return new QList<QString>(self->importPathList());
}

//  void QQmlTypeLoader::setImportPathList(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader17setImportPathListERK5QListI7QStringE(
    QQmlTypeLoader *self,
    const QList<QString> *paths) {
  self->setImportPathList(*paths);
}

//  void QQmlTypeLoader::addImportPath(const QString &dir, AddPathMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader13addImportPathERK7QStringNS_11AddPathModeE(
    QQmlTypeLoader *self,
    const QString *dir,
    QQmlTypeLoader::AddPathMode mode) {
  self->addImportPath(*dir, mode);
}

//  QStringList QQmlTypeLoader::pluginPathList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlTypeLoader14pluginPathListEv(
    const QQmlTypeLoader *self) {
  return new QList<QString>(self->pluginPathList());
}

//  void QQmlTypeLoader::setPluginPathList(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader17setPluginPathListERK5QListI7QStringE(
    QQmlTypeLoader *self,
    const QList<QString> *paths) {
  self->setPluginPathList(*paths);
}

//  void QQmlTypeLoader::addPluginPath(const QString &path, AddPathMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader13addPluginPathERK7QStringNS_11AddPathModeE(
    QQmlTypeLoader *self,
    const QString *path,
    QQmlTypeLoader::AddPathMode mode) {
  self->addPluginPath(*path, mode);
}

#if QT_CONFIG(qml_network)
//  QQmlNetworkAccessManagerFactoryPtrConst
//      QQmlTypeLoader::networkAccessManagerFactory() const
extern "C" Q_DECL_EXPORT
QQmlNetworkAccessManagerFactoryPtrConst *ritual_ZNK14QQmlTypeLoader27networkAccessManagerFactoryEv(
    const QQmlTypeLoader *self) {
  return new QQmlNetworkAccessManagerFactoryPtrConst(
      self->networkAccessManagerFactory());
}
#endif  // QT_CONFIG(qml_network)

#if QT_CONFIG(qml_network)
//  void QQmlTypeLoader::setNetworkAccessManagerFactory(QQmlNetworkAccessMana
//      gerFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader30setNetworkAccessManagerFactoryEP31QQmlNetworkAccessManagerFactory(
    QQmlTypeLoader *self,
    QQmlNetworkAccessManagerFactory *factory) {
  self->setNetworkAccessManagerFactory(factory);
}
#endif  // QT_CONFIG(qml_network)

#if QT_CONFIG(qml_network)
//  QNetworkAccessManager *QQmlTypeLoader::createNetworkAccessManager(QObject
//      *parent) const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZNK14QQmlTypeLoader26createNetworkAccessManagerEP7QObject(
    const QQmlTypeLoader *self,
    QObject *parent) {
  return self->createNetworkAccessManager(parent);
}
#endif  // QT_CONFIG(qml_network)

//  bool QQmlTypeLoader::writeCacheFile()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader14writeCacheFileEv(QQmlTypeLoader *self) {
  return self->writeCacheFile();
}

//  bool QQmlTypeLoader::readCacheFile()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader13readCacheFileEv(QQmlTypeLoader *self) {
  return self->readCacheFile();
}

//  bool QQmlTypeLoader::isDebugging()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader11isDebuggingEv(QQmlTypeLoader *self) {
  return self->isDebugging();
}

//  QStringList QQmlTypeLoader::urlsForModule(const QString &module) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlTypeLoader13urlsForModuleERK7QString(
    const QQmlTypeLoader *self,
    const QString *module) {
  return new QList<QString>(self->urlsForModule(*module));
}

//  bool QQmlTypeLoader::isResource(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeLoader10isResourceERK7QString(const QString *path) {
  return QQmlTypeLoader::isResource(*path);
}

//  QQmlTypeLoaderThread *QQmlTypeLoader::thread() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderThread *ritual_ZNK14QQmlTypeLoader6threadEv(
    const QQmlTypeLoader *self) {
  return self->thread();
}

//  QV4::ExecutionEngine *QQmlTypeLoader::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK14QQmlTypeLoader6engineEv(
    const QQmlTypeLoader *self) {
  return self->engine();
}

//  void QQmlTypeLoader::startThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader11startThreadEv(QQmlTypeLoader *self) {
  self->startThread();
}

//  void QQmlTypeLoader::shutdownThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader14shutdownThreadEv(QQmlTypeLoader *self) {
  self->shutdownThread();
}

//  QQmlTypeLoaderThread *QQmlTypeLoader::ensureThread()
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderThread *ritual_ZN14QQmlTypeLoader12ensureThreadEv(
    QQmlTypeLoader *self) {
  return self->ensureThread();
}

//  void QQmlTypeLoader::trimCache(const QQmlTypeLoaderSharedDataPtr &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader9trimCacheERK31QQmlTypeLoaderSharedDataPtrBaseI24QQmlTypeLoaderSharedData24QQmlTypeLoaderLockedDataE(
    QQmlTypeLoader *self,
    const QQmlTypeLoaderSharedDataPtr *data) {
  self->trimCache(*data);
}

//  void QQmlTypeLoader::loadThread(const QQmlDataBlob::Ptr &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader10loadThreadERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *a0) {
  self->loadThread(*a0);
}

//  void QQmlTypeLoader::loadWithStaticDataThread(const QQmlDataBlob::Ptr
//      &a0, const QByteArray &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader24loadWithStaticDataThreadERK14QQmlRefPointerI12QQmlDataBlobERK10QByteArray(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *a0,
    const QByteArray *a1) {
  self->loadWithStaticDataThread(*a0, *a1);
}

//  void QQmlTypeLoader::loadWithCachedUnitThread(const QQmlDataBlob::Ptr
//      &blob, const QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader24loadWithCachedUnitThreadERK14QQmlRefPointerI12QQmlDataBlobEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->loadWithCachedUnitThread(*blob, unit);
}

#if QT_CONFIG(qml_network)
//  void QQmlTypeLoader::networkReplyFinished(QNetworkReply *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader20networkReplyFinishedEP13QNetworkReply(
    QQmlTypeLoader *self,
    QNetworkReply *a0) {
  self->networkReplyFinished(a0);
}
#endif  // QT_CONFIG(qml_network)

#if QT_CONFIG(qml_network)
//  void QQmlTypeLoader::networkReplyProgress(QNetworkReply *a0, qint64 a1,
//      qint64 a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader20networkReplyProgressEP13QNetworkReplyxx(
    QQmlTypeLoader *self,
    QNetworkReply *a0,
    qint64 a1,
    qint64 a2) {
  self->networkReplyProgress(a0, a1, a2);
}
#endif  // QT_CONFIG(qml_network)

//  void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
//      QByteArray &a1, DataOrigin a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader7setDataERK14QQmlRefPointerI12QQmlDataBlobERK10QByteArrayNS_10DataOriginE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *a0,
    const QByteArray *a1,
    QQmlTypeLoader::DataOrigin a2) {
  self->setData(*a0, *a1, a2);
}

//  void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const QString
//      &fileName, bool exists)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader7setDataERK14QQmlRefPointerI12QQmlDataBlobERK7QStringb(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *a0,
    const QString *fileName,
    bool exists) {
  self->setData(*a0, *fileName, exists);
}

//  void QQmlTypeLoader::setData(const QQmlDataBlob::Ptr &a0, const
//      QQmlDataBlob::SourceCodeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader7setDataERK14QQmlRefPointerI12QQmlDataBlobERKNS1_14SourceCodeDataE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *a0,
    const QQmlDataBlob::SourceCodeData *a1) {
  self->setData(*a0, *a1);
}

//  void QQmlTypeLoader::setCachedUnit(const QQmlDataBlob::Ptr &blob, const
//      QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader13setCachedUnitERK14QQmlRefPointerI12QQmlDataBlobEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->setCachedUnit(*blob, unit);
}

//  QStringList QQmlTypeLoader::importPathList(PathType type) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlTypeLoader14importPathListENS_8PathTypeE(
    const QQmlTypeLoader *self,
    QQmlTypeLoader::PathType type) {
  return new QList<QString>(self->importPathList(type));
}

//  void QQmlTypeLoader::clearQmldirInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader15clearQmldirInfoEv(QQmlTypeLoader *self) {
  self->clearQmldirInfo();
}

//  LocalQmldirResult QQmlTypeLoader::locateLocalQmldir(QQmlTypeLoader::Blob
//      *blob, const QQmlTypeLoader::Blob::PendingImportPtr &import,
//      QList<QQmlError> *errors)
extern "C" Q_DECL_EXPORT
QQmlTypeLoader::LocalQmldirResult ritual_ZN14QQmlTypeLoader17locateLocalQmldirEPNS_4BlobERKSt10shared_ptrINS0_13PendingImportEEP5QListI9QQmlErrorE(
    QQmlTypeLoader *self,
    QQmlTypeLoader::Blob *blob,
    const QQmlTypeLoader::Blob::PendingImportPtr *import,
    QList<QQmlError> *errors) {
  return self->locateLocalQmldir(blob, *import, errors);
}

//  void QQmlTypeLoader::load(const QQmlDataBlob::Ptr &blob, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4loadERK14QQmlRefPointerI12QQmlDataBlobENS_4ModeE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob,
    QQmlTypeLoader::Mode mode) {
  self->load(*blob, mode);
}

//  void QQmlTypeLoader::loadWithCachedUnit(const QQmlDataBlob::Ptr &blob,
//      const QQmlPrivate::CachedQmlUnit *unit, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader18loadWithCachedUnitERK14QQmlRefPointerI12QQmlDataBlobEPKN11QQmlPrivate13CachedQmlUnitENS_4ModeE(
    QQmlTypeLoader *self,
    const QQmlDataBlob::Ptr *blob,
    const QQmlPrivate::CachedQmlUnit *unit,
    QQmlTypeLoader::Mode mode) {
  self->loadWithCachedUnit(*blob, unit, mode);
}

//  void QQmlTypeLoader::updateTypeCacheTrimThreshold(const
//      QQmlTypeLoaderSharedDataPtr &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader28updateTypeCacheTrimThresholdERK31QQmlTypeLoaderSharedDataPtrBaseI24QQmlTypeLoaderSharedData24QQmlTypeLoaderLockedDataE(
    QQmlTypeLoader *self,
    const QQmlTypeLoaderSharedDataPtr *data) {
  self->updateTypeCacheTrimThreshold(*data);
}

//  QQmlMetaType::CacheMode QQmlTypeLoader::aotCacheMode()
extern "C" Q_DECL_EXPORT
QQmlMetaType::CacheMode ritual_ZN14QQmlTypeLoader12aotCacheModeEv(
    QQmlTypeLoader *self) {
  return self->aotCacheMode();
}

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QQmlTypeLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlTypeLoader__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}

//  a QQmlNetworkAccessManagerFactoryPtrConst a ritual of QQmlTypeLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlTypeLoader__QQmlNetworkAccessManagerFactoryPtrConst(
    QQmlNetworkAccessManagerFactoryPtrConst *self) {
  delete self;
}

//  static QQmlTypeLoader *QQmlTypeLoader::get<QQmlEngine,
//      QQmlEnginePrivate, void>(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZN14QQmlTypeLoader3getI10QQmlEngine17QQmlEnginePrivatevEEPS_PT_(
    QQmlEngine *engine) {
  return QQmlTypeLoader::get<QQmlEngine>(engine);
}

//  QQmlRefPointer<QQmlTypeData>
//      QQmlTypeLoader::finalizeBlob<QQmlTypeData>(
//      QQmlRefPointer<QQmlTypeData> &&blob, QQmlTypeLoader::Mode mode)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlTypeData> *ritual_ZN14QQmlTypeLoader12finalizeBlobI12QQmlTypeDataEE14QQmlRefPointerIT_EOS4_NS_4ModeE(
    QQmlTypeLoader *self,
    QQmlRefPointer<QQmlTypeData> *blob,
    int mode) {
  return new QQmlRefPointer<QQmlTypeData>(
      self->finalizeBlob<QQmlTypeData>(
          std::move(*blob), static_cast<QQmlTypeLoader::Mode>(mode)));
}

//  QQmlRefPointer<QQmlScriptBlob>
//      QQmlTypeLoader::finalizeBlob<QQmlScriptBlob>(
//      QQmlRefPointer<QQmlScriptBlob> &&blob, QQmlTypeLoader::Mode mode)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlScriptBlob> *ritual_ZN14QQmlTypeLoader12finalizeBlobI14QQmlScriptBlobEE14QQmlRefPointerIT_EOS4_NS_4ModeE(
    QQmlTypeLoader *self,
    QQmlRefPointer<QQmlScriptBlob> *blob,
    int mode) {
  return new QQmlRefPointer<QQmlScriptBlob>(
      self->finalizeBlob<QQmlScriptBlob>(
          std::move(*blob), static_cast<QQmlTypeLoader::Mode>(mode)));
}

//  QQmlRefPointer<QQmlQmldirData>
//      QQmlTypeLoader::finalizeBlob<QQmlQmldirData>(
//      QQmlRefPointer<QQmlQmldirData> &&blob, QQmlTypeLoader::Mode mode)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlQmldirData> *ritual_ZN14QQmlTypeLoader12finalizeBlobI14QQmlQmldirDataEE14QQmlRefPointerIT_EOS4_NS_4ModeE(
    QQmlTypeLoader *self,
    QQmlRefPointer<QQmlQmldirData> *blob,
    int mode) {
  return new QQmlRefPointer<QQmlQmldirData>(
      self->finalizeBlob<QQmlQmldirData>(
          std::move(*blob), static_cast<QQmlTypeLoader::Mode>(mode)));
}
