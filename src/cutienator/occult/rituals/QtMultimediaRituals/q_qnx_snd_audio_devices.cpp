//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qqnxsndaudiosink_p.h>
#include <QtMultimedia/private/qqnxsndhelpers_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qthread.h>
#include <QtCore/QLoggingCategory>
#include <algorithm>
#include <QtMultimedia/private/qqnxsndaudiosource_p.h>
#include <QtMultimedia/private/qqnxsndhelpers_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qthread.h>
#include <QtCore/QLoggingCategory>
#include <algorithm>
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

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiodevices.cpp, line 27, as local:qqnxsndaudiodevices.cpp:free_char
namespace {
struct free_char
{
    void operator()(char *c) const { ::free(c); }
};
}  // namespace

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiodevices.cpp, line 32, as local:qqnxsndaudiodevices.cpp:unique_str
namespace {
using unique_str = std::unique_ptr<char, free_char>;
}  // namespace

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiodevices.cpp, line 112, as local:qqnxsndaudiodevices.cpp:hasDeviceFilesForMode
namespace {
inline bool hasDeviceFilesForMode(QAudioDevice::Mode mode)
{
    QDir dir(QStringLiteral("/dev/snd"));
    const char16_t suffix = mode == QAudioDevice::Input ? u'c' : u'p';
    for (const QString &entry : dir.entryList(QDir::Files)) {
        if (entry.startsWith(QStringLiteral("pcm")) && entry.back() == suffix)
            return true;
    }
    return false;
}
}  // namespace

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosink.cpp, line 399, as _ZN16QQnxSndAudioSinkC1E12QAudioDeviceRK12QAudioFormatP7QObject
inline QQnxSndAudioSink::QQnxSndAudioSink(QAudioDevice device, const QAudioFormat &format, QObject *parent)
    : BaseClass{ std::move(device), format, parent }
{
}

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosource.cpp, line 317, as _ZN18QQnxSndAudioSourceC1E12QAudioDeviceRK12QAudioFormatP7QObject
inline QQnxSndAudioSource::QQnxSndAudioSource(QAudioDevice device, const QAudioFormat &format,
                                       QObject *parent)
    : BaseClass{ std::move(device), format, parent }
{
}

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 74, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream11requestStopEv
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioIOStream::requestStop()
{
    m_stopRequested.store(true, std::memory_order_release);
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

//  from ../qtmultimedia/src/multimedia/audio/qaudiosystem_platform_stream_support.cpp, line 41, as _ZN19QtMultimediaPrivate22QPlatformAudioIOStream9setVolumeEf
namespace QtMultimediaPrivate {
using namespace std::chrono_literals;
inline void QPlatformAudioIOStream::setVolume(float volume)
{
    m_volume.store(volume, std::memory_order_relaxed);
}
}  // namespace QtMultimediaPrivate

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosink.cpp, line 48, as _ZN22QQnxSndAudioSinkStream4openEv
inline bool QQnxSndAudioSinkStream::open()
{
    return openPcmDevice();
}

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosink.cpp, line 145, as _ZN22QQnxSndAudioSinkStream4stopEN19QtMultimediaPrivate22QPlatformAudioIOStream14ShutdownPolicyE
inline void QQnxSndAudioSinkStream::stop(ShutdownPolicy shutdownPolicy)
{
    // Draining is meaningless on a suspended stream — downgrade so we
    // can shut down synchronously instead of waiting on a drain that
    // can never complete.
    if (m_suspended.load(std::memory_order_acquire))
        shutdownPolicy = ShutdownPolicy::DiscardRingbuffer;

    m_shutdownPolicy.store(shutdownPolicy, std::memory_order_release);
    requestStop();

    // Sever the source-QIODevice signals on every shutdown path. Otherwise
    // pullFromQIODevice() can fire mid-teardown and refill the ringbuffer
    // we are tearing down. Matches the pipewire backend's pattern.
    disconnectQIODeviceConnections();

    switch (shutdownPolicy) {
    case ShutdownPolicy::DiscardRingbuffer:
        // joinWorkerThread() issues snd_pcm_drop itself to break the
        // worker out of any blocking snd_pcm_writei.
        joinWorkerThread();
        closePcmDevice();
        m_parent.store(nullptr, std::memory_order_release);
        return;
    case ShutdownPolicy::DrainRingbuffer:
        // Clear m_parent now, synchronously on the app thread, before this call
        // returns. The drain completion runs asynchronously and keeps the stream
        // alive via the captured shared_ptr, but the front class (m_parent) may
        // be destroyed as soon as stop() returns. Nulling it here guarantees any
        // worker-originated callback fired during the drain reads nullptr rather
        // than a dangling pointer (the completion lambda re-stores it for
        // defence-in-depth).
        m_parent.store(nullptr, std::memory_order_release);
        m_ringbufferDrained.callOnActivated([self = shared_from_this()]() mutable {
            self->joinWorkerThread();
            self->closePcmDevice();
            self->m_parent.store(nullptr, std::memory_order_release);
            self = {};
        });
        return;
    }
}

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosource.cpp, line 47, as _ZN24QQnxSndAudioSourceStream4openEv
inline bool QQnxSndAudioSourceStream::open()
{
    return openPcmDevice();
}

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosource.cpp, line 138, as _ZN24QQnxSndAudioSourceStream4stopEN19QtMultimediaPrivate22QPlatformAudioIOStream14ShutdownPolicyE
inline void QQnxSndAudioSourceStream::stop(ShutdownPolicy shutdownPolicy)
{
    requestStop();
    disconnectQIODeviceConnections();

    // joinWorkerThread() issues snd_pcm_drop itself to break the worker
    // out of any blocking snd_pcm_readi.
    joinWorkerThread();
    closePcmDevice();
    m_parent.store(nullptr, std::memory_order_release);

    finalizeQIODevice(shutdownPolicy);
    if (shutdownPolicy == ShutdownPolicy::DiscardRingbuffer)
        emptyRingbuffer();
}
//  -----------------------------------------------------------------------

//  QLatin1String QQnxSndAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK19QQnxSndAudioDevices11backendNameEv(
    const QQnxSndAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QQnxSndAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQnxSndAudioDevices14hasCallbackApiEv(
    const QQnxSndAudioDevices *self) {
  return self->hasCallbackApi();
}

#endif  // QT_CONFIG(qnx_io_snd)
