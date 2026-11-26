//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstorageinfo_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 2.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstorageinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstorageinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlatin1stringview.h>

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

#if (!(defined(Q_OS_WIN))) && (!(defined(Q_OS_DARWIN))) && \
    (defined(Q_OS_LINUX))
//  void QStorageInfoPrivate::setFromMountInfo(MountInfo &&info)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStorageInfoPrivate16setFromMountInfoEONS_9MountInfoE(
    QStorageInfoPrivate *self,
    QStorageInfoPrivate::MountInfo *info) {
  self->setFromMountInfo(std::move(*info));
}
#endif

#if (!(defined(Q_OS_WIN))) && (!(defined(Q_OS_DARWIN))) && \
    (defined(Q_OS_LINUX))
//  QStorageInfoPrivate::QStorageInfoPrivate(MountInfo &&info)
extern "C" Q_DECL_EXPORT
QStorageInfoPrivate *ritual_ZN19QStorageInfoPrivateC1EONS_9MountInfoE(
    QStorageInfoPrivate::MountInfo *info) {
  return new QStorageInfoPrivate(std::move(*info));
}
#endif

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

#if defined(Q_OS_UNIX)
//  static bool QStorageInfoPrivate::isParentOf(const QString &parent,
//      const QString &dirName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QStorageInfoPrivate10isParentOfI7QStringEEbRKT_RKS1_(
    const QString *parent,
    const QString *dirName) {
  return QStorageInfoPrivate::isParentOf(*parent, *dirName);
}

//  static bool QStorageInfoPrivate::isParentOf(const QLatin1StringView
//      &parent, const QString &dirName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QStorageInfoPrivate10isParentOfI13QLatin1StringEEbRKT_RK7QString(
    const QLatin1StringView *parent,
    const QString *dirName) {
  return QStorageInfoPrivate::isParentOf(*parent, *dirName);
}
#endif  // defined(Q_OS_UNIX)
