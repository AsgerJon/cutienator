//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystementry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystementry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfilesystementry_p.h"
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

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qfilesystementry.cpp, line 100, as _ZNK16QFileSystemEntry8filePathEv
inline QString QFileSystemEntry::filePath() const
{
    resolveFilePath();
    return m_filePath;
}

//  from src/corelib/io/qfilesystementry.cpp, line 106, as _ZNK16QFileSystemEntry14nativeFilePathEv
inline QFileSystemEntry::NativePath QFileSystemEntry::nativeFilePath() const
{
    resolveNativeFilePath();
    return m_nativeFilePath;
}

//  from src/corelib/io/qfilesystementry.cpp, line 306, as _ZNK16QFileSystemEntry6isRootEv
inline bool QFileSystemEntry::isRoot() const
{
    resolveFilePath();
    return isRootPath(m_filePath);
}

//  from src/corelib/io/qfilesystementry.cpp, line 312, as _ZNK16QFileSystemEntry7isEmptyEv
inline bool QFileSystemEntry::isEmpty() const
{
    return m_filePath.isEmpty() && m_nativeFilePath.isEmpty();
}

//  from src/corelib/io/qfilesystementry.cpp, line 112, as _ZNK16QFileSystemEntry15resolveFilePathEv
inline void QFileSystemEntry::resolveFilePath() const
{
    if (m_filePath.isEmpty() && !m_nativeFilePath.isEmpty()) {
#ifdef Q_OS_WIN
        m_filePath = QDir::fromNativeSeparators(m_nativeFilePath);
#else
        m_filePath = QDir::fromNativeSeparators(QFile::decodeName(m_nativeFilePath));
#endif
    }
}

//  from src/corelib/io/qfilesystementry.cpp, line 123, as _ZNK16QFileSystemEntry21resolveNativeFilePathEv
inline void QFileSystemEntry::resolveNativeFilePath() const
{
    if (!m_filePath.isEmpty() && m_nativeFilePath.isEmpty()) {
#ifdef Q_OS_WIN
        QString filePath = m_filePath;
        if (isRelative())
            filePath = fixIfRelativeUncPath(m_filePath);
        m_nativeFilePath = QFSFileEnginePrivate::longFileName(QDir::toNativeSeparators(filePath));
#else
        m_nativeFilePath = QFile::encodeName(QDir::toNativeSeparators(m_filePath));
#endif
    }
}
//  -----------------------------------------------------------------------

//  QFileSystemEntry::QFileSystemEntry()
extern "C" Q_DECL_EXPORT
QFileSystemEntry *ritual_ZN16QFileSystemEntryC1Ev() {
  return new QFileSystemEntry();
}

//  QString QFileSystemEntry::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry8filePathEv(
    const QFileSystemEntry *self) {
  return new QString(self->filePath());
}

//  NativePath QFileSystemEntry::nativeFilePath() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QFileSystemEntry14nativeFilePathEv(
    const QFileSystemEntry *self) {
  return new QByteArray(self->nativeFilePath());
}

//  bool QFileSystemEntry::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemEntry6isRootEv(const QFileSystemEntry *self) {
  return self->isRoot();
}

//  bool QFileSystemEntry::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemEntry7isEmptyEv(const QFileSystemEntry *self) {
  return self->isEmpty();
}

//  void QFileSystemEntry::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemEntry5clearEv(QFileSystemEntry *self) {
  self->clear();
}

//  bool QFileSystemEntry::isRootPath(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemEntry10isRootPathERK7QString(
    const QString *path) {
  return QFileSystemEntry::isRootPath(*path);
}

//  void QFileSystemEntry::resolveFilePath() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileSystemEntry15resolveFilePathEv(
    const QFileSystemEntry *self) {
  self->resolveFilePath();
}

//  void QFileSystemEntry::resolveNativeFilePath() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileSystemEntry21resolveNativeFilePathEv(
    const QFileSystemEntry *self) {
  self->resolveNativeFilePath();
}

//  QFileSystemEntry::~QFileSystemEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemEntryD1Ev(QFileSystemEntry *self) {
  delete self;
}
