//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qeuckrcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qeuckrcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qeuckrcodec_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 880, as _ZN11QEucKrCodec5_nameEv
inline QByteArray QEucKrCodec::_name()
{
  return "EUC-KR";
}

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 875, as _ZN11QEucKrCodec8_mibEnumEv
inline int QEucKrCodec::_mibEnum()
{
  return 38;
}
//  -----------------------------------------------------------------------

//  A QEucKrCodec that Python can take functions over in. Every QEucKrCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQEucKrCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQEucKrCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQEucKrCodec : public QEucKrCodec {
public:
  using QEucKrCodec::QEucKrCodec;
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
  //  QByteArray QEucKrCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQEucKrCodecCall0 call = reinterpret_cast<CuteQEucKrCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QEucKrCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QEucKrCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQEucKrCodecCall1 call = reinterpret_cast<CuteQEucKrCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QEucKrCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QEucKrCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QEucKrCodec5_nameEv() {
  return new QByteArray(QEucKrCodec::_name());
}

//  QList<QByteArray> QEucKrCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN11QEucKrCodec8_aliasesEv() {
  return new QList<QByteArray>(QEucKrCodec::_aliases());
}

//  int QEucKrCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QEucKrCodec8_mibEnumEv() {
  return QEucKrCodec::_mibEnum();
}

//  QByteArray QEucKrCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QEucKrCodec4nameEv(const QEucKrCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QEucKrCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QEucKrCodec7aliasesEv(
    const QEucKrCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QEucKrCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEucKrCodec7mibEnumEv(const QEucKrCodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQEucKrCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEucKrCodec(
    QEucKrCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEucKrCodec *>(self)->take(key, call);
}

//  QByteArray QEucKrCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QEucKrCodec4nameEv(const QEucKrCodec *self) {
  return new QByteArray(self->QEucKrCodec::name());
}

//  int QEucKrCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QEucKrCodec7mibEnumEv(const QEucKrCodec *self) {
  return self->QEucKrCodec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
