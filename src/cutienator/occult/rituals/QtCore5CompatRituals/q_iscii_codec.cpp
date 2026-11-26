//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qisciicodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(codecs) && QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qisciicodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qisciicodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 20, as local:qisciicodec.cpp:Codecs
struct Codecs {
    const char name[10];
    ushort base;
};

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 25, as local:qisciicodec.cpp:codecs
static const Codecs codecs [] = {
    { "iscii-dev", 0x900 },
    { "iscii-bng", 0x980 },
    { "iscii-pnj", 0xa00 },
    { "iscii-gjr", 0xa80 },
    { "iscii-ori", 0xb00 },
    { "iscii-tml", 0xb80 },
    { "iscii-tlg", 0xc00 },
    { "iscii-knd", 0xc80 },
    { "iscii-mlm", 0xd00 }
};

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 64, as local:qisciicodec.cpp:inv
static const uchar inv = 0xFF;

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 67, as local:qisciicodec.cpp:iscii_to_uni_table
static const uchar iscii_to_uni_table[0x60] = {
    0x00, 0x01, 0x02, 0x03,
    0x05, 0x06, 0x07, 0x08,
    0x09, 0x0a, 0x0b, 0x0e,
    0x0f, 0x20, 0x0d, 0x12,

    0x13, 0x14, 0x11, 0x15,
    0x16, 0x17, 0x18, 0x19,
    0x1a, 0x1b, 0x1c, 0x1d,
    0x1e, 0x1f, 0x20, 0x21,

    0x22, 0x23, 0x24, 0x25,
    0x26, 0x27, 0x28, 0x29,
    0x2a, 0x2b, 0x2c, 0x2d,
    0x2e, 0x2f, 0x5f, 0x30,

    0x31, 0x32, 0x33, 0x34,
    0x35, 0x36, 0x37, 0x38,
    0x39,  inv, 0x3e, 0x3f,
    0x40, 0x41, 0x42, 0x43,

    0x46, 0x47, 0x48, 0x45,
    0x4a, 0x4b, 0x4c, 0x49,
    0x4d, 0x3c, 0x64, 0x00,
    0x00, 0x00, 0x00, 0x00,

    0x00, 0x66, 0x67, 0x68,
    0x69, 0x6a, 0x6b, 0x6c,
    0x6d, 0x6e, 0x6f, 0x00,
    0x00, 0x00, 0x00, 0x00
};

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 99, as local:qisciicodec.cpp:uni_to_iscii_table
static const uchar uni_to_iscii_table[0x80] = {
    0x00, 0xa1, 0xa2, 0xa3,
    0x00, 0xa4, 0xa5, 0xa6,
    0xa7, 0xa8, 0xa9, 0xaa,
    0x00, 0xae, 0xab, 0xac,

    0xad, 0xb2, 0xaf, 0xb0,
    0xb1, 0xb3, 0xb4, 0xb5,
    0xb6, 0xb7, 0xb8, 0xb9,
    0xba, 0xbb, 0xbc, 0xbd,

    0xbe, 0xbf, 0xc0, 0xc1,
    0xc2, 0xc3, 0xc4, 0xc5,
    0xc6, 0xc7, 0xc8, 0xc9,
    0xca, 0xcb, 0xcc, 0xcd,

    0xcf, 0xd0, 0xd1, 0xd2,
    0xd3, 0xd4, 0xd5, 0xd6,
    0xd7, 0xd8, 0x00, 0x00,
    0xe9, 0x00, 0xda, 0xdb,

    0xdc, 0xdd, 0xde, 0xdf,
    0x00, 0xe3, 0xe0, 0xe1,
    0xe2, 0xe7, 0xe4, 0xe5,
    0xe6, 0xe8, 0x00, 0x00,

    0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00,
    0x01, 0x02, 0x03, 0x04, // decomposable into the uc codes listed here + nukta
    0x05, 0x06, 0x07, 0xce,

    0x00, 0x00, 0x00, 0x00,
    0xea, 0x08, 0xf1, 0xf2,
    0xf3, 0xf4, 0xf5, 0xf6,
    0xf7, 0xf8, 0xf9, 0xfa,

    0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00
};

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 141, as local:qisciicodec.cpp:uni_to_iscii_pairs
static const uchar uni_to_iscii_pairs[] = {
    0x00, 0x00,
    0x15, 0x3c, // 0x958
    0x16, 0x3c, // 0x959
    0x17, 0x3c, // 0x95a
    0x1c, 0x3c, // 0x95b
    0x21, 0x3c, // 0x95c
    0x22, 0x3c, // 0x95d
    0x2b, 0x3c, // 0x95e
    0x64, 0x64  // 0x965
};

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 221, as _ZNK11QIsciiCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QIsciiCodec::convertToUnicode(const char* chars, int len, ConverterState *state) const
{
    bool halant = false;
    if (state) {
        halant = state->state_data[0];
    }

    QString result(len, QT_PREPEND_NAMESPACE(Qt::Uninitialized));
    QChar *uc = result.data();

    const int base = codecs[idx].base;

    for (int i = 0; i < len; ++i) {
        char16_t ch = (uchar) chars[i];
        if (ch < 0xa0)
            *uc++ = ch;
        else {
            ushort c = iscii_to_uni_table[ch - 0xa0];
            if (halant && (ch == inv || ch == 0xe9)) {
                // Consonant Halant inv -> Consonant Halant ZWJ
                // Consonant Halant Nukta -> Consonant Halant ZWJ
                *uc++ = QChar(0x200d);
            } else if (halant && ch == 0xe8) {
                // Consonant Halant Halant -> Consonant Halant ZWNJ
                *uc++ = QChar(0x200c);
            } else {
                *uc++ = QChar(c+base);
            }
        }
        halant = ((uchar)chars[i] == 0xe8);
    }
    result.resize(uc - result.unicode());

    if (state) {
        state->state_data[0] = halant;
    }
    return result;
}

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 53, as _ZNK11QIsciiCodec4nameEv
inline QByteArray QIsciiCodec::name() const
{
  return codecs[idx].name;
}

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 58, as _ZNK11QIsciiCodec7mibEnumEv
inline int QIsciiCodec::mibEnum() const
{
    /* There is no MIBEnum for Iscii */
    return -3000-idx;
}

//  from ../qt5compat/src/core5/codecs/qisciicodec.cpp, line 49, as _ZN11QIsciiCodecD1Ev
inline QIsciiCodec::~QIsciiCodec()
{
}
//  -----------------------------------------------------------------------

//  A QIsciiCodec that Python can take functions over in. Every QIsciiCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQIsciiCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef int (*CuteQIsciiCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQIsciiCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQIsciiCodec : public QIsciiCodec {
public:
  using QIsciiCodec::QIsciiCodec;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  QByteArray QIsciiCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIsciiCodecCall0 call = reinterpret_cast<CuteQIsciiCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QIsciiCodec::name();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  int QIsciiCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIsciiCodecCall1 call = reinterpret_cast<CuteQIsciiCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QIsciiCodec::mibEnum();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  QByteArray QIsciiCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQIsciiCodecCall2 call = reinterpret_cast<CuteQIsciiCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QIsciiCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QIsciiCodec::~QIsciiCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIsciiCodecD1Ev(QIsciiCodec *self) {
  delete self;
}

//  QByteArray QIsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QIsciiCodec4nameEv(const QIsciiCodec *self) {
  return new QByteArray(self->name());
}

//  int QIsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QIsciiCodec7mibEnumEv(const QIsciiCodec *self) {
  return self->mibEnum();
}

//  QString QIsciiCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIsciiCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QIsciiCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QIsciiCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QIsciiCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QIsciiCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQIsciiCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIsciiCodec(
    QIsciiCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIsciiCodec *>(self)->take(key, call);
}

//  QByteArray QIsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QIsciiCodec4nameEv(const QIsciiCodec *self) {
  return new QByteArray(self->QIsciiCodec::name());
}

//  int QIsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QIsciiCodec7mibEnumEv(const QIsciiCodec *self) {
  return self->QIsciiCodec::mibEnum();
}

#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(codecs) && QT_CONFIG(textcodec)
