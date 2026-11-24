//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qwindowscodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec) && defined(Q_OS_WIN) && !QT_CONFIG(icu)
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qwindowscodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qwindowscodec_p.h>
#include <QtCore/private/qstringconverter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qwindowscodec.cpp, line 10, as _ZN18QWindowsLocalCodecC1Ev
inline QWindowsLocalCodec::QWindowsLocalCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qwindowscodec.cpp, line 14, as _ZN18QWindowsLocalCodecD1Ev
inline QWindowsLocalCodec::~QWindowsLocalCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qwindowscodec.cpp, line 34, as _ZNK18QWindowsLocalCodec4nameEv
inline QByteArray QWindowsLocalCodec::name() const
{
    return "System";
}

//  from ../qt5compat/src/core5/codecs/qwindowscodec.cpp, line 39, as _ZNK18QWindowsLocalCodec7mibEnumEv
inline int QWindowsLocalCodec::mibEnum() const
{
    return 0;
}
//  -----------------------------------------------------------------------

//  A QWindowsLocalCodec that Python can take functions over in. Every QWindowsLocalCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQWindowsLocalCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQWindowsLocalCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQWindowsLocalCodec : public QWindowsLocalCodec {
public:
  using QWindowsLocalCodec::QWindowsLocalCodec;
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
  //  QByteArray QWindowsLocalCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsLocalCodecCall0 call = reinterpret_cast<CuteQWindowsLocalCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsLocalCodec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QWindowsLocalCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsLocalCodecCall1 call = reinterpret_cast<CuteQWindowsLocalCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsLocalCodec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QWindowsLocalCodec::QWindowsLocalCodec()
extern "C" Q_DECL_EXPORT
QWindowsLocalCodec *ritual_ZN18QWindowsLocalCodecC1Ev() {
  return new CuteQWindowsLocalCodec();
}

//  QWindowsLocalCodec::~QWindowsLocalCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsLocalCodecD1Ev(QWindowsLocalCodec *self) {
  delete self;
}

//  QByteArray QWindowsLocalCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QWindowsLocalCodec4nameEv(
    const QWindowsLocalCodec *self) {
  return new QByteArray(self->name());
}

//  int QWindowsLocalCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWindowsLocalCodec7mibEnumEv(
    const QWindowsLocalCodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQWindowsLocalCodec, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsLocalCodec(
    QWindowsLocalCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsLocalCodec *>(self)->take(key, call);
}

//  QByteArray QWindowsLocalCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK18QWindowsLocalCodec4nameEv(
    const QWindowsLocalCodec *self) {
  return new QByteArray(self->QWindowsLocalCodec::name());
}

//  int QWindowsLocalCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QWindowsLocalCodec7mibEnumEv(
    const QWindowsLocalCodec *self) {
  return self->QWindowsLocalCodec::mibEnum();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec) && defined(Q_OS_WIN) && !QT_CONFIG(icu)
