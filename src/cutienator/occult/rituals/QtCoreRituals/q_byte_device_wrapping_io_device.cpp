//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qnoncontiguousbytedevice_p.h"
#include <qbuffer.h>
#include <qdebug.h>
#include <qfile.h>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 357, as _ZNK27QByteDeviceWrappingIoDevice12isSequentialEv
inline bool QByteDeviceWrappingIoDevice::isSequential() const
{
    return (byteDevice->size() == -1);
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 362, as _ZNK27QByteDeviceWrappingIoDevice5atEndEv
inline bool QByteDeviceWrappingIoDevice::atEnd() const
{
    return byteDevice->atEnd();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 367, as _ZN27QByteDeviceWrappingIoDevice5resetEv
inline bool QByteDeviceWrappingIoDevice::reset()
{
    return byteDevice->reset();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 372, as _ZNK27QByteDeviceWrappingIoDevice4sizeEv
inline qint64 QByteDeviceWrappingIoDevice::size() const
{
    if (isSequential())
        return 0;

    return byteDevice->size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 392, as _ZN27QByteDeviceWrappingIoDevice9writeDataEPKcx
inline qint64 QByteDeviceWrappingIoDevice::writeData(const char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);
    return -1;
}
//  -----------------------------------------------------------------------

//  A QByteDeviceWrappingIoDevice that Python can take functions over in. Every QByteDeviceWrappingIoDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall0)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall1)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall2)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall3)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall4)(const void *, int, int *);
typedef void (*CuteQByteDeviceWrappingIoDeviceCall5)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall6)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall7)(const void *, qint64, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall8)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall9)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall10)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall11)(const void *, int, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall12)(const void *, int, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall13)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQByteDeviceWrappingIoDevice : public QByteDeviceWrappingIoDevice {
public:
  using QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QByteDeviceWrappingIoDevice::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall0 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::isSequential();
  }

  //  bool QByteDeviceWrappingIoDevice::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall1 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::atEnd();
  }

  //  bool QByteDeviceWrappingIoDevice::reset()
  bool reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall2 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::reset();
  }

  //  qint64 QByteDeviceWrappingIoDevice::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall3 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::size();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall4 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall4>(taken[4]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[5]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall5 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall6 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[7]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall7 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall7>(taken[7]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall8 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall9 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall10 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall11 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall12 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall13 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall14 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall15 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall16 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall17 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall18 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall19 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall20 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QByteDeviceWrappingIoDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QByteDeviceWrappingIoDevice10metaObjectEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->metaObject();
}

//  bool QByteDeviceWrappingIoDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->isSequential();
}

//  bool QByteDeviceWrappingIoDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QByteDeviceWrappingIoDevice5atEndEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->atEnd();
}

//  bool QByteDeviceWrappingIoDevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QByteDeviceWrappingIoDevice5resetEv(
    QByteDeviceWrappingIoDevice *self) {
  return self->reset();
}

//  qint64 QByteDeviceWrappingIoDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK27QByteDeviceWrappingIoDevice4sizeEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->size();
}

//  qint64 QByteDeviceWrappingIoDevice::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN27QByteDeviceWrappingIoDevice9writeDataEPKcx(
    QByteDeviceWrappingIoDevice *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  a Python function taken by a CuteQByteDeviceWrappingIoDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QByteDeviceWrappingIoDevice(
    QByteDeviceWrappingIoDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQByteDeviceWrappingIoDevice *>(self)->take(key, call);
}

//  bool QByteDeviceWrappingIoDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::isSequential();
}

//  bool QByteDeviceWrappingIoDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QByteDeviceWrappingIoDevice5atEndEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::atEnd();
}

//  bool QByteDeviceWrappingIoDevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QByteDeviceWrappingIoDevice5resetEv(
    QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::reset();
}

//  qint64 QByteDeviceWrappingIoDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK27QByteDeviceWrappingIoDevice4sizeEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::size();
}
