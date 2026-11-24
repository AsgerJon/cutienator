//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 4)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h>
#if QT_DEPRECATED_SINCE(6, 4)
#include <QtQml/qqmlengine.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 64, as _ZN31QQuickLabsPlatformStandardPaths11displayNameEN14QStandardPaths16StandardLocationE
#if QT_DEPRECATED_SINCE(6, 4)
inline QString QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::StandardLocation type)
{
    return QStandardPaths::displayName(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 76, as _ZN31QQuickLabsPlatformStandardPaths14findExecutableERK7QStringRK5QListIS0_E
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::findExecutable(const QString &executableName, const QStringList &paths)
{
    return QUrl::fromLocalFile(QStandardPaths::findExecutable(executableName, paths));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 88, as _ZN31QQuickLabsPlatformStandardPaths6locateEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::locate(QStandardPaths::StandardLocation type, const QString &fileName, QStandardPaths::LocateOptions options)
{
    return QUrl::fromLocalFile(QStandardPaths::locate(type, fileName, options));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 112, as _ZN31QQuickLabsPlatformStandardPaths18setTestModeEnabledEb
#if QT_DEPRECATED_SINCE(6, 4)
inline void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool testMode)
{
    QStandardPaths::setTestModeEnabled(testMode);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 136, as _ZN31QQuickLabsPlatformStandardPaths16writableLocationEN14QStandardPaths16StandardLocationE
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::writableLocation(QStandardPaths::StandardLocation type)
{
    return QUrl::fromLocalFile(QStandardPaths::writableLocation(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLabsPlatformStandardPaths::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformStandardPaths10metaObjectEv(
    const QQuickLabsPlatformStandardPaths *self) {
  return self->metaObject();
}

//  void QQuickLabsPlatformStandardPaths::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths22qt_qmlMarker_singletonEv(
    QQuickLabsPlatformStandardPaths *self) {
  self->qt_qmlMarker_singleton();
}

//  const QMetaObject
//      *QQuickLabsPlatformStandardPaths::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN31QQuickLabsPlatformStandardPaths20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformStandardPaths::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformStandardPaths::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformStandardPaths *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QString QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::Stan
//      dardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickLabsPlatformStandardPaths11displayNameEN14QStandardPaths16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QQuickLabsPlatformStandardPaths::displayName(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl QQuickLabsPlatformStandardPaths::findExecutable(const QString
//      &executableName, const QStringList &paths)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths14findExecutableERK7QStringRK5QListIS0_E(
    const QString *executableName,
    const QList<QString> *paths) {
  return new QUrl(
      QQuickLabsPlatformStandardPaths::findExecutable(
          *executableName,
          *paths));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl
//      QQuickLabsPlatformStandardPaths::locate(QStandardPaths::StandardLocat
//      ion type, const QString &fileName, QStandardPaths::LocateOptions
//      options)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths6locateEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE(
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QUrl(
      QQuickLabsPlatformStandardPaths::locate(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool testMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths18setTestModeEnabledEb(
    bool testMode) {
  QQuickLabsPlatformStandardPaths::setTestModeEnabled(testMode);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl QQuickLabsPlatformStandardPaths::writableLocation(QStandardPaths::St
//      andardLocation type)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths16writableLocationEN14QStandardPaths16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QUrl(QQuickLabsPlatformStandardPaths::writableLocation(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#endif  // QT_DEPRECATED_SINCE(6, 4)
