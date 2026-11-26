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
#include <QtGui/private/qpkmhandler_p.h>
#include <QtGui/private/qtexturefiledata_p.h>
#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QSize>
#include <QtCore/qendian.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qpkmhandler.cpp, line 17, as local:qpkmhandler.cpp:qpkmh_headerSize
static const int qpkmh_headerSize = 16;

//  from src/gui/util/qpkmhandler.cpp, line 19, as local:qpkmhandler.cpp:PkmType
struct PkmType
{
    quint32 glFormat;
    quint32 bytesPerBlock;
};

//  from src/gui/util/qpkmhandler.cpp, line 25, as local:qpkmhandler.cpp:typeMap
static constexpr PkmType typeMap[5] = {
    { 0x8D64,  8 },   // GL_ETC1_RGB8_OES
    { 0x9274,  8 },   // GL_COMPRESSED_RGB8_ETC2
    { 0, 0 },         // unused (obsolete)
    { 0x9278, 16},    // GL_COMPRESSED_RGBA8_ETC2_EAC
    { 0x9276,  8 }    // GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2
};

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
  CuteQPkmHandler(const QPkmHandler & other) : QPkmHandler(other) {}
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

//  QPkmHandler::~QPkmHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPkmHandlerD1Ev(QPkmHandler *self) {
  delete self;
}

//  bool QPkmHandler::canRead(const QByteArray &suffix, const QByteArray
//      &block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPkmHandler7canReadERK10QByteArrayS2_(
    const QByteArray *suffix,
    const QByteArray *block) {
  return QPkmHandler::canRead(*suffix, *block);
}

//  QTextureFileData QPkmHandler::read()
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN11QPkmHandler4readEv(QPkmHandler *self) {
  return new QTextureFileData(self->read());
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
