//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qtsciicodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qtsciicodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qtsciicodec_p.h"
#include "qlist.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 26, as _ZN11QTsciiCodecD1Ev
inline QTsciiCodec::~QTsciiCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 130, as _ZNK11QTsciiCodec4nameEv
inline QByteArray QTsciiCodec::name() const
{
    return "TSCII";
}

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 140, as _ZNK11QTsciiCodec7mibEnumEv
inline int QTsciiCodec::mibEnum() const
{
  return 2107;
}
//  -----------------------------------------------------------------------

//  A QTsciiCodec that Python can take functions over in. Every QTsciiCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQTsciiCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef int (*CuteQTsciiCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQTsciiCodec : public QTsciiCodec {
public:
  using QTsciiCodec::QTsciiCodec;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  QByteArray QTsciiCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTsciiCodecCall0 call = reinterpret_cast<CuteQTsciiCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTsciiCodec::name();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  int QTsciiCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTsciiCodecCall1 call = reinterpret_cast<CuteQTsciiCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTsciiCodec::mibEnum();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QTsciiCodec::~QTsciiCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTsciiCodecD1Ev(QTsciiCodec *self) {
  delete self;
}

//  QByteArray QTsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTsciiCodec4nameEv(const QTsciiCodec *self) {
  return new QByteArray(self->name());
}

//  int QTsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTsciiCodec7mibEnumEv(const QTsciiCodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQTsciiCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTsciiCodec(
    QTsciiCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTsciiCodec *>(self)->take(key, call);
}

//  QByteArray QTsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QTsciiCodec4nameEv(const QTsciiCodec *self) {
  return new QByteArray(self->QTsciiCodec::name());
}

//  int QTsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTsciiCodec7mibEnumEv(const QTsciiCodec *self) {
  return self->QTsciiCodec::mibEnum();
}

#endif  // QT_CONFIG(codecs)
