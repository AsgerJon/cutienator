//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosink_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(alsa)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosink_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcoreapplication.h>
#include <QtCore/qvarlengtharray.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qalsaaudiosink_p.h>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 622, as _ZN17AlsaOutputPrivate9writeDataEPKcx
inline qint64 AlsaOutputPrivate::writeData(const char* data, qint64 len)
{
    int retry = 0;
    qint64 written = 0;
    if((audioDevice->deviceState == QAudio::ActiveState)
            ||(audioDevice->deviceState == QAudio::IdleState)) {
        while(written < len) {
            int chunk = audioDevice->write(data+written,(len-written));
            if(chunk <= 0)
                retry++;
            written+=chunk;
            if(retry > 10)
                return written;
        }
    }
    return written;

}
//  -----------------------------------------------------------------------

//  A AlsaOutputPrivate that Python can take functions over in. Every AlsaOutputPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteAlsaOutputPrivateCall0)(const void *, int *);
typedef bool (*CuteAlsaOutputPrivateCall1)(const void *, int, int *);
typedef void (*CuteAlsaOutputPrivateCall2)(const void *, int *);
typedef qint64 (*CuteAlsaOutputPrivateCall3)(const void *, int *);
typedef qint64 (*CuteAlsaOutputPrivateCall4)(const void *, int *);
typedef bool (*CuteAlsaOutputPrivateCall5)(const void *, qint64, int *);
typedef bool (*CuteAlsaOutputPrivateCall6)(const void *, int *);
typedef bool (*CuteAlsaOutputPrivateCall7)(const void *, int *);
typedef qint64 (*CuteAlsaOutputPrivateCall8)(const void *, int *);
typedef qint64 (*CuteAlsaOutputPrivateCall9)(const void *, int *);
typedef bool (*CuteAlsaOutputPrivateCall10)(const void *, int *);
typedef bool (*CuteAlsaOutputPrivateCall11)(const void *, int, int *);
typedef bool (*CuteAlsaOutputPrivateCall12)(const void *, int, int *);
typedef qint64 (*CuteAlsaOutputPrivateCall13)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAlsaOutputPrivateCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAlsaOutputPrivateCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAlsaOutputPrivateCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAlsaOutputPrivateCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAlsaOutputPrivateCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAlsaOutputPrivateCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAlsaOutputPrivateCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAlsaOutputPrivate : public AlsaOutputPrivate {
public:
  using AlsaOutputPrivate::AlsaOutputPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
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

  //  bool QIODevice::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall0 call = reinterpret_cast<CuteAlsaOutputPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::isSequential();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall1 call = reinterpret_cast<CuteAlsaOutputPrivateCall1>(taken[1]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall2 call = reinterpret_cast<CuteAlsaOutputPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[3]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall3 call = reinterpret_cast<CuteAlsaOutputPrivateCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall4 call = reinterpret_cast<CuteAlsaOutputPrivateCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[5]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall5 call = reinterpret_cast<CuteAlsaOutputPrivateCall5>(taken[5]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall6 call = reinterpret_cast<CuteAlsaOutputPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[7]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall7 call = reinterpret_cast<CuteAlsaOutputPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[8]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall8 call = reinterpret_cast<CuteAlsaOutputPrivateCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[9]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall9 call = reinterpret_cast<CuteAlsaOutputPrivateCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall10 call = reinterpret_cast<CuteAlsaOutputPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall11 call = reinterpret_cast<CuteAlsaOutputPrivateCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall12 call = reinterpret_cast<CuteAlsaOutputPrivateCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteAlsaOutputPrivateCall13 call = reinterpret_cast<CuteAlsaOutputPrivateCall13>(taken[13]);
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
      CuteAlsaOutputPrivateCall14 call = reinterpret_cast<CuteAlsaOutputPrivateCall14>(taken[14]);
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
      CuteAlsaOutputPrivateCall15 call = reinterpret_cast<CuteAlsaOutputPrivateCall15>(taken[15]);
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
      CuteAlsaOutputPrivateCall16 call = reinterpret_cast<CuteAlsaOutputPrivateCall16>(taken[16]);
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
      CuteAlsaOutputPrivateCall17 call = reinterpret_cast<CuteAlsaOutputPrivateCall17>(taken[17]);
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
      CuteAlsaOutputPrivateCall18 call = reinterpret_cast<CuteAlsaOutputPrivateCall18>(taken[18]);
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
      CuteAlsaOutputPrivateCall19 call = reinterpret_cast<CuteAlsaOutputPrivateCall19>(taken[19]);
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
      CuteAlsaOutputPrivateCall20 call = reinterpret_cast<CuteAlsaOutputPrivateCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AlsaOutputPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17AlsaOutputPrivate10metaObjectEv(
    const AlsaOutputPrivate *self) {
  return self->metaObject();
}

//  qint64 AlsaOutputPrivate::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17AlsaOutputPrivate9writeDataEPKcx(
    AlsaOutputPrivate *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  a Python function taken by a CuteAlsaOutputPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AlsaOutputPrivate(
    AlsaOutputPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteAlsaOutputPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(alsa)
