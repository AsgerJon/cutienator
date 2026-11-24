//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlLexicalHandler that Python can take functions over in. Every QXmlLexicalHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQXmlLexicalHandlerCall0)(const void *, const QString *, const QString *, const QString *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall1)(const void *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall2)(const void *, const QString *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall3)(const void *, const QString *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall4)(const void *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall5)(const void *, int *);
typedef bool (*CuteQXmlLexicalHandlerCall6)(const void *, const QString *, int *);
typedef QString * (*CuteQXmlLexicalHandlerCall7)(const void *, int *);
class CuteQXmlLexicalHandler : public QXmlLexicalHandler {
public:
  using QXmlLexicalHandler::QXmlLexicalHandler;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler8startDTDERK7QStringS2_S2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler6endDTDEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler11startEntityERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler9endEntityERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler10startCDATAEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler8endCDATAEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QXmlLexicalHandler7commentERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QXmlLexicalHandler11errorStringEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool QXmlLexicalHandler::startDTD(const QString &name, const QString
  //      &publicId, const QString &systemId)
  bool startDTD(
      const QString &name,
      const QString &publicId,
      const QString &systemId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall0 call = reinterpret_cast<CuteQXmlLexicalHandlerCall0>(taken[0]);
      bool given = call(this, &name, &publicId, &systemId, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::endDTD()
  bool endDTD() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall1 call = reinterpret_cast<CuteQXmlLexicalHandlerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::startEntity(const QString &name)
  bool startEntity(const QString &name) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall2 call = reinterpret_cast<CuteQXmlLexicalHandlerCall2>(taken[2]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::endEntity(const QString &name)
  bool endEntity(const QString &name) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall3 call = reinterpret_cast<CuteQXmlLexicalHandlerCall3>(taken[3]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::startCDATA()
  bool startCDATA() override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall4 call = reinterpret_cast<CuteQXmlLexicalHandlerCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::endCDATA()
  bool endCDATA() override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall5 call = reinterpret_cast<CuteQXmlLexicalHandlerCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlLexicalHandler::comment(const QString &ch)
  bool comment(const QString &ch) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall6 call = reinterpret_cast<CuteQXmlLexicalHandlerCall6>(taken[6]);
      bool given = call(this, &ch, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QXmlLexicalHandler::errorString() const
  QString errorString() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQXmlLexicalHandlerCall7 call = reinterpret_cast<CuteQXmlLexicalHandlerCall7>(taken[7]);
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

//  QXmlLexicalHandler::~QXmlLexicalHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlLexicalHandlerD1Ev(QXmlLexicalHandler *self) {
  delete self;
}

//  bool QXmlLexicalHandler::startDTD(const QString &name, const QString
//      &publicId, const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler8startDTDERK7QStringS2_S2_(
    QXmlLexicalHandler *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->startDTD(*name, *publicId, *systemId);
}

//  bool QXmlLexicalHandler::endDTD()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler6endDTDEv(QXmlLexicalHandler *self) {
  return self->endDTD();
}

//  bool QXmlLexicalHandler::startEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler11startEntityERK7QString(
    QXmlLexicalHandler *self,
    const QString *name) {
  return self->startEntity(*name);
}

//  bool QXmlLexicalHandler::endEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler9endEntityERK7QString(
    QXmlLexicalHandler *self,
    const QString *name) {
  return self->endEntity(*name);
}

//  bool QXmlLexicalHandler::startCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler10startCDATAEv(QXmlLexicalHandler *self) {
  return self->startCDATA();
}

//  bool QXmlLexicalHandler::endCDATA()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler8endCDATAEv(QXmlLexicalHandler *self) {
  return self->endCDATA();
}

//  bool QXmlLexicalHandler::comment(const QString &ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlLexicalHandler7commentERK7QString(
    QXmlLexicalHandler *self,
    const QString *ch) {
  return self->comment(*ch);
}

//  QString QXmlLexicalHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlLexicalHandler11errorStringEv(
    const QXmlLexicalHandler *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlLexicalHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlLexicalHandler(
    QXmlLexicalHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlLexicalHandler *>(self)->take(key, call);
}
