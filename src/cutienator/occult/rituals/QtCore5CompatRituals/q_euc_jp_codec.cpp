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
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qeucjpcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 115, as _ZNK11QEucJpCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QEucJpCodec::convertToUnicode(const char* chars, int len, ConverterState *state) const
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
            } else if (ch == Ss2 || ch == Ss3) {
                // JIS X 0201 Kana or JIS X 0212
                buf[0] = ch;
                nbuf = 1;
            } else if (IsEucChar(ch)) {
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
            if (buf[0] == Ss2) {
                // JIS X 0201 Kana
                if (IsKana(ch)) {
                    uint u = conv->jisx0201ToUnicode(ch);
                    result += QValidChar(u);
                } else {
                    result += replacement;
                    ++invalid;
                }
                nbuf = 0;
            } else if (buf[0] == Ss3) {
                // JIS X 0212-1990
                if (IsEucChar(ch)) {
                    buf[1] = ch;
                    nbuf = 2;
                } else {
                    // Error
                    result += replacement;
                    ++invalid;
                    nbuf = 0;
                }
            } else {
                // JIS X 0208-1990
                if (IsEucChar(ch)) {
                    uint u = conv->jisx0208ToUnicode(buf[0] & 0x7f, ch & 0x7f);
                    result += QValidChar(u);
                } else {
                    // Error
                    result += replacement;
                    ++invalid;
                }
                nbuf = 0;
            }
            break;
        case 2:
            // JIS X 0212
            if (IsEucChar(ch)) {
                uint u = conv->jisx0212ToUnicode(buf[1] & 0x7f, ch & 0x7f);
                result += QValidChar(u);
            } else {
                result += replacement;
                ++invalid;
            }
            nbuf = 0;
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

//  from ../qt5compat/src/core5/codecs/qeucjpcodec.cpp, line 63, as _ZNK11QEucJpCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QEucJpCodec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
{
    char replacement = '?';
    if (state) {
        if (state->flags & ConvertInvalidToNull)
            replacement = 0;
    }
    int invalid = 0;

    int rlen = 3*len + 1;
    QByteArray rstr;
    rstr.resize(rlen);
    uchar* cursor = (uchar*)rstr.data();
    for (int i = 0; i < len; i++) {
        QChar ch = uc[i];
        uint j;
        if (ch.unicode() < 0x80) {
            // ASCII
            *cursor++ = ch.cell();
        } else if ((j = conv->unicodeToJisx0201(ch.row(), ch.cell())) != 0) {
            if (j < 0x80) {
                // JIS X 0201 Latin ?
                *cursor++ = j;
            } else {
                // JIS X 0201 Kana
                *cursor++ = Ss2;
                *cursor++ = j;
            }
        } else if ((j = conv->unicodeToJisx0208(ch.row(), ch.cell())) != 0) {
            // JIS X 0208
            *cursor++ = (j >> 8)   | 0x80;
            *cursor++ = (j & 0xff) | 0x80;
        } else if ((j = conv->unicodeToJisx0212(ch.row(), ch.cell())) != 0) {
            // JIS X 0212
            *cursor++ = Ss3;
            *cursor++ = (j >> 8)   | 0x80;
            *cursor++ = (j & 0xff) | 0x80;
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
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQEucJpCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQEucJpCodec : public QEucJpCodec {
public:
  using QEucJpCodec::QEucJpCodec;
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

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QEucJpCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQEucJpCodecCall2 call = reinterpret_cast<CuteQEucJpCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QEucJpCodec::convertFromUnicode(a0, a1, a2);
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

//  QString QEucJpCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QEucJpCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QEucJpCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QEucJpCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QEucJpCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QEucJpCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
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

//  QByteArray QEucJpCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QEucJpCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QEucJpCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QEucJpCodec::convertFromUnicode(a0, a1, a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
