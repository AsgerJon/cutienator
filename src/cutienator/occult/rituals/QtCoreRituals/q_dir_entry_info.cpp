//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdirentryinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdirentryinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from src/corelib/io/qfilesystementry.cpp, line 137, as _ZNK16QFileSystemEntry8fileNameEv
inline QString QFileSystemEntry::fileName() const
{
    findLastSeparator();
#if defined(Q_OS_WIN)
    if (m_lastSeparator == -1 && m_filePath.length() >= 2 && m_filePath.at(1) == u':')
        return m_filePath.mid(2);
#endif
    return m_filePath.mid(m_lastSeparator + 1);
}

//  from src/corelib/io/qfilesystementry.cpp, line 166, as _ZNK16QFileSystemEntry8baseNameEv
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

//  from src/corelib/io/qfilesystementry.cpp, line 182, as _ZNK16QFileSystemEntry16completeBaseNameEv
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

//  from src/corelib/io/qfilesystementry.cpp, line 100, as _ZNK16QFileSystemEntry8filePathEv
inline QString QFileSystemEntry::filePath() const
{
    resolveFilePath();
    return m_filePath;
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
//  -----------------------------------------------------------------------

//  QDirEntryInfo::QDirEntryInfo()
extern "C" Q_DECL_EXPORT
QDirEntryInfo *ritual_ZN13QDirEntryInfoC1Ev() {
  return new QDirEntryInfo();
}

//  QDirEntryInfo::QDirEntryInfo(const QAbstractFileEngineIterator *iterator)
extern "C" Q_DECL_EXPORT
QDirEntryInfo *ritual_ZN13QDirEntryInfoC1EPK27QAbstractFileEngineIterator(
    const QAbstractFileEngineIterator *iterator) {
  return new QDirEntryInfo(iterator);
}

//  QString QDirEntryInfo::filePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDirEntryInfo8filePathEv(QDirEntryInfo *self) {
  return new QString(self->filePath());
}

//  QDirEntryInfo::~QDirEntryInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDirEntryInfoD1Ev(QDirEntryInfo *self) {
  delete self;
}
