//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'qprint_p.h' and the ritual stand
//  under '__has_include(<cups/ppd.h>)' where Qt's 'qprint_p.h' includes
//  that header of CUPS (macOS, and Unix where Qt has 'cups'), as a
//  Linux without the headers of CUPS refused the file; elsewhere, as on
//  Windows, they stay as they were. Kept as it is when the generator
//  runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#if __has_include(<cups/ppd.h>) \
    || !(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPrint::InputSlot::~InputSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPrint9InputSlotD1Ev(QPrint::InputSlot *self) {
  delete self;
}

#endif  // __has_include(<cups/ppd.h>) || !(defined(Q_OS_MACOS)
        //     || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#endif  // !defined(QT_NO_PRINTER)
