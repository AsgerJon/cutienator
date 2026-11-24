//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioresampler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioresampler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiobuffer.h>

//  QPlatformAudioResampler::~QPlatformAudioResampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformAudioResamplerD1Ev(QPlatformAudioResampler *self) {
  delete self;
}

//  QAudioBuffer QPlatformAudioResampler::resample(const char *data, size_t
//      size)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN23QPlatformAudioResampler8resampleEPKcm(
    QPlatformAudioResampler *self,
    const char *data,
    size_t size) {
  return new QAudioBuffer(self->resample(data, size));
}
