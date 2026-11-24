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

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 26, as _ZN13QGb18030CodecC1Ev
inline QGb18030Codec::QGb18030Codec()
{
}
//  -----------------------------------------------------------------------

//  A QGb18030Codec that Python can take functions over in. Every QGb18030Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb18030CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQGb18030CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQGb18030Codec : public QGb18030Codec {
public:
  using QGb18030Codec::QGb18030Codec;
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
  //  QByteArray QGb18030Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGb18030CodecCall0 call = reinterpret_cast<CuteQGb18030CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGb18030Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QGb18030Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGb18030CodecCall1 call = reinterpret_cast<CuteQGb18030CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGb18030Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QGb18030Codec::QGb18030Codec()
extern "C" Q_DECL_EXPORT
QGb18030Codec *ritual_ZN13QGb18030CodecC1Ev() {
  return new CuteQGb18030Codec();
}

//  QByteArray QGb18030Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN13QGb18030Codec5_nameEv() {
  return new QByteArray(QGb18030Codec::_name());
}

//  QList<QByteArray> QGb18030Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN13QGb18030Codec8_aliasesEv() {
  return new QList<QByteArray>(QGb18030Codec::_aliases());
}

//  int QGb18030Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN13QGb18030Codec8_mibEnumEv() {
  return QGb18030Codec::_mibEnum();
}

//  QByteArray QGb18030Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QGb18030Codec4nameEv(const QGb18030Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QGb18030Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QGb18030Codec7aliasesEv(
    const QGb18030Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QGb18030Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGb18030Codec7mibEnumEv(const QGb18030Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQGb18030Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGb18030Codec(
    QGb18030Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGb18030Codec *>(self)->take(key, call);
}

//  QByteArray QGb18030Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QGb18030Codec4nameEv(const QGb18030Codec *self) {
  return new QByteArray(self->QGb18030Codec::name());
}

//  int QGb18030Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QGb18030Codec7mibEnumEv(const QGb18030Codec *self) {
  return self->QGb18030Codec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
