//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <cstring>
#include <QtMultimedia/QAudioDevice>
#include <QtMultimedia/QAudioFormat>
#include <optional>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qaudiosystem_platform_stream_support_p.h>
#include <QtMultimedia/private/qaudio_qiodevice_support_p.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 16, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStreamC2E12QAudioDevice12QAudioFormatSt8optionalIiES3_INS_18NativePeriodFramesEEf
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioIOStream::QPlatformAudioIOStream(QAudioDevice m_audioDevice, QAudioFormat m_format,
                                               std::optional<int> ringbufferSize,
                                               std::optional<NativePeriodFrames> nativePeriodFrames,
                                               float volume)
    : m_audioDevice{
          std::move(m_audioDevice),
      },
      m_format{
          m_format,
      },
      m_nativePeriodFrames{
          nativePeriodFrames,
      },
      m_volume{
          volume,
      }
{
    prepareRingbuffer(ringbufferSize);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 36, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStreamD2Ev
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioIOStream::~QPlatformAudioIOStream()
{
    Q_ASSERT(m_stopRequested);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 46, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream17prepareRingbufferESt8optionalIiE
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioIOStream::prepareRingbuffer(std::optional<int> ringbufferSize)
{
    using SampleFormat = QAudioFormat::SampleFormat;

    // Warning: QAudioSink::setBufferSize is measured in *bytes* not in *frames*
    int ringbufferElements = inferRingbufferFrames(ringbufferSize, m_nativePeriodFrames, m_format)
            * m_format.channelCount();

    switch (m_format.sampleFormat()) {
    case SampleFormat::Float:
        m_ringbuffer.emplace<QAudioRingBuffer<float>>(ringbufferElements);
        break;
    case SampleFormat::Int16:
        m_ringbuffer.emplace<QAudioRingBuffer<int16_t>>(ringbufferElements);
        break;
    case SampleFormat::Int32:
        m_ringbuffer.emplace<QAudioRingBuffer<int32_t>>(ringbufferElements);
        break;
    case SampleFormat::UInt8:
        m_ringbuffer.emplace<QAudioRingBuffer<uint8_t>>(ringbufferElements);
        break;

    default:
        qCritical() << "invalid sample format";
        Q_UNREACHABLE_RETURN();
    }
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 79, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream21inferRingbufferFramesERKSt8optionalIiERKS1_INS_18NativePeriodFramesEERK12QAudioFormat
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline qsizetype
QPlatformAudioIOStream::inferRingbufferFrames(const std::optional<int> &ringbufferSize,
                                              const std::optional<NativePeriodFrames> &nativePeriodFrames,
                                              const QAudioFormat &format)
{
    int bytesPerFrame = format.bytesPerFrame();
    Q_PRESUME(bytesPerFrame > 0);

    return inferRingbufferBytes(ringbufferSize, nativePeriodFrames, format) / bytesPerFrame;
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 90, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream20inferRingbufferBytesERKSt8optionalIiERKS1_INS_18NativePeriodFramesEERK12QAudioFormat
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline qsizetype
QPlatformAudioIOStream::inferRingbufferBytes(const std::optional<int> &ringbufferSize,
                                             const std::optional<NativePeriodFrames> &nativePeriodFrames,
                                             const QAudioFormat &format)
{
    // ensure to a sane minimum ringbuffer size of twice the hw buffer size or 32 frames
    const int minimumRingbufferFrames = nativePeriodFrames
            ? qToUnderlying(*nativePeriodFrames) * 2
            : 32;
    const int minimumRingbufferBytes = format.bytesForFrames(minimumRingbufferFrames);
    if (ringbufferSize)
        return ringbufferSize >= minimumRingbufferBytes ? *ringbufferSize : minimumRingbufferBytes;

    using namespace std::chrono;
    static constexpr auto defaultBufferDuration = 250ms;

    return format.bytesForDuration(microseconds(defaultBufferDuration).count());
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 328, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStreamC1E12QAudioDeviceRK12QAudioFormatSt8optionalIiES5_INS_18NativePeriodFramesEEf
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioSourceStream::QPlatformAudioSourceStream(QAudioDevice audioDevice,
                                                       const QAudioFormat &format,
                                                       std::optional<int> ringbufferSize,
                                                       std::optional<NativePeriodFrames> nativePeriodFrames,
                                                       float volume)
    : QPlatformAudioIOStream{
          std::move(audioDevice), format, ringbufferSize, nativePeriodFrames, volume,
      }
{
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 339, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStreamD1Ev
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioSourceStream::~QPlatformAudioSourceStream() = default;
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 431, as _ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream10bytesReadyEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline qsizetype QPlatformAudioSourceStream::bytesReady() const
{
    return visitRingbuffer([](const auto &ringbuffer) {
        return ringbuffer.used() * sizeof(typename std::decay_t<decltype(ringbuffer)>::ValueType);
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 438, as _ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream17processedDurationEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline std::chrono::microseconds QPlatformAudioSourceStream::processedDuration() const
{
    return std::chrono::microseconds{
        m_format.durationForFrames(
                qint32(m_totalNumberOfFramesPushedToRingbuffer.load(std::memory_order_relaxed))),
    };
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 446, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream12setQIODeviceEP9QIODevice
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::setQIODevice(QIODevice *device)
{
    m_device = device;
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 451, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream26createQIODeviceConnectionsEP9QIODevice
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::createQIODeviceConnections(QIODevice *device)
{
    bool pushToDevice = !deviceIsRingbufferReader();

    if (pushToDevice) {
        m_ringbufferHasDataConnection = m_ringbufferHasData.callOnActivated(device, [this] {
            if (!isStopRequested())
                updateStreamIdle(false);
            pushToIODevice();
        });
    } else {
        m_ringbufferHasDataConnection = m_ringbufferHasData.callOnActivated(device, [this] {
            if (!isStopRequested())
                updateStreamIdle(false);
            Q_EMIT m_device->readyRead();
        });
    }

    m_ringbufferIsFullConnection = m_ringbufferHasData.callOnActivated(device, [this] {
        if (!isStopRequested())
            updateStreamIdle(false);
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 475, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream30disconnectQIODeviceConnectionsEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::disconnectQIODeviceConnections()
{
    QObject::disconnect(m_ringbufferHasDataConnection);
    QObject::disconnect(m_ringbufferIsFullConnection);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 481, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream28createRingbufferReaderDeviceEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QIODevice *QPlatformAudioSourceStream::createRingbufferReaderDevice()
{
    using namespace QtPrivate;

    m_ringbufferReaderDevice = visitRingbuffer([&](auto &rb) -> std::unique_ptr<QIODevice> {
        using SampleType = typename std::decay_t<decltype(rb)>::ValueType;
        return std::make_unique<QIODeviceRingBufferReader<SampleType>>(&rb);
    });

    m_ringbufferReaderDevice->open(QIODevice::ReadOnly | QIODevice::Unbuffered);

    return m_ringbufferReaderDevice.get();
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 384, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream14pushToIODeviceEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::pushToIODevice()
{
    Q_ASSERT(thread()->isCurrentThread());

    qsizetype bytesPushed = visitRingbuffer([&](auto &ringbuffer) {
        return QtPrivate::pushToQIODeviceFromRingbuffer(*m_device, ringbuffer);
    });

    if (bytesPushed)
        Q_EMIT m_device->readyRead();
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 396, as _ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream24deviceIsRingbufferReaderEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline bool QPlatformAudioSourceStream::deviceIsRingbufferReader() const
{
    return m_device == m_ringbufferReaderDevice.get();
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 401, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream17finalizeQIODeviceENS_22QPlatformAudioIOStream14ShutdownPolicyE
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::finalizeQIODevice(ShutdownPolicy shutdownPolicy)
{
    switch (shutdownPolicy) {
    case ShutdownPolicy::DiscardRingbuffer:
        return;
    case ShutdownPolicy::DrainRingbuffer:
        if (!deviceIsRingbufferReader())
            pushToIODevice();
        return;

    default:
        Q_UNREACHABLE_RETURN();
    }
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 416, as _ZN19QtMultimediaPrivate26QPlatformAudioSourceStream15emptyRingbufferEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSourceStream::emptyRingbuffer()
{
    visitRingbuffer([](auto &ringbuffer) {
        ringbuffer.consumeAll([](auto &) {
        });
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 424, as _ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream6threadEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QThread *QPlatformAudioSourceStream::thread() const
{
    // QPlatformAudioSourceStream is not a QObject, but still has a notion of an application thread
    // where it lives on.
    return m_ringbufferHasData.thread();
}
}  // namespace QtMultimediaPrivate
//  -----------------------------------------------------------------------

//  A QtMultimediaPrivate::QPlatformAudioSourceStream that Python can take functions over in. Every QtMultimediaPrivate::QPlatformAudioSourceStream
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0)(const void *, bool, int *);
class CuteQtMultimediaPrivate_QPlatformAudioSourceStream : public QtMultimediaPrivate::QPlatformAudioSourceStream {
public:
  using QtMultimediaPrivate::QPlatformAudioSourceStream::QPlatformAudioSourceStream;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream16updateStreamIdleEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QtMultimediaPrivate::QPlatformAudioSourceStream::updateStreamIdl
  //      e(bool a0)
  void updateStreamIdle(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0 call = reinterpret_cast<CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
};

//  QtMultimediaPrivate::QPlatformAudioSourceStream::QPlatformAudioSourceStre
//      am(QAudioDevice a0, const QAudioFormat &a1, std::optional<int>
//      ringbufferSize, std::optional<NativePeriodFrames> nativePeriodFrames,
//      float volume)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QPlatformAudioSourceStream *ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStreamC1E12QAudioDeviceRK12QAudioFormatSt8optionalIiES5_INS_18NativePeriodFramesEEf(
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    const std::optional<int> *ringbufferSize,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames,
    float volume) {
  return new CuteQtMultimediaPrivate_QPlatformAudioSourceStream(
      *a0,
      *a1,
      *ringbufferSize,
      *nativePeriodFrames,
      volume);
}

//  QtMultimediaPrivate::QPlatformAudioSourceStream::~QPlatformAudioSourceStr
//      eam()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStreamD1Ev(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  delete self;
}

//  qsizetype QtMultimediaPrivate::QPlatformAudioSourceStream::bytesReady()
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream10bytesReadyEv(
    const QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  return self->bytesReady();
}

//  std::chrono::microseconds
//      QtMultimediaPrivate::QPlatformAudioSourceStream::processedDuration()
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream17processedDurationEv(
    const QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  return static_cast<long long>(self->processedDuration().count());
}

//  void
//      QtMultimediaPrivate::QPlatformAudioSourceStream::setQIODevice(QIODevi
//      ce *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream12setQIODeviceEP9QIODevice(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    QIODevice *device) {
  self->setQIODevice(device);
}

//  void QtMultimediaPrivate::QPlatformAudioSourceStream::createQIODeviceConn
//      ections(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream26createQIODeviceConnectionsEP9QIODevice(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    QIODevice *device) {
  self->createQIODeviceConnections(device);
}

//  void QtMultimediaPrivate::QPlatformAudioSourceStream::disconnectQIODevice
//      Connections()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream30disconnectQIODeviceConnectionsEv(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  self->disconnectQIODeviceConnections();
}

//  QIODevice *QtMultimediaPrivate::QPlatformAudioSourceStream::createRingbuf
//      ferReaderDevice()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream28createRingbufferReaderDeviceEv(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  return self->createRingbufferReaderDevice();
}

//  void QtMultimediaPrivate::QPlatformAudioSourceStream::pushToIODevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream14pushToIODeviceEv(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  self->pushToIODevice();
}

//  bool QtMultimediaPrivate::QPlatformAudioSourceStream::deviceIsRingbufferR
//      eader() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream24deviceIsRingbufferReaderEv(
    const QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  return self->deviceIsRingbufferReader();
}

//  void QtMultimediaPrivate::QPlatformAudioSourceStream::finalizeQIODevice(S
//      hutdownPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream17finalizeQIODeviceENS_22QPlatformAudioIOStream14ShutdownPolicyE(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    QtMultimediaPrivate::QPlatformAudioIOStream::ShutdownPolicy a0) {
  self->finalizeQIODevice(a0);
}

//  void QtMultimediaPrivate::QPlatformAudioSourceStream::emptyRingbuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream15emptyRingbufferEv(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  self->emptyRingbuffer();
}

//  void
//      QtMultimediaPrivate::QPlatformAudioSourceStream::updateStreamIdle(boo
//      l a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream16updateStreamIdleEb(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  QThread *QtMultimediaPrivate::QPlatformAudioSourceStream::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK19QtMultimediaPrivate26QPlatformAudioSourceStream6threadEv(
    const QtMultimediaPrivate::QPlatformAudioSourceStream *self) {
  return self->thread();
}

//  a Python function taken by a
//      CuteQtMultimediaPrivate_QPlatformAudioSourceStream, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtMultimediaPrivate_QPlatformAudioSourceStream(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtMultimediaPrivate_QPlatformAudioSourceStream *>(self)->take(key, call);
}
