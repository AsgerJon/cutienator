//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolstate_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQStyleKitControlState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQStyleKitControlState10metaObjectEv(
    const QQStyleKitControlState *self) {
  return self->metaObject();
}

//  QQSK::State QQStyleKitControlState::nestedState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQStyleKitControlState11nestedStateEv(
    const QQStyleKitControlState *self) {
  return static_cast<int>(self->nestedState().toInt());
}
