//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintersupport.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintersupport.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformPrinterSupport that Python can take functions over in. Every QPlatformPrinterSupport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQPlatformPrinterSupportCall0)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQPlatformPrinterSupportCall1)(const void *, QPrintEngine *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQPlatformPrinterSupportCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
class CuteQPlatformPrinterSupport : public QPlatformPrinterSupport {
public:
  using QPlatformPrinterSupport::QPlatformPrinterSupport;
  CuteQPlatformPrinterSupport(const QPlatformPrinterSupport &other) : QPlatformPrinterSupport(other) {}
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
  //  QPrintEngine *QPlatformPrinterSupport::createNativePrintEngine(QPrint
  //      er::PrinterMode printerMode, const QString &deviceId)
  QPrintEngine *createNativePrintEngine(
      QPrinter::PrinterMode printerMode,
      const QString &deviceId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformPrinterSupportCall0 call = reinterpret_cast<CuteQPlatformPrinterSupportCall0>(taken[0]);
      void * given = call(this, static_cast<int>(printerMode), &deviceId, &handled);
      if (handled) return static_cast<QPrintEngine *>(given);
    }
    return QPlatformPrinterSupport::createNativePrintEngine(printerMode, deviceId);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPaintEngine *QPlatformPrinterSupport::createPaintEngine(QPrintEngine
  //      *a0, QPrinter::PrinterMode printerMode)
  QPaintEngine *createPaintEngine(
      QPrintEngine *a0,
      QPrinter::PrinterMode printerMode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformPrinterSupportCall1 call = reinterpret_cast<CuteQPlatformPrinterSupportCall1>(taken[1]);
      void * given = call(this, a0, static_cast<int>(printerMode), &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPlatformPrinterSupport::createPaintEngine(a0, printerMode);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QPlatformPrinterSupport::defaultPrintDeviceId() const
  QString defaultPrintDeviceId() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformPrinterSupportCall2 call = reinterpret_cast<CuteQPlatformPrinterSupportCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformPrinterSupport::defaultPrintDeviceId();
  }
#endif  // !defined(QT_NO_PRINTER)
};

//  QPlatformPrinterSupport::QPlatformPrinterSupport()
extern "C" Q_DECL_EXPORT
QPlatformPrinterSupport *ritual_ZN23QPlatformPrinterSupportC1Ev() {
  return new CuteQPlatformPrinterSupport();
}

//  QPlatformPrinterSupport::~QPlatformPrinterSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformPrinterSupportD1Ev(QPlatformPrinterSupport *self) {
  delete self;
}

//  QPrintEngine
//      *QPlatformPrinterSupport::createNativePrintEngine(QPrinter::PrinterMo
//      de printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_ZN23QPlatformPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QPlatformPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->createNativePrintEngine(printerMode, *deviceId);
}

//  QPaintEngine *QPlatformPrinterSupport::createPaintEngine(QPrintEngine
//      *a0, QPrinter::PrinterMode printerMode)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QPlatformPrinterSupport *self,
    QPrintEngine *a0,
    QPrinter::PrinterMode printerMode) {
  return self->createPaintEngine(a0, printerMode);
}

//  QStringList QPlatformPrinterSupport::availablePrintDeviceIds() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QPlatformPrinterSupport23availablePrintDeviceIdsEv(
    const QPlatformPrinterSupport *self) {
  return new QList<QString>(self->availablePrintDeviceIds());
}

//  QString QPlatformPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv(
    const QPlatformPrinterSupport *self) {
  return new QString(self->defaultPrintDeviceId());
}

//  QPageSize QPlatformPrinterSupport::createPageSize(const QString &id,
//      QSize size, const QString &localizedName)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN23QPlatformPrinterSupport14createPageSizeERK7QString5QSizeS2_(
    const QString *id,
    const QSize *size,
    const QString *localizedName) {
  return new QPageSize(
      QPlatformPrinterSupport::createPageSize(
          *id,
          *size,
          *localizedName));
}

//  a Python function taken by a CuteQPlatformPrinterSupport, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformPrinterSupport(
    QPlatformPrinterSupport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformPrinterSupport *>(self)->take(key, call);
}

//  QPrintEngine
//      *QPlatformPrinterSupport::createNativePrintEngine(QPrinter::PrinterMo
//      de printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_own_ZN23QPlatformPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QPlatformPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->QPlatformPrinterSupport::createNativePrintEngine(
      printerMode,
      *deviceId);
}

//  QPaintEngine *QPlatformPrinterSupport::createPaintEngine(QPrintEngine
//      *a0, QPrinter::PrinterMode printerMode)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QPlatformPrinterSupport *self,
    QPrintEngine *a0,
    QPrinter::PrinterMode printerMode) {
  return self->QPlatformPrinterSupport::createPaintEngine(a0, printerMode);
}

//  QString QPlatformPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv(
    const QPlatformPrinterSupport *self) {
  return new QString(self->QPlatformPrinterSupport::defaultPrintDeviceId());
}

#endif  // !defined(QT_NO_PRINTER)
