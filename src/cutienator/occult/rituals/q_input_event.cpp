//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QInputEvent *QInputEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputEvent *ritual_ZNK11QInputEvent5cloneEv(const QInputEvent *self) {
  return self->clone();
}

//  QInputEvent::~QInputEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEventD1Ev(QInputEvent *self) {
  delete self;
}

//  QInputEvent::QInputEvent(Type type, const QInputDevice *m_dev,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QInputEvent *ritual_ZN11QInputEventC1EN6QEvent4TypeEPK12QInputDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QEvent::Type type,
    const QInputDevice *m_dev,
    int modifiers) {
  return new QInputEvent(
      type,
      m_dev,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  const QInputDevice *QInputEvent::device() const
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZNK11QInputEvent6deviceEv(
    const QInputEvent *self) {
  return self->device();
}

//  QInputDevice::DeviceType QInputEvent::deviceType() const
extern "C" Q_DECL_EXPORT
QInputDevice::DeviceType ritual_ZNK11QInputEvent10deviceTypeEv(
    const QInputEvent *self) {
  return self->deviceType();
}

//  Qt::KeyboardModifiers QInputEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QInputEvent9modifiersEv(const QInputEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QInputEvent::setModifiers(Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QInputEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  quint64 QInputEvent::timestamp() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK11QInputEvent9timestampEv(const QInputEvent *self) {
  return self->timestamp();
}

//  void QInputEvent::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QInputEvent12setTimestampEy(
    QInputEvent *self,
    quint64 timestamp) {
  self->setTimestamp(timestamp);
}
