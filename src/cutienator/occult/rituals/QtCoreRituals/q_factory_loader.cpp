//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfactoryloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_QOBJECT)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfactoryloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcborarray.h>
#include <QtCore/qlist.h>

//  QString QFactoryLoader::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QFactoryLoader2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QFactoryLoader::tr(sourceText, disambiguation, n));
}

//  QFactoryLoader::QFactoryLoader(const char *iid, const QString &suffix,
//      Qt::CaseSensitivity a2)
extern "C" Q_DECL_EXPORT
QFactoryLoader *ritual_ZN14QFactoryLoaderC1EPKcRK7QStringN2Qt15CaseSensitivityE(
    const char *iid,
    const QString *suffix,
    Qt::CaseSensitivity a2) {
  return new QFactoryLoader(iid, *suffix, a2);
}

#if QT_CONFIG(library)
//  QFactoryLoader::~QFactoryLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFactoryLoaderD1Ev(QFactoryLoader *self) {
  delete self;
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  void QFactoryLoader::setLoadHints(QLibrary::LoadHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFactoryLoader12setLoadHintsE6QFlagsIN8QLibrary8LoadHintEE(
    QFactoryLoader *self,
    int hints) {
  self->setLoadHints(QFlags<QLibrary::LoadHint>::fromInt(hints));
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  void QFactoryLoader::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFactoryLoader6updateEv(QFactoryLoader *self) {
  self->update();
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
//  void QFactoryLoader::refreshAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFactoryLoader10refreshAllEv() {
  QFactoryLoader::refreshAll();
}
#endif  // QT_CONFIG(library)

#if QT_CONFIG(library)
#if defined(Q_OS_UNIX) && !defined (Q_OS_DARWIN)
//  QLibraryPrivate *QFactoryLoader::library(const QString &key) const
extern "C" Q_DECL_EXPORT
QLibraryPrivate *ritual_ZNK14QFactoryLoader7libraryERK7QString(
    const QFactoryLoader *self,
    const QString *key) {
  return self->library(*key);
}
#endif  // defined(Q_OS_UNIX) && !defined (Q_OS_DARWIN)
#endif  // QT_CONFIG(library)

//  void QFactoryLoader::setExtraSearchPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFactoryLoader18setExtraSearchPathERK7QString(
    QFactoryLoader *self,
    const QString *path) {
  self->setExtraSearchPath(*path);
}

//  int QFactoryLoader::indexOf(const QString &needle) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QFactoryLoader7indexOfERK7QString(
    const QFactoryLoader *self,
    const QString *needle) {
  return self->indexOf(*needle);
}

//  MetaDataList QFactoryLoader::metaData() const
extern "C" Q_DECL_EXPORT
QList<QPluginParsedMetaData> *ritual_ZNK14QFactoryLoader8metaDataEv(
    const QFactoryLoader *self) {
  return new QList<QPluginParsedMetaData>(self->metaData());
}

//  QList<QCborArray> QFactoryLoader::metaDataKeys() const
extern "C" Q_DECL_EXPORT
QList<QCborArray> *ritual_ZNK14QFactoryLoader12metaDataKeysEv(
    const QFactoryLoader *self) {
  return new QList<QCborArray>(self->metaDataKeys());
}

//  QObject *QFactoryLoader::instance(int index) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK14QFactoryLoader8instanceEi(
    const QFactoryLoader *self,
    int index) {
  return self->instance(index);
}

#endif  // !defined(QT_NO_QOBJECT)
