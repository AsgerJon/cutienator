//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprinter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/qprinter.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprinter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/qprinterinfo.h>
#include <QtCore/qvariant.h>

//  QPrinter *QPrinterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPrinter *ritual_ZN15QPrinterPrivate6q_funcEv(QPrinterPrivate *self) {
  return self->q_func();
}

//  const QPrinter *QPrinterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPrinter *ritual_ZNK15QPrinterPrivate6q_funcEv(
    const QPrinterPrivate *self) {
  return self->q_func();
}

//  QPrinterPrivate::QPrinterPrivate(QPrinter *printer)
extern "C" Q_DECL_EXPORT
QPrinterPrivate *ritual_ZN15QPrinterPrivateC1EP8QPrinter(QPrinter *printer) {
  return new QPrinterPrivate(printer);
}

//  QPrinterPrivate::~QPrinterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivateD1Ev(QPrinterPrivate *self) {
  delete self;
}

//  QPrinterPrivate *QPrinterPrivate::get(QPrinter *printer)
extern "C" Q_DECL_EXPORT
QPrinterPrivate *ritual_ZN15QPrinterPrivate3getEP8QPrinter(
    QPrinter *printer) {
  return QPrinterPrivate::get(printer);
}

//  void QPrinterPrivate::init(const QPrinterInfo &printer,
//      QPrinter::PrinterMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivate4initERK12QPrinterInfoN8QPrinter11PrinterModeE(
    QPrinterPrivate *self,
    const QPrinterInfo *printer,
    QPrinter::PrinterMode mode) {
  self->init(*printer, mode);
}

//  QPrinterInfo QPrinterPrivate::findValidPrinter(const QPrinterInfo
//      &printer)
extern "C" Q_DECL_EXPORT
QPrinterInfo *ritual_ZN15QPrinterPrivate16findValidPrinterERK12QPrinterInfo(
    QPrinterPrivate *self,
    const QPrinterInfo *printer) {
  return new QPrinterInfo(self->findValidPrinter(*printer));
}

//  void QPrinterPrivate::initEngines(QPrinter::OutputFormat format, const
//      QPrinterInfo &printer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivate11initEnginesEN8QPrinter12OutputFormatERK12QPrinterInfo(
    QPrinterPrivate *self,
    QPrinter::OutputFormat format,
    const QPrinterInfo *printer) {
  self->initEngines(format, *printer);
}

//  void QPrinterPrivate::changeEngines(QPrinter::OutputFormat format, const
//      QPrinterInfo &printer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivate13changeEnginesEN8QPrinter12OutputFormatERK12QPrinterInfo(
    QPrinterPrivate *self,
    QPrinter::OutputFormat format,
    const QPrinterInfo *printer) {
  self->changeEngines(format, *printer);
}

#if QT_CONFIG(printpreviewwidget)
//  void QPrinterPrivate::setPreviewMode(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivate14setPreviewModeEb(
    QPrinterPrivate *self,
    bool a0) {
  self->setPreviewMode(a0);
}
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
//  bool QPrinterPrivate::previewMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPrinterPrivate11previewModeEv(
    const QPrinterPrivate *self) {
  return self->previewMode();
}
#endif  // QT_CONFIG(printpreviewwidget)

//  void QPrinterPrivate::setProperty(QPrintEngine::PrintEnginePropertyKey
//      key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPrinterPrivate11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QPrinterPrivate *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->setProperty(key, *value);
}

#endif  // !defined(QT_NO_PRINTER)
