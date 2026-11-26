//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 2. Kept as it is
//  when the generator runs again.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlDefaultHandler that Python can take functions over in. Every QXmlDefaultHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXmlDefaultHandlerCall0)(const void *, QXmlLocator *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall1)(const void *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall2)(const void *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall3)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall4)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall5)(const void *, const QString *, const QString *, const QString *, const QXmlAttributes *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall6)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall7)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall8)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall9)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall10)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall11)(const void *, const QXmlParseException *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall12)(const void *, const QXmlParseException *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall13)(const void *, const QXmlParseException *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall14)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall15)(const void *, const QString *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall16)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall17)(const void *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall18)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall19)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall20)(const void *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall21)(const void *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall22)(const void *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall23)(const void *, const QString *, const QString *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall24)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDefaultHandlerCall25)(const void *, const QString *, const QString *, const QString *, int *);
typedef QString * (*CuteQXmlDefaultHandlerCall26)(const void *, int *);
class CuteQXmlDefaultHandler : public QXmlDefaultHandler {
public:
  using QXmlDefaultHandler::QXmlDefaultHandler;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QXmlContentHandler18setDocumentLocatorEP11QXmlLocator")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler13startDocumentEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler11endDocumentEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler18startPrefixMappingERK7QStringS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler16endPrefixMappingERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler12startElementERK7QStringS2_S2_RK14QXmlAttributes")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler10endElementERK7QStringS2_S2_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler10charactersERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler19ignorableWhitespaceERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler21processingInstructionERK7QStringS2_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlContentHandler13skippedEntityERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler7warningERK18QXmlParseException")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler5errorERK18QXmlParseException")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler10fatalErrorERK18QXmlParseException")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QXmlDTDHandler12notationDeclERK7QStringS2_S2_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QXmlDTDHandler18unparsedEntityDeclERK7QStringS2_S2_S2_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler8startDTDERK7QStringS2_S2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler6endDTDEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler11startEntityERK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler9endEntityERK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler10startCDATAEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler8endCDATAEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler7commentERK7QString")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler13attributeDeclERK7QStringS2_S2_S2_S2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler18internalEntityDeclERK7QStringS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler18externalEntityDeclERK7QStringS2_S2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QXmlContentHandler11errorStringEv")) {
      taken[26] = call;
      return true;
    }
    return false;
  }

  //  void QXmlDefaultHandler::setDocumentLocator(QXmlLocator *locator)
  void setDocumentLocator(QXmlLocator *locator) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall0 call = reinterpret_cast<CuteQXmlDefaultHandlerCall0>(taken[0]);
      call(this, locator, &handled);
      if (handled) return;
    }
    QXmlDefaultHandler::setDocumentLocator(locator);
  }

  //  bool QXmlDefaultHandler::startDocument()
  bool startDocument() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall1 call = reinterpret_cast<CuteQXmlDefaultHandlerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startDocument();
  }

  //  bool QXmlDefaultHandler::endDocument()
  bool endDocument() override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall2 call = reinterpret_cast<CuteQXmlDefaultHandlerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endDocument();
  }

  //  bool QXmlDefaultHandler::startPrefixMapping(const QString &prefix,
  //      const QString &uri)
  bool startPrefixMapping(
      const QString &prefix,
      const QString &uri) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall3 call = reinterpret_cast<CuteQXmlDefaultHandlerCall3>(taken[3]);
      bool given = call(this, &prefix, &uri, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startPrefixMapping(prefix, uri);
  }

  //  bool QXmlDefaultHandler::endPrefixMapping(const QString &prefix)
  bool endPrefixMapping(const QString &prefix) override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall4 call = reinterpret_cast<CuteQXmlDefaultHandlerCall4>(taken[4]);
      bool given = call(this, &prefix, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endPrefixMapping(prefix);
  }

  //  bool QXmlDefaultHandler::startElement(const QString &namespaceURI,
  //      const QString &localName, const QString &qName, const
  //      QXmlAttributes &atts)
  bool startElement(
      const QString &namespaceURI,
      const QString &localName,
      const QString &qName,
      const QXmlAttributes &atts) override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall5 call = reinterpret_cast<CuteQXmlDefaultHandlerCall5>(taken[5]);
      bool given = call(this, &namespaceURI, &localName, &qName, &atts, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startElement(namespaceURI, localName, qName, atts);
  }

  //  bool QXmlDefaultHandler::endElement(const QString &namespaceURI,
  //      const QString &localName, const QString &qName)
  bool endElement(
      const QString &namespaceURI,
      const QString &localName,
      const QString &qName) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall6 call = reinterpret_cast<CuteQXmlDefaultHandlerCall6>(taken[6]);
      bool given = call(this, &namespaceURI, &localName, &qName, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endElement(namespaceURI, localName, qName);
  }

  //  bool QXmlDefaultHandler::characters(const QString &ch)
  bool characters(const QString &ch) override {
    if (taken[7]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall7 call = reinterpret_cast<CuteQXmlDefaultHandlerCall7>(taken[7]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::characters(ch);
  }

  //  bool QXmlDefaultHandler::ignorableWhitespace(const QString &ch)
  bool ignorableWhitespace(const QString &ch) override {
    if (taken[8]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall8 call = reinterpret_cast<CuteQXmlDefaultHandlerCall8>(taken[8]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::ignorableWhitespace(ch);
  }

  //  bool QXmlDefaultHandler::processingInstruction(const QString &target,
  //      const QString &data)
  bool processingInstruction(
      const QString &target,
      const QString &data) override {
    if (taken[9]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall9 call = reinterpret_cast<CuteQXmlDefaultHandlerCall9>(taken[9]);
      bool given = call(this, &target, &data, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::processingInstruction(target, data);
  }

  //  bool QXmlDefaultHandler::skippedEntity(const QString &name)
  bool skippedEntity(const QString &name) override {
    if (taken[10]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall10 call = reinterpret_cast<CuteQXmlDefaultHandlerCall10>(taken[10]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::skippedEntity(name);
  }

  //  bool QXmlDefaultHandler::warning(const QXmlParseException &exception)
  bool warning(const QXmlParseException &exception) override {
    if (taken[11]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall11 call = reinterpret_cast<CuteQXmlDefaultHandlerCall11>(taken[11]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::warning(exception);
  }

  //  bool QXmlDefaultHandler::error(const QXmlParseException &exception)
  bool error(const QXmlParseException &exception) override {
    if (taken[12]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall12 call = reinterpret_cast<CuteQXmlDefaultHandlerCall12>(taken[12]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::error(exception);
  }

  //  bool QXmlDefaultHandler::fatalError(const QXmlParseException
  //      &exception)
  bool fatalError(const QXmlParseException &exception) override {
    if (taken[13]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall13 call = reinterpret_cast<CuteQXmlDefaultHandlerCall13>(taken[13]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::fatalError(exception);
  }

  //  bool QXmlDefaultHandler::notationDecl(const QString &name, const
  //      QString &publicId, const QString &systemId)
  bool notationDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[14]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall14 call = reinterpret_cast<CuteQXmlDefaultHandlerCall14>(taken[14]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::notationDecl(name, publicId, systemId);
  }

  //  bool QXmlDefaultHandler::unparsedEntityDecl(const QString &name,
  //      const QString &publicId, const QString &systemId, const QString
  //      &notationName)
  bool unparsedEntityDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId,
      const QString &notationName) override {
    if (taken[15]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall15 call = reinterpret_cast<CuteQXmlDefaultHandlerCall15>(taken[15]);
      bool given = call(this, &name, &publicId, &systemId, &notationName, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::unparsedEntityDecl(name, publicId, systemId, notationName);
  }

  //  bool QXmlDefaultHandler::startDTD(const QString &name, const QString
  //      &publicId, const QString &systemId)
  bool startDTD(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[16]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall16 call = reinterpret_cast<CuteQXmlDefaultHandlerCall16>(taken[16]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startDTD(name, publicId, systemId);
  }

  //  bool QXmlDefaultHandler::endDTD()
  bool endDTD() override {
    if (taken[17]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall17 call = reinterpret_cast<CuteQXmlDefaultHandlerCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endDTD();
  }

  //  bool QXmlDefaultHandler::startEntity(const QString &name)
  bool startEntity(const QString &name) override {
    if (taken[18]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall18 call = reinterpret_cast<CuteQXmlDefaultHandlerCall18>(taken[18]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startEntity(name);
  }

  //  bool QXmlDefaultHandler::endEntity(const QString &name)
  bool endEntity(const QString &name) override {
    if (taken[19]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall19 call = reinterpret_cast<CuteQXmlDefaultHandlerCall19>(taken[19]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endEntity(name);
  }

  //  bool QXmlDefaultHandler::startCDATA()
  bool startCDATA() override {
    if (taken[20]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall20 call = reinterpret_cast<CuteQXmlDefaultHandlerCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::startCDATA();
  }

  //  bool QXmlDefaultHandler::endCDATA()
  bool endCDATA() override {
    if (taken[21]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall21 call = reinterpret_cast<CuteQXmlDefaultHandlerCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::endCDATA();
  }

  //  bool QXmlDefaultHandler::comment(const QString &ch)
  bool comment(const QString &ch) override {
    if (taken[22]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall22 call = reinterpret_cast<CuteQXmlDefaultHandlerCall22>(taken[22]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::comment(ch);
  }

  //  bool QXmlDefaultHandler::attributeDecl(const QString &eName, const
  //      QString &aName, const QString &type, const QString &valueDefault,
  //      const QString &value)
  bool attributeDecl(
      const QString &eName,
      const QString &aName,
      const QString &type,
      const QString &valueDefault,
      const QString &value) override {
    if (taken[23]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall23 call = reinterpret_cast<CuteQXmlDefaultHandlerCall23>(taken[23]);
      bool given = call(this, &eName, &aName, &type, &valueDefault, &value, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::attributeDecl(eName, aName, type, valueDefault, value);
  }

  //  bool QXmlDefaultHandler::internalEntityDecl(const QString &name,
  //      const QString &value)
  bool internalEntityDecl(
      const QString &name,
      const QString &value) override {
    if (taken[24]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall24 call = reinterpret_cast<CuteQXmlDefaultHandlerCall24>(taken[24]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::internalEntityDecl(name, value);
  }

  //  bool QXmlDefaultHandler::externalEntityDecl(const QString &name,
  //      const QString &publicId, const QString &systemId)
  bool externalEntityDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[25]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall25 call = reinterpret_cast<CuteQXmlDefaultHandlerCall25>(taken[25]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return QXmlDefaultHandler::externalEntityDecl(name, publicId, systemId);
  }

  //  QString QXmlDefaultHandler::errorString() const
  QString errorString() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQXmlDefaultHandlerCall26 call = reinterpret_cast<CuteQXmlDefaultHandlerCall26>(taken[26]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QXmlDefaultHandler::errorString();
  }
};

//  QXmlDefaultHandler::QXmlDefaultHandler()
extern "C" Q_DECL_EXPORT
QXmlDefaultHandler *ritual_ZN18QXmlDefaultHandlerC1Ev() {
  return new CuteQXmlDefaultHandler();
}

//  QXmlDefaultHandler::~QXmlDefaultHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlDefaultHandlerD1Ev(QXmlDefaultHandler *self) {
  delete self;
}

//  void QXmlDefaultHandler::setDocumentLocator(QXmlLocator *locator)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlDefaultHandler18setDocumentLocatorEP11QXmlLocator(
    QXmlDefaultHandler *self,
    QXmlLocator *locator) {
  self->setDocumentLocator(locator);
}

//  bool QXmlDefaultHandler::startDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler13startDocumentEv(
    QXmlDefaultHandler *self) {
  return self->startDocument();
}

//  bool QXmlDefaultHandler::endDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler11endDocumentEv(QXmlDefaultHandler *self) {
  return self->endDocument();
}

//  bool QXmlDefaultHandler::startPrefixMapping(const QString &prefix, const
//      QString &uri)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler18startPrefixMappingERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *prefix,
    const QString *uri) {
  return self->startPrefixMapping(*prefix, *uri);
}

//  bool QXmlDefaultHandler::endPrefixMapping(const QString &prefix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler16endPrefixMappingERK7QString(
    QXmlDefaultHandler *self,
    const QString *prefix) {
  return self->endPrefixMapping(*prefix);
}

//  bool QXmlDefaultHandler::startElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName, const QXmlAttributes &atts)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler12startElementERK7QStringS2_S2_RK14QXmlAttributes(
    QXmlDefaultHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName,
    const QXmlAttributes *atts) {
  return self->startElement(*namespaceURI, *localName, *qName, *atts);
}

//  bool QXmlDefaultHandler::endElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler10endElementERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName) {
  return self->endElement(*namespaceURI, *localName, *qName);
}

//  bool QXmlDefaultHandler::characters(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler10charactersERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->characters(*ch);
}

//  bool QXmlDefaultHandler::ignorableWhitespace(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler19ignorableWhitespaceERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->ignorableWhitespace(*ch);
}

//  bool QXmlDefaultHandler::processingInstruction(const QString &target,
//      const QString &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler21processingInstructionERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *target,
    const QString *data) {
  return self->processingInstruction(*target, *data);
}

//  bool QXmlDefaultHandler::skippedEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler13skippedEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->skippedEntity(*name);
}

//  bool QXmlDefaultHandler::warning(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler7warningERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->warning(*exception);
}

//  bool QXmlDefaultHandler::error(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler5errorERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->error(*exception);
}

//  bool QXmlDefaultHandler::fatalError(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler10fatalErrorERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->fatalError(*exception);
}

//  bool QXmlDefaultHandler::notationDecl(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler12notationDeclERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->notationDecl(*name, *publicId, *systemId);
}

//  bool QXmlDefaultHandler::unparsedEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId, const QString
//      &notationName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler18unparsedEntityDeclERK7QStringS2_S2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId,
    const QString *notationName) {
  return self->unparsedEntityDecl(
      *name,
      *publicId,
      *systemId,
      *notationName);
}

//  bool QXmlDefaultHandler::startDTD(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler8startDTDERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->startDTD(*name, *publicId, *systemId);
}

//  bool QXmlDefaultHandler::endDTD()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler6endDTDEv(QXmlDefaultHandler *self) {
  return self->endDTD();
}

//  bool QXmlDefaultHandler::startEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler11startEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->startEntity(*name);
}

//  bool QXmlDefaultHandler::endEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler9endEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->endEntity(*name);
}

//  bool QXmlDefaultHandler::startCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler10startCDATAEv(QXmlDefaultHandler *self) {
  return self->startCDATA();
}

//  bool QXmlDefaultHandler::endCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler8endCDATAEv(QXmlDefaultHandler *self) {
  return self->endCDATA();
}

//  bool QXmlDefaultHandler::comment(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler7commentERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->comment(*ch);
}

//  bool QXmlDefaultHandler::attributeDecl(const QString &eName, const
//      QString &aName, const QString &type, const QString &valueDefault,
//      const QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler13attributeDeclERK7QStringS2_S2_S2_S2_(
    QXmlDefaultHandler *self,
    const QString *eName,
    const QString *aName,
    const QString *type,
    const QString *valueDefault,
    const QString *value) {
  return self->attributeDecl(*eName, *aName, *type, *valueDefault, *value);
}

//  bool QXmlDefaultHandler::internalEntityDecl(const QString &name, const
//      QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler18internalEntityDeclERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *value) {
  return self->internalEntityDecl(*name, *value);
}

//  bool QXmlDefaultHandler::externalEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler18externalEntityDeclERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->externalEntityDecl(*name, *publicId, *systemId);
}

//  QString QXmlDefaultHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlDefaultHandler11errorStringEv(
    const QXmlDefaultHandler *self) {
  return new QString(self->errorString());
}

//  QXmlDefaultHandler as the QXmlErrorHandler it is built on
extern "C" Q_DECL_EXPORT
QXmlErrorHandler *ritual_cast_QXmlDefaultHandler_QXmlErrorHandler(
    QXmlDefaultHandler *self) {
  return static_cast<QXmlErrorHandler *>(self);
}

//  QXmlDefaultHandler as the QXmlDTDHandler it is built on
extern "C" Q_DECL_EXPORT
QXmlDTDHandler *ritual_cast_QXmlDefaultHandler_QXmlDTDHandler(
    QXmlDefaultHandler *self) {
  return static_cast<QXmlDTDHandler *>(self);
}

//  QXmlDefaultHandler as the QXmlEntityResolver it is built on
extern "C" Q_DECL_EXPORT
QXmlEntityResolver *ritual_cast_QXmlDefaultHandler_QXmlEntityResolver(
    QXmlDefaultHandler *self) {
  return static_cast<QXmlEntityResolver *>(self);
}

//  QXmlDefaultHandler as the QXmlLexicalHandler it is built on
extern "C" Q_DECL_EXPORT
QXmlLexicalHandler *ritual_cast_QXmlDefaultHandler_QXmlLexicalHandler(
    QXmlDefaultHandler *self) {
  return static_cast<QXmlLexicalHandler *>(self);
}

//  QXmlDefaultHandler as the QXmlDeclHandler it is built on
extern "C" Q_DECL_EXPORT
QXmlDeclHandler *ritual_cast_QXmlDefaultHandler_QXmlDeclHandler(
    QXmlDefaultHandler *self) {
  return static_cast<QXmlDeclHandler *>(self);
}

//  a Python function taken by a CuteQXmlDefaultHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlDefaultHandler(
    QXmlDefaultHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlDefaultHandler *>(self)->take(key, call);
}

//  void QXmlDefaultHandler::setDocumentLocator(QXmlLocator *locator)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QXmlDefaultHandler18setDocumentLocatorEP11QXmlLocator(
    QXmlDefaultHandler *self,
    QXmlLocator *locator) {
  self->QXmlDefaultHandler::setDocumentLocator(locator);
}

//  bool QXmlDefaultHandler::startDocument()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler13startDocumentEv(
    QXmlDefaultHandler *self) {
  return self->QXmlDefaultHandler::startDocument();
}

//  bool QXmlDefaultHandler::endDocument()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler11endDocumentEv(
    QXmlDefaultHandler *self) {
  return self->QXmlDefaultHandler::endDocument();
}

//  bool QXmlDefaultHandler::startPrefixMapping(const QString &prefix, const
//      QString &uri)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler18startPrefixMappingERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *prefix,
    const QString *uri) {
  return self->QXmlDefaultHandler::startPrefixMapping(*prefix, *uri);
}

//  bool QXmlDefaultHandler::endPrefixMapping(const QString &prefix)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler16endPrefixMappingERK7QString(
    QXmlDefaultHandler *self,
    const QString *prefix) {
  return self->QXmlDefaultHandler::endPrefixMapping(*prefix);
}

//  bool QXmlDefaultHandler::startElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName, const QXmlAttributes &atts)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler12startElementERK7QStringS2_S2_RK14QXmlAttributes(
    QXmlDefaultHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName,
    const QXmlAttributes *atts) {
  return self->QXmlDefaultHandler::startElement(
      *namespaceURI,
      *localName,
      *qName,
      *atts);
}

//  bool QXmlDefaultHandler::endElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler10endElementERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName) {
  return self->QXmlDefaultHandler::endElement(
      *namespaceURI,
      *localName,
      *qName);
}

//  bool QXmlDefaultHandler::characters(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler10charactersERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->QXmlDefaultHandler::characters(*ch);
}

//  bool QXmlDefaultHandler::ignorableWhitespace(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler19ignorableWhitespaceERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->QXmlDefaultHandler::ignorableWhitespace(*ch);
}

//  bool QXmlDefaultHandler::processingInstruction(const QString &target,
//      const QString &data)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler21processingInstructionERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *target,
    const QString *data) {
  return self->QXmlDefaultHandler::processingInstruction(*target, *data);
}

//  bool QXmlDefaultHandler::skippedEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler13skippedEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->QXmlDefaultHandler::skippedEntity(*name);
}

//  bool QXmlDefaultHandler::warning(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler7warningERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->QXmlDefaultHandler::warning(*exception);
}

//  bool QXmlDefaultHandler::error(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler5errorERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->QXmlDefaultHandler::error(*exception);
}

//  bool QXmlDefaultHandler::fatalError(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler10fatalErrorERK18QXmlParseException(
    QXmlDefaultHandler *self,
    const QXmlParseException *exception) {
  return self->QXmlDefaultHandler::fatalError(*exception);
}

//  bool QXmlDefaultHandler::notationDecl(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler12notationDeclERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->QXmlDefaultHandler::notationDecl(*name, *publicId, *systemId);
}

//  bool QXmlDefaultHandler::unparsedEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId, const QString
//      &notationName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler18unparsedEntityDeclERK7QStringS2_S2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId,
    const QString *notationName) {
  return self->QXmlDefaultHandler::unparsedEntityDecl(
      *name,
      *publicId,
      *systemId,
      *notationName);
}

//  bool QXmlDefaultHandler::startDTD(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler8startDTDERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->QXmlDefaultHandler::startDTD(*name, *publicId, *systemId);
}

//  bool QXmlDefaultHandler::endDTD()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler6endDTDEv(QXmlDefaultHandler *self) {
  return self->QXmlDefaultHandler::endDTD();
}

//  bool QXmlDefaultHandler::startEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler11startEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->QXmlDefaultHandler::startEntity(*name);
}

//  bool QXmlDefaultHandler::endEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler9endEntityERK7QString(
    QXmlDefaultHandler *self,
    const QString *name) {
  return self->QXmlDefaultHandler::endEntity(*name);
}

//  bool QXmlDefaultHandler::startCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler10startCDATAEv(
    QXmlDefaultHandler *self) {
  return self->QXmlDefaultHandler::startCDATA();
}

//  bool QXmlDefaultHandler::endCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler8endCDATAEv(QXmlDefaultHandler *self) {
  return self->QXmlDefaultHandler::endCDATA();
}

//  bool QXmlDefaultHandler::comment(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler7commentERK7QString(
    QXmlDefaultHandler *self,
    const QString *ch) {
  return self->QXmlDefaultHandler::comment(*ch);
}

//  bool QXmlDefaultHandler::attributeDecl(const QString &eName, const
//      QString &aName, const QString &type, const QString &valueDefault,
//      const QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler13attributeDeclERK7QStringS2_S2_S2_S2_(
    QXmlDefaultHandler *self,
    const QString *eName,
    const QString *aName,
    const QString *type,
    const QString *valueDefault,
    const QString *value) {
  return self->QXmlDefaultHandler::attributeDecl(
      *eName,
      *aName,
      *type,
      *valueDefault,
      *value);
}

//  bool QXmlDefaultHandler::internalEntityDecl(const QString &name, const
//      QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler18internalEntityDeclERK7QStringS2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *value) {
  return self->QXmlDefaultHandler::internalEntityDecl(*name, *value);
}

//  bool QXmlDefaultHandler::externalEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler18externalEntityDeclERK7QStringS2_S2_(
    QXmlDefaultHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->QXmlDefaultHandler::externalEntityDecl(
      *name,
      *publicId,
      *systemId);
}

//  QString QXmlDefaultHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QXmlDefaultHandler11errorStringEv(
    const QXmlDefaultHandler *self) {
  return new QString(self->QXmlDefaultHandler::errorString());
}

//  bool QXmlDefaultHandler::resolveEntity(const QString &publicId, const
//      QString &systemId, QXmlInputSource *&ret)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlDefaultHandler13resolveEntityERK7QStringS2_RP15QXmlInputSource(
    QXmlDefaultHandler *self,
    const QString *publicId,
    const QString *systemId,
    QXmlInputSource **ret) {
  return self->resolveEntity(*publicId, *systemId, *ret);
}

//  bool QXmlDefaultHandler::resolveEntity(const QString &publicId, const
//      QString &systemId, QXmlInputSource *&ret)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QXmlDefaultHandler13resolveEntityERK7QStringS2_RP15QXmlInputSource(
    QXmlDefaultHandler *self,
    const QString *publicId,
    const QString *systemId,
    QXmlInputSource **ret) {
  return self->QXmlDefaultHandler::resolveEntity(
      *publicId, *systemId, *ret);
}
