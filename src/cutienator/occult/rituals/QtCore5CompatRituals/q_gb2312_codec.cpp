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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 394, as _ZN12QGb2312CodecC1Ev
inline QGb2312Codec::QGb2312Codec()
    : QGb18030Codec()
{
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 404, as _ZN12QGb2312Codec5_nameEv
inline QByteArray QGb2312Codec::_name()
{
    return "GB2312";
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 399, as _ZN12QGb2312Codec8_mibEnumEv
inline int QGb2312Codec::_mibEnum()
{
    return 2025;
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 410, as _ZNK12QGb2312Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QGb2312Codec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    uchar buf[2] = {0, 0};
    int nbuf = 0;
    ushort replacement = QChar::ReplacementCharacter;
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = QChar::Null;
        nbuf = state->remainingChars;
        buf[0] = state->state_data[0];
        buf[1] = state->state_data[1];
    }
    int invalid = 0;

    QString result;
    result.resize(len);
    int unicodeLen = 0;
    ushort *const resultData = reinterpret_cast<ushort*>(result.data());
    //qDebug("QGb2312Decoder::toUnicode(const char* chars, int len = %d)", len);
    for (int i=0; i<len; i++) {
        uchar ch = chars[i];
        switch (nbuf) {
        case 0:
            if (IsLatin(ch)) {
                // ASCII
                resultData[unicodeLen] = ch;
                ++unicodeLen;
            } else if (IsByteInGb2312(ch)) {
                // GB2312 1st byte?
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
            // GB2312 2nd byte
            if (IsByteInGb2312(ch)) {
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
            } else {
                // Error
                resultData[unicodeLen] = replacement;
                ++unicodeLen;
                ++invalid;
                nbuf = 0;
            }
            break;
        }
    }
    result.resize(unicodeLen);

    if (state) {
        state->remainingChars = nbuf;
        state->state_data[0] = buf[0];
        state->state_data[1] = buf[1];
        state->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qgb18030codec.cpp, line 485, as _ZNK12QGb2312Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QGb2312Codec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
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

    //qDebug("QGb2312Codec::fromUnicode(const QString& uc, int& lenInOut = %d) const", lenInOut);
    for (int i = 0; i < len; i++) {
        QChar ch = uc[i];
        uchar buf[2];

        if (ch.row() == 0x00 && ch.cell() < 0x80) {
            // ASCII
            *cursor++ = ch.cell();
        } else if ((qt_UnicodeToGbk(ch.unicode(), buf) == 2) &&
                    (buf[0] >= 0xA1) && (buf[1] >= 0xA1)) {
            *cursor++ = buf[0];
            *cursor++ = buf[1];
        } else {
            // Error
            *cursor++ = replacement;
            ++invalid;
        }
    }
    rstr.resize(cursor - (const uchar*)rstr.constData());

    if (state) {
        state->invalidChars += invalid;
    }
    return rstr;
}
//  -----------------------------------------------------------------------

//  A QGb2312Codec that Python can take functions over in. Every QGb2312Codec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb2312CodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQGb2312CodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQGb2312CodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQGb2312Codec : public QGb2312Codec {
public:
  using QGb2312Codec::QGb2312Codec;
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
  //  QByteArray QGb2312Codec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGb2312CodecCall0 call = reinterpret_cast<CuteQGb2312CodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGb2312Codec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QGb2312Codec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGb2312CodecCall1 call = reinterpret_cast<CuteQGb2312CodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGb2312Codec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QGb2312Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGb2312CodecCall2 call = reinterpret_cast<CuteQGb2312CodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QGb2312Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QGb2312Codec::QGb2312Codec()
extern "C" Q_DECL_EXPORT
QGb2312Codec *ritual_ZN12QGb2312CodecC1Ev() {
  return new CuteQGb2312Codec();
}

//  QByteArray QGb2312Codec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QGb2312Codec5_nameEv() {
  return new QByteArray(QGb2312Codec::_name());
}

//  QList<QByteArray> QGb2312Codec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN12QGb2312Codec8_aliasesEv() {
  return new QList<QByteArray>(QGb2312Codec::_aliases());
}

//  int QGb2312Codec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QGb2312Codec8_mibEnumEv() {
  return QGb2312Codec::_mibEnum();
}

//  QByteArray QGb2312Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QGb2312Codec4nameEv(const QGb2312Codec *self) {
  return new QByteArray(self->name());
}

//  int QGb2312Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGb2312Codec7mibEnumEv(const QGb2312Codec *self) {
  return self->mibEnum();
}

//  QString QGb2312Codec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QGb2312Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QGb2312Codec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QGb2312Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QGb2312Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QGb2312Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQGb2312Codec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGb2312Codec(
    QGb2312Codec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGb2312Codec *>(self)->take(key, call);
}

//  QByteArray QGb2312Codec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QGb2312Codec4nameEv(const QGb2312Codec *self) {
  return new QByteArray(self->QGb2312Codec::name());
}

//  int QGb2312Codec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QGb2312Codec7mibEnumEv(const QGb2312Codec *self) {
  return self->QGb2312Codec::mibEnum();
}

//  QByteArray QGb2312Codec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12QGb2312Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QGb2312Codec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QGb2312Codec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
