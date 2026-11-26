//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qtsciicodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(codecs) && QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qtsciicodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qtsciicodec_p.h>
#include <QtCore/qlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 145, as local:qtsciicodec.cpp:UnToTsLast
static const int UnToTsLast = 124;

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 146, as local:qtsciicodec.cpp:UnToTs
static const ushort UnToTs [][4] = {
    // *Sorted* list of TSCII maping for unicode chars
    //FIRST  SECOND  THIRD   TSCII
    {0x00A0, 0x0000, 0x0000, 0xA0},
    {0x00A9, 0x0000, 0x0000, 0xA9},
    {0x0B83, 0x0000, 0x0000, 0xB7},
    {0x0B85, 0x0000, 0x0000, 0xAB},
    {0x0B86, 0x0000, 0x0000, 0xAC},
    {0x0B87, 0x0000, 0x0000, 0xAD},
    {0x0B88, 0x0000, 0x0000, 0xAE},
    {0x0B89, 0x0000, 0x0000, 0xAF},
    {0x0B8A, 0x0000, 0x0000, 0xB0},
    {0x0B8E, 0x0000, 0x0000, 0xB1},
    {0x0B8F, 0x0000, 0x0000, 0xB2},
    {0x0B90, 0x0000, 0x0000, 0xB3},
    {0x0B92, 0x0000, 0x0000, 0xB4},
    {0x0B93, 0x0000, 0x0000, 0xB5},
    {0x0B94, 0x0000, 0x0000, 0xB6},
    {0x0B95, 0x0000, 0x0000, 0xB8},
    {0x0B95, 0x0BC1, 0x0000, 0xCC},
    {0x0B95, 0x0BC2, 0x0000, 0xDC},
    {0x0B95, 0x0BCD, 0x0000, 0xEC},
    {0x0B99, 0x0000, 0x0000, 0xB9},
    {0x0B99, 0x0BC1, 0x0000, 0x99},
    {0x0B99, 0x0BC2, 0x0000, 0x9B},
    {0x0B99, 0x0BCD, 0x0000, 0xED},
    {0x0B9A, 0x0000, 0x0000, 0xBA},
    {0x0B9A, 0x0BC1, 0x0000, 0xCD},
    {0x0B9A, 0x0BC2, 0x0000, 0xDD},
    {0x0B9A, 0x0BCD, 0x0000, 0xEE},
    {0x0B9C, 0x0000, 0x0000, 0x83},
    {0x0B9C, 0x0BCD, 0x0000, 0x88},
    {0x0B9E, 0x0000, 0x0000, 0xBB},
    {0x0B9E, 0x0BCD, 0x0000, 0xEF},
    {0x0B9E, 0x0BC1, 0x0000, 0x9A},
    {0x0B9E, 0x0BC2, 0x0000, 0x9C},
    {0x0B9F, 0x0000, 0x0000, 0xBC},
    {0x0B9F, 0x0BBF, 0x0000, 0xCA},
    {0x0B9F, 0x0BC0, 0x0000, 0xCB},
    {0x0B9F, 0x0BC1, 0x0000, 0xCE},
    {0x0B9F, 0x0BC2, 0x0000, 0xDE},
    {0x0B9F, 0x0BCD, 0x0000, 0xF0},
    {0x0BA3, 0x0000, 0x0000, 0xBD},
    {0x0BA3, 0x0BCD, 0x0000, 0xF1},
    {0x0BA3, 0x0BC1, 0x0000, 0xCF},
    {0x0BA3, 0x0BC2, 0x0000, 0xDF},
    {0x0BA4, 0x0000, 0x0000, 0xBE},
    {0x0BA4, 0x0BC1, 0x0000, 0xD0},
    {0x0BA4, 0x0BC2, 0x0000, 0xE0},
    {0x0BA4, 0x0BCD, 0x0000, 0xF2},
    {0x0BA8, 0x0000, 0x0000, 0xBF},
    {0x0BA8, 0x0BC1, 0x0000, 0xD1},
    {0x0BA8, 0x0BC2, 0x0000, 0xE1},
    {0x0BA8, 0x0BCD, 0x0000, 0xF3},
    {0x0BA9, 0x0000, 0x0000, 0xC9},
    {0x0BA9, 0x0BC1, 0x0000, 0xDB},
    {0x0BA9, 0x0BC2, 0x0000, 0xEB},
    {0x0BA9, 0x0BCD, 0x0000, 0xFD},
    {0x0BAA, 0x0000, 0x0000, 0xC0},
    {0x0BAA, 0x0BC1, 0x0000, 0xD2},
    {0x0BAA, 0x0BC2, 0x0000, 0xE2},
    {0x0BAA, 0x0BCD, 0x0000, 0xF4},
    {0x0BAE, 0x0000, 0x0000, 0xC1},
    {0x0BAE, 0x0BC1, 0x0000, 0xD3},
    {0x0BAE, 0x0BC2, 0x0000, 0xE3},
    {0x0BAE, 0x0BCD, 0x0000, 0xF5},
    {0x0BAF, 0x0000, 0x0000, 0xC2},
    {0x0BAF, 0x0BC1, 0x0000, 0xD4},
    {0x0BAF, 0x0BC2, 0x0000, 0xE4},
    {0x0BAF, 0x0BCD, 0x0000, 0xF6},
    {0x0BB0, 0x0000, 0x0000, 0xC3},
    {0x0BB0, 0x0BC1, 0x0000, 0xD5},
    {0x0BB0, 0x0BC2, 0x0000, 0xE5},
    {0x0BB0, 0x0BCD, 0x0000, 0xF7},
    {0x0BB1, 0x0000, 0x0000, 0xC8},
    {0x0BB1, 0x0BC1, 0x0000, 0xDA},
    {0x0BB1, 0x0BC2, 0x0000, 0xEA},
    {0x0BB1, 0x0BCD, 0x0000, 0xFC},
    {0x0BB2, 0x0000, 0x0000, 0xC4},
    {0x0BB2, 0x0BC1, 0x0000, 0xD6},
    {0x0BB2, 0x0BC2, 0x0000, 0xE6},
    {0x0BB2, 0x0BCD, 0x0000, 0xF8},
    {0x0BB3, 0x0000, 0x0000, 0xC7},
    {0x0BB3, 0x0BC1, 0x0000, 0xD9},
    {0x0BB3, 0x0BC2, 0x0000, 0xE9},
    {0x0BB3, 0x0BCD, 0x0000, 0xFB},
    {0x0BB4, 0x0000, 0x0000, 0xC6},
    {0x0BB4, 0x0BC1, 0x0000, 0xD8},
    {0x0BB4, 0x0BC2, 0x0000, 0xE8},
    {0x0BB4, 0x0BCD, 0x0000, 0xFA},
    {0x0BB5, 0x0000, 0x0000, 0xC5},
    {0x0BB5, 0x0BC1, 0x0000, 0xD7},
    {0x0BB5, 0x0BC2, 0x0000, 0xE7},
    {0x0BB5, 0x0BCD, 0x0000, 0xF9},
    {0x0BB7, 0x0000, 0x0000, 0x84},
    {0x0BB7, 0x0BCD, 0x0000, 0x89},
    {0x0BB8, 0x0000, 0x0000, 0x85},
    {0x0BB8, 0x0BCD, 0x0000, 0x8A},
    {0x0BB9, 0x0000, 0x0000, 0x86},
    {0x0BB9, 0x0BCD, 0x0000, 0x8B},
    {0x0BBE, 0x0000, 0x0000, 0xA1},
    {0x0BBF, 0x0000, 0x0000, 0xA2},
    {0x0BC0, 0x0000, 0x0000, 0xA3},
    {0x0BC1, 0x0000, 0x0000, 0xA4},
    {0x0BC2, 0x0000, 0x0000, 0xA5},
    {0x0BC6, 0x0000, 0x0000, 0xA6},
    {0x0BC7, 0x0000, 0x0000, 0xA7},
    {0x0BC8, 0x0000, 0x0000, 0xA8},
    {0x0BCC, 0x0000, 0x0000, 0xAA},
    {0x0BE6, 0x0000, 0x0000, 0x80},
    {0x0BE7, 0x0000, 0x0000, 0x81},
    {0x0BE7, 0x0BB7, 0x0000, 0x87},
    {0x0BE7, 0x0BB7, 0x0B82, 0x8C},
    {0x0BE8, 0x0000, 0x0000, 0x8D},
    {0x0BE9, 0x0000, 0x0000, 0x8E},
    {0x0BEA, 0x0000, 0x0000, 0x8F},
    {0x0BEB, 0x0000, 0x0000, 0x90},
    {0x0BEC, 0x0000, 0x0000, 0x95},
    {0x0BED, 0x0000, 0x0000, 0x96},
    {0x0BEE, 0x0000, 0x0000, 0x97},
    {0x0BEF, 0x0000, 0x0000, 0x98},
    {0x0BF0, 0x0000, 0x0000, 0x9D},
    {0x0BF1, 0x0000, 0x0000, 0x9E},
    {0x0BF2, 0x0000, 0x0000, 0x9F},
    {0x2018, 0x0000, 0x0000, 0x91},
    {0x2019, 0x0000, 0x0000, 0x92},
    {0x201C, 0x0000, 0x0000, 0x93},
    {0x201C, 0x0000, 0x0000, 0x94}
};

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 130, as _ZNK11QTsciiCodec4nameEv
inline QByteArray QTsciiCodec::name() const
{
    return "TSCII";
}

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 140, as _ZNK11QTsciiCodec7mibEnumEv
inline int QTsciiCodec::mibEnum() const
{
  return 2107;
}

//  from ../qt5compat/src/core5/codecs/qtsciicodec.cpp, line 26, as _ZN11QTsciiCodecD1Ev
inline QTsciiCodec::~QTsciiCodec()
{
}
//  -----------------------------------------------------------------------

//  A QTsciiCodec that Python can take functions over in. Every QTsciiCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQTsciiCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef int (*CuteQTsciiCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
typedef const QByteArray * (*CuteQTsciiCodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
class CuteQTsciiCodec : public QTsciiCodec {
public:
  using QTsciiCodec::QTsciiCodec;
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
  //  QByteArray QTsciiCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTsciiCodecCall0 call = reinterpret_cast<CuteQTsciiCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTsciiCodec::name();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  int QTsciiCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTsciiCodecCall1 call = reinterpret_cast<CuteQTsciiCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTsciiCodec::mibEnum();
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(codecs)
  //  QByteArray QTsciiCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTsciiCodecCall2 call = reinterpret_cast<CuteQTsciiCodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QTsciiCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(textcodec)
};

//  QTsciiCodec::~QTsciiCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTsciiCodecD1Ev(QTsciiCodec *self) {
  delete self;
}

//  QByteArray QTsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTsciiCodec4nameEv(const QTsciiCodec *self) {
  return new QByteArray(self->name());
}

//  int QTsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTsciiCodec7mibEnumEv(const QTsciiCodec *self) {
  return self->mibEnum();
}

//  QString QTsciiCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTsciiCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QTsciiCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QTsciiCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTsciiCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QTsciiCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  a Python function taken by a CuteQTsciiCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTsciiCodec(
    QTsciiCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTsciiCodec *>(self)->take(key, call);
}

//  QByteArray QTsciiCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QTsciiCodec4nameEv(const QTsciiCodec *self) {
  return new QByteArray(self->QTsciiCodec::name());
}

//  int QTsciiCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTsciiCodec7mibEnumEv(const QTsciiCodec *self) {
  return self->QTsciiCodec::mibEnum();
}

#endif  // QT_CONFIG(codecs)
#endif  // QT_CONFIG(codecs) && QT_CONFIG(textcodec)
