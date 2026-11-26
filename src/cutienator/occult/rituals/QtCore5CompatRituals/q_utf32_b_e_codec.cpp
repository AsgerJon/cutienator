//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qutfcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qutfcodec_p.h>
#include <QtCore/qlist.h>
#include <QtCore/qendian.h>
#include <QtCore/qchar.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/private/qstringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 123, as _ZN11QUtf32CodecD2Ev
#if QT_CONFIG(textcodec)
inline QUtf32Codec::~QUtf32Codec()
{
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 135, as _ZNK11QUtf32Codec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
#if QT_CONFIG(textcodec)
inline QString QUtf32Codec::convertToUnicode(const char *chars, int len, ConverterState *state) const
{
    ConverterState s(QStringConverter::Flag::Stateless);
    if (!state)
        state = &s;
    return QUtf32::convertToUnicode(QByteArrayView(chars, len), state, e);
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 127, as _ZNK11QUtf32Codec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
#if QT_CONFIG(textcodec)
inline QByteArray QUtf32Codec::convertFromUnicode(const QChar *uc, int len, ConverterState *state) const
{
    ConverterState s(QStringConverter::Flag::Stateless);
    if (!state)
        state = &s;
    return QUtf32::convertFromUnicode(QStringView(uc, len), state, e);
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 164, as _ZNK13QUtf32BECodec4nameEv
#if QT_CONFIG(textcodec)
inline QByteArray QUtf32BECodec::name() const
{
    return "UTF-32BE";
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 169, as _ZNK13QUtf32BECodec7aliasesEv
#if QT_CONFIG(textcodec)
inline QList<QByteArray> QUtf32BECodec::aliases() const
{
    QList<QByteArray> list;
    return list;
}
#endif  // QT_CONFIG(textcodec)

//  from ../qt5compat/src/core5/codecs/qutfcodec.cpp, line 159, as _ZNK13QUtf32BECodec7mibEnumEv
#if QT_CONFIG(textcodec)
inline int QUtf32BECodec::mibEnum() const
{
    return 1018;
}
#endif  // QT_CONFIG(textcodec)
//  -----------------------------------------------------------------------

//  A QUtf32BECodec that Python can take functions over in. Every QUtf32BECodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQUtf32BECodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQUtf32BECodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQUtf32BECodecCall2)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQUtf32BECodec : public QUtf32BECodec {
public:
  using QUtf32BECodec::QUtf32BECodec;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
  //  QByteArray QUtf32BECodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQUtf32BECodecCall0 call = reinterpret_cast<CuteQUtf32BECodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QUtf32BECodec::name();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QUtf32BECodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUtf32BECodecCall1 call = reinterpret_cast<CuteQUtf32BECodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUtf32BECodec::mibEnum();
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  QByteArray QUtf32Codec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQUtf32BECodecCall2 call = reinterpret_cast<CuteQUtf32BECodecCall2>(taken[2]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QUtf32Codec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(textcodec)
};

//  QByteArray QUtf32BECodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QUtf32BECodec4nameEv(const QUtf32BECodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QUtf32BECodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QUtf32BECodec7aliasesEv(
    const QUtf32BECodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QUtf32BECodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QUtf32BECodec7mibEnumEv(const QUtf32BECodec *self) {
  return self->mibEnum();
}

//  a Python function taken by a CuteQUtf32BECodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUtf32BECodec(
    QUtf32BECodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUtf32BECodec *>(self)->take(key, call);
}

#if QT_CONFIG(textcodec)
//  QByteArray QUtf32BECodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QUtf32BECodec4nameEv(const QUtf32BECodec *self) {
  return new QByteArray(self->QUtf32BECodec::name());
}
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
//  int QUtf32BECodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QUtf32BECodec7mibEnumEv(const QUtf32BECodec *self) {
  return self->QUtf32BECodec::mibEnum();
}
#endif  // QT_CONFIG(textcodec)

#endif  // QT_CONFIG(textcodec)
