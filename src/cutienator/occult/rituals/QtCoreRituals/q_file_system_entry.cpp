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

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystementry.cpp, line 21, as local:qfilesystementry.cpp:Uninitialized
constexpr int Uninitialized = -2;

//  from src/corelib/io/qfilesystementry.cpp, line 319, as _ZNK16QFileSystemEntry17findLastSeparatorEv
inline void QFileSystemEntry::findLastSeparator() const
{
    if (m_lastSeparator == Uninitialized) {
        resolveFilePath();
        m_lastSeparator = m_filePath.lastIndexOf(u'/');
    }
}

//  from src/corelib/io/qfilesystementry.cpp, line 327, as _ZNK16QFileSystemEntry22findFileNameSeparatorsEv
inline void QFileSystemEntry::findFileNameSeparators() const
{
    if (m_firstDotInFileName == Uninitialized) {
        resolveFilePath();
        int firstDotInFileName = -1;
        int lastDotInFileName = -1;
        int lastSeparator = m_lastSeparator;

        int stop;
        if (lastSeparator < 0) {
            lastSeparator = -1;
            stop = 0;
        } else {
            stop = lastSeparator;
        }

        Q_ASSERT(m_filePath.size() == int(m_filePath.size()));
        int i = int(m_filePath.size() - 1);
        for (; i >= stop; --i) {
            if (m_filePath.at(i).unicode() == '.') {
                firstDotInFileName = lastDotInFileName = i;
                break;
            } else if (m_filePath.at(i).unicode() == '/') {
                lastSeparator = i;
                break;
            }
        }

        if (lastSeparator != i) {
            for (--i; i >= stop; --i) {
                if (m_filePath.at(i).unicode() == '.')
                    firstDotInFileName = i;
                else if (m_filePath.at(i).unicode() == '/') {
                    lastSeparator = i;
                    break;
                }
            }
        }
        m_lastSeparator = lastSeparator;
        m_firstDotInFileName = firstDotInFileName == -1 ? -1 : firstDotInFileName - qMax(0, lastSeparator);
        if (lastDotInFileName == -1)
            m_lastDotInFileName = -1;
        else if (firstDotInFileName == lastDotInFileName)
            m_lastDotInFileName = 0;
        else
            m_lastDotInFileName = lastDotInFileName - firstDotInFileName;
    }
}

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

//  from src/corelib/io/qfilesystementry.cpp, line 147, as _ZNK16QFileSystemEntry4pathEv
#if defined(Q_OS_LINUX)
inline QString QFileSystemEntry::path() const
{
    findLastSeparator();
    if (m_lastSeparator == -1) {
#if defined(Q_OS_WIN)
        if (m_filePath.length() >= 2 && m_filePath.at(1) == u':')
            return m_filePath.left(2);
#endif
        return QString(u'.');
    }
    if (m_lastSeparator == 0)
        return QString(u'/');
#if defined(Q_OS_WIN)
    if (m_lastSeparator == 2 && m_filePath.at(1) == u':')
        return m_filePath.left(m_lastSeparator + 1);
#endif
    return m_filePath.left(m_lastSeparator);
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystementry.cpp, line 106, as _ZNK16QFileSystemEntry14nativeFilePathEv
inline QFileSystemEntry::NativePath QFileSystemEntry::nativeFilePath() const
{
    resolveNativeFilePath();
    return m_nativeFilePath;
}

//  from src/corelib/io/qfilesystementry.cpp, line 166, as _ZNK16QFileSystemEntry8baseNameEv
#if defined(Q_OS_LINUX)
inline QString QFileSystemEntry::baseName() const
{
    findFileNameSeparators();
    int length = -1;
    if (m_firstDotInFileName >= 0) {
        length = m_firstDotInFileName;
        if (m_lastSeparator != -1) // avoid off by one
            length--;
    }
#if defined(Q_OS_WIN)
    if (m_lastSeparator == -1 && m_filePath.length() >= 2 && m_filePath.at(1) == u':')
        return m_filePath.mid(2, length - 2);
#endif
    return m_filePath.mid(m_lastSeparator + 1, length);
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystementry.cpp, line 182, as _ZNK16QFileSystemEntry16completeBaseNameEv
#if defined(Q_OS_LINUX)
inline QString QFileSystemEntry::completeBaseName() const
{
    findFileNameSeparators();
    int length = -1;
    if (m_firstDotInFileName >= 0) {
        length = m_firstDotInFileName + m_lastDotInFileName;
        if (m_lastSeparator != -1) // avoid off by one
            length--;
    }
#if defined(Q_OS_WIN)
    if (m_lastSeparator == -1 && m_filePath.length() >= 2 && m_filePath.at(1) == u':')
        return m_filePath.mid(2, length - 2);
#endif
    return m_filePath.mid(m_lastSeparator + 1, length);
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystementry.cpp, line 198, as _ZNK16QFileSystemEntry6suffixEv
inline QString QFileSystemEntry::suffix() const
{
    findFileNameSeparators();

    if (m_lastDotInFileName == -1)
        return QString();

    return m_filePath.mid(qMax((qint16)0, m_lastSeparator) + m_firstDotInFileName + m_lastDotInFileName + 1);
}

//  from src/corelib/io/qfilesystementry.cpp, line 208, as _ZNK16QFileSystemEntry14completeSuffixEv
inline QString QFileSystemEntry::completeSuffix() const
{
    findFileNameSeparators();
    if (m_firstDotInFileName == -1)
        return QString();

    return m_filePath.mid(qMax((qint16)0, m_lastSeparator) + m_firstDotInFileName + 1);
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
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystementry.cpp, line 123, as _ZNK16QFileSystemEntry21resolveNativeFilePathEv
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)
//  -----------------------------------------------------------------------

//  QFileSystemEntry::QFileSystemEntry()
extern "C" Q_DECL_EXPORT
QFileSystemEntry *ritual_ZN16QFileSystemEntryC1Ev() {
  return new QFileSystemEntry();
}

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry8filePathEv(
    const QFileSystemEntry *self) {
  return new QString(self->filePath());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry8fileNameEv(
    const QFileSystemEntry *self) {
  return new QString(self->fileName());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry4pathEv(const QFileSystemEntry *self) {
  return new QString(self->path());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  NativePath QFileSystemEntry::nativeFilePath() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QFileSystemEntry14nativeFilePathEv(
    const QFileSystemEntry *self) {
  return new QByteArray(self->nativeFilePath());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::baseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry8baseNameEv(
    const QFileSystemEntry *self) {
  return new QString(self->baseName());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::completeBaseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry16completeBaseNameEv(
    const QFileSystemEntry *self) {
  return new QString(self->completeBaseName());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry6suffixEv(
    const QFileSystemEntry *self) {
  return new QString(self->suffix());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEntry::completeSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemEntry14completeSuffixEv(
    const QFileSystemEntry *self) {
  return new QString(self->completeSuffix());
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  bool QFileSystemEntry::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemEntry6isRootEv(const QFileSystemEntry *self) {
  return self->isRoot();
}
#endif  // defined(Q_OS_LINUX)

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

#if defined(Q_OS_LINUX)
//  void QFileSystemEntry::resolveFilePath() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileSystemEntry15resolveFilePathEv(
    const QFileSystemEntry *self) {
  self->resolveFilePath();
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QFileSystemEntry::resolveNativeFilePath() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileSystemEntry21resolveNativeFilePathEv(
    const QFileSystemEntry *self) {
  self->resolveNativeFilePath();
}
#endif  // defined(Q_OS_LINUX)

//  QFileSystemEntry::~QFileSystemEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemEntryD1Ev(QFileSystemEntry *self) {
  delete self;
}
