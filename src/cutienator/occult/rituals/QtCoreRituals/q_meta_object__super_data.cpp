//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QMetaObject::SuperData::SuperData()
extern "C" Q_DECL_EXPORT
QMetaObject::SuperData *ritual_ZN11QMetaObject9SuperDataC1Ev() {
  return new QMetaObject::SuperData();
}

//  QMetaObject::SuperData::SuperData(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QMetaObject::SuperData *ritual_ZN11QMetaObject9SuperDataC1EDn() {
  return new QMetaObject::SuperData(nullptr);
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

#if !(defined(QT_NO_DATA_RELOCATION))
//  QMetaObject::SuperData::SuperData(Getter g)
extern "C" Q_DECL_EXPORT
QMetaObject::SuperData *ritual_ZN11QMetaObject9SuperDataC1EPFPKS_vE(
    void *g) {
  return new QMetaObject::SuperData(
      reinterpret_cast<QMetaObject::SuperData::Getter>(g));
}
#endif  // !(defined(QT_NO_DATA_RELOCATION))

#if !(defined(QT_NO_DATA_RELOCATION))
//  const QMetaObject *QMetaObject::SuperData::operator const QMetaObject *()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMetaObject9SuperDatacvPKS_Ev(
    const QMetaObject::SuperData *self) {
  return self->operator const QMetaObject *();
}
#endif  // !(defined(QT_NO_DATA_RELOCATION))

//  QMetaObject::SuperData::~SuperData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObject9SuperDataD1Ev(QMetaObject::SuperData *self) {
  delete self;
}
