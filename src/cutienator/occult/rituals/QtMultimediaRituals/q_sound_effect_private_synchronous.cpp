//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectsynchronous_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectsynchronous_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSoundEffectPrivateSynchronous that Python can take functions over in. Every QSoundEffectPrivateSynchronous
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSoundEffectPrivateSynchronousCall0)(const void *, int *);
typedef qint64 (*CuteQSoundEffectPrivateSynchronousCall1)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall2)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall3)(const void *, int *);
typedef int (*CuteQSoundEffectPrivateSynchronousCall4)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall5)(const void *, int, int *);
typedef int (*CuteQSoundEffectPrivateSynchronousCall6)(const void *, int *);
typedef float (*CuteQSoundEffectPrivateSynchronousCall7)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall8)(const void *, float, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall9)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall10)(const void *, bool, int *);
typedef void (*CuteQSoundEffectPrivateSynchronousCall11)(const void *, int *);
typedef void (*CuteQSoundEffectPrivateSynchronousCall12)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall13)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall14)(const void *, const QAudioDevice *, int *);
typedef int (*CuteQSoundEffectPrivateSynchronousCall15)(const void *, int *);
typedef const QAudioDevice * (*CuteQSoundEffectPrivateSynchronousCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectPrivateSynchronousCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectPrivateSynchronousCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSoundEffectPrivateSynchronousCall19)(const void *, int, int *);
typedef void (*CuteQSoundEffectPrivateSynchronousCall20)(const void *, int *);
typedef qint64 (*CuteQSoundEffectPrivateSynchronousCall21)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall22)(const void *, qint64, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall23)(const void *, int *);
typedef qint64 (*CuteQSoundEffectPrivateSynchronousCall24)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall25)(const void *, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall26)(const void *, int, int *);
typedef bool (*CuteQSoundEffectPrivateSynchronousCall27)(const void *, int, int *);
typedef qint64 (*CuteQSoundEffectPrivateSynchronousCall28)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSoundEffectPrivateSynchronousCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSoundEffectPrivateSynchronousCall30)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectPrivateSynchronousCall31)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectPrivateSynchronousCall32)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectPrivateSynchronousCall33)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSoundEffectPrivateSynchronous : public QSoundEffectPrivateSynchronous {
public:
  using QSoundEffectPrivateSynchronous::QSoundEffectPrivateSynchronous;
  void *taken[34] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate9loopCountEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate12setLoopCountEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate14loopsRemainingEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate6volumeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate9setVolumeEf")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate5mutedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate8setMutedEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate4playEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate4stopEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate7playingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSoundEffectPrivate14setAudioDeviceE12QAudioDevice")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate6statusEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSoundEffectPrivate11audioDeviceEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[28] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  qint64 QSoundEffectPrivateSynchronous::size() const
  qint64 size() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall0 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::size();
  }

  //  qint64 QSoundEffectPrivateSynchronous::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall1 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::bytesAvailable();
  }

  //  bool QSoundEffectPrivateSynchronous::isSequential() const
  bool isSequential() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall2 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::isSequential();
  }

  //  bool QSoundEffectPrivateSynchronous::atEnd() const
  bool atEnd() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall3 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::atEnd();
  }

  //  int QSoundEffectPrivateSynchronous::loopCount() const
  int loopCount() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall4 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::loopCount();
  }

  //  bool QSoundEffectPrivateSynchronous::setLoopCount(int loopCount)
  bool setLoopCount(int loopCount) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall5 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall5>(taken[5]);
      bool given = call(this, loopCount, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::setLoopCount(loopCount);
  }

  //  int QSoundEffectPrivateSynchronous::loopsRemaining() const
  int loopsRemaining() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall6 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::loopsRemaining();
  }

  //  float QSoundEffectPrivateSynchronous::volume() const
  float volume() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall7 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall7>(taken[7]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::volume();
  }

  //  bool QSoundEffectPrivateSynchronous::setVolume(float volume)
  bool setVolume(float volume) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall8 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall8>(taken[8]);
      bool given = call(this, volume, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::setVolume(volume);
  }

  //  bool QSoundEffectPrivateSynchronous::muted() const
  bool muted() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall9 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::muted();
  }

  //  bool QSoundEffectPrivateSynchronous::setMuted(bool muted)
  bool setMuted(bool muted) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall10 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall10>(taken[10]);
      bool given = call(this, muted, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::setMuted(muted);
  }

  //  void QSoundEffectPrivateSynchronous::play()
  void play() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall11 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSoundEffectPrivateSynchronous::play();
  }

  //  void QSoundEffectPrivateSynchronous::stop()
  void stop() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall12 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSoundEffectPrivateSynchronous::stop();
  }

  //  bool QSoundEffectPrivateSynchronous::playing() const
  bool playing() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall13 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::playing();
  }

  //  bool QSoundEffectPrivateSynchronous::setAudioDevice(QAudioDevice
  //      device)
  bool setAudioDevice(QAudioDevice device) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall14 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall14>(taken[14]);
      bool given = call(this, &device, &handled);
      if (handled) return given;
    }
    return QSoundEffectPrivateSynchronous::setAudioDevice(device);
  }

  //  QSoundEffect::Status QSoundEffectPrivateSynchronous::status() const
  QSoundEffect::Status status() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall15 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSoundEffect::Status>(given);
    }
    return QSoundEffectPrivateSynchronous::status();
  }

  //  QAudioDevice QSoundEffectPrivateSynchronous::audioDevice() const
  QAudioDevice audioDevice() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall16 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall16>(taken[16]);
      const QAudioDevice * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSoundEffectPrivateSynchronous::audioDevice();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObjectPrivate::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall17 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObjectPrivate::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObjectPrivate::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall18 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObjectPrivate::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall19 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall19>(taken[19]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall20 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall21 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall21>(taken[21]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall22 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall22>(taken[22]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[23]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall23 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall24 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall24>(taken[24]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall25 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall26 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall26>(taken[26]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall27 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall27>(taken[27]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall28 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall28>(taken[28]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall29 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall29>(taken[29]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall30 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall30>(taken[30]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall31 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall32 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSoundEffectPrivateSynchronousCall33 call = reinterpret_cast<CuteQSoundEffectPrivateSynchronousCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSoundEffectPrivateSynchronous::QSoundEffectPrivateSynchronous(QSoundEffe
//      ct *q, const QAudioDevice &audioDevice)
extern "C" Q_DECL_EXPORT
QSoundEffectPrivateSynchronous *ritual_ZN30QSoundEffectPrivateSynchronousC1EP12QSoundEffectRK12QAudioDevice(
    QSoundEffect *q,
    const QAudioDevice *audioDevice) {
  return new CuteQSoundEffectPrivateSynchronous(q, *audioDevice);
}

//  QSoundEffectPrivateSynchronous::~QSoundEffectPrivateSynchronous()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronousD1Ev(
    QSoundEffectPrivateSynchronous *self) {
  delete self;
}

//  qint64 QSoundEffectPrivateSynchronous::writeData(const char *data, qint64
//      len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN30QSoundEffectPrivateSynchronous9writeDataEPKcx(
    QSoundEffectPrivateSynchronous *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  qint64 QSoundEffectPrivateSynchronous::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK30QSoundEffectPrivateSynchronous4sizeEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->size();
}

//  qint64 QSoundEffectPrivateSynchronous::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK30QSoundEffectPrivateSynchronous14bytesAvailableEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->bytesAvailable();
}

//  bool QSoundEffectPrivateSynchronous::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QSoundEffectPrivateSynchronous12isSequentialEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->isSequential();
}

//  bool QSoundEffectPrivateSynchronous::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QSoundEffectPrivateSynchronous5atEndEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->atEnd();
}

//  void QSoundEffectPrivateSynchronous::setLoopsRemaining(int
//      loopsRemaining)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous17setLoopsRemainingEi(
    QSoundEffectPrivateSynchronous *self,
    int loopsRemaining) {
  self->setLoopsRemaining(loopsRemaining);
}

//  void QSoundEffectPrivateSynchronous::setStatus(QSoundEffect::Status
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous9setStatusEN12QSoundEffect6StatusE(
    QSoundEffectPrivateSynchronous *self,
    QSoundEffect::Status status) {
  self->setStatus(status);
}

//  void QSoundEffectPrivateSynchronous::setPlaying(bool playing)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous10setPlayingEb(
    QSoundEffectPrivateSynchronous *self,
    bool playing) {
  self->setPlaying(playing);
}

//  bool QSoundEffectPrivateSynchronous::updateAudioOutput()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QSoundEffectPrivateSynchronous17updateAudioOutputEv(
    QSoundEffectPrivateSynchronous *self) {
  return self->updateAudioOutput();
}

//  void QSoundEffectPrivateSynchronous::decoderError()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous12decoderErrorEv(
    QSoundEffectPrivateSynchronous *self) {
  self->decoderError();
}

//  int QSoundEffectPrivateSynchronous::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QSoundEffectPrivateSynchronous9loopCountEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->loopCount();
}

//  bool QSoundEffectPrivateSynchronous::setLoopCount(int loopCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QSoundEffectPrivateSynchronous12setLoopCountEi(
    QSoundEffectPrivateSynchronous *self,
    int loopCount) {
  return self->setLoopCount(loopCount);
}

//  int QSoundEffectPrivateSynchronous::loopsRemaining() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QSoundEffectPrivateSynchronous14loopsRemainingEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->loopsRemaining();
}

//  float QSoundEffectPrivateSynchronous::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QSoundEffectPrivateSynchronous6volumeEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->volume();
}

//  bool QSoundEffectPrivateSynchronous::setVolume(float volume)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QSoundEffectPrivateSynchronous9setVolumeEf(
    QSoundEffectPrivateSynchronous *self,
    float volume) {
  return self->setVolume(volume);
}

//  bool QSoundEffectPrivateSynchronous::muted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QSoundEffectPrivateSynchronous5mutedEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->muted();
}

//  bool QSoundEffectPrivateSynchronous::setMuted(bool muted)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QSoundEffectPrivateSynchronous8setMutedEb(
    QSoundEffectPrivateSynchronous *self,
    bool muted) {
  return self->setMuted(muted);
}

//  void QSoundEffectPrivateSynchronous::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous4playEv(
    QSoundEffectPrivateSynchronous *self) {
  self->play();
}

//  void QSoundEffectPrivateSynchronous::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous4stopEv(
    QSoundEffectPrivateSynchronous *self) {
  self->stop();
}

//  bool QSoundEffectPrivateSynchronous::playing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QSoundEffectPrivateSynchronous7playingEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->playing();
}

//  bool QSoundEffectPrivateSynchronous::setAudioDevice(QAudioDevice device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QSoundEffectPrivateSynchronous14setAudioDeviceE12QAudioDevice(
    QSoundEffectPrivateSynchronous *self,
    const QAudioDevice *device) {
  return self->setAudioDevice(*device);
}

//  QSoundEffect::Status QSoundEffectPrivateSynchronous::status() const
extern "C" Q_DECL_EXPORT
QSoundEffect::Status ritual_ZNK30QSoundEffectPrivateSynchronous6statusEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->status();
}

//  QAudioDevice QSoundEffectPrivateSynchronous::audioDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK30QSoundEffectPrivateSynchronous11audioDeviceEv(
    const QSoundEffectPrivateSynchronous *self) {
  return new QAudioDevice(self->audioDevice());
}

//  void QSoundEffectPrivateSynchronous::stateChanged(QAudio::State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSoundEffectPrivateSynchronous12stateChangedEN6QAudio5StateE(
    QSoundEffectPrivateSynchronous *self,
    QAudio::State a0) {
  self->stateChanged(a0);
}

//  QSoundEffectPrivateSynchronous as the QSoundEffectPrivate it is built on
extern "C" Q_DECL_EXPORT
QSoundEffectPrivate *ritual_cast_QSoundEffectPrivateSynchronous_QSoundEffectPrivate(
    QSoundEffectPrivateSynchronous *self) {
  return static_cast<QSoundEffectPrivate *>(self);
}

//  a Python function taken by a CuteQSoundEffectPrivateSynchronous, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSoundEffectPrivateSynchronous(
    QSoundEffectPrivateSynchronous *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSoundEffectPrivateSynchronous *>(self)->take(key, call);
}

//  qint64 QSoundEffectPrivateSynchronous::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK30QSoundEffectPrivateSynchronous4sizeEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::size();
}

//  qint64 QSoundEffectPrivateSynchronous::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK30QSoundEffectPrivateSynchronous14bytesAvailableEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::bytesAvailable();
}

//  bool QSoundEffectPrivateSynchronous::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QSoundEffectPrivateSynchronous12isSequentialEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::isSequential();
}

//  bool QSoundEffectPrivateSynchronous::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QSoundEffectPrivateSynchronous5atEndEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::atEnd();
}

//  int QSoundEffectPrivateSynchronous::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK30QSoundEffectPrivateSynchronous9loopCountEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::loopCount();
}

//  bool QSoundEffectPrivateSynchronous::setLoopCount(int loopCount)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QSoundEffectPrivateSynchronous12setLoopCountEi(
    QSoundEffectPrivateSynchronous *self,
    int loopCount) {
  return self->QSoundEffectPrivateSynchronous::setLoopCount(loopCount);
}

//  int QSoundEffectPrivateSynchronous::loopsRemaining() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK30QSoundEffectPrivateSynchronous14loopsRemainingEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::loopsRemaining();
}

//  float QSoundEffectPrivateSynchronous::volume() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK30QSoundEffectPrivateSynchronous6volumeEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::volume();
}

//  bool QSoundEffectPrivateSynchronous::setVolume(float volume)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QSoundEffectPrivateSynchronous9setVolumeEf(
    QSoundEffectPrivateSynchronous *self,
    float volume) {
  return self->QSoundEffectPrivateSynchronous::setVolume(volume);
}

//  bool QSoundEffectPrivateSynchronous::muted() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QSoundEffectPrivateSynchronous5mutedEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::muted();
}

//  bool QSoundEffectPrivateSynchronous::setMuted(bool muted)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QSoundEffectPrivateSynchronous8setMutedEb(
    QSoundEffectPrivateSynchronous *self,
    bool muted) {
  return self->QSoundEffectPrivateSynchronous::setMuted(muted);
}

//  void QSoundEffectPrivateSynchronous::play()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QSoundEffectPrivateSynchronous4playEv(
    QSoundEffectPrivateSynchronous *self) {
  self->QSoundEffectPrivateSynchronous::play();
}

//  void QSoundEffectPrivateSynchronous::stop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QSoundEffectPrivateSynchronous4stopEv(
    QSoundEffectPrivateSynchronous *self) {
  self->QSoundEffectPrivateSynchronous::stop();
}

//  bool QSoundEffectPrivateSynchronous::playing() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QSoundEffectPrivateSynchronous7playingEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::playing();
}

//  bool QSoundEffectPrivateSynchronous::setAudioDevice(QAudioDevice device)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QSoundEffectPrivateSynchronous14setAudioDeviceE12QAudioDevice(
    QSoundEffectPrivateSynchronous *self,
    const QAudioDevice *device) {
  return self->QSoundEffectPrivateSynchronous::setAudioDevice(*device);
}

//  QSoundEffect::Status QSoundEffectPrivateSynchronous::status() const
extern "C" Q_DECL_EXPORT
QSoundEffect::Status ritual_own_ZNK30QSoundEffectPrivateSynchronous6statusEv(
    const QSoundEffectPrivateSynchronous *self) {
  return self->QSoundEffectPrivateSynchronous::status();
}

//  QAudioDevice QSoundEffectPrivateSynchronous::audioDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_own_ZNK30QSoundEffectPrivateSynchronous11audioDeviceEv(
    const QSoundEffectPrivateSynchronous *self) {
  return new QAudioDevice(
      self->QSoundEffectPrivateSynchronous::audioDevice());
}
