//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ItemData::ItemData()
extern "C" Q_DECL_EXPORT
qdesigner_internal::ItemData *ritual_ZN18qdesigner_internal8ItemDataC1Ev() {
  return new qdesigner_internal::ItemData();
}

//  bool qdesigner_internal::ItemData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal8ItemData7isValidEv(
    const qdesigner_internal::ItemData *self) {
  return self->isValid();
}

//  bool operator==(const ItemData &lhs, const ItemData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_8ItemDataES2_(
    const qdesigner_internal::ItemData *lhs,
    const qdesigner_internal::ItemData *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ItemData &lhs, const ItemData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_8ItemDataES2_(
    const qdesigner_internal::ItemData *lhs,
    const qdesigner_internal::ItemData *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::ItemData::~ItemData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ItemDataD1Ev(
    qdesigner_internal::ItemData *self) {
  delete self;
}
