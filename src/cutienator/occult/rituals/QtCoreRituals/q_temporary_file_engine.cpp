//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-27: code taken from Qt's source no longer stands under
//  defined(Q_OS_LINUX), which Qt does not write there; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(temporaryfile)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#include <QtCore/QFlags>
#include <QtCore/QIODeviceBase>
#include <optional>
#include <QtCore/QFile>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfsfileengine_p.h>
#include <QtCore/private/qfsfileengine_iterator_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qset.h>
#include <QtCore/qdebug.h>
#ifndef QT_NO_FSFILEENGINE
#include <errno.h>
#if defined(Q_OS_UNIX)
#include <QtCore/private/qcore_unix_p.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#if defined(Q_OS_DARWIN)
# include <QtCore/private/qcore_mac_p.h>
#endif
#endif
#include <QtCore/qtemporaryfile.h>
#include "qplatformdefs.h"
#include <QtCore/qrandom.h>
#include <QtCore/private/qtemporaryfile_p.h>
#include <QtCore/private/qfile_p.h>
#include <QtCore/private/qsystemerror_p.h>
#if !defined(Q_OS_WIN)
#include <QtCore/private/qcore_unix_p.h>       // overrides QT_OPEN
#include <errno.h>
#endif
#if defined(QT_BUILD_CORE_LIB)
#include <QtCore/qcoreapplication.h>
#else
#endif
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystementry.cpp, line 21, as local:qfilesystementry.cpp:Uninitialized
constexpr int Uninitialized = -2;

//  from src/corelib/io/qtemporaryfile.cpp, line 37, as local:qtemporaryfile.cpp:NativeFileHandle
#if defined(Q_OS_WIN)
typedef HANDLE NativeFileHandle;
#endif  // defined(Q_OS_WIN)

//  from src/corelib/io/qtemporaryfile.cpp, line 232, as local:qtemporaryfile.cpp:CreateUnnamedFileStatus
#if QT_CONFIG(temporaryfile)
enum class CreateUnnamedFileStatus {
    Success = 0,
    NotSupported,
    OtherError
};
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qfsfileengine.cpp, line 464, as _ZN20QFSFileEnginePrivate8unmapAllEv
#if !defined(QT_NO_FSFILEENGINE)
inline void QFSFileEnginePrivate::unmapAll()
{
    if (!maps.isEmpty()) {
        const QList<uchar*> keys = maps.keys(); // Make a copy since unmap() modifies the map.
        for (int i = 0; i < keys.size(); ++i)
            unmap(keys.at(i));
    }
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qtemporaryfile.cpp, line 304, as _ZN20QTemporaryFileEngine11setFileNameERK7QString
#if QT_CONFIG(temporaryfile)
inline void QTemporaryFileEngine::setFileName(const QString &file)
{
    // Really close the file, so we don't leak
    QFSFileEngine::close();
    QFSFileEngine::setFileName(file);
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 389, as _ZN20QTemporaryFileEngine15renameOverwriteERK7QString
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::renameOverwrite(const QString &newName)
{
    if (isUnnamedFile()) {
        bool ok = materializeUnnamedFile(newName, Overwrite);
        QFSFileEngine::close();
        return ok;
    }
#ifdef Q_OS_WIN
    if (flags & Win32NonShared) {
        QFileSystemEntry newEntry(newName, QFileSystemEntry::FromInternalPath());
        bool ok = d_func()->nativeRenameOverwrite(newEntry);
        QFSFileEngine::close();
        if (ok) {
            // Match what QFSFileEngine::renameOverwrite() does
            setFileEntry(std::move(newEntry));
        }
        return ok;
    }
#endif
    QFSFileEngine::close();
    return QFSFileEngine::renameOverwrite(newName);
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 412, as _ZN20QTemporaryFileEngine5closeEv
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::close()
{
    // Don't close the file, just seek to the front.
    seek(0);
    setError(QFile::UnspecifiedError, QString());
    return true;
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 356, as _ZN20QTemporaryFileEngine6removeEv
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::remove()
{
    Q_D(QFSFileEngine);
    // Since the QTemporaryFileEngine::close() does not really close the file,
    // we must explicitly call QFSFileEngine::close() before we remove it.
    d->unmapAll();
    QFSFileEngine::close();
    if (isUnnamedFile())
        return true;
    if (!filePathIsTemplate && QFSFileEngine::remove()) {
        d->fileEntry.clear();
        // If a QTemporaryFile is constructed using a template file path, the path
        // is generated in QTemporaryFileEngine::open() and then filePathIsTemplate
        // is set to false. If remove() and then open() are called on the same
        // QTemporaryFile, the path is not regenerated. Here we ensure that if the
        // file path was generated, it will be generated again in the scenario above.
        filePathIsTemplate = filePathWasTemplate;
        return true;
    }
    return false;
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 378, as _ZN20QTemporaryFileEngine6renameERK7QString
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::rename(const QString &newName)
{
    if (isUnnamedFile()) {
        bool ok = materializeUnnamedFile(newName, DontOverwrite);
        QFSFileEngine::close();
        return ok;
    }
    QFSFileEngine::close();
    return QFSFileEngine::rename(newName);
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qfilesystementry.cpp, line 312, as _ZNK16QFileSystemEntry7isEmptyEv
inline bool QFileSystemEntry::isEmpty() const
{
    return m_filePath.isEmpty() && m_nativeFilePath.isEmpty();
}

//  from src/corelib/io/qtemporaryfile.cpp, line 420, as _ZNK20QTemporaryFileEngine8fileNameEN19QAbstractFileEngine8FileNameE
#if QT_CONFIG(temporaryfile)
inline QString QTemporaryFileEngine::fileName(QAbstractFileEngine::FileName file) const
{
    if (isUnnamedFile()) {
        if (file == AbsoluteLinkTarget || file == RawLinkPath) {
            // we know our file isn't (won't be) a symlink
            return QString();
        }

        // for all other cases, materialize the file
        const_cast<QTemporaryFileEngine *>(this)->materializeUnnamedFile(templateName, NameIsTemplate);
    }
    return QFSFileEngine::fileName(file);
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qtemporaryfile.cpp, line 434, as _ZN20QTemporaryFileEngine22materializeUnnamedFileERK7QStringNS_19MaterializationModeE
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::materializeUnnamedFile(const QString &newName, QTemporaryFileEngine::MaterializationMode mode)
{
    Q_ASSERT(isUnnamedFile());

#ifdef LINUX_UNNAMED_TMPFILE
    Q_D(QFSFileEngine);
    const QByteArray src = "/proc/self/fd/" + QByteArray::number(d->fd);
    auto materializeAt = [=](const QFileSystemEntry &dst) {
        return ::linkat(AT_FDCWD, src, AT_FDCWD, dst.nativeFilePath(), AT_SYMLINK_FOLLOW) == 0;
    };
#else
    auto materializeAt = [](const QFileSystemEntry &) { return false; };
#endif

    auto success = [this](const QFileSystemEntry &entry) {
        filePathIsTemplate = false;
        unnamedFile = false;
        d_func()->fileEntry = entry;
        return true;
    };

    auto materializeAsTemplate = [=](const QString &newName) {
        QTemporaryFileName tfn(newName);
        static const int maxAttempts = 16;
        for (int attempt = 0; attempt < maxAttempts; ++attempt) {
            tfn.generateNext();
            QFileSystemEntry entry(tfn.path, QFileSystemEntry::FromNativePath());
            if (materializeAt(entry))
                return success(entry);
        }
        return false;
    };

    if (mode == NameIsTemplate) {
        if (materializeAsTemplate(newName))
            return true;
    } else {
        // Use linkat to materialize the file
        QFileSystemEntry dst(newName);
        if (materializeAt(dst))
            return success(dst);

        if (errno == EEXIST && mode == Overwrite) {
            // retry by first creating a temporary file in the right dir
            if (!materializeAsTemplate(templateName))
                return false;

            // then rename the materialized file to target (same as renameOverwrite)
            QFSFileEngine::close();
            return QFSFileEngine::renameOverwrite(newName);
        }
    }

    // failed
    setError(QFile::RenameError, QSystemError(errno, QSystemError::NativeError).toString());
    return false;
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 282, as _ZN20QTemporaryFileEngineD1Ev
#if QT_CONFIG(temporaryfile)
inline QTemporaryFileEngine::~QTemporaryFileEngine()
{
    Q_D(QFSFileEngine);
    d->unmapAll();
    QFSFileEngine::close();
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 289, as _ZNK20QTemporaryFileEngine12isReallyOpenEv
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::isReallyOpen() const
{
    Q_D(const QFSFileEngine);

    if (!((nullptr == d->fh) && (-1 == d->fd)
#if defined Q_OS_WIN
                && (INVALID_HANDLE_VALUE == d->fileHandle)
#endif
            ))
        return true;

    return false;

}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 492, as _ZNK20QTemporaryFileEngine13isUnnamedFileEv
#if QT_CONFIG(temporaryfile)
inline bool QTemporaryFileEngine::isUnnamedFile() const
{
#ifdef LINUX_UNNAMED_TMPFILE
    if (unnamedFile) {
        Q_ASSERT(d_func()->fileEntry.isEmpty());
        Q_ASSERT(filePathIsTemplate);
    }
    return unnamedFile;
#else
    return false;
#endif
}
#endif  // QT_CONFIG(temporaryfile)
//  -----------------------------------------------------------------------

//  A QTemporaryFileEngine that Python can take functions over in. Every QTemporaryFileEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(temporaryfile)
typedef void (*CuteQTemporaryFileEngineCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQTemporaryFileEngineCall1)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQTemporaryFileEngineCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQTemporaryFileEngineCall3)(const void *, const QString *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQTemporaryFileEngineCall4)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef QString * (*CuteQTemporaryFileEngineCall5)(const void *, int, int *);
#endif  // QT_CONFIG(temporaryfile)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall6)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall7)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQTemporaryFileEngineCall8)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQTemporaryFileEngineCall9)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall10)(const void *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall11)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall12)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall13)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall14)(const void *, const QString *, bool, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall15)(const void *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall16)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall17)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQTemporaryFileEngineCall18)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall19)(const void *, uint, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef const QByteArray * (*CuteQTemporaryFileEngineCall20)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef uint (*CuteQTemporaryFileEngineCall21)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef QString * (*CuteQTemporaryFileEngineCall22)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQTemporaryFileEngineCall23)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQTemporaryFileEngineCall24)(const void *, char *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQTemporaryFileEngineCall25)(const void *, char *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQTemporaryFileEngineCall26)(const void *, QAbstractFileEngine *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall27)(const void *, int, const QAbstractFileEngine::ExtensionOption *, QAbstractFileEngine::ExtensionReturn *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQTemporaryFileEngineCall28)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
class CuteQTemporaryFileEngine : public QTemporaryFileEngine {
public:
  using QTemporaryFileEngine::QTemporaryFileEngine;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine11setFileNameERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6removeEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6renameERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine15renameOverwriteERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5closeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5flushEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine10syncToDiskEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine4sizeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine3posEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4seekEx")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine12isSequentialEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4copyERK7QString")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4linkERK7QString")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5rmdirERK7QStringb")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7setSizeEx")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine13caseSensitiveEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine14isRelativePathEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine14setPermissionsEj")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine2idEv")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine6handleEv")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4readEPcx")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine8readLineEPcx")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7cloneToEPS_")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
    return false;
  }

#if QT_CONFIG(temporaryfile)
  //  void QTemporaryFileEngine::setFileName(const QString &file)
  void setFileName(const QString &file) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall0 call = reinterpret_cast<CuteQTemporaryFileEngineCall0>(taken[0]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QTemporaryFileEngine::setFileName(file);
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QTemporaryFileEngine::remove()
  bool remove() override {
    if (taken[1]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall1 call = reinterpret_cast<CuteQTemporaryFileEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTemporaryFileEngine::remove();
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QTemporaryFileEngine::rename(const QString &newName)
  bool rename(const QString &newName) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall2 call = reinterpret_cast<CuteQTemporaryFileEngineCall2>(taken[2]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QTemporaryFileEngine::rename(newName);
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QTemporaryFileEngine::renameOverwrite(const QString &newName)
  bool renameOverwrite(const QString &newName) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall3 call = reinterpret_cast<CuteQTemporaryFileEngineCall3>(taken[3]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QTemporaryFileEngine::renameOverwrite(newName);
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QTemporaryFileEngine::close()
  bool close() override {
    if (taken[4]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall4 call = reinterpret_cast<CuteQTemporaryFileEngineCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTemporaryFileEngine::close();
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  QString QTemporaryFileEngine::fileName(FileName file) const
  QString fileName(QAbstractFileEngine::FileName file) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall5 call = reinterpret_cast<CuteQTemporaryFileEngineCall5>(taken[5]);
      QString * given = call(this, static_cast<int>(file), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTemporaryFileEngine::fileName(file);
  }
#endif  // QT_CONFIG(temporaryfile)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::flush()
  bool flush() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall6 call = reinterpret_cast<CuteQTemporaryFileEngineCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::flush();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::syncToDisk()
  bool syncToDisk() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall7 call = reinterpret_cast<CuteQTemporaryFileEngineCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::syncToDisk();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::size() const
  qint64 size() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall8 call = reinterpret_cast<CuteQTemporaryFileEngineCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::size();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::pos() const
  qint64 pos() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall9 call = reinterpret_cast<CuteQTemporaryFileEngineCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::pos();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::seek(qint64 a0)
  bool seek(qint64 a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall10 call = reinterpret_cast<CuteQTemporaryFileEngineCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::seek(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::isSequential() const
  bool isSequential() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall11 call = reinterpret_cast<CuteQTemporaryFileEngineCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::isSequential();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::copy(const QString &newName)
  bool copy(const QString &newName) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall12 call = reinterpret_cast<CuteQTemporaryFileEngineCall12>(taken[12]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::copy(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::link(const QString &newName)
  bool link(const QString &newName) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall13 call = reinterpret_cast<CuteQTemporaryFileEngineCall13>(taken[13]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::link(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::rmdir(const QString &dirName, bool
  //      recurseParentDirectories) const
  bool rmdir(
      const QString &dirName,
      bool recurseParentDirectories) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall14 call = reinterpret_cast<CuteQTemporaryFileEngineCall14>(taken[14]);
      bool given = call(this, &dirName, recurseParentDirectories, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::rmdir(dirName, recurseParentDirectories);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::setSize(qint64 size)
  bool setSize(qint64 size) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall15 call = reinterpret_cast<CuteQTemporaryFileEngineCall15>(taken[15]);
      bool given = call(this, size, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::setSize(size);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::caseSensitive() const
  bool caseSensitive() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall16 call = reinterpret_cast<CuteQTemporaryFileEngineCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::caseSensitive();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::isRelativePath() const
  bool isRelativePath() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall17 call = reinterpret_cast<CuteQTemporaryFileEngineCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::isRelativePath();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  FileFlags QFSFileEngine::fileFlags(FileFlags type) const
  QAbstractFileEngine::FileFlags fileFlags(
      QAbstractFileEngine::FileFlags type) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall18 call = reinterpret_cast<CuteQTemporaryFileEngineCall18>(taken[18]);
      int given = call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return QFlags<QAbstractFileEngine::FileFlag>::fromInt(given);
    }
    return QFSFileEngine::fileFlags(type);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::setPermissions(uint perms)
  bool setPermissions(uint perms) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall19 call = reinterpret_cast<CuteQTemporaryFileEngineCall19>(taken[19]);
      bool given = call(this, perms, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::setPermissions(perms);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  QByteArray QFSFileEngine::id() const
  QByteArray id() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall20 call = reinterpret_cast<CuteQTemporaryFileEngineCall20>(taken[20]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFSFileEngine::id();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  uint QFSFileEngine::ownerId(FileOwner a0) const
  uint ownerId(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall21 call = reinterpret_cast<CuteQTemporaryFileEngineCall21>(taken[21]);
      uint given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QFSFileEngine::ownerId(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  QString QFSFileEngine::owner(FileOwner a0) const
  QString owner(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall22 call = reinterpret_cast<CuteQTemporaryFileEngineCall22>(taken[22]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFSFileEngine::owner(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  int QFSFileEngine::handle() const
  int handle() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall23 call = reinterpret_cast<CuteQTemporaryFileEngineCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::handle();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall24 call = reinterpret_cast<CuteQTemporaryFileEngineCall24>(taken[24]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::read(data, maxlen);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::readLine(char *data, qint64 maxlen)
  qint64 readLine(char *data, qint64 maxlen) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall25 call = reinterpret_cast<CuteQTemporaryFileEngineCall25>(taken[25]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::readLine(data, maxlen);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine *target)
  QAbstractFileEngine::TriStateResult cloneTo(
      QAbstractFileEngine *target) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall26 call = reinterpret_cast<CuteQTemporaryFileEngineCall26>(taken[26]);
      int given = call(this, target, &handled);
      if (handled) return static_cast<QAbstractFileEngine::TriStateResult>(given);
    }
    return QFSFileEngine::cloneTo(target);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::extension(Extension extension, const
  //      ExtensionOption *option, ExtensionReturn *output)
  bool extension(
      QAbstractFileEngine::Extension extension,
      const QAbstractFileEngine::ExtensionOption *option,
      QAbstractFileEngine::ExtensionReturn *output) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall27 call = reinterpret_cast<CuteQTemporaryFileEngineCall27>(taken[27]);
      bool given = call(this, static_cast<int>(extension), option, output, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::extension(extension, option, output);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::supportsExtension(Extension extension) const
  bool supportsExtension(
      QAbstractFileEngine::Extension extension) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQTemporaryFileEngineCall28 call = reinterpret_cast<CuteQTemporaryFileEngineCall28>(taken[28]);
      bool given = call(this, static_cast<int>(extension), &handled);
      if (handled) return given;
    }
    return QFSFileEngine::supportsExtension(extension);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)
};

//  QFSFileEnginePrivate *QTemporaryFileEngine::d_func()
extern "C" Q_DECL_EXPORT
QFSFileEnginePrivate *ritual_ZN20QTemporaryFileEngine6d_funcEv(
    QTemporaryFileEngine *self) {
  return self->d_func();
}

//  const QFSFileEnginePrivate *QTemporaryFileEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QFSFileEnginePrivate *ritual_ZNK20QTemporaryFileEngine6d_funcEv(
    const QTemporaryFileEngine *self) {
  return self->d_func();
}

//  QTemporaryFileEngine::~QTemporaryFileEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTemporaryFileEngineD1Ev(QTemporaryFileEngine *self) {
  delete self;
}

#if QT_CONFIG(temporaryfile)
//  bool QTemporaryFileEngine::isReallyOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTemporaryFileEngine12isReallyOpenEv(
    const QTemporaryFileEngine *self) {
  return self->isReallyOpen();
}
#endif  // QT_CONFIG(temporaryfile)

//  void QTemporaryFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTemporaryFileEngine11setFileNameERK7QString(
    QTemporaryFileEngine *self,
    const QString *file) {
  self->setFileName(*file);
}

//  bool QTemporaryFileEngine::open(QIODevice::OpenMode flags,
//      std::optional<QFile::Permissions> permissions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTemporaryFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEESt8optionalIS0_IN11QFileDevice10PermissionEEE(
    QTemporaryFileEngine *self,
    int flags,
    const std::optional<QFile::Permissions> *permissions) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      *permissions);
}

//  bool QTemporaryFileEngine::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTemporaryFileEngine6removeEv(QTemporaryFileEngine *self) {
  return self->remove();
}

//  bool QTemporaryFileEngine::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTemporaryFileEngine6renameERK7QString(
    QTemporaryFileEngine *self,
    const QString *newName) {
  return self->rename(*newName);
}

//  bool QTemporaryFileEngine::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTemporaryFileEngine15renameOverwriteERK7QString(
    QTemporaryFileEngine *self,
    const QString *newName) {
  return self->renameOverwrite(*newName);
}

//  bool QTemporaryFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTemporaryFileEngine5closeEv(QTemporaryFileEngine *self) {
  return self->close();
}

//  QString QTemporaryFileEngine::fileName(FileName file) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QTemporaryFileEngine8fileNameEN19QAbstractFileEngine8FileNameE(
    const QTemporaryFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->fileName(file));
}

#if QT_CONFIG(temporaryfile)
//  bool QTemporaryFileEngine::isUnnamedFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTemporaryFileEngine13isUnnamedFileEv(
    const QTemporaryFileEngine *self) {
  return self->isUnnamedFile();
}
#endif  // QT_CONFIG(temporaryfile)

//  a Python function taken by a CuteQTemporaryFileEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTemporaryFileEngine(
    QTemporaryFileEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTemporaryFileEngine *>(self)->take(key, call);
}

#if QT_CONFIG(temporaryfile)
//  void QTemporaryFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QTemporaryFileEngine11setFileNameERK7QString(
    QTemporaryFileEngine *self,
    const QString *file) {
  self->QTemporaryFileEngine::setFileName(*file);
}
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
//  bool QTemporaryFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTemporaryFileEngine5closeEv(
    QTemporaryFileEngine *self) {
  return self->QTemporaryFileEngine::close();
}
#endif  // QT_CONFIG(temporaryfile)

#endif  // QT_CONFIG(temporaryfile)
