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
#include <QtCore/qstring.h>
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

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 4041, as _ZN11QCP949Codec5_nameEv
inline QByteArray QCP949Codec::_name()
{
    return "windows-949";
}

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 4046, as _ZN11QCP949Codec8_aliasesEv
inline QList<QByteArray> QCP949Codec::_aliases()
{
    QList<QByteArray> aliases;
    aliases += "CP949";
    return aliases;
}

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 4036, as _ZN11QCP949Codec8_mibEnumEv
inline int QCP949Codec::_mibEnum()
{
  return -949; // CP949 has no MIBenum. So we have to use fake value.
}

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 4129, as _ZNK11QCP949Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QCP949Codec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    uchar buf[2] = {0, 0};
    int nbuf = 0;
    QChar replacement = QChar::ReplacementCharacter;
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = QChar::Null;
        nbuf = state->remainingChars;
        buf[0] = state->state_data[0];
        buf[1] = state->state_data[1];
    }
    int invalid = 0;

    QString result;
    for (int i=0; i<len; i++) {
        uchar ch = chars[i];
        switch (nbuf) {
        case 0:
            if (ch < 0x80) {
                // ASCII
                result += QLatin1Char(ch);
            } else if (IsEucChar(ch)) {
                // KSC 5601
                buf[0] = ch;
                nbuf = 1;
            } else if (IsCP949Char(ch)){
                buf[0] = ch;
                nbuf = 1;
            } else {
                // Invalid
                result += replacement;
                ++invalid;
            }
            break;
        case 1:
            // KSC 5601
            if (IsEucChar(ch) && !IsCP949Char(buf[0])) {
                uint u = qt_Ksc5601ToUnicode((buf[0] << 8) |  ch);
                result += QValidChar(u);
            } else {
                // Rest of CP949
                int row, column;
                nbuf = 0;
                row = buf[0] - 0x81;
                if (0x41 <= ch && ch <= 0x5a)
                   column = ch - 0x41;
                else if (0x61 <= ch && ch <= 0x7a)
                    column = ch - 0x61 + 26;
                else if (0x81 <= ch && ch <= 0xfe)
                    column = ch - 0x81 + 52;
                else {
                    result += replacement;
                    ++invalid;
                    break;
                }

                int internal_code;
                if (row < 32)
                    internal_code = row * 178 + column;
                else
                    internal_code = 3008 + row * 84 + column;
                // check whether the conversion avialble in the table.
                if (internal_code < 0 || internal_code >= 8822) {
                    result += replacement;
                    ++invalid;
                    break;
                }
                else
                    result += QValidChar(cp949_icode_to_unicode[internal_code]);
            }
            nbuf = 0;
            break;
        }
    }

    if (state) {
        state->remainingChars = nbuf;
        state->state_data[0] = buf[0];
        state->state_data[1] = buf[1];
        state->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qeuckrcodec.cpp, line 4053, as _ZNK11QCP949Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QCP949Codec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
{
    char replacement = '?';
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = 0;
    }
    int invalid = 0;

    int rlen = 2*len + 1;
    QByteArray rstr;
    rstr.resize(rlen);
    uchar* cursor = (uchar*)rstr.data();
    for (int i = 0; i < len; i++) {
        unsigned short ch = uc[i].unicode();
        uint j;
        if (ch < 0x80) {
            // ASCII
            *cursor++ = ch;
        } else if ((j = qt_UnicodeToKsc5601(ch))) {
            // KSC 5601
            *cursor++ = (j >> 8)   | 0x80;
            *cursor++ = (j & 0xff) | 0x80;
        } else {
            const unsigned short *ptr = std::lower_bound(cp949_icode_to_unicode, cp949_icode_to_unicode + 8822, ch);
            if (ptr == cp949_icode_to_unicode + 8822 || ch < *ptr) {
                // Error
                *cursor++ = replacement;
                ++invalid;
            }
            else {
                // The table 'cp949_icode_to_unicode' contains following
                // 1. Elements of row 81-a0 (32 rows) consisting of 178 elements each.
                // 2. Elements of row a1-fe not in EUC-KR consisting of 84 elements each.
                // On each row the elements are distributed (41-5A), (61-7A), (81-FE) in order.
                // http://www.microsoft.com/globaldev/reference/dbcs/949.mspx

                // find the position of the current unicode in the table.
                int internal_code = ptr - cp949_icode_to_unicode;

                int row, column;
                if(internal_code < 32 * 178) {
                    // code between row 81-a0
                    row = internal_code / 178;
                    column = internal_code % 178;
                }
                else {
                    // code between a1-fe
                    internal_code -= 3008;
                    row = internal_code / 84;
                    column = internal_code % 84;
                }

                unsigned char first, second;
                first = row + 0x81;

                if(column < 26)
                    second = column + 0x41; // between 41-5A
                else if(column < 52)
                    second = column - 26 + 0x61; // between 61-7A
                else
                    second = column - 52 + 0x81; // between 81-FE

                *cursor++ = first;
                *cursor++ = second;
            }
        }
    }
    rstr.resize(cursor - (const uchar*)rstr.constData());

    if (state) {
        state->invalidChars += invalid;
    }
    return rstr;
}
//  -----------------------------------------------------------------------

//  A QCP949Codec that Python can take functions over in. Every QCP949Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQCP949CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQCP949CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQCP949CodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQCP949Codec : public QCP949Codec {
public:
  using QCP949Codec::QCP949Codec;
  void *taken[3] = {};

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
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QCP949Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCP949CodecCall0 call = reinterpret_cast<CuteQCP949CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCP949Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QCP949Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCP949CodecCall1 call = reinterpret_cast<CuteQCP949CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCP949Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QCP949Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCP949CodecCall2 call = reinterpret_cast<CuteQCP949CodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QCP949Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QCP949Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QCP949Codec5_nameEv() {
  return new QByteArray(QCP949Codec::_name());
}

//  QList<QByteArray> QCP949Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN11QCP949Codec8_aliasesEv() {
  return new QList<QByteArray>(QCP949Codec::_aliases());
}

//  int QCP949Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QCP949Codec8_mibEnumEv() {
  return QCP949Codec::_mibEnum();
}

//  QByteArray QCP949Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QCP949Codec4nameEv(const QCP949Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QCP949Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QCP949Codec7aliasesEv(
    const QCP949Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QCP949Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QCP949Codec7mibEnumEv(const QCP949Codec *self) {
  return self->mibEnum();
}

//  QString QCP949Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QCP949Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QCP949Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QCP949Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QCP949Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QCP949Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQCP949Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCP949Codec(
    QCP949Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCP949Codec *>(self)->take(key, call);
}

//  QByteArray QCP949Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QCP949Codec4nameEv(const QCP949Codec *self) {
  return new QByteArray(self->QCP949Codec::name());
}

//  int QCP949Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QCP949Codec7mibEnumEv(const QCP949Codec *self) {
  return self->QCP949Codec::mibEnum();
}

//  QByteArray QCP949Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QCP949Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QCP949Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QCP949Codec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
