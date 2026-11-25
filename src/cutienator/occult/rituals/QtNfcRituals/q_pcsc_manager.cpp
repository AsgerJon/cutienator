//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qpcscmanager_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, 'tr', 'connectToCard', the slots
//  and the signal.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/qtnfc-config.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qpcscmanager_p.h>

//  const QMetaObject *QPcscManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QPcscManager10metaObjectEv(
    const QPcscManager *self) {
  return self->metaObject();
}

//  QPcscManager::~QPcscManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPcscManagerD1Ev(QPcscManager *self) {
  delete self;
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
