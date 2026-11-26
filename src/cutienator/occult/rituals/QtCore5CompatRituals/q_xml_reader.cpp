//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlReader that Python can take functions over in. Every QXmlReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXmlReaderCall0)(const void *, const QString *, bool, int *);
typedef bool (*CuteQXmlReaderCall1)(const void *, const QString *, int *);
typedef void (*CuteQXmlReaderCall2)(const void *, const QString *, void *, int *);
typedef bool (*CuteQXmlReaderCall3)(const void *, const QString *, int *);
typedef void (*CuteQXmlReaderCall4)(const void *, QXmlEntityResolver *, int *);
typedef void * (*CuteQXmlReaderCall5)(const void *, int *);
typedef void (*CuteQXmlReaderCall6)(const void *, QXmlDTDHandler *, int *);
typedef void * (*CuteQXmlReaderCall7)(const void *, int *);
typedef void (*CuteQXmlReaderCall8)(const void *, QXmlContentHandler *, int *);
typedef void * (*CuteQXmlReaderCall9)(const void *, int *);
typedef void (*CuteQXmlReaderCall10)(const void *, QXmlErrorHandler *, int *);
typedef void * (*CuteQXmlReaderCall11)(const void *, int *);
typedef void (*CuteQXmlReaderCall12)(const void *, QXmlLexicalHandler *, int *);
typedef void * (*CuteQXmlReaderCall13)(const void *, int *);
typedef void (*CuteQXmlReaderCall14)(const void *, QXmlDeclHandler *, int *);
typedef void * (*CuteQXmlReaderCall15)(const void *, int *);
typedef bool (*CuteQXmlReaderCall16)(const void *, const QXmlInputSource *, int *);
typedef bool (*CuteQXmlReaderCall17)(const void *, const QXmlInputSource *, int *);
class CuteQXmlReader : public QXmlReader {
public:
  using QXmlReader::QXmlReader;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QXmlReader10setFeatureERK7QStringb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader10hasFeatureERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader11setPropertyERK7QStringPv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader11hasPropertyERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setEntityResolverEP18QXmlEntityResolver")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14entityResolverEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader13setDTDHandlerEP14QXmlDTDHandler")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader10DTDHandlerEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setContentHandlerEP18QXmlContentHandler")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14contentHandlerEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader15setErrorHandlerEP16QXmlErrorHandler")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader12errorHandlerEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setLexicalHandlerEP18QXmlLexicalHandler")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14lexicalHandlerEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader14setDeclHandlerEP15QXmlDeclHandler")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader11declHandlerEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader5parseERK15QXmlInputSource")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader5parseEPK15QXmlInputSource")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QXmlReader::setFeature(const QString &name, bool value)
  void setFeature(const QString &name, bool value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlReaderCall0 call = reinterpret_cast<CuteQXmlReaderCall0>(taken[0]);
      call(this, &name, value, &handled);
      if (handled) return;
    }
  }

  //  bool QXmlReader::hasFeature(const QString &name) const
  bool hasFeature(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlReaderCall1 call = reinterpret_cast<CuteQXmlReaderCall1>(taken[1]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QXmlReader::setProperty(const QString &name, void *value)
  void setProperty(const QString &name, void *value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlReaderCall2 call = reinterpret_cast<CuteQXmlReaderCall2>(taken[2]);
      call(this, &name, value, &handled);
      if (handled) return;
    }
  }

  //  bool QXmlReader::hasProperty(const QString &name) const
  bool hasProperty(const QString &name) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlReaderCall3 call = reinterpret_cast<CuteQXmlReaderCall3>(taken[3]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QXmlReader::setEntityResolver(QXmlEntityResolver *handler)
  void setEntityResolver(QXmlEntityResolver *handler) override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlReaderCall4 call = reinterpret_cast<CuteQXmlReaderCall4>(taken[4]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlEntityResolver *QXmlReader::entityResolver() const
  QXmlEntityResolver *entityResolver() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlReaderCall5 call = reinterpret_cast<CuteQXmlReaderCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlEntityResolver *>(given);
    }
    return {};
  }

  //  void QXmlReader::setDTDHandler(QXmlDTDHandler *handler)
  void setDTDHandler(QXmlDTDHandler *handler) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlReaderCall6 call = reinterpret_cast<CuteQXmlReaderCall6>(taken[6]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlDTDHandler *QXmlReader::DTDHandler() const
  QXmlDTDHandler *DTDHandler() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQXmlReaderCall7 call = reinterpret_cast<CuteQXmlReaderCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlDTDHandler *>(given);
    }
    return {};
  }

  //  void QXmlReader::setContentHandler(QXmlContentHandler *handler)
  void setContentHandler(QXmlContentHandler *handler) override {
    if (taken[8]) {
      int handled = 0;
      CuteQXmlReaderCall8 call = reinterpret_cast<CuteQXmlReaderCall8>(taken[8]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlContentHandler *QXmlReader::contentHandler() const
  QXmlContentHandler *contentHandler() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQXmlReaderCall9 call = reinterpret_cast<CuteQXmlReaderCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlContentHandler *>(given);
    }
    return {};
  }

  //  void QXmlReader::setErrorHandler(QXmlErrorHandler *handler)
  void setErrorHandler(QXmlErrorHandler *handler) override {
    if (taken[10]) {
      int handled = 0;
      CuteQXmlReaderCall10 call = reinterpret_cast<CuteQXmlReaderCall10>(taken[10]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlErrorHandler *QXmlReader::errorHandler() const
  QXmlErrorHandler *errorHandler() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQXmlReaderCall11 call = reinterpret_cast<CuteQXmlReaderCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlErrorHandler *>(given);
    }
    return {};
  }

  //  void QXmlReader::setLexicalHandler(QXmlLexicalHandler *handler)
  void setLexicalHandler(QXmlLexicalHandler *handler) override {
    if (taken[12]) {
      int handled = 0;
      CuteQXmlReaderCall12 call = reinterpret_cast<CuteQXmlReaderCall12>(taken[12]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlLexicalHandler *QXmlReader::lexicalHandler() const
  QXmlLexicalHandler *lexicalHandler() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQXmlReaderCall13 call = reinterpret_cast<CuteQXmlReaderCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlLexicalHandler *>(given);
    }
    return {};
  }

  //  void QXmlReader::setDeclHandler(QXmlDeclHandler *handler)
  void setDeclHandler(QXmlDeclHandler *handler) override {
    if (taken[14]) {
      int handled = 0;
      CuteQXmlReaderCall14 call = reinterpret_cast<CuteQXmlReaderCall14>(taken[14]);
      call(this, handler, &handled);
      if (handled) return;
    }
  }

  //  QXmlDeclHandler *QXmlReader::declHandler() const
  QXmlDeclHandler *declHandler() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQXmlReaderCall15 call = reinterpret_cast<CuteQXmlReaderCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlDeclHandler *>(given);
    }
    return {};
  }

  //  bool QXmlReader::parse(const QXmlInputSource &input)
  bool parse(const QXmlInputSource &input) override {
    if (taken[16]) {
      int handled = 0;
      CuteQXmlReaderCall16 call = reinterpret_cast<CuteQXmlReaderCall16>(taken[16]);
      bool given = call(this, &input, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlReader::parse(const QXmlInputSource *input)
  bool parse(const QXmlInputSource *input) override {
    if (taken[17]) {
      int handled = 0;
      CuteQXmlReaderCall17 call = reinterpret_cast<CuteQXmlReaderCall17>(taken[17]);
      bool given = call(this, input, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QXmlReader::~QXmlReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReaderD1Ev(QXmlReader *self) {
  delete self;
}

//  bool QXmlReader::feature(const QString &name, bool *ok) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QXmlReader7featureERK7QStringPb(
    const QXmlReader *self,
    const QString *name,
    bool *ok) {
  return self->feature(*name, ok);
}

//  void QXmlReader::setFeature(const QString &name, bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader10setFeatureERK7QStringb(
    QXmlReader *self,
    const QString *name,
    bool value) {
  self->setFeature(*name, value);
}

//  bool QXmlReader::hasFeature(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QXmlReader10hasFeatureERK7QString(
    const QXmlReader *self,
    const QString *name) {
  return self->hasFeature(*name);
}

//  void *QXmlReader::property(const QString &name, bool *ok) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK10QXmlReader8propertyERK7QStringPb(
    const QXmlReader *self,
    const QString *name,
    bool *ok) {
  return self->property(*name, ok);
}

//  void QXmlReader::setProperty(const QString &name, void *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader11setPropertyERK7QStringPv(
    QXmlReader *self,
    const QString *name,
    void *value) {
  self->setProperty(*name, value);
}

//  bool QXmlReader::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QXmlReader11hasPropertyERK7QString(
    const QXmlReader *self,
    const QString *name) {
  return self->hasProperty(*name);
}

//  void QXmlReader::setEntityResolver(QXmlEntityResolver *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader17setEntityResolverEP18QXmlEntityResolver(
    QXmlReader *self,
    QXmlEntityResolver *handler) {
  self->setEntityResolver(handler);
}

//  QXmlEntityResolver *QXmlReader::entityResolver() const
extern "C" Q_DECL_EXPORT
QXmlEntityResolver *ritual_ZNK10QXmlReader14entityResolverEv(
    const QXmlReader *self) {
  return self->entityResolver();
}

//  void QXmlReader::setDTDHandler(QXmlDTDHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader13setDTDHandlerEP14QXmlDTDHandler(
    QXmlReader *self,
    QXmlDTDHandler *handler) {
  self->setDTDHandler(handler);
}

//  QXmlDTDHandler *QXmlReader::DTDHandler() const
extern "C" Q_DECL_EXPORT
QXmlDTDHandler *ritual_ZNK10QXmlReader10DTDHandlerEv(
    const QXmlReader *self) {
  return self->DTDHandler();
}

//  void QXmlReader::setContentHandler(QXmlContentHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader17setContentHandlerEP18QXmlContentHandler(
    QXmlReader *self,
    QXmlContentHandler *handler) {
  self->setContentHandler(handler);
}

//  QXmlContentHandler *QXmlReader::contentHandler() const
extern "C" Q_DECL_EXPORT
QXmlContentHandler *ritual_ZNK10QXmlReader14contentHandlerEv(
    const QXmlReader *self) {
  return self->contentHandler();
}

//  void QXmlReader::setErrorHandler(QXmlErrorHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader15setErrorHandlerEP16QXmlErrorHandler(
    QXmlReader *self,
    QXmlErrorHandler *handler) {
  self->setErrorHandler(handler);
}

//  QXmlErrorHandler *QXmlReader::errorHandler() const
extern "C" Q_DECL_EXPORT
QXmlErrorHandler *ritual_ZNK10QXmlReader12errorHandlerEv(
    const QXmlReader *self) {
  return self->errorHandler();
}

//  void QXmlReader::setLexicalHandler(QXmlLexicalHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader17setLexicalHandlerEP18QXmlLexicalHandler(
    QXmlReader *self,
    QXmlLexicalHandler *handler) {
  self->setLexicalHandler(handler);
}

//  QXmlLexicalHandler *QXmlReader::lexicalHandler() const
extern "C" Q_DECL_EXPORT
QXmlLexicalHandler *ritual_ZNK10QXmlReader14lexicalHandlerEv(
    const QXmlReader *self) {
  return self->lexicalHandler();
}

//  void QXmlReader::setDeclHandler(QXmlDeclHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXmlReader14setDeclHandlerEP15QXmlDeclHandler(
    QXmlReader *self,
    QXmlDeclHandler *handler) {
  self->setDeclHandler(handler);
}

//  QXmlDeclHandler *QXmlReader::declHandler() const
extern "C" Q_DECL_EXPORT
QXmlDeclHandler *ritual_ZNK10QXmlReader11declHandlerEv(
    const QXmlReader *self) {
  return self->declHandler();
}

//  bool QXmlReader::parse(const QXmlInputSource &input)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QXmlReader5parseERK15QXmlInputSource(
    QXmlReader *self,
    const QXmlInputSource *input) {
  return self->parse(*input);
}

//  bool QXmlReader::parse(const QXmlInputSource *input)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QXmlReader5parseEPK15QXmlInputSource(
    QXmlReader *self,
    const QXmlInputSource *input) {
  return self->parse(input);
}

//  a Python function taken by a CuteQXmlReader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlReader(QXmlReader *self, const char *key, void *call) {
  return static_cast<CuteQXmlReader *>(self)->take(key, call);
}
