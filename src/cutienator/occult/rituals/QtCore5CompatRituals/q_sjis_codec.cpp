//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qsjiscodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qsjiscodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qsjiscodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 163, as _ZN10QSjisCodec5_nameEv
inline QByteArray QSjisCodec::_name()
{
    return "Shift_JIS";
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 171, as _ZN10QSjisCodec8_aliasesEv
inline QList<QByteArray> QSjisCodec::_aliases()
{
    QList<QByteArray> list;
    list << "SJIS" // Qt 3 compat
         << "MS_Kanji";
    return list;
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 158, as _ZN10QSjisCodec8_mibEnumEv
inline int QSjisCodec::_mibEnum()
{
    return 17;
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 91, as _ZNK10QSjisCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QSjisCodec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    uchar buf[1] = {0};
    int nbuf = 0;
    QChar replacement = QChar::ReplacementCharacter;
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = QChar::Null;
        nbuf = state->remainingChars;
        buf[0] = state->state_data[0];
    }
    int invalid = 0;
    uint u= 0;
    QString result;
    for (int i=0; i<len; i++) {
        uchar ch = chars[i];
        switch (nbuf) {
        case 0:
            if (ch < 0x80) {
                result += QValidChar(ch);
            } else if (IsKana(ch)) {
                // JIS X 0201 Latin or JIS X 0201 Kana
                u = conv->jisx0201ToUnicode(ch);
                result += QValidChar(u);
            } else if (IsSjisChar1(ch)) {
                // JIS X 0208
                buf[0] = ch;
                nbuf = 1;
            } else {
                // Invalid
                result += replacement;
                ++invalid;
            }
            break;
        case 1:
            // JIS X 0208
            if (IsSjisChar2(ch)) {
                if ((u = conv->sjisibmvdcToUnicode(buf[0], ch))) {
                    result += QValidChar(u);
                } else if ((u = conv->cp932ToUnicode(buf[0], ch))) {
                    result += QValidChar(u);
                }
                else if (IsUserDefinedChar1(buf[0])) {
                    result += QChar::ReplacementCharacter;
                } else {
                    u = conv->sjisToUnicode(buf[0], ch);
                    result += QValidChar(u);
                }
            } else {
                // Invalid
                result += replacement;
                ++invalid;
            }
            nbuf = 0;
            break;
        }
    }

    if (state) {
        state->remainingChars = nbuf;
        state->state_data[0] = buf[0];
        state->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 39, as _ZNK10QSjisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QSjisCodec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
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
        QChar ch = uc[i];
        uint j;
        if (ch.row() == 0x00 && ch.cell() < 0x80) {
            // ASCII
            *cursor++ = ch.cell();
        } else if ((j = conv->unicodeToJisx0201(ch.row(), ch.cell())) != 0) {
            // JIS X 0201 Latin or JIS X 0201 Kana
            *cursor++ = j;
        } else if ((j = conv->unicodeToSjis(ch.row(), ch.cell())) != 0) {
            // JIS X 0208
            *cursor++ = (j >> 8);
            *cursor++ = (j & 0xff);
        } else if ((j = conv->unicodeToSjisibmvdc(ch.row(), ch.cell())) != 0) {
            // JIS X 0208 IBM VDC
            *cursor++ = (j >> 8);
            *cursor++ = (j & 0xff);
        } else if ((j = conv->unicodeToCp932(ch.row(), ch.cell())) != 0) {
            // CP932 (for lead bytes 87, ee & ed)
            *cursor++ = (j >> 8);
            *cursor++ = (j & 0xff);
        } else if ((j = conv->unicodeToJisx0212(ch.row(), ch.cell())) != 0) {
            // JIS X 0212 (can't be encoded in ShiftJIS !)
            *cursor++ = 0x81;        // white square
            *cursor++ = 0xa0;        // white square
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

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 24, as _ZN10QSjisCodecC1Ev
inline QSjisCodec::QSjisCodec() : conv(QJpUnicodeConv::newConverter(QJpUnicodeConv::Default))
{
}

//  from ../qt5compat/src/core5/codecs/qsjiscodec.cpp, line 32, as _ZN10QSjisCodecD1Ev
inline QSjisCodec::~QSjisCodec()
{
    delete (const QJpUnicodeConv*)conv;
    conv = 0;
}
//  -----------------------------------------------------------------------

//  A QSjisCodec that Python can take functions over in. Every QSjisCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQSjisCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQSjisCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQSjisCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQSjisCodec : public QSjisCodec {
public:
  using QSjisCodec::QSjisCodec;
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
  //  QByteArray QSjisCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSjisCodecCall0 call = reinterpret_cast<CuteQSjisCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSjisCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QSjisCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSjisCodecCall1 call = reinterpret_cast<CuteQSjisCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSjisCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QSjisCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSjisCodecCall2 call = reinterpret_cast<CuteQSjisCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QSjisCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QSjisCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QSjisCodec5_nameEv() {
  return new QByteArray(QSjisCodec::_name());
}

//  QList<QByteArray> QSjisCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN10QSjisCodec8_aliasesEv() {
  return new QList<QByteArray>(QSjisCodec::_aliases());
}

//  int QSjisCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSjisCodec8_mibEnumEv() {
  return QSjisCodec::_mibEnum();
}

//  QByteArray QSjisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QSjisCodec4nameEv(const QSjisCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QSjisCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK10QSjisCodec7aliasesEv(const QSjisCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QSjisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSjisCodec7mibEnumEv(const QSjisCodec *self) {
  return self->mibEnum();
}

//  QString QSjisCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSjisCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QSjisCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QSjisCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QSjisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QSjisCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  QSjisCodec::QSjisCodec()
extern "C" Q_DECL_EXPORT
QSjisCodec *ritual_ZN10QSjisCodecC1Ev() {
  return new CuteQSjisCodec();
}

//  QSjisCodec::~QSjisCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSjisCodecD1Ev(QSjisCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQSjisCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSjisCodec(QSjisCodec *self, const char *key, void *call) {
  return static_cast<CuteQSjisCodec *>(self)->take(key, call);
}

//  QByteArray QSjisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QSjisCodec4nameEv(const QSjisCodec *self) {
  return new QByteArray(self->QSjisCodec::name());
}

//  int QSjisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QSjisCodec7mibEnumEv(const QSjisCodec *self) {
  return self->QSjisCodec::mibEnum();
}

//  QByteArray QSjisCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK10QSjisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QSjisCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QSjisCodec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
