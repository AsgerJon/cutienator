//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
#include <QtCore/qxmlstream.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QXmlStreamReader::QXmlStreamReader()
extern "C" Q_DECL_EXPORT
QXmlStreamReader *ritual_ZN16QXmlStreamReaderC1Ev() {
  return new QXmlStreamReader();
}

//  QXmlStreamReader::QXmlStreamReader(QIODevice *device)
extern "C" Q_DECL_EXPORT
QXmlStreamReader *ritual_ZN16QXmlStreamReaderC1EP9QIODevice(
    QIODevice *device) {
  return new QXmlStreamReader(device);
}

//  QXmlStreamReader::QXmlStreamReader(QAnyStringView data)
extern "C" Q_DECL_EXPORT
QXmlStreamReader *ritual_ZN16QXmlStreamReaderC1E14QAnyStringView(
    const QString *data) {
  return new QXmlStreamReader(QAnyStringView(*data));
}

//  QXmlStreamReader::~QXmlStreamReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReaderD1Ev(QXmlStreamReader *self) {
  delete self;
}

//  void QXmlStreamReader::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader9setDeviceEP9QIODevice(
    QXmlStreamReader *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QXmlStreamReader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK16QXmlStreamReader6deviceEv(
    const QXmlStreamReader *self) {
  return self->device();
}

//  void QXmlStreamReader::addData(QAnyStringView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader7addDataE14QAnyStringView(
    QXmlStreamReader *self,
    const QString *data) {
  self->addData(QAnyStringView(*data));
}

//  void QXmlStreamReader::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader5clearEv(QXmlStreamReader *self) {
  self->clear();
}

//  bool QXmlStreamReader::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader5atEndEv(const QXmlStreamReader *self) {
  return self->atEnd();
}

//  TokenType QXmlStreamReader::readNext()
extern "C" Q_DECL_EXPORT
QXmlStreamReader::TokenType ritual_ZN16QXmlStreamReader8readNextEv(
    QXmlStreamReader *self) {
  return self->readNext();
}

//  bool QXmlStreamReader::readNextStartElement()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlStreamReader20readNextStartElementEv(
    QXmlStreamReader *self) {
  return self->readNextStartElement();
}

//  void QXmlStreamReader::skipCurrentElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader18skipCurrentElementEv(
    QXmlStreamReader *self) {
  self->skipCurrentElement();
}

//  QString QXmlStreamReader::readRawInnerData()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QXmlStreamReader16readRawInnerDataEv(
    QXmlStreamReader *self) {
  return new QString(self->readRawInnerData());
}

//  TokenType QXmlStreamReader::tokenType() const
extern "C" Q_DECL_EXPORT
QXmlStreamReader::TokenType ritual_ZNK16QXmlStreamReader9tokenTypeEv(
    const QXmlStreamReader *self) {
  return self->tokenType();
}

//  QString QXmlStreamReader::tokenString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader11tokenStringEv(
    const QXmlStreamReader *self) {
  return new QString(self->tokenString());
}

//  void QXmlStreamReader::setNamespaceProcessing(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader22setNamespaceProcessingEb(
    QXmlStreamReader *self,
    bool a0) {
  self->setNamespaceProcessing(a0);
}

//  bool QXmlStreamReader::namespaceProcessing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader19namespaceProcessingEv(
    const QXmlStreamReader *self) {
  return self->namespaceProcessing();
}

//  bool QXmlStreamReader::isStartDocument() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader15isStartDocumentEv(
    const QXmlStreamReader *self) {
  return self->isStartDocument();
}

//  bool QXmlStreamReader::isEndDocument() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader13isEndDocumentEv(
    const QXmlStreamReader *self) {
  return self->isEndDocument();
}

//  bool QXmlStreamReader::isStartElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader14isStartElementEv(
    const QXmlStreamReader *self) {
  return self->isStartElement();
}

//  bool QXmlStreamReader::isEndElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader12isEndElementEv(
    const QXmlStreamReader *self) {
  return self->isEndElement();
}

//  bool QXmlStreamReader::isCharacters() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader12isCharactersEv(
    const QXmlStreamReader *self) {
  return self->isCharacters();
}

//  bool QXmlStreamReader::isWhitespace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader12isWhitespaceEv(
    const QXmlStreamReader *self) {
  return self->isWhitespace();
}

//  bool QXmlStreamReader::isCDATA() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader7isCDATAEv(const QXmlStreamReader *self) {
  return self->isCDATA();
}

//  bool QXmlStreamReader::isComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader9isCommentEv(const QXmlStreamReader *self) {
  return self->isComment();
}

//  bool QXmlStreamReader::isDTD() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader5isDTDEv(const QXmlStreamReader *self) {
  return self->isDTD();
}

//  bool QXmlStreamReader::isEntityReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader17isEntityReferenceEv(
    const QXmlStreamReader *self) {
  return self->isEntityReference();
}

//  bool QXmlStreamReader::isProcessingInstruction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader23isProcessingInstructionEv(
    const QXmlStreamReader *self) {
  return self->isProcessingInstruction();
}

//  bool QXmlStreamReader::isStandaloneDocument() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader20isStandaloneDocumentEv(
    const QXmlStreamReader *self) {
  return self->isStandaloneDocument();
}

//  bool QXmlStreamReader::hasStandaloneDeclaration() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader24hasStandaloneDeclarationEv(
    const QXmlStreamReader *self) {
  return self->hasStandaloneDeclaration();
}

//  QStringView QXmlStreamReader::documentVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader15documentVersionEv(
    const QXmlStreamReader *self) {
  return new QString(self->documentVersion().toString());
}

//  QStringView QXmlStreamReader::documentEncoding() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader16documentEncodingEv(
    const QXmlStreamReader *self) {
  return new QString(self->documentEncoding().toString());
}

//  qint64 QXmlStreamReader::lineNumber() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QXmlStreamReader10lineNumberEv(
    const QXmlStreamReader *self) {
  return self->lineNumber();
}

//  qint64 QXmlStreamReader::columnNumber() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QXmlStreamReader12columnNumberEv(
    const QXmlStreamReader *self) {
  return self->columnNumber();
}

//  qint64 QXmlStreamReader::characterOffset() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QXmlStreamReader15characterOffsetEv(
    const QXmlStreamReader *self) {
  return self->characterOffset();
}

//  QXmlStreamAttributes QXmlStreamReader::attributes() const
extern "C" Q_DECL_EXPORT
QXmlStreamAttributes *ritual_ZNK16QXmlStreamReader10attributesEv(
    const QXmlStreamReader *self) {
  return new QXmlStreamAttributes(self->attributes());
}

//  QString QXmlStreamReader::readElementText(ReadElementTextBehaviour
//      behaviour)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QXmlStreamReader15readElementTextENS_24ReadElementTextBehaviourE(
    QXmlStreamReader *self,
    QXmlStreamReader::ReadElementTextBehaviour behaviour) {
  return new QString(self->readElementText(behaviour));
}

//  QStringView QXmlStreamReader::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader4nameEv(const QXmlStreamReader *self) {
  return new QString(self->name().toString());
}

//  QStringView QXmlStreamReader::namespaceUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader12namespaceUriEv(
    const QXmlStreamReader *self) {
  return new QString(self->namespaceUri().toString());
}

//  QStringView QXmlStreamReader::qualifiedName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader13qualifiedNameEv(
    const QXmlStreamReader *self) {
  return new QString(self->qualifiedName().toString());
}

//  QStringView QXmlStreamReader::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader6prefixEv(
    const QXmlStreamReader *self) {
  return new QString(self->prefix().toString());
}

//  QStringView QXmlStreamReader::processingInstructionTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader27processingInstructionTargetEv(
    const QXmlStreamReader *self) {
  return new QString(self->processingInstructionTarget().toString());
}

//  QStringView QXmlStreamReader::processingInstructionData() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader25processingInstructionDataEv(
    const QXmlStreamReader *self) {
  return new QString(self->processingInstructionData().toString());
}

//  QStringView QXmlStreamReader::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader4textEv(const QXmlStreamReader *self) {
  return new QString(self->text().toString());
}

//  QXmlStreamNamespaceDeclarations QXmlStreamReader::namespaceDeclarations()
//      const
extern "C" Q_DECL_EXPORT
QList<QXmlStreamNamespaceDeclaration> *ritual_ZNK16QXmlStreamReader21namespaceDeclarationsEv(
    const QXmlStreamReader *self) {
  return new QList<QXmlStreamNamespaceDeclaration>(
      self->namespaceDeclarations());
}

//  void QXmlStreamReader::addExtraNamespaceDeclaration(const
//      QXmlStreamNamespaceDeclaration &extraNamespaceDeclaraction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader28addExtraNamespaceDeclarationERK30QXmlStreamNamespaceDeclaration(
    QXmlStreamReader *self,
    const QXmlStreamNamespaceDeclaration *extraNamespaceDeclaraction) {
  self->addExtraNamespaceDeclaration(*extraNamespaceDeclaraction);
}

//  void QXmlStreamReader::addExtraNamespaceDeclarations(const
//      QXmlStreamNamespaceDeclarations &extraNamespaceDeclaractions)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader29addExtraNamespaceDeclarationsERK5QListI30QXmlStreamNamespaceDeclarationE(
    QXmlStreamReader *self,
    const QList<QXmlStreamNamespaceDeclaration> *extraNamespaceDeclaractions) {
  self->addExtraNamespaceDeclarations(*extraNamespaceDeclaractions);
}

//  QXmlStreamNotationDeclarations QXmlStreamReader::notationDeclarations()
//      const
extern "C" Q_DECL_EXPORT
QList<QXmlStreamNotationDeclaration> *ritual_ZNK16QXmlStreamReader20notationDeclarationsEv(
    const QXmlStreamReader *self) {
  return new QList<QXmlStreamNotationDeclaration>(
      self->notationDeclarations());
}

//  QXmlStreamEntityDeclarations QXmlStreamReader::entityDeclarations() const
extern "C" Q_DECL_EXPORT
QList<QXmlStreamEntityDeclaration> *ritual_ZNK16QXmlStreamReader18entityDeclarationsEv(
    const QXmlStreamReader *self) {
  return new QList<QXmlStreamEntityDeclaration>(self->entityDeclarations());
}

//  QStringView QXmlStreamReader::dtdName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader7dtdNameEv(
    const QXmlStreamReader *self) {
  return new QString(self->dtdName().toString());
}

//  QStringView QXmlStreamReader::dtdPublicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader11dtdPublicIdEv(
    const QXmlStreamReader *self) {
  return new QString(self->dtdPublicId().toString());
}

//  QStringView QXmlStreamReader::dtdSystemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader11dtdSystemIdEv(
    const QXmlStreamReader *self) {
  return new QString(self->dtdSystemId().toString());
}

//  int QXmlStreamReader::entityExpansionLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QXmlStreamReader20entityExpansionLimitEv(
    const QXmlStreamReader *self) {
  return self->entityExpansionLimit();
}

//  void QXmlStreamReader::setEntityExpansionLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader23setEntityExpansionLimitEi(
    QXmlStreamReader *self,
    int limit) {
  self->setEntityExpansionLimit(limit);
}

//  void QXmlStreamReader::raiseError(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader10raiseErrorERK7QString(
    QXmlStreamReader *self,
    const QString *message) {
  self->raiseError(*message);
}

//  QString QXmlStreamReader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlStreamReader11errorStringEv(
    const QXmlStreamReader *self) {
  return new QString(self->errorString());
}

//  Error QXmlStreamReader::error() const
extern "C" Q_DECL_EXPORT
QXmlStreamReader::Error ritual_ZNK16QXmlStreamReader5errorEv(
    const QXmlStreamReader *self) {
  return self->error();
}

//  bool QXmlStreamReader::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlStreamReader8hasErrorEv(const QXmlStreamReader *self) {
  return self->hasError();
}

//  void QXmlStreamReader::setEntityResolver(QXmlStreamEntityResolver
//      *resolver)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader17setEntityResolverEP24QXmlStreamEntityResolver(
    QXmlStreamReader *self,
    QXmlStreamEntityResolver *resolver) {
  self->setEntityResolver(resolver);
}

//  QXmlStreamEntityResolver *QXmlStreamReader::entityResolver() const
extern "C" Q_DECL_EXPORT
QXmlStreamEntityResolver *ritual_ZNK16QXmlStreamReader14entityResolverEv(
    const QXmlStreamReader *self) {
  return self->entityResolver();
}

//  void QXmlStreamReader::addDataImpl(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlStreamReader11addDataImplERK10QByteArray(
    QXmlStreamReader *self,
    const QByteArray *data) {
  self->addDataImpl(*data);
}

//  QXmlStreamReaderPrivate *QXmlStreamReader::d_func()
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate *ritual_ZN16QXmlStreamReader6d_funcEv(
    QXmlStreamReader *self) {
  return self->d_func();
}

//  const QXmlStreamReaderPrivate *QXmlStreamReader::d_func() const
extern "C" Q_DECL_EXPORT
const QXmlStreamReaderPrivate *ritual_ZNK16QXmlStreamReader6d_funcEv(
    const QXmlStreamReader *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)
#endif  // QT_CONFIG(xmlstream)
