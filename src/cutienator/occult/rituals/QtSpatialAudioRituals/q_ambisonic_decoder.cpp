//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qambisonicdecoder_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: the class QAmbisonicDecoderFilter, taken
//  from Qt's qambisonicdecoder.cpp, no longer stands under
//  'defined(Q_PROCESSOR_X86_64)', which Qt does not write there: Qt defines
//  it for every processor, only one line of it for x86, and the destructor
//  taken, which stands everywhere here, needs it whole (Apple silicon
//  refused it). Kept as it is when the generator runs again.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qambisonicdecoder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtmultimedia/src/spatialaudio/qambisonicdecoder.cpp, line 236, as _ZN17QAmbisonicDecoderD1Ev
inline QAmbisonicDecoder::~QAmbisonicDecoder() = default;
//  -----------------------------------------------------------------------

//  QAmbisonicDecoder::~QAmbisonicDecoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAmbisonicDecoderD1Ev(QAmbisonicDecoder *self) {
  delete self;
}

//  bool QAmbisonicDecoder::hasValidConfig() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAmbisonicDecoder14hasValidConfigEv(
    const QAmbisonicDecoder *self) {
  return self->hasValidConfig();
}

//  int QAmbisonicDecoder::nInputChannels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAmbisonicDecoder14nInputChannelsEv(
    const QAmbisonicDecoder *self) {
  return self->nInputChannels();
}

//  int QAmbisonicDecoder::nOutputChannels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAmbisonicDecoder15nOutputChannelsEv(
    const QAmbisonicDecoder *self) {
  return self->nOutputChannels();
}

//  int QAmbisonicDecoder::outputSamples(int nFrames) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAmbisonicDecoder13outputSamplesEi(
    const QAmbisonicDecoder *self,
    int nFrames) {
  return self->outputSamples(nFrames);
}
