//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsavefile_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(temporaryfile)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qsavefile.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsavefile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qfiledevice.h>
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#include <QtCore/qsavefile.h>
#if QT_CONFIG(temporaryfile)
#include "qplatformdefs.h"
#include <QtCore/private/qsavefile_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qttranslation.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/private/qtemporaryfile_p.h>
#ifdef Q_OS_UNIX
#include <errno.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qfiledevice.cpp, line 36, as _ZNK18QFileDevicePrivate11permissionsEv
inline QFileDevice::Permissions QFileDevicePrivate::permissions() const
{
    QAbstractFileEngine::FileFlags perms = engine()->fileFlags(QAbstractFileEngine::PermsMask) & QAbstractFileEngine::PermsMask;
    return QFile::Permissions::fromInt(perms.toInt()); //ewww
}

//  from src/corelib/io/qsavefile.cpp, line 34, as _ZN16QSaveFilePrivateD1Ev
#if QT_CONFIG(temporaryfile)
inline QSaveFilePrivate::~QSaveFilePrivate()
{
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qsavefile.cpp, line 189, as _ZNK16QSaveFilePrivate11permissionsEv
#if QT_CONFIG(temporaryfile)
inline QFileDevice::Permissions QSaveFilePrivate::permissions() const
{
    if (finalPermissions)
        return *finalPermissions;
    return QFileDevicePrivate::permissions();
}
#endif  // QT_CONFIG(temporaryfile)

//  from src/corelib/io/qsavefile.cpp, line 196, as _ZN16QSaveFilePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE
#if QT_CONFIG(temporaryfile)
inline bool QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)
{
    finalPermissions = perms;
    return true;
}
#endif  // QT_CONFIG(temporaryfile)
//  -----------------------------------------------------------------------

//  A QSaveFilePrivate that Python can take functions over in. Every QSaveFilePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(temporaryfile)
typedef int (*CuteQSaveFilePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQSaveFilePrivateCall1)(const void *, int, int *);
#endif  // QT_CONFIG(temporaryfile)
typedef void * (*CuteQSaveFilePrivateCall2)(const void *, int *);
typedef bool (*CuteQSaveFilePrivateCall3)(const void *, char, int *);
typedef const QByteArray * (*CuteQSaveFilePrivateCall4)(const void *, qint64, int *);
class CuteQSaveFilePrivate : public QSaveFilePrivate {
public:
  using QSaveFilePrivate::QSaveFilePrivate;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZNK18QFileDevicePrivate11permissionsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZNK18QFileDevicePrivate6engineEv")) {
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
  //  QFileDevice::Permissions QSaveFilePrivate::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSaveFilePrivateCall0 call = reinterpret_cast<CuteQSaveFilePrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QSaveFilePrivate::permissions();
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)
  bool setPermissions(QFileDevice::Permissions perms) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSaveFilePrivateCall1 call = reinterpret_cast<CuteQSaveFilePrivateCall1>(taken[1]);
      bool given = call(this, static_cast<int>(perms.toInt()), &handled);
      if (handled) return given;
    }
    return QSaveFilePrivate::setPermissions(perms);
  }
#endif  // QT_CONFIG(temporaryfile)

  //  QAbstractFileEngine *QFileDevicePrivate::engine() const
  QAbstractFileEngine *engine() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSaveFilePrivateCall2 call = reinterpret_cast<CuteQSaveFilePrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractFileEngine *>(given);
    }
    return QFileDevicePrivate::engine();
  }

  //  bool QFileDevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSaveFilePrivateCall3 call = reinterpret_cast<CuteQSaveFilePrivateCall3>(taken[3]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSaveFilePrivateCall4 call = reinterpret_cast<CuteQSaveFilePrivateCall4>(taken[4]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QSaveFile *QSaveFilePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSaveFile *ritual_ZN16QSaveFilePrivate6q_funcEv(QSaveFilePrivate *self) {
  return self->q_func();
}

//  const QSaveFile *QSaveFilePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSaveFile *ritual_ZNK16QSaveFilePrivate6q_funcEv(
    const QSaveFilePrivate *self) {
  return self->q_func();
}

//  QSaveFilePrivate::~QSaveFilePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSaveFilePrivateD1Ev(QSaveFilePrivate *self) {
  delete self;
}

//  QFileDevice::Permissions QSaveFilePrivate::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSaveFilePrivate11permissionsEv(
    const QSaveFilePrivate *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  bool QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSaveFilePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QSaveFilePrivate *self,
    int perms) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(perms));
}

//  a Python function taken by a CuteQSaveFilePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSaveFilePrivate(
    QSaveFilePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSaveFilePrivate *>(self)->take(key, call);
}

#if QT_CONFIG(temporaryfile)
//  QFileDevice::Permissions QSaveFilePrivate::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QSaveFilePrivate11permissionsEv(
    const QSaveFilePrivate *self) {
  return static_cast<int>(self->QSaveFilePrivate::permissions().toInt());
}
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
//  bool QSaveFilePrivate::setPermissions(QFileDevice::Permissions perms)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSaveFilePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QSaveFilePrivate *self,
    int perms) {
  return self->QSaveFilePrivate::setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(perms));
}
#endif  // QT_CONFIG(temporaryfile)

#endif  // QT_CONFIG(temporaryfile)
