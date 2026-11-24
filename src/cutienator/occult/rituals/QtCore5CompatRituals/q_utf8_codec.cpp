//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qutfcodec_p.h"
#include "qlist.h"
#include "qendian.h"
#include "qchar.h"
#include "private/qsimd_p.h"
#include "private/qstringiterator_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 18, as _ZN10QUtf8CodecD1Ev
#if QT_CONFIG(textcodec)
inline QUtf8Codec::~QUtf8Codec()
{
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 46, as _ZNK10QUtf8Codec4nameEv
#if QT_CONFIG(textcodec)
inline QByteArray QUtf8Codec::name() const
{
    return "UTF-8";
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 51, as _ZNK10QUtf8Codec7mibEnumEv
#if QT_CONFIG(textcodec)
inline int QUtf8Codec::mibEnum() const
{
    return 106;
}
#endif  // QT_CONFIG(textcodec)
//  -----------------------------------------------------------------------

//  A QUtf8Codec that Python can take functions over in. Every QUtf8Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQUtf8CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQUtf8CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQUtf8Codec : public QUtf8Codec {
public:
  using QUtf8Codec::QUtf8Codec;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
  //  QByteArray QUtf8Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQUtf8CodecCall0 call = reinterpret_cast<CuteQUtf8CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QUtf8Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QUtf8Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUtf8CodecCall1 call = reinterpret_cast<CuteQUtf8CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUtf8Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QUtf8Codec::~QUtf8Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUtf8CodecD1Ev(QUtf8Codec *self) {
  delete self;
}

//  QByteArray QUtf8Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QUtf8Codec4nameEv(const QUtf8Codec *self) {
  return new QByteArray(self->name());
}

//  int QUtf8Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUtf8Codec7mibEnumEv(const QUtf8Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQUtf8Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUtf8Codec(QUtf8Codec *self, const char *key, void *call) {
  return static_cast<CuteQUtf8Codec *>(self)->take(key, call);
}

#if QT_CONFIG(textcodec)
//  QByteArray QUtf8Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QUtf8Codec4nameEv(const QUtf8Codec *self) {
  return new QByteArray(self->QUtf8Codec::name());
}
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
//  int QUtf8Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QUtf8Codec7mibEnumEv(const QUtf8Codec *self) {
  return self->QUtf8Codec::mibEnum();
}
#endif  // QT_CONFIG(textcodec)

#endif  // QT_CONFIG(textcodec)
