//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobject.h>

//  QObjectData::~QObjectData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QObjectDataD1Ev(QObjectData *self) {
  delete self;
}

//  const QMetaObject *QObjectData::dynamicMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QObjectData17dynamicMetaObjectEv(
    const QObjectData *self) {
  return self->dynamicMetaObject();
}
