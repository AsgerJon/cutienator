//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlSimpleReader that Python can take functions over in. Every QXmlSimpleReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXmlSimpleReaderCall0)(const void *, const QString *, bool, int *);
typedef bool (*CuteQXmlSimpleReaderCall1)(const void *, const QString *, int *);
typedef bool (*CuteQXmlSimpleReaderCall2)(const void *, const QString *, int *);
typedef void (*CuteQXmlSimpleReaderCall3)(const void *, QXmlEntityResolver *, int *);
typedef void * (*CuteQXmlSimpleReaderCall4)(const void *, int *);
typedef void (*CuteQXmlSimpleReaderCall5)(const void *, QXmlDTDHandler *, int *);
typedef void * (*CuteQXmlSimpleReaderCall6)(const void *, int *);
typedef void (*CuteQXmlSimpleReaderCall7)(const void *, QXmlContentHandler *, int *);
typedef void * (*CuteQXmlSimpleReaderCall8)(const void *, int *);
typedef void (*CuteQXmlSimpleReaderCall9)(const void *, QXmlErrorHandler *, int *);
typedef void * (*CuteQXmlSimpleReaderCall10)(const void *, int *);
typedef void (*CuteQXmlSimpleReaderCall11)(const void *, QXmlLexicalHandler *, int *);
typedef void * (*CuteQXmlSimpleReaderCall12)(const void *, int *);
typedef void (*CuteQXmlSimpleReaderCall13)(const void *, QXmlDeclHandler *, int *);
typedef void * (*CuteQXmlSimpleReaderCall14)(const void *, int *);
typedef bool (*CuteQXmlSimpleReaderCall15)(const void *, const QXmlInputSource *, int *);
typedef bool (*CuteQXmlSimpleReaderCall16)(const void *, const QXmlInputSource *, int *);
typedef bool (*CuteQXmlSimpleReaderCall17)(const void *, const QXmlInputSource *, bool, int *);
typedef bool (*CuteQXmlSimpleReaderCall18)(const void *, int *);
class CuteQXmlSimpleReader : public QXmlSimpleReader {
public:
  using QXmlSimpleReader::QXmlSimpleReader;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QXmlReader10setFeatureERK7QStringb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader10hasFeatureERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader11hasPropertyERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setEntityResolverEP18QXmlEntityResolver")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14entityResolverEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader13setDTDHandlerEP14QXmlDTDHandler")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader10DTDHandlerEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setContentHandlerEP18QXmlContentHandler")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14contentHandlerEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader15setErrorHandlerEP16QXmlErrorHandler")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader12errorHandlerEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader17setLexicalHandlerEP18QXmlLexicalHandler")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader14lexicalHandlerEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader14setDeclHandlerEP15QXmlDeclHandler")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QXmlReader11declHandlerEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader5parseERK15QXmlInputSource")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QXmlReader5parseEPK15QXmlInputSource")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlSimpleReader13parseContinueEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  void QXmlSimpleReader::setFeature(const QString &name, bool value)
  void setFeature(const QString &name, bool value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall0 call = reinterpret_cast<CuteQXmlSimpleReaderCall0>(taken[0]);
      call(this, &name, value, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setFeature(name, value);
  }

  //  bool QXmlSimpleReader::hasFeature(const QString &name) const
  bool hasFeature(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall1 call = reinterpret_cast<CuteQXmlSimpleReaderCall1>(taken[1]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::hasFeature(name);
  }

  //  bool QXmlSimpleReader::hasProperty(const QString &name) const
  bool hasProperty(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall2 call = reinterpret_cast<CuteQXmlSimpleReaderCall2>(taken[2]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::hasProperty(name);
  }

  //  void QXmlSimpleReader::setEntityResolver(QXmlEntityResolver *handler)
  void setEntityResolver(QXmlEntityResolver *handler) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall3 call = reinterpret_cast<CuteQXmlSimpleReaderCall3>(taken[3]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setEntityResolver(handler);
  }

  //  QXmlEntityResolver *QXmlSimpleReader::entityResolver() const
  QXmlEntityResolver *entityResolver() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall4 call = reinterpret_cast<CuteQXmlSimpleReaderCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlEntityResolver *>(given);
    }
    return QXmlSimpleReader::entityResolver();
  }

  //  void QXmlSimpleReader::setDTDHandler(QXmlDTDHandler *handler)
  void setDTDHandler(QXmlDTDHandler *handler) override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall5 call = reinterpret_cast<CuteQXmlSimpleReaderCall5>(taken[5]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setDTDHandler(handler);
  }

  //  QXmlDTDHandler *QXmlSimpleReader::DTDHandler() const
  QXmlDTDHandler *DTDHandler() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall6 call = reinterpret_cast<CuteQXmlSimpleReaderCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlDTDHandler *>(given);
    }
    return QXmlSimpleReader::DTDHandler();
  }

  //  void QXmlSimpleReader::setContentHandler(QXmlContentHandler *handler)
  void setContentHandler(QXmlContentHandler *handler) override {
    if (taken[7]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall7 call = reinterpret_cast<CuteQXmlSimpleReaderCall7>(taken[7]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setContentHandler(handler);
  }

  //  QXmlContentHandler *QXmlSimpleReader::contentHandler() const
  QXmlContentHandler *contentHandler() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall8 call = reinterpret_cast<CuteQXmlSimpleReaderCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlContentHandler *>(given);
    }
    return QXmlSimpleReader::contentHandler();
  }

  //  void QXmlSimpleReader::setErrorHandler(QXmlErrorHandler *handler)
  void setErrorHandler(QXmlErrorHandler *handler) override {
    if (taken[9]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall9 call = reinterpret_cast<CuteQXmlSimpleReaderCall9>(taken[9]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setErrorHandler(handler);
  }

  //  QXmlErrorHandler *QXmlSimpleReader::errorHandler() const
  QXmlErrorHandler *errorHandler() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall10 call = reinterpret_cast<CuteQXmlSimpleReaderCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlErrorHandler *>(given);
    }
    return QXmlSimpleReader::errorHandler();
  }

  //  void QXmlSimpleReader::setLexicalHandler(QXmlLexicalHandler *handler)
  void setLexicalHandler(QXmlLexicalHandler *handler) override {
    if (taken[11]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall11 call = reinterpret_cast<CuteQXmlSimpleReaderCall11>(taken[11]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setLexicalHandler(handler);
  }

  //  QXmlLexicalHandler *QXmlSimpleReader::lexicalHandler() const
  QXmlLexicalHandler *lexicalHandler() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall12 call = reinterpret_cast<CuteQXmlSimpleReaderCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlLexicalHandler *>(given);
    }
    return QXmlSimpleReader::lexicalHandler();
  }

  //  void QXmlSimpleReader::setDeclHandler(QXmlDeclHandler *handler)
  void setDeclHandler(QXmlDeclHandler *handler) override {
    if (taken[13]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall13 call = reinterpret_cast<CuteQXmlSimpleReaderCall13>(taken[13]);
      call(this, handler, &handled);
      if (handled) return;
    }
    QXmlSimpleReader::setDeclHandler(handler);
  }

  //  QXmlDeclHandler *QXmlSimpleReader::declHandler() const
  QXmlDeclHandler *declHandler() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall14 call = reinterpret_cast<CuteQXmlSimpleReaderCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXmlDeclHandler *>(given);
    }
    return QXmlSimpleReader::declHandler();
  }

  //  bool QXmlSimpleReader::parse(const QXmlInputSource &input)
  bool parse(const QXmlInputSource &input) override {
    if (taken[15]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall15 call = reinterpret_cast<CuteQXmlSimpleReaderCall15>(taken[15]);
      bool given = call(this, &input, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::parse(input);
  }

  //  bool QXmlSimpleReader::parse(const QXmlInputSource *input)
  bool parse(const QXmlInputSource *input) override {
    if (taken[16]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall16 call = reinterpret_cast<CuteQXmlSimpleReaderCall16>(taken[16]);
      bool given = call(this, input, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::parse(input);
  }

  //  bool QXmlSimpleReader::parse(const QXmlInputSource *input, bool
  //      incremental)
  bool parse(const QXmlInputSource *input, bool incremental) override {
    if (taken[17]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall17 call = reinterpret_cast<CuteQXmlSimpleReaderCall17>(taken[17]);
      bool given = call(this, input, incremental, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::parse(input, incremental);
  }

  //  bool QXmlSimpleReader::parseContinue()
  bool parseContinue() override {
    if (taken[18]) {
      int handled = 0;
      CuteQXmlSimpleReaderCall18 call = reinterpret_cast<CuteQXmlSimpleReaderCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QXmlSimpleReader::parseContinue();
  }
};

//  QXmlSimpleReader::QXmlSimpleReader()
extern "C" Q_DECL_EXPORT
QXmlSimpleReader *ritual_ZN16QXmlSimpleReaderC1Ev() {
  return new CuteQXmlSimpleReader();
}

//  QXmlSimpleReader::~QXmlSimpleReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReaderD1Ev(QXmlSimpleReader *self) {
  delete self;
}

//  bool QXmlSimpleReader::feature(const QString &name, bool *ok) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlSimpleReader7featureERK7QStringPb(
    const QXmlSimpleReader *self,
    const QString *name,
    bool *ok) {
  return self->feature(*name, ok);
}

//  void QXmlSimpleReader::setFeature(const QString &name, bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader10setFeatureERK7QStringb(
    QXmlSimpleReader *self,
    const QString *name,
    bool value) {
  self->setFeature(*name, value);
}

//  bool QXmlSimpleReader::hasFeature(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlSimpleReader10hasFeatureERK7QString(
    const QXmlSimpleReader *self,
    const QString *name) {
  return self->hasFeature(*name);
}

//  bool QXmlSimpleReader::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QXmlSimpleReader11hasPropertyERK7QString(
    const QXmlSimpleReader *self,
    const QString *name) {
  return self->hasProperty(*name);
}

//  void QXmlSimpleReader::setEntityResolver(QXmlEntityResolver *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader17setEntityResolverEP18QXmlEntityResolver(
    QXmlSimpleReader *self,
    QXmlEntityResolver *handler) {
  self->setEntityResolver(handler);
}

//  QXmlEntityResolver *QXmlSimpleReader::entityResolver() const
extern "C" Q_DECL_EXPORT
QXmlEntityResolver *ritual_ZNK16QXmlSimpleReader14entityResolverEv(
    const QXmlSimpleReader *self) {
  return self->entityResolver();
}

//  void QXmlSimpleReader::setDTDHandler(QXmlDTDHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader13setDTDHandlerEP14QXmlDTDHandler(
    QXmlSimpleReader *self,
    QXmlDTDHandler *handler) {
  self->setDTDHandler(handler);
}

//  QXmlDTDHandler *QXmlSimpleReader::DTDHandler() const
extern "C" Q_DECL_EXPORT
QXmlDTDHandler *ritual_ZNK16QXmlSimpleReader10DTDHandlerEv(
    const QXmlSimpleReader *self) {
  return self->DTDHandler();
}

//  void QXmlSimpleReader::setContentHandler(QXmlContentHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader17setContentHandlerEP18QXmlContentHandler(
    QXmlSimpleReader *self,
    QXmlContentHandler *handler) {
  self->setContentHandler(handler);
}

//  QXmlContentHandler *QXmlSimpleReader::contentHandler() const
extern "C" Q_DECL_EXPORT
QXmlContentHandler *ritual_ZNK16QXmlSimpleReader14contentHandlerEv(
    const QXmlSimpleReader *self) {
  return self->contentHandler();
}

//  void QXmlSimpleReader::setErrorHandler(QXmlErrorHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader15setErrorHandlerEP16QXmlErrorHandler(
    QXmlSimpleReader *self,
    QXmlErrorHandler *handler) {
  self->setErrorHandler(handler);
}

//  QXmlErrorHandler *QXmlSimpleReader::errorHandler() const
extern "C" Q_DECL_EXPORT
QXmlErrorHandler *ritual_ZNK16QXmlSimpleReader12errorHandlerEv(
    const QXmlSimpleReader *self) {
  return self->errorHandler();
}

//  void QXmlSimpleReader::setLexicalHandler(QXmlLexicalHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader17setLexicalHandlerEP18QXmlLexicalHandler(
    QXmlSimpleReader *self,
    QXmlLexicalHandler *handler) {
  self->setLexicalHandler(handler);
}

//  QXmlLexicalHandler *QXmlSimpleReader::lexicalHandler() const
extern "C" Q_DECL_EXPORT
QXmlLexicalHandler *ritual_ZNK16QXmlSimpleReader14lexicalHandlerEv(
    const QXmlSimpleReader *self) {
  return self->lexicalHandler();
}

//  void QXmlSimpleReader::setDeclHandler(QXmlDeclHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlSimpleReader14setDeclHandlerEP15QXmlDeclHandler(
    QXmlSimpleReader *self,
    QXmlDeclHandler *handler) {
  self->setDeclHandler(handler);
}

//  QXmlDeclHandler *QXmlSimpleReader::declHandler() const
extern "C" Q_DECL_EXPORT
QXmlDeclHandler *ritual_ZNK16QXmlSimpleReader11declHandlerEv(
    const QXmlSimpleReader *self) {
  return self->declHandler();
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource &input)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlSimpleReader5parseERK15QXmlInputSource(
    QXmlSimpleReader *self,
    const QXmlInputSource *input) {
  return self->parse(*input);
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource *input)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlSimpleReader5parseEPK15QXmlInputSource(
    QXmlSimpleReader *self,
    const QXmlInputSource *input) {
  return self->parse(input);
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource *input, bool
//      incremental)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb(
    QXmlSimpleReader *self,
    const QXmlInputSource *input,
    bool incremental) {
  return self->parse(input, incremental);
}

//  bool QXmlSimpleReader::parseContinue()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlSimpleReader13parseContinueEv(QXmlSimpleReader *self) {
  return self->parseContinue();
}

//  QXmlSimpleReaderPrivate *QXmlSimpleReader::d_func()
extern "C" Q_DECL_EXPORT
QXmlSimpleReaderPrivate *ritual_ZN16QXmlSimpleReader6d_funcEv(
    QXmlSimpleReader *self) {
  return self->d_func();
}

//  const QXmlSimpleReaderPrivate *QXmlSimpleReader::d_func() const
extern "C" Q_DECL_EXPORT
const QXmlSimpleReaderPrivate *ritual_ZNK16QXmlSimpleReader6d_funcEv(
    const QXmlSimpleReader *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQXmlSimpleReader, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlSimpleReader(
    QXmlSimpleReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlSimpleReader *>(self)->take(key, call);
}

//  void QXmlSimpleReader::setFeature(const QString &name, bool value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader10setFeatureERK7QStringb(
    QXmlSimpleReader *self,
    const QString *name,
    bool value) {
  self->QXmlSimpleReader::setFeature(*name, value);
}

//  bool QXmlSimpleReader::hasFeature(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QXmlSimpleReader10hasFeatureERK7QString(
    const QXmlSimpleReader *self,
    const QString *name) {
  return self->QXmlSimpleReader::hasFeature(*name);
}

//  bool QXmlSimpleReader::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QXmlSimpleReader11hasPropertyERK7QString(
    const QXmlSimpleReader *self,
    const QString *name) {
  return self->QXmlSimpleReader::hasProperty(*name);
}

//  void QXmlSimpleReader::setEntityResolver(QXmlEntityResolver *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader17setEntityResolverEP18QXmlEntityResolver(
    QXmlSimpleReader *self,
    QXmlEntityResolver *handler) {
  self->QXmlSimpleReader::setEntityResolver(handler);
}

//  QXmlEntityResolver *QXmlSimpleReader::entityResolver() const
extern "C" Q_DECL_EXPORT
QXmlEntityResolver *ritual_own_ZNK16QXmlSimpleReader14entityResolverEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::entityResolver();
}

//  void QXmlSimpleReader::setDTDHandler(QXmlDTDHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader13setDTDHandlerEP14QXmlDTDHandler(
    QXmlSimpleReader *self,
    QXmlDTDHandler *handler) {
  self->QXmlSimpleReader::setDTDHandler(handler);
}

//  QXmlDTDHandler *QXmlSimpleReader::DTDHandler() const
extern "C" Q_DECL_EXPORT
QXmlDTDHandler *ritual_own_ZNK16QXmlSimpleReader10DTDHandlerEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::DTDHandler();
}

//  void QXmlSimpleReader::setContentHandler(QXmlContentHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader17setContentHandlerEP18QXmlContentHandler(
    QXmlSimpleReader *self,
    QXmlContentHandler *handler) {
  self->QXmlSimpleReader::setContentHandler(handler);
}

//  QXmlContentHandler *QXmlSimpleReader::contentHandler() const
extern "C" Q_DECL_EXPORT
QXmlContentHandler *ritual_own_ZNK16QXmlSimpleReader14contentHandlerEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::contentHandler();
}

//  void QXmlSimpleReader::setErrorHandler(QXmlErrorHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader15setErrorHandlerEP16QXmlErrorHandler(
    QXmlSimpleReader *self,
    QXmlErrorHandler *handler) {
  self->QXmlSimpleReader::setErrorHandler(handler);
}

//  QXmlErrorHandler *QXmlSimpleReader::errorHandler() const
extern "C" Q_DECL_EXPORT
QXmlErrorHandler *ritual_own_ZNK16QXmlSimpleReader12errorHandlerEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::errorHandler();
}

//  void QXmlSimpleReader::setLexicalHandler(QXmlLexicalHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader17setLexicalHandlerEP18QXmlLexicalHandler(
    QXmlSimpleReader *self,
    QXmlLexicalHandler *handler) {
  self->QXmlSimpleReader::setLexicalHandler(handler);
}

//  QXmlLexicalHandler *QXmlSimpleReader::lexicalHandler() const
extern "C" Q_DECL_EXPORT
QXmlLexicalHandler *ritual_own_ZNK16QXmlSimpleReader14lexicalHandlerEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::lexicalHandler();
}

//  void QXmlSimpleReader::setDeclHandler(QXmlDeclHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXmlSimpleReader14setDeclHandlerEP15QXmlDeclHandler(
    QXmlSimpleReader *self,
    QXmlDeclHandler *handler) {
  self->QXmlSimpleReader::setDeclHandler(handler);
}

//  QXmlDeclHandler *QXmlSimpleReader::declHandler() const
extern "C" Q_DECL_EXPORT
QXmlDeclHandler *ritual_own_ZNK16QXmlSimpleReader11declHandlerEv(
    const QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::declHandler();
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource &input)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QXmlSimpleReader5parseERK15QXmlInputSource(
    QXmlSimpleReader *self,
    const QXmlInputSource *input) {
  return self->QXmlSimpleReader::parse(*input);
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource *input)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QXmlSimpleReader5parseEPK15QXmlInputSource(
    QXmlSimpleReader *self,
    const QXmlInputSource *input) {
  return self->QXmlSimpleReader::parse(input);
}

//  bool QXmlSimpleReader::parse(const QXmlInputSource *input, bool
//      incremental)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb(
    QXmlSimpleReader *self,
    const QXmlInputSource *input,
    bool incremental) {
  return self->QXmlSimpleReader::parse(input, incremental);
}

//  bool QXmlSimpleReader::parseContinue()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QXmlSimpleReader13parseContinueEv(
    QXmlSimpleReader *self) {
  return self->QXmlSimpleReader::parseContinue();
}
