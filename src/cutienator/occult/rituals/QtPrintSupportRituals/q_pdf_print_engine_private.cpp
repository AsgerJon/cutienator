//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_pdf_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: 'qprintengine_pdf_p.h' and all that
//  needs it stand under '__has_include(<cups/ppd.h>)' where Qt's
//  'qprint_p.h', which it includes, includes that header of CUPS
//  (macOS, and Unix where Qt has 'cups'), as a Linux without the
//  headers of CUPS refused the file; elsewhere, as on Windows, they
//  stay as they were. Kept as it is when the generator runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#include <cstring>
#if __has_include(<cups/ppd.h>) \
    || !(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_pdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  A QPdfPrintEnginePrivate that Python can take functions over in. Every QPdfPrintEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPdfPrintEnginePrivateCall0)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPdfPrintEnginePrivateCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
typedef void (*CuteQPdfPrintEnginePrivateCall2)(const void *, int *);
typedef void * (*CuteQPdfPrintEnginePrivateCall3)(const void *, int *);
class CuteQPdfPrintEnginePrivate : public QPdfPrintEnginePrivate {
public:
  using QPdfPrintEnginePrivate::QPdfPrintEnginePrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN22QPdfPrintEnginePrivate15openPrintDeviceEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN22QPdfPrintEnginePrivate16closePrintDeviceEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  bool QPdfPrintEnginePrivate::openPrintDevice()
  bool openPrintDevice() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfPrintEnginePrivateCall0 call = reinterpret_cast<CuteQPdfPrintEnginePrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfPrintEnginePrivate::openPrintDevice();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPdfPrintEnginePrivate::closePrintDevice()
  void closePrintDevice() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfPrintEnginePrivateCall1 call = reinterpret_cast<CuteQPdfPrintEnginePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPdfPrintEnginePrivate::closePrintDevice();
  }
#endif  // !defined(QT_NO_PRINTER)

  //  void QPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfPrintEnginePrivateCall2 call = reinterpret_cast<CuteQPdfPrintEnginePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfPrintEnginePrivateCall3 call = reinterpret_cast<CuteQPdfPrintEnginePrivateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }
};

//  QPdfPrintEngine *QPdfPrintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPdfPrintEngine *ritual_ZN22QPdfPrintEnginePrivate6q_funcEv(
    QPdfPrintEnginePrivate *self) {
  return self->q_func();
}

//  const QPdfPrintEngine *QPdfPrintEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPdfPrintEngine *ritual_ZNK22QPdfPrintEnginePrivate6q_funcEv(
    const QPdfPrintEnginePrivate *self) {
  return self->q_func();
}

//  QPdfPrintEnginePrivate::QPdfPrintEnginePrivate(QPrinter::PrinterMode m)
extern "C" Q_DECL_EXPORT
QPdfPrintEnginePrivate *ritual_ZN22QPdfPrintEnginePrivateC1EN8QPrinter11PrinterModeE(
    QPrinter::PrinterMode m) {
  return new CuteQPdfPrintEnginePrivate(m);
}

//  QPdfPrintEnginePrivate::~QPdfPrintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPdfPrintEnginePrivateD1Ev(QPdfPrintEnginePrivate *self) {
  delete self;
}

//  QPrinter::ColorMode QPdfPrintEnginePrivate::printerColorMode() const
extern "C" Q_DECL_EXPORT
QPrinter::ColorMode ritual_ZNK22QPdfPrintEnginePrivate16printerColorModeEv(
    const QPdfPrintEnginePrivate *self) {
  return self->printerColorMode();
}

//  bool QPdfPrintEnginePrivate::openPrintDevice()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPdfPrintEnginePrivate15openPrintDeviceEv(
    QPdfPrintEnginePrivate *self) {
  return self->openPrintDevice();
}

//  void QPdfPrintEnginePrivate::closePrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPdfPrintEnginePrivate16closePrintDeviceEv(
    QPdfPrintEnginePrivate *self) {
  self->closePrintDevice();
}

//  a Python function taken by a CuteQPdfPrintEnginePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfPrintEnginePrivate(
    QPdfPrintEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfPrintEnginePrivate *>(self)->take(key, call);
}

//  bool QPdfPrintEnginePrivate::openPrintDevice()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QPdfPrintEnginePrivate15openPrintDeviceEv(
    QPdfPrintEnginePrivate *self) {
  return self->QPdfPrintEnginePrivate::openPrintDevice();
}

//  void QPdfPrintEnginePrivate::closePrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPdfPrintEnginePrivate16closePrintDeviceEv(
    QPdfPrintEnginePrivate *self) {
  self->QPdfPrintEnginePrivate::closePrintDevice();
}

#endif  // __has_include(<cups/ppd.h>) || !(defined(Q_OS_MACOS)
        //     || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#endif  // !defined(QT_NO_PRINTER)
