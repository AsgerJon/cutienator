//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtQml/qqmlabstracturlinterceptor.h>
#include <QtCore/qlist.h>

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

//  QQmlMetaType::CacheMode QQmlTypeLoader::aotCacheMode()
extern "C" Q_DECL_EXPORT
QQmlMetaType::CacheMode ritual_ZN14QQmlTypeLoader12aotCacheModeEv(
    QQmlTypeLoader *self) {
  return self->aotCacheMode();
}
