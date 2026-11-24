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

//  QnxSndHelpers::HintsDeleter::~HintsDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QnxSndHelpers12HintsDeleterD1Ev(
    QnxSndHelpers::HintsDeleter *self) {
  delete self;
}

#endif  // QT_CONFIG(qnx_io_snd)
