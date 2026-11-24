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

//  QnxSndHelpers::WakePipe::WakePipe()
extern "C" Q_DECL_EXPORT
QnxSndHelpers::WakePipe *ritual_ZN13QnxSndHelpers8WakePipeC1Ev() {
  return new QnxSndHelpers::WakePipe();
}

//  int QnxSndHelpers::WakePipe::readFd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QnxSndHelpers8WakePipe6readFdEv(
    const QnxSndHelpers::WakePipe *self) {
  return self->readFd();
}

//  bool QnxSndHelpers::WakePipe::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QnxSndHelpers8WakePipe6isOpenEv(
    const QnxSndHelpers::WakePipe *self) {
  return self->isOpen();
}

#endif  // QT_CONFIG(qnx_io_snd)
