//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(temporaryfile)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#include "qplatformdefs.h"
#include <QtCore/qfiledevice.h>
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfsfileengine_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfile.cpp, line 40, as _ZN12QFilePrivateC2Ev
inline QFilePrivate::QFilePrivate()
{
}

//  from src/corelib/io/qfile.cpp, line 44, as _ZN12QFilePrivateD2Ev
inline QFilePrivate::~QFilePrivate()
{
}

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

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

//  from src/corelib/io/qfile.cpp, line 1423, as _ZNK12QFilePrivate18writeToDebugStreamER6QDebug
#if !defined(QT_NO_DEBUG_STREAM)
inline void QFilePrivate::writeToDebugStream(QDebug &dbg) const
{
    Q_Q(const QFile);
    dbg.nospace();
    dbg << "QFile(" << q->fileName() << ')';
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  from src/corelib/io/qfiledevice.cpp, line 36, as _ZNK18QFileDevicePrivate11permissionsEv
inline QFileDevice::Permissions QFileDevicePrivate::permissions() const
{
    QAbstractFileEngine::FileFlags perms = engine()->fileFlags(QAbstractFileEngine::PermsMask) & QAbstractFileEngine::PermsMask;
    return QFile::Permissions::fromInt(perms.toInt()); //ewww
}

//  from src/corelib/io/qtemporaryfile.cpp, line 289, as _ZNK20QTemporaryFileEngine12isReallyOpenEv
#if QT_CONFIG(temporaryfile)
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 516, as _ZN21QTemporaryFilePrivateD1Ev
#if QT_CONFIG(temporaryfile)
inline QTemporaryFilePrivate::~QTemporaryFilePrivate()
{
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 520, as _ZNK21QTemporaryFilePrivate6engineEv
#if QT_CONFIG(temporaryfile)
inline QAbstractFileEngine *QTemporaryFilePrivate::engine() const
{
    if (!fileEngine) {
        fileEngine.reset(new QTemporaryFileEngine(&templateName));
        resetFileEngine();
    }
    return fileEngine.get();
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qtemporaryfile.cpp, line 541, as _ZN21QTemporaryFilePrivate22materializeUnnamedFileEv
#if QT_CONFIG(temporaryfile)
inline void QTemporaryFilePrivate::materializeUnnamedFile()
{
#ifdef LINUX_UNNAMED_TMPFILE
    if (!fileName.isEmpty() || !fileEngine)
        return;

    auto *tef = static_cast<QTemporaryFileEngine *>(fileEngine.get());
    fileName = tef->fileName(QAbstractFileEngine::DefaultName);
#endif
}
#endif  // QT_CONFIG(temporaryfile)
//  -----------------------------------------------------------------------

//  A QTemporaryFilePrivate that Python can take functions over in. Every QTemporaryFilePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(temporaryfile)
typedef void * (*CuteQTemporaryFilePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
typedef int (*CuteQTemporaryFilePrivateCall1)(const void *, int *);
typedef bool (*CuteQTemporaryFilePrivateCall2)(const void *, int, int *);
typedef bool (*CuteQTemporaryFilePrivateCall3)(const void *, char, int *);
typedef const QByteArray * (*CuteQTemporaryFilePrivateCall4)(const void *, qint64, int *);
class CuteQTemporaryFilePrivate : public QTemporaryFilePrivate {
public:
  using QTemporaryFilePrivate::QTemporaryFilePrivate;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZNK18QFileDevicePrivate6engineEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
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
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(temporaryfile)
  //  QAbstractFileEngine *QTemporaryFilePrivate::engine() const
  QAbstractFileEngine *engine() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTemporaryFilePrivateCall0 call = reinterpret_cast<CuteQTemporaryFilePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractFileEngine *>(given);
    }
    return QTemporaryFilePrivate::engine();
  }
#endif  // QT_CONFIG(temporaryfile)

  //  QFileDevice::Permissions QFileDevicePrivate::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTemporaryFilePrivateCall1 call = reinterpret_cast<CuteQTemporaryFilePrivateCall1>(taken[1]);
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
      CuteQTemporaryFilePrivateCall2 call = reinterpret_cast<CuteQTemporaryFilePrivateCall2>(taken[2]);
      bool given = call(this, static_cast<int>(perms.toInt()), &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::setPermissions(perms);
  }

  //  bool QFileDevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTemporaryFilePrivateCall3 call = reinterpret_cast<CuteQTemporaryFilePrivateCall3>(taken[3]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTemporaryFilePrivateCall4 call = reinterpret_cast<CuteQTemporaryFilePrivateCall4>(taken[4]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QTemporaryFile *QTemporaryFilePrivate::q_func()
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN21QTemporaryFilePrivate6q_funcEv(
    QTemporaryFilePrivate *self) {
  return self->q_func();
}

//  const QTemporaryFile *QTemporaryFilePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTemporaryFile *ritual_ZNK21QTemporaryFilePrivate6q_funcEv(
    const QTemporaryFilePrivate *self) {
  return self->q_func();
}

//  QTemporaryFilePrivate::~QTemporaryFilePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTemporaryFilePrivateD1Ev(QTemporaryFilePrivate *self) {
  delete self;
}

//  QAbstractFileEngine *QTemporaryFilePrivate::engine() const
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZNK21QTemporaryFilePrivate6engineEv(
    const QTemporaryFilePrivate *self) {
  return self->engine();
}

#if QT_CONFIG(temporaryfile)
//  void QTemporaryFilePrivate::materializeUnnamedFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTemporaryFilePrivate22materializeUnnamedFileEv(
    QTemporaryFilePrivate *self) {
  self->materializeUnnamedFile();
}
#endif  // QT_CONFIG(temporaryfile)

//  a Python function taken by a CuteQTemporaryFilePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTemporaryFilePrivate(
    QTemporaryFilePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTemporaryFilePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(temporaryfile)
