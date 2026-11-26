//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qchar.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4jsonobject_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4booleanobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qstack.h>
#include <QtCore/qstringlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 26, as local:qv4jsonobject.cpp:BEGIN
#if defined(PARSER_DEBUG)
#define BEGIN qDebug() << QByteArray(4*indent++, ' ').constData()
#endif  // defined(PARSER_DEBUG)

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 27, as local:qv4jsonobject.cpp:END
#if defined(PARSER_DEBUG)
#define END --indent
#endif  // defined(PARSER_DEBUG)

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 38, as local:qv4jsonobject.cpp:nestingLimit
static const int nestingLimit = 1024;

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 75, as local:qv4jsonobject.cpp:Space
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 89, as _ZN3QV410JsonParser8eatSpaceEv
namespace QV4 {
inline bool JsonParser::eatSpace()
{
    while (json < end) {
        const char16_t ch = json->unicode();
        if (ch > Space)
            break;
        if (ch != Space &&
            ch != Tab &&
            ch != LineFeed &&
            ch != Return)
            break;
        ++json;
    }
    return (json < end);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 41, as _ZN3QV410JsonParserC1EPNS_15ExecutionEngineEPK5QChari
namespace QV4 {
inline JsonParser::JsonParser(ExecutionEngine *engine, const QChar *json, int length)
    : engine(engine), head(json), json(json), nestingLevel(0), lastError(QJsonParseError::NoError)
{
    end = json + length;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4jsonobject.cpp, line 105, as _ZN3QV410JsonParser9nextTokenEv
namespace QV4 {
inline QChar JsonParser::nextToken()
{
    if (!eatSpace())
        return u'\0';
    QChar token = *json++;
    switch (token.unicode()) {
    case BeginArray:
    case BeginObject:
    case NameSeparator:
    case ValueSeparator:
    case EndArray:
    case EndObject:
        eatSpace();
        break;
    case Quote:
        break;
    default:
        token = u'\0';
        break;
    }
    return token;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::JsonParser::JsonParser(ExecutionEngine *engine, const QChar *json,
//      int length)
extern "C" Q_DECL_EXPORT
QV4::JsonParser *ritual_ZN3QV410JsonParserC1EPNS_15ExecutionEngineEPK5QChari(
    QV4::ExecutionEngine *engine,
    const QChar *json,
    int length) {
  return new QV4::JsonParser(engine, json, length);
}

//  QChar QV4::JsonParser::nextToken()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN3QV410JsonParser9nextTokenEv(QV4::JsonParser *self) {
  return new QChar(self->nextToken());
}

//  QV4::JsonParser::~JsonParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410JsonParserD1Ev(QV4::JsonParser *self) {
  delete self;
}
