//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlibraryinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlibraryinfo.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qstring.h>

//  const char *QLibraryInfo::build()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN12QLibraryInfo5buildEv() {
  return QLibraryInfo::build();
}

//  bool QLibraryInfo::isDebugBuild()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLibraryInfo12isDebugBuildEv() {
  return QLibraryInfo::isDebugBuild();
}

//  bool QLibraryInfo::isSharedBuild()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLibraryInfo13isSharedBuildEv() {
  return QLibraryInfo::isSharedBuild();
}

//  QVersionNumber QLibraryInfo::version()
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN12QLibraryInfo7versionEv() {
  return new QVersionNumber(QLibraryInfo::version());
}

//  QString QLibraryInfo::path(LibraryPath p)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QLibraryInfo4pathENS_11LibraryPathE(
    QLibraryInfo::LibraryPath p) {
  return new QString(QLibraryInfo::path(p));
}

//  QString QLibraryInfo::location(LibraryLocation location)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QLibraryInfo8locationENS_11LibraryPathE(
    QLibraryInfo::LibraryLocation location) {
  return new QString(QLibraryInfo::location(location));
}

//  QLibraryInfo::~QLibraryInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLibraryInfoD1Ev(QLibraryInfo *self) {
  delete self;
}
