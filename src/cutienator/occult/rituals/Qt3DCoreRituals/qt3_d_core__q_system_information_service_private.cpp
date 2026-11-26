//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Qt3DCore::QSystemInformationServicePrivate::QSystemInformationServicePriv
//      ate(QAspectEngine *aspectEngine, const QString &description)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationServicePrivate *ritual_ZN8Qt3DCore32QSystemInformationServicePrivateC1EPNS_13QAspectEngineERK7QString(
    Qt3DCore::QAspectEngine *aspectEngine,
    const QString *description) {
  return new Qt3DCore::QSystemInformationServicePrivate(
      aspectEngine,
      *description);
}

//  Qt3DCore::QSystemInformationServicePrivate::~QSystemInformationServicePri
//      vate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore32QSystemInformationServicePrivateD1Ev(
    Qt3DCore::QSystemInformationServicePrivate *self) {
  delete self;
}

//  QSystemInformationServicePrivate *Qt3DCore::QSystemInformationServicePriv
//      ate::get(QSystemInformationService *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationServicePrivate *ritual_ZN8Qt3DCore32QSystemInformationServicePrivate3getEPNS_25QSystemInformationServiceE(
    Qt3DCore::QSystemInformationService *q) {
  return Qt3DCore::QSystemInformationServicePrivate::get(q);
}

//  void Qt3DCore::QSystemInformationServicePrivate::addJobLogStatsEntry(JobR
//      unStats &stats)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore32QSystemInformationServicePrivate19addJobLogStatsEntryERNS0_11JobRunStatsE(
    Qt3DCore::QSystemInformationServicePrivate *self,
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats *stats) {
  self->addJobLogStatsEntry(*stats);
}

//  void Qt3DCore::QSystemInformationServicePrivate::addSubmissionLogStatsEnt
//      ry(JobRunStats &stats)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore32QSystemInformationServicePrivate26addSubmissionLogStatsEntryERNS0_11JobRunStatsE(
    Qt3DCore::QSystemInformationServicePrivate *self,
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats *stats) {
  self->addSubmissionLogStatsEntry(*stats);
}

//  void Qt3DCore::QSystemInformationServicePrivate::writeFrameJobLogStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore32QSystemInformationServicePrivate21writeFrameJobLogStatsEv(
    Qt3DCore::QSystemInformationServicePrivate *self) {
  self->writeFrameJobLogStats();
}

//  void Qt3DCore::QSystemInformationServicePrivate::updateTracing()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore32QSystemInformationServicePrivate13updateTracingEv(
    Qt3DCore::QSystemInformationServicePrivate *self) {
  self->updateTracing();
}

//  QSystemInformationService
//      *Qt3DCore::QSystemInformationServicePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService *ritual_ZN8Qt3DCore32QSystemInformationServicePrivate6q_funcEv(
    Qt3DCore::QSystemInformationServicePrivate *self) {
  return self->q_func();
}

//  const QSystemInformationService
//      *Qt3DCore::QSystemInformationServicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QSystemInformationService *ritual_ZNK8Qt3DCore32QSystemInformationServicePrivate6q_funcEv(
    const Qt3DCore::QSystemInformationServicePrivate *self) {
  return self->q_func();
}
