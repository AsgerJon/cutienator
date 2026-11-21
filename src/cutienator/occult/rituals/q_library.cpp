//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlibrary.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlibrary.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QLibrary::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QLibrary10metaObjectEv(const QLibrary *self) {
  return self->metaObject();
}

//  QString QLibrary::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QLibrary2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLibrary::tr(s, c, n));
}

//  QLibrary::QLibrary(QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1EP7QObject(QObject *parent) {
  return new QLibrary(parent);
}

//  QLibrary::QLibrary(const QString &fileName, QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringP7QObject(
    const QString *fileName,
    QObject *parent) {
  return new QLibrary(*fileName, parent);
}

//  QLibrary::QLibrary(const QString &fileName, int verNum, QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringiP7QObject(
    const QString *fileName,
    int verNum,
    QObject *parent) {
  return new QLibrary(*fileName, verNum, parent);
}

//  QLibrary::QLibrary(const QString &fileName, const QString &version,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringS2_P7QObject(
    const QString *fileName,
    const QString *version,
    QObject *parent) {
  return new QLibrary(*fileName, *version, parent);
}

//  QLibrary::~QLibrary()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibraryD1Ev(QLibrary *self) {
  delete self;
}

//  bool QLibrary::load()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary4loadEv(QLibrary *self) {
  return self->load();
}

//  bool QLibrary::unload()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary6unloadEv(QLibrary *self) {
  return self->unload();
}

//  bool QLibrary::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QLibrary8isLoadedEv(const QLibrary *self) {
  return self->isLoaded();
}

//  bool QLibrary::isLibrary(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary9isLibraryERK7QString(const QString *fileName) {
  return QLibrary::isLibrary(*fileName);
}

//  void QLibrary::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary11setFileNameERK7QString(
    QLibrary *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QLibrary::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QLibrary8fileNameEv(const QLibrary *self) {
  return new QString(self->fileName());
}

//  void QLibrary::setFileNameAndVersion(const QString &fileName, int verNum)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringi(
    QLibrary *self,
    const QString *fileName,
    int verNum) {
  self->setFileNameAndVersion(*fileName, verNum);
}

//  void QLibrary::setFileNameAndVersion(const QString &fileName, const
//      QString &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringS2_(
    QLibrary *self,
    const QString *fileName,
    const QString *version) {
  self->setFileNameAndVersion(*fileName, *version);
}

//  QString QLibrary::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QLibrary11errorStringEv(const QLibrary *self) {
  return new QString(self->errorString());
}

//  void QLibrary::setLoadHints(LoadHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary12setLoadHintsE6QFlagsINS_8LoadHintEE(
    QLibrary *self,
    int hints) {
  self->setLoadHints(QFlags<QLibrary::LoadHint>::fromInt(hints));
}

//  LoadHints QLibrary::loadHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QLibrary9loadHintsEv(const QLibrary *self) {
  return static_cast<int>(self->loadHints().toInt());
}
