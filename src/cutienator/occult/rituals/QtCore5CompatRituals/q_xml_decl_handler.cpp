//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlDeclHandler that Python can take functions over in. Every QXmlDeclHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQXmlDeclHandlerCall0)(const void *, const QString *, const QString *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDeclHandlerCall1)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlDeclHandlerCall2)(const void *, const QString *, const QString *, const QString *, int *);
typedef QString * (*CuteQXmlDeclHandlerCall3)(const void *, int *);
class CuteQXmlDeclHandler : public QXmlDeclHandler {
public:
  using QXmlDeclHandler::QXmlDeclHandler;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler13attributeDeclERK7QStringS2_S2_S2_S2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler18internalEntityDeclERK7QStringS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlDeclHandler18externalEntityDeclERK7QStringS2_S2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QXmlDeclHandler11errorStringEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QXmlDeclHandler::attributeDecl(const QString &eName, const
  //      QString &aName, const QString &type, const QString &valueDefault,
  //      const QString &value)
  bool attributeDecl(
      const QString &eName,
      const QString &aName,
      const QString &type,
      const QString &valueDefault,
      const QString &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlDeclHandlerCall0 call = reinterpret_cast<CuteQXmlDeclHandlerCall0>(taken[0]);
      bool given = call(this, &eName, &aName, &type, &valueDefault, &value, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlDeclHandler::internalEntityDecl(const QString &name, const
  //      QString &value)
  bool internalEntityDecl(
      const QString &name,
      const QString &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlDeclHandlerCall1 call = reinterpret_cast<CuteQXmlDeclHandlerCall1>(taken[1]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlDeclHandler::externalEntityDecl(const QString &name, const
  //      QString &publicId, const QString &systemId)
  bool externalEntityDecl(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlDeclHandlerCall2 call = reinterpret_cast<CuteQXmlDeclHandlerCall2>(taken[2]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QXmlDeclHandler::errorString() const
  QString errorString() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlDeclHandlerCall3 call = reinterpret_cast<CuteQXmlDeclHandlerCall3>(taken[3]);
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

//  QXmlDeclHandler::~QXmlDeclHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlDeclHandlerD1Ev(QXmlDeclHandler *self) {
  delete self;
}

//  bool QXmlDeclHandler::attributeDecl(const QString &eName, const QString
//      &aName, const QString &type, const QString &valueDefault, const
//      QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QXmlDeclHandler13attributeDeclERK7QStringS2_S2_S2_S2_(
    QXmlDeclHandler *self,
    const QString *eName,
    const QString *aName,
    const QString *type,
    const QString *valueDefault,
    const QString *value) {
  return self->attributeDecl(*eName, *aName, *type, *valueDefault, *value);
}

//  bool QXmlDeclHandler::internalEntityDecl(const QString &name, const
//      QString &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QXmlDeclHandler18internalEntityDeclERK7QStringS2_(
    QXmlDeclHandler *self,
    const QString *name,
    const QString *value) {
  return self->internalEntityDecl(*name, *value);
}

//  bool QXmlDeclHandler::externalEntityDecl(const QString &name, const
//      QString &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QXmlDeclHandler18externalEntityDeclERK7QStringS2_S2_(
    QXmlDeclHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->externalEntityDecl(*name, *publicId, *systemId);
}

//  QString QXmlDeclHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QXmlDeclHandler11errorStringEv(
    const QXmlDeclHandler *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlDeclHandler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlDeclHandler(
    QXmlDeclHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlDeclHandler *>(self)->take(key, call);
}
