//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qsimplecodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qsimplecodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsimplecodec_p.h"
#include "qlist.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qsimplecodec.cpp, line 576, as _ZN16QSimpleTextCodecD1Ev
inline QSimpleTextCodec::~QSimpleTextCodec()
{
    delete reverseMap.loadAcquire();
}
//  -----------------------------------------------------------------------

//  A QSimpleTextCodec that Python can take functions over in. Every QSimpleTextCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQSimpleTextCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQSimpleTextCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQSimpleTextCodec : public QSimpleTextCodec {
public:
  using QSimpleTextCodec::QSimpleTextCodec;
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
  //  QByteArray QSimpleTextCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSimpleTextCodecCall0 call = reinterpret_cast<CuteQSimpleTextCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSimpleTextCodec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QSimpleTextCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSimpleTextCodecCall1 call = reinterpret_cast<CuteQSimpleTextCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSimpleTextCodec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QSimpleTextCodec::~QSimpleTextCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSimpleTextCodecD1Ev(QSimpleTextCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQSimpleTextCodec, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSimpleTextCodec(
    QSimpleTextCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSimpleTextCodec *>(self)->take(key, call);
}

#endif  // QT_CONFIG(textcodec)
