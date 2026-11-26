//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfiledevice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qfiledevice.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfiledevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qfiledevice.h>
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/corelib/io/qfiledevice.cpp, line 20, as _ZN18QFileDevicePrivateC1Ev
inline QFileDevicePrivate::QFileDevicePrivate()
    : cachedSize(0),
      error(QFile::NoError), lastWasWrite(false)
{
    writeBufferChunkSize = QFILE_WRITEBUFFER_SIZE;
}

//  from src/corelib/io/qfiledevice.cpp, line 27, as _ZN18QFileDevicePrivateD1Ev
inline QFileDevicePrivate::~QFileDevicePrivate() = default;

//  from src/corelib/io/qfiledevice.cpp, line 52, as _ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE
inline void QFileDevicePrivate::setError(QFileDevice::FileError err)
{
    error = err;
    errorString.clear();
}

//  from src/corelib/io/qfiledevice.cpp, line 58, as _ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE7QString
inline void QFileDevicePrivate::setError(QFileDevice::FileError err, QString errStr)
{
    error = err;
    errorString = std::move(errStr);
}

//  from src/corelib/io/qfiledevice.cpp, line 64, as _ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorEi
inline void QFileDevicePrivate::setError(QFileDevice::FileError err, int errNum)
{
    error = err;
    errorString = qt_error_string(errNum);
}
//  -----------------------------------------------------------------------

//  Only a class built on QFileDevicePrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileDevicePrivate : QFileDevicePrivate {
  using QFileDevicePrivate::putCharHelper;
};

//  A QFileDevicePrivate that Python can take functions over in. Every QFileDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQFileDevicePrivateCall0)(const void *, int *);
typedef int (*CuteQFileDevicePrivateCall1)(const void *, int *);
typedef bool (*CuteQFileDevicePrivateCall2)(const void *, int, int *);
typedef bool (*CuteQFileDevicePrivateCall3)(const void *, char, int *);
typedef qint64 (*CuteQFileDevicePrivateCall4)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQFileDevicePrivateCall5)(const void *, qint64, int *);
class CuteQFileDevicePrivate : public QFileDevicePrivate {
public:
  using QFileDevicePrivate::QFileDevicePrivate;
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

  //  QAbstractFileEngine *QFileDevicePrivate::engine() const
  QAbstractFileEngine *engine() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileDevicePrivateCall0 call = reinterpret_cast<CuteQFileDevicePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractFileEngine *>(given);
    }
    return QFileDevicePrivate::engine();
  }

  //  QFileDevice::Permissions QFileDevicePrivate::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileDevicePrivateCall1 call = reinterpret_cast<CuteQFileDevicePrivateCall1>(taken[1]);
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
      CuteQFileDevicePrivateCall2 call = reinterpret_cast<CuteQFileDevicePrivateCall2>(taken[2]);
      bool given = call(this, static_cast<int>(perms.toInt()), &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::setPermissions(perms);
  }

  //  bool QFileDevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileDevicePrivateCall3 call = reinterpret_cast<CuteQFileDevicePrivateCall3>(taken[3]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QFileDevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileDevicePrivateCall4 call = reinterpret_cast<CuteQFileDevicePrivateCall4>(taken[4]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileDevicePrivateCall5 call = reinterpret_cast<CuteQFileDevicePrivateCall5>(taken[5]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QFileDevice *QFileDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileDevice *ritual_ZN18QFileDevicePrivate6q_funcEv(
    QFileDevicePrivate *self) {
  return self->q_func();
}

//  const QFileDevice *QFileDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileDevice *ritual_ZNK18QFileDevicePrivate6q_funcEv(
    const QFileDevicePrivate *self) {
  return self->q_func();
}

#if defined(Q_OS_LINUX)
//  QFileDevicePrivate::QFileDevicePrivate()
extern "C" Q_DECL_EXPORT
QFileDevicePrivate *ritual_ZN18QFileDevicePrivateC1Ev() {
  return new CuteQFileDevicePrivate();
}
#endif  // defined(Q_OS_LINUX)

//  QFileDevicePrivate::~QFileDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDevicePrivateD1Ev(QFileDevicePrivate *self) {
  delete self;
}

//  QAbstractFileEngine *QFileDevicePrivate::engine() const
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZNK18QFileDevicePrivate6engineEv(
    const QFileDevicePrivate *self) {
  return self->engine();
}

//  QFileDevice::Permissions QFileDevicePrivate::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFileDevicePrivate11permissionsEv(
    const QFileDevicePrivate *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  bool QFileDevicePrivate::setPermissions(QFileDevice::Permissions perms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFileDevicePrivate *self,
    int perms) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(perms));
}

//  bool QFileDevicePrivate::ensureFlushed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFileDevicePrivate13ensureFlushedEv(
    const QFileDevicePrivate *self) {
  return self->ensureFlushed();
}

//  bool QFileDevicePrivate::putCharHelper(char c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDevicePrivate13putCharHelperEc(
    QFileDevicePrivate *self,
    char c) {
  return self->putCharHelper(c);
}

//  void QFileDevicePrivate::setError(QFileDevice::FileError err)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE(
    QFileDevicePrivate *self,
    QFileDevice::FileError err) {
  self->setError(err);
}

//  void QFileDevicePrivate::setError(QFileDevice::FileError err, QString
//      errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorE7QString(
    QFileDevicePrivate *self,
    QFileDevice::FileError err,
    const QString *errorString) {
  self->setError(err, *errorString);
}

//  void QFileDevicePrivate::setError(QFileDevice::FileError err, int errNum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDevicePrivate8setErrorEN11QFileDevice9FileErrorEi(
    QFileDevicePrivate *self,
    QFileDevice::FileError err,
    int errNum) {
  self->setError(err, errNum);
}

//  a Python function taken by a CuteQFileDevicePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileDevicePrivate(
    QFileDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileDevicePrivate *>(self)->take(key, call);
}

//  QAbstractFileEngine *QFileDevicePrivate::engine() const
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_own_ZNK18QFileDevicePrivate6engineEv(
    const QFileDevicePrivate *self) {
  return self->QFileDevicePrivate::engine();
}

//  QFileDevice::Permissions QFileDevicePrivate::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QFileDevicePrivate11permissionsEv(
    const QFileDevicePrivate *self) {
  return static_cast<int>(self->QFileDevicePrivate::permissions().toInt());
}

//  bool QFileDevicePrivate::setPermissions(QFileDevice::Permissions perms)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QFileDevicePrivate14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFileDevicePrivate *self,
    int perms) {
  return self->QFileDevicePrivate::setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(perms));
}

#if defined(Q_OS_LINUX)
//  bool QFileDevicePrivate::putCharHelper(char c)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QFileDevicePrivate13putCharHelperEc(
    QFileDevicePrivate *self,
    char c) {
  return static_cast<OwnQFileDevicePrivate *>(self)->OwnQFileDevicePrivate::putCharHelper(
      c);
}
#endif  // defined(Q_OS_LINUX)
