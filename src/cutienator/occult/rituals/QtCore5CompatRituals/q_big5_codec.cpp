//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbig5codec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbig5codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbig5codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 17, as _ZN10QBig5Codec5_nameEv
inline QByteArray QBig5Codec::_name()
{
    return "Big5";
}

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 1765, as _ZN10QBig5Codec8_aliasesEv
inline QList<QByteArray> QBig5Codec::_aliases()
{
    QList<QByteArray> aliases;
    aliases += "Big5-ETen";
    aliases += "CP950";
    return aliases;
}

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 12, as _ZN10QBig5Codec8_mibEnumEv
inline int QBig5Codec::_mibEnum()
{
    return 2026;
}
//  -----------------------------------------------------------------------

//  A QBig5Codec that Python can take functions over in. Every QBig5Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQBig5CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQBig5CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQBig5Codec : public QBig5Codec {
public:
  using QBig5Codec::QBig5Codec;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QBig5Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBig5CodecCall0 call = reinterpret_cast<CuteQBig5CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBig5Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QBig5Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBig5CodecCall1 call = reinterpret_cast<CuteQBig5CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBig5Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QBig5Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QBig5Codec5_nameEv() {
  return new QByteArray(QBig5Codec::_name());
}

//  QList<QByteArray> QBig5Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN10QBig5Codec8_aliasesEv() {
  return new QList<QByteArray>(QBig5Codec::_aliases());
}

//  int QBig5Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QBig5Codec8_mibEnumEv() {
  return QBig5Codec::_mibEnum();
}

//  QByteArray QBig5Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QBig5Codec4nameEv(const QBig5Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QBig5Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK10QBig5Codec7aliasesEv(const QBig5Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QBig5Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBig5Codec7mibEnumEv(const QBig5Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQBig5Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBig5Codec(QBig5Codec *self, const char *key, void *call) {
  return static_cast<CuteQBig5Codec *>(self)->take(key, call);
}

//  QByteArray QBig5Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QBig5Codec4nameEv(const QBig5Codec *self) {
  return new QByteArray(self->QBig5Codec::name());
}

//  int QBig5Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBig5Codec7mibEnumEv(const QBig5Codec *self) {
  return self->QBig5Codec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
