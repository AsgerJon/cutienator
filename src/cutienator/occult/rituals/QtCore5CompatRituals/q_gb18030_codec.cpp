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
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qgb18030codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 26, as _ZN13QGb18030CodecC1Ev
inline QGb18030Codec::QGb18030Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 100, as _ZNK13QGb18030Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QGb18030Codec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    uchar buf[4];
    int nbuf = 0;
    ushort replacement = QChar::ReplacementCharacter;
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = QChar::Null;
        nbuf = state->remainingChars;
        buf[0] = (state->state_data[0] >> 24) & 0xff;
        buf[1] = (state->state_data[0] >> 16) & 0xff;
        buf[2] = (state->state_data[0] >>  8) & 0xff;
        buf[3] = (state->state_data[0] >>  0) & 0xff;
    }
    int invalid = 0;

    QString result;
    result.resize(len);
    int unicodeLen = 0;
    ushort *const resultData = reinterpret_cast<ushort*>(result.data());
    //qDebug("QGb18030Decoder::toUnicode(const char* chars, int len = %d)", len);
    for (int i = 0; i < len; i++) {
        uchar ch = chars[i];
        switch (nbuf) {
        case 0:
            if (IsLatin(ch)) {
                // ASCII
                resultData[unicodeLen] = ch;
                ++unicodeLen;
            } else if (Is1stByte(ch)) {
                // GB18030?
                buf[0] = ch;
                nbuf = 1;
            } else {
                // Invalid
                resultData[unicodeLen] = replacement;
                ++unicodeLen;
                ++invalid;
            }
            break;
        case 1:
            // GB18030 2 bytes
            if (Is2ndByteIn2Bytes(ch)) {
                buf[1] = ch;
                int clen = 2;
                uint u = qt_Gb18030ToUnicode(buf, clen);
                if (clen == 2) {
                    resultData[unicodeLen] = qValidChar(static_cast<ushort>(u));
                    ++unicodeLen;
                } else {
                    resultData[unicodeLen] = replacement;
                    ++unicodeLen;
                    ++invalid;
                }
                nbuf = 0;
            } else if (Is2ndByteIn4Bytes(ch)) {
                buf[1] = ch;
                nbuf = 2;
            } else {
                // Error
                resultData[unicodeLen] = replacement;
                ++unicodeLen;
                ++invalid;
                nbuf = 0;
            }
            break;
        case 2:
            // GB18030 3 bytes
            if (Is3rdByte(ch)) {
                buf[2] = ch;
                nbuf = 3;
            } else {
                resultData[unicodeLen] = replacement;
                ++unicodeLen;
                ++invalid;
                nbuf = 0;
            }
            break;
        case 3:
            // GB18030 4 bytes
            if (Is4thByte(ch)) {
                buf[3] = ch;
                int clen = 4;
                uint u = qt_Gb18030ToUnicode(buf, clen);
                if (clen == 4) {
                    resultData[unicodeLen] = qValidChar(u);
                    ++unicodeLen;
                } else {
                    resultData[unicodeLen] = replacement;
                    ++unicodeLen;
                    ++invalid;
                }
            } else {
                resultData[unicodeLen] = replacement;
                ++unicodeLen;
                ++invalid;
            }
            nbuf = 0;
            break;
        }
    }
    result.resize(unicodeLen);

    if (state) {
        state->remainingChars = nbuf;
        state->state_data[0] = (buf[0] << 24) + (buf[1] << 16) + (buf[2] << 8) + buf[3];
        state->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 30, as _ZNK13QGb18030Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QGb18030Codec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
{
    char replacement = '?';
    int high = -1;
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = 0;
        if (state->remainingChars)
            high = state->state_data[0];
    }
    int invalid = 0;

    int rlen = 4 *len + 1;
    QByteArray rstr;
    rstr.resize(rlen);
    uchar* cursor = (uchar*)rstr.data();

    //qDebug("QGb18030Codec::fromUnicode(const QString& uc, int& lenInOut = %d)", lenInOut);
    for (int i = 0; i < len; i++) {
        unsigned short ch = uc[i].unicode();
        int len;
        uchar buf[4];
        if (high >= 0) {
            if (uc[i].isLowSurrogate()) {
                // valid surrogate pair
                uint u = QChar::surrogateToUcs4(high, uc[i].unicode());
                len = qt_UnicodeToGb18030(u, buf);
                if (len >= 2) {
                    for (int j=0; j<len; j++)
                        *cursor++ = buf[j];
                } else {
                    *cursor++ = replacement;
                    ++invalid;
                }
                high = -1;
                continue;
            } else {
                *cursor++ = replacement;
                ++invalid;
                high = -1;
            }
        }

        if (IsLatin(ch)) {
            // ASCII
            *cursor++ = ch;
        } else if (uc[i].isHighSurrogate()) {
            // surrogates area. check for correct encoding
            // we need at least one more character, first the high surrogate, then the low one
            high = ch;
        } else if ((len = qt_UnicodeToGb18030(ch, buf)) >= 2) {
            for (int j=0; j<len; j++)
                *cursor++ = buf[j];
        } else {
            // Error
            *cursor++ = replacement;
            ++invalid;
        }
    }
    rstr.resize(cursor - (const uchar*)rstr.constData());

    if (state) {
        state->invalidChars += invalid;
        state->state_data[0] = high;
        if (high)
            state->remainingChars = 1;
    }
    return rstr;
}
//  -----------------------------------------------------------------------

//  A QGb18030Codec that Python can take functions over in. Every QGb18030Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb18030CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQGb18030CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb18030CodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQGb18030Codec : public QGb18030Codec {
public:
  using QGb18030Codec::QGb18030Codec;
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
  //  QByteArray QGb18030Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGb18030CodecCall0 call = reinterpret_cast<CuteQGb18030CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGb18030Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QGb18030Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGb18030CodecCall1 call = reinterpret_cast<CuteQGb18030CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGb18030Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QGb18030Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGb18030CodecCall2 call = reinterpret_cast<CuteQGb18030CodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QGb18030Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QGb18030Codec::QGb18030Codec()
extern "C" Q_DECL_EXPORT
QGb18030Codec *ritual_ZN13QGb18030CodecC1Ev() {
  return new CuteQGb18030Codec();
}

//  QByteArray QGb18030Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN13QGb18030Codec5_nameEv() {
  return new QByteArray(QGb18030Codec::_name());
}

//  QList<QByteArray> QGb18030Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN13QGb18030Codec8_aliasesEv() {
  return new QList<QByteArray>(QGb18030Codec::_aliases());
}

//  int QGb18030Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN13QGb18030Codec8_mibEnumEv() {
  return QGb18030Codec::_mibEnum();
}

//  QByteArray QGb18030Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QGb18030Codec4nameEv(const QGb18030Codec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QGb18030Codec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QGb18030Codec7aliasesEv(
    const QGb18030Codec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QGb18030Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGb18030Codec7mibEnumEv(const QGb18030Codec *self) {
  return self->mibEnum();
}

//  QString QGb18030Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QGb18030Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QGb18030Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QGb18030Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QGb18030Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QGb18030Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQGb18030Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGb18030Codec(
    QGb18030Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGb18030Codec *>(self)->take(key, call);
}

//  QByteArray QGb18030Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QGb18030Codec4nameEv(const QGb18030Codec *self) {
  return new QByteArray(self->QGb18030Codec::name());
}

//  int QGb18030Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QGb18030Codec7mibEnumEv(const QGb18030Codec *self) {
  return self->QGb18030Codec::mibEnum();
}

//  QByteArray QGb18030Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QGb18030Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QGb18030Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QGb18030Codec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
