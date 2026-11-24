//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamwriter)
#include <QtCore/qxmlstream.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QXmlStreamWriter::QXmlStreamWriter()
extern "C" Q_DECL_EXPORT
QXmlStreamWriter *ritual_ZN16QXmlStreamWriterC1Ev() {
  return new QXmlStreamWriter();
}

//  QXmlStreamWriter::QXmlStreamWriter(QIODevice *device)
extern "C" Q_DECL_EXPORT
QXmlStreamWriter *ritual_ZN16QXmlStreamWriterC1EP9QIODevice(
    QIODevice *device) {
  return new QXmlStreamWriter(device);
}

//  QXmlStreamWriter::QXmlStreamWriter(QByteArray *array)
extern "C" Q_DECL_EXPORT
QXmlStreamWriter *ritual_ZN16QXmlStreamWriterC1EP10QByteArray(
    QByteArray *array) {
  return new QXmlStreamWriter(array);
}

//  QXmlStreamWriter::QXmlStreamWriter(QString *string)
extern "C" Q_DECL_EXPORT
QXmlStreamWriter *ritual_ZN16QXmlStreamWriterC1EP7QString(QString *string) {
  return new QXmlStreamWriter(string);
}

//  QXmlStreamWriter::~QXmlStreamWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriterD1Ev(QXmlStreamWriter *self) {
  delete self;
}

//  void QXmlStreamWriter::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter9setDeviceEP9QIODevice(
    QXmlStreamWriter *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QXmlStreamWriter::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK16QXmlStreamWriter6deviceEv(
    const QXmlStreamWriter *self) {
  return self->device();
}

//  void QXmlStreamWriter::setAutoFormatting(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter17setAutoFormattingEb(
    QXmlStreamWriter *self,
    bool a0) {
  self->setAutoFormatting(a0);
}

//  bool QXmlStreamWriter::autoFormatting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamWriter14autoFormattingEv(
    const QXmlStreamWriter *self) {
  return self->autoFormatting();
}

//  void QXmlStreamWriter::setAutoFormattingIndent(int spacesOrTabs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter23setAutoFormattingIndentEi(
    QXmlStreamWriter *self,
    int spacesOrTabs) {
  self->setAutoFormattingIndent(spacesOrTabs);
}

//  int QXmlStreamWriter::autoFormattingIndent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QXmlStreamWriter20autoFormattingIndentEv(
    const QXmlStreamWriter *self) {
  return self->autoFormattingIndent();
}

//  void QXmlStreamWriter::setStopWritingOnError(bool stop)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter21setStopWritingOnErrorEb(
    QXmlStreamWriter *self,
    bool stop) {
  self->setStopWritingOnError(stop);
}

//  bool QXmlStreamWriter::stopWritingOnError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamWriter18stopWritingOnErrorEv(
    const QXmlStreamWriter *self) {
  return self->stopWritingOnError();
}

//  void QXmlStreamWriter::writeAttribute(QAnyStringView qualifiedName,
//      QAnyStringView value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter14writeAttributeE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *qualifiedName,
    const QString *value) {
  self->writeAttribute(
      QAnyStringView(*qualifiedName),
      QAnyStringView(*value));
}

//  void QXmlStreamWriter::writeAttribute(QAnyStringView namespaceUri,
//      QAnyStringView name, QAnyStringView value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter14writeAttributeE14QAnyStringViewS0_S0_(
    QXmlStreamWriter *self,
    const QString *namespaceUri,
    const QString *name,
    const QString *value) {
  self->writeAttribute(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*name),
      QAnyStringView(*value));
}

//  void QXmlStreamWriter::writeAttribute(const QXmlStreamAttribute
//      &attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter14writeAttributeERK19QXmlStreamAttribute(
    QXmlStreamWriter *self,
    const QXmlStreamAttribute *attribute) {
  self->writeAttribute(*attribute);
}

//  void QXmlStreamWriter::writeAttributes(const QXmlStreamAttributes
//      &attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter15writeAttributesERK20QXmlStreamAttributes(
    QXmlStreamWriter *self,
    const QXmlStreamAttributes *attributes) {
  self->writeAttributes(*attributes);
}

//  void QXmlStreamWriter::writeCDATA(QAnyStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter10writeCDATAE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *text) {
  self->writeCDATA(QAnyStringView(*text));
}

//  void QXmlStreamWriter::writeCharacters(QAnyStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter15writeCharactersE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *text) {
  self->writeCharacters(QAnyStringView(*text));
}

//  void QXmlStreamWriter::writeComment(QAnyStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter12writeCommentE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *text) {
  self->writeComment(QAnyStringView(*text));
}

//  void QXmlStreamWriter::writeDTD(QAnyStringView dtd)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter8writeDTDE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *dtd) {
  self->writeDTD(QAnyStringView(*dtd));
}

//  void QXmlStreamWriter::writeEmptyElement(QAnyStringView qualifiedName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter17writeEmptyElementE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *qualifiedName) {
  self->writeEmptyElement(QAnyStringView(*qualifiedName));
}

//  void QXmlStreamWriter::writeEmptyElement(QAnyStringView namespaceUri,
//      QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter17writeEmptyElementE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *namespaceUri,
    const QString *name) {
  self->writeEmptyElement(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*name));
}

//  void QXmlStreamWriter::writeTextElement(QAnyStringView qualifiedName,
//      QAnyStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter16writeTextElementE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *qualifiedName,
    const QString *text) {
  self->writeTextElement(
      QAnyStringView(*qualifiedName),
      QAnyStringView(*text));
}

//  void QXmlStreamWriter::writeTextElement(QAnyStringView namespaceUri,
//      QAnyStringView name, QAnyStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter16writeTextElementE14QAnyStringViewS0_S0_(
    QXmlStreamWriter *self,
    const QString *namespaceUri,
    const QString *name,
    const QString *text) {
  self->writeTextElement(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*name),
      QAnyStringView(*text));
}

//  void QXmlStreamWriter::writeEndDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter16writeEndDocumentEv(
    QXmlStreamWriter *self) {
  self->writeEndDocument();
}

//  void QXmlStreamWriter::writeEndElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter15writeEndElementEv(QXmlStreamWriter *self) {
  self->writeEndElement();
}

//  void QXmlStreamWriter::writeEntityReference(QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter20writeEntityReferenceE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *name) {
  self->writeEntityReference(QAnyStringView(*name));
}

//  void QXmlStreamWriter::writeNamespace(QAnyStringView namespaceUri,
//      QAnyStringView prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter14writeNamespaceE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *namespaceUri,
    const QString *prefix) {
  self->writeNamespace(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*prefix));
}

//  void QXmlStreamWriter::writeDefaultNamespace(QAnyStringView namespaceUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter21writeDefaultNamespaceE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *namespaceUri) {
  self->writeDefaultNamespace(QAnyStringView(*namespaceUri));
}

//  void QXmlStreamWriter::writeProcessingInstruction(QAnyStringView target,
//      QAnyStringView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter26writeProcessingInstructionE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *target,
    const QString *data) {
  self->writeProcessingInstruction(
      QAnyStringView(*target),
      QAnyStringView(*data));
}

//  void QXmlStreamWriter::writeStartDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter18writeStartDocumentEv(
    QXmlStreamWriter *self) {
  self->writeStartDocument();
}

//  void QXmlStreamWriter::writeStartDocument(QAnyStringView version)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter18writeStartDocumentE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *version) {
  self->writeStartDocument(QAnyStringView(*version));
}

//  void QXmlStreamWriter::writeStartDocument(QAnyStringView version, bool
//      standalone)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter18writeStartDocumentE14QAnyStringViewb(
    QXmlStreamWriter *self,
    const QString *version,
    bool standalone) {
  self->writeStartDocument(QAnyStringView(*version), standalone);
}

//  void QXmlStreamWriter::writeStartElement(QAnyStringView qualifiedName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter17writeStartElementE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *qualifiedName) {
  self->writeStartElement(QAnyStringView(*qualifiedName));
}

//  void QXmlStreamWriter::writeStartElement(QAnyStringView namespaceUri,
//      QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter17writeStartElementE14QAnyStringViewS0_(
    QXmlStreamWriter *self,
    const QString *namespaceUri,
    const QString *name) {
  self->writeStartElement(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*name));
}

//  void QXmlStreamWriter::raiseError(QAnyStringView message)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamWriter10raiseErrorE14QAnyStringView(
    QXmlStreamWriter *self,
    const QString *message) {
  self->raiseError(QAnyStringView(*message));
}

//  QString QXmlStreamWriter::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamWriter11errorStringEv(
    const QXmlStreamWriter *self) {
  return new QString(self->errorString());
}

//  Error QXmlStreamWriter::error() const
extern "C" Q_DECL_EXPORT
QXmlStreamWriter::Error ritual_ZNK16QXmlStreamWriter5errorEv(
    const QXmlStreamWriter *self) {
  return self->error();
}

//  bool QXmlStreamWriter::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamWriter8hasErrorEv(const QXmlStreamWriter *self) {
  return self->hasError();
}

#endif  // QT_CONFIG(xmlstreamwriter)
#endif  // QT_CONFIG(xmlstream)
