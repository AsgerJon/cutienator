//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstandardpaths.h>
#include <QtCore/qstring.h>

//  QString QStandardPaths::writableLocation(StandardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths16writableLocationENS_16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QStandardPaths::writableLocation(type));
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

//  QString QStandardPaths::displayName(StandardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStandardPaths11displayNameENS_16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QStandardPaths::displayName(type));
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
