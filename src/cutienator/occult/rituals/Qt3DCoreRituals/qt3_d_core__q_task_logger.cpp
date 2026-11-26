//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
//      const JobId &jobId, Type type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QTaskLogger *ritual_ZN8Qt3DCore11QTaskLoggerC1EPNS_25QSystemInformationServiceERKNS_5JobIdENS0_4TypeE(
    Qt3DCore::QSystemInformationService *service,
    const Qt3DCore::JobId *jobId,
    Qt3DCore::QTaskLogger::Type type) {
  return new Qt3DCore::QTaskLogger(service, *jobId, type);
}

//  Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
//      const quint32 jobType, const quint32 instance, Type type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QTaskLogger *ritual_ZN8Qt3DCore11QTaskLoggerC1EPNS_25QSystemInformationServiceEjjNS0_4TypeE(
    Qt3DCore::QSystemInformationService *service,
    quint32 jobType,
    quint32 instance,
    Qt3DCore::QTaskLogger::Type type) {
  return new Qt3DCore::QTaskLogger(service, jobType, instance, type);
}

//  Qt3DCore::QTaskLogger::~QTaskLogger()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QTaskLoggerD1Ev(Qt3DCore::QTaskLogger *self) {
  delete self;
}

//  void Qt3DCore::QTaskLogger::end(qint64 t)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore11QTaskLogger3endEx(
    Qt3DCore::QTaskLogger *self,
    qint64 t) {
  self->end(t);
}

//  qint64 Qt3DCore::QTaskLogger::restart()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN8Qt3DCore11QTaskLogger7restartEv(
    Qt3DCore::QTaskLogger *self) {
  return self->restart();
}
