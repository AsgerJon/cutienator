//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiohelpers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiohelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAudioHelperInternal::CatmullRomInterpolator::CatmullRomInterpolator(int
//      nChannels, int inputRate, int outputRate)
extern "C" Q_DECL_EXPORT
QAudioHelperInternal::CatmullRomInterpolator *ritual_ZN20QAudioHelperInternal22CatmullRomInterpolatorC1Eiii(
    int nChannels,
    int inputRate,
    int outputRate) {
  return new QAudioHelperInternal::CatmullRomInterpolator(
      nChannels,
      inputRate,
      outputRate);
}

//  QAudioHelperInternal::CatmullRomInterpolator::~CatmullRomInterpolator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioHelperInternal22CatmullRomInterpolatorD1Ev(
    QAudioHelperInternal::CatmullRomInterpolator *self) {
  delete self;
}

//  void QAudioHelperInternal::CatmullRomInterpolator::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioHelperInternal22CatmullRomInterpolator5resetEv(
    QAudioHelperInternal::CatmullRomInterpolator *self) {
  self->reset();
}

//  void QAudioHelperInternal::CatmullRomInterpolator::advancePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioHelperInternal22CatmullRomInterpolator15advancePositionEv(
    QAudioHelperInternal::CatmullRomInterpolator *self) {
  self->advancePosition();
}
