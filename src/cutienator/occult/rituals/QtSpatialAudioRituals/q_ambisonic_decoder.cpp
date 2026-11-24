//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qambisonicdecoder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qambisonicdecoder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
