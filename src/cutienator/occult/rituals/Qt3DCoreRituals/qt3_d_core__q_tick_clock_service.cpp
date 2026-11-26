//  Written by hand on 2026-11-25 from
//  Qt3DCore/6.12.0/Qt3DCore/private/qtickclockservice_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. Qt's library
//  offers nothing of this class by name: only its virtual functions are
//  called, through the object. The class marks waitForNextFrame, start and
//  stop 'final', which would make the compiler call Qt's functions, which it
//  does not export, directly: those rituals take 'self' as the
//  QAbstractFrameAdvanceService that declares them, so the call stays
//  virtual. Not written: the constructor and 'tr'.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qtickclockservice_p.h>

//  const QMetaObject *Qt3DCore::QTickClockService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore17QTickClockService10metaObjectEv(
    const Qt3DCore::QTickClockService *self) {
  return self->metaObject();
}

//  Qt3DCore::QTickClockService::~QTickClockService()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QTickClockServiceD1Ev(
    Qt3DCore::QTickClockService *self) {
  delete self;
}

//  qint64 Qt3DCore::QTickClockService::waitForNextFrame()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN8Qt3DCore17QTickClockService16waitForNextFrameEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  return self->waitForNextFrame();
}

//  void Qt3DCore::QTickClockService::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QTickClockService5startEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  self->start();
}

//  void Qt3DCore::QTickClockService::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QTickClockService4stopEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  self->stop();
}

//  QTickClockServicePrivate *Qt3DCore::QTickClockService::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QTickClockServicePrivate *ritual_ZN8Qt3DCore17QTickClockService6d_funcEv(
    Qt3DCore::QTickClockService *self) {
  return self->d_func();
}

//  const QTickClockServicePrivate *Qt3DCore::QTickClockService::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QTickClockServicePrivate *ritual_ZNK8Qt3DCore17QTickClockService6d_funcEv(
    const Qt3DCore::QTickClockService *self) {
  return self->d_func();
}
