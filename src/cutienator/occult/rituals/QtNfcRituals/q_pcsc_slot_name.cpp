//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qpcsc_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called. On Windows it is a QString and takes
//  and gives 'wchar_t' text, which is not passed: there only its
//  destructor is written. Not written: 'nameSize', which Qt's
//  library offers not by name, the 'ptr' that gives the text to be
//  written into, and the 'qHash' friend.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/qtnfc-config.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qpcsc_p.h>

#if defined(Q_OS_MACOS)
//  QPcscSlotName::QPcscSlotName(CPtr p)
extern "C" Q_DECL_EXPORT
QPcscSlotName *ritual_ZN13QPcscSlotNameC1EPKc(const char *p) {
  return new QPcscSlotName(p);
}
#endif  // defined(Q_OS_MACOS)

#if defined(Q_OS_MACOS)
//  CPtr QPcscSlotName::ptr() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QPcscSlotName3ptrEv(const QPcscSlotName *self) {
  return self->ptr();
}
#endif  // defined(Q_OS_MACOS)

//  QPcscSlotName::~QPcscSlotName()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPcscSlotNameD1Ev(QPcscSlotName *self) {
  delete self;
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
