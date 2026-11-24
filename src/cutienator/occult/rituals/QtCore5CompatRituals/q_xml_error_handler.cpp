//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlErrorHandler that Python can take functions over in. Every QXmlErrorHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQXmlErrorHandlerCall0)(const void *, const QXmlParseException *, int *);
typedef bool (*CuteQXmlErrorHandlerCall1)(const void *, const QXmlParseException *, int *);
typedef bool (*CuteQXmlErrorHandlerCall2)(const void *, const QXmlParseException *, int *);
typedef QString * (*CuteQXmlErrorHandlerCall3)(const void *, int *);
class CuteQXmlErrorHandler : public QXmlErrorHandler {
public:
  using QXmlErrorHandler::QXmlErrorHandler;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler7warningERK18QXmlParseException")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler5errorERK18QXmlParseException")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QXmlErrorHandler10fatalErrorERK18QXmlParseException")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QXmlErrorHandler11errorStringEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QXmlErrorHandler::warning(const QXmlParseException &exception)
  bool warning(const QXmlParseException &exception) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlErrorHandlerCall0 call = reinterpret_cast<CuteQXmlErrorHandlerCall0>(taken[0]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlErrorHandler::error(const QXmlParseException &exception)
  bool error(const QXmlParseException &exception) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlErrorHandlerCall1 call = reinterpret_cast<CuteQXmlErrorHandlerCall1>(taken[1]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QXmlErrorHandler::fatalError(const QXmlParseException
  //      &exception)
  bool fatalError(const QXmlParseException &exception) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlErrorHandlerCall2 call = reinterpret_cast<CuteQXmlErrorHandlerCall2>(taken[2]);
      bool given = call(this, &exception, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QXmlErrorHandler::errorString() const
  QString errorString() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlErrorHandlerCall3 call = reinterpret_cast<CuteQXmlErrorHandlerCall3>(taken[3]);
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

//  QXmlErrorHandler::~QXmlErrorHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXmlErrorHandlerD1Ev(QXmlErrorHandler *self) {
  delete self;
}

//  bool QXmlErrorHandler::warning(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlErrorHandler7warningERK18QXmlParseException(
    QXmlErrorHandler *self,
    const QXmlParseException *exception) {
  return self->warning(*exception);
}

//  bool QXmlErrorHandler::error(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlErrorHandler5errorERK18QXmlParseException(
    QXmlErrorHandler *self,
    const QXmlParseException *exception) {
  return self->error(*exception);
}

//  bool QXmlErrorHandler::fatalError(const QXmlParseException &exception)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXmlErrorHandler10fatalErrorERK18QXmlParseException(
    QXmlErrorHandler *self,
    const QXmlParseException *exception) {
  return self->fatalError(*exception);
}

//  QString QXmlErrorHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QXmlErrorHandler11errorStringEv(
    const QXmlErrorHandler *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlErrorHandler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlErrorHandler(
    QXmlErrorHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlErrorHandler *>(self)->take(key, call);
}
