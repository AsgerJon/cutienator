//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpdfwriter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_PDF)
#include <QtGui/qpdfwriter.h>
#include <QtCore/qstring.h>
#include <QtCore/quuid.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qpdfoutputintent.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpageranges.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPdfWriter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPdfWriter : QPdfWriter {
  using QPdfWriter::paintEngine;
  using QPdfWriter::metric;
};

//  A QPdfWriter that Python can take functions over in. Every QPdfWriter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PDF)
typedef bool (*CuteQPdfWriterCall0)(const void *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void * (*CuteQPdfWriterCall1)(const void *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef int (*CuteQPdfWriterCall2)(const void *, int, int *);
#endif  // !defined(QT_NO_PDF)
typedef bool (*CuteQPdfWriterCall3)(const void *, const QPageLayout *, int *);
typedef bool (*CuteQPdfWriterCall4)(const void *, const QPageSize *, int *);
typedef bool (*CuteQPdfWriterCall5)(const void *, int, int *);
typedef bool (*CuteQPdfWriterCall6)(const void *, const QMarginsF *, int, int *);
typedef void (*CuteQPdfWriterCall7)(const void *, const QPageRanges *, int *);
typedef int (*CuteQPdfWriterCall8)(const void *, int *);
typedef void (*CuteQPdfWriterCall9)(const void *, QPainter *, int *);
typedef void * (*CuteQPdfWriterCall10)(const void *, QPoint *, int *);
typedef void * (*CuteQPdfWriterCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfWriterCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfWriterCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfWriterCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfWriterCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfWriterCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfWriterCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfWriterCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfWriter : public QPdfWriter {
public:
  using QPdfWriter::QPdfWriter;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice7newPageEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11OrientationE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_PDF)
  //  bool QPdfWriter::newPage()
  bool newPage() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfWriterCall0 call = reinterpret_cast<CuteQPdfWriterCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfWriter::newPage();
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  QPaintEngine *QPdfWriter::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfWriterCall1 call = reinterpret_cast<CuteQPdfWriterCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPdfWriter::paintEngine();
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  int QPdfWriter::metric(PaintDeviceMetric id) const
  int metric(QPaintDevice::PaintDeviceMetric id) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfWriterCall2 call = reinterpret_cast<CuteQPdfWriterCall2>(taken[2]);
      int given = call(this, static_cast<int>(id), &handled);
      if (handled) return given;
    }
    return QPdfWriter::metric(id);
  }
#endif  // !defined(QT_NO_PDF)

  //  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
  bool setPageLayout(const QPageLayout &pageLayout) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfWriterCall3 call = reinterpret_cast<CuteQPdfWriterCall3>(taken[3]);
      bool given = call(this, &pageLayout, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageLayout(pageLayout);
  }

  //  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
  bool setPageSize(const QPageSize &pageSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPdfWriterCall4 call = reinterpret_cast<CuteQPdfWriterCall4>(taken[4]);
      bool given = call(this, &pageSize, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageSize(pageSize);
  }

  //  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
  //      orientation)
  bool setPageOrientation(QPageLayout::Orientation orientation) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPdfWriterCall5 call = reinterpret_cast<CuteQPdfWriterCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQPdfWriterCall6 call = reinterpret_cast<CuteQPdfWriterCall6>(taken[6]);
      bool given = call(this, &margins, static_cast<int>(units), &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageMargins(margins, units);
  }

  //  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
  void setPageRanges(const QPageRanges &ranges) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPdfWriterCall7 call = reinterpret_cast<CuteQPdfWriterCall7>(taken[7]);
      call(this, &ranges, &handled);
      if (handled) return;
    }
    QPagedPaintDevice::setPageRanges(ranges);
  }

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPdfWriterCall8 call = reinterpret_cast<CuteQPdfWriterCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPdfWriterCall9 call = reinterpret_cast<CuteQPdfWriterCall9>(taken[9]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPdfWriterCall10 call = reinterpret_cast<CuteQPdfWriterCall10>(taken[10]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPdfWriterCall11 call = reinterpret_cast<CuteQPdfWriterCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPdfWriterCall12 call = reinterpret_cast<CuteQPdfWriterCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPdfWriterCall13 call = reinterpret_cast<CuteQPdfWriterCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPdfWriterCall14 call = reinterpret_cast<CuteQPdfWriterCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPdfWriterCall15 call = reinterpret_cast<CuteQPdfWriterCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPdfWriterCall16 call = reinterpret_cast<CuteQPdfWriterCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPdfWriterCall17 call = reinterpret_cast<CuteQPdfWriterCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPdfWriterCall18 call = reinterpret_cast<CuteQPdfWriterCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfWriter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QPdfWriter10metaObjectEv(
    const QPdfWriter *self) {
  return self->metaObject();
}

//  void *QPdfWriter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QPdfWriter11qt_metacastEPKc(
    QPdfWriter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfWriter::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QPdfWriter11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfWriter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfWriter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QPdfWriter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPdfWriter::tr(s, c, n));
}

//  QPdfWriter::QPdfWriter(const QString &filename)
extern "C" Q_DECL_EXPORT
QPdfWriter *ritual_ZN10QPdfWriterC1ERK7QString(const QString *filename) {
  return new CuteQPdfWriter(*filename);
}

//  QPdfWriter::QPdfWriter(QIODevice *device)
extern "C" Q_DECL_EXPORT
QPdfWriter *ritual_ZN10QPdfWriterC1EP9QIODevice(QIODevice *device) {
  return new CuteQPdfWriter(device);
}

//  QPdfWriter::~QPdfWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriterD1Ev(QPdfWriter *self) {
  delete self;
}

//  void QPdfWriter::setPdfVersion(PdfVersion version)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter13setPdfVersionEN17QPagedPaintDevice10PdfVersionE(
    QPdfWriter *self,
    QPagedPaintDevice::PdfVersion version) {
  self->setPdfVersion(version);
}

//  PdfVersion QPdfWriter::pdfVersion() const
extern "C" Q_DECL_EXPORT
QPagedPaintDevice::PdfVersion ritual_ZNK10QPdfWriter10pdfVersionEv(
    const QPdfWriter *self) {
  return self->pdfVersion();
}

//  QString QPdfWriter::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QPdfWriter5titleEv(const QPdfWriter *self) {
  return new QString(self->title());
}

//  void QPdfWriter::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter8setTitleERK7QString(
    QPdfWriter *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QPdfWriter::creator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QPdfWriter7creatorEv(const QPdfWriter *self) {
  return new QString(self->creator());
}

//  void QPdfWriter::setCreator(const QString &creator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter10setCreatorERK7QString(
    QPdfWriter *self,
    const QString *creator) {
  self->setCreator(*creator);
}

//  QUuid QPdfWriter::documentId() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QPdfWriter10documentIdEv(const QPdfWriter *self) {
  return new QUuid(self->documentId());
}

//  void QPdfWriter::setDocumentId(QUuid documentId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter13setDocumentIdE5QUuid(
    QPdfWriter *self,
    const QUuid *documentId) {
  self->setDocumentId(*documentId);
}

//  QString QPdfWriter::author() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QPdfWriter6authorEv(const QPdfWriter *self) {
  return new QString(self->author());
}

//  void QPdfWriter::setAuthor(const QString &author)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter9setAuthorERK7QString(
    QPdfWriter *self,
    const QString *author) {
  self->setAuthor(*author);
}

//  bool QPdfWriter::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPdfWriter7newPageEv(QPdfWriter *self) {
  return self->newPage();
}

//  void QPdfWriter::setResolution(int resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter13setResolutionEi(
    QPdfWriter *self,
    int resolution) {
  self->setResolution(resolution);
}

//  int QPdfWriter::resolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QPdfWriter10resolutionEv(const QPdfWriter *self) {
  return self->resolution();
}

//  void QPdfWriter::setDocumentXmpMetadata(const QByteArray &xmpMetadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter22setDocumentXmpMetadataERK10QByteArray(
    QPdfWriter *self,
    const QByteArray *xmpMetadata) {
  self->setDocumentXmpMetadata(*xmpMetadata);
}

//  QByteArray QPdfWriter::documentXmpMetadata() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QPdfWriter19documentXmpMetadataEv(
    const QPdfWriter *self) {
  return new QByteArray(self->documentXmpMetadata());
}

//  void QPdfWriter::addFileAttachment(const QString &fileName, const
//      QByteArray &data, const QString &mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter17addFileAttachmentERK7QStringRK10QByteArrayS2_(
    QPdfWriter *self,
    const QString *fileName,
    const QByteArray *data,
    const QString *mimeType) {
  self->addFileAttachment(*fileName, *data, *mimeType);
}

//  ColorModel QPdfWriter::colorModel() const
extern "C" Q_DECL_EXPORT
QPdfWriter::ColorModel ritual_ZNK10QPdfWriter10colorModelEv(
    const QPdfWriter *self) {
  return self->colorModel();
}

//  void QPdfWriter::setColorModel(ColorModel model)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter13setColorModelENS_10ColorModelE(
    QPdfWriter *self,
    QPdfWriter::ColorModel model) {
  self->setColorModel(model);
}

//  QPdfOutputIntent QPdfWriter::outputIntent() const
extern "C" Q_DECL_EXPORT
QPdfOutputIntent *ritual_ZNK10QPdfWriter12outputIntentEv(
    const QPdfWriter *self) {
  return new QPdfOutputIntent(self->outputIntent());
}

//  void QPdfWriter::setOutputIntent(const QPdfOutputIntent &intent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfWriter15setOutputIntentERK16QPdfOutputIntent(
    QPdfWriter *self,
    const QPdfOutputIntent *intent) {
  self->setOutputIntent(*intent);
}

//  QPaintEngine *QPdfWriter::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK10QPdfWriter11paintEngineEv(const QPdfWriter *self) {
  return self->paintEngine();
}

//  int QPdfWriter::metric(PaintDeviceMetric id) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QPdfWriter6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPdfWriter *self,
    QPaintDevice::PaintDeviceMetric id) {
  return self->metric(id);
}

//  QPdfWriterPrivate *QPdfWriter::d_func()
extern "C" Q_DECL_EXPORT
QPdfWriterPrivate *ritual_ZN10QPdfWriter6d_funcEv(QPdfWriter *self) {
  return self->d_func();
}

//  const QPdfWriterPrivate *QPdfWriter::d_func() const
extern "C" Q_DECL_EXPORT
const QPdfWriterPrivate *ritual_ZNK10QPdfWriter6d_funcEv(
    const QPdfWriter *self) {
  return self->d_func();
}

//  QPdfWriter as the QPagedPaintDevice it is built on
extern "C" Q_DECL_EXPORT
QPagedPaintDevice *ritual_cast_QPdfWriter_QPagedPaintDevice(
    QPdfWriter *self) {
  return static_cast<QPagedPaintDevice *>(self);
}

//  a Python function taken by a CuteQPdfWriter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfWriter(QPdfWriter *self, const char *key, void *call) {
  return static_cast<CuteQPdfWriter *>(self)->take(key, call);
}

//  bool QPdfWriter::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QPdfWriter7newPageEv(QPdfWriter *self) {
  return self->QPdfWriter::newPage();
}

//  QPaintEngine *QPdfWriter::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK10QPdfWriter11paintEngineEv(
    const QPdfWriter *self) {
  return static_cast<const OwnQPdfWriter *>(self)->OwnQPdfWriter::paintEngine();
}

//  int QPdfWriter::metric(PaintDeviceMetric id) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QPdfWriter6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPdfWriter *self,
    QPaintDevice::PaintDeviceMetric id) {
  return static_cast<const OwnQPdfWriter *>(self)->OwnQPdfWriter::metric(id);
}

#endif  // !defined(QT_NO_PDF)
