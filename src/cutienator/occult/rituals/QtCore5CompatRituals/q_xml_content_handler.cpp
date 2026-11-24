//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlContentHandler that Python can take functions over in. Every QXmlContentHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXmlContentHandlerCall0)(const void *, QXmlLocator *, int *);
typedef bool (*CuteQXmlContentHandlerCall1)(const void *, int *);
typedef bool (*CuteQXmlContentHandlerCall2)(const void *, int *);
typedef bool (*CuteQXmlContentHandlerCall3)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall4)(const void *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall5)(const void *, const QString *, const QString *, const QString *, const QXmlAttributes *, int *);
typedef bool (*CuteQXmlContentHandlerCall6)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall7)(const void *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall8)(const void *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall9)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlContentHandlerCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQXmlContentHandlerCall11)(const void *, int *);
class CuteQXmlContentHandler : public QXmlContentHandler {
public:
  using QXmlContentHandler::QXmlContentHandler;
  void *taken[12] = {};

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
    if (!std::strcmp(key, "_ZNK18QXmlContentHandler11errorStringEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  void QXmlContentHandler::setDocumentLocator(QXmlLocator *locator)
  void setDocumentLocator(QXmlLocator *locator) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlContentHandlerCall0 call = reinterpret_cast<CuteQXmlContentHandlerCall0>(taken[0]);
      call(this, locator, &handled);
      if (handled) return;
    }
  }

  //  bool QXmlContentHandler::startDocument()
  bool startDocument() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlContentHandlerCall1 call = reinterpret_cast<CuteQXmlContentHandlerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::endDocument()
  bool endDocument() override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlContentHandlerCall2 call = reinterpret_cast<CuteQXmlContentHandlerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::startPrefixMapping(const QString &prefix,
  //      const QString &uri)
  bool startPrefixMapping(
      const QString &prefix,
      const QString &uri) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlContentHandlerCall3 call = reinterpret_cast<CuteQXmlContentHandlerCall3>(taken[3]);
      bool given = call(this, &prefix, &uri, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::endPrefixMapping(const QString &prefix)
  bool endPrefixMapping(const QString &prefix) override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlContentHandlerCall4 call = reinterpret_cast<CuteQXmlContentHandlerCall4>(taken[4]);
      bool given = call(this, &prefix, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::startElement(const QString &namespaceURI,
  //      const QString &localName, const QString &qName, const
  //      QXmlAttributes &atts)
  bool startElement(
      const QString &namespaceURI,
      const QString &localName,
      const QString &qName,
      const QXmlAttributes &atts) override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlContentHandlerCall5 call = reinterpret_cast<CuteQXmlContentHandlerCall5>(taken[5]);
      bool given = call(this, &namespaceURI, &localName, &qName, &atts, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::endElement(const QString &namespaceURI,
  //      const QString &localName, const QString &qName)
  bool endElement(
      const QString &namespaceURI,
      const QString &localName,
      const QString &qName) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlContentHandlerCall6 call = reinterpret_cast<CuteQXmlContentHandlerCall6>(taken[6]);
      bool given = call(this, &namespaceURI, &localName, &qName, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::characters(const QString &ch)
  bool characters(const QString &ch) override {
    if (taken[7]) {
      int handled = 0;
      CuteQXmlContentHandlerCall7 call = reinterpret_cast<CuteQXmlContentHandlerCall7>(taken[7]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::ignorableWhitespace(const QString &ch)
  bool ignorableWhitespace(const QString &ch) override {
    if (taken[8]) {
      int handled = 0;
      CuteQXmlContentHandlerCall8 call = reinterpret_cast<CuteQXmlContentHandlerCall8>(taken[8]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::processingInstruction(const QString &target,
  //      const QString &data)
  bool processingInstruction(
      const QString &target,
      const QString &data) override {
    if (taken[9]) {
      int handled = 0;
      CuteQXmlContentHandlerCall9 call = reinterpret_cast<CuteQXmlContentHandlerCall9>(taken[9]);
      bool given = call(this, &target, &data, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlContentHandler::skippedEntity(const QString &name)
  bool skippedEntity(const QString &name) override {
    if (taken[10]) {
      int handled = 0;
      CuteQXmlContentHandlerCall10 call = reinterpret_cast<CuteQXmlContentHandlerCall10>(taken[10]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QXmlContentHandler::errorString() const
  QString errorString() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQXmlContentHandlerCall11 call = reinterpret_cast<CuteQXmlContentHandlerCall11>(taken[11]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QXmlContentHandler::~QXmlContentHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlContentHandlerD1Ev(QXmlContentHandler *self) {
  delete self;
}

//  void QXmlContentHandler::setDocumentLocator(QXmlLocator *locator)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlContentHandler18setDocumentLocatorEP11QXmlLocator(
    QXmlContentHandler *self,
    QXmlLocator *locator) {
  self->setDocumentLocator(locator);
}

//  bool QXmlContentHandler::startDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler13startDocumentEv(
    QXmlContentHandler *self) {
  return self->startDocument();
}

//  bool QXmlContentHandler::endDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler11endDocumentEv(QXmlContentHandler *self) {
  return self->endDocument();
}

//  bool QXmlContentHandler::startPrefixMapping(const QString &prefix, const
//      QString &uri)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler18startPrefixMappingERK7QStringS2_(
    QXmlContentHandler *self,
    const QString *prefix,
    const QString *uri) {
  return self->startPrefixMapping(*prefix, *uri);
}

//  bool QXmlContentHandler::endPrefixMapping(const QString &prefix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler16endPrefixMappingERK7QString(
    QXmlContentHandler *self,
    const QString *prefix) {
  return self->endPrefixMapping(*prefix);
}

//  bool QXmlContentHandler::startElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName, const QXmlAttributes &atts)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler12startElementERK7QStringS2_S2_RK14QXmlAttributes(
    QXmlContentHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName,
    const QXmlAttributes *atts) {
  return self->startElement(*namespaceURI, *localName, *qName, *atts);
}

//  bool QXmlContentHandler::endElement(const QString &namespaceURI, const
//      QString &localName, const QString &qName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler10endElementERK7QStringS2_S2_(
    QXmlContentHandler *self,
    const QString *namespaceURI,
    const QString *localName,
    const QString *qName) {
  return self->endElement(*namespaceURI, *localName, *qName);
}

//  bool QXmlContentHandler::characters(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler10charactersERK7QString(
    QXmlContentHandler *self,
    const QString *ch) {
  return self->characters(*ch);
}

//  bool QXmlContentHandler::ignorableWhitespace(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler19ignorableWhitespaceERK7QString(
    QXmlContentHandler *self,
    const QString *ch) {
  return self->ignorableWhitespace(*ch);
}

//  bool QXmlContentHandler::processingInstruction(const QString &target,
//      const QString &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler21processingInstructionERK7QStringS2_(
    QXmlContentHandler *self,
    const QString *target,
    const QString *data) {
  return self->processingInstruction(*target, *data);
}

//  bool QXmlContentHandler::skippedEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlContentHandler13skippedEntityERK7QString(
    QXmlContentHandler *self,
    const QString *name) {
  return self->skippedEntity(*name);
}

//  QString QXmlContentHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlContentHandler11errorStringEv(
    const QXmlContentHandler *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlContentHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlContentHandler(
    QXmlContentHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlContentHandler *>(self)->take(key, call);
}
