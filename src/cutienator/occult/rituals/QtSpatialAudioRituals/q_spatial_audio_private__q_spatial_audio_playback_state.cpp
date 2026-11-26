//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiobuffer.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/QSpan>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/private/qaudio_qspan_support_p.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qmultimediautils_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtSpatialAudio/private/qaudioengine_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qurl.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 22, as local:qspatialaudiosound.cpp:InfiniteLoops
namespace QSpatialAudioPrivate {
constexpr int InfiniteLoops = -1;
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 24, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateC1E12QAudioBufferbi
namespace QSpatialAudioPrivate {
inline QSpatialAudioPlaybackState::QSpatialAudioPlaybackState(QAudioBuffer buffer, bool playing, int loops)
    : m_playing(playing), m_loops(loops), m_buffer(std::move(buffer))
{
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 29, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState9getBufferE5QSpanIfLm18446744073709551615EE
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::getBuffer(QSpan<float> output)
{
    using QtMultimediaPrivate::drop;
    using QtMultimediaPrivate::take;
    namespace ranges = QtMultimediaPrivate::ranges;

    if (!m_playing.load(std::memory_order_relaxed)) {
        ranges::fill(output, 0.f);
        return;
    }

    QSpan<const float> wholeSampleBuffer{
        m_buffer.constData<float>(),
        m_buffer.sampleCount(),
    };

    while (!output.empty()) {
        QSpan remainingSamples = drop(wholeSampleBuffer, m_currentSample);
        const QSpan samplesToCopy = take(remainingSamples, output.size());
        ranges::copy(samplesToCopy, output.begin());
        output = drop(output, samplesToCopy.size());
        m_currentSample += samplesToCopy.size();

        if (output.empty())
            return;

        // Reached end of buffer
        Q_ASSERT(m_currentSample == wholeSampleBuffer.size());
        m_currentSample = 0;

        switch (m_loops) {
        case InfiniteLoops:
            break; // Continue looping
        case 0:
            m_playing = false;
            m_currentLoop = 0;
            ranges::fill(output, 0.f);
            return;
        default:
            ++m_currentLoop;
            if (m_currentLoop >= m_loops) {
                m_playing = false;
                m_currentLoop = 0;
                ranges::fill(output, 0.f);
                return;
            }
            break;
        }
    }
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 95, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState5pauseEv
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::pause()
{
    m_playing = false;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 80, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState6resumeEv
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::resume()
{
    m_playing = true;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 85, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState8setLoopsEi
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::setLoops(int loops)
{
    m_loops = loops;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 90, as _ZNK20QSpatialAudioPrivate26QSpatialAudioPlaybackState6formatEv
namespace QSpatialAudioPrivate {
inline QAudioFormat QSpatialAudioPlaybackState::format() const
{
    return m_buffer.format();
}
}  // namespace QSpatialAudioPrivate
//  -----------------------------------------------------------------------

//  QSpatialAudioPrivate::QSpatialAudioPlaybackState::QSpatialAudioPlaybackSt
//      ate(QAudioBuffer buffer, bool playing, int loops)
extern "C" Q_DECL_EXPORT
QSpatialAudioPrivate::QSpatialAudioPlaybackState *ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateC1E12QAudioBufferbi(
    const QAudioBuffer *buffer,
    bool playing,
    int loops) {
  return new QSpatialAudioPrivate::QSpatialAudioPlaybackState(
      *buffer,
      playing,
      loops);
}

//  void
//      QSpatialAudioPrivate::QSpatialAudioPlaybackState::getBuffer(QSpan<flo
//      at> output)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState9getBufferE5QSpanIfLm18446744073709551615EE(
    QSpatialAudioPrivate::QSpatialAudioPlaybackState *self,
    const QSpan<float> *output) {
  self->getBuffer(*output);
}

//  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState5pauseEv(
    QSpatialAudioPrivate::QSpatialAudioPlaybackState *self) {
  self->pause();
}

//  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState6resumeEv(
    QSpatialAudioPrivate::QSpatialAudioPlaybackState *self) {
  self->resume();
}

//  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::setLoops(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState8setLoopsEi(
    QSpatialAudioPrivate::QSpatialAudioPlaybackState *self,
    int a0) {
  self->setLoops(a0);
}

//  QAudioFormat QSpatialAudioPrivate::QSpatialAudioPlaybackState::format()
//      const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK20QSpatialAudioPrivate26QSpatialAudioPlaybackState6formatEv(
    const QSpatialAudioPrivate::QSpatialAudioPlaybackState *self) {
  return new QAudioFormat(self->format());
}
