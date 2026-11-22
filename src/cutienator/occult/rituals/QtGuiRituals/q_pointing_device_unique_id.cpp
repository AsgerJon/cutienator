//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpointingdevice.h>

//  QPointingDeviceUniqueId::QPointingDeviceUniqueId()
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZN23QPointingDeviceUniqueIdC1Ev() {
  return new QPointingDeviceUniqueId();
}

//  QPointingDeviceUniqueId QPointingDeviceUniqueId::fromNumericId(qint64 id)
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZN23QPointingDeviceUniqueId13fromNumericIdEx(
    qint64 id) {
  return new QPointingDeviceUniqueId(
      QPointingDeviceUniqueId::fromNumericId(
          id));
}

//  bool QPointingDeviceUniqueId::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPointingDeviceUniqueId7isValidEv(
    const QPointingDeviceUniqueId *self) {
  return self->isValid();
}

//  qint64 QPointingDeviceUniqueId::numericId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK23QPointingDeviceUniqueId9numericIdEv(
    const QPointingDeviceUniqueId *self) {
  return self->numericId();
}

//  bool operator==(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq23QPointingDeviceUniqueIdS_(
    const QPointingDeviceUniqueId *lhs,
    const QPointingDeviceUniqueId *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zne23QPointingDeviceUniqueIdS_(
    const QPointingDeviceUniqueId *lhs,
    const QPointingDeviceUniqueId *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QPointingDeviceUniqueId::~QPointingDeviceUniqueId()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPointingDeviceUniqueIdD1Ev(QPointingDeviceUniqueId *self) {
  delete self;
}
