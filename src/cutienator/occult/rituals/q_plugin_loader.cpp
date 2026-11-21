//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpluginloader.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpluginloader.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>

//  const QMetaObject *QPluginLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPluginLoader10metaObjectEv(
    const QPluginLoader *self) {
  return self->metaObject();
}

//  QString QPluginLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPluginLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPluginLoader::tr(s, c, n));
}

//  QPluginLoader::QPluginLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QPluginLoader *ritual_ZN13QPluginLoaderC1EP7QObject(QObject *parent) {
  return new QPluginLoader(parent);
}

//  QPluginLoader::QPluginLoader(const QString &fileName, QObject *parent)
extern "C" Q_DECL_EXPORT
QPluginLoader *ritual_ZN13QPluginLoaderC1ERK7QStringP7QObject(
    const QString *fileName,
    QObject *parent) {
  return new QPluginLoader(*fileName, parent);
}

//  QPluginLoader::~QPluginLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoaderD1Ev(QPluginLoader *self) {
  delete self;
}

//  QObject *QPluginLoader::instance()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QPluginLoader8instanceEv(QPluginLoader *self) {
  return self->instance();
}

//  QJsonObject QPluginLoader::metaData() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QPluginLoader8metaDataEv(
    const QPluginLoader *self) {
  return new QJsonObject(self->metaData());
}

//  bool QPluginLoader::load()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPluginLoader4loadEv(QPluginLoader *self) {
  return self->load();
}

//  bool QPluginLoader::unload()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPluginLoader6unloadEv(QPluginLoader *self) {
  return self->unload();
}

//  bool QPluginLoader::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPluginLoader8isLoadedEv(const QPluginLoader *self) {
  return self->isLoaded();
}

//  void QPluginLoader::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoader11setFileNameERK7QString(
    QPluginLoader *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QPluginLoader::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPluginLoader8fileNameEv(const QPluginLoader *self) {
  return new QString(self->fileName());
}

//  QString QPluginLoader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPluginLoader11errorStringEv(
    const QPluginLoader *self) {
  return new QString(self->errorString());
}

//  void QPluginLoader::setLoadHints(QLibrary::LoadHints loadHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoader12setLoadHintsE6QFlagsIN8QLibrary8LoadHintEE(
    QPluginLoader *self,
    int loadHints) {
  self->setLoadHints(QFlags<QLibrary::LoadHint>::fromInt(loadHints));
}

//  QLibrary::LoadHints QPluginLoader::loadHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPluginLoader9loadHintsEv(const QPluginLoader *self) {
  return static_cast<int>(self->loadHints().toInt());
}
