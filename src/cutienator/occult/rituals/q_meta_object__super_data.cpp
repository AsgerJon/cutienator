//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QMetaObject::SuperData::SuperData()
extern "C" Q_DECL_EXPORT
QMetaObject::SuperData *ritual_ZN11QMetaObject9SuperDataC1Ev() {
  return new QMetaObject::SuperData();
}

//  QMetaObject::SuperData::SuperData(const QMetaObject *mo)
extern "C" Q_DECL_EXPORT
QMetaObject::SuperData *ritual_ZN11QMetaObject9SuperDataC1EPKS_(
    const QMetaObject *mo) {
  return new QMetaObject::SuperData(mo);
}

//  const QMetaObject *QMetaObject::SuperData::operator->() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMetaObject9SuperDataptEv(
    const QMetaObject::SuperData *self) {
  return self->operator->();
}

//  const QMetaObject *QMetaObject::SuperData::operator const QMetaObject *()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMetaObject9SuperDatacvPKS_Ev(
    const QMetaObject::SuperData *self) {
  return self->operator const QMetaObject *();
}

//  QMetaObject::SuperData::~SuperData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObject9SuperDataD1Ev(QMetaObject::SuperData *self) {
  delete self;
}
