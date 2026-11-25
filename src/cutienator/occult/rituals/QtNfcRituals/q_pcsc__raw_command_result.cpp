//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qpcsc_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this struct by name: only what its
//  header writes out is called. Not written: 'QPcsc::errorMessage',
//  which Qt's library offers not by name.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/qtnfc-config.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qpcsc_p.h>

//  bool QPcsc::RawCommandResult::isOk() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QPcsc16RawCommandResult4isOkEv(
    const QPcsc::RawCommandResult *self) {
  return self->isOk();
}

//  QPcsc::RawCommandResult::~RawCommandResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QPcsc16RawCommandResultD1Ev(QPcsc::RawCommandResult *self) {
  delete self;
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_MACOS)) && QT_CONFIG(pcsclite)
