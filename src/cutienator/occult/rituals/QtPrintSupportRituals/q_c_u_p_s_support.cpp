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
#include <QtCore/qstring.h>

//  void QCUPSSupport::setCupsOption(QPrinter *printer, const QString
//      &option, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport13setCupsOptionEP8QPrinterRK7QStringS4_(
    QPrinter *printer,
    const QString *option,
    const QString *value) {
  QCUPSSupport::setCupsOption(printer, *option, *value);
}

//  void QCUPSSupport::clearCupsOption(QPrinter *printer, const QString
//      &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport15clearCupsOptionEP8QPrinterRK7QString(
    QPrinter *printer,
    const QString *option) {
  QCUPSSupport::clearCupsOption(printer, *option);
}

//  void QCUPSSupport::clearCupsOptions(QPrinter *printer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport16clearCupsOptionsEP8QPrinter(
    QPrinter *printer) {
  QCUPSSupport::clearCupsOptions(printer);
}

//  void QCUPSSupport::setJobBilling(QPrinter *printer, const QString
//      &jobBilling)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport13setJobBillingEP8QPrinterRK7QString(
    QPrinter *printer,
    const QString *jobBilling) {
  QCUPSSupport::setJobBilling(printer, *jobBilling);
}

//  void QCUPSSupport::setJobPriority(QPrinter *printer, int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport14setJobPriorityEP8QPrinteri(
    QPrinter *printer,
    int priority) {
  QCUPSSupport::setJobPriority(printer, priority);
}

//  void QCUPSSupport::setPageRange(QPrinter *printer, int pageFrom, int
//      pageTo)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport12setPageRangeEP8QPrinterii(
    QPrinter *printer,
    int pageFrom,
    int pageTo) {
  QCUPSSupport::setPageRange(printer, pageFrom, pageTo);
}

//  void QCUPSSupport::setPageRange(QPrinter *printer, const QString
//      &pageRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupport12setPageRangeEP8QPrinterRK7QString(
    QPrinter *printer,
    const QString *pageRange) {
  QCUPSSupport::setPageRange(printer, *pageRange);
}

//  JobSheets QCUPSSupport::parseJobSheets(const QString &jobSheets)
extern "C" Q_DECL_EXPORT
QCUPSSupport::JobSheets *ritual_ZN12QCUPSSupport14parseJobSheetsERK7QString(
    const QString *jobSheets) {
  return new QCUPSSupport::JobSheets(
      QCUPSSupport::parseJobSheets(
          *jobSheets));
}

//  JobHoldUntilWithTime QCUPSSupport::parseJobHoldUntil(const QString
//      &jobHoldUntil)
extern "C" Q_DECL_EXPORT
QCUPSSupport::JobHoldUntilWithTime *ritual_ZN12QCUPSSupport17parseJobHoldUntilERK7QString(
    const QString *jobHoldUntil) {
  return new QCUPSSupport::JobHoldUntilWithTime(
      QCUPSSupport::parseJobHoldUntil(
          *jobHoldUntil));
}

//  QCUPSSupport::~QCUPSSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCUPSSupportD1Ev(QCUPSSupport *self) {
  delete self;
}

#endif  // QT_CONFIG(cups)
#endif  // QT_CONFIG(cups) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
        //     && __has_include(<cups/ppd.h>)
