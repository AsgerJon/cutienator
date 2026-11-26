//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qcocoaprintersupport_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_MACOS)
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qcocoaprintersupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QString>

//  A QCocoaPrinterSupport that Python can take functions over in. Every QCocoaPrinterSupport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQCocoaPrinterSupportCall0)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQCocoaPrinterSupportCall1)(const void *, QPrintEngine *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQCocoaPrinterSupportCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
class CuteQCocoaPrinterSupport : public QCocoaPrinterSupport {
public:
  using QCocoaPrinterSupport::QCocoaPrinterSupport;
  CuteQCocoaPrinterSupport(const QCocoaPrinterSupport & other) : QCocoaPrinterSupport(other) {}
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
  //  QPrintEngine
  //      *QCocoaPrinterSupport::createNativePrintEngine(QPrinter::PrinterM
  //      ode printerMode, const QString &deviceId)
  QPrintEngine *createNativePrintEngine(
      QPrinter::PrinterMode printerMode,
      const QString &deviceId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCocoaPrinterSupportCall0 call = reinterpret_cast<CuteQCocoaPrinterSupportCall0>(taken[0]);
      void * given = call(this, static_cast<int>(printerMode), &deviceId, &handled);
      if (handled) return static_cast<QPrintEngine *>(given);
    }
    return QCocoaPrinterSupport::createNativePrintEngine(printerMode, deviceId);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPaintEngine *QCocoaPrinterSupport::createPaintEngine(QPrintEngine
  //      *a0, QPrinter::PrinterMode printerMode)
  QPaintEngine *createPaintEngine(
      QPrintEngine *a0,
      QPrinter::PrinterMode printerMode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCocoaPrinterSupportCall1 call = reinterpret_cast<CuteQCocoaPrinterSupportCall1>(taken[1]);
      void * given = call(this, a0, static_cast<int>(printerMode), &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QCocoaPrinterSupport::createPaintEngine(a0, printerMode);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QCocoaPrinterSupport::defaultPrintDeviceId() const
  QString defaultPrintDeviceId() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCocoaPrinterSupportCall2 call = reinterpret_cast<CuteQCocoaPrinterSupportCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCocoaPrinterSupport::defaultPrintDeviceId();
  }
#endif  // !defined(QT_NO_PRINTER)
};

//  QCocoaPrinterSupport::QCocoaPrinterSupport()
extern "C" Q_DECL_EXPORT
QCocoaPrinterSupport *ritual_ZN20QCocoaPrinterSupportC1Ev() {
  return new CuteQCocoaPrinterSupport();
}

//  QCocoaPrinterSupport::~QCocoaPrinterSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCocoaPrinterSupportD1Ev(QCocoaPrinterSupport *self) {
  delete self;
}

//  QPrintEngine
//      *QCocoaPrinterSupport::createNativePrintEngine(QPrinter::PrinterMode
//      printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_ZN20QCocoaPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QCocoaPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->createNativePrintEngine(printerMode, *deviceId);
}

//  QPaintEngine *QCocoaPrinterSupport::createPaintEngine(QPrintEngine *a0,
//      QPrinter::PrinterMode printerMode)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN20QCocoaPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QCocoaPrinterSupport *self,
    QPrintEngine *a0,
    QPrinter::PrinterMode printerMode) {
  return self->createPaintEngine(a0, printerMode);
}

//  QPrintDevice QCocoaPrinterSupport::createPrintDevice(const QString &id)
extern "C" Q_DECL_EXPORT
QPrintDevice *ritual_ZN20QCocoaPrinterSupport17createPrintDeviceERK7QString(
    QCocoaPrinterSupport *self,
    const QString *id) {
  return new QPrintDevice(self->createPrintDevice(*id));
}

//  QStringList QCocoaPrinterSupport::availablePrintDeviceIds() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QCocoaPrinterSupport23availablePrintDeviceIdsEv(
    const QCocoaPrinterSupport *self) {
  return new QList<QString>(self->availablePrintDeviceIds());
}

//  QString QCocoaPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QCocoaPrinterSupport20defaultPrintDeviceIdEv(
    const QCocoaPrinterSupport *self) {
  return new QString(self->defaultPrintDeviceId());
}

//  a Python function taken by a CuteQCocoaPrinterSupport, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCocoaPrinterSupport(
    QCocoaPrinterSupport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCocoaPrinterSupport *>(self)->take(key, call);
}

//  QPrintEngine
//      *QCocoaPrinterSupport::createNativePrintEngine(QPrinter::PrinterMode
//      printerMode, const QString &deviceId)
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_own_ZN20QCocoaPrinterSupport23createNativePrintEngineEN8QPrinter11PrinterModeERK7QString(
    QCocoaPrinterSupport *self,
    QPrinter::PrinterMode printerMode,
    const QString *deviceId) {
  return self->QCocoaPrinterSupport::createNativePrintEngine(
      printerMode,
      *deviceId);
}

//  QPaintEngine *QCocoaPrinterSupport::createPaintEngine(QPrintEngine *a0,
//      QPrinter::PrinterMode printerMode)
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZN20QCocoaPrinterSupport17createPaintEngineEP12QPrintEngineN8QPrinter11PrinterModeE(
    QCocoaPrinterSupport *self,
    QPrintEngine *a0,
    QPrinter::PrinterMode printerMode) {
  return self->QCocoaPrinterSupport::createPaintEngine(a0, printerMode);
}

//  QString QCocoaPrinterSupport::defaultPrintDeviceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QCocoaPrinterSupport20defaultPrintDeviceIdEv(
    const QCocoaPrinterSupport *self) {
  return new QString(self->QCocoaPrinterSupport::defaultPrintDeviceId());
}

//  a QPrintDevice a ritual of QCocoaPrinterSupport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCocoaPrinterSupport__QPrintDevice(QPrintDevice *self) {
  delete self;
}

#endif  // !defined(QT_NO_PRINTER)
#endif  // defined(Q_OS_MACOS)
