//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand: 'ritual_ZN17QPdfEnginePrivate7xprintfEPKcz'.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PDF)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <cstring>

//  A QPdfEnginePrivate that Python can take functions over in. Every QPdfEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPdfEnginePrivateCall0)(const void *, int *);
typedef void * (*CuteQPdfEnginePrivateCall1)(const void *, int *);
typedef void * (*CuteQPdfEnginePrivateCall2)(const void *, int *);
class CuteQPdfEnginePrivate : public QPdfEnginePrivate {
public:
  using QPdfEnginePrivate::QPdfEnginePrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate12nativeHandleEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfEnginePrivateCall0 call = reinterpret_cast<CuteQPdfEnginePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfEnginePrivateCall1 call = reinterpret_cast<CuteQPdfEnginePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }

  //  Qt::HANDLE QPaintEnginePrivate::nativeHandle()
  Qt::HANDLE nativeHandle() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfEnginePrivateCall2 call = reinterpret_cast<CuteQPdfEnginePrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return QPaintEnginePrivate::nativeHandle();
  }
};

//  QPdfEngine *QPdfEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPdfEngine *ritual_ZN17QPdfEnginePrivate6q_funcEv(QPdfEnginePrivate *self) {
  return self->q_func();
}

//  const QPdfEngine *QPdfEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPdfEngine *ritual_ZNK17QPdfEnginePrivate6q_funcEv(
    const QPdfEnginePrivate *self) {
  return self->q_func();
}

//  QPdfEnginePrivate::QPdfEnginePrivate()
extern "C" Q_DECL_EXPORT
QPdfEnginePrivate *ritual_ZN17QPdfEnginePrivateC1Ev() {
  return new CuteQPdfEnginePrivate();
}

//  QPdfEnginePrivate::~QPdfEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivateD1Ev(QPdfEnginePrivate *self) {
  delete self;
}

//  uint QPdfEnginePrivate::requestObject()
extern "C" Q_DECL_EXPORT
uint ritual_ZN17QPdfEnginePrivate13requestObjectEv(QPdfEnginePrivate *self) {
  return self->requestObject();
}

//  void QPdfEnginePrivate::writeHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate11writeHeaderEv(QPdfEnginePrivate *self) {
  self->writeHeader();
}

//  void QPdfEnginePrivate::writeTail()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate9writeTailEv(QPdfEnginePrivate *self) {
  self->writeTail();
}

//  int QPdfEnginePrivate::addImage(const QImage &image, bool *bitmap, bool
//      lossless, qint64 serial_no)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate8addImageERK6QImagePbbx(
    QPdfEnginePrivate *self,
    const QImage *image,
    bool *bitmap,
    bool lossless,
    qint64 serial_no) {
  return self->addImage(*image, bitmap, lossless, serial_no);
}

//  int QPdfEnginePrivate::addConstantAlphaObject(int brushAlpha, int
//      penAlpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate22addConstantAlphaObjectEii(
    QPdfEnginePrivate *self,
    int brushAlpha,
    int penAlpha) {
  return self->addConstantAlphaObject(brushAlpha, penAlpha);
}

//  int QPdfEnginePrivate::addBrushPattern(const QTransform &matrix, bool
//      *specifyColor, int *gStateObject)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate15addBrushPatternERK10QTransformPbPi(
    QPdfEnginePrivate *self,
    const QTransform *matrix,
    bool *specifyColor,
    int *gStateObject) {
  return self->addBrushPattern(*matrix, specifyColor, gStateObject);
}

//  void QPdfEnginePrivate::drawTextItem(const QPointF &p, const QTextItemInt
//      &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate12drawTextItemERK7QPointFRK12QTextItemInt(
    QPdfEnginePrivate *self,
    const QPointF *p,
    const QTextItemInt *ti) {
  self->drawTextItem(*p, *ti);
}

//  QTransform QPdfEnginePrivate::pageMatrix() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QPdfEnginePrivate10pageMatrixEv(
    const QPdfEnginePrivate *self) {
  return new QTransform(self->pageMatrix());
}

//  void QPdfEnginePrivate::newPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate7newPageEv(QPdfEnginePrivate *self) {
  self->newPage();
}

//  int QPdfEnginePrivate::gradientBrush(const QBrush &b, const QTransform
//      &matrix, int *gStateObject)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate13gradientBrushERK6QBrushRK10QTransformPi(
    QPdfEnginePrivate *self,
    const QBrush *b,
    const QTransform *matrix,
    int *gStateObject) {
  return self->gradientBrush(*b, *matrix, gStateObject);
}

//  int QPdfEnginePrivate::generateGradientShader(const QGradient *gradient,
//      const QTransform &matrix, bool alpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate22generateGradientShaderEPK9QGradientRK10QTransformb(
    QPdfEnginePrivate *self,
    const QGradient *gradient,
    const QTransform *matrix,
    bool alpha) {
  return self->generateGradientShader(gradient, *matrix, alpha);
}

//  int QPdfEnginePrivate::generateLinearGradientShader(const QLinearGradient
//      *lg, const QTransform &matrix, bool alpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate28generateLinearGradientShaderEPK15QLinearGradientRK10QTransformb(
    QPdfEnginePrivate *self,
    const QLinearGradient *lg,
    const QTransform *matrix,
    bool alpha) {
  return self->generateLinearGradientShader(lg, *matrix, alpha);
}

//  int QPdfEnginePrivate::generateRadialGradientShader(const QRadialGradient
//      *gradient, const QTransform &matrix, bool alpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate28generateRadialGradientShaderEPK15QRadialGradientRK10QTransformb(
    QPdfEnginePrivate *self,
    const QRadialGradient *gradient,
    const QTransform *matrix,
    bool alpha) {
  return self->generateRadialGradientShader(gradient, *matrix, alpha);
}

//  ShadingFunctionResult QPdfEnginePrivate::createShadingFunction(const
//      QGradient *gradient, int from, int to, bool reflect, bool alpha)
extern "C" Q_DECL_EXPORT
QPdfEnginePrivate::ShadingFunctionResult *ritual_ZN17QPdfEnginePrivate21createShadingFunctionEPK9QGradientiibb(
    QPdfEnginePrivate *self,
    const QGradient *gradient,
    int from,
    int to,
    bool reflect,
    bool alpha) {
  return new QPdfEnginePrivate::ShadingFunctionResult(
      self->createShadingFunction(
          gradient,
          from,
          to,
          reflect,
          alpha));
}

//  QPdfEngine::ColorModel QPdfEnginePrivate::colorModelForColor(const QColor
//      &color) const
extern "C" Q_DECL_EXPORT
QPdfEngine::ColorModel ritual_ZNK17QPdfEnginePrivate18colorModelForColorERK6QColor(
    const QPdfEnginePrivate *self,
    const QColor *color) {
  return self->colorModelForColor(*color);
}

//  void QPdfEnginePrivate::writeColor(ColorDomain domain, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate10writeColorENS_11ColorDomainERK6QColor(
    QPdfEnginePrivate *self,
    QPdfEnginePrivate::ColorDomain domain,
    const QColor *color) {
  self->writeColor(domain, *color);
}

//  void QPdfEnginePrivate::writeInfo(const QDateTime &date)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate9writeInfoERK9QDateTime(
    QPdfEnginePrivate *self,
    const QDateTime *date) {
  self->writeInfo(*date);
}

//  int QPdfEnginePrivate::writeXmpDocumentMetaData(const QDateTime &date)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate24writeXmpDocumentMetaDataERK9QDateTime(
    QPdfEnginePrivate *self,
    const QDateTime *date) {
  return self->writeXmpDocumentMetaData(*date);
}

//  int QPdfEnginePrivate::writeOutputIntent()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate17writeOutputIntentEv(
    QPdfEnginePrivate *self) {
  return self->writeOutputIntent();
}

//  void QPdfEnginePrivate::writePageRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate13writePageRootEv(QPdfEnginePrivate *self) {
  self->writePageRoot();
}

//  void QPdfEnginePrivate::writeDestsRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate14writeDestsRootEv(
    QPdfEnginePrivate *self) {
  self->writeDestsRoot();
}

//  void QPdfEnginePrivate::writeAttachmentRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate19writeAttachmentRootEv(
    QPdfEnginePrivate *self) {
  self->writeAttachmentRoot();
}

//  void QPdfEnginePrivate::writeNamesRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate14writeNamesRootEv(
    QPdfEnginePrivate *self) {
  self->writeNamesRoot();
}

//  void QPdfEnginePrivate::writeFonts()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate10writeFontsEv(QPdfEnginePrivate *self) {
  self->writeFonts();
}

//  void QPdfEnginePrivate::embedFont(QFontSubset *font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate9embedFontEP11QFontSubset(
    QPdfEnginePrivate *self,
    QFontSubset *font) {
  self->embedFont(font);
}

//  qreal QPdfEnginePrivate::calcUserUnit() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QPdfEnginePrivate12calcUserUnitEv(
    const QPdfEnginePrivate *self) {
  return self->calcUserUnit();
}

//  int QPdfEnginePrivate::writeImage(const QByteArray &data, int width, int
//      height, WriteImageOption option, int maskObject, int softMaskObject,
//      bool dct, bool isMono)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate10writeImageERK10QByteArrayiiNS_16WriteImageOptionEiibb(
    QPdfEnginePrivate *self,
    const QByteArray *data,
    int width,
    int height,
    QPdfEnginePrivate::WriteImageOption option,
    int maskObject,
    int softMaskObject,
    bool dct,
    bool isMono) {
  return self->writeImage(
      *data,
      width,
      height,
      option,
      maskObject,
      softMaskObject,
      dct,
      isMono);
}

//  void QPdfEnginePrivate::writePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate9writePageEv(QPdfEnginePrivate *self) {
  self->writePage();
}

//  int QPdfEnginePrivate::addXrefEntry(int object, bool printostr)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate12addXrefEntryEib(
    QPdfEnginePrivate *self,
    int object,
    bool printostr) {
  return self->addXrefEntry(object, printostr);
}

//  void QPdfEnginePrivate::printString(QStringView string)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate11printStringE11QStringView(
    QPdfEnginePrivate *self,
    const QString *string) {
  self->printString(QStringView(*string));
}

//  void QPdfEnginePrivate::write(QByteArrayView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate5writeE14QByteArrayView(
    QPdfEnginePrivate *self,
    const QByteArrayView *data) {
  self->write(*data);
}

//  int QPdfEnginePrivate::writeCompressed(const char *src, int len)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate15writeCompressedEPKci(
    QPdfEnginePrivate *self,
    const char *src,
    int len) {
  return self->writeCompressed(src, len);
}

//  int QPdfEnginePrivate::writeCompressed(const QByteArray &data)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate15writeCompressedERK10QByteArray(
    QPdfEnginePrivate *self,
    const QByteArray *data) {
  return self->writeCompressed(*data);
}

//  int QPdfEnginePrivate::writeCompressed(QIODevice *dev)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfEnginePrivate15writeCompressedEP9QIODevice(
    QPdfEnginePrivate *self,
    QIODevice *dev) {
  return self->writeCompressed(dev);
}

//  a Python function taken by a CuteQPdfEnginePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfEnginePrivate(
    QPdfEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfEnginePrivate *>(self)->take(key, call);
}

//  a QPdfEnginePrivate::ShadingFunctionResult a ritual of QPdfEnginePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPdfEnginePrivate__QPdfEnginePrivate_ShadingFunctionResult(
    QPdfEnginePrivate::ShadingFunctionResult *self) {
  delete self;
}

//  void QPdfEnginePrivate::xprintf(const char *fmt, ...)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfEnginePrivate7xprintfEPKcz(
    QPdfEnginePrivate *self,
    const char *text) {
  self->xprintf("%s", text);
}

#endif  // !defined(QT_NO_PDF)
