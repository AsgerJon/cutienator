//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsystemsemaphore.h"
#include "qsystemsemaphore_p.h"
#if QT_CONFIG(systemsemaphore)
#include <QtCore/q20memory.h>
#include <errno.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 342, as _ZN23QSystemSemaphorePrivate18setUnixErrorStringE13QLatin1String
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView function)
{
    // EINVAL is handled in functions so they can give better error strings
    switch (errno) {
    case EPERM:
    case EACCES:
        errorString = QSystemSemaphore::tr("%1: permission denied").arg(function);
        error = QSystemSemaphore::PermissionDenied;
        break;
    case EEXIST:
        errorString = QSystemSemaphore::tr("%1: already exists").arg(function);
        error = QSystemSemaphore::AlreadyExists;
        break;
    case ENOENT:
        errorString = QSystemSemaphore::tr("%1: does not exist").arg(function);
        error = QSystemSemaphore::NotFound;
        break;
    case ERANGE:
    case ENOSPC:
    case EMFILE:
        errorString = QSystemSemaphore::tr("%1: out of resources").arg(function);
        error = QSystemSemaphore::OutOfResources;
        break;
    case ENAMETOOLONG:
        errorString = QSystemSemaphore::tr("%1: key too long").arg(function);
        error = QSystemSemaphore::KeyError;
        break;
    default:
        errorString = QSystemSemaphore::tr("%1: unknown error: %2")
                .arg(function, qt_error_string(errno));
        error = QSystemSemaphore::UnknownError;
#if defined QSYSTEMSEMAPHORE_DEBUG
        qDebug() << errorString << "key" << key << "errno" << errno << EINVAL;
#endif
    }
}
#endif  // QT_CONFIG(systemsemaphore)

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 17, as _ZN23QSystemSemaphorePrivate16constructBackendEv
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::constructBackend()
{
    visit([](auto p) { q20::construct_at(p); });
}
#endif  // QT_CONFIG(systemsemaphore)

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 22, as _ZN23QSystemSemaphorePrivate15destructBackendEv
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::destructBackend()
{
    visit([](auto p) { std::destroy_at(p); });
}
#endif  // QT_CONFIG(systemsemaphore)
//  -----------------------------------------------------------------------

#if QT_CONFIG(systemsemaphore)
//  QSystemSemaphorePrivate::QSystemSemaphorePrivate(QNativeIpcKey::Type
//      type)
extern "C" Q_DECL_EXPORT
QSystemSemaphorePrivate *ritual_ZN23QSystemSemaphorePrivateC1EN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return new QSystemSemaphorePrivate(type);
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  QSystemSemaphorePrivate::~QSystemSemaphorePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivateD1Ev(QSystemSemaphorePrivate *self) {
  delete self;
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView
//      function)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate18setUnixErrorStringE13QLatin1String(
    QSystemSemaphorePrivate *self,
    const QLatin1String *function) {
  self->setUnixErrorString(*function);
}
#endif  // QT_CONFIG(systemsemaphore)

//  void
//      QSystemSemaphorePrivate::setError(QSystemSemaphore::SystemSemaphoreEr
//      ror e, const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate8setErrorEN16QSystemSemaphore20SystemSemaphoreErrorERK7QString(
    QSystemSemaphorePrivate *self,
    QSystemSemaphore::SystemSemaphoreError e,
    const QString *message) {
  self->setError(e, *message);
}

//  void QSystemSemaphorePrivate::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate10clearErrorEv(
    QSystemSemaphorePrivate *self) {
  self->clearError();
}

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::constructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate16constructBackendEv(
    QSystemSemaphorePrivate *self) {
  self->constructBackend();
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::destructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate15destructBackendEv(
    QSystemSemaphorePrivate *self) {
  self->destructBackend();
}
#endif  // QT_CONFIG(systemsemaphore)

#endif  // QT_CONFIG(systemsemaphore)
