//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstorageinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if (!(defined(Q_OS_WIN))) && (!(defined(Q_OS_DARWIN))) && (defined(Q_OS_LINUX))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstorageinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStorageInfoPrivate::MountInfo::~MountInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStorageInfoPrivate9MountInfoD1Ev(
    QStorageInfoPrivate::MountInfo *self) {
  delete self;
}

#endif  // (!(defined(Q_OS_WIN))) && (!(defined(Q_OS_DARWIN))) && (defined(Q_OS_LINUX))
