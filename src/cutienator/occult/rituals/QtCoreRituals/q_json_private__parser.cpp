//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qjsonparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qjsonparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcborvalue.h>
#include <QtCore/QUtf8StringView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qcoreapplication.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/private/qjsonparser_p.h>
#include <QtCore/private/qjson_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/private/qcborvalue_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qjsonparser.cpp, line 17, as local:qjsonparser.cpp:nestingLimit
static const int nestingLimit = 1024;

//  from src/corelib/serialization/qjsonparser.cpp, line 159, as local:qjsonparser.cpp:StashedContainer
class StashedContainer
{
    Q_DISABLE_COPY_MOVE(StashedContainer)
public:
    StashedContainer(QExplicitlySharedDataPointer<QCborContainerPrivate> *container,
                     QCborValue::Type type)
        : type(type), stashed(std::move(*container))
    {
    }

    QCborValue intoValue(QExplicitlySharedDataPointer<QCborContainerPrivate> *parent)
    {
        std::swap(stashed, *parent);
        return QCborContainerPrivate::makeValue(type, -1, stashed.take(),
                                                QCborContainerPrivate::MoveContainer);
    }

private:
    QCborValue::Type type;
    QExplicitlySharedDataPointer<QCborContainerPrivate> stashed;
};

//  from src/corelib/serialization/qjsonparser.cpp, line 216, as local:qjsonparser.cpp:Quote
enum {
    Space = 0x20,
    Tab = 0x09,
    LineFeed = 0x0a,
    Return = 0x0d,
    BeginArray = 0x5b,
    BeginObject = 0x7b,
    EndArray = 0x5d,
    EndObject = 0x7d,
    NameSeparator = 0x3a,
    ValueSeparator = 0x2c,
    Quote = 0x22
};

//  from src/corelib/serialization/qjsonparser.cpp, line 788, as local:qjsonparser.cpp:scanUtf8Char
static inline bool scanUtf8Char(const char *&json, const char *end, char32_t *result)
{
    auto usrc = reinterpret_cast<const qchar8_t*>(json);
    const auto uend = reinterpret_cast<const qchar8_t*>(end);
    constexpr char32_t Invalid = ~U'\0';
    const char32_t ch = QUtf8Functions::nextUcs4FromUtf8(usrc, uend, Invalid);
    if (ch == Invalid)
        return false;
    *result = ch;
    json = reinterpret_cast<const char *>(usrc);
    return true;
}

//  from src/corelib/serialization/qjsonparser.cpp, line 241, as _ZN12QJsonPrivate6Parser8eatSpaceEv
namespace QJsonPrivate {
using namespace QtMiscUtils;
inline bool Parser::eatSpace()
{
    while (json < end) {
        if (*json > Space)
            break;
        if (*json != Space &&
            *json != Tab &&
            *json != LineFeed &&
            *json != Return)
            break;
        ++json;
    }
    return (json < end);
}
}  // namespace QJsonPrivate

//  from src/corelib/serialization/qjsonparser.cpp, line 181, as _ZN12QJsonPrivate6ParserC1E20QBasicUtf8StringViewILb0EE
namespace QJsonPrivate {
using namespace QtMiscUtils;
inline Parser::Parser(QUtf8StringView json)
    : head(json.data()), json(head), end(json.end())
    , nestingLevel(0)
    , lastError(QJsonParseError::NoError)
{
}
}  // namespace QJsonPrivate

//  from src/corelib/serialization/qjsonparser.cpp, line 230, as _ZN12QJsonPrivate6Parser6eatBOMEv
namespace QJsonPrivate {
using namespace QtMiscUtils;
inline void Parser::eatBOM()
{
    // eat UTF-8 byte order mark
    uchar utf8bom[3] = { 0xef, 0xbb, 0xbf };
    if (end - json > 3 &&
        (uchar)json[0] == utf8bom[0] &&
        (uchar)json[1] == utf8bom[1] &&
        (uchar)json[2] == utf8bom[2])
        json += 3;
}
}  // namespace QJsonPrivate

//  from src/corelib/serialization/qjsonparser.cpp, line 650, as _ZN12QJsonPrivate6Parser11parseNumberEv
namespace QJsonPrivate {
using namespace QtMiscUtils;
inline QCborValue Parser::parseNumber()
{
    const char *start = json;
    bool isInt = true;

    // minus
    if (json < end && *json == '-')
        ++json;

    // int = zero / ( digit1-9 *DIGIT )
    if (json < end && *json == '0') {
        ++json;
    } else {
        while (json < end && isAsciiDigit(*json))
            ++json;
    }

    // frac = decimal-point 1*DIGIT
    if (json < end && *json == '.') {
        ++json;
        while (json < end && isAsciiDigit(*json)) {
            isInt = isInt && *json == '0';
            ++json;
        }
    }

    // exp = e [ minus / plus ] 1*DIGIT
    if (json < end && (*json == 'e' || *json == 'E')) {
        isInt = false;
        ++json;
        if (json < end && (*json == '-' || *json == '+'))
            ++json;
        while (json < end && isAsciiDigit(*json))
            ++json;
    }

    const QByteArray number = QByteArray::fromRawData(start, json - start);

    if (isInt) {
        bool ok;
        qlonglong n = number.toLongLong(&ok);
        if (ok) {
            return QCborValue(n);
        }
    }

    bool ok;
    double d = number.toDouble(&ok);

    if (!ok) {
        lastError = QJsonParseError::IllegalNumber;
        return QCborValue();
    }

    qint64 n;
    if (convertDoubleTo(d, &n))
        return QCborValue(n);
    return QCborValue(d);
}
}  // namespace QJsonPrivate
//  -----------------------------------------------------------------------

//  QJsonPrivate::Parser::Parser(QUtf8StringView json)
extern "C" Q_DECL_EXPORT
QJsonPrivate::Parser *ritual_ZN12QJsonPrivate6ParserC1E20QBasicUtf8StringViewILb0EE(
    const QUtf8StringView *json) {
  return new QJsonPrivate::Parser(*json);
}

//  void QJsonPrivate::Parser::eatBOM()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QJsonPrivate6Parser6eatBOMEv(QJsonPrivate::Parser *self) {
  self->eatBOM();
}

//  QCborValue QJsonPrivate::Parser::parseNumber()
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN12QJsonPrivate6Parser11parseNumberEv(
    QJsonPrivate::Parser *self) {
  return new QCborValue(self->parseNumber());
}
