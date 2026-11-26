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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 63, as _ZN13QLatin15CodecD1Ev
inline QLatin15Codec::~QLatin15Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 67, as _ZNK13QLatin15Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QLatin15Codec::convertToUnicode(const char* chars, int len, ConverterState *) const
{
    QString str = QString::fromLatin1(chars, len);
    QChar *uc = str.data();
    while(len--) {
        switch(uc->unicode()) {
            case 0xa4:
                *uc = QChar(0x20ac);
                break;
            case 0xa6:
                *uc = QChar(0x0160);
                break;
            case 0xa8:
                *uc = QChar(0x0161);
                break;
            case 0xb4:
                *uc = QChar(0x017d);
                break;
            case 0xb8:
                *uc = QChar(0x017e);
                break;
            case 0xbc:
                *uc = QChar(0x0152);
                break;
            case 0xbd:
                *uc = QChar(0x0153);
                break;
            case 0xbe:
                *uc = QChar(0x0178);
                break;
            default:
                break;
        }
        uc++;
    }
    return str;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 105, as _ZNK13QLatin15Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QLatin15Codec::convertFromUnicode(const QChar *in, int length, ConverterState *state) const
{
    const char replacement = (state && state->flags & ConvertInvalidToNull) ? 0 : '?';
    QByteArray r(length, QT_PREPEND_NAMESPACE(Qt::Uninitialized));
    char *d = r.data();
    int invalid = 0;
    for (int i = 0; i < length; ++i) {
        uchar c;
        ushort uc = in[i].unicode();
        if (uc < 0x0100) {
            if (uc > 0xa3) {
                switch(uc) {
                case 0xa4:
                case 0xa6:
                case 0xa8:
                case 0xb4:
                case 0xb8:
                case 0xbc:
                case 0xbd:
                case 0xbe:
                    c = replacement;
                    ++invalid;
                    break;
                default:
                    c = (unsigned char) uc;
                    break;
                }
            } else {
                c = (unsigned char) uc;
            }
        } else {
            if (uc == 0x20ac)
                c = 0xa4;
            else if ((uc & 0xff00) == 0x0100) {
                switch(uc) {
                case 0x0160:
                    c = 0xa6;
                    break;
                case 0x0161:
                    c = 0xa8;
                    break;
                case 0x017d:
                    c = 0xb4;
                    break;
                case 0x017e:
                    c = 0xb8;
                    break;
                case 0x0152:
                    c = 0xbc;
                    break;
                case 0x0153:
                    c = 0xbd;
                    break;
                case 0x0178:
                    c = 0xbe;
                    break;
                default:
                    c = replacement;
                    ++invalid;
                }
            } else {
                c = replacement;
                ++invalid;
            }
        }
        d[i] = (char)c;
    }
    if (state) {
        state->remainingChars = 0;
        state->invalidChars += invalid;
    }
    return r;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 180, as _ZNK13QLatin15Codec4nameEv
inline QByteArray QLatin15Codec::name() const
{
    return "ISO-8859-15";
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 185, as _ZNK13QLatin15Codec7aliasesEv
inline QList<QByteArray> QLatin15Codec::aliases() const
{
    QList<QByteArray> list;
    list << "latin9";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qlatincodec.cpp, line 192, as _ZNK13QLatin15Codec7mibEnumEv
inline int QLatin15Codec::mibEnum() const
{
    return 111;
}
//  -----------------------------------------------------------------------

//  A QLatin15Codec that Python can take functions over in. Every QLatin15Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin15CodecCall0)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQLatin15CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQLatin15CodecCall2)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQLatin15Codec : public QLatin15Codec {
public:
  using QLatin15Codec::QLatin15Codec;
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
  //  QByteArray QLatin15Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLatin15CodecCall0 call = reinterpret_cast<CuteQLatin15CodecCall0>(taken[0]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QLatin15Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  QByteArray QLatin15Codec::name() const
  QByteArray name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLatin15CodecCall1 call = reinterpret_cast<CuteQLatin15CodecCall1>(taken[1]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLatin15Codec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QLatin15Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLatin15CodecCall2 call = reinterpret_cast<CuteQLatin15CodecCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLatin15Codec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)
};

//  QLatin15Codec::~QLatin15Codec()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLatin15CodecD1Ev(QLatin15Codec *self) {
  delete self;
}

//  QString QLatin15Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QLatin15Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QLatin15Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QLatin15Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QLatin15Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QLatin15Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  QByteArray QLatin15Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QLatin15Codec4nameEv(const QLatin15Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QLatin15Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QLatin15Codec7aliasesEv(
    const QLatin15Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QLatin15Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin15Codec7mibEnumEv(const QLatin15Codec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQLatin15Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLatin15Codec(
    QLatin15Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLatin15Codec *>(self)->take(key, call);
}

//  QByteArray QLatin15Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QLatin15Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QLatin15Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QLatin15Codec::convertFromUnicode(a0, a1, a2));
}

//  QByteArray QLatin15Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QLatin15Codec4nameEv(const QLatin15Codec *self) {
  return new QByteArray(self->QLatin15Codec::name());
}

//  int QLatin15Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QLatin15Codec7mibEnumEv(const QLatin15Codec *self) {
  return self->QLatin15Codec::mibEnum();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec)
