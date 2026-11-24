//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qeucjpcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qeucjpcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qeucjpcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 212, as _ZN11QEucJpCodec5_nameEv
inline QByteArray QEucJpCodec::_name()
{
    return "EUC-JP";
}

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 207, as _ZN11QEucJpCodec8_mibEnumEv
inline int QEucJpCodec::_mibEnum()
{
    return 18;
}

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 50, as _ZN11QEucJpCodecC1Ev
inline QEucJpCodec::QEucJpCodec() : conv(QJpUnicodeConv::newConverter(QJpUnicodeConv::Default))
{
}

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 57, as _ZN11QEucJpCodecD1Ev
inline QEucJpCodec::~QEucJpCodec()
{
    delete (const QJpUnicodeConv*)conv;
    conv = 0;
}
//  -----------------------------------------------------------------------

//  A QEucJpCodec that Python can take functions over in. Every QEucJpCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQEucJpCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQEucJpCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQEucJpCodec : public QEucJpCodec {
public:
  using QEucJpCodec::QEucJpCodec;
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
  //  QByteArray QEucJpCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQEucJpCodecCall0 call = reinterpret_cast<CuteQEucJpCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QEucJpCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QEucJpCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQEucJpCodecCall1 call = reinterpret_cast<CuteQEucJpCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QEucJpCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QEucJpCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QEucJpCodec5_nameEv() {
  return new QByteArray(QEucJpCodec::_name());
}

//  QList<QByteArray> QEucJpCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN11QEucJpCodec8_aliasesEv() {
  return new QList<QByteArray>(QEucJpCodec::_aliases());
}

//  int QEucJpCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QEucJpCodec8_mibEnumEv() {
  return QEucJpCodec::_mibEnum();
}

//  QByteArray QEucJpCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QEucJpCodec4nameEv(const QEucJpCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QEucJpCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QEucJpCodec7aliasesEv(
    const QEucJpCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QEucJpCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEucJpCodec7mibEnumEv(const QEucJpCodec *self) {
  return self->mibEnum();
}

//  QEucJpCodec::QEucJpCodec()
extern "C" Q_DECL_EXPORT
QEucJpCodec *ritual_ZN11QEucJpCodecC1Ev() {
  return new CuteQEucJpCodec();
}

//  QEucJpCodec::~QEucJpCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEucJpCodecD1Ev(QEucJpCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQEucJpCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEucJpCodec(
    QEucJpCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEucJpCodec *>(self)->take(key, call);
}

//  QByteArray QEucJpCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QEucJpCodec4nameEv(const QEucJpCodec *self) {
  return new QByteArray(self->QEucJpCodec::name());
}

//  int QEucJpCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QEucJpCodec7mibEnumEv(const QEucJpCodec *self) {
  return self->QEucJpCodec::mibEnum();
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
