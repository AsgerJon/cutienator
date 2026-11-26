//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qlatincodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qlatincodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qlatincodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 10, as _ZN12QLatin1CodecD1Ev
inline QLatin1Codec::~QLatin1Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 14, as _ZNK12QLatin1Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QLatin1Codec::convertToUnicode(const char *chars, int len, ConverterState *) const
{
    return QString::fromLatin1(chars, len);
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 20, as _ZNK12QLatin1Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QLatin1Codec::convertFromUnicode(const QChar *ch, int len, ConverterState *state) const
{
    const char replacement = (state && state->flags & ConvertInvalidToNull) ? 0 : '?';
    QByteArray r(len, QT_PREPEND_NAMESPACE(Qt::Uninitialized));
    char *d = r.data();
    int invalid = 0;
    for (int i = 0; i < len; ++i) {
        if (ch[i] > QChar(0xff)) {
            d[i] = replacement;
            ++invalid;
        } else {
            d[i] = (char)ch[i].cell();
        }
    }
    if (state) {
        state->invalidChars += invalid;
    }
    return r;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 40, as _ZNK12QLatin1Codec4nameEv
inline QByteArray QLatin1Codec::name() const
{
    return "ISO-8859-1";
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 45, as _ZNK12QLatin1Codec7aliasesEv
inline QList<QByteArray> QLatin1Codec::aliases() const
{
    QList<QByteArray> list;
    list << "latin1"
         << "CP819"
         << "IBM819"
         << "iso-ir-100"
         << "csISOLatin1";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 57, as _ZNK12QLatin1Codec7mibEnumEv
inline int QLatin1Codec::mibEnum() const
{
    return 4;
}
//  -----------------------------------------------------------------------

//  A QLatin1Codec that Python can take functions over in. Every QLatin1Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin1CodecCall0)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin1CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQLatin1CodecCall2)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQLatin1Codec : public QLatin1Codec {
public:
  using QLatin1Codec::QLatin1Codec;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
  //  QByteArray QLatin1Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLatin1CodecCall0 call = reinterpret_cast<CuteQLatin1CodecCall0>(taken[0]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QLatin1Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  QByteArray QLatin1Codec::name() const
  QByteArray name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLatin1CodecCall1 call = reinterpret_cast<CuteQLatin1CodecCall1>(taken[1]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLatin1Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QLatin1Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLatin1CodecCall2 call = reinterpret_cast<CuteQLatin1CodecCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLatin1Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QLatin1Codec::~QLatin1Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLatin1CodecD1Ev(QLatin1Codec *self) {
  delete self;
}

//  QString QLatin1Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLatin1Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QLatin1Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QLatin1Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QLatin1Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QLatin1Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  QByteArray QLatin1Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QLatin1Codec4nameEv(const QLatin1Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QLatin1Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12QLatin1Codec7aliasesEv(
    const QLatin1Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QLatin1Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLatin1Codec7mibEnumEv(const QLatin1Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQLatin1Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLatin1Codec(
    QLatin1Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLatin1Codec *>(self)->take(key, call);
}

//  QByteArray QLatin1Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QLatin1Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QLatin1Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QLatin1Codec::convertFromUnicode(a0, a1, a2));
}

//  QByteArray QLatin1Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QLatin1Codec4nameEv(const QLatin1Codec *self) {
  return new QByteArray(self->QLatin1Codec::name());
}

//  int QLatin1Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QLatin1Codec7mibEnumEv(const QLatin1Codec *self) {
  return self->QLatin1Codec::mibEnum();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec)
