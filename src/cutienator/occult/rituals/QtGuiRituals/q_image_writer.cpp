//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimagewriter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimagewriter.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>

//  QString QImageWriter::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QImageWriter2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QImageWriter::tr(sourceText, disambiguation, n));
}

//  QImageWriter::QImageWriter()
extern "C" Q_DECL_EXPORT
QImageWriter *ritual_ZN12QImageWriterC1Ev() {
  return new QImageWriter();
}

//  QImageWriter::QImageWriter(QIODevice *device, const QByteArray &format)
extern "C" Q_DECL_EXPORT
QImageWriter *ritual_ZN12QImageWriterC1EP9QIODeviceRK10QByteArray(
    QIODevice *device,
    const QByteArray *format) {
  return new QImageWriter(device, *format);
}

//  QImageWriter::QImageWriter(const QString &fileName, const QByteArray
//      &format)
extern "C" Q_DECL_EXPORT
QImageWriter *ritual_ZN12QImageWriterC1ERK7QStringRK10QByteArray(
    const QString *fileName,
    const QByteArray *format) {
  return new QImageWriter(*fileName, *format);
}

//  QImageWriter::~QImageWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriterD1Ev(QImageWriter *self) {
  delete self;
}

//  void QImageWriter::setFormat(const QByteArray &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter9setFormatERK10QByteArray(
    QImageWriter *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  QByteArray QImageWriter::format() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QImageWriter6formatEv(const QImageWriter *self) {
  return new QByteArray(self->format());
}

//  void QImageWriter::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter9setDeviceEP9QIODevice(
    QImageWriter *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QImageWriter::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK12QImageWriter6deviceEv(const QImageWriter *self) {
  return self->device();
}

//  void QImageWriter::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter11setFileNameERK7QString(
    QImageWriter *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QImageWriter::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QImageWriter8fileNameEv(const QImageWriter *self) {
  return new QString(self->fileName());
}

//  void QImageWriter::setQuality(int quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter10setQualityEi(QImageWriter *self, int quality) {
  self->setQuality(quality);
}

//  int QImageWriter::quality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageWriter7qualityEv(const QImageWriter *self) {
  return self->quality();
}

//  void QImageWriter::setCompression(int compression)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter14setCompressionEi(
    QImageWriter *self,
    int compression) {
  self->setCompression(compression);
}

//  int QImageWriter::compression() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageWriter11compressionEv(const QImageWriter *self) {
  return self->compression();
}

//  void QImageWriter::setSubType(const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter10setSubTypeERK10QByteArray(
    QImageWriter *self,
    const QByteArray *type) {
  self->setSubType(*type);
}

//  QByteArray QImageWriter::subType() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QImageWriter7subTypeEv(const QImageWriter *self) {
  return new QByteArray(self->subType());
}

//  void QImageWriter::setOptimizedWrite(bool optimize)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter17setOptimizedWriteEb(
    QImageWriter *self,
    bool optimize) {
  self->setOptimizedWrite(optimize);
}

//  bool QImageWriter::optimizedWrite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageWriter14optimizedWriteEv(const QImageWriter *self) {
  return self->optimizedWrite();
}

//  void QImageWriter::setProgressiveScanWrite(bool progressive)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter23setProgressiveScanWriteEb(
    QImageWriter *self,
    bool progressive) {
  self->setProgressiveScanWrite(progressive);
}

//  bool QImageWriter::progressiveScanWrite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageWriter20progressiveScanWriteEv(
    const QImageWriter *self) {
  return self->progressiveScanWrite();
}

//  QImageIOHandler::Transformations QImageWriter::transformation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageWriter14transformationEv(const QImageWriter *self) {
  return static_cast<int>(self->transformation().toInt());
}

//  void QImageWriter::setTransformation(QImageIOHandler::Transformations
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter17setTransformationE6QFlagsIN15QImageIOHandler14TransformationEE(
    QImageWriter *self,
    int orientation) {
  self->setTransformation(
      QFlags<QImageIOHandler::Transformation>::fromInt(orientation));
}

//  void QImageWriter::setText(const QString &key, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageWriter7setTextERK7QStringS2_(
    QImageWriter *self,
    const QString *key,
    const QString *text) {
  self->setText(*key, *text);
}

//  bool QImageWriter::canWrite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageWriter8canWriteEv(const QImageWriter *self) {
  return self->canWrite();
}

//  bool QImageWriter::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QImageWriter5writeERK6QImage(
    QImageWriter *self,
    const QImage *image) {
  return self->write(*image);
}

//  ImageWriterError QImageWriter::error() const
extern "C" Q_DECL_EXPORT
QImageWriter::ImageWriterError ritual_ZNK12QImageWriter5errorEv(
    const QImageWriter *self) {
  return self->error();
}

//  QString QImageWriter::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QImageWriter11errorStringEv(const QImageWriter *self) {
  return new QString(self->errorString());
}

//  bool QImageWriter::supportsOption(QImageIOHandler::ImageOption option)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageWriter14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QImageWriter *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}
