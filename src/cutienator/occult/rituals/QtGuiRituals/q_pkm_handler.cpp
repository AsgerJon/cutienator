//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpkmhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpkmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpkmhandler_p.h"
#include "qtexturefiledata_p.h"
#include <QFile>
#include <QDebug>
#include <QSize>
#include <qendian.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qpkmhandler.cpp, line 35, as _ZN11QPkmHandler7canReadERK10QByteArrayS2_
inline bool QPkmHandler::canRead(const QByteArray &suffix, const QByteArray &block)
{
    Q_UNUSED(suffix);

    return block.startsWith("PKM ");
}
//  -----------------------------------------------------------------------

//  A QPkmHandler that Python can take functions over in. Every QPkmHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QTextureFileData * (*CuteQPkmHandlerCall0)(const void *, int *);
class CuteQPkmHandler : public QPkmHandler {
public:
  using QPkmHandler::QPkmHandler;
  CuteQPkmHandler(const QPkmHandler &other) : QPkmHandler(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QTextureFileHandler4readEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QTextureFileData QPkmHandler::read()
  QTextureFileData read() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPkmHandlerCall0 call = reinterpret_cast<CuteQPkmHandlerCall0>(taken[0]);
      const QTextureFileData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPkmHandler::read();
  }
};

//  bool QPkmHandler::canRead(const QByteArray &suffix, const QByteArray
//      &block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPkmHandler7canReadERK10QByteArrayS2_(
    const QByteArray *suffix,
    const QByteArray *block) {
  return QPkmHandler::canRead(*suffix, *block);
}

//  a Python function taken by a CuteQPkmHandler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPkmHandler(
    QPkmHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPkmHandler *>(self)->take(key, call);
}
