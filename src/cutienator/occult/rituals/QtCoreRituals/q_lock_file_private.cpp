//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlockfile_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlockfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qlockfile.h"
#include "qlockfile_p.h"
#include <QtCore/qthread.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <qplatformdefs.h>
#ifdef Q_OS_WIN
#include <io.h>
#include <qt_windows.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qlockfile.cpp, line 476, as _ZN16QLockFilePrivateC1ERK7QString
inline QLockFilePrivate::QLockFilePrivate(const QString &fn)
    : fileName(fn)
{
}
//  -----------------------------------------------------------------------

//  QLockFilePrivate::QLockFilePrivate(const QString &fn)
extern "C" Q_DECL_EXPORT
QLockFilePrivate *ritual_ZN16QLockFilePrivateC1ERK7QString(
    const QString *fn) {
  return new QLockFilePrivate(*fn);
}

//  QString QLockFilePrivate::processNameByPid(qint64 pid)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QLockFilePrivate16processNameByPidEx(qint64 pid) {
  return new QString(QLockFilePrivate::processNameByPid(pid));
}

//  int QLockFilePrivate::getLockFileHandle(QLockFile *f)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QLockFilePrivate17getLockFileHandleEP9QLockFile(
    QLockFile *f) {
  return QLockFilePrivate::getLockFileHandle(f);
}
