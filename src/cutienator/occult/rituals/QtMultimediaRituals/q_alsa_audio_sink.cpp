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
#include <QtMultimedia/qaudioformat.h>
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

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 607, as _ZN17AlsaOutputPrivateC1EP14QAlsaAudioSink
inline AlsaOutputPrivate::AlsaOutputPrivate(QAlsaAudioSink* audio)
{
    audioDevice = qobject_cast<QAlsaAudioSink*>(audio);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 22, as _ZN14QAlsaAudioSinkD1Ev
inline QAlsaAudioSink::~QAlsaAudioSink()
{
    close();
    disconnect(timer, &QTimer::timeout, this, &QAlsaAudioSink::userFeed);
    delete timer;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 113, as _ZN14QAlsaAudioSink5startEP9QIODevice
inline void QAlsaAudioSink::start(QIODevice* device)
{
    if(deviceState != QAudio::StoppedState)
        deviceState = QAudio::StoppedState;

    errorState = QAudio::NoError;

    // Handle change of mode
    if(audioSource && !pullMode) {
        delete audioSource;
        audioSource = 0;
    }

    close();

    pullMode = true;
    audioSource = device;

    connect(audioSource, &QIODevice::readyRead, timer, [this] {
        if (!timer->isActive()) {
            timer->start(period_time / 1000);
        }
    });
    deviceState = QAudio::ActiveState;

    open();

    emit stateChanged(deviceState);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 143, as _ZN14QAlsaAudioSink5startEv
inline QIODevice* QAlsaAudioSink::start()
{
    if(deviceState != QAudio::StoppedState)
        deviceState = QAudio::StoppedState;

    errorState = QAudio::NoError;

    // Handle change of mode
    if(audioSource && !pullMode) {
        delete audioSource;
        audioSource = 0;
    }

    close();

    audioSource = new AlsaOutputPrivate(this);
    audioSource->open(QIODevice::WriteOnly|QIODevice::Unbuffered);
    pullMode = false;

    deviceState = QAudio::IdleState;

    open();

    emit stateChanged(deviceState);

    return audioSource;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 171, as _ZN14QAlsaAudioSink4stopEv
inline void QAlsaAudioSink::stop()
{
    if(deviceState == QAudio::StoppedState)
        return;
    errorState = QAudio::NoError;
    deviceState = QAudio::StoppedState;
    close();
    emit stateChanged(deviceState);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 599, as _ZN14QAlsaAudioSink5resetEv
inline void QAlsaAudioSink::reset()
{
    if(handle)
        snd_pcm_reset(handle);

    stop();
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 501, as _ZN14QAlsaAudioSink7suspendEv
inline void QAlsaAudioSink::suspend()
{
    if(deviceState == QAudio::ActiveState || deviceState == QAudio::IdleState || resuming) {
        suspendedInState = deviceState;
        snd_pcm_drain(handle);
        timer->stop();
        deviceState = QAudio::SuspendedState;
        errorState = QAudio::NoError;
        emit stateChanged(deviceState);
    }
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 476, as _ZN14QAlsaAudioSink6resumeEv
inline void QAlsaAudioSink::resume()
{
    if(deviceState == QAudio::SuspendedState) {
        int err = 0;

        if(handle) {
            err = snd_pcm_prepare( handle );
            if(err < 0)
                xrun_recovery(err);

            err = snd_pcm_start(handle);
            if(err < 0)
                xrun_recovery(err);

            bytesAvailable = (int)snd_pcm_frames_to_bytes(handle, buffer_frames);
        }
        resuming = true;

        deviceState = suspendedInState;
        errorState = QAudio::NoError;
        timer->start(period_time/1000);
        emit stateChanged(deviceState);
    }
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 384, as _ZNK14QAlsaAudioSink9bytesFreeEv
inline qsizetype QAlsaAudioSink::bytesFree() const
{
    if(resuming)
        return period_size;

    if(deviceState != QAudio::ActiveState && deviceState != QAudio::IdleState)
        return 0;

    int frames = snd_pcm_avail_update(handle);
    if (frames == -EPIPE) {
        // Try and handle buffer underrun
        int err = snd_pcm_recover(handle, frames, 0);
        if (err < 0)
            return 0;
        else
            frames = snd_pcm_avail_update(handle);
    } else if (frames < 0) {
        return 0;
    }

    if ((int)frames > (int)buffer_frames)
        frames = buffer_frames;

    return snd_pcm_frames_to_bytes(handle, frames);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 460, as _ZN14QAlsaAudioSink13setBufferSizeEx
inline void QAlsaAudioSink::setBufferSize(qsizetype value)
{
    if(deviceState == QAudio::StoppedState)
        buffer_size = value;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 466, as _ZNK14QAlsaAudioSink10bufferSizeEv
inline qsizetype QAlsaAudioSink::bufferSize() const
{
    return buffer_size;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 471, as _ZNK14QAlsaAudioSink14processedUSecsEv
inline qint64 QAlsaAudioSink::processedUSecs() const
{
    return qint64(1000000) * totalTimeValue / m_format.sampleRate();
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 29, as _ZNK14QAlsaAudioSink5stateEv
inline QAudio::State QAlsaAudioSink::state() const
{
    return deviceState;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 78, as _ZN14QAlsaAudioSink9setFormatEv
inline int QAlsaAudioSink::setFormat()
{
    snd_pcm_format_t pcmformat = SND_PCM_FORMAT_UNKNOWN;

    switch (m_format.sampleFormat()) {
    case QAudioFormat::UInt8:
        pcmformat = SND_PCM_FORMAT_U8;
        break;
    case QAudioFormat::Int16:
        if constexpr (QSysInfo::ByteOrder == QSysInfo::BigEndian)
            pcmformat = SND_PCM_FORMAT_S16_BE;
        else
            pcmformat = SND_PCM_FORMAT_S16_LE;
        break;
    case QAudioFormat::Int32:
        if constexpr (QSysInfo::ByteOrder == QSysInfo::BigEndian)
            pcmformat = SND_PCM_FORMAT_S32_BE;
        else
            pcmformat = SND_PCM_FORMAT_S32_LE;
        break;
    case QAudioFormat::Float:
        if constexpr (QSysInfo::ByteOrder == QSysInfo::BigEndian)
            pcmformat = SND_PCM_FORMAT_FLOAT_BE;
        else
            pcmformat = SND_PCM_FORMAT_FLOAT_LE;
        break;
    default:
        break;
    }

    return pcmformat != SND_PCM_FORMAT_UNKNOWN
            ? snd_pcm_hw_params_set_format( handle, hwparams, pcmformat)
            : -1;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosink.cpp, line 366, as _ZN14QAlsaAudioSink5closeEv
inline void QAlsaAudioSink::close()
{
    timer->stop();

    if ( handle ) {
        snd_pcm_drain( handle );
        snd_pcm_close( handle );
        handle = 0;
        delete [] audioBuffer;
        audioBuffer=0;
    }
    if(!pullMode && audioSource) {
        delete audioSource;
        audioSource = 0;
    }
    opened = false;
}
//  -----------------------------------------------------------------------

//  A QAlsaAudioSink that Python can take functions over in. Every QAlsaAudioSink
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAlsaAudioSinkCall0)(const void *, QIODevice *, int *);
typedef void * (*CuteQAlsaAudioSinkCall1)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall2)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall3)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall4)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall5)(const void *, int *);
typedef qsizetype (*CuteQAlsaAudioSinkCall6)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall7)(const void *, qsizetype, int *);
typedef qsizetype (*CuteQAlsaAudioSinkCall8)(const void *, int *);
typedef qint64 (*CuteQAlsaAudioSinkCall9)(const void *, int *);
typedef int (*CuteQAlsaAudioSinkCall10)(const void *, int *);
typedef bool (*CuteQAlsaAudioSinkCall11)(const void *, int *);
typedef void (*CuteQAlsaAudioSinkCall12)(const void *, int, int *);
typedef void (*CuteQAlsaAudioSinkCall13)(const void *, int, int *);
typedef bool (*CuteQAlsaAudioSinkCall14)(const void *, const QAudioFormat *, int *);
typedef void (*CuteQAlsaAudioSinkCall15)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioSinkCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioSinkCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSinkCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSinkCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSinkCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSinkCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSinkCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAlsaAudioSink : public QAlsaAudioSink {
public:
  using QAlsaAudioSink::QAlsaAudioSink;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5startEP9QIODevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5startEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink4stopEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink7suspendEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink6resumeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink9bytesFreeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink13setBufferSizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink10bufferSizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink14processedUSecsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase5stateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink14hasCallbackAPIEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17AudioEndpointRoleE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase9setVolumeEf")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAlsaAudioSink::start(QIODevice *device)
  void start(QIODevice *device) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall0 call = reinterpret_cast<CuteQAlsaAudioSinkCall0>(taken[0]);
      call(this, device, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::start(device);
  }

  //  QIODevice *QAlsaAudioSink::start()
  QIODevice *start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall1 call = reinterpret_cast<CuteQAlsaAudioSinkCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QAlsaAudioSink::start();
  }

  //  void QAlsaAudioSink::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall2 call = reinterpret_cast<CuteQAlsaAudioSinkCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::stop();
  }

  //  void QAlsaAudioSink::reset()
  void reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall3 call = reinterpret_cast<CuteQAlsaAudioSinkCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::reset();
  }

  //  void QAlsaAudioSink::suspend()
  void suspend() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall4 call = reinterpret_cast<CuteQAlsaAudioSinkCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::suspend();
  }

  //  void QAlsaAudioSink::resume()
  void resume() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall5 call = reinterpret_cast<CuteQAlsaAudioSinkCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::resume();
  }

  //  qsizetype QAlsaAudioSink::bytesFree() const
  qsizetype bytesFree() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall6 call = reinterpret_cast<CuteQAlsaAudioSinkCall6>(taken[6]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSink::bytesFree();
  }

  //  void QAlsaAudioSink::setBufferSize(qsizetype value)
  void setBufferSize(qsizetype value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall7 call = reinterpret_cast<CuteQAlsaAudioSinkCall7>(taken[7]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAlsaAudioSink::setBufferSize(value);
  }

  //  qsizetype QAlsaAudioSink::bufferSize() const
  qsizetype bufferSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall8 call = reinterpret_cast<CuteQAlsaAudioSinkCall8>(taken[8]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSink::bufferSize();
  }

  //  qint64 QAlsaAudioSink::processedUSecs() const
  qint64 processedUSecs() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall9 call = reinterpret_cast<CuteQAlsaAudioSinkCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSink::processedUSecs();
  }

  //  QAudio::State QAlsaAudioSink::state() const
  QAudio::State state() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall10 call = reinterpret_cast<CuteQAlsaAudioSinkCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAudio::State>(given);
    }
    return QAlsaAudioSink::state();
  }

  //  bool QPlatformAudioSink::hasCallbackAPI()
  bool hasCallbackAPI() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall11 call = reinterpret_cast<CuteQAlsaAudioSinkCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioSink::hasCallbackAPI();
  }

  //  void QPlatformAudioSink::setRole(AudioEndpointRole a0)
  void setRole(QPlatformAudioSink::AudioEndpointRole a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall12 call = reinterpret_cast<CuteQAlsaAudioSinkCall12>(taken[12]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioSink::setRole(a0);
  }

  //  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
  void setError(QAudio::Error a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall13 call = reinterpret_cast<CuteQAlsaAudioSinkCall13>(taken[13]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setError(a0);
  }

  //  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
  //      &format) const
  bool isFormatSupported(const QAudioFormat &format) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall14 call = reinterpret_cast<CuteQAlsaAudioSinkCall14>(taken[14]);
      bool given = call(this, &format, &handled);
      if (handled) return given;
    }
    return QPlatformAudioEndpointBase::isFormatSupported(format);
  }

  //  void QPlatformAudioEndpointBase::setVolume(float volume)
  void setVolume(float volume) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall15 call = reinterpret_cast<CuteQAlsaAudioSinkCall15>(taken[15]);
      call(this, volume, &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setVolume(volume);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall16 call = reinterpret_cast<CuteQAlsaAudioSinkCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall17 call = reinterpret_cast<CuteQAlsaAudioSinkCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall18 call = reinterpret_cast<CuteQAlsaAudioSinkCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall19 call = reinterpret_cast<CuteQAlsaAudioSinkCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall20 call = reinterpret_cast<CuteQAlsaAudioSinkCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall21 call = reinterpret_cast<CuteQAlsaAudioSinkCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAlsaAudioSinkCall22 call = reinterpret_cast<CuteQAlsaAudioSinkCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAlsaAudioSink::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAlsaAudioSink10metaObjectEv(
    const QAlsaAudioSink *self) {
  return self->metaObject();
}

//  QAlsaAudioSink::~QAlsaAudioSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSinkD1Ev(QAlsaAudioSink *self) {
  delete self;
}

//  void QAlsaAudioSink::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink5startEP9QIODevice(
    QAlsaAudioSink *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QAlsaAudioSink::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN14QAlsaAudioSink5startEv(QAlsaAudioSink *self) {
  return self->start();
}

//  void QAlsaAudioSink::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink4stopEv(QAlsaAudioSink *self) {
  self->stop();
}

//  void QAlsaAudioSink::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink5resetEv(QAlsaAudioSink *self) {
  self->reset();
}

//  void QAlsaAudioSink::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink7suspendEv(QAlsaAudioSink *self) {
  self->suspend();
}

//  void QAlsaAudioSink::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink6resumeEv(QAlsaAudioSink *self) {
  self->resume();
}

//  qsizetype QAlsaAudioSink::bytesFree() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAlsaAudioSink9bytesFreeEv(
    const QAlsaAudioSink *self) {
  return self->bytesFree();
}

//  void QAlsaAudioSink::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink13setBufferSizeEx(
    QAlsaAudioSink *self,
    qsizetype value) {
  self->setBufferSize(value);
}

//  qsizetype QAlsaAudioSink::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QAlsaAudioSink10bufferSizeEv(
    const QAlsaAudioSink *self) {
  return self->bufferSize();
}

//  qint64 QAlsaAudioSink::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QAlsaAudioSink14processedUSecsEv(
    const QAlsaAudioSink *self) {
  return self->processedUSecs();
}

//  QAudio::State QAlsaAudioSink::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_ZNK14QAlsaAudioSink5stateEv(
    const QAlsaAudioSink *self) {
  return self->state();
}

//  int QAlsaAudioSink::setFormat()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAlsaAudioSink9setFormatEv(QAlsaAudioSink *self) {
  return self->setFormat();
}

//  void QAlsaAudioSink::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAlsaAudioSink5closeEv(QAlsaAudioSink *self) {
  self->close();
}

//  a Python function taken by a CuteQAlsaAudioSink, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAlsaAudioSink(
    QAlsaAudioSink *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAlsaAudioSink *>(self)->take(key, call);
}

//  void QAlsaAudioSink::stop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAlsaAudioSink4stopEv(QAlsaAudioSink *self) {
  self->QAlsaAudioSink::stop();
}

//  void QAlsaAudioSink::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAlsaAudioSink5resetEv(QAlsaAudioSink *self) {
  self->QAlsaAudioSink::reset();
}

//  void QAlsaAudioSink::suspend()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAlsaAudioSink7suspendEv(QAlsaAudioSink *self) {
  self->QAlsaAudioSink::suspend();
}

//  qsizetype QAlsaAudioSink::bytesFree() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK14QAlsaAudioSink9bytesFreeEv(
    const QAlsaAudioSink *self) {
  return self->QAlsaAudioSink::bytesFree();
}

//  void QAlsaAudioSink::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAlsaAudioSink13setBufferSizeEx(
    QAlsaAudioSink *self,
    qsizetype value) {
  self->QAlsaAudioSink::setBufferSize(value);
}

//  qsizetype QAlsaAudioSink::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK14QAlsaAudioSink10bufferSizeEv(
    const QAlsaAudioSink *self) {
  return self->QAlsaAudioSink::bufferSize();
}

//  qint64 QAlsaAudioSink::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK14QAlsaAudioSink14processedUSecsEv(
    const QAlsaAudioSink *self) {
  return self->QAlsaAudioSink::processedUSecs();
}

//  QAudio::State QAlsaAudioSink::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_own_ZNK14QAlsaAudioSink5stateEv(
    const QAlsaAudioSink *self) {
  return self->QAlsaAudioSink::state();
}

#endif  // QT_CONFIG(alsa)
