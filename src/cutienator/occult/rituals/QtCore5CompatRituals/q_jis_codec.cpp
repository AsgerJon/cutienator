//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qjiscodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qjiscodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qjiscodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 316, as _ZN9QJisCodec5_nameEv
inline QByteArray QJisCodec::_name()
{
    return "ISO-2022-JP";
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 324, as _ZN9QJisCodec8_aliasesEv
inline QList<QByteArray> QJisCodec::_aliases()
{
    QList<QByteArray> list;
    list << "JIS7"; // Qt 3 compat
    return list;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 308, as _ZN9QJisCodec8_mibEnumEv
inline int QJisCodec::_mibEnum()
{
    return 39;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 140, as _ZNK9QJisCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QJisCodec::convertToUnicode(const char* chars, int len, ConverterState *cs) const
{
    uchar buf[4] = {0, 0, 0, 0};
    int nbuf = 0;
    Iso2022State state = Ascii, prev = Ascii;
    bool esc = false;
    QChar replacement = QChar::ReplacementCharacter;
    if (cs) {
        if (cs->flags & ConvertInvalidToNull)
            replacement = QChar::Null;
        nbuf = cs->remainingChars;
        buf[0] = (cs->state_data[0] >> 24) & 0xff;
        buf[1] = (cs->state_data[0] >> 16) & 0xff;
        buf[2] = (cs->state_data[0] >>  8) & 0xff;
        buf[3] = (cs->state_data[0] >>  0) & 0xff;
        state = (Iso2022State)((cs->state_data[1] >>  0) & 0xff);
        prev = (Iso2022State)((cs->state_data[1] >>  8) & 0xff);
        esc = cs->state_data[2];
    }
    int invalid = 0;

    QString result;
    for (int i=0; i<len; i++) {
        uchar ch = chars[i];
        if (esc) {
            // Escape sequence
            state = UnknownState;
            switch (nbuf) {
            case 0:
                if (ch == '$' || strchr(Esc_CHARS, ch)) {
                    buf[nbuf++] = ch;
                } else {
                    nbuf = 0;
                    esc = false;
                }
                break;
            case 1:
                if (buf[0] == '$') {
                    if (strchr(Esc_CHARS, ch)) {
                        buf[nbuf++] = ch;
                    } else {
                        switch (ch) {
                        case '@':
                            state = JISX0208_1978;        // Esc $ @
                            break;
                        case 'B':
                            state = JISX0208_1983;        // Esc $ B
                            break;
                        }
                        nbuf = 0;
                        esc = false;
                    }
                } else {
                    if (buf[0] == '(') {
                        switch (ch) {
                        case 'B':
                            state = Ascii;        // Esc (B
                            break;
                        case 'I':
                            state = JISX0201_Kana;        // Esc (I
                            break;
                        case 'J':
                            state = JISX0201_Latin;        // Esc (J
                            break;
                        }
                    }
                    nbuf = 0;
                    esc = false;
                }
                break;
            case 2:
                if (buf[1] == '(') {
                    switch (ch) {
                    case 'D':
                        state = JISX0212;        // Esc $ (D
                        break;
                    }
                }
                nbuf = 0;
                esc = false;
                break;
            }
        } else {
            if (ch == Esc) {
                // Escape sequence
                nbuf = 0;
                esc = true;
            } else if (ch == So) {
                // Shift out
                prev = state;
                state = JISX0201_Kana;
                nbuf = 0;
            } else if (ch == Si) {
                // Shift in
                if (prev == Ascii || prev == JISX0201_Latin) {
                    state = prev;
                } else {
                    state = Ascii;
                }
                nbuf = 0;
            } else {
                uint u;
                switch (nbuf) {
                case 0:
                    switch (state) {
                    case Ascii:
                        if (ch < 0x80) {
                            result += QLatin1Char(ch);
                            break;
                        }
                        Q_FALLTHROUGH();
                    case JISX0201_Latin:
                        u = conv->jisx0201ToUnicode(ch);
                        result += QValidChar(u);
                        break;
                    case JISX0201_Kana:
                        u = conv->jisx0201ToUnicode(ch | 0x80);
                        result += QValidChar(u);
                        break;
                    case JISX0208_1978:
                    case JISX0208_1983:
                    case JISX0212:
                        buf[nbuf++] = ch;
                        break;
                    default:
                        result += QChar::ReplacementCharacter;
                        break;
                    }
                    break;
                case 1:
                    switch (state) {
                    case JISX0208_1978:
                    case JISX0208_1983:
                        u = conv->jisx0208ToUnicode(buf[0] & 0x7f, ch & 0x7f);
                        result += QValidChar(u);
                        break;
                    case JISX0212:
                        u = conv->jisx0212ToUnicode(buf[0] & 0x7f, ch & 0x7f);
                        result += QValidChar(u);
                        break;
                    default:
                        result += replacement;
                        ++invalid;
                        break;
                    }
                    nbuf = 0;
                    break;
                }
            }
        }
    }

    if (cs) {
        cs->remainingChars = nbuf;
        cs->invalidChars += invalid;
        cs->state_data[0] = (buf[0] << 24) + (buf[1] << 16) + (buf[2] << 8) + buf[3];
        cs->state_data[1] = (prev << 8) + state;
        cs->state_data[2] = esc;
    }

    return result;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 69, as _ZNK9QJisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QJisCodec::convertFromUnicode(const QChar *uc, int len, ConverterState *cs) const
{
    char replacement = '?';
    if (cs) {
        if (cs->flags & ConvertInvalidToNull)
            replacement = 0;
    }
    int invalid = 0;

    QByteArray result;
    Iso2022State state = Ascii;
    Iso2022State prev = Ascii;
    for (int i = 0; i < len; i++) {
        QChar ch = uc[i];
        uint j;
        if (ch.row() == 0x00 && ch.cell() < 0x80) {
            // Ascii
            if (state != JISX0201_Latin ||
                ch.cell() == ReverseSolidus || ch.cell() == Tilde) {
                state = Ascii;
            }
            j = ch.cell();
        } else if ((j = conv->unicodeToJisx0201(ch.row(), ch.cell())) != 0) {
            if (j < 0x80) {
                // JIS X 0201 Latin
                if (state != Ascii ||
                    ch.cell() == YenSign || ch.cell() == Overline) {
                    state = JISX0201_Latin;
                }
            } else {
                // JIS X 0201 Kana
                state = JISX0201_Kana;
                j &= 0x7f;
            }
        } else if ((j = conv->unicodeToJisx0208(ch.row(), ch.cell())) != 0) {
            // JIS X 0208
            state = JISX0208_1983;
        } else if ((j = conv->unicodeToJisx0212(ch.row(), ch.cell())) != 0) {
            // JIS X 0212
            state = JISX0212;
        } else {
            // Invalid
            state = UnknownState;
            j = replacement;
            ++invalid;
        }
        if (state != prev) {
            if (state == UnknownState) {
                result += Esc_Ascii;
            } else {
                result += Esc_SEQ[state - MinState];
            }
            prev = state;
        }
        if (j < 0x0100) {
            result += j & 0xff;
        } else {
            result += (j >> 8) & 0xff;
            result += j & 0xff;
        }
    }
    if (prev != Ascii) {
        result += Esc_Ascii;
    }

    if (cs) {
        cs->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 55, as _ZN9QJisCodecC1Ev
inline QJisCodec::QJisCodec() : conv(QJpUnicodeConv::newConverter(QJpUnicodeConv::Default))
{
}

//  from ../qt5compat/src/core5/codecs/qjiscodec.cpp, line 63, as _ZN9QJisCodecD1Ev
inline QJisCodec::~QJisCodec()
{
    delete (const QJpUnicodeConv*)conv;
    conv = 0;
}
//  -----------------------------------------------------------------------

//  A QJisCodec that Python can take functions over in. Every QJisCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQJisCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQJisCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQJisCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQJisCodec : public QJisCodec {
public:
  using QJisCodec::QJisCodec;
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
  //  QByteArray QJisCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQJisCodecCall0 call = reinterpret_cast<CuteQJisCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QJisCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QJisCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQJisCodecCall1 call = reinterpret_cast<CuteQJisCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QJisCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QJisCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQJisCodecCall2 call = reinterpret_cast<CuteQJisCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QJisCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QJisCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QJisCodec5_nameEv() {
  return new QByteArray(QJisCodec::_name());
}

//  QList<QByteArray> QJisCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QJisCodec8_aliasesEv() {
  return new QList<QByteArray>(QJisCodec::_aliases());
}

//  int QJisCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJisCodec8_mibEnumEv() {
  return QJisCodec::_mibEnum();
}

//  QByteArray QJisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QJisCodec4nameEv(const QJisCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QJisCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK9QJisCodec7aliasesEv(const QJisCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QJisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QJisCodec7mibEnumEv(const QJisCodec *self) {
  return self->mibEnum();
}

//  QString QJisCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QJisCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QJisCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QJisCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QJisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QJisCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  QJisCodec::QJisCodec()
extern "C" Q_DECL_EXPORT
QJisCodec *ritual_ZN9QJisCodecC1Ev() {
  return new CuteQJisCodec();
}

//  QJisCodec::~QJisCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJisCodecD1Ev(QJisCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQJisCodec, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJisCodec(QJisCodec *self, const char *key, void *call) {
  return static_cast<CuteQJisCodec *>(self)->take(key, call);
}

//  QByteArray QJisCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK9QJisCodec4nameEv(const QJisCodec *self) {
  return new QByteArray(self->QJisCodec::name());
}

//  int QJisCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QJisCodec7mibEnumEv(const QJisCodec *self) {
  return self->QJisCodec::mibEnum();
}

//  QByteArray QJisCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK9QJisCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QJisCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QJisCodec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
