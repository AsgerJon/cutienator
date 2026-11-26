//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(iconv)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qglobal_p.h>
#include <QtCore5Compat/private/qiconvcodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qthreadstorage.h>
#include <errno.h>
#include <locale.h>
#include <stdio.h>
#include <dlfcn.h>
#include <unistd.h>
#if defined(_XOPEN_UNIX) && !defined(Q_OS_QNX)
#  include <langinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 42, as _ZN11QIconvCodecC1Ev
inline QIconvCodec::QIconvCodec()
    : utf16Codec(0)
{
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 59, as _ZN11QIconvCodecD1Ev
inline QIconvCodec::~QIconvCodec()
{
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 94, as _ZNK11QIconvCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE
inline QString QIconvCodec::convertToUnicode(const char* chars, int len, ConverterState *convState) const
{
    if (utf16Codec == reinterpret_cast<QTextCodec *>(~0))
        return QString::fromLatin1(chars, len);

    int invalidCount = 0;
    int remainingCount = 0;
    char *remainingBuffer = 0;
    IconvState *temporaryState = 0;
    IconvState **pstate;

    if (convState) {
        // stateful conversion
        pstate = reinterpret_cast<IconvState **>(&convState->d[0]);
        if (convState->d[0]) {
            // restore state
            remainingCount = convState->remainingChars;
            remainingBuffer = (*pstate)->buffer;
        } else {
            // first time
            convState->clearFn = qIconvCodecStateFree;
        }
    } else {
        QThreadStorage<QIconvCodec::IconvState *> *ts = toUnicodeState();
        if (!ts) {
            // we're running after the Q_GLOBAL_STATIC has been deleted
            // or before the QCoreApplication initialization
            // bad programmer, no cookie for you
            pstate = &temporaryState;
        } else {
            // stateless conversion -- use thread-local data
            pstate = &toUnicodeState()->localData();
        }
    }

    if (!*pstate) {
        // first time, create the state
        iconv_t cd = createIconv_t(UTF16, 0);
        if (cd == reinterpret_cast<iconv_t>(-1)) {
            static int reported = 0;
            if (!reported++) {
                fprintf(stderr,
                        "QIconvCodec::convertToUnicode: using Latin-1 for conversion, iconv_open failed\n");
            }
            return QString::fromLatin1(chars, len);
        }

        *pstate = new IconvState(cd);
    }

    IconvState *state = *pstate;
    size_t inBytesLeft = len;
    // best case assumption, each byte is converted into one UTF-16 character, plus 2 bytes for the BOM
    char *inBytes = const_cast<char *>(chars); // GNU and posix don't agree

    QByteArray in;
    if (remainingCount) {
        // we have to prepend the remaining bytes from the previous conversion
        inBytesLeft += remainingCount;
        in.resize(inBytesLeft);
        inBytes = in.data();

        memcpy(in.data(), remainingBuffer, remainingCount);
        memcpy(in.data() + remainingCount, chars, len);

        remainingCount = 0;
    }

    size_t outBytesLeft = len * 2 + 2;
    QByteArray ba(outBytesLeft, QT_PREPEND_NAMESPACE(Qt::Uninitialized));
    char *outBytes = ba.data();
    do {
        size_t ret = iconv(state->cd, &inBytes, &inBytesLeft, &outBytes, &outBytesLeft);
        if (ret == (size_t) -1) {
            if (errno == E2BIG) {
                int offset = ba.size() - outBytesLeft;
                ba.resize(ba.size() * 2);
                outBytes = ba.data() + offset;
                outBytesLeft = ba.size() - offset;

                continue;
            }

            if (errno == EILSEQ) {
                // conversion stopped because of an invalid character in the sequence
                ++invalidCount;
            } else if (errno == EINVAL && convState) {
                // conversion stopped because the remaining inBytesLeft make up
                // an incomplete multi-byte sequence; save them for later
                state->saveChars(inBytes, inBytesLeft);
                remainingCount = inBytesLeft;
                break;
            }

            if (errno == EILSEQ || errno == EINVAL) {
                // skip the next character
                ++inBytes;
                --inBytesLeft;
                continue;
            }

            // some other error
            // note, cannot use qWarning() since we are implementing the codecForLocale :)
            perror("QIconvCodec::convertToUnicode: using Latin-1 for conversion, iconv failed");

            if (!convState) {
                // reset state
                iconv(state->cd, 0, &inBytesLeft, 0, &outBytesLeft);
            }

            delete temporaryState;
            return QString::fromLatin1(chars, len);
        }
    } while (inBytesLeft != 0);

    QString s;

    if (convState) {
        s = utf16Codec->toUnicode(ba.constData(), ba.size() - outBytesLeft, &state->internalState);

        convState->invalidChars = invalidCount;
        convState->remainingChars = remainingCount;
    } else {
        s = utf16Codec->toUnicode(ba.constData(), ba.size() - outBytesLeft);

        // reset state
        iconv(state->cd, 0, &inBytesLeft, 0, &outBytesLeft);
    }

    delete temporaryState;
    return s;
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 253, as _ZNK11QIconvCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE
inline QByteArray QIconvCodec::convertFromUnicode(const QChar *uc, int len, ConverterState *convState) const
{
    char *inBytes;
    char *outBytes;
    size_t inBytesLeft;

    char **inBytesPtr = &inBytes; // GNU and posix don't agree

    IconvState *temporaryState = 0;
    QThreadStorage<QIconvCodec::IconvState *> *ts = fromUnicodeState();
    IconvState *&state = ts ? ts->localData() : temporaryState;
    if (!state) {
        iconv_t cd = createIconv_t(0, UTF16);
        if (cd != reinterpret_cast<iconv_t>(-1)) {
            if (!setByteOrder(cd)) {
                perror("QIconvCodec::convertFromUnicode: using Latin-1 for conversion, iconv failed for BOM");

                iconv_close(cd);
                cd = reinterpret_cast<iconv_t>(-1);

                return QString(uc, len).toLatin1();
            }
        }
        state = new IconvState(cd);
    }
    if (state->cd == reinterpret_cast<iconv_t>(-1)) {
        static int reported = 0;
        if (!reported++) {
            fprintf(stderr,
                    "QIconvCodec::convertFromUnicode: using Latin-1 for conversion, iconv_open failed\n");
        }
        delete temporaryState;
        return QString(uc, len).toLatin1();
    }

    size_t outBytesLeft = len;
    QByteArray ba(outBytesLeft, QT_PREPEND_NAMESPACE(Qt::Uninitialized));
    outBytes = ba.data();

    // now feed iconv() the real data
    inBytes = const_cast<char *>(reinterpret_cast<const char *>(uc));
    inBytesLeft = len * sizeof(QChar);

    QByteArray in;
    if (convState && convState->remainingChars) {
        // we have one surrogate char to be prepended
        in.resize(sizeof(QChar) + inBytesLeft);
        inBytes = in.data();

        QChar remaining(convState->state_data[0]);
        memcpy(in.data(), &remaining, sizeof(QChar));
        memcpy(in.data() + sizeof(QChar), uc, inBytesLeft);

        inBytesLeft += sizeof(QChar);
        convState->remainingChars = 0;
    }

    int invalidCount = 0;
    while (inBytesLeft != 0) {
        if (iconv(state->cd, inBytesPtr, &inBytesLeft, &outBytes, &outBytesLeft) == (size_t) -1) {
            if (errno == EINVAL && convState) {
                // buffer ends in a surrogate
                Q_ASSERT(inBytesLeft == 2);
                convState->remainingChars = 1;
                convState->state_data[0] = uc[len - 1].unicode();
                break;
            }

            switch (errno) {
            case EILSEQ:
                ++invalidCount;
                Q_FALLTHROUGH();
            case EINVAL:
                {
                    inBytes += sizeof(QChar);
                    inBytesLeft -= sizeof(QChar);
                    break;
                }
            case E2BIG:
                {
                    int offset = ba.size() - outBytesLeft;
                    ba.resize(ba.size() * 2);
                    outBytes = ba.data() + offset;
                    outBytesLeft = ba.size() - offset;
                    break;
                }
            default:
                {
                    // note, cannot use qWarning() since we are implementing the codecForLocale :)
                    perror("QIconvCodec::convertFromUnicode: using Latin-1 for conversion, iconv failed");

                    // reset to initial state
                    iconv(state->cd, 0, &inBytesLeft, 0, &outBytesLeft);

                    delete temporaryState;
                    return QString(uc, len).toLatin1();
                }
            }
        }
    }

    // reset to initial state
    iconv(state->cd, 0, &inBytesLeft, 0, &outBytesLeft);
    setByteOrder(state->cd);

    ba.resize(ba.size() - outBytesLeft);

    if (convState)
        convState->invalidChars = invalidCount;

    delete temporaryState;
    return ba;
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 367, as _ZNK11QIconvCodec4nameEv
inline QByteArray QIconvCodec::name() const
{
    return "System";
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 372, as _ZNK11QIconvCodec7mibEnumEv
inline int QIconvCodec::mibEnum() const
{
    return 0;
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 47, as _ZNK11QIconvCodec4initEv
inline void QIconvCodec::init() const
{
    utf16Codec = QTextCodec::codecForMib(1015);
    Q_ASSERT_X(utf16Codec != 0,
               "QIconvCodec::convertToUnicode",
               "internal error, UTF-16 codec not found");
    if (!utf16Codec) {
        fprintf(stderr, "QIconvCodec::convertToUnicode: internal error, UTF-16 codec not found\n");
        utf16Codec = reinterpret_cast<QTextCodec *>(~0);
    }
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 377, as _ZNK11QIconvCodec13createIconv_tEPKcS1_
#if defined(Q_OS_LINUX)
inline iconv_t QIconvCodec::createIconv_t(const char *to, const char *from) const
{
    Q_ASSERT((to == 0 && from != 0) || (to != 0 && from == 0));

    if (!utf16Codec)
        init();

    iconv_t cd = (iconv_t) -1;
#if defined(Q_OS_QNX)
    // on QNX the default locale is UTF-8, and an empty string will cause iconv_open to fail
    static const char empty_codeset[] = "UTF-8";
#else
    // both GLIBC and libgnuiconv will use the locale's encoding if from or to is an empty string
    static const char empty_codeset[] = "";
#endif
    const char *codeset = empty_codeset;
    cd = iconv_open(to ? to : codeset, from ? from : codeset);

#if defined(_XOPEN_UNIX) && !defined(Q_OS_QNX)
    if (cd == (iconv_t) -1) {
        codeset = nl_langinfo(CODESET);
        if (codeset)
            cd = iconv_open(to ? to : codeset, from ? from : codeset);
    }
#endif

    if (cd == (iconv_t) -1) {
        // Very poorly defined and followed standards causes lots of
        // code to try to get all the cases... This logic is
        // duplicated in QTextCodec, so if you change it here, change
        // it there too.

        // Try to determine locale codeset from locale name assigned to
        // LC_CTYPE category.

        // First part is getting that locale name.  First try setlocale() which
        // definitely knows it, but since we cannot fully trust it, get ready
        // to fall back to environment variables.
        char * ctype = qstrdup(setlocale(LC_CTYPE, 0));

        // Get the first nonempty value from $LC_ALL, $LC_CTYPE, and $LANG
        // environment variables.
        char * lang = qstrdup(qgetenv("LC_ALL").constData());
        if (!lang || lang[0] == 0 || strcmp(lang, "C") == 0) {
            if (lang) delete [] lang;
            lang = qstrdup(qgetenv("LC_CTYPE").constData());
        }
        if (!lang || lang[0] == 0 || strcmp(lang, "C") == 0) {
            if (lang) delete [] lang;
            lang = qstrdup(qgetenv("LANG").constData());
        }

        // Now try these in order:
        // 1. CODESET from ctype if it contains a .CODESET part (e.g. en_US.ISO8859-15)
        // 2. CODESET from lang if it contains a .CODESET part
        // 3. ctype (maybe the locale is named "ISO-8859-1" or something)
        // 4. locale (ditto)
        // 5. check for "@euro"

        // 1. CODESET from ctype if it contains a .CODESET part (e.g. en_US.ISO8859-15)
        codeset = ctype ? strchr(ctype, '.') : 0;
        if (codeset && *codeset == '.') {
            ++codeset;
            cd = iconv_open(to ? to : codeset, from ? from : codeset);
        }

        // 2. CODESET from lang if it contains a .CODESET part
        codeset = lang ? strchr(lang, '.') : 0;
        if (cd == (iconv_t) -1 && codeset && *codeset == '.') {
            ++codeset;
            cd = iconv_open(to ? to : codeset, from ? from : codeset);
        }

        // 3. ctype (maybe the locale is named "ISO-8859-1" or something)
        if (cd == (iconv_t) -1 && ctype && *ctype != 0 && strcmp (ctype, "C") != 0)
            cd = iconv_open(to ? to : ctype, from ? from : ctype);


        // 4. locale (ditto)
        if (cd == (iconv_t) -1 && lang && *lang != 0)
            cd = iconv_open(to ? to : lang, from ? from : lang);

        // 5. "@euro"
        if ((cd == (iconv_t) -1 && ctype && strstr(ctype, "@euro")) || (lang && strstr(lang, "@euro")))
            cd = iconv_open(to ? to : "ISO8859-15", from ? from : "ISO8859-15");

        delete [] ctype;
        delete [] lang;
    }

    return cd;
}
#endif  // defined(Q_OS_LINUX)
//  -----------------------------------------------------------------------

//  A QIconvCodec that Python can take functions over in. Every QIconvCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
typedef const QByteArray * (*CuteQIconvCodecCall0)(const void *, const QChar *, int, QTextCodec::ConverterState *, int *);
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
typedef const QByteArray * (*CuteQIconvCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
typedef int (*CuteQIconvCodecCall2)(const void *, int *);
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
class CuteQIconvCodec : public QIconvCodec {
public:
  using QIconvCodec::QIconvCodec;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
    if (!std::strcmp(key, "_ZNK10QTextCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
  //  QByteArray QIconvCodec::convertFromUnicode(const QChar *a0, int a1,
  //      ConverterState *a2) const
  QByteArray convertFromUnicode(
      const QChar *a0,
      int a1,
      QTextCodec::ConverterState *a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconvCodecCall0 call = reinterpret_cast<CuteQIconvCodecCall0>(taken[0]);
      const QByteArray * given = call(this, a0, a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QIconvCodec::convertFromUnicode(a0, a1, a2);
  }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
  //  QByteArray QIconvCodec::name() const
  QByteArray name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconvCodecCall1 call = reinterpret_cast<CuteQIconvCodecCall1>(taken[1]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QIconvCodec::name();
  }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
#if QT_CONFIG(iconv)
  //  int QIconvCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQIconvCodecCall2 call = reinterpret_cast<CuteQIconvCodecCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QIconvCodec::mibEnum();
  }
#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(textcodec)
};

//  QIconvCodec::QIconvCodec()
extern "C" Q_DECL_EXPORT
QIconvCodec *ritual_ZN11QIconvCodecC1Ev() {
  return new CuteQIconvCodec();
}

//  QIconvCodec::~QIconvCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconvCodecD1Ev(QIconvCodec *self) {
  delete self;
}

//  QString QIconvCodec::convertToUnicode(const char *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIconvCodec16convertToUnicodeEPKciPN20QStringConverterBase5StateE(
    const QIconvCodec *self,
    const char *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QString(self->convertToUnicode(a0, a1, a2));
}

//  QByteArray QIconvCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QIconvCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QIconvCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->convertFromUnicode(a0, a1, a2));
}

//  QByteArray QIconvCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QIconvCodec4nameEv(const QIconvCodec *self) {
  return new QByteArray(self->name());
}

//  int QIconvCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QIconvCodec7mibEnumEv(const QIconvCodec *self) {
  return self->mibEnum();
}

//  void QIconvCodec::init() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QIconvCodec4initEv(const QIconvCodec *self) {
  self->init();
}

//  iconv_t QIconvCodec::createIconv_t(const char *to, const char *from)
//      const
extern "C" Q_DECL_EXPORT
iconv_t *ritual_ZNK11QIconvCodec13createIconv_tEPKcS1_(
    const QIconvCodec *self,
    const char *to,
    const char *from) {
  return new iconv_t(self->createIconv_t(to, from));
}

//  a Python function taken by a CuteQIconvCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconvCodec(
    QIconvCodec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconvCodec *>(self)->take(key, call);
}

//  QByteArray QIconvCodec::convertFromUnicode(const QChar *a0, int a1,
//      ConverterState *a2) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QIconvCodec18convertFromUnicodeEPK5QChariPN20QStringConverterBase5StateE(
    const QIconvCodec *self,
    const QChar *a0,
    int a1,
    QTextCodec::ConverterState *a2) {
  return new QByteArray(self->QIconvCodec::convertFromUnicode(a0, a1, a2));
}

//  QByteArray QIconvCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK11QIconvCodec4nameEv(const QIconvCodec *self) {
  return new QByteArray(self->QIconvCodec::name());
}

//  int QIconvCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QIconvCodec7mibEnumEv(const QIconvCodec *self) {
  return self->QIconvCodec::mibEnum();
}

//  a iconv_t a ritual of QIconvCodec gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QIconvCodec__iconv_t(iconv_t *self) {
  delete self;
}

#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
