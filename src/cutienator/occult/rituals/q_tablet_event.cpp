//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QTabletEvent *QTabletEvent::clone() const
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZNK12QTabletEvent5cloneEv(const QTabletEvent *self) {
  return self->clone();
}

//  QTabletEvent::~QTabletEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTabletEventD1Ev(QTabletEvent *self) {
  delete self;
}

//  QTabletEvent::QTabletEvent(Type t, const QPointingDevice *device, const
//      QPointF &pos, const QPointF &globalPos, qreal pressure, float xTilt,
//      float yTilt, float tangentialPressure, qreal rotation, float z,
//      Qt::KeyboardModifiers keyState, Qt::MouseButton button,
//      Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZN12QTabletEventC1EN6QEvent4TypeEPK15QPointingDeviceRK7QPointFS7_dfffdf6QFlagsIN2Qt16KeyboardModifierEENS9_11MouseButtonES8_ISC_E(
    QEvent::Type t,
    const QPointingDevice *device,
    const QPointF *pos,
    const QPointF *globalPos,
    qreal pressure,
    float xTilt,
    float yTilt,
    float tangentialPressure,
    qreal rotation,
    float z,
    int keyState,
    Qt::MouseButton button,
    int buttons) {
  return new QTabletEvent(
      t,
      device,
      *pos,
      *globalPos,
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(keyState),
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  QPoint QTabletEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QTabletEvent3posEv(const QTabletEvent *self) {
  return new QPoint(self->pos());
}

//  QPoint QTabletEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QTabletEvent9globalPosEv(const QTabletEvent *self) {
  return new QPoint(self->globalPos());
}

//  const QPointF QTabletEvent::posF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QTabletEvent4posFEv(const QTabletEvent *self) {
  return new QPointF(self->posF());
}

//  const QPointF QTabletEvent::globalPosF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QTabletEvent10globalPosFEv(const QTabletEvent *self) {
  return new QPointF(self->globalPosF());
}

//  int QTabletEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent1xEv(const QTabletEvent *self) {
  return self->x();
}

//  int QTabletEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent1yEv(const QTabletEvent *self) {
  return self->y();
}

//  int QTabletEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent7globalXEv(const QTabletEvent *self) {
  return self->globalX();
}

//  int QTabletEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent7globalYEv(const QTabletEvent *self) {
  return self->globalY();
}

//  qreal QTabletEvent::hiResGlobalX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent12hiResGlobalXEv(const QTabletEvent *self) {
  return self->hiResGlobalX();
}

//  qreal QTabletEvent::hiResGlobalY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent12hiResGlobalYEv(const QTabletEvent *self) {
  return self->hiResGlobalY();
}

//  qint64 QTabletEvent::uniqueId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QTabletEvent8uniqueIdEv(const QTabletEvent *self) {
  return self->uniqueId();
}

//  qreal QTabletEvent::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent8pressureEv(const QTabletEvent *self) {
  return self->pressure();
}

//  qreal QTabletEvent::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent8rotationEv(const QTabletEvent *self) {
  return self->rotation();
}

//  qreal QTabletEvent::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent1zEv(const QTabletEvent *self) {
  return self->z();
}

//  qreal QTabletEvent::tangentialPressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent18tangentialPressureEv(
    const QTabletEvent *self) {
  return self->tangentialPressure();
}

//  qreal QTabletEvent::xTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent5xTiltEv(const QTabletEvent *self) {
  return self->xTilt();
}

//  qreal QTabletEvent::yTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent5yTiltEv(const QTabletEvent *self) {
  return self->yTilt();
}
