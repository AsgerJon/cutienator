//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qgb18030codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 394, as _ZN12QGb2312CodecC1Ev
inline QGb2312Codec::QGb2312Codec()
    : QGb18030Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 404, as _ZN12QGb2312Codec5_nameEv
inline QByteArray QGb2312Codec::_name()
{
    return "GB2312";
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 399, as _ZN12QGb2312Codec8_mibEnumEv
inline int QGb2312Codec::_mibEnum()
{
    return 2025;
}
//  -----------------------------------------------------------------------

//  A QGb2312Codec that Python can take functions over in. Every QGb2312Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb2312CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQGb2312CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQGb2312Codec : public QGb2312Codec {
public:
  using QGb2312Codec::QGb2312Codec;
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
  //  QByteArray QGb2312Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGb2312CodecCall0 call = reinterpret_cast<CuteQGb2312CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGb2312Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QGb2312Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGb2312CodecCall1 call = reinterpret_cast<CuteQGb2312CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGb2312Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QGb2312Codec::QGb2312Codec()
extern "C" Q_DECL_EXPORT
QGb2312Codec *ritual_ZN12QGb2312CodecC1Ev() {
  return new CuteQGb2312Codec();
}

//  QByteArray QGb2312Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QGb2312Codec5_nameEv() {
  return new QByteArray(QGb2312Codec::_name());
}

//  QList<QByteArray> QGb2312Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN12QGb2312Codec8_aliasesEv() {
  return new QList<QByteArray>(QGb2312Codec::_aliases());
}

//  int QGb2312Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QGb2312Codec8_mibEnumEv() {
  return QGb2312Codec::_mibEnum();
}

//  QByteArray QGb2312Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QGb2312Codec4nameEv(const QGb2312Codec *self) {
  return new QByteArray(self->name());
}

//  int QGb2312Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGb2312Codec7mibEnumEv(const QGb2312Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQGb2312Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGb2312Codec(
    QGb2312Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGb2312Codec *>(self)->take(key, call);
}

//  QByteArray QGb2312Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QGb2312Codec4nameEv(const QGb2312Codec *self) {
  return new QByteArray(self->QGb2312Codec::name());
}

//  int QGb2312Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QGb2312Codec7mibEnumEv(const QGb2312Codec *self) {
  return self->QGb2312Codec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
