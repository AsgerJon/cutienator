//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_threaded_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_threaded_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/qaudioengine.h>
#include <QtSpatialAudio/private/qaudioengine_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtSpatialAudio/private/qaudioengine_threaded_p.h>
#include <QtSpatialAudio/private/qaudioengine_withplayer_p.h>
#include <QtCore/qspan.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qaudiosystem_p.h>
#include <QtMultimedia/private/qplatformaudiodevices_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtCore/q20vector.h>
#include <QtSpatialAudio/private/qaudioengine_threaded_p.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/private/qaudio_qspan_support_p.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#ifdef Q_OS_WIN
#  include <QtMultimedia/private/qwindows_wasapi_warmup_client_p.h>
#endif
#include <QtSpatialAudio/qambientsound.h>
#include <QtSpatialAudio/qaudiolistener.h>
#include <QtSpatialAudio/private/qambisonicdecoder_p.h>
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qdebug.h>
#include <QtCore/qelapsedtimer.h>
#include <memory>
#include <QtCore/q20vector.h>
#include <QtSpatialAudio/private/qambisonicdecoder_p.h>
#include <QtMultimedia/private/qaudio_qspan_support_p.h>
#include <QtSpatialAudio/private/qambisonicdecoderdata_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <array>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 28, as local:qambisonicdecoder.cpp:QAmbisonicDecoderData
struct QAmbisonicDecoderData
{
    const QAudioFormat::ChannelConfig config;
    const std::array<const float *, 3> lf;
    const std::array<const float *, 3> hf;
    const float *const reverb;
};

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 36, as local:qambisonicdecoder.cpp:reverb_x_0
constexpr float reverb_x_0[] = {
    1.f, 0.f, // L
    0.f, 1.f, // R
    .7f, .7f, // C
    1.f, 0.f, // Ls
    0.f, 1.f, // Rs
    1.f, 0.f, // Lb
    0.f, 1.f, // Rb
};

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 46, as local:qambisonicdecoder.cpp:reverb_x_1
constexpr float reverb_x_1[] = {
    1.f, 0.f, // L
    0.f, 1.f, // R
    .7f, .7f, // C
    .0f, .0f, // LFE
    1.f, 0.f, // Ls
    0.f, 1.f, // Rs
    1.f, 0.f, // Lb
    0.f, 1.f, // Rb
};

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 82, as local:qambisonicdecoder.cpp:QAmbisonicDecoderFilter
#if defined(Q_PROCESSOR_X86_64)
class QAmbisonicDecoderFilter
{
public:
    QAmbisonicDecoderFilter() = default;
    void configure(float sampleRate, float cutoffFrequency = 380)
    {
        double k = std::tan(M_PI * cutoffFrequency / sampleRate);
        double denom = k * k + 2.0 * k + 1.0;

        a1 = 2.0 * (k * k - 1.0) / denom;
        a2 = (k * k - 2.0 * k + 1.0) / denom;

        b0_lf = (k * k) / denom;
        b1_lf = 2.0 * b0_lf;

        b0_hf = 1.0 / denom;
        b1_hf = -2.0 * b0_hf;
    }

    struct Output
    {
        float lf;
        float hf;
    };

    Output next(float x)
    {
#ifdef Q_PROCESSOR_X86
        // tiny DC offset to prevent denormals, which can cause severe performance degradation on x86 CPUs
        x += 1e-18f;
#endif
        // Process LF
        double r_lf = x * b0_lf + s1_lf;
        s1_lf = x * b1_lf - r_lf * a1 + s2_lf;
        s2_lf = x * b0_lf - r_lf * a2;

        // Process HF
        double r_hf = x * b0_hf + s1_hf;
        s1_hf = x * b1_hf - r_hf * a1 + s2_hf;
        s2_hf = x * b0_hf - r_hf * a2;

        return Output{
            float(r_lf),
            float(r_hf),
        };
    }

private:
    // coefficients
    double a1 = 0.;
    double a2 = 0.;
    double b0_hf = 0.;
    double b1_hf = 0.;
    double b0_lf = 0.;
    double b1_lf = 0.;

    // state
    double s1_lf = 0.0, s2_lf = 0.0;
    double s1_hf = 0.0, s2_hf = 0.0;
};
#endif  // defined(Q_PROCESSOR_X86_64)

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 145, as local:qambisonicdecoder.cpp:inputChannelsForAmbisonicOrder
namespace {
inline int inputChannelsForAmbisonicOrder(QAmbisonicDecoder::AmbisonicOrder ambisonicOrder)
{
    auto order = qToUnderlying(ambisonicOrder);
    Q_ASSERT(order > 0 && order <= 3);
    return (order + 1) * (order + 1);
}
}  // namespace

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 152, as local:qambisonicdecoder.cpp:ambisonicDecoderChannelConfig
namespace {
inline QAudioFormat::ChannelConfig ambisonicDecoderChannelConfig(QAudioFormat::ChannelConfig channelConfig,
                                                          int numberOfOutputChannels)
{
    if (channelConfig == QAudioFormat::ChannelConfigUnknown)
        channelConfig = QAudioFormat::defaultChannelConfigForChannelCount(numberOfOutputChannels);
    return channelConfig;
}
}  // namespace

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 32, as local:qaudioengine_threaded.cpp:bufferTimeMs
const int bufferTimeMs = 100;

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 36, as local:qaudioengine_threaded.cpp:QAudioOutputStream
#if defined(Q_OS_LINUX)
class QAudioOutputStream : public QIODevice
{
public:
    explicit QAudioOutputStream(QAudioEngineThreaded *d) : d(d) { open(QIODevice::ReadOnly); }
    ~QAudioOutputStream() override;

    qint64 readData(char *data, qint64 len) override;

    qint64 writeData(const char *, qint64) override;

    qint64 size() const override { return 0; }
    qint64 bytesAvailable() const override {
        return std::numeric_limits<qint64>::max();
    }
    bool isSequential() const override {
        return true;
    }
    bool atEnd() const override {
        return false;
    }
    qint64 pos() const override {
        return m_pos;
    }

    void startOutput()
    {
        d->mutex.lock();
        Q_ASSERT(!sink);
        auto channelConfig = d->outputMode() == QAudioEngine::Surround
                ? d->m_device.channelConfiguration()
                : QAudioFormat::ChannelConfigStereo;

        QAudioFormat format;
        if (channelConfig != QAudioFormat::ChannelConfigUnknown)
            format.setChannelConfig(channelConfig);
        else
            format.setChannelCount(d->m_device.preferredFormat().channelCount());
        format.setSampleRate(d->sampleRate());
        format.setSampleFormat(QAudioFormat::Int16);

        ambisonicDecoder = std::make_unique<QAmbisonicDecoder>(
                QAmbisonicDecoder::AmbisonicOrder::HighQuality, format.sampleRate(),
                format.channelCount(), format.channelConfig());

        sink = std::make_unique<QAudioSink>(d->m_device, format);
        const qsizetype bufferSize = format.bytesForDuration(bufferTimeMs * 1000);
        sink->setBufferSize(bufferSize);
        d->mutex.unlock();
        // It is important to unlock the mutex before starting the sink, as the sink will
        // call readData() in the audio thread, which will try to lock the mutex (again)
        sink->start(this);

#ifdef Q_OS_WIN
        QtMultimediaPrivate::refreshWarmupClient();
#endif
    }

    void stopOutput()
    {
        if (!sink)
            return;
        sink->stop();
        sink.reset();
        ambisonicDecoder.reset();
    }

    void setPaused(bool paused) {
        if (paused)
            sink->suspend();
        else
            sink->resume();
    }

private:
    qint64 m_pos = 0;
    QAudioEngineThreaded *d = nullptr;
    std::unique_ptr<QAudioSink> sink;
    std::unique_ptr<QAmbisonicDecoder> ambisonicDecoder;
};
#endif  // defined(Q_OS_LINUX)

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 118, as local:qaudioengine_threaded.cpp:QAudioOutputStream::writeData
inline qint64 QAudioOutputStream::writeData(const char *, qint64)
{
    return 0;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 37, as _ZN19QAudioEnginePrivateD2Ev
inline QAudioEnginePrivate::~QAudioEnginePrivate() = default;

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 245, as _ZN20QAudioEngineThreaded4stopEv
inline void QAudioEngineThreaded::stop()
{
    if (!outputStream)
        return; // already stopped

    QMetaObject::invokeMethod(outputStream.get(), &QAudioOutputStream::stopOutput,
                              Qt::BlockingQueuedConnection);
    outputStream.reset();
    audioThread.exit(0);
    audioThread.wait();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 233, as _ZN20QAudioEngineThreaded5startEv
inline void QAudioEngineThreaded::start()
{
    if (outputStream)
        return; // already started

    outputStream = std::make_unique<QAudioOutputStream>(this);
    outputStream->moveToThread(&audioThread);
    audioThread.start(QThread::TimeCriticalPriority);

    QMetaObject::invokeMethod(outputStream.get(), &QAudioOutputStream::startOutput);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 257, as _ZN20QAudioEngineThreaded9setPausedEb
inline void QAudioEngineThreaded::setPaused(bool paused)
{
    if (!outputStream)
        return; // can't pause if not started

    bool old = m_paused.fetchAndStoreRelaxed(paused);
    if (old != paused) {
        if (outputStream)
            outputStream->setPaused(paused);
        Q_Q(QAudioEngine);
        emit q->pausedChanged();
    }
}

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 236, as _ZN17QAmbisonicDecoderD1Ev
inline QAmbisonicDecoder::~QAmbisonicDecoder() = default;

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 271, as _ZNK20QAudioEngineThreaded8isPausedEv
inline bool QAudioEngineThreaded::isPaused() const
{
    return m_paused.loadRelaxed();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 276, as _ZN20QAudioEngineThreaded15setOutputDeviceERK12QAudioDevice
inline void QAudioEngineThreaded::setOutputDevice(const QAudioDevice &device)
{
    if (m_device == device)
        return;
    if (outputStream) {
        qWarning() << "Changing device on a running engine not implemented";
        return;
    }
    m_device = device;
    Q_Q(QAudioEngine);
    emit q->outputDeviceChanged();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 289, as _ZN20QAudioEngineThreaded8addSoundEP25QSpatialAudioSoundPrivate
inline void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate *sound)
{
    std::lock_guard l(mutex);
    playbackStates.emplace(sound, nullptr);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 295, as _ZN20QAudioEngineThreaded11removeSoundEP25QSpatialAudioSoundPrivate
inline void QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *sound)
{
    std::lock_guard l(mutex);
    playbackStates.erase(sound);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 301, as _ZN20QAudioEngineThreaded20setSoundPlaybackDataEP25QSpatialAudioSoundPrivateSt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE
inline void QAudioEngineThreaded::setSoundPlaybackData(QSpatialAudioSoundPrivate *sound,
                                                SharedPlaybackState state)
{
    std::lock_guard l(mutex);
    playbackStates.insert_or_assign(sound, std::move(state));
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 308, as _ZN20QAudioEngineThreaded17updateRoomEffectsEv
inline void QAudioEngineThreaded::updateRoomEffects()
{
    std::lock_guard l(mutex);
    for (auto [sound, key] : playbackStates)
        sound->updateRoomEffects();
}
//  -----------------------------------------------------------------------

//  bool QAudioEngineThreaded::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAudioEngineThreaded8isPausedEv(
    const QAudioEngineThreaded *self) {
  return self->isPaused();
}

//  void QAudioEngineThreaded::setOutputDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded15setOutputDeviceERK12QAudioDevice(
    QAudioEngineThreaded *self,
    const QAudioDevice *device) {
  self->setOutputDevice(*device);
}

//  QAudioDevice QAudioEngineThreaded::outputDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK20QAudioEngineThreaded12outputDeviceEv(
    const QAudioEngineThreaded *self) {
  return new QAudioDevice(self->outputDevice());
}

//  void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded8addSoundEP25QSpatialAudioSoundPrivate(
    QAudioEngineThreaded *self,
    QSpatialAudioSoundPrivate *a0) {
  self->addSound(a0);
}

//  void QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded11removeSoundEP25QSpatialAudioSoundPrivate(
    QAudioEngineThreaded *self,
    QSpatialAudioSoundPrivate *a0) {
  self->removeSound(a0);
}

//  void QAudioEngineThreaded::setSoundPlaybackData(QSpatialAudioSoundPrivate
//      *a0, SharedPlaybackState a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded20setSoundPlaybackDataEP25QSpatialAudioSoundPrivateSt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE(
    QAudioEngineThreaded *self,
    QSpatialAudioSoundPrivate *a0,
    const QAudioEngineThreaded::SharedPlaybackState *a1) {
  self->setSoundPlaybackData(a0, *a1);
}

//  void QAudioEngineThreaded::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded17updateRoomEffectsEv(
    QAudioEngineThreaded *self) {
  self->updateRoomEffects();
}
