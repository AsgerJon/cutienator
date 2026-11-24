//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey()
extern "C" Q_DECL_EXPORT
QFileSystemWatcherPathKey *ritual_ZN25QFileSystemWatcherPathKeyC1Ev() {
  return new QFileSystemWatcherPathKey();
}

//  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const QString
//      &other)
extern "C" Q_DECL_EXPORT
QFileSystemWatcherPathKey *ritual_ZN25QFileSystemWatcherPathKeyC1ERK7QString(
    const QString *other) {
  return new QFileSystemWatcherPathKey(*other);
}

//  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const
//      QFileSystemWatcherPathKey &other)
extern "C" Q_DECL_EXPORT
QFileSystemWatcherPathKey *ritual_ZN25QFileSystemWatcherPathKeyC1ERKS_(
    const QFileSystemWatcherPathKey *other) {
  return new QFileSystemWatcherPathKey(*other);
}

//  bool QFileSystemWatcherPathKey::operator==(const
//      QFileSystemWatcherPathKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QFileSystemWatcherPathKeyeqERKS_(
    const QFileSystemWatcherPathKey *self,
    const QFileSystemWatcherPathKey *other) {
  return self->operator==(*other);
}

//  QFileSystemWatcherPathKey::~QFileSystemWatcherPathKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QFileSystemWatcherPathKeyD1Ev(
    QFileSystemWatcherPathKey *self) {
  delete self;
}

#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
