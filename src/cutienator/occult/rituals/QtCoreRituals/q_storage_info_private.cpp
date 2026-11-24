//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstorageinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstorageinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstorageinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QStorageInfoPrivate::QStorageInfoPrivate()
extern "C" Q_DECL_EXPORT
QStorageInfoPrivate *ritual_ZN19QStorageInfoPrivateC1Ev() {
  return new QStorageInfoPrivate();
}

//  QStorageInfo QStorageInfoPrivate::root()
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN19QStorageInfoPrivate4rootEv() {
  return new QStorageInfo(QStorageInfoPrivate::root());
}

#if defined(Q_OS_UNIX)
//  bool QStorageInfoPrivate::shouldIncludeFs(const QString &mountDir, const
//      QByteArray &fsType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QStorageInfoPrivate15shouldIncludeFsERK7QStringRK10QByteArray(
    const QString *mountDir,
    const QByteArray *fsType) {
  return QStorageInfoPrivate::shouldIncludeFs(*mountDir, *fsType);
}
#endif  // defined(Q_OS_UNIX)

//  QStorageInfoPrivate::~QStorageInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStorageInfoPrivateD1Ev(QStorageInfoPrivate *self) {
  delete self;
}
