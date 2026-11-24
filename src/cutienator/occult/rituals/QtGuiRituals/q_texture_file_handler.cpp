//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexturefilehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefilehandler_p.h>
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QTextureFileHandler that Python can take functions over in. Every QTextureFileHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QTextureFileData * (*CuteQTextureFileHandlerCall0)(const void *, int *);
class CuteQTextureFileHandler : public QTextureFileHandler {
public:
  using QTextureFileHandler::QTextureFileHandler;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QTextureFileHandler4readEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QTextureFileData QTextureFileHandler::read()
  QTextureFileData read() override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextureFileHandlerCall0 call = reinterpret_cast<CuteQTextureFileHandlerCall0>(taken[0]);
      const QTextureFileData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QTextureFileHandler::~QTextureFileHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextureFileHandlerD1Ev(QTextureFileHandler *self) {
  delete self;
}

//  QTextureFileData QTextureFileHandler::read()
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN19QTextureFileHandler4readEv(
    QTextureFileHandler *self) {
  return new QTextureFileData(self->read());
}

//  QIODevice *QTextureFileHandler::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK19QTextureFileHandler6deviceEv(
    const QTextureFileHandler *self) {
  return self->device();
}

//  QByteArray QTextureFileHandler::logName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QTextureFileHandler7logNameEv(
    const QTextureFileHandler *self) {
  return new QByteArray(self->logName());
}

//  a Python function taken by a CuteQTextureFileHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextureFileHandler(
    QTextureFileHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextureFileHandler *>(self)->take(key, call);
}
