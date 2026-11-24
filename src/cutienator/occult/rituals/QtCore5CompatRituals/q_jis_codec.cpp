//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qjiscodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qjiscodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qjiscodec_p.h"
#include "qlist.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 316, as _ZN9QJisCodec5_nameEv
inline QByteArray QJisCodec::_name()
{
    return "ISO-2022-JP";
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 324, as _ZN9QJisCodec8_aliasesEv
inline QList<QByteArray> QJisCodec::_aliases()
{
    QList<QByteArray> list;
    list << "JIS7"; // Qt 3 compat
    return list;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 308, as _ZN9QJisCodec8_mibEnumEv
inline int QJisCodec::_mibEnum()
{
    return 39;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 55, as _ZN9QJisCodecC1Ev
inline QJisCodec::QJisCodec() : conv(QJpUnicodeConv::newConverter(QJpUnicodeConv::Default))
{
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 63, as _ZN9QJisCodecD1Ev
inline QJisCodec::~QJisCodec()
{
    delete (const QJpUnicodeConv*)conv;
    conv = 0;
}
//  -----------------------------------------------------------------------

//  A QJisCodec that Python can take functions over in. Every QJisCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQJisCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQJisCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQJisCodec : public QJisCodec {
public:
  using QJisCodec::QJisCodec;
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
  //  QByteArray QJisCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQJisCodecCall0 call = reinterpret_cast<CuteQJisCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QJisCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QJisCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQJisCodecCall1 call = reinterpret_cast<CuteQJisCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QJisCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QJisCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QJisCodec5_nameEv() {
  return new QByteArray(QJisCodec::_name());
}

//  QList<QByteArray> QJisCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QJisCodec8_aliasesEv() {
  return new QList<QByteArray>(QJisCodec::_aliases());
}

//  int QJisCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJisCodec8_mibEnumEv() {
  return QJisCodec::_mibEnum();
}

//  QByteArray QJisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QJisCodec4nameEv(const QJisCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QJisCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK9QJisCodec7aliasesEv(const QJisCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QJisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QJisCodec7mibEnumEv(const QJisCodec *self) {
  return self->mibEnum();
}

//  QJisCodec::QJisCodec()
extern "C" Q_DECL_EXPORT
QJisCodec *ritual_ZN9QJisCodecC1Ev() {
  return new CuteQJisCodec();
}

//  QJisCodec::~QJisCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJisCodecD1Ev(QJisCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQJisCodec, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJisCodec(QJisCodec *self, const char *key, void *call) {
  return static_cast<CuteQJisCodec *>(self)->take(key, call);
}

//  QByteArray QJisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK9QJisCodec4nameEv(const QJisCodec *self) {
  return new QByteArray(self->QJisCodec::name());
}

//  int QJisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QJisCodec7mibEnumEv(const QJisCodec *self) {
  return self->QJisCodec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
