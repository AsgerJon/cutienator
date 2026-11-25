//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qpcscslot_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, 'tr', 'processStateChange' and
//  'invalidateInsertedCard', which Qt's library offers not by name.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/qtnfc-config.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qpcscslot_p.h>

//  const QMetaObject *QPcscSlot::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QPcscSlot10metaObjectEv(
    const QPcscSlot *self) {
  return self->metaObject();
}

//  QPcscSlot::~QPcscSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPcscSlotD1Ev(QPcscSlot *self) {
  delete self;
}

//  const QPcscSlotName &QPcscSlot::name() const
extern "C" Q_DECL_EXPORT
QPcscSlotName *ritual_ZNK9QPcscSlot4nameEv(const QPcscSlot *self) {
  return new QPcscSlotName(self->name());
}

//  bool QPcscSlot::hasCard() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPcscSlot7hasCardEv(const QPcscSlot *self) {
  return self->hasCard();
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
