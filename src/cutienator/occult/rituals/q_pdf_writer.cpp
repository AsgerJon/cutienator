//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpdfwriter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpdfwriter.h>
#include <QtCore/qstring.h>
#include <QtCore/quuid.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qpdfoutputintent.h>

//  const QMetaObject *QPdfWriter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QPdfWriter10metaObjectEv(
    const QPdfWriter *self) {
  return self->metaObject();
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
  return new QPdfWriter(*filename);
}

//  QPdfWriter::QPdfWriter(QIODevice *device)
extern "C" Q_DECL_EXPORT
QPdfWriter *ritual_ZN10QPdfWriterC1EP9QIODevice(QIODevice *device) {
  return new QPdfWriter(device);
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
