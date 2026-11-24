//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>

//  QQSK::Property PropertyPathId::property() const
extern "C" Q_DECL_EXPORT
QQSK::Property ritual_ZNK14PropertyPathId8propertyEv(
    const PropertyPathId *self) {
  return self->property();
}

//  PropertyPathId_t PropertyPathId::pathId() const
extern "C" Q_DECL_EXPORT
PropertyPathId_t ritual_ZNK14PropertyPathId6pathIdEv(
    const PropertyPathId *self) {
  return self->pathId();
}

//  PropertyStorageId PropertyPathId::storageId(QQSK::State state) const
extern "C" Q_DECL_EXPORT
PropertyStorageId ritual_ZNK14PropertyPathId9storageIdE6QFlagsIN4QQSK9StateFlagEE(
    const PropertyPathId *self,
    int state) {
  return self->storageId(QFlags<QQSK::StateFlag>::fromInt(state));
}

//  PropertyPathId::~PropertyPathId()
extern "C" Q_DECL_EXPORT
void ritual_ZN14PropertyPathIdD1Ev(PropertyPathId *self) {
  delete self;
}
