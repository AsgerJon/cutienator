//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qcups_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<cups/ppd.h>)' too, as 'qcups_p.h' includes that
//  header of CUPS through 'qprint_p.h' and a Linux without the
//  headers of CUPS refused the file. Kept as it is when the generator
//  runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(cups) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN) \
    && __has_include(<cups/ppd.h>)
#if QT_CONFIG(cups)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qcups_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCUPSSupport::JobSheets::JobSheets(BannerPage s, BannerPage e)
extern "C" Q_DECL_EXPORT
QCUPSSupport::JobSheets *ritual_ZN12QCUPSSupport9JobSheetsC1ENS_10BannerPageES1_(
    QCUPSSupport::BannerPage s,
    QCUPSSupport::BannerPage e) {
  return new QCUPSSupport::JobSheets(s, e);
}

//  QCUPSSupport::JobSheets::~JobSheets()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport9JobSheetsD1Ev(QCUPSSupport::JobSheets *self) {
  delete self;
}

#endif  // QT_CONFIG(cups)
#endif  // QT_CONFIG(cups) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
        //     && __has_include(<cups/ppd.h>)
