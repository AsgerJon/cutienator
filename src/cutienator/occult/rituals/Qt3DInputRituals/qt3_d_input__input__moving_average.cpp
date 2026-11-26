//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/movingaverage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/movingaverage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/movingaverage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/movingaverage.cpp, line 11, as _ZN9Qt3DInput5Input13MovingAverageC1Ej
namespace Qt3DInput::Input {
inline MovingAverage::MovingAverage(unsigned int samples)
    : m_maxSampleCount(samples)
    , m_sampleCount(0)
    , m_currentSample(0)
    , m_total(0.0f)
    , m_samples(samples)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/movingaverage.cpp, line 20, as _ZN9Qt3DInput5Input13MovingAverage9addSampleEf
namespace Qt3DInput::Input {
inline void MovingAverage::addSample(float sample)
{
    if (m_sampleCount == m_maxSampleCount)
        m_total -= m_samples[m_currentSample];
    else
        ++m_sampleCount;

    m_samples[m_currentSample] = sample;
    m_total += sample;
    ++m_currentSample;
    if (m_currentSample >= m_maxSampleCount)
        m_currentSample = 0;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/movingaverage.cpp, line 34, as _ZNK9Qt3DInput5Input13MovingAverage7averageEv
namespace Qt3DInput::Input {
inline float MovingAverage::average() const
{
    return m_sampleCount ? m_total / static_cast<float>(m_sampleCount) : 0.0f;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::MovingAverage::MovingAverage(unsigned int samples)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MovingAverage *ritual_ZN9Qt3DInput5Input13MovingAverageC1Ej(
    unsigned int samples) {
  return new Qt3DInput::Input::MovingAverage(samples);
}

//  void Qt3DInput::Input::MovingAverage::addSample(float sample)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13MovingAverage9addSampleEf(
    Qt3DInput::Input::MovingAverage *self,
    float sample) {
  self->addSample(sample);
}

//  float Qt3DInput::Input::MovingAverage::average() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input13MovingAverage7averageEv(
    const Qt3DInput::Input::MovingAverage *self) {
  return self->average();
}

//  Qt3DInput::Input::MovingAverage::~MovingAverage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13MovingAverageD1Ev(
    Qt3DInput::Input::MovingAverage *self) {
  delete self;
}
