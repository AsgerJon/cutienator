//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextdocumentwriter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextdocumentwriter.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextdocumentfragment.h>
#include <QtCore/qlist.h>

//  QTextDocumentWriter::QTextDocumentWriter()
extern "C" Q_DECL_EXPORT
QTextDocumentWriter *ritual_ZN19QTextDocumentWriterC1Ev() {
  return new QTextDocumentWriter();
}

//  QTextDocumentWriter::QTextDocumentWriter(QIODevice *device, const
//      QByteArray &format)
extern "C" Q_DECL_EXPORT
QTextDocumentWriter *ritual_ZN19QTextDocumentWriterC1EP9QIODeviceRK10QByteArray(
    QIODevice *device,
    const QByteArray *format) {
  return new QTextDocumentWriter(device, *format);
}

//  QTextDocumentWriter::QTextDocumentWriter(const QString &fileName, const
//      QByteArray &format)
extern "C" Q_DECL_EXPORT
QTextDocumentWriter *ritual_ZN19QTextDocumentWriterC1ERK7QStringRK10QByteArray(
    const QString *fileName,
    const QByteArray *format) {
  return new QTextDocumentWriter(*fileName, *format);
}

//  QTextDocumentWriter::~QTextDocumentWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentWriterD1Ev(QTextDocumentWriter *self) {
  delete self;
}

//  void QTextDocumentWriter::setFormat(const QByteArray &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentWriter9setFormatERK10QByteArray(
    QTextDocumentWriter *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  QByteArray QTextDocumentWriter::format() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QTextDocumentWriter6formatEv(
    const QTextDocumentWriter *self) {
  return new QByteArray(self->format());
}

//  void QTextDocumentWriter::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentWriter9setDeviceEP9QIODevice(
    QTextDocumentWriter *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QTextDocumentWriter::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK19QTextDocumentWriter6deviceEv(
    const QTextDocumentWriter *self) {
  return self->device();
}

//  void QTextDocumentWriter::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentWriter11setFileNameERK7QString(
    QTextDocumentWriter *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QTextDocumentWriter::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QTextDocumentWriter8fileNameEv(
    const QTextDocumentWriter *self) {
  return new QString(self->fileName());
}

//  bool QTextDocumentWriter::write(const QTextDocument *document)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextDocumentWriter5writeEPK13QTextDocument(
    QTextDocumentWriter *self,
    const QTextDocument *document) {
  return self->write(document);
}

//  bool QTextDocumentWriter::write(const QTextDocumentFragment &fragment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextDocumentWriter5writeERK21QTextDocumentFragment(
    QTextDocumentWriter *self,
    const QTextDocumentFragment *fragment) {
  return self->write(*fragment);
}

//  QList<QByteArray> QTextDocumentWriter::supportedDocumentFormats()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN19QTextDocumentWriter24supportedDocumentFormatsEv() {
  return new QList<QByteArray>(
      QTextDocumentWriter::supportedDocumentFormats());
}
