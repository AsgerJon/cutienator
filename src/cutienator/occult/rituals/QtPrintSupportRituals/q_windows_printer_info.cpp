//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintdevice_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintdevice_p.h>

//  bool QWindowsPrinterInfo::operator==(const QWindowsPrinterInfo &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrinterInfoeqERKS_(
    const QWindowsPrinterInfo *self,
    const QWindowsPrinterInfo *other) {
  return self->operator==(*other);
}

//  QWindowsPrinterInfo::~QWindowsPrinterInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWindowsPrinterInfoD1Ev(QWindowsPrinterInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
