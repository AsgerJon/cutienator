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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 119, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStreamC1E12QAudioDeviceRK12QAudioFormatSt8optionalIiES5_INS_18NativePeriodFramesEEf
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioSinkStream::QPlatformAudioSinkStream(QAudioDevice audioDevice,
                                                   const QAudioFormat &format,
                                                   std::optional<int> ringbufferSize,
                                                   std::optional<NativePeriodFrames> nativePeriodFrames,
                                                   float volume)
    : QPlatformAudioIOStream{
          std::move(audioDevice), format, ringbufferSize, nativePeriodFrames, volume,
      }
{
    m_streamIdleDetectionConnection = m_streamIdleDetectionNotifier.callOnActivated([this] {
        if (isStopRequested())
            return;

        bool sinkIsIdle = m_streamIsIdle.load();

        if (sinkIsIdle) {
            // data has been pushed to the ringbuffer, while the stream is
            // still idle, this will change during the next audio callback
            bool ringbufferIsEmpty = visitRingbuffer([&](auto &ringbuffer) {
                return ringbuffer.free() == ringbuffer.size();
            });

            sinkIsIdle = ringbufferIsEmpty;
        }

        updateStreamIdle(sinkIsIdle);
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 148, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStreamD1Ev
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioSinkStream::~QPlatformAudioSinkStream() = default;
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 209, as _ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream9bytesFreeEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline quint64 QPlatformAudioSinkStream::bytesFree() const
{
    return visitRingbuffer([](auto &ringbuffer) {
        using SampleType = typename std::decay_t<decltype(ringbuffer)>::ValueType;
        return ringbuffer.free() * sizeof(SampleType);
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 217, as _ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream17processedDurationEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline std::chrono::microseconds QPlatformAudioSinkStream::processedDuration() const
{
    return std::chrono::microseconds{
        m_processedFrameCount * 1'000'000 / m_format.sampleRate(),
    };
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 267, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream28createRingbufferWriterDeviceEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QIODevice *QPlatformAudioSinkStream::createRingbufferWriterDevice()
{
    m_ringbufferWriterDevice = visitRingbuffer(
            [&](auto &ringbuffer) -> std::unique_ptr<QtPrivate::QIODeviceRingBufferWriterBase> {
        using SampleType = typename std::decay_t<decltype(ringbuffer)>::ValueType;
        return std::make_unique<QtPrivate::QIODeviceRingBufferWriter<SampleType>>(&ringbuffer);
    });

    return m_ringbufferWriterDevice.get();
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 278, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream12setQIODeviceEP9QIODevice
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::setQIODevice(QIODevice *device)
{
    m_device = device;
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 244, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream26createQIODeviceConnectionsEP9QIODevice
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::createQIODeviceConnections(QIODevice *device)
{
    // consumed from audio thread
    m_ringbufferHasSpaceConnection = m_ringbufferHasSpace.callOnActivated(device, [this] {
        pullFromQIODevice();
    });

    // data has been pushed to device
    m_iodeviceHasNewDataConnection =
            QObject::connect(device, &QIODevice::readyRead, device, [this] {
        withPullIODeviceReentrancyGuard([this] {
            pullFromQIODeviceImpl();
            updateStreamIdle(false);
        });
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 261, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream30disconnectQIODeviceConnectionsEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::disconnectQIODeviceConnections()
{
    QObject::disconnect(m_ringbufferHasSpaceConnection);
    QObject::disconnect(m_iodeviceHasNewDataConnection);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 224, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream17pullFromQIODeviceEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::pullFromQIODevice()
{
    withPullIODeviceReentrancyGuard([this] {
        pullFromQIODeviceImpl();
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 283, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream12setIdleStateEb
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::setIdleState(bool x)
{
    m_streamIsIdle.store(x);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 288, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream17stopIdleDetectionEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::stopIdleDetection()
{
    QObject::disconnect(m_streamIdleDetectionConnection);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 293, as _ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream6threadEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QThread *QPlatformAudioSinkStream::thread() const
{
    // QPlatformAudioSinkStream is not a QObject, but still has a notion of an application thread
    // where it lives on.
    return m_streamIdleDetectionNotifier.thread();
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 231, as _ZN19QtMultimediaPrivate24QPlatformAudioSinkStream21pullFromQIODeviceImplEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioSinkStream::pullFromQIODeviceImpl()
{
    Q_ASSERT(thread()->isCurrentThread());
    Q_ASSERT(m_device);
    Q_ASSERT(m_pullIODeviceReentrancyGuard);

    visitRingbuffer([&](auto &ringbuffer) {
        int elementsPulled = pullFromQIODeviceToRingbuffer(*m_device, ringbuffer);
        if (elementsPulled)
            updateStreamIdle(false);
    });
}
}  // namespace QtMultimediaPrivate
//  -----------------------------------------------------------------------

//  A QtMultimediaPrivate::QPlatformAudioSinkStream that Python can take functions over in. Every QtMultimediaPrivate::QPlatformAudioSinkStream
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtMultimediaPrivate_QPlatformAudioSinkStreamCall0)(const void *, bool, int *);
class CuteQtMultimediaPrivate_QPlatformAudioSinkStream : public QtMultimediaPrivate::QPlatformAudioSinkStream {
public:
  using QtMultimediaPrivate::QPlatformAudioSinkStream::QPlatformAudioSinkStream;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream16updateStreamIdleEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void
  //      QtMultimediaPrivate::QPlatformAudioSinkStream::updateStreamIdle(b
  //      ool a0)
  void updateStreamIdle(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtMultimediaPrivate_QPlatformAudioSinkStreamCall0 call = reinterpret_cast<CuteQtMultimediaPrivate_QPlatformAudioSinkStreamCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
};

//  QtMultimediaPrivate::QPlatformAudioSinkStream::QPlatformAudioSinkStream(Q
//      AudioDevice a0, const QAudioFormat &a1, std::optional<int>
//      ringbufferSize, std::optional<NativePeriodFrames> nativePeriodFrames,
//      float volume)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QPlatformAudioSinkStream *ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStreamC1E12QAudioDeviceRK12QAudioFormatSt8optionalIiES5_INS_18NativePeriodFramesEEf(
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    const std::optional<int> *ringbufferSize,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames,
    float volume) {
  return new CuteQtMultimediaPrivate_QPlatformAudioSinkStream(
      *a0,
      *a1,
      *ringbufferSize,
      *nativePeriodFrames,
      volume);
}

//  QtMultimediaPrivate::QPlatformAudioSinkStream::~QPlatformAudioSinkStream(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStreamD1Ev(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  delete self;
}

//  quint64 QtMultimediaPrivate::QPlatformAudioSinkStream::bytesFree() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream9bytesFreeEv(
    const QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  return self->bytesFree();
}

//  std::chrono::microseconds
//      QtMultimediaPrivate::QPlatformAudioSinkStream::processedDuration()
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream17processedDurationEv(
    const QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  return static_cast<long long>(self->processedDuration().count());
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::updateStreamIdle(bool
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream16updateStreamIdleEb(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  QIODevice *QtMultimediaPrivate::QPlatformAudioSinkStream::createRingbuffe
//      rWriterDevice()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream28createRingbufferWriterDeviceEv(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  return self->createRingbufferWriterDevice();
}

//  void
//      QtMultimediaPrivate::QPlatformAudioSinkStream::setQIODevice(QIODevice
//      *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream12setQIODeviceEP9QIODevice(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    QIODevice *device) {
  self->setQIODevice(device);
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::createQIODeviceConnec
//      tions(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream26createQIODeviceConnectionsEP9QIODevice(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    QIODevice *device) {
  self->createQIODeviceConnections(device);
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::disconnectQIODeviceCo
//      nnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream30disconnectQIODeviceConnectionsEv(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  self->disconnectQIODeviceConnections();
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::pullFromQIODevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream17pullFromQIODeviceEv(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  self->pullFromQIODevice();
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::setIdleState(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream12setIdleStateEb(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    bool a0) {
  self->setIdleState(a0);
}

//  bool
//      QtMultimediaPrivate::QPlatformAudioSinkStream::isIdle(std::memory_ord
//      er order) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream6isIdleESt12memory_order(
    const QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    const std::memory_order *order) {
  return self->isIdle(*order);
}

//  void QtMultimediaPrivate::QPlatformAudioSinkStream::stopIdleDetection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream17stopIdleDetectionEv(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  self->stopIdleDetection();
}

//  QThread *QtMultimediaPrivate::QPlatformAudioSinkStream::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK19QtMultimediaPrivate24QPlatformAudioSinkStream6threadEv(
    const QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  return self->thread();
}

//  void
//      QtMultimediaPrivate::QPlatformAudioSinkStream::pullFromQIODeviceImpl(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate24QPlatformAudioSinkStream21pullFromQIODeviceImplEv(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self) {
  self->pullFromQIODeviceImpl();
}

//  a Python function taken by a
//      CuteQtMultimediaPrivate_QPlatformAudioSinkStream, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtMultimediaPrivate_QPlatformAudioSinkStream(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtMultimediaPrivate_QPlatformAudioSinkStream *>(self)->take(key, call);
}
