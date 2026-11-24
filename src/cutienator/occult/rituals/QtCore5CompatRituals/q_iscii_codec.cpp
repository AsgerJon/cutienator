//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qisciicodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(codecs) && QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qisciicodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qisciicodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 49, as _ZN11QIsciiCodecD1Ev
inline QIsciiCodec::~QIsciiCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 58, as _ZNK11QIsciiCodec7mibEnumEv
inline int QIsciiCodec::mibEnum() const
{
    /* There is no MIBEnum for Iscii */
    return -3000-idx;
}
//  -----------------------------------------------------------------------

//  A QIsciiCodec that Python can take functions over in. Every QIsciiCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQIsciiCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef int (*CuteQIsciiCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQIsciiCodec : public QIsciiCodec {
public:
  using QIsciiCodec::QIsciiCodec;
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
  //  QByteArray QIsciiCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIsciiCodecCall0 call = reinterpret_cast<CuteQIsciiCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QIsciiCodec::name();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  int QIsciiCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIsciiCodecCall1 call = reinterpret_cast<CuteQIsciiCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QIsciiCodec::mibEnum();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QIsciiCodec::~QIsciiCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIsciiCodecD1Ev(QIsciiCodec *self) {
  delete self;
}

//  int QIsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QIsciiCodec7mibEnumEv(const QIsciiCodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQIsciiCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIsciiCodec(
    QIsciiCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIsciiCodec *>(self)->take(key, call);
}

//  int QIsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QIsciiCodec7mibEnumEv(const QIsciiCodec *self) {
  return self->QIsciiCodec::mibEnum();
}

#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(codecs) && QT_CONFIG(textcodec)
