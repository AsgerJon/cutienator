//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qutfcodec_p.h>
#include <QtCore/qlist.h>
#include <QtCore/qendian.h>
#include <QtCore/qchar.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/private/qstringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 18, as _ZN10QUtf8CodecD1Ev
#if QT_CONFIG(textcodec)
inline QUtf8Codec::~QUtf8Codec()
{
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 46, as _ZNK10QUtf8Codec4nameEv
#if QT_CONFIG(textcodec)
inline QByteArray QUtf8Codec::name() const
{
    return "UTF-8";
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 51, as _ZNK10QUtf8Codec7mibEnumEv
#if QT_CONFIG(textcodec)
inline int QUtf8Codec::mibEnum() const
{
    return 106;
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 38, as _ZNK10QUtf8Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
#if QT_CONFIG(textcodec)
inline QString QUtf8Codec::convertToUnicode(const char *chars, int len, ConverterState *state) const
{
    ConverterState s(QStringConverter::Flag::Stateless);
    if (!state)
        state = &s;
    return QUtf8::convertToUnicode(QByteArrayView(chars, len), state);
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 22, as _ZNK10QUtf8Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
#if QT_CONFIG(textcodec)
inline QByteArray QUtf8Codec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
{
    ConverterState s(QStringConverter::Flag::Stateless);
    if (!state)
        state = &s;
    return QUtf8::convertFromUnicode(QStringView(uc, len), state);
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 30, as _ZNK10QUtf8Codec16convertToUnicodeEP7QStringPKciPN20QStringConverterBase5StateE
#if QT_CONFIG(textcodec)
inline void QUtf8Codec::convertToUnicode(QString *target, const char *chars, int len, ConverterState *state) const
{
    ConverterState s(QStringConverter::Flag::Stateless);
    if (!state)
        state = &s;
    *target += QUtf8::convertToUnicode(QByteArrayView(chars, len), state);
}
#endif  // QT_CONFIG(textcodec)
//  -----------------------------------------------------------------------

//  A QUtf8Codec that Python can take functions over in. Every QUtf8Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQUtf8CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQUtf8CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQUtf8CodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQUtf8Codec : public QUtf8Codec {
public:
  using QUtf8Codec::QUtf8Codec;
  void *taken[3] = {};

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
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
  //  QByteArray QUtf8Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQUtf8CodecCall0 call = reinterpret_cast<CuteQUtf8CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QUtf8Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QUtf8Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUtf8CodecCall1 call = reinterpret_cast<CuteQUtf8CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUtf8Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  QByteArray QUtf8Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQUtf8CodecCall2 call = reinterpret_cast<CuteQUtf8CodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QUtf8Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(textcodec)
};

//  QUtf8Codec::~QUtf8Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUtf8CodecD1Ev(QUtf8Codec *self) {
  delete self;
}

//  QByteArray QUtf8Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QUtf8Codec4nameEv(const QUtf8Codec *self) {
  return new QByteArray(self->name());
}

//  int QUtf8Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUtf8Codec7mibEnumEv(const QUtf8Codec *self) {
  return self->mibEnum();
}

//  QString QUtf8Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUtf8Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QUtf8Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QUtf8Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QUtf8Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QUtf8Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

#if QT_CONFIG(textcodec)
//  void QUtf8Codec::convertToUnicode(QString *target, const char *a1, int
//      a2, ConverterState *a3) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QUtf8Codec16convertToUnicodeEP7QStringPKciPN20QStringConverterBase5StateE(
    const QUtf8Codec *self,
    QString *target,
    const char *a1,
    int a2,
    QTextCodec::ConverterState *a3) {
  self->convertToUnicode(target, a1, a2, a3);
}
#endif  // QT_CONFIG(textcodec)

//  a Python function taken by a CuteQUtf8Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUtf8Codec(QUtf8Codec *self, const char *key, void *call) {
  return static_cast<CuteQUtf8Codec *>(self)->take(key, call);
}

#if QT_CONFIG(textcodec)
//  QByteArray QUtf8Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QUtf8Codec4nameEv(const QUtf8Codec *self) {
  return new QByteArray(self->QUtf8Codec::name());
}
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
//  int QUtf8Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QUtf8Codec7mibEnumEv(const QUtf8Codec *self) {
  return self->QUtf8Codec::mibEnum();
}
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
//  QByteArray QUtf8Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QUtf8Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QUtf8Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QUtf8Codec::convertFromUnicode(a0, a1, a2));
}
#endif  // QT_CONFIG(textcodec)

#endif  // QT_CONFIG(textcodec)
