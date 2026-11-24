//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmediarecorder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qmediarecorder.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmediarecorder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QMediaRecorder *QMediaRecorderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMediaRecorder *ritual_ZN21QMediaRecorderPrivate6q_funcEv(
    QMediaRecorderPrivate *self) {
  return self->q_func();
}

//  const QMediaRecorder *QMediaRecorderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMediaRecorder *ritual_ZNK21QMediaRecorderPrivate6q_funcEv(
    const QMediaRecorderPrivate *self) {
  return self->q_func();
}

//  QMediaRecorderPrivate::QMediaRecorderPrivate()
extern "C" Q_DECL_EXPORT
QMediaRecorderPrivate *ritual_ZN21QMediaRecorderPrivateC1Ev() {
  return new QMediaRecorderPrivate();
}

//  QString QMediaRecorderPrivate::msgFailedStartRecording()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QMediaRecorderPrivate23msgFailedStartRecordingEv() {
  return new QString(QMediaRecorderPrivate::msgFailedStartRecording());
}

//  QMediaRecorderPrivate::~QMediaRecorderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaRecorderPrivateD1Ev(QMediaRecorderPrivate *self) {
  delete self;
}
