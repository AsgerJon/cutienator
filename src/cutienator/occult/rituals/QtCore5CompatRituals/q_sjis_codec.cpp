//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qsjiscodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qsjiscodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsjiscodec_p.h"
#include "qlist.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 163, as _ZN10QSjisCodec5_nameEv
inline QByteArray QSjisCodec::_name()
{
    return "Shift_JIS";
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 171, as _ZN10QSjisCodec8_aliasesEv
inline QList<QByteArray> QSjisCodec::_aliases()
{
    QList<QByteArray> list;
    list << "SJIS" // Qt 3 compat
         << "MS_Kanji";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 158, as _ZN10QSjisCodec8_mibEnumEv
inline int QSjisCodec::_mibEnum()
{
    return 17;
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 24, as _ZN10QSjisCodecC1Ev
inline QSjisCodec::QSjisCodec() : conv(QJpUnicodeConv::newConverter(QJpUnicodeConv::Default))
{
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 32, as _ZN10QSjisCodecD1Ev
inline QSjisCodec::~QSjisCodec()
{
    delete (const QJpUnicodeConv*)conv;
    conv = 0;
}
//  -----------------------------------------------------------------------

//  A QSjisCodec that Python can take functions over in. Every QSjisCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQSjisCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQSjisCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQSjisCodec : public QSjisCodec {
public:
  using QSjisCodec::QSjisCodec;
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
  //  QByteArray QSjisCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSjisCodecCall0 call = reinterpret_cast<CuteQSjisCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSjisCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QSjisCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSjisCodecCall1 call = reinterpret_cast<CuteQSjisCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSjisCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QSjisCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QSjisCodec5_nameEv() {
  return new QByteArray(QSjisCodec::_name());
}

//  QList<QByteArray> QSjisCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN10QSjisCodec8_aliasesEv() {
  return new QList<QByteArray>(QSjisCodec::_aliases());
}

//  int QSjisCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSjisCodec8_mibEnumEv() {
  return QSjisCodec::_mibEnum();
}

//  QByteArray QSjisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QSjisCodec4nameEv(const QSjisCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QSjisCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK10QSjisCodec7aliasesEv(const QSjisCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QSjisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSjisCodec7mibEnumEv(const QSjisCodec *self) {
  return self->mibEnum();
}

//  QSjisCodec::QSjisCodec()
extern "C" Q_DECL_EXPORT
QSjisCodec *ritual_ZN10QSjisCodecC1Ev() {
  return new CuteQSjisCodec();
}

//  QSjisCodec::~QSjisCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSjisCodecD1Ev(QSjisCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQSjisCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSjisCodec(QSjisCodec *self, const char *key, void *call) {
  return static_cast<CuteQSjisCodec *>(self)->take(key, call);
}

//  QByteArray QSjisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QSjisCodec4nameEv(const QSjisCodec *self) {
  return new QByteArray(self->QSjisCodec::name());
}

//  int QSjisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QSjisCodec7mibEnumEv(const QSjisCodec *self) {
  return self->QSjisCodec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
