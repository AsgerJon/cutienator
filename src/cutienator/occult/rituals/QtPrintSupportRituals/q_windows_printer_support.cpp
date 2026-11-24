//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintersupport_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_WIN)
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintersupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWindowsPrinterSupport that Python can take functions over in. Every QWindowsPrinterSupport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQWindowsPrinterSupportCall0)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQWindowsPrinterSupportCall1)(const void *, QPrintEngine *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQWindowsPrinterSupportCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
class CuteQWindowsPrinterSupport : public QWindowsPrinterSupport {
public:
  using QWindowsPrinterSupport::QWindowsPrinterSupport;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN23QPlatformPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  QPrintEngine *QWindowsPrinterSupport::createNativePrintEngine(QPrinte
  //      r::PrinterMode printerMode, const QString &deviceId)
  QPrintEngine *createNativePrintEngine(
      QPrinter::PrinterMode printerMode,
      const QString &deviceId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsPrinterSupportCall0 call = reinterpret_cast<CuteQWindowsPrinterSupportCall0>(taken[0]);
      void * given = call(this, static_cast<int>(printerMode), &deviceId, &handled);
      if (handled) return static_cast<QPrintEngine *>(given);
    }
    return QWindowsPrinterSupport::createNativePrintEngine(printerMode, deviceId);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPaintEngine *QWindowsPrinterSupport::createPaintEngine(QPrintEngine
  //      *printEngine, QPrinter::PrinterMode a1)
  QPaintEngine *createPaintEngine(
      QPrintEngine *printEngine,
      QPrinter::PrinterMode a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsPrinterSupportCall1 call = reinterpret_cast<CuteQWindowsPrinterSupportCall1>(taken[1]);
      void * given = call(this, printEngine, static_cast<int>(a1), &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWindowsPrinterSupport::createPaintEngine(printEngine, a1);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QWindowsPrinterSupport::defaultPrintDeviceId() const
  QString defaultPrintDeviceId() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsPrinterSupportCall2 call = reinterpret_cast<CuteQWindowsPrinterSupportCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QWindowsPrinterSupport::defaultPrintDeviceId();
  }
#endif  // !defined(QT_NO_PRINTER)
};

//  QWindowsPrinterSupport::QWindowsPrinterSupport()
extern "C" Q_DECL_EXPORT
QWindowsPrinterSupport *ritual_ZN22QWindowsPrinterSupportC1Ev() {
  return new CuteQWindowsPrinterSupport();
}

//  QWindowsPrinterSupport::~QWindowsPrinterSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowsPrinterSupportD1Ev(QWindowsPrinterSupport *self) {
  delete self;
}

//  QPrintEngine
//      *QWindowsPrinterSupport::createNativePrintEngine(QPrinter::PrinterMod
//      e printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_ZN22QWindowsPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QWindowsPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->createNativePrintEngine(printerMode, *deviceId);
}

//  QPaintEngine *QWindowsPrinterSupport::createPaintEngine(QPrintEngine
//      *printEngine, QPrinter::PrinterMode a1)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN22QWindowsPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QWindowsPrinterSupport *self,
    QPrintEngine *printEngine,
    QPrinter::PrinterMode a1) {
  return self->createPaintEngine(printEngine, a1);
}

//  QStringList QWindowsPrinterSupport::availablePrintDeviceIds() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QWindowsPrinterSupport23availablePrintDeviceIdsEv(
    const QWindowsPrinterSupport *self) {
  return new QList<QString>(self->availablePrintDeviceIds());
}

//  QString QWindowsPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWindowsPrinterSupport20defaultPrintDeviceIdEv(
    const QWindowsPrinterSupport *self) {
  return new QString(self->defaultPrintDeviceId());
}

//  a Python function taken by a CuteQWindowsPrinterSupport, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsPrinterSupport(
    QWindowsPrinterSupport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsPrinterSupport *>(self)->take(key, call);
}

//  QPrintEngine
//      *QWindowsPrinterSupport::createNativePrintEngine(QPrinter::PrinterMod
//      e printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_own_ZN22QWindowsPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QWindowsPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->QWindowsPrinterSupport::createNativePrintEngine(
      printerMode,
      *deviceId);
}

//  QPaintEngine *QWindowsPrinterSupport::createPaintEngine(QPrintEngine
//      *printEngine, QPrinter::PrinterMode a1)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZN22QWindowsPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QWindowsPrinterSupport *self,
    QPrintEngine *printEngine,
    QPrinter::PrinterMode a1) {
  return self->QWindowsPrinterSupport::createPaintEngine(printEngine, a1);
}

//  QString QWindowsPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QWindowsPrinterSupport20defaultPrintDeviceIdEv(
    const QWindowsPrinterSupport *self) {
  return new QString(self->QWindowsPrinterSupport::defaultPrintDeviceId());
}

#endif  // !defined(QT_NO_PRINTER)
#endif  // defined(Q_OS_WIN)
