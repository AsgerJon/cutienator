//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qktxhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qktxhandler_p.h>
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qktxhandler_p.h"
#include "qtexturefiledata_p.h"
#include <QtEndian>
#include <QSize>
#include <QMap>
#include <QtCore/qiodevice.h>
#ifdef KTX_DEBUG
#include <QDebug>
#include <QMetaEnum>
#include <QOpenGLTexture>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qktxhandler.cpp, line 352, as _ZNK11QKtxHandler6decodeEj
inline quint32 QKtxHandler::decode(quint32 val) const
{
    return inverseEndian ? qbswap<quint32>(val) : val;
}
//  -----------------------------------------------------------------------

//  A QKtxHandler that Python can take functions over in. Every QKtxHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QTextureFileData * (*CuteQKtxHandlerCall0)(const void *, int *);
class CuteQKtxHandler : public QKtxHandler {
public:
  using QKtxHandler::QKtxHandler;
  CuteQKtxHandler(const QKtxHandler &other) : QKtxHandler(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QTextureFileHandler4readEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QTextureFileData QKtxHandler::read()
  QTextureFileData read() override {
    if (taken[0]) {
      int handled = 0;
      CuteQKtxHandlerCall0 call = reinterpret_cast<CuteQKtxHandlerCall0>(taken[0]);
      const QTextureFileData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QKtxHandler::read();
  }
};

//  quint32 QKtxHandler::decode(quint32 val) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK11QKtxHandler6decodeEj(
    const QKtxHandler *self,
    quint32 val) {
  return self->decode(val);
}

//  a Python function taken by a CuteQKtxHandler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKtxHandler(
    QKtxHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQKtxHandler *>(self)->take(key, call);
}
