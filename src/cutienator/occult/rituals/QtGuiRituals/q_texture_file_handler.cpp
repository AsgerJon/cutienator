//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexturefilehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefilehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qtexturefilereader_p.h>
#include <QtGui/private/qpkmhandler_p.h>
#include <QtGui/private/qktxhandler_p.h>
#include <QtGui/private/qastchandler_p.h>
#include <QtCore/QFileInfo>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qtexturefilereader.cpp, line 15, as _ZN19QTextureFileHandlerD2Ev
inline QTextureFileHandler::~QTextureFileHandler() = default;
//  -----------------------------------------------------------------------

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

//  QTextureFileHandler::QTextureFileHandler(QIODevice *device, const
//      QByteArray &logName)
extern "C" Q_DECL_EXPORT
QTextureFileHandler *ritual_ZN19QTextureFileHandlerC1EP9QIODeviceRK10QByteArray(
    QIODevice *device,
    const QByteArray *logName) {
  return new CuteQTextureFileHandler(device, *logName);
}

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
