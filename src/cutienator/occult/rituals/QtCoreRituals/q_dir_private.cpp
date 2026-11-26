//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdir_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdir_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdirlisting.h>
#include <QtCore/qdir.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qdir.cpp, line 206, as local:qdir.cpp:QDirSortItem
struct QDirSortItem
{
    QDirSortItem() = default;
    QDirSortItem(const QFileInfo &fi, QDir::SortFlags sort)
        : item(fi)
    {
        // A dir e.g. "dirA.bar" doesn't have actually have an extension/suffix, when
        // sorting by type such "suffix" should be ignored but that would complicate
        // the code and uses can change the behavior by setting DirsFirst/DirsLast
        if (sort.testAnyFlag(QDir::Type))
            suffix_cache = item.suffix();
    }

    mutable QString filename_cache;
    QString suffix_cache;
    QFileInfo item;
};

//  from src/corelib/io/qdir.cpp, line 224, as local:qdir.cpp:QDirSortItemComparator
class QDirSortItemComparator
{
    QDir::SortFlags qt_cmp_si_sort_flags;

#ifndef QT_BOOTSTRAPPED
    QCollator *collator = nullptr;
#endif
public:
#ifndef QT_BOOTSTRAPPED
    QDirSortItemComparator(QDir::SortFlags flags, QCollator *coll = nullptr)
        : qt_cmp_si_sort_flags(flags), collator(coll)
    {
        Q_ASSERT(!qt_cmp_si_sort_flags.testAnyFlag(QDir::LocaleAware) || collator);

        if (collator && qt_cmp_si_sort_flags.testAnyFlag(QDir::IgnoreCase))
            collator->setCaseSensitivity(Qt::CaseInsensitive);
    }
#else
    QDirSortItemComparator(QDir::SortFlags flags)
        : qt_cmp_si_sort_flags(flags)
    {
    }
#endif
    bool operator()(const QDirSortItem &, const QDirSortItem &) const;

    int compareStrings(const QString &a, const QString &b, Qt::CaseSensitivity cs) const
    {
#ifndef QT_BOOTSTRAPPED
        if (collator)
            return collator->compare(a, b);
#endif
        return a.compare(b, cs);
    }
};

//  from src/corelib/io/qdir.cpp, line 259, as local:qdir.cpp:QDirSortItemComparator::operator
inline bool QDirSortItemComparator::operator()(const QDirSortItem &n1, const QDirSortItem &n2) const
{
    const QDirSortItem* f1 = &n1;
    const QDirSortItem* f2 = &n2;

    if ((qt_cmp_si_sort_flags & QDir::DirsFirst) && (f1->item.isDir() != f2->item.isDir()))
        return f1->item.isDir();
    if ((qt_cmp_si_sort_flags & QDir::DirsLast) && (f1->item.isDir() != f2->item.isDir()))
        return !f1->item.isDir();

    const bool ic = qt_cmp_si_sort_flags.testAnyFlag(QDir::IgnoreCase);
    const auto qtcase = ic ? Qt::CaseInsensitive : Qt::CaseSensitive;

    qint64 r = 0;
    int sortBy = ((qt_cmp_si_sort_flags & QDir::SortByMask)
                 | (qt_cmp_si_sort_flags & QDir::Type)).toInt();

    switch (sortBy) {
      case QDir::Time: {
        const QDateTime firstModified = f1->item.lastModified(QTimeZone::UTC);
        const QDateTime secondModified = f2->item.lastModified(QTimeZone::UTC);
        r = firstModified.msecsTo(secondModified);
        break;
      }
      case QDir::Size:
          r = f2->item.size() - f1->item.size();
        break;
    case QDir::Type:
        r = compareStrings(f1->suffix_cache, f2->suffix_cache, qtcase);
        break;
      default:
        ;
    }

    if (r == 0 && sortBy != QDir::Unsorted) {
        // Still not sorted - sort by name

        if (f1->filename_cache.isNull())
            f1->filename_cache = f1->item.fileName();
        if (f2->filename_cache.isNull())
            f2->filename_cache = f2->item.fileName();

        r = compareStrings(f1->filename_cache, f2->filename_cache, qtcase);
    }
    if (qt_cmp_si_sort_flags & QDir::Reversed)
        return r > 0;
    return r < 0;
}

//  from src/corelib/io/qdir.cpp, line 365, as local:qdir.cpp:checkPermissions
#if !defined(QT_BOOTSTRAPPED)
static bool checkPermissions(const QDirListing::DirEntry &dirEntry, QDir::Filters filters)
{
    const auto perms = filters & QDir::PermissionMask;
    const bool filterByPermissions = perms != 0 && perms != QDir::PermissionMask;
    if (filterByPermissions) {
        const QFileInfo fileInfo = dirEntry.fileInfo();
        if (filters.testFlags(QDir::Readable) && !fileInfo.isReadable())
            return false;
        if (filters.testFlags(QDir::Writable) && !fileInfo.isWritable())
            return false;
        if (filters.testFlags(QDir::Executable) && !fileInfo.isExecutable())
            return false;
    }
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qdir.cpp, line 381, as local:qdir.cpp:checkDotOrDotDot
#if !defined(QT_BOOTSTRAPPED)
static bool checkDotOrDotDot(const QDirListing::DirEntry &dirEntry, QDir::Filters filters)
{
    const QString fileName = dirEntry.fileName();
    if ((filters & QDir::NoDot) && fileName == u".")
        return false;
    if ((filters & QDir::NoDotDot) && fileName == u"..")
        return false;
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qdir.cpp, line 403, as local:qdir.cpp:appendIfMatchesNonDirListingFlags
#if !defined(QT_BOOTSTRAPPED)
static void appendIfMatchesNonDirListingFlags(const QDirListing::DirEntry &dirEntry,
                                              QDir::Filters filters, QFileInfoList &l)
{
    if (QDirPrivate::checkNonDirListingFlags(dirEntry, filters))
        l.emplace_back(dirEntry.fileInfo());
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qfilesystemengine.cpp, line 100, as local:qfilesystemengine.cpp:_q_checkEntry
static inline bool _q_checkEntry(QFileSystemEntry &entry, QFileSystemMetaData &data, bool resolvingEntry)
{
    if (resolvingEntry) {
        if (!QFileSystemEngine::fillMetaData(entry, data, QFileSystemMetaData::ExistsAttribute)
                || !data.exists()) {
            data.clear();
            return false;
        }
    }

    return true;
}

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qdir.cpp, line 308, as _ZN11QDirPrivate12sortFileListE6QFlagsIN4QDir8SortFlagEERK5QListI9QFileInfoEPS4_I7QStringEPS6_
inline void QDirPrivate::sortFileList(QDir::SortFlags sort, const QFileInfoList &l,
                                      QStringList *names, QFileInfoList *infos)
{
    Q_ASSERT(names || infos);
    Q_ASSERT(!infos || infos->isEmpty());
    Q_ASSERT(!names || names->isEmpty());

    const qsizetype n = l.size();
    if (n == 0)
        return;

    if (n == 1 || (sort & QDir::SortByMask) == QDir::Unsorted) {
        if (infos)
            *infos = l;

        if (names) {
            for (const QFileInfo &fi : l)
                names->append(fi.fileName());
        }
    } else {
        QVarLengthArray<QDirSortItem, 64> si;
        si.reserve(n);
        for (qsizetype i = 0; i < n; ++i)
            si.emplace_back(l.at(i), sort);

#ifndef QT_BOOTSTRAPPED
    if (sort.testAnyFlag(QDir::LocaleAware)) {
            QCollator coll;
            std::sort(si.data(), si.data() + n, QDirSortItemComparator(sort, &coll));
        } else {
            std::sort(si.data(), si.data() + n, QDirSortItemComparator(sort));
        }
#else
        std::sort(si.data(), si.data() + n, QDirSortItemComparator(sort));
#endif // QT_BOOTSTRAPPED

        // put them back in the list(s)
        for (qsizetype i = 0; i < n; ++i) {
            auto &fileInfo = si[i].item;
            if (infos)
                infos->append(fileInfo);
            if (names) {
                const bool cached = !si[i].filename_cache.isNull();
                names->append(cached ? si[i].filename_cache : fileInfo.fileName());
            }
        }
    }
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

//  from src/corelib/io/qdir.cpp, line 397, as _ZN11QDirPrivate23checkNonDirListingFlagsERKN11QDirListing8DirEntryE6QFlagsIN4QDir6FilterEE
#if !defined(QT_BOOTSTRAPPED)
inline bool QDirPrivate::checkNonDirListingFlags(const QDirListing::DirEntry &dirEntry,
                                          QDir::Filters filters)
{
    return checkPermissions(dirEntry, filters) && checkDotOrDotDot(dirEntry, filters);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qdir.cpp, line 456, as _ZNK11QDirPrivate13initFileListsERK4QDir
#if !defined(QT_BOOTSTRAPPED)
inline void QDirPrivate::initFileLists(const QDir &dir) const
{
    QMutexLocker locker(&fileCache.mutex);
    if (!fileCache.fileListsInitialized) {
        QFileInfoList l;
        QDirListing::IteratorFlags flags = toDirListingFlags(dir.filter());
        for (const auto &dirEntry : QDirListing(dir.path(), dir.nameFilters(), flags))
            appendIfMatchesNonDirListingFlags(dirEntry, dir.filter(), l);

        sortFileList(sort, l, &fileCache.files, &fileCache.fileInfos);
        fileCache.fileListsInitialized = true;
    }
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

#if !defined(QT_BOOTSTRAPPED)
//  bool QDirPrivate::checkNonDirListingFlags(const QDirListing::DirEntry
//      &dirEntry, QDir::Filters filters)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDirPrivate23checkNonDirListingFlagsERKN11QDirListing8DirEntryE6QFlagsIN4QDir6FilterEE(
    const QDirListing::DirEntry *dirEntry,
    int filters) {
  return QDirPrivate::checkNonDirListingFlags(
      *dirEntry,
      QFlags<QDir::Filter>::fromInt(filters));
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  void QDirPrivate::initFileLists(const QDir &dir) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QDirPrivate13initFileListsERK4QDir(
    const QDirPrivate *self,
    const QDir *dir) {
  self->initFileLists(*dir);
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
