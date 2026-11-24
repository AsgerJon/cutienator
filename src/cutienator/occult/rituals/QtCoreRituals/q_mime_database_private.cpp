//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimedatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimedatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h> // always first
#include <QtCore/qmimedatabase.h>
#include <QtCore/private/qmimedatabase_p.h>
#include <QtCore/private/qmimeprovider_p.h>
#include <QtCore/private/qmimetype_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <QtCore/QStandardPaths>
#include <QtCore/QBuffer>
#include <QtCore/QUrl>
#include <QtCore/QDebug>
#include <algorithm>
#include <functional>
#include <stack>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 159, as _ZN20QMimeDatabasePrivate9providersEv
inline const QMimeDatabasePrivate::Providers &QMimeDatabasePrivate::providers()
{
#if QT_CONFIG(thread) // stub implementation always returns true
    Q_ASSERT(!mutex.tryLock()); // caller should have locked mutex
#endif
    if (m_providers.empty()) {
        loadProviders();
        m_lastCheck.start();
    } else {
        if (shouldCheck())
            loadProviders();
    }
    return m_providers;
}

//  from src/corelib/io/qfilesystementry.cpp, line 137, as _ZNK16QFileSystemEntry8fileNameEv
#if defined(Q_OS_LINUX)
inline QString QFileSystemEntry::fileName() const
{
    findLastSeparator();
#if defined(Q_OS_WIN)
    if (m_lastSeparator == -1 && m_filePath.length() >= 2 && m_filePath.at(1) == u':')
        return m_filePath.mid(2);
#endif
    return m_filePath.mid(m_lastSeparator + 1);
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 48, as _ZN20QMimeDatabasePrivateC1Ev
inline QMimeDatabasePrivate::QMimeDatabasePrivate()
    : m_defaultMimeType(QStringLiteral("application/octet-stream"))
{
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 53, as _ZN20QMimeDatabasePrivateD1Ev
inline QMimeDatabasePrivate::~QMimeDatabasePrivate()
{
}
//  -----------------------------------------------------------------------

//  QMimeDatabasePrivate::QMimeDatabasePrivate()
extern "C" Q_DECL_EXPORT
QMimeDatabasePrivate *ritual_ZN20QMimeDatabasePrivateC1Ev() {
  return new QMimeDatabasePrivate();
}

//  QMimeDatabasePrivate::~QMimeDatabasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeDatabasePrivateD1Ev(QMimeDatabasePrivate *self) {
  delete self;
}

//  const QString &QMimeDatabasePrivate::defaultMimeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QMimeDatabasePrivate15defaultMimeTypeEv(
    const QMimeDatabasePrivate *self) {
  return new QString(self->defaultMimeType());
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
