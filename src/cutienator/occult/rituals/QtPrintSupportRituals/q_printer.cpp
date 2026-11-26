//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/qprinter.h, Qt 6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/qprinter.h>
#include <QtPrintSupport/qprinterinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpageranges.h>
#include <cstring>
#include <QtCore/QList>

//  Only a class built on QPrinter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPrinter : QPrinter {
  using QPrinter::metric;
};

//  A QPrinter that Python can take functions over in. Every QPrinter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPrinterCall0)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPrinterCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQPrinterCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPrinterCall3)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
typedef bool (*CuteQPrinterCall4)(const void *, const QPageLayout *, int *);
typedef bool (*CuteQPrinterCall5)(const void *, const QPageSize *, int *);
typedef bool (*CuteQPrinterCall6)(const void *, int, int *);
typedef bool (*CuteQPrinterCall7)(const void *, const QMarginsF *, int, int *);
typedef void (*CuteQPrinterCall8)(const void *, const QPageRanges *, int *);
typedef void (*CuteQPrinterCall9)(const void *, QPainter *, int *);
typedef void * (*CuteQPrinterCall10)(const void *, QPoint *, int *);
typedef void * (*CuteQPrinterCall11)(const void *, int *);
class CuteQPrinter : public QPrinter {
public:
  using QPrinter::QPrinter;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice7newPageEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11OrientationE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  int QPrinter::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPrinterCall0 call = reinterpret_cast<CuteQPrinterCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPrinter::devType();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPrinter::newPage()
  bool newPage() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPrinterCall1 call = reinterpret_cast<CuteQPrinterCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPrinter::newPage();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPaintEngine *QPrinter::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPrinterCall2 call = reinterpret_cast<CuteQPrinterCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPrinter::paintEngine();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  int QPrinter::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPrinterCall3 call = reinterpret_cast<CuteQPrinterCall3>(taken[3]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPrinter::metric(a0);
  }
#endif  // !defined(QT_NO_PRINTER)

  //  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
  bool setPageLayout(const QPageLayout &pageLayout) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPrinterCall4 call = reinterpret_cast<CuteQPrinterCall4>(taken[4]);
      bool given = call(this, &pageLayout, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageLayout(pageLayout);
  }

  //  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
  bool setPageSize(const QPageSize &pageSize) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPrinterCall5 call = reinterpret_cast<CuteQPrinterCall5>(taken[5]);
      bool given = call(this, &pageSize, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageSize(pageSize);
  }

  //  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
  //      orientation)
  bool setPageOrientation(QPageLayout::Orientation orientation) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPrinterCall6 call = reinterpret_cast<CuteQPrinterCall6>(taken[6]);
      bool given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageOrientation(orientation);
  }

  //  bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
  //      QPageLayout::Unit units)
  bool setPageMargins(
      const QMarginsF &margins,
      QPageLayout::Unit units) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPrinterCall7 call = reinterpret_cast<CuteQPrinterCall7>(taken[7]);
      bool given = call(this, &margins, static_cast<int>(units), &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageMargins(margins, units);
  }

  //  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
  void setPageRanges(const QPageRanges &ranges) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPrinterCall8 call = reinterpret_cast<CuteQPrinterCall8>(taken[8]);
      call(this, &ranges, &handled);
      if (handled) return;
    }
    QPagedPaintDevice::setPageRanges(ranges);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPrinterCall9 call = reinterpret_cast<CuteQPrinterCall9>(taken[9]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPrinterCall10 call = reinterpret_cast<CuteQPrinterCall10>(taken[10]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPrinterCall11 call = reinterpret_cast<CuteQPrinterCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QPrinterPrivate *QPrinter::d_func()
extern "C" Q_DECL_EXPORT
QPrinterPrivate *ritual_ZN8QPrinter6d_funcEv(QPrinter *self) {
  return self->d_func();
}

//  const QPrinterPrivate *QPrinter::d_func() const
extern "C" Q_DECL_EXPORT
const QPrinterPrivate *ritual_ZNK8QPrinter6d_funcEv(const QPrinter *self) {
  return self->d_func();
}

//  QPrinter::QPrinter(PrinterMode mode)
extern "C" Q_DECL_EXPORT
QPrinter *ritual_ZN8QPrinterC1ENS_11PrinterModeE(
    QPrinter::PrinterMode mode) {
  return new CuteQPrinter(mode);
}

//  QPrinter::QPrinter(const QPrinterInfo &printer, PrinterMode mode)
extern "C" Q_DECL_EXPORT
QPrinter *ritual_ZN8QPrinterC1ERK12QPrinterInfoNS_11PrinterModeE(
    const QPrinterInfo *printer,
    QPrinter::PrinterMode mode) {
  return new CuteQPrinter(*printer, mode);
}

//  QPrinter::~QPrinter()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinterD1Ev(QPrinter *self) {
  delete self;
}

//  int QPrinter::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter7devTypeEv(const QPrinter *self) {
  return self->devType();
}

//  void QPrinter::setOutputFormat(OutputFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter15setOutputFormatENS_12OutputFormatE(
    QPrinter *self,
    QPrinter::OutputFormat format) {
  self->setOutputFormat(format);
}

//  OutputFormat QPrinter::outputFormat() const
extern "C" Q_DECL_EXPORT
QPrinter::OutputFormat ritual_ZNK8QPrinter12outputFormatEv(
    const QPrinter *self) {
  return self->outputFormat();
}

//  void QPrinter::setPdfVersion(PdfVersion version)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter13setPdfVersionEN17QPagedPaintDevice10PdfVersionE(
    QPrinter *self,
    QPagedPaintDevice::PdfVersion version) {
  self->setPdfVersion(version);
}

//  PdfVersion QPrinter::pdfVersion() const
extern "C" Q_DECL_EXPORT
QPagedPaintDevice::PdfVersion ritual_ZNK8QPrinter10pdfVersionEv(
    const QPrinter *self) {
  return self->pdfVersion();
}

//  void QPrinter::setPrinterName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter14setPrinterNameERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setPrinterName(*a0);
}

//  QString QPrinter::printerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter11printerNameEv(const QPrinter *self) {
  return new QString(self->printerName());
}

//  bool QPrinter::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPrinter7isValidEv(const QPrinter *self) {
  return self->isValid();
}

//  void QPrinter::setOutputFileName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter17setOutputFileNameERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setOutputFileName(*a0);
}

//  QString QPrinter::outputFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter14outputFileNameEv(const QPrinter *self) {
  return new QString(self->outputFileName());
}

//  void QPrinter::setPrintProgram(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter15setPrintProgramERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setPrintProgram(*a0);
}

//  QString QPrinter::printProgram() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter12printProgramEv(const QPrinter *self) {
  return new QString(self->printProgram());
}

//  void QPrinter::setDocName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter10setDocNameERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setDocName(*a0);
}

//  QString QPrinter::docName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter7docNameEv(const QPrinter *self) {
  return new QString(self->docName());
}

//  void QPrinter::setCreator(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter10setCreatorERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setCreator(*a0);
}

//  QString QPrinter::creator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter7creatorEv(const QPrinter *self) {
  return new QString(self->creator());
}

//  void QPrinter::setPageOrder(PageOrder a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter12setPageOrderENS_9PageOrderE(
    QPrinter *self,
    QPrinter::PageOrder a0) {
  self->setPageOrder(a0);
}

//  PageOrder QPrinter::pageOrder() const
extern "C" Q_DECL_EXPORT
QPrinter::PageOrder ritual_ZNK8QPrinter9pageOrderEv(const QPrinter *self) {
  return self->pageOrder();
}

//  void QPrinter::setResolution(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter13setResolutionEi(QPrinter *self, int a0) {
  self->setResolution(a0);
}

//  int QPrinter::resolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter10resolutionEv(const QPrinter *self) {
  return self->resolution();
}

//  void QPrinter::setColorMode(ColorMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter12setColorModeENS_9ColorModeE(
    QPrinter *self,
    QPrinter::ColorMode a0) {
  self->setColorMode(a0);
}

//  ColorMode QPrinter::colorMode() const
extern "C" Q_DECL_EXPORT
QPrinter::ColorMode ritual_ZNK8QPrinter9colorModeEv(const QPrinter *self) {
  return self->colorMode();
}

//  void QPrinter::setCollateCopies(bool collate)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter16setCollateCopiesEb(QPrinter *self, bool collate) {
  self->setCollateCopies(collate);
}

//  bool QPrinter::collateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPrinter13collateCopiesEv(const QPrinter *self) {
  return self->collateCopies();
}

//  void QPrinter::setFullPage(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter11setFullPageEb(QPrinter *self, bool a0) {
  self->setFullPage(a0);
}

//  bool QPrinter::fullPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPrinter8fullPageEv(const QPrinter *self) {
  return self->fullPage();
}

//  void QPrinter::setCopyCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter12setCopyCountEi(QPrinter *self, int a0) {
  self->setCopyCount(a0);
}

//  int QPrinter::copyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter9copyCountEv(const QPrinter *self) {
  return self->copyCount();
}

//  bool QPrinter::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPrinter22supportsMultipleCopiesEv(const QPrinter *self) {
  return self->supportsMultipleCopies();
}

//  void QPrinter::setPaperSource(PaperSource a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter14setPaperSourceENS_11PaperSourceE(
    QPrinter *self,
    QPrinter::PaperSource a0) {
  self->setPaperSource(a0);
}

//  PaperSource QPrinter::paperSource() const
extern "C" Q_DECL_EXPORT
QPrinter::PaperSource ritual_ZNK8QPrinter11paperSourceEv(
    const QPrinter *self) {
  return self->paperSource();
}

//  void QPrinter::setDuplex(DuplexMode duplex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter9setDuplexENS_10DuplexModeE(
    QPrinter *self,
    QPrinter::DuplexMode duplex) {
  self->setDuplex(duplex);
}

//  DuplexMode QPrinter::duplex() const
extern "C" Q_DECL_EXPORT
QPrinter::DuplexMode ritual_ZNK8QPrinter6duplexEv(const QPrinter *self) {
  return self->duplex();
}

//  QList<int> QPrinter::supportedResolutions() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK8QPrinter20supportedResolutionsEv(
    const QPrinter *self) {
  return new QList<int>(self->supportedResolutions());
}

//  void QPrinter::setFontEmbeddingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter23setFontEmbeddingEnabledEb(
    QPrinter *self,
    bool enable) {
  self->setFontEmbeddingEnabled(enable);
}

//  bool QPrinter::fontEmbeddingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPrinter20fontEmbeddingEnabledEv(const QPrinter *self) {
  return self->fontEmbeddingEnabled();
}

//  QRectF QPrinter::paperRect(Unit a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QPrinter9paperRectENS_4UnitE(
    const QPrinter *self,
    QPrinter::Unit a0) {
  return new QRectF(self->paperRect(a0));
}

//  QRectF QPrinter::pageRect(Unit a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QPrinter8pageRectENS_4UnitE(
    const QPrinter *self,
    QPrinter::Unit a0) {
  return new QRectF(self->pageRect(a0));
}

//  QString QPrinter::printerSelectionOption() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPrinter22printerSelectionOptionEv(
    const QPrinter *self) {
  return new QString(self->printerSelectionOption());
}

//  void QPrinter::setPrinterSelectionOption(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter25setPrinterSelectionOptionERK7QString(
    QPrinter *self,
    const QString *a0) {
  self->setPrinterSelectionOption(*a0);
}

//  bool QPrinter::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPrinter7newPageEv(QPrinter *self) {
  return self->newPage();
}

//  bool QPrinter::abort()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPrinter5abortEv(QPrinter *self) {
  return self->abort();
}

//  PrinterState QPrinter::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK8QPrinter12printerStateEv(
    const QPrinter *self) {
  return self->printerState();
}

//  QPaintEngine *QPrinter::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK8QPrinter11paintEngineEv(const QPrinter *self) {
  return self->paintEngine();
}

//  QPrintEngine *QPrinter::printEngine() const
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_ZNK8QPrinter11printEngineEv(const QPrinter *self) {
  return self->printEngine();
}

//  void QPrinter::setFromTo(int fromPage, int toPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter9setFromToEii(
    QPrinter *self,
    int fromPage,
    int toPage) {
  self->setFromTo(fromPage, toPage);
}

//  int QPrinter::fromPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter8fromPageEv(const QPrinter *self) {
  return self->fromPage();
}

//  int QPrinter::toPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter6toPageEv(const QPrinter *self) {
  return self->toPage();
}

//  void QPrinter::setPrintRange(PrintRange range)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter13setPrintRangeENS_10PrintRangeE(
    QPrinter *self,
    QPrinter::PrintRange range) {
  self->setPrintRange(range);
}

//  PrintRange QPrinter::printRange() const
extern "C" Q_DECL_EXPORT
QPrinter::PrintRange ritual_ZNK8QPrinter10printRangeEv(
    const QPrinter *self) {
  return self->printRange();
}

//  int QPrinter::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPrinter6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPrinter *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  void QPrinter::setEngines(QPrintEngine *printEngine, QPaintEngine
//      *paintEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPrinter10setEnginesEP12QPrintEngineP12QPaintEngine(
    QPrinter *self,
    QPrintEngine *printEngine,
    QPaintEngine *paintEngine) {
  self->setEngines(printEngine, paintEngine);
}

//  a Python function taken by a CuteQPrinter, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPrinter(QPrinter *self, const char *key, void *call) {
  return static_cast<CuteQPrinter *>(self)->take(key, call);
}

//  int QPrinter::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QPrinter7devTypeEv(const QPrinter *self) {
  return self->QPrinter::devType();
}

//  bool QPrinter::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QPrinter7newPageEv(QPrinter *self) {
  return self->QPrinter::newPage();
}

//  QPaintEngine *QPrinter::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK8QPrinter11paintEngineEv(const QPrinter *self) {
  return self->QPrinter::paintEngine();
}

//  int QPrinter::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QPrinter6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPrinter *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return static_cast<const OwnQPrinter *>(self)->OwnQPrinter::metric(a0);
}

//  a QList<int> a ritual of QPrinter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPrinter__QList_int(QList<int> *self) {
  delete self;
}

#endif  // !defined(QT_NO_PRINTER)
