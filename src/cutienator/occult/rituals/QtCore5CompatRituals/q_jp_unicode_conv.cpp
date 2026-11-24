//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qjpunicode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(big_codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qjpunicode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qjpunicode_p.h>
#include <QtCore/qbytearray.h>
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 720, as _ZN14QJpUnicodeConv12newConverterEi
inline QJpUnicodeConv *QJpUnicodeConv::newConverter(int rule)
{
    QByteArray env = qgetenv("UNICODEMAP_JP");
    if (rule == Default && !env.isNull()) {
        for (int i = 0; i < (int)env.length();) {
            int j = env.indexOf(',', i);
            QByteArray part;
            if (j < 0) {
                part = env.mid(i).trimmed();
                i = env.length();
            } else {
                part = env.mid(i, j - i).trimmed();
                i = j + 1;
            }
            const auto s = part.constData();
            if (qstricmp(s, "unicode-0.9") == 0) {
                rule = (rule & 0xff00) | Unicode;
            } else if (qstricmp(s, "unicode-0201") == 0) {
                rule = (rule & 0xff00) | Unicode_JISX0201;
            } else if (qstricmp(s, "unicode-ascii") == 0) {
                rule = (rule & 0xff00) | Unicode_ASCII;
            } else if (qstricmp(s, "jisx0221-1995") == 0) {
                rule = (rule & 0xff00) | JISX0221_JISX0201;
            } else if ((qstricmp(s, "open-0201") == 0) ||
                       (qstricmp(s, "open-19970715-0201") == 0)) {
                rule = (rule & 0xff00) | JISX0221_JISX0201;
            } else if ((qstricmp(s, "open-ascii") == 0) ||
                       (qstricmp(s, "open-19970715-ascii") == 0)) {
                rule = (rule & 0xff00) | JISX0221_ASCII;
            } else if ((qstricmp(s, "open-ms") == 0) ||
                       (qstricmp(s, "open-19970715-ms") == 0)) {
                rule = (rule & 0xff00) | Microsoft_CP932;
            } else if (qstricmp(s, "cp932") == 0) {
                rule = (rule & 0xff00) | Microsoft_CP932;
            } else if (qstricmp(s, "jdk1.1.7") == 0) {
                rule = (rule & 0xff00) | Sun_JDK117;
            } else if (qstricmp(s, "nec-vdc") == 0) {
                rule = rule | NEC_VDC;
            } else if (qstricmp(s, "ibm-vdc") == 0) {
                rule = rule | IBM_VDC;
            } else if (qstricmp(s, "udc") == 0) {
                rule = rule | UDC;
            }
        }
    }

    switch (rule & 0x00ff) {
    case Unicode_JISX0201:
        return new QJpUnicodeConv_Unicode_JISX0201(rule);
    case Unicode_ASCII:
        return new QJpUnicodeConv_Unicode_ASCII(rule);
    case JISX0221_JISX0201:
        return new QJpUnicodeConv_JISX0221_JISX0201(rule);
    case JISX0221_ASCII:
        return new QJpUnicodeConv_JISX0221_ASCII(rule);
    case Sun_JDK117:
        return new QJpUnicodeConv_Sun(rule);
    case Microsoft_CP932:
        return new QJpUnicodeConv_Microsoft(rule);
    default:
        return new QJpUnicodeConv_Unicode_ASCII(rule);
    }
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 73, as _ZNK14QJpUnicodeConv17jisx0201ToUnicodeEjj
inline uint QJpUnicodeConv::jisx0201ToUnicode(uint h, uint l) const
{
    if (h == 0) {
        if (IsLatin(l)) {
            return jisx0201LatinToUnicode(h, l);
        } else if (IsKana(l)) {
            return jisx0201KanaToUnicode(h, l);
        }
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 99, as _ZNK14QJpUnicodeConv21jisx0201KanaToUnicodeEjj
inline uint QJpUnicodeConv::jisx0201KanaToUnicode(uint h, uint l) const
{
    if ((h == 0) && IsKana(l)) {
        return jisx0201ToUnicode11(h, l);
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 162, as _ZNK14QJpUnicodeConv17unicodeToJisx0201Ejj
inline uint QJpUnicodeConv::unicodeToJisx0201(uint h, uint l) const
{
    uint jis;
    if ((jis = unicodeToJisx0201Latin(h, l)) != 0) {
        return jis;
    } else if ((jis = unicodeToJisx0201Kana(h, l)) != 0) {
        return jis;
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 188, as _ZNK14QJpUnicodeConv21unicodeToJisx0201KanaEjj
inline uint QJpUnicodeConv::unicodeToJisx0201Kana(uint h, uint l) const
{
    uint jis = unicode11ToJisx0201(h, l);
    if (IsKana(jis)) {
        return jis;
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 247, as _ZNK14QJpUnicodeConv13sjisToUnicodeEjj
inline uint QJpUnicodeConv::sjisToUnicode(uint h, uint l) const
{
    if (h == 0) {
        return jisx0201ToUnicode(h, l);
    } else if (IsSjisChar1(h) && IsSjisChar2(l)) {
        return jisx0208ToUnicode(sjisToJisx0208(h, l));
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 260, as _ZNK14QJpUnicodeConv13unicodeToSjisEjj
inline uint QJpUnicodeConv::unicodeToSjis(uint h, uint l) const
{
    uint jis;
    if ((jis = unicodeToJisx0201(h, l)) != 0x0000) {
        return jis;
    } else if ((jis = unicodeToJisx0208(h, l)) != 0x0000) {
        return jisx0208ToSjis(jis);
    } else if ((jis = unicodeToJisx0212(h, l)) != 0x0000) {
        return 0x0000;
    }
    return 0x0000;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 10493, as _ZNK14QJpUnicodeConv19sjisibmvdcToUnicodeEjj
inline uint QJpUnicodeConv::sjisibmvdcToUnicode(uint h, uint l) const
{
    if (((rule & IBM_VDC) || (rule & Microsoft_CP932))  && IsSjisIBMVDCChar1(h))
          return sjis208ibmvdc_unicode[((h - 0x00fa)*189 + (l-0x0040))];
    else
        return 0;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 10501, as _ZNK14QJpUnicodeConv19unicodeToSjisibmvdcEjj
inline uint QJpUnicodeConv::unicodeToSjisibmvdc(uint h, uint l) const
{
    if ((rule & IBM_VDC) || (rule & Microsoft_CP932)) {
        uint u = (h<<8) | l;
        //since there is no direct mapping, do a linear search
       for (uint i =0; i<sizeof(sjis208ibmvdc_unicode)/sizeof(short) ; i++) {
           //the table has zeros after 0xfc4b
           if (!sjis208ibmvdc_unicode[i])
               return 0;
           if (u==sjis208ibmvdc_unicode[i]){
               return (((0x00fa +(i/189))<<8) | (0x0040+(i%189)));
           }
       }
    }
    return 0;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 10587, as _ZNK14QJpUnicodeConv14cp932ToUnicodeEjj
inline uint QJpUnicodeConv::cp932ToUnicode(uint h, uint l) const
{
    if (rule & Microsoft_CP932) {
        if (h == 0x0087 && (l >= 0x0040 && l <= 0x009c))
            return cp932_87_unicode[l-0x0040];
        else if ((h == 0x00ed || h == 0x00ee)  && (l >= 0x0040 && l <= 0x00fc))
            return cp932_ed_ee_unicode[((h - 0x00ed)*189 + (l-0x0040))];
    }
    return 0;
}

//  from ../qt5compat/src/core5/codecs/qjpunicode.cpp, line 10598, as _ZNK14QJpUnicodeConv14unicodeToCp932Ejj
inline uint QJpUnicodeConv::unicodeToCp932(uint h, uint l) const
{
    if ((rule & Microsoft_CP932)) {
        uint u = (h<<8) | l;
        //since there is no direct mapping, do a linear search
        for (uint i =0; i<sizeof(cp932_87_unicode)/sizeof(short) ; i++) {
           //the table has zeros for some characters
           if (!cp932_87_unicode[i])
               return 0;
           if (u == cp932_87_unicode[i]){
               return ((0x0087<<8) | (0x0040+i));
           }
        }
       for (uint j =0; j<sizeof(cp932_ed_ee_unicode)/sizeof(short) ; j++) {
           if (!cp932_ed_ee_unicode[j])
               return 0;
           if (u==cp932_ed_ee_unicode[j]){
               return (((0x00ed +(j/189))<<8) | (0x0040+(j%189)));
           }
       }
    }
    return 0;
}
//  -----------------------------------------------------------------------

//  A QJpUnicodeConv that Python can take functions over in. Every QJpUnicodeConv
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall0)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall1)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall2)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall3)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall4)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall5)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall6)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
typedef uint (*CuteQJpUnicodeConvCall7)(const void *, uint, uint, int *);
#endif  // QT_CONFIG(big_codecs)
class CuteQJpUnicodeConv : public QJpUnicodeConv {
public:
  using QJpUnicodeConv::QJpUnicodeConv;
  CuteQJpUnicodeConv(const QJpUnicodeConv &other) : QJpUnicodeConv(other) {}
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv14asciiToUnicodeEjj")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv14unicodeToAsciiEjj")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
#if QT_CONFIG(big_codecs)
    if (!std::strcmp(key, "_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(big_codecs)
    return false;
  }

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::asciiToUnicode(uint h, uint l) const
  uint asciiToUnicode(uint h, uint l) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQJpUnicodeConvCall0 call = reinterpret_cast<CuteQJpUnicodeConvCall0>(taken[0]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::asciiToUnicode(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint h, uint l) const
  uint jisx0201LatinToUnicode(uint h, uint l) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQJpUnicodeConvCall1 call = reinterpret_cast<CuteQJpUnicodeConvCall1>(taken[1]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::jisx0201LatinToUnicode(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::jisx0208ToUnicode(uint h, uint l) const
  uint jisx0208ToUnicode(uint h, uint l) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQJpUnicodeConvCall2 call = reinterpret_cast<CuteQJpUnicodeConvCall2>(taken[2]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::jisx0208ToUnicode(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::jisx0212ToUnicode(uint h, uint l) const
  uint jisx0212ToUnicode(uint h, uint l) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQJpUnicodeConvCall3 call = reinterpret_cast<CuteQJpUnicodeConvCall3>(taken[3]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::jisx0212ToUnicode(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::unicodeToAscii(uint h, uint l) const
  uint unicodeToAscii(uint h, uint l) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQJpUnicodeConvCall4 call = reinterpret_cast<CuteQJpUnicodeConvCall4>(taken[4]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::unicodeToAscii(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint h, uint l) const
  uint unicodeToJisx0201Latin(uint h, uint l) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQJpUnicodeConvCall5 call = reinterpret_cast<CuteQJpUnicodeConvCall5>(taken[5]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::unicodeToJisx0201Latin(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::unicodeToJisx0208(uint h, uint l) const
  uint unicodeToJisx0208(uint h, uint l) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQJpUnicodeConvCall6 call = reinterpret_cast<CuteQJpUnicodeConvCall6>(taken[6]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::unicodeToJisx0208(h, l);
  }
#endif  // QT_CONFIG(big_codecs)

#if QT_CONFIG(big_codecs)
  //  uint QJpUnicodeConv::unicodeToJisx0212(uint h, uint l) const
  uint unicodeToJisx0212(uint h, uint l) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQJpUnicodeConvCall7 call = reinterpret_cast<CuteQJpUnicodeConvCall7>(taken[7]);
      uint given = call(this, h, l, &handled);
      if (handled) return given;
    }
    return QJpUnicodeConv::unicodeToJisx0212(h, l);
  }
#endif  // QT_CONFIG(big_codecs)
};

//  QJpUnicodeConv::~QJpUnicodeConv()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QJpUnicodeConvD1Ev(QJpUnicodeConv *self) {
  delete self;
}

//  QJpUnicodeConv *QJpUnicodeConv::newConverter(int rule)
extern "C" Q_DECL_EXPORT
QJpUnicodeConv *ritual_ZN14QJpUnicodeConv12newConverterEi(int rule) {
  return QJpUnicodeConv::newConverter(rule);
}

//  uint QJpUnicodeConv::asciiToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14asciiToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->asciiToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0201ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0201ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->jisx0201ToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->jisx0201LatinToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0201KanaToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv21jisx0201KanaToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->jisx0201KanaToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0208ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->jisx0208ToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0212ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->jisx0212ToUnicode(h, l);
}

//  uint QJpUnicodeConv::asciiToUnicode(uint ascii) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14asciiToUnicodeEj(
    const QJpUnicodeConv *self,
    uint ascii) {
  return self->asciiToUnicode(ascii);
}

//  uint QJpUnicodeConv::jisx0201ToUnicode(uint jis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0201ToUnicodeEj(
    const QJpUnicodeConv *self,
    uint jis) {
  return self->jisx0201ToUnicode(jis);
}

//  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint jis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEj(
    const QJpUnicodeConv *self,
    uint jis) {
  return self->jisx0201LatinToUnicode(jis);
}

//  uint QJpUnicodeConv::jisx0201KanaToUnicode(uint jis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv21jisx0201KanaToUnicodeEj(
    const QJpUnicodeConv *self,
    uint jis) {
  return self->jisx0201KanaToUnicode(jis);
}

//  uint QJpUnicodeConv::jisx0208ToUnicode(uint jis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEj(
    const QJpUnicodeConv *self,
    uint jis) {
  return self->jisx0208ToUnicode(jis);
}

//  uint QJpUnicodeConv::jisx0212ToUnicode(uint jis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEj(
    const QJpUnicodeConv *self,
    uint jis) {
  return self->jisx0212ToUnicode(jis);
}

//  uint QJpUnicodeConv::unicodeToAscii(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14unicodeToAsciiEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToAscii(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0201(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0201Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToJisx0201(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToJisx0201Latin(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0201Kana(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv21unicodeToJisx0201KanaEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToJisx0201Kana(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0208(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToJisx0208(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0212(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToJisx0212(h, l);
}

//  uint QJpUnicodeConv::unicodeToAscii(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14unicodeToAsciiEj(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToAscii(unicode);
}

//  uint QJpUnicodeConv::unicodeToJisx0201(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0201Ej(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToJisx0201(unicode);
}

//  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEj(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToJisx0201Latin(unicode);
}

//  uint QJpUnicodeConv::unicodeToJisx0201Kana(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv21unicodeToJisx0201KanaEj(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToJisx0201Kana(unicode);
}

//  uint QJpUnicodeConv::unicodeToJisx0208(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0208Ej(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToJisx0208(unicode);
}

//  uint QJpUnicodeConv::unicodeToJisx0212(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv17unicodeToJisx0212Ej(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToJisx0212(unicode);
}

//  uint QJpUnicodeConv::sjisToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv13sjisToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->sjisToUnicode(h, l);
}

//  uint QJpUnicodeConv::unicodeToSjis(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv13unicodeToSjisEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToSjis(h, l);
}

//  uint QJpUnicodeConv::sjisibmvdcToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv19sjisibmvdcToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->sjisibmvdcToUnicode(h, l);
}

//  uint QJpUnicodeConv::unicodeToSjisibmvdc(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv19unicodeToSjisibmvdcEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToSjisibmvdc(h, l);
}

//  uint QJpUnicodeConv::cp932ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14cp932ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->cp932ToUnicode(h, l);
}

//  uint QJpUnicodeConv::unicodeToCp932(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv14unicodeToCp932Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->unicodeToCp932(h, l);
}

//  uint QJpUnicodeConv::sjisToUnicode(uint sjis) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv13sjisToUnicodeEj(
    const QJpUnicodeConv *self,
    uint sjis) {
  return self->sjisToUnicode(sjis);
}

//  uint QJpUnicodeConv::unicodeToSjis(uint unicode) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QJpUnicodeConv13unicodeToSjisEj(
    const QJpUnicodeConv *self,
    uint unicode) {
  return self->unicodeToSjis(unicode);
}

//  QJpUnicodeConv::QJpUnicodeConv(int r)
extern "C" Q_DECL_EXPORT
QJpUnicodeConv *ritual_ZN14QJpUnicodeConvC1Ei(int r) {
  return new CuteQJpUnicodeConv(r);
}

//  a Python function taken by a CuteQJpUnicodeConv, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJpUnicodeConv(
    QJpUnicodeConv *self,
    const char *key,
    void *call) {
  return static_cast<CuteQJpUnicodeConv *>(self)->take(key, call);
}

//  uint QJpUnicodeConv::asciiToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv14asciiToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::asciiToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::jisx0201LatinToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0208ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::jisx0208ToUnicode(h, l);
}

//  uint QJpUnicodeConv::jisx0212ToUnicode(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::jisx0212ToUnicode(h, l);
}

//  uint QJpUnicodeConv::unicodeToAscii(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv14unicodeToAsciiEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::unicodeToAscii(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::unicodeToJisx0201Latin(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0208(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::unicodeToJisx0208(h, l);
}

//  uint QJpUnicodeConv::unicodeToJisx0212(uint h, uint l) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj(
    const QJpUnicodeConv *self,
    uint h,
    uint l) {
  return self->QJpUnicodeConv::unicodeToJisx0212(h, l);
}

#endif  // QT_CONFIG(big_codecs)
#endif  // QT_CONFIG(big_codecs) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
