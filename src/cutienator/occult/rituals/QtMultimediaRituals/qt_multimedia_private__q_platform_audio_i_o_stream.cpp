//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiodevice.h>
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

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 16, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStreamC1E12QAudioDevice12QAudioFormatSt8optionalIiES3_INS_18NativePeriodFramesEEf
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

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 36, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStreamD1Ev
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline QPlatformAudioIOStream::~QPlatformAudioIOStream()
{
    Q_ASSERT(m_stopRequested);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 41, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream9setVolumeEf
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioIOStream::setVolume(float volume)
{
    m_volume.store(volume, std::memory_order_relaxed);
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

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 109, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream21ringbufferSizeInBytesEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline int QPlatformAudioIOStream::ringbufferSizeInBytes()
{
    return visitRingbuffer([](auto &ringbuffer) {
        using SampleType = typename std::decay_t<decltype(ringbuffer)>::ValueType;
        return ringbuffer.size() * sizeof(SampleType);
    });
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 74, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream11requestStopEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioIOStream::requestStop()
{
    m_stopRequested.store(true, std::memory_order_release);
}
}  // namespace QtMultimediaPrivate
//  -----------------------------------------------------------------------

//  qsizetype
//      QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferFrames(co
//      nst std::optional<int> &ringbufferSize, const
//      std::optional<NativePeriodFrames> &nativePeriodFrames, const
//      QAudioFormat &a2)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream21inferRingbufferFramesERKSt8optionalIiERKS1_INS_18NativePeriodFramesEERK12QAudioFormat(
    const std::optional<int> *ringbufferSize,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames,
    const QAudioFormat *a2) {
  return QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferFrames(
      *ringbufferSize,
      *nativePeriodFrames,
      *a2);
}

//  qsizetype
//      QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferBytes(con
//      st std::optional<int> &ringbufferSize, const
//      std::optional<NativePeriodFrames> &nativePeriodFrames, const
//      QAudioFormat &a2)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream20inferRingbufferBytesERKSt8optionalIiERKS1_INS_18NativePeriodFramesEERK12QAudioFormat(
    const std::optional<int> *ringbufferSize,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames,
    const QAudioFormat *a2) {
  return QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferBytes(
      *ringbufferSize,
      *nativePeriodFrames,
      *a2);
}

//  QtMultimediaPrivate::QPlatformAudioIOStream::QPlatformAudioIOStream(QAudi
//      oDevice m_audioDevice, QAudioFormat m_format, std::optional<int>
//      ringbufferSize, std::optional<NativePeriodFrames> nativePeriodFrames,
//      float volume)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QPlatformAudioIOStream *ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStreamC1E12QAudioDevice12QAudioFormatSt8optionalIiES3_INS_18NativePeriodFramesEEf(
    const QAudioDevice *m_audioDevice,
    const QAudioFormat *m_format,
    const std::optional<int> *ringbufferSize,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames,
    float volume) {
  return new QtMultimediaPrivate::QPlatformAudioIOStream(
      *m_audioDevice,
      *m_format,
      *ringbufferSize,
      *nativePeriodFrames,
      volume);
}

//  QtMultimediaPrivate::QPlatformAudioIOStream::~QPlatformAudioIOStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStreamD1Ev(
    QtMultimediaPrivate::QPlatformAudioIOStream *self) {
  delete self;
}

//  void QtMultimediaPrivate::QPlatformAudioIOStream::setVolume(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream9setVolumeEf(
    QtMultimediaPrivate::QPlatformAudioIOStream *self,
    float a0) {
  self->setVolume(a0);
}

//  float QtMultimediaPrivate::QPlatformAudioIOStream::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QtMultimediaPrivate22QPlatformAudioIOStream6volumeEv(
    const QtMultimediaPrivate::QPlatformAudioIOStream *self) {
  return self->volume();
}

//  void QtMultimediaPrivate::QPlatformAudioIOStream::prepareRingbuffer(std::
//      optional<int> ringbufferSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream17prepareRingbufferESt8optionalIiE(
    QtMultimediaPrivate::QPlatformAudioIOStream *self,
    const std::optional<int> *ringbufferSize) {
  self->prepareRingbuffer(*ringbufferSize);
}

//  int QtMultimediaPrivate::QPlatformAudioIOStream::ringbufferSizeInBytes()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream21ringbufferSizeInBytesEv(
    QtMultimediaPrivate::QPlatformAudioIOStream *self) {
  return self->ringbufferSizeInBytes();
}

//  void QtMultimediaPrivate::QPlatformAudioIOStream::requestStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream11requestStopEv(
    QtMultimediaPrivate::QPlatformAudioIOStream *self) {
  self->requestStop();
}

//  bool QtMultimediaPrivate::QPlatformAudioIOStream::isStopRequested(std::me
//      mory_order memory_order) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate22QPlatformAudioIOStream15isStopRequestedESt12memory_order(
    const QtMultimediaPrivate::QPlatformAudioIOStream *self,
    const std::memory_order *memory_order) {
  return self->isStopRequested(*memory_order);
}
