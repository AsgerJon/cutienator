//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(iconv)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qglobal_p.h>
#include <QtCore5Compat/private/qiconvcodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qthreadstorage.h>
#include <errno.h>
#include <locale.h>
#include <stdio.h>
#include <dlfcn.h>
#include <unistd.h>
#if defined(_XOPEN_UNIX) && !defined(Q_OS_QNX)
#  include <langinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 42, as _ZN11QIconvCodecC1Ev
inline QIconvCodec::QIconvCodec()
    : utf16Codec(0)
{
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 59, as _ZN11QIconvCodecD1Ev
inline QIconvCodec::~QIconvCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 367, as _ZNK11QIconvCodec4nameEv
inline QByteArray QIconvCodec::name() const
{
    return "System";
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 372, as _ZNK11QIconvCodec7mibEnumEv
inline int QIconvCodec::mibEnum() const
{
    return 0;
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 47, as _ZNK11QIconvCodec4initEv
inline void QIconvCodec::init() const
{
    utf16Codec = QTextCodec::codecForMib(1015);
    Q_ASSERT_X(utf16Codec != 0,
               "QIconvCodec::convertToUnicode",
               "internal error, UTF-16 codec not found");
    if (!utf16Codec) {
        fprintf(stderr, "QIconvCodec::convertToUnicode: internal error, UTF-16 codec not found\n");
        utf16Codec = reinterpret_cast<QTextCodec *>(~0);
    }
}
//  -----------------------------------------------------------------------

//  A QIconvCodec that Python can take functions over in. Every QIconvCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
typedef const QByteArray * (*CuteQIconvCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
typedef int (*CuteQIconvCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
class CuteQIconvCodec : public QIconvCodec {
public:
  using QIconvCodec::QIconvCodec;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
  //  QByteArray QIconvCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconvCodecCall0 call = reinterpret_cast<CuteQIconvCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QIconvCodec::name();
  }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
  //  int QIconvCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconvCodecCall1 call = reinterpret_cast<CuteQIconvCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QIconvCodec::mibEnum();
  }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
};

//  QIconvCodec::QIconvCodec()
extern "C" Q_DECL_EXPORT
QIconvCodec *ritual_ZN11QIconvCodecC1Ev() {
  return new CuteQIconvCodec();
}

//  QIconvCodec::~QIconvCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconvCodecD1Ev(QIconvCodec *self) {
  delete self;
}

//  QByteArray QIconvCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QIconvCodec4nameEv(const QIconvCodec *self) {
  return new QByteArray(self->name());
}

//  int QIconvCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QIconvCodec7mibEnumEv(const QIconvCodec *self) {
  return self->mibEnum();
}

//  void QIconvCodec::init() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QIconvCodec4initEv(const QIconvCodec *self) {
  self->init();
}

//  a Python function taken by a CuteQIconvCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconvCodec(
    QIconvCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconvCodec *>(self)->take(key, call);
}

//  QByteArray QIconvCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QIconvCodec4nameEv(const QIconvCodec *self) {
  return new QByteArray(self->QIconvCodec::name());
}

//  int QIconvCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QIconvCodec7mibEnumEv(const QIconvCodec *self) {
  return self->QIconvCodec::mibEnum();
}

#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
