//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndhelpers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndhelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QnxSndHelpers::PcmOpenResult::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QnxSndHelpers13PcmOpenResultcvbEv(
    const QnxSndHelpers::PcmOpenResult *self) {
  return self->operator bool();
}

//  QnxSndHelpers::PcmOpenResult::~PcmOpenResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QnxSndHelpers13PcmOpenResultD1Ev(
    QnxSndHelpers::PcmOpenResult *self) {
  delete self;
}

#endif  // QT_CONFIG(qnx_io_snd)
