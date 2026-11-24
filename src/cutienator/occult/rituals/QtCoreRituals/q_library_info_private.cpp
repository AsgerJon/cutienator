//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlibraryinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlibraryinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

#if QT_CONFIG(settings)
//  QSettings *QLibraryInfoPrivate::configuration()
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN19QLibraryInfoPrivate13configurationEv() {
  return QLibraryInfoPrivate::configuration();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  void QLibraryInfoPrivate::setQtconfManualPath(const QString
//      *qtconfManualPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLibraryInfoPrivate19setQtconfManualPathEPK7QString(
    const QString *qtconfManualPath) {
  QLibraryInfoPrivate::setQtconfManualPath(qtconfManualPath);
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  QString QLibraryInfoPrivate::expandEnvVariables(QString path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QLibraryInfoPrivate18expandEnvVariablesE7QString(
    const QString *path) {
  return new QString(QLibraryInfoPrivate::expandEnvVariables(*path));
}
#endif  // QT_CONFIG(settings)

//  void QLibraryInfoPrivate::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLibraryInfoPrivate6reloadEv() {
  QLibraryInfoPrivate::reload();
}

//  LocationInfo QLibraryInfoPrivate::locationInfo(QLibraryInfo::LibraryPath
//      loc)
extern "C" Q_DECL_EXPORT
QLibraryInfoPrivate::LocationInfo *ritual_ZN19QLibraryInfoPrivate12locationInfoEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath loc) {
  return new QLibraryInfoPrivate::LocationInfo(
      QLibraryInfoPrivate::locationInfo(
          loc));
}

//  QString QLibraryInfoPrivate::path(QLibraryInfo::LibraryPath p)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QLibraryInfoPrivate4pathEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath p) {
  return new QString(QLibraryInfoPrivate::path(p));
}

//  QStringList QLibraryInfoPrivate::paths(QLibraryInfo::LibraryPath p)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QLibraryInfoPrivate5pathsEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath p) {
  return new QList<QString>(QLibraryInfoPrivate::paths(p));
}

//  QStringList QLibraryInfoPrivate::qtConfPaths(QLibraryInfo::LibraryPath
//      location)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QLibraryInfoPrivate11qtConfPathsEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath location) {
  return new QList<QString>(QLibraryInfoPrivate::qtConfPaths(location));
}

//  QStringList QLibraryInfoPrivate::appPaths(QLibraryInfo::LibraryPath
//      location)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QLibraryInfoPrivate8appPathsEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath location) {
  return new QList<QString>(QLibraryInfoPrivate::appPaths(location));
}

//  QStringList QLibraryInfoPrivate::qtPaths(QLibraryInfo::LibraryPath
//      location)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QLibraryInfoPrivate7qtPathsEN12QLibraryInfo11LibraryPathE(
    QLibraryInfo::LibraryPath location) {
  return new QList<QString>(QLibraryInfoPrivate::qtPaths(location));
}

//  QLibraryInfoPrivate::~QLibraryInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLibraryInfoPrivateD1Ev(QLibraryInfoPrivate *self) {
  delete self;
}
