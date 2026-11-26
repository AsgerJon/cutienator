//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qktxhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qktxhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <optional>
#include <QtCore/QMap>
#include <QtCore/QByteArray>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qktxhandler_p.h>
#include <QtGui/private/qtexturefiledata_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QSize>
#include <QtCore/QMap>
#include <QtCore/qiodevice.h>
#ifdef KTX_DEBUG
#include <QtCore/QDebug>
#include <QtCore/QMetaEnum>
#include <QOpenGLTexture>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/util/qktxhandler.cpp, line 23, as local:qktxhandler.cpp:KTX_IDENTIFIER_LENGTH
#define KTX_IDENTIFIER_LENGTH 12

//  from src/gui/util/qktxhandler.cpp, line 24, as local:qktxhandler.cpp:ktxIdentifier
static const char ktxIdentifier[KTX_IDENTIFIER_LENGTH] = { '\xAB', 'K', 'T', 'X', ' ', '1', '1', '\xBB', '\r', '\n', '\x1A', '\n' };

//  from src/gui/util/qktxhandler.cpp, line 87, as local:qktxhandler.cpp:safeView
static QByteArrayView safeView(QByteArrayView view, quint32 start, quint32 length)
{
    quint32 end = 0;
    if (qAddOverflow(start, length, &end) || end > quint32(view.length()))
        return {};
    return view.sliced(start, length);
}

//  from src/gui/util/qktxhandler.cpp, line 97, as _ZN11QKtxHandler7canReadERK10QByteArrayS2_
inline bool QKtxHandler::canRead(const QByteArray &suffix, const QByteArray &block)
{
    Q_UNUSED(suffix);
    return block.startsWith(ktxIdentifier);
}

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
  CuteQKtxHandler(const QKtxHandler & other) : QKtxHandler(other) {}
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

//  QKtxHandler::~QKtxHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QKtxHandlerD1Ev(QKtxHandler *self) {
  delete self;
}

//  bool QKtxHandler::canRead(const QByteArray &suffix, const QByteArray
//      &block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QKtxHandler7canReadERK10QByteArrayS2_(
    const QByteArray *suffix,
    const QByteArray *block) {
  return QKtxHandler::canRead(*suffix, *block);
}

//  QTextureFileData QKtxHandler::read()
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN11QKtxHandler4readEv(QKtxHandler *self) {
  return new QTextureFileData(self->read());
}

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

//  a std::optional<QMap<QByteArray, QByteArray>> a ritual of QKtxHandler
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QKtxHandler__std_optional_QMap_QByteArray_QByteArray(
    std::optional<QMap<QByteArray, QByteArray>> *self) {
  delete self;
}
