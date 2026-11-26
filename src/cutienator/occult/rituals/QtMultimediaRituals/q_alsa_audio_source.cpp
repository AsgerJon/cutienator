//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(alsa)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcoreapplication.h>
#include <QtCore/qvarlengtharray.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qalsaaudiosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 648, as _ZN10RingBuffer6resizeEi
inline void RingBuffer::resize(int size)
{
    m_data.resize(size);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 642, as _ZN10RingBufferC1Ev
inline RingBuffer::RingBuffer() :
        m_head(0),
        m_tail(0)
{
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 34, as _ZN16QAlsaAudioSourceD1Ev
inline QAlsaAudioSource::~QAlsaAudioSource()
{
    close();
    disconnect(timer, &QTimer::timeout, this, &QAlsaAudioSource::userFeed);
    delete timer;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 127, as _ZN16QAlsaAudioSource5startEP9QIODevice
inline void QAlsaAudioSource::start(QIODevice* device)
{
    if(deviceState != QAudio::StoppedState)
        close();

    if(!pullMode && audioSource)
        delete audioSource;

    pullMode = true;
    audioSource = device;

    deviceState = QAudio::ActiveState;

    if( !open() )
        return;

    emit stateChanged(deviceState);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 146, as _ZN16QAlsaAudioSource5startEv
inline QIODevice* QAlsaAudioSource::start()
{
    if(deviceState != QAudio::StoppedState)
        close();

    if(!pullMode && audioSource)
        delete audioSource;

    pullMode = false;
    audioSource = new AlsaInputPrivate(this);
    audioSource->open(QIODevice::ReadOnly | QIODevice::Unbuffered);

    deviceState = QAudio::IdleState;

    if( !open() )
        return 0;

    emit stateChanged(deviceState);

    return audioSource;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 168, as _ZN16QAlsaAudioSource4stopEv
inline void QAlsaAudioSource::stop()
{
    if(deviceState == QAudio::StoppedState)
        return;

    deviceState = QAudio::StoppedState;

    close();
    emit stateChanged(deviceState);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 602, as _ZN16QAlsaAudioSource5resetEv
inline void QAlsaAudioSource::reset()
{
    if(handle)
        snd_pcm_reset(handle);
    stop();
    bytesAvailable = 0;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 549, as _ZN16QAlsaAudioSource7suspendEv
inline void QAlsaAudioSource::suspend()
{
    if(deviceState == QAudio::ActiveState||resuming) {
        snd_pcm_drain(handle);
        timer->stop();
        deviceState = QAudio::SuspendedState;
        emit stateChanged(deviceState);
    }
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 506, as _ZN16QAlsaAudioSource6resumeEv
inline void QAlsaAudioSource::resume()
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

            bytesAvailable = buffer_size;
        }
        resuming = true;
        deviceState = QAudio::ActiveState;
        int chunks = buffer_size/period_size;
        timer->start(period_time*chunks/2000);
        emit stateChanged(deviceState);
    }
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 357, as _ZNK16QAlsaAudioSource10bytesReadyEv
inline qsizetype QAlsaAudioSource::bytesReady() const
{
    return qMax(bytesAvailable, 0);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 530, as _ZN16QAlsaAudioSource13setBufferSizeEx
inline void QAlsaAudioSource::setBufferSize(qsizetype value)
{
    buffer_size = value;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 535, as _ZNK16QAlsaAudioSource10bufferSizeEv
inline qsizetype QAlsaAudioSource::bufferSize() const
{
    return buffer_size;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 540, as _ZNK16QAlsaAudioSource14processedUSecsEv
inline qint64 QAlsaAudioSource::processedUSecs() const
{
    qint64 result = qint64(1000000) * totalTimeValue /
        m_format.bytesPerFrame() /
        m_format.sampleRate();

    return result;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 41, as _ZNK16QAlsaAudioSource5stateEv
inline QAudio::State QAlsaAudioSource::state() const
{
    return deviceState;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 337, as _ZN16QAlsaAudioSource15checkBytesReadyEv
inline int QAlsaAudioSource::checkBytesReady()
{
    if(resuming)
        bytesAvailable = period_size;
    else if(deviceState != QAudio::ActiveState
            && deviceState != QAudio::IdleState)
        bytesAvailable = 0;
    else {
        int frames = snd_pcm_avail_update(handle);
        if (frames < 0) {
            bytesAvailable = frames;
        } else {
            if((int)frames > (int)buffer_frames)
                frames = buffer_frames;
            bytesAvailable = snd_pcm_frames_to_bytes(handle, frames);
        }
    }
    return bytesAvailable;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 92, as _ZN16QAlsaAudioSource9setFormatEv
inline int QAlsaAudioSource::setFormat()
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

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 326, as _ZN16QAlsaAudioSource5closeEv
inline void QAlsaAudioSource::close()
{
    timer->stop();

    if ( handle ) {
        snd_pcm_drop( handle );
        snd_pcm_close( handle );
        handle = 0;
    }
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 610, as _ZN16QAlsaAudioSource5drainEv
inline void QAlsaAudioSource::drain()
{
    if(handle)
        snd_pcm_drain(handle);
}
//  -----------------------------------------------------------------------

//  A QAlsaAudioSource that Python can take functions over in. Every QAlsaAudioSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAlsaAudioSourceCall0)(const void *, QIODevice *, int *);
typedef void * (*CuteQAlsaAudioSourceCall1)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall2)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall3)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall4)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall5)(const void *, int *);
typedef qsizetype (*CuteQAlsaAudioSourceCall6)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall7)(const void *, qsizetype, int *);
typedef qsizetype (*CuteQAlsaAudioSourceCall8)(const void *, int *);
typedef qint64 (*CuteQAlsaAudioSourceCall9)(const void *, int *);
typedef int (*CuteQAlsaAudioSourceCall10)(const void *, int *);
typedef bool (*CuteQAlsaAudioSourceCall11)(const void *, int *);
typedef void (*CuteQAlsaAudioSourceCall12)(const void *, int, int *);
typedef bool (*CuteQAlsaAudioSourceCall13)(const void *, const QAudioFormat *, int *);
typedef void (*CuteQAlsaAudioSourceCall14)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioSourceCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAlsaAudioSourceCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSourceCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSourceCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSourceCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSourceCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAlsaAudioSourceCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAlsaAudioSource : public QAlsaAudioSource {
public:
  using QAlsaAudioSource::QAlsaAudioSource;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5startEP9QIODevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5startEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource4stopEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource7suspendEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource6resumeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource10bytesReadyEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource13setBufferSizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource10bufferSizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource14processedUSecsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase5stateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource14hasCallbackAPIEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase9setVolumeEf")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAlsaAudioSource::start(QIODevice *device)
  void start(QIODevice *device) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall0 call = reinterpret_cast<CuteQAlsaAudioSourceCall0>(taken[0]);
      call(this, device, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::start(device);
  }

  //  QIODevice *QAlsaAudioSource::start()
  QIODevice *start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall1 call = reinterpret_cast<CuteQAlsaAudioSourceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QAlsaAudioSource::start();
  }

  //  void QAlsaAudioSource::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall2 call = reinterpret_cast<CuteQAlsaAudioSourceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::stop();
  }

  //  void QAlsaAudioSource::reset()
  void reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall3 call = reinterpret_cast<CuteQAlsaAudioSourceCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::reset();
  }

  //  void QAlsaAudioSource::suspend()
  void suspend() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall4 call = reinterpret_cast<CuteQAlsaAudioSourceCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::suspend();
  }

  //  void QAlsaAudioSource::resume()
  void resume() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall5 call = reinterpret_cast<CuteQAlsaAudioSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::resume();
  }

  //  qsizetype QAlsaAudioSource::bytesReady() const
  qsizetype bytesReady() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall6 call = reinterpret_cast<CuteQAlsaAudioSourceCall6>(taken[6]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSource::bytesReady();
  }

  //  void QAlsaAudioSource::setBufferSize(qsizetype value)
  void setBufferSize(qsizetype value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall7 call = reinterpret_cast<CuteQAlsaAudioSourceCall7>(taken[7]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAlsaAudioSource::setBufferSize(value);
  }

  //  qsizetype QAlsaAudioSource::bufferSize() const
  qsizetype bufferSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall8 call = reinterpret_cast<CuteQAlsaAudioSourceCall8>(taken[8]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSource::bufferSize();
  }

  //  qint64 QAlsaAudioSource::processedUSecs() const
  qint64 processedUSecs() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall9 call = reinterpret_cast<CuteQAlsaAudioSourceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAlsaAudioSource::processedUSecs();
  }

  //  QAudio::State QAlsaAudioSource::state() const
  QAudio::State state() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall10 call = reinterpret_cast<CuteQAlsaAudioSourceCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAudio::State>(given);
    }
    return QAlsaAudioSource::state();
  }

  //  bool QPlatformAudioSource::hasCallbackAPI()
  bool hasCallbackAPI() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall11 call = reinterpret_cast<CuteQAlsaAudioSourceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioSource::hasCallbackAPI();
  }

  //  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
  void setError(QAudio::Error a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall12 call = reinterpret_cast<CuteQAlsaAudioSourceCall12>(taken[12]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setError(a0);
  }

  //  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
  //      &format) const
  bool isFormatSupported(const QAudioFormat &format) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall13 call = reinterpret_cast<CuteQAlsaAudioSourceCall13>(taken[13]);
      bool given = call(this, &format, &handled);
      if (handled) return given;
    }
    return QPlatformAudioEndpointBase::isFormatSupported(format);
  }

  //  void QPlatformAudioEndpointBase::setVolume(float volume)
  void setVolume(float volume) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall14 call = reinterpret_cast<CuteQAlsaAudioSourceCall14>(taken[14]);
      call(this, volume, &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setVolume(volume);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall15 call = reinterpret_cast<CuteQAlsaAudioSourceCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall16 call = reinterpret_cast<CuteQAlsaAudioSourceCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall17 call = reinterpret_cast<CuteQAlsaAudioSourceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall18 call = reinterpret_cast<CuteQAlsaAudioSourceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall19 call = reinterpret_cast<CuteQAlsaAudioSourceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall20 call = reinterpret_cast<CuteQAlsaAudioSourceCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAlsaAudioSourceCall21 call = reinterpret_cast<CuteQAlsaAudioSourceCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAlsaAudioSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAlsaAudioSource10metaObjectEv(
    const QAlsaAudioSource *self) {
  return self->metaObject();
}

//  QAlsaAudioSource::~QAlsaAudioSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSourceD1Ev(QAlsaAudioSource *self) {
  delete self;
}

//  void QAlsaAudioSource::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource5startEP9QIODevice(
    QAlsaAudioSource *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QAlsaAudioSource::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN16QAlsaAudioSource5startEv(QAlsaAudioSource *self) {
  return self->start();
}

//  void QAlsaAudioSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource4stopEv(QAlsaAudioSource *self) {
  self->stop();
}

//  void QAlsaAudioSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource5resetEv(QAlsaAudioSource *self) {
  self->reset();
}

//  void QAlsaAudioSource::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource7suspendEv(QAlsaAudioSource *self) {
  self->suspend();
}

//  void QAlsaAudioSource::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource6resumeEv(QAlsaAudioSource *self) {
  self->resume();
}

//  qsizetype QAlsaAudioSource::bytesReady() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QAlsaAudioSource10bytesReadyEv(
    const QAlsaAudioSource *self) {
  return self->bytesReady();
}

//  void QAlsaAudioSource::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource13setBufferSizeEx(
    QAlsaAudioSource *self,
    qsizetype value) {
  self->setBufferSize(value);
}

//  qsizetype QAlsaAudioSource::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QAlsaAudioSource10bufferSizeEv(
    const QAlsaAudioSource *self) {
  return self->bufferSize();
}

//  qint64 QAlsaAudioSource::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QAlsaAudioSource14processedUSecsEv(
    const QAlsaAudioSource *self) {
  return self->processedUSecs();
}

//  QAudio::State QAlsaAudioSource::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_ZNK16QAlsaAudioSource5stateEv(
    const QAlsaAudioSource *self) {
  return self->state();
}

//  int QAlsaAudioSource::checkBytesReady()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QAlsaAudioSource15checkBytesReadyEv(QAlsaAudioSource *self) {
  return self->checkBytesReady();
}

//  int QAlsaAudioSource::setFormat()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QAlsaAudioSource9setFormatEv(QAlsaAudioSource *self) {
  return self->setFormat();
}

//  void QAlsaAudioSource::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource5closeEv(QAlsaAudioSource *self) {
  self->close();
}

//  void QAlsaAudioSource::drain()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAlsaAudioSource5drainEv(QAlsaAudioSource *self) {
  self->drain();
}

//  a Python function taken by a CuteQAlsaAudioSource, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAlsaAudioSource(
    QAlsaAudioSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAlsaAudioSource *>(self)->take(key, call);
}

//  void QAlsaAudioSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAlsaAudioSource4stopEv(QAlsaAudioSource *self) {
  self->QAlsaAudioSource::stop();
}

//  void QAlsaAudioSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAlsaAudioSource5resetEv(QAlsaAudioSource *self) {
  self->QAlsaAudioSource::reset();
}

//  void QAlsaAudioSource::suspend()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAlsaAudioSource7suspendEv(QAlsaAudioSource *self) {
  self->QAlsaAudioSource::suspend();
}

//  qsizetype QAlsaAudioSource::bytesReady() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK16QAlsaAudioSource10bytesReadyEv(
    const QAlsaAudioSource *self) {
  return self->QAlsaAudioSource::bytesReady();
}

//  void QAlsaAudioSource::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAlsaAudioSource13setBufferSizeEx(
    QAlsaAudioSource *self,
    qsizetype value) {
  self->QAlsaAudioSource::setBufferSize(value);
}

//  qsizetype QAlsaAudioSource::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK16QAlsaAudioSource10bufferSizeEv(
    const QAlsaAudioSource *self) {
  return self->QAlsaAudioSource::bufferSize();
}

//  qint64 QAlsaAudioSource::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QAlsaAudioSource14processedUSecsEv(
    const QAlsaAudioSource *self) {
  return self->QAlsaAudioSource::processedUSecs();
}

//  QAudio::State QAlsaAudioSource::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_own_ZNK16QAlsaAudioSource5stateEv(
    const QAlsaAudioSource *self) {
  return self->QAlsaAudioSource::state();
}

#endif  // QT_CONFIG(alsa)
