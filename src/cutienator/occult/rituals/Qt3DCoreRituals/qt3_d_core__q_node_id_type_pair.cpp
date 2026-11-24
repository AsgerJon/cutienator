//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qnode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/qnodeid.h>

//  Qt3DCore::QNodeIdTypePair::QNodeIdTypePair()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdTypePair *ritual_ZN8Qt3DCore15QNodeIdTypePairC1Ev() {
  return new Qt3DCore::QNodeIdTypePair();
}

//  Qt3DCore::QNodeIdTypePair::QNodeIdTypePair(QNodeId _id, const QMetaObject
//      *_type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdTypePair *ritual_ZN8Qt3DCore15QNodeIdTypePairC1ENS_7QNodeIdEPK11QMetaObject(
    const Qt3DCore::QNodeId *_id,
    const QMetaObject *_type) {
  return new Qt3DCore::QNodeIdTypePair(*_id, _type);
}

//  Qt3DCore::QNodeIdTypePair::~QNodeIdTypePair()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QNodeIdTypePairD1Ev(
    Qt3DCore::QNodeIdTypePair *self) {
  delete self;
}
