//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qlatincodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qlatincodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qlatincodec_p.h"
#include "qlist.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 63, as _ZN13QLatin15CodecD1Ev
inline QLatin15Codec::~QLatin15Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 180, as _ZNK13QLatin15Codec4nameEv
inline QByteArray QLatin15Codec::name() const
{
    return "ISO-8859-15";
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 185, as _ZNK13QLatin15Codec7aliasesEv
inline QList<QByteArray> QLatin15Codec::aliases() const
{
    QList<QByteArray> list;
    list << "latin9";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 192, as _ZNK13QLatin15Codec7mibEnumEv
inline int QLatin15Codec::mibEnum() const
{
    return 111;
}
//  -----------------------------------------------------------------------

//  A QLatin15Codec that Python can take functions over in. Every QLatin15Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin15CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQLatin15CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQLatin15Codec : public QLatin15Codec {
public:
  using QLatin15Codec::QLatin15Codec;
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
  //  QByteArray QLatin15Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLatin15CodecCall0 call = reinterpret_cast<CuteQLatin15CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLatin15Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QLatin15Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLatin15CodecCall1 call = reinterpret_cast<CuteQLatin15CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLatin15Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QLatin15Codec::~QLatin15Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLatin15CodecD1Ev(QLatin15Codec *self) {
  delete self;
}

//  QByteArray QLatin15Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QLatin15Codec4nameEv(const QLatin15Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QLatin15Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QLatin15Codec7aliasesEv(
    const QLatin15Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QLatin15Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin15Codec7mibEnumEv(const QLatin15Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQLatin15Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLatin15Codec(
    QLatin15Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLatin15Codec *>(self)->take(key, call);
}

//  QByteArray QLatin15Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QLatin15Codec4nameEv(const QLatin15Codec *self) {
  return new QByteArray(self->QLatin15Codec::name());
}

//  int QLatin15Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QLatin15Codec7mibEnumEv(const QLatin15Codec *self) {
  return self->QLatin15Codec::mibEnum();
}

#endif  // QT_CONFIG(textcodec)
