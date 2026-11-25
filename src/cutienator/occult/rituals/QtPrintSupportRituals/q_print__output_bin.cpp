//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the '#if' the whole file stands under
//  now also asks '__has_include(<cups/ppd.h>)' where Qt's 'qprint_p.h'
//  includes that header of CUPS, on macOS and on Unix with
//  'QT_CONFIG(cups)', since a machine without the headers of CUPS, as
//  GitHub's Linux, refused the file. Kept as it is when the generator
//  runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER) && \
    (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || \
     __has_include(<cups/ppd.h>))
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPrint::OutputBin::~OutputBin()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPrint9OutputBinD1Ev(QPrint::OutputBin *self) {
  delete self;
}

#endif  // !defined(QT_NO_PRINTER) && (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || __has_include(<cups/ppd.h>))
