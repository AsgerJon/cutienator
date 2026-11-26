//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfile_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qfile.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qfiledevice.h>
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#include "qplatformdefs.h"
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/private/qfsfileengine_p.h>
#include <QtCore/qlist.h>
#include <QtCore/qsavefile.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/private/qfile_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/private/qsavefile_p.h>
#include <QtCore/private/qsystemerror_p.h>
#include <QtCore/private/qtemporaryfile_p.h>
#if defined(QT_BUILD_CORE_LIB)
# include <QtCore/qcoreapplication.h>
#endif
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qset.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/private/qabstractfileengine_p.h>
#ifdef QT_BUILD_CORE_LIB
#include <QtCore/private/qresource_p.h>
#endif
#include <QtCore/private/qduplicatetracker_p.h>
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

//  from src/corelib/io/qfiledevice.cpp, line 17, as local:qfiledevice.cpp:QFILE_WRITEBUFFER_SIZE
#define QFILE_WRITEBUFFER_SIZE 16384

//  from src/corelib/io/qfiledevice.cpp, line 507, as _ZN18QFileDevicePrivate13putCharHelperEc
#if defined(Q_OS_LINUX)
inline bool QFileDevicePrivate::putCharHelper(char c)
{
#ifdef QT_NO_QOBJECT
    return QIODevicePrivate::putCharHelper(c);
#else

    // Cutoff for code that doesn't only touch the buffer.
    qint64 writeBufferSize = writeBuffer.size();
    if ((openMode & QIODevice::Unbuffered) || writeBufferSize + 1 >= writeBufferChunkSize
#ifdef Q_OS_WIN
        || ((openMode & QIODevice::Text) && c == '\n'
            && writeBufferSize + 2 >= writeBufferChunkSize)
#endif
        ) {
        return QIODevicePrivate::putCharHelper(c);
    }

    if (!(openMode & QIODevice::WriteOnly)) {
        if (openMode == QIODevice::NotOpen)
            qWarning("QIODevice::putChar: Closed device");
        else
            qWarning("QIODevice::putChar: ReadOnly device");
        return false;
    }

    // Make sure the device is positioned correctly.
    const bool sequential = isSequential();
    if (pos != devicePos && !sequential && !q_func()->seek(pos))
        return false;

    lastWasWrite = true;

    int len = 1;
#ifdef Q_OS_WIN
    if ((openMode & QIODevice::Text) && c == '\n') {
        ++len;
        *writeBuffer.reserve(1) = '\r';
    }
#endif

    // Write to buffer.
    *writeBuffer.reserve(1) = c;

    if (!sequential) {
        pos += len;
        devicePos += len;
        if (!buffer.isEmpty())
            buffer.skip(len);
    }

    return true;
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfiledevice.cpp, line 42, as _ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE
inline bool QFileDevicePrivate::setPermissions(QFileDevice::Permissions perms)
{
    if (engine()->setPermissions(perms.toInt())) {
        setError(QFileDevice::NoError);
        return true;
    }
    setError(QFile::PermissionsError, fileEngine->errorString());
    return false;
}

//  from src/corelib/io/qfiledevice.cpp, line 20, as _ZN18QFileDevicePrivateC2Ev
inline QFileDevicePrivate::QFileDevicePrivate()
    : cachedSize(0),
      error(QFile::NoError), lastWasWrite(false)
{
    writeBufferChunkSize = QFILE_WRITEBUFFER_SIZE;
}

//  from src/corelib/io/qfiledevice.cpp, line 27, as _ZN18QFileDevicePrivateD2Ev
inline QFileDevicePrivate::~QFileDevicePrivate() = default;

//  from src/corelib/io/qfile.cpp, line 1423, as _ZNK12QFilePrivate18writeToDebugStreamER6QDebug
#if !defined(QT_NO_DEBUG_STREAM)
inline void QFilePrivate::writeToDebugStream(QDebug &dbg) const
{
    Q_Q(const QFile);
    dbg.nospace();
    dbg << "QFile(" << q->fileName() << ')';
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  from src/corelib/io/qfile.cpp, line 78, as _ZNK12QFilePrivate6engineEv
inline QAbstractFileEngine *QFilePrivate::engine() const
{
    if (!fileEngine)
        fileEngine = QAbstractFileEngine::create(fileName);
    return fileEngine.get();
}

//  from src/corelib/io/qfiledevice.cpp, line 36, as _ZNK18QFileDevicePrivate11permissionsEv
inline QFileDevice::Permissions QFileDevicePrivate::permissions() const
{
    QAbstractFileEngine::FileFlags perms = engine()->fileFlags(QAbstractFileEngine::PermsMask) & QAbstractFileEngine::PermsMask;
    return QFile::Permissions::fromInt(perms.toInt()); //ewww
}

//  from src/corelib/io/qfiledevice.cpp, line 29, as _ZNK18QFileDevicePrivate6engineEv
inline QAbstractFileEngine *QFileDevicePrivate::engine() const
{
    if (!fileEngine)
        fileEngine = std::make_unique<QFSFileEngine>();
    return fileEngine.get();
}

//  from src/corelib/io/qfilesystemengine.cpp, line 204, as _ZN17QFileSystemEngine18createLegacyEngineERK7QString
inline std::unique_ptr<QAbstractFileEngine>
QFileSystemEngine::createLegacyEngine(const QString &fileName)
{
    QFileSystemEntry entry(fileName);
    QFileSystemMetaData metaData;
    return createLegacyEngine(entry, metaData);
}

//  from src/corelib/io/qfiledevice.cpp, line 52, as _ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE
inline void QFileDevicePrivate::setError(QFileDevice::FileError err)
{
    error = err;
    errorString.clear();
}

//  from src/corelib/io/qfile.cpp, line 44, as _ZN12QFilePrivateD1Ev
inline QFilePrivate::~QFilePrivate()
{
}

//  from src/corelib/io/qfile.cpp, line 48, as _ZN12QFilePrivate16openExternalFileE6QFlagsIN13QIODeviceBase12OpenModeFlagEEiS0_IN11QFileDevice14FileHandleFlagEE
inline bool
QFilePrivate::openExternalFile(QIODevice::OpenMode flags, int fd, QFile::FileHandleFlags handleFlags)
{
#ifdef QT_NO_FSFILEENGINE
    Q_UNUSED(flags);
    Q_UNUSED(fd);
    return false;
#else
    auto fs = std::make_unique<QFSFileEngine>();
    auto fe = fs.get();
    fileEngine = std::move(fs);
    return fe->open(flags, fd, handleFlags);
#endif
}

//  from src/corelib/io/qfile.cpp, line 63, as _ZN12QFilePrivate16openExternalFileE6QFlagsIN13QIODeviceBase12OpenModeFlagEEP8_IO_FILES0_IN11QFileDevice14FileHandleFlagEE
inline bool
QFilePrivate::openExternalFile(QIODevice::OpenMode flags, FILE *fh, QFile::FileHandleFlags handleFlags)
{
#ifdef QT_NO_FSFILEENGINE
    Q_UNUSED(flags);
    Q_UNUSED(fh);
    return false;
#else
    auto fs = std::make_unique<QFSFileEngine>();
    auto fe = fs.get();
    fileEngine = std::move(fs);
    return fe->open(flags, fh, handleFlags);
#endif
}
//  -----------------------------------------------------------------------

//  Only a class built on QFilePrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFilePrivate : QFilePrivate {
  using QFilePrivate::engine;
};

//  A QFilePrivate that Python can take functions over in. Every QFilePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQFilePrivateCall0)(const void *, int *);
typedef int (*CuteQFilePrivateCall1)(const void *, int *);
typedef bool (*CuteQFilePrivateCall2)(const void *, int, int *);
typedef bool (*CuteQFilePrivateCall3)(const void *, char, int *);
typedef qint64 (*CuteQFilePrivateCall4)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQFilePrivateCall5)(const void *, qint64, int *);
class CuteQFilePrivate : public QFilePrivate {
public:
  using QFilePrivate::QFilePrivate;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QFileDevicePrivate6engineEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QFileDevicePrivate11permissionsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEPcx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QAbstractFileEngine *QFilePrivate::engine() const
  QAbstractFileEngine *engine() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFilePrivateCall0 call = reinterpret_cast<CuteQFilePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractFileEngine *>(given);
    }
    return QFilePrivate::engine();
  }

  //  QFileDevice::Permissions QFileDevicePrivate::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFilePrivateCall1 call = reinterpret_cast<CuteQFilePrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFileDevicePrivate::permissions();
  }

  //  bool QFileDevicePrivate::setPermissions(QFileDevice::Permissions
  //      perms)
  bool setPermissions(QFileDevice::Permissions perms) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFilePrivateCall2 call = reinterpret_cast<CuteQFilePrivateCall2>(taken[2]);
      bool given = call(this, static_cast<int>(perms.toInt()), &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::setPermissions(perms);
  }

  //  bool QFileDevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFilePrivateCall3 call = reinterpret_cast<CuteQFilePrivateCall3>(taken[3]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFilePrivateCall4 call = reinterpret_cast<CuteQFilePrivateCall4>(taken[4]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFilePrivateCall5 call = reinterpret_cast<CuteQFilePrivateCall5>(taken[5]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QFile *QFilePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN12QFilePrivate6q_funcEv(QFilePrivate *self) {
  return self->q_func();
}

//  const QFile *QFilePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFile *ritual_ZNK12QFilePrivate6q_funcEv(const QFilePrivate *self) {
  return self->q_func();
}

//  QFilePrivate::~QFilePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFilePrivateD1Ev(QFilePrivate *self) {
  delete self;
}

//  bool QFilePrivate::openExternalFile(QIODevice::OpenMode flags, int fd,
//      QFile::FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QFilePrivate16openExternalFileE6QFlagsIN13QIODeviceBase12OpenModeFlagEEiS0_IN11QFileDevice14FileHandleFlagEE(
    QFilePrivate *self,
    int flags,
    int fd,
    int handleFlags) {
  return self->openExternalFile(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fd,
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  bool QFilePrivate::openExternalFile(QIODevice::OpenMode flags, FILE *fh,
//      QFile::FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QFilePrivate16openExternalFileE6QFlagsIN13QIODeviceBase12OpenModeFlagEEP8_IO_FILES0_IN11QFileDevice14FileHandleFlagEE(
    QFilePrivate *self,
    int flags,
    FILE *fh,
    int handleFlags) {
  return self->openExternalFile(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fh,
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  QAbstractFileEngine *QFilePrivate::engine() const
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZNK12QFilePrivate6engineEv(
    const QFilePrivate *self) {
  return self->engine();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  void QFilePrivate::writeToDebugStream(QDebug &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFilePrivate18writeToDebugStreamER6QDebug(
    const QFilePrivate *self,
    QDebug *a0) {
  self->writeToDebugStream(*a0);
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a Python function taken by a CuteQFilePrivate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFilePrivate(
    QFilePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFilePrivate *>(self)->take(key, call);
}

//  QAbstractFileEngine *QFilePrivate::engine() const
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_own_ZNK12QFilePrivate6engineEv(
    const QFilePrivate *self) {
  return static_cast<const OwnQFilePrivate *>(self)->OwnQFilePrivate::engine();
}
