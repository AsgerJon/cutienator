//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdir_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdir_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#include "qplatformdefs.h"
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifndef QT_NO_DEBUG_STREAM
#include <QtCore/qdebug.h>
#endif
#include <QtCore/qdirlisting.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(regularexpression)
#  include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qvarlengtharray.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/private/qfilesystemmetadata_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qstringbuilder.h>
#ifndef QT_BOOTSTRAPPED
#  include <QtCore/qcollator.h>
#  include <QtCore/qreadwritelock.h>
#  include <QtCore/qmutex.h>
#endif
#include <QtCore/private/qorderedmutexlocker_p.h>
#include <algorithm>
#include <memory>
#include <stack>
#include <stdlib.h>
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

//  from src/corelib/io/qdir.cpp, line 106, as _ZN11QDirPrivateC1ERKS_
inline QDirPrivate::QDirPrivate(const QDirPrivate &copy)
    : QSharedData(copy),
      // mutex is not copied
      nameFilters(copy.nameFilters),
      sort(copy.sort),
      filters(copy.filters),
      // fileEngine is not copied
      dirEntry(copy.dirEntry)
{
    QMutexLocker locker(&copy.fileCache.mutex);
    fileCache.fileListsInitialized = copy.fileCache.fileListsInitialized.load();
    fileCache.files = copy.fileCache.files;
    fileCache.fileInfos = copy.fileCache.fileInfos;
    fileCache.absoluteDirEntry = copy.fileCache.absoluteDirEntry;
    fileCache.metaData = copy.fileCache.metaData;
}

//  from src/corelib/io/qdir.cpp, line 418, as _ZN11QDirPrivate17toDirListingFlagsE6QFlagsIN4QDir6FilterEE
#if !defined(QT_BOOTSTRAPPED)
inline QDirListing::IteratorFlags QDirPrivate::toDirListingFlags(QDir::Filters filters)
{
    if (filters == QDir::NoFilter)
        filters = QDir::AllEntries;

    using F = QDirListing::IteratorFlag;
    QDirListing::IteratorFlags flags;
    if (!(filters & QDir::Dirs) && !(filters & QDir::AllDirs))
        flags |= F::ExcludeDirs;
    if (!(filters & QDir::Files))
        flags |= F::ExcludeFiles;
    if (!(filters & QDir::NoSymLinks))
        flags |= F::ResolveSymlinks;
    if (filters & QDir::Hidden)
        flags |= F::IncludeHidden;

    if (!(filters & QDir::System))
        flags |= F::ExcludeOther;
    else
        flags |= F::IncludeBrokenSymlinks; // QDir::System lists broken symlinks...


    if (filters & QDir::AllDirs)
        flags |= F::NoNameFiltersForDirs;
    if (filters & QDir::CaseSensitive)
        flags |= F::CaseSensitive;

    // QDir::Filter has NoDot and NoDotDot; QDirListing has only one,
    // F::IncludeDotAndDotDot. If either of the QDir::Filter values are
    // not set, list both and use checkDotOrDotDot() to filter it later.
    if (!(filters & QDir::NoDot) || !(filters & QDir::NoDotDot)) {
        if (!(flags & F::ExcludeDirs)) // treat '.' and '..' as dirs
            flags |= F::IncludeDotAndDotDot;
    }

    return flags;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qdir.cpp, line 143, as _ZN11QDirPrivate16getFilterSepCharERK7QString
inline QChar QDirPrivate::getFilterSepChar(const QString &nameFilter)
{
    QChar sep(u';');
    qsizetype i = nameFilter.indexOf(sep, 0);
    if (i == -1 && nameFilter.indexOf(u' ', 0) != -1)
        sep = QChar(u' ');
    return sep;
}

//  from src/corelib/io/qdir.cpp, line 153, as _ZN11QDirPrivate12splitFiltersERK7QString5QChar
inline QStringList QDirPrivate::splitFilters(const QString &nameFilter, QChar sep)
{
    if (sep.isNull())
        sep = getFilterSepChar(nameFilter);
    QStringList ret;
    for (auto e : qTokenize(nameFilter, sep))
        ret.append(e.trimmed().toString());
    return ret;
}
//  -----------------------------------------------------------------------

//  QDirPrivate::QDirPrivate(const QDirPrivate &copy)
extern "C" Q_DECL_EXPORT
QDirPrivate *ritual_ZN11QDirPrivateC1ERKS_(const QDirPrivate *copy) {
  return new QDirPrivate(*copy);
}

#if !defined(QT_BOOTSTRAPPED)
//  QDirListing::IteratorFlags QDirPrivate::toDirListingFlags(QDir::Filters
//      filters)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QDirPrivate17toDirListingFlagsE6QFlagsIN4QDir6FilterEE(
    int filters) {
  return static_cast<int>(
      QDirPrivate::toDirListingFlags(
          QFlags<QDir::Filter>::fromInt(filters)).toInt());
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QChar QDirPrivate::getFilterSepChar(const QString &nameFilter)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN11QDirPrivate16getFilterSepCharERK7QString(
    const QString *nameFilter) {
  return new QChar(QDirPrivate::getFilterSepChar(*nameFilter));
}

//  QStringList QDirPrivate::splitFilters(const QString &nameFilter, QChar
//      sep)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QDirPrivate12splitFiltersERK7QString5QChar(
    const QString *nameFilter,
    const QChar *sep) {
  return new QList<QString>(QDirPrivate::splitFilters(*nameFilter, *sep));
}

//  QDirPrivate::~QDirPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirPrivateD1Ev(QDirPrivate *self) {
  delete self;
}
