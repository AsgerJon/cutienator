//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/qprintengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/qprintengine.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QPrintEngine that Python can take functions over in. Every QPrintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPrintEngineCall0)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QVariant * (*CuteQPrintEngineCall1)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPrintEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPrintEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPrintEngineCall4)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPrintEngineCall5)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
class CuteQPrintEngine : public QPrintEngine {
public:
  using QPrintEngine::QPrintEngine;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8QVariant")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPrintEngine7newPageEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPrintEngine5abortEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine12printerStateEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  void QPrintEngine::setProperty(PrintEnginePropertyKey key, const
  //      QVariant &value)
  void setProperty(
      QPrintEngine::PrintEnginePropertyKey key,
      const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPrintEngineCall0 call = reinterpret_cast<CuteQPrintEngineCall0>(taken[0]);
      call(this, static_cast<int>(key), &value, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QVariant QPrintEngine::property(PrintEnginePropertyKey key) const
  QVariant property(
      QPrintEngine::PrintEnginePropertyKey key) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPrintEngineCall1 call = reinterpret_cast<CuteQPrintEngineCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPrintEngine::newPage()
  bool newPage() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPrintEngineCall2 call = reinterpret_cast<CuteQPrintEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPrintEngine::abort()
  bool abort() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPrintEngineCall3 call = reinterpret_cast<CuteQPrintEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  int QPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPrintEngineCall4 call = reinterpret_cast<CuteQPrintEngineCall4>(taken[4]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrinter::PrinterState QPrintEngine::printerState() const
  QPrinter::PrinterState printerState() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPrintEngineCall5 call = reinterpret_cast<CuteQPrintEngineCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrinter::PrinterState>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)
};

//  QPrintEngine::~QPrintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintEngineD1Ev(QPrintEngine *self) {
  delete self;
}

//  void QPrintEngine::setProperty(PrintEnginePropertyKey key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8QVariant(
    QPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->setProperty(key, *value);
}

//  QVariant QPrintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE(
    const QPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->property(key));
}

//  bool QPrintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPrintEngine7newPageEv(QPrintEngine *self) {
  return self->newPage();
}

//  bool QPrintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPrintEngine5abortEv(QPrintEngine *self) {
  return self->abort();
}

//  int QPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPrintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  QPrinter::PrinterState QPrintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK12QPrintEngine12printerStateEv(
    const QPrintEngine *self) {
  return self->printerState();
}

//  a Python function taken by a CuteQPrintEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPrintEngine(
    QPrintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPrintEngine *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_PRINTER)
