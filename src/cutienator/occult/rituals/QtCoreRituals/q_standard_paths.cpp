//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_STANDARDPATHS)
#include <QtCore/qstandardpaths.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QString QStandardPaths::writableLocation(StandardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths16writableLocationENS_16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QStandardPaths::writableLocation(type));
}

//  QStringList QStandardPaths::standardLocations(StandardLocation type)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN14QStandardPaths17standardLocationsENS_16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QList<QString>(QStandardPaths::standardLocations(type));
}

//  QString QStandardPaths::locate(StandardLocation type, const QString
//      &fileName, LocateOptions options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths6locateENS_16StandardLocationERK7QString6QFlagsINS_12LocateOptionEE(
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QString(
      QStandardPaths::locate(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}

//  QStringList QStandardPaths::locateAll(StandardLocation type, const
//      QString &fileName, LocateOptions options)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN14QStandardPaths9locateAllENS_16StandardLocationERK7QString6QFlagsINS_12LocateOptionEE(
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QList<QString>(
      QStandardPaths::locateAll(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}

#if !defined(QT_BOOTSTRAPPED)
//  QString QStandardPaths::displayName(StandardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths11displayNameENS_16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QStandardPaths::displayName(type));
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QString QStandardPaths::findExecutable(const QString &executableName,
//      const QStringList &paths)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths14findExecutableERK7QStringRK5QListIS0_E(
    const QString *executableName,
    const QList<QString> *paths) {
  return new QString(
      QStandardPaths::findExecutable(
          *executableName,
          *paths));
}

//  void QStandardPaths::setTestModeEnabled(bool testMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStandardPaths18setTestModeEnabledEb(bool testMode) {
  QStandardPaths::setTestModeEnabled(testMode);
}

//  bool QStandardPaths::isTestModeEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QStandardPaths17isTestModeEnabledEv() {
  return QStandardPaths::isTestModeEnabled();
}

#endif  // !defined(QT_NO_STANDARDPATHS)
