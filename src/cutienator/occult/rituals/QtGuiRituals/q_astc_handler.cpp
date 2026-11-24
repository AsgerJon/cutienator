//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qastchandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qastchandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qastchandler_p.h>
#include <QtGui/private/qtexturefiledata_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QSize>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qastchandler.cpp, line 29, as _ZN12QAstcHandler7canReadERK10QByteArrayS2_
inline bool QAstcHandler::canRead(const QByteArray &suffix, const QByteArray &block)
{
    Q_UNUSED(suffix);

    return block.startsWith("\x13\xAB\xA1\x5C");
}

//  from src/gui/util/qastchandler.cpp, line 36, as _ZNK12QAstcHandler12astcGLFormatEhh
inline quint32 QAstcHandler::astcGLFormat(quint8 xBlockDim, quint8 yBlockDim) const
{
    static const quint32 glFormatRGBABase = 0x93B0;    // GL_COMPRESSED_RGBA_ASTC_4x4_KHR
    static const quint32 glFormatSRGBBase = 0x93D0;    // GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR

    Q_CONSTINIT static QSize dims[14] = {
        {  4, 4  },     // GL_COMPRESSED_xxx_ASTC_4x4_KHR
        {  5, 4  },     // GL_COMPRESSED_xxx_ASTC_5x4_KHR
        {  5, 5  },     // GL_COMPRESSED_xxx_ASTC_5x5_KHR
        {  6, 5  },     // GL_COMPRESSED_xxx_ASTC_6x5_KHR
        {  6, 6  },     // GL_COMPRESSED_xxx_ASTC_6x6_KHR
        {  8, 5  },     // GL_COMPRESSED_xxx_ASTC_8x5_KHR
        {  8, 6  },     // GL_COMPRESSED_xxx_ASTC_8x6_KHR
        {  8, 8  },     // GL_COMPRESSED_xxx_ASTC_8x8_KHR
        { 10, 5  },     // GL_COMPRESSED_xxx_ASTC_10x5_KHR
        { 10, 6  },     // GL_COMPRESSED_xxx_ASTC_10x6_KHR
        { 10, 8  },     // GL_COMPRESSED_xxx_ASTC_10x8_KHR
        { 10, 10 },     // GL_COMPRESSED_xxx_ASTC_10x10_KHR
        { 12, 10 },     // GL_COMPRESSED_xxx_ASTC_12x10_KHR
        { 12, 12 }      // GL_COMPRESSED_xxx_ASTC_12x12_KHR
    };

    const QSize dim(xBlockDim, yBlockDim);
    int index = -1;
    for (int i = 0; i < 14; i++) {
        if (dim == dims[i]) {
            index = i;
            break;
        }
    }
    if (index < 0)
        return 0;

    bool useSrgb = qEnvironmentVariableIsSet("QT_ASTCHANDLER_USE_SRGB")
                   || logName().toLower().contains("srgb");

    return useSrgb ? (glFormatSRGBBase + index) : (glFormatRGBABase + index);
}
//  -----------------------------------------------------------------------

//  A QAstcHandler that Python can take functions over in. Every QAstcHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QTextureFileData * (*CuteQAstcHandlerCall0)(const void *, int *);
class CuteQAstcHandler : public QAstcHandler {
public:
  using QAstcHandler::QAstcHandler;
  CuteQAstcHandler(const QAstcHandler &other) : QAstcHandler(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QTextureFileHandler4readEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QTextureFileData QAstcHandler::read()
  QTextureFileData read() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAstcHandlerCall0 call = reinterpret_cast<CuteQAstcHandlerCall0>(taken[0]);
      const QTextureFileData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAstcHandler::read();
  }
};

//  bool QAstcHandler::canRead(const QByteArray &suffix, const QByteArray
//      &block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QAstcHandler7canReadERK10QByteArrayS2_(
    const QByteArray *suffix,
    const QByteArray *block) {
  return QAstcHandler::canRead(*suffix, *block);
}

//  quint32 QAstcHandler::astcGLFormat(quint8 xBlockDim, quint8 yBlockDim)
//      const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QAstcHandler12astcGLFormatEhh(
    const QAstcHandler *self,
    quint8 xBlockDim,
    quint8 yBlockDim) {
  return self->astcGLFormat(xBlockDim, yBlockDim);
}

//  a Python function taken by a CuteQAstcHandler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAstcHandler(
    QAstcHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAstcHandler *>(self)->take(key, call);
}
