//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbig5codec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbig5codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbig5codec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 1779, as _ZN15QBig5hkscsCodec5_nameEv
inline QByteArray QBig5hkscsCodec::_name()
{
    return "Big5-HKSCS";
}

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 1773, as _ZN15QBig5hkscsCodec8_mibEnumEv
inline int QBig5hkscsCodec::_mibEnum()
{
    return 2101;
}

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 1785, as _ZNK15QBig5hkscsCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QBig5hkscsCodec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    uchar buf[2] = {0};
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

    //qDebug("QBig5hkscsCodec::toUnicode(const char* chars = \"%s\", int len = %d)", chars, len);
    QString result;
    for (int i=0; i<len; i++) {
        uchar ch = chars[i];
        switch (nbuf) {
        case 0:
            if (IsLatin(ch)) {
                // ASCII
                result += QLatin1Char(ch);
            } else if (Is1stByte(ch)) {
                // Big5-HKSCS
                buf[0] = ch;
                nbuf = 1;
            } else {
                // Invalid
                result += replacement;
                ++invalid;
            }
            break;
        case 1:
            if (IsSecondByte(ch)) {
                // Big5-HKSCS
                uint u;
                buf[1] = ch;
                if (qt_Big5hkscsToUnicode(buf, &u) == 2)
                    result += QValidChar(u);
                else {
                    // Error
                    result += replacement;
                    ++invalid;
                }
            } else {
                // Error
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
        state->state_data[1] = buf[1];
        state->invalidChars += invalid;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qbig5codec.cpp, line 1849, as _ZNK15QBig5hkscsCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QBig5hkscsCodec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
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
        uchar c[2];
        if (ch < 0x80) {
            // ASCII
            *cursor++ = ch;
        } else if (qt_UnicodeToBig5hkscs(ch, c) == 2) {
            // Big5-HKSCS
            *cursor++ = c[0];
            *cursor++ = c[1];
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

//  A QBig5hkscsCodec that Python can take functions over in. Every QBig5hkscsCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQBig5hkscsCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef int (*CuteQBig5hkscsCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
typedef const QByteArray * (*CuteQBig5hkscsCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQBig5hkscsCodec : public QBig5hkscsCodec {
public:
  using QBig5hkscsCodec::QBig5hkscsCodec;
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
  //  QByteArray QBig5hkscsCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBig5hkscsCodecCall0 call = reinterpret_cast<CuteQBig5hkscsCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBig5hkscsCodec::name();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  int QBig5hkscsCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBig5hkscsCodecCall1 call = reinterpret_cast<CuteQBig5hkscsCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBig5hkscsCodec::mibEnum();
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(big_codecs)
  //  QByteArray QBig5hkscsCodec::convertFromUnicode(const QChar *a0, int
  //      a1, ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBig5hkscsCodecCall2 call = reinterpret_cast<CuteQBig5hkscsCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QBig5hkscsCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QBig5hkscsCodec::_name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QBig5hkscsCodec5_nameEv() {
  return new QByteArray(QBig5hkscsCodec::_name());
}

//  QList<QByteArray> QBig5hkscsCodec::_aliases()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN15QBig5hkscsCodec8_aliasesEv() {
  return new QList<QByteArray>(QBig5hkscsCodec::_aliases());
}

//  int QBig5hkscsCodec::_mibEnum()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QBig5hkscsCodec8_mibEnumEv() {
  return QBig5hkscsCodec::_mibEnum();
}

//  QByteArray QBig5hkscsCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QBig5hkscsCodec4nameEv(const QBig5hkscsCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QBig5hkscsCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QBig5hkscsCodec7aliasesEv(
    const QBig5hkscsCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QBig5hkscsCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QBig5hkscsCodec7mibEnumEv(const QBig5hkscsCodec *self) {
  return self->mibEnum();
}

//  QString QBig5hkscsCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QBig5hkscsCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QBig5hkscsCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QBig5hkscsCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QBig5hkscsCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QBig5hkscsCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQBig5hkscsCodec, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBig5hkscsCodec(
    QBig5hkscsCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBig5hkscsCodec *>(self)->take(key, call);
}

//  QByteArray QBig5hkscsCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK15QBig5hkscsCodec4nameEv(
    const QBig5hkscsCodec *self) {
  return new QByteArray(self->QBig5hkscsCodec::name());
}

//  int QBig5hkscsCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QBig5hkscsCodec7mibEnumEv(const QBig5hkscsCodec *self) {
  return self->QBig5hkscsCodec::mibEnum();
}

//  QByteArray QBig5hkscsCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK15QBig5hkscsCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QBig5hkscsCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(
      self->QBig5hkscsCodec::convertFromUnicode(
          a0,
          a1,
          a2));
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
