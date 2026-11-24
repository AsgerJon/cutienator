//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qgb18030codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 236, as _ZN9QGbkCodecC1Ev
inline QGbkCodec::QGbkCodec()
    : QGb18030Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 246, as _ZN9QGbkCodec5_nameEv
inline QByteArray QGbkCodec::_name()
{
    return "GBK";
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 251, as _ZN9QGbkCodec8_aliasesEv
inline QList<QByteArray> QGbkCodec::_aliases()
{
    QList<QByteArray> list;
    list << "CP936"
         << "MS936"
         << "windows-936";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 241, as _ZN9QGbkCodec8_mibEnumEv
inline int QGbkCodec::_mibEnum()
{
    return 113;
}
//  -----------------------------------------------------------------------

//  A QGbkCodec that Python can take functions over in. Every QGbkCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGbkCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQGbkCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQGbkCodec : public QGbkCodec {
public:
  using QGbkCodec::QGbkCodec;
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
  //  QByteArray QGbkCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGbkCodecCall0 call = reinterpret_cast<CuteQGbkCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGbkCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QGbkCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGbkCodecCall1 call = reinterpret_cast<CuteQGbkCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGbkCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QGbkCodec::QGbkCodec()
extern "C" Q_DECL_EXPORT
QGbkCodec *ritual_ZN9QGbkCodecC1Ev() {
  return new CuteQGbkCodec();
}

//  QByteArray QGbkCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QGbkCodec5_nameEv() {
  return new QByteArray(QGbkCodec::_name());
}

//  QList<QByteArray> QGbkCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QGbkCodec8_aliasesEv() {
  return new QList<QByteArray>(QGbkCodec::_aliases());
}

//  int QGbkCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN9QGbkCodec8_mibEnumEv() {
  return QGbkCodec::_mibEnum();
}

//  QByteArray QGbkCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QGbkCodec4nameEv(const QGbkCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QGbkCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK9QGbkCodec7aliasesEv(const QGbkCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QGbkCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGbkCodec7mibEnumEv(const QGbkCodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQGbkCodec, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGbkCodec(QGbkCodec *self, const char *key, void *call) {
  return static_cast<CuteQGbkCodec *>(self)->take(key, call);
}

//  QByteArray QGbkCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK9QGbkCodec4nameEv(const QGbkCodec *self) {
  return new QByteArray(self->QGbkCodec::name());
}

//  int QGbkCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QGbkCodec7mibEnumEv(const QGbkCodec *self) {
  return self->QGbkCodec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
