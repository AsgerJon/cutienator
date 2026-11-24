//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qlatincodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
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
#include <QtCore5Compat/private/qlatincodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 10, as _ZN12QLatin1CodecD1Ev
inline QLatin1Codec::~QLatin1Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 40, as _ZNK12QLatin1Codec4nameEv
inline QByteArray QLatin1Codec::name() const
{
    return "ISO-8859-1";
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 45, as _ZNK12QLatin1Codec7aliasesEv
inline QList<QByteArray> QLatin1Codec::aliases() const
{
    QList<QByteArray> list;
    list << "latin1"
         << "CP819"
         << "IBM819"
         << "iso-ir-100"
         << "csISOLatin1";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 57, as _ZNK12QLatin1Codec7mibEnumEv
inline int QLatin1Codec::mibEnum() const
{
    return 4;
}
//  -----------------------------------------------------------------------

//  A QLatin1Codec that Python can take functions over in. Every QLatin1Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin1CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQLatin1CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQLatin1Codec : public QLatin1Codec {
public:
  using QLatin1Codec::QLatin1Codec;
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
  //  QByteArray QLatin1Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLatin1CodecCall0 call = reinterpret_cast<CuteQLatin1CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLatin1Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QLatin1Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLatin1CodecCall1 call = reinterpret_cast<CuteQLatin1CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLatin1Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QLatin1Codec::~QLatin1Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLatin1CodecD1Ev(QLatin1Codec *self) {
  delete self;
}

//  QByteArray QLatin1Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QLatin1Codec4nameEv(const QLatin1Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QLatin1Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12QLatin1Codec7aliasesEv(
    const QLatin1Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QLatin1Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLatin1Codec7mibEnumEv(const QLatin1Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQLatin1Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLatin1Codec(
    QLatin1Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLatin1Codec *>(self)->take(key, call);
}

//  QByteArray QLatin1Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QLatin1Codec4nameEv(const QLatin1Codec *self) {
  return new QByteArray(self->QLatin1Codec::name());
}

//  int QLatin1Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QLatin1Codec7mibEnumEv(const QLatin1Codec *self) {
  return self->QLatin1Codec::mibEnum();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec)
