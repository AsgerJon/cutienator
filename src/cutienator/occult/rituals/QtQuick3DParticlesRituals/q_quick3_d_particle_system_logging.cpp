//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystemlogging_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystemlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuick3DParticleSystemLogging::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DParticleSystemLogging10metaObjectEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleSystemLogging::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuick3DParticleSystemLogging2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSystemLogging::tr(s, c, n));
}

//  void QQuick3DParticleSystemLogging::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleSystemLogging22qt_qmlMarker_anonymousEv(
    QQuick3DParticleSystemLogging *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuick3DParticleSystemLogging::QQuick3DParticleSystemLogging(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystemLogging *ritual_ZN29QQuick3DParticleSystemLoggingC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleSystemLogging(parent);
}

//  int QQuick3DParticleSystemLogging::loggingInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuick3DParticleSystemLogging15loggingIntervalEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->loggingInterval();
}

//  int QQuick3DParticleSystemLogging::updates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuick3DParticleSystemLogging7updatesEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->updates();
}

//  int QQuick3DParticleSystemLogging::particlesMax() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuick3DParticleSystemLogging12particlesMaxEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->particlesMax();
}

//  int QQuick3DParticleSystemLogging::particlesUsed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuick3DParticleSystemLogging13particlesUsedEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->particlesUsed();
}

//  float QQuick3DParticleSystemLogging::time() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QQuick3DParticleSystemLogging4timeEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->time();
}

//  float QQuick3DParticleSystemLogging::timeAverage() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QQuick3DParticleSystemLogging11timeAverageEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->timeAverage();
}

//  float QQuick3DParticleSystemLogging::timeDeviation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QQuick3DParticleSystemLogging13timeDeviationEv(
    const QQuick3DParticleSystemLogging *self) {
  return self->timeDeviation();
}

//  void QQuick3DParticleSystemLogging::setLoggingInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleSystemLogging18setLoggingIntervalEi(
    QQuick3DParticleSystemLogging *self,
    int interval) {
  self->setLoggingInterval(interval);
}

//  void QQuick3DParticleSystemLogging::updateTimes(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleSystemLogging11updateTimesEx(
    QQuick3DParticleSystemLogging *self,
    qint64 time) {
  self->updateTimes(time);
}

//  void QQuick3DParticleSystemLogging::resetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleSystemLogging9resetDataEv(
    QQuick3DParticleSystemLogging *self) {
  self->resetData();
}
