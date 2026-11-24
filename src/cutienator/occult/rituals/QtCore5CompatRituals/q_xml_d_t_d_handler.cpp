//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlDTDHandler that Python can take functions over in. Every QXmlDTDHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQXmlDTDHandlerCall0)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDTDHandlerCall1)(const void *, const QString *, const QString *, const QString *, const QString *, int *);
typedef QString * (*CuteQXmlDTDHandlerCall2)(const void *, int *);
class CuteQXmlDTDHandler : public QXmlDTDHandler {
public:
  using QXmlDTDHandler::QXmlDTDHandler;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QXmlDTDHandler12notationDeclERK7QStringS2_S2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QXmlDTDHandler18unparsedEntityDeclERK7QStringS2_S2_S2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QXmlDTDHandler11errorStringEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QXmlDTDHandler::notationDecl(const QString &name, const QString
  //      &publicId, const QString &systemId)
  bool notationDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlDTDHandlerCall0 call = reinterpret_cast<CuteQXmlDTDHandlerCall0>(taken[0]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlDTDHandler::unparsedEntityDecl(const QString &name, const
  //      QString &publicId, const QString &systemId, const QString
  //      &notationName)
  bool unparsedEntityDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId,
      const QString &notationName) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlDTDHandlerCall1 call = reinterpret_cast<CuteQXmlDTDHandlerCall1>(taken[1]);
      bool given = call(this, &name, &publicId, &systemId, &notationName, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QXmlDTDHandler::errorString() const
  QString errorString() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlDTDHandlerCall2 call = reinterpret_cast<CuteQXmlDTDHandlerCall2>(taken[2]);
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

//  QXmlDTDHandler::~QXmlDTDHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXmlDTDHandlerD1Ev(QXmlDTDHandler *self) {
  delete self;
}

//  bool QXmlDTDHandler::notationDecl(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QXmlDTDHandler12notationDeclERK7QStringS2_S2_(
    QXmlDTDHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->notationDecl(*name, *publicId, *systemId);
}

//  bool QXmlDTDHandler::unparsedEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId, const QString
//      &notationName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QXmlDTDHandler18unparsedEntityDeclERK7QStringS2_S2_S2_(
    QXmlDTDHandler *self,
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

//  QString QXmlDTDHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlDTDHandler11errorStringEv(
    const QXmlDTDHandler *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlDTDHandler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlDTDHandler(
    QXmlDTDHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlDTDHandler *>(self)->take(key, call);
}
