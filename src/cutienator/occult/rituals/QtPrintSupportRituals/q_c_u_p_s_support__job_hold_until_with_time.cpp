//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qcups_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the '#if' the whole file stands under
//  now also asks '__has_include(<cups/ppd.h>)', the header of CUPS
//  that Qt's 'qcups_p.h' pulls in through 'qprint_p.h', since a machine
//  without the headers of CUPS, as GitHub's Linux, refused the file.
//  Kept as it is when the generator runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(cups) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN) && \
    __has_include(<cups/ppd.h>)
#if QT_CONFIG(cups)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qcups_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>

//  QCUPSSupport::JobHoldUntilWithTime::JobHoldUntilWithTime(JobHoldUntil jh,
//      QTime t)
extern "C" Q_DECL_EXPORT
QCUPSSupport::JobHoldUntilWithTime *ritual_ZN12QCUPSSupport20JobHoldUntilWithTimeC1ENS_12JobHoldUntilE5QTime(
    QCUPSSupport::JobHoldUntil jh,
    const QTime *t) {
  return new QCUPSSupport::JobHoldUntilWithTime(jh, *t);
}

//  QCUPSSupport::JobHoldUntilWithTime::~JobHoldUntilWithTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport20JobHoldUntilWithTimeD1Ev(
    QCUPSSupport::JobHoldUntilWithTime *self) {
  delete self;
}

#endif  // QT_CONFIG(cups)
#endif  // QT_CONFIG(cups) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN) && __has_include(<cups/ppd.h>)
