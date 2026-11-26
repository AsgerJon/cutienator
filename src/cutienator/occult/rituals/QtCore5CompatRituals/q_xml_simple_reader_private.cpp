//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qxml_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/qxml.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qxml_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/qxml.h>
#include <QtCore5Compat/private/qxml_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore5Compat/qtextcodec.h>
#endif
#include <QtCore/qbuffer.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <QtCore/qstack.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 27, as local:qxml.cpp:XMLERR_OK
#define XMLERR_OK                         QT_TRANSLATE_NOOP("QXml", "no error occurred")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 29, as local:qxml.cpp:XMLERR_UNEXPECTEDEOF
#define XMLERR_UNEXPECTEDEOF              QT_TRANSLATE_NOOP("QXml", "unexpected end of file")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 31, as local:qxml.cpp:XMLERR_ERRORPARSINGELEMENT
#define XMLERR_ERRORPARSINGELEMENT        QT_TRANSLATE_NOOP("QXml", "error occurred while parsing element")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 32, as local:qxml.cpp:XMLERR_TAGMISMATCH
#define XMLERR_TAGMISMATCH                QT_TRANSLATE_NOOP("QXml", "tag mismatch")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 33, as local:qxml.cpp:XMLERR_ERRORPARSINGCONTENT
#define XMLERR_ERRORPARSINGCONTENT        QT_TRANSLATE_NOOP("QXml", "error occurred while parsing content")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 34, as local:qxml.cpp:XMLERR_UNEXPECTEDCHARACTER
#define XMLERR_UNEXPECTEDCHARACTER        QT_TRANSLATE_NOOP("QXml", "unexpected character")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 44, as local:qxml.cpp:XMLERR_INTERNALGENERALENTITYINDTD
#define XMLERR_INTERNALGENERALENTITYINDTD QT_TRANSLATE_NOOP("QXml", "internal general entity reference not allowed in DTD")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 45, as local:qxml.cpp:XMLERR_EXTERNALGENERALENTITYINAV
#define XMLERR_EXTERNALGENERALENTITYINAV  QT_TRANSLATE_NOOP("QXml", "external parsed general entity reference not allowed in attribute value")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 46, as local:qxml.cpp:XMLERR_EXTERNALGENERALENTITYINDTD
#define XMLERR_EXTERNALGENERALENTITYINDTD QT_TRANSLATE_NOOP("QXml", "external parsed general entity reference not allowed in DTD")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 47, as local:qxml.cpp:XMLERR_UNPARSEDENTITYREFERENCE
#define XMLERR_UNPARSEDENTITYREFERENCE    QT_TRANSLATE_NOOP("QXml", "unparsed entity reference in wrong context")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 48, as local:qxml.cpp:XMLERR_RECURSIVEENTITIES
#define XMLERR_RECURSIVEENTITIES          QT_TRANSLATE_NOOP("QXml", "recursive entities")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 49, as local:qxml.cpp:XMLERR_ERRORINTEXTDECL
#define XMLERR_ERRORINTEXTDECL            QT_TRANSLATE_NOOP("QXml", "error in the text declaration of an external entity")

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 56, as local:qxml.cpp:clear
namespace {
inline template <typename Container>
void clear(Container &c) { c = Container(); }
}  // namespace

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 76, as local:qxml.cpp:cltUnknown
static const signed char cltUnknown = 14;

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 161, as local:qxml.cpp:stripTextDecl
static bool stripTextDecl(QString& str)
{
    QLatin1String textDeclStart("<?xml");
    if (str.startsWith(textDeclStart)) {
#if QT_CONFIG(regularexpression)
        QRegularExpression textDecl(QString::fromLatin1(
            "^<\\?xml\\s+"
            "(version\\s*=\\s*((['\"])[-a-zA-Z0-9_.:]+\\3))?"
            "\\s*"
            "(encoding\\s*=\\s*((['\"])[A-Za-z][-a-zA-Z0-9_.]*\\6))?"
            "\\s*\\?>"
        ));
        QString strTmp = str.replace(textDecl, QLatin1String(""));
        if (strTmp.size() != str.size())
            return false; // external entity has wrong TextDecl
        str = strTmp;
#else
        return false;
#endif
    }
    return true;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 393, as local:qxml.cpp:QXmlSimpleReaderLocator
class QXmlSimpleReaderLocator : public QXmlLocator
{
public:
    QXmlSimpleReaderLocator(QXmlSimpleReader* parent)
    {
        reader = parent;
    }
    ~QXmlSimpleReaderLocator()
    {
    }

    int columnNumber() const override
    {
        return (reader->d_ptr->columnNr == -1 ? -1 : reader->d_ptr->columnNr + 1);
    }
    int lineNumber() const override
    {
        return (reader->d_ptr->lineNr == -1 ? -1 : reader->d_ptr->lineNr + 1);
    }

private:
    QXmlSimpleReader *reader;
};

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 423, as local:qxml.cpp:NamespaceMap
typedef QMap<QString, QString> NamespaceMap;

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 425, as local:qxml.cpp:QXmlNamespaceSupportPrivate
class QXmlNamespaceSupportPrivate
{
public:
    QXmlNamespaceSupportPrivate()
    {
        ns.insert(QLatin1String("xml"), QLatin1String("http://www.w3.org/XML/1998/namespace")); // the XML namespace
    }

    ~QXmlNamespaceSupportPrivate()
    {
    }

    QStack<NamespaceMap> nsStack;
    NamespaceMap ns;
};

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2495, as local:qxml.cpp:ItemInitState
constexpr int ItemInitState = 0;

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2850, as local:qxml.cpp:is_S
static inline bool is_S(QChar ch)
{
    ushort uc = ch.unicode();
    return (uc == ' ' || uc == '\t' || uc == '\n' || uc == '\r');
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2856, as local:qxml.cpp:NameChar
enum NameChar { NameBeginning, NameNotBeginning, NotName };

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7691, as local:qxml.cpp:updateValue
inline static void updateValue(QString &value, const QChar *array, int &arrayPos, int &valueLen)
{
    value.resize(valueLen + arrayPos);
    memcpy(value.data() + valueLen, array, arrayPos * sizeof(QChar));
    valueLen += arrayPos;
    arrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7716, as _ZN23QXmlSimpleReaderPrivate10stringAddCE5QChar
inline void QXmlSimpleReaderPrivate::stringAddC(QChar ch)
{
    if (stringArrayPos == 256)
        updateValue(stringValue, stringArray, stringArrayPos, stringValueLen);
    stringArray[stringArrayPos++] = ch;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7722, as _ZN23QXmlSimpleReaderPrivate8nameAddCE5QChar
inline void QXmlSimpleReaderPrivate::nameAddC(QChar ch)
{
    if (nameArrayPos == 256)
        updateValue(nameValue, nameArray, nameArrayPos, nameValueLen);
    nameArray[nameArrayPos++] = ch;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7728, as _ZN23QXmlSimpleReaderPrivate7refAddCE5QChar
inline void QXmlSimpleReaderPrivate::refAddC(QChar ch)
{
    if (refArrayPos == 256)
        updateValue(refValue, refArray, refArrayPos, refValueLen);
    refArray[refArrayPos++] = ch;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7669, as _ZN23QXmlSimpleReaderPrivate11parseFailedEMS_FbvEi
inline void QXmlSimpleReaderPrivate::parseFailed(ParseFunction where, int state)
{
    if (parseStack != nullptr && error.isNull()) {
        pushParseState(where, state);
    }
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 6180, as _ZN23QXmlSimpleReaderPrivate19parseChoiceSeqFrameERi
inline QXmlSimpleReaderPrivate::FrameParseResult QXmlSimpleReaderPrivate::parseChoiceSeqFrame(int &state)
{
    const signed char Init             = 0;
    const signed char Ws1              = 1; // eat whitespace
    const signed char CoS              = 2; // choice or set
    const signed char Ws2              = 3; // eat whitespace
    const signed char More             = 4; // more cp to read
    const signed char Name             = 5; // read name
    const signed char Done             = 6; //

    const signed char InpWs            = 0; // S
    const signed char InpOp            = 1; // (
    const signed char InpCp            = 2; //)
    const signed char InpQm            = 3; // ?
    const signed char InpAst           = 4; // *
    const signed char InpPlus          = 5; // +
    const signed char InpPipe          = 6; // |
    const signed char InpComm          = 7; // ,
    const signed char InpUnknown       = 8;

    static const signed char table[6][9] = {
     /*  InpWs   InpOp  InpCp  InpQm  InpAst  InpPlus  InpPipe  InpComm  InpUnknown */
        { -1,     Ws1,   -1,    -1,    -1,     -1,      -1,      -1,      Name  }, // Init
        { -1,     CoS,   -1,    -1,    -1,     -1,      -1,      -1,      CoS   }, // Ws1
        { Ws2,    -1,    Done,  Ws2,   Ws2,    Ws2,     More,    More,    -1    }, // CS
        { -1,     -1,    Done,  -1,    -1,     -1,      More,    More,    -1    }, // Ws2
        { -1,     Ws1,   -1,    -1,    -1,     -1,      -1,      -1,      Name  }, // More (same as Init)
        { Ws2,    -1,    Done,  Ws2,   Ws2,    Ws2,     More,    More,    -1    }  // Name (same as CS)
    };
    static_assert(Init == ItemInitState);
    signed char input;

    for (;;) {
        switch (state) {
            case Done:
                return FrameParseResult::Done;
            case -1:
                // Error
                reportParseError(QLatin1String(XMLERR_UNEXPECTEDCHARACTER));
                return FrameParseResult::Failed;
        }

        if (atEnd()) {
            unexpectedEof(&QXmlSimpleReaderPrivate::parseChoiceSeq, state);
            return FrameParseResult::Failed;
        }
        if (is_S(c)) {
            input = InpWs;
        } else if (c == QLatin1Char('(')) {
            input = InpOp;
        } else if (c == QLatin1Char(')')) {
            input = InpCp;
        } else if (c == QLatin1Char('?')) {
            input = InpQm;
        } else if (c == QLatin1Char('*')) {
            input = InpAst;
        } else if (c == QLatin1Char('+')) {
            input = InpPlus;
        } else if (c == QLatin1Char('|')) {
            input = InpPipe;
        } else if (c == QLatin1Char(',')) {
            input = InpComm;
        } else {
            input = InpUnknown;
        }
        state = table[state][input];

        switch (state) {
            case Ws1:
                if (!next_eat_ws()) {
                    parseFailed(&QXmlSimpleReaderPrivate::parseChoiceSeq, state);
                    return FrameParseResult::Failed;
                }
                break;
            case CoS:
                // a nested choice or seq follows
                return FrameParseResult::EnterChoiceSeq;
            case Ws2:
                if (!next_eat_ws()) {
                    parseFailed(&QXmlSimpleReaderPrivate::parseChoiceSeq, state);
                    return FrameParseResult::Failed;
                }
                break;
            case More:
                if (!next_eat_ws()) {
                    parseFailed(&QXmlSimpleReaderPrivate::parseChoiceSeq, state);
                    return FrameParseResult::Failed;
                }
                break;
            case Name:
                parseName_useRef = false;
                if (!parseName()) {
                    parseFailed(&QXmlSimpleReaderPrivate::parseChoiceSeq, state);
                    return FrameParseResult::Failed;
                }
                break;
            case Done:
                next();
                break;
        }
    }
    return FrameParseResult::Failed;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7705, as _ZN23QXmlSimpleReaderPrivate4nameEv
inline const QString& QXmlSimpleReaderPrivate::name()
{
    updateValue(nameValue, nameArray, nameArrayPos, nameValueLen);
    return nameValue;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7710, as _ZN23QXmlSimpleReaderPrivate3refEv
inline const QString& QXmlSimpleReaderPrivate::ref()
{
    updateValue(refValue, refArray, refArrayPos, refValueLen);
    return refValue;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2502, as _ZN23QXmlSimpleReaderPrivate19tryUnwindParseStackEMS_FbvE
inline int QXmlSimpleReaderPrivate::tryUnwindParseStack(ParseState::ParseFunction func)
{
    int state;
    if (parseStack == nullptr || parseStack->isEmpty()) {
        state = ItemInitState;
    } else {
        state = parseStack->pop().state;
#if defined(QT_QXML_DEBUG)
        qDebug("QXmlSimpleReader: %s (cont) in state %d",
               func == &QXmlSimpleReaderPrivate::parseProlog ?       "parseProlog" :
               func == &QXmlSimpleReaderPrivate::parseElement ?      "parseElement" :
               func == &QXmlSimpleReaderPrivate::parseContent ?      "parseContent" :
               func == &QXmlSimpleReaderPrivate::parseMisc ?         "parseMisc" :
               func == &QXmlSimpleReaderPrivate::parsePI ?           "parsePI" :
               func == &QXmlSimpleReaderPrivate::parseDoctype ?      "parseDoctype" :
               func == &QXmlSimpleReaderPrivate::parseExternalID ?   "parseExternalID" :
               func == &QXmlSimpleReaderPrivate::parseMarkupdecl ?   "parseMarkupdecl" :
               func == &QXmlSimpleReaderPrivate::parsePEReference ?  "parsePEReference" :
               func == &QXmlSimpleReaderPrivate::parseAttlistDecl ?  "parseAttlistDecl" :
               func == &QXmlSimpleReaderPrivate::parseAttType ?      "parseAttType" :
               func == &QXmlSimpleReaderPrivate::parseAttValue ?     "parseAttValue" :
               func == &QXmlSimpleReaderPrivate::parseElementDecl ?  "parseElementDecl" :
               func == &QXmlSimpleReaderPrivate::parseNotationDecl ? "parseNotationDecl" :
               func == &QXmlSimpleReaderPrivate::parseChoiceSeq ?    "parseChoiceSeq" :
               func == &QXmlSimpleReaderPrivate::parseEntityDecl ?   "parseEntityDecl" :
               func == &QXmlSimpleReaderPrivate::parseEntityValue ?  "parseEntityValue" :
               func == &QXmlSimpleReaderPrivate::parseComment ?      "parseComment" :
               func == &QXmlSimpleReaderPrivate::parseAttribute ?    "parseAttribute" :
               func == &QXmlSimpleReaderPrivate::parseName ?         "parseName" :
               func == &QXmlSimpleReaderPrivate::parseNmtoken ?      "parseNmtoken" :
               func == &QXmlSimpleReaderPrivate::parseReference ?    "parseReference" :
               func == &QXmlSimpleReaderPrivate::parseString ?       "parseString" :
               /* else */                                            "<unknown function>",
               state);
#endif
        if (!resumeSuspendedCall()) {
            parseFailed(func, state);
            return -1;
        }
    }

    return state;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2461, as _ZN23QXmlSimpleReaderPrivateD1Ev
inline QXmlSimpleReaderPrivate::~QXmlSimpleReaderPrivate()
{
    delete parseStack;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2441, as _ZN23QXmlSimpleReaderPrivateC1EP16QXmlSimpleReader
inline QXmlSimpleReaderPrivate::QXmlSimpleReaderPrivate(QXmlSimpleReader *reader)
{
    q_ptr = reader;
    parseStack = nullptr;

    locator.reset(new QXmlSimpleReaderLocator(reader));
    entityRes  = nullptr;
    dtdHnd     = nullptr;
    contentHnd = nullptr;
    errorHnd   = nullptr;
    lexicalHnd = nullptr;
    declHnd    = nullptr;

    // default feature settings
    useNamespaces = true;
    useNamespacePrefixes = false;
    reportWhitespaceCharData = true;
    reportEntities = false;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2466, as _ZN23QXmlSimpleReaderPrivate22initIncrementalParsingEv
inline void QXmlSimpleReaderPrivate::initIncrementalParsing()
{
    if (parseStack)
        parseStack->clear();
    else
        parseStack = new QStack<ParseState>;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7700, as _ZN23QXmlSimpleReaderPrivate6stringEv
inline const QString& QXmlSimpleReaderPrivate::string()
{
    updateValue(stringValue, stringArray, stringArrayPos, stringValueLen);
    return stringValue;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2427, as _ZN23QXmlSimpleReaderPrivate11stringClearEv
inline void QXmlSimpleReaderPrivate::stringClear()
{
    stringValueLen = 0; stringArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2431, as _ZN23QXmlSimpleReaderPrivate9nameClearEv
inline void QXmlSimpleReaderPrivate::nameClear()
{
    nameValueLen = 0; nameArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2436, as _ZN23QXmlSimpleReaderPrivate8refClearEv
inline void QXmlSimpleReaderPrivate::refClear()
{
    refValueLen = 0; refArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7511, as _ZN23QXmlSimpleReaderPrivate4nextEv
inline void QXmlSimpleReaderPrivate::next()
{
    int count = xmlRefStack.size();
    while (count != 0) {
        if (xmlRefStack.top().isEmpty()) {
            xmlRefStack.pop_back();
            count--;
        } else {
            c = xmlRefStack.top().next();
            return;
        }
    }

    // the following could be written nicer, but since it is a time-critical
    // function, rather optimize for speed
    ushort uc = c.unicode();
    c = inputSource->next();
    // If we are not incremental parsing, we just skip over EndOfData chars to give the
    // parser an uninterrupted stream of document chars.
    if (c == QXmlInputSource::EndOfData && parseStack == nullptr)
        c = inputSource->next();
    if (uc == '\n') {
        lineNr++;
        columnNr = -1;
    } else if (uc == '\r') {
        if (c != QLatin1Char('\n')) {
            lineNr++;
            columnNr = -1;
        }
    }
    ++columnNr;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2422, as _ZN23QXmlSimpleReaderPrivate5atEndEv
inline bool QXmlSimpleReaderPrivate::atEnd()
{
    return (c.unicode()|0x0001) == 0xffff;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7579, as _ZN23QXmlSimpleReaderPrivate4initEPK15QXmlInputSource
inline void QXmlSimpleReaderPrivate::init(const QXmlInputSource *i)
{
    lineNr = 0;
    columnNr = -1;
    inputSource = const_cast<QXmlInputSource *>(i);
    initData();

    externParameterEntities.clear();
    parameterEntities.clear();
    externEntities.clear();
    entities.clear();

    clear(tags);

    doctype.clear();
    xmlVersion.clear();
    encoding.clear();
    standalone = QXmlSimpleReaderPrivate::Unknown;
    error.clear();
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7604, as _ZN23QXmlSimpleReaderPrivate8initDataEv
inline void QXmlSimpleReaderPrivate::initData()
{
    c = QXmlInputSource::EndOfData;
    xmlRefStack.clear();
    next();
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7615, as _ZNK23QXmlSimpleReaderPrivate11entityExistERK7QString
inline bool QXmlSimpleReaderPrivate::entityExist(const QString& e) const
{
    if ( parameterEntities.find(e) == parameterEntities.end() &&
          externParameterEntities.find(e) == externParameterEntities.end() &&
          externEntities.find(e) == externEntities.end() &&
          entities.find(e) == entities.end()) {
        return false;
    } else {
        return true;
    }
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 3856, as _ZN23QXmlSimpleReaderPrivate22processElementEmptyTagEv
inline bool QXmlSimpleReaderPrivate::processElementEmptyTag()
{
    QString uri, lname;
    // pop the stack and call the handler
    if (contentHnd) {
        if (useNamespaces) {
            // report startElement first...
            namespaceSupport.processName(tags.top(), false, uri, lname);
            if (!contentHnd->startElement(uri, lname, tags.top(), attList)) {
                reportParseError(contentHnd->errorString());
                return false;
            }
            // ... followed by endElement...
            const bool endElementReturnedFalse = !contentHnd->endElement(uri, lname, tags.top());
            tags.pop();
            if (endElementReturnedFalse) {
                reportParseError(contentHnd->errorString());
                return false;
            }
            // ... followed by endPrefixMapping
            QStringList prefixesBefore, prefixesAfter;
            if (contentHnd) {
                prefixesBefore = namespaceSupport.prefixes();
            }
            namespaceSupport.popContext();
            // call the handler for prefix mapping
            prefixesAfter = namespaceSupport.prefixes();
            for (QStringList::Iterator it = prefixesBefore.begin(); it != prefixesBefore.end(); ++it) {
                if (!prefixesAfter.contains(*it)) {
                    if (!contentHnd->endPrefixMapping(*it)) {
                        reportParseError(contentHnd->errorString());
                        return false;
                    }
                }
            }
        } else {
            // report startElement first...
            if (!contentHnd->startElement(QString(), QString(), tags.top(), attList)) {
                reportParseError(contentHnd->errorString());
                return false;
            }
            // ... followed by endElement
            const bool endElementReturnedFalse = !contentHnd->endElement(QString(), QString(), tags.top());
            tags.pop();
            if (endElementReturnedFalse) {
                reportParseError(contentHnd->errorString());
                return false;
            }
        }
    } else {
        tags.pop();
        namespaceSupport.popContext();
    }
    return true;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 3964, as _ZN23QXmlSimpleReaderPrivate23processElementAttributeEv
inline bool QXmlSimpleReaderPrivate::processElementAttribute()
{
    QString uri, lname, prefix;
    const QString &name = QXmlSimpleReaderPrivate::name();
    const QString &string = QXmlSimpleReaderPrivate::string();

    // add the attribute to the list
    if (useNamespaces) {
        // is it a namespace declaration?
        namespaceSupport.splitName(name, prefix, lname);
        if (prefix == QLatin1String("xmlns")) {
            // namespace declaration
            namespaceSupport.setPrefix(lname, string);
            if (useNamespacePrefixes) {
                // according to http://www.w3.org/2000/xmlns/, the "prefix"
                // xmlns maps to the namespace name
                // http://www.w3.org/2000/xmlns/
                attList.append(name, QLatin1String("http://www.w3.org/2000/xmlns/"), lname, string);
            }
            // call the handler for prefix mapping
            if (contentHnd) {
                if (!contentHnd->startPrefixMapping(lname, string)) {
                    reportParseError(contentHnd->errorString());
                    return false;
                }
            }
        } else {
            // no namespace delcaration
            namespaceSupport.processName(name, true, uri, lname);
            attList.append(name, uri, lname, string);
        }
    } else {
        // no namespace support
        attList.append(name, uri, lname, string);
    }
    return true;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7225, as _ZN23QXmlSimpleReaderPrivate16processReferenceEv
inline bool QXmlSimpleReaderPrivate::processReference()
{
    QString reference = ref();
    if (reference == QLatin1String("amp")) {
        if (parseReference_context == InEntityValue) {
            // Bypassed
            stringAddC(QLatin1Char('&')); stringAddC(QLatin1Char('a')); stringAddC(QLatin1Char('m')); stringAddC(QLatin1Char('p')); stringAddC(QLatin1Char(';'));
        } else {
            // Included or Included in literal
            stringAddC(QLatin1Char('&'));
        }
        parseReference_charDataRead = true;
    } else if (reference == QLatin1String("lt")) {
        if (parseReference_context == InEntityValue) {
            // Bypassed
            stringAddC(QLatin1Char('&')); stringAddC(QLatin1Char('l')); stringAddC(QLatin1Char('t')); stringAddC(QLatin1Char(';'));
        } else {
            // Included or Included in literal
            stringAddC(QLatin1Char('<'));
        }
        parseReference_charDataRead = true;
    } else if (reference == QLatin1String("gt")) {
        if (parseReference_context == InEntityValue) {
            // Bypassed
            stringAddC(QLatin1Char('&')); stringAddC(QLatin1Char('g')); stringAddC(QLatin1Char('t')); stringAddC(QLatin1Char(';'));
        } else {
            // Included or Included in literal
            stringAddC(QLatin1Char('>'));
        }
        parseReference_charDataRead = true;
    } else if (reference == QLatin1String("apos")) {
        if (parseReference_context == InEntityValue) {
            // Bypassed
            stringAddC(QLatin1Char('&')); stringAddC(QLatin1Char('a')); stringAddC(QLatin1Char('p')); stringAddC(QLatin1Char('o')); stringAddC(QLatin1Char('s')); stringAddC(QLatin1Char(';'));
        } else {
            // Included or Included in literal
            stringAddC(QLatin1Char('\''));
        }
        parseReference_charDataRead = true;
    } else if (reference == QLatin1String("quot")) {
        if (parseReference_context == InEntityValue) {
            // Bypassed
            stringAddC(QLatin1Char('&')); stringAddC(QLatin1Char('q')); stringAddC(QLatin1Char('u')); stringAddC(QLatin1Char('o')); stringAddC(QLatin1Char('t')); stringAddC(QLatin1Char(';'));
        } else {
            // Included or Included in literal
            stringAddC(QLatin1Char('"'));
        }
        parseReference_charDataRead = true;
    } else {
        QMap<QString,QString>::Iterator it;
        it = entities.find(reference);
        if (it != entities.end()) {
            // "Internal General"
            switch (parseReference_context) {
                case InContent:
                    // Included
                    if (!insertXmlRef(*it, reference, false))
                        return false;
                    parseReference_charDataRead = false;
                    break;
                case InAttributeValue:
                    // Included in literal
                    if (!insertXmlRef(*it, reference, true))
                        return false;
                    parseReference_charDataRead = false;
                    break;
                case InEntityValue:
                    {
                        // Bypassed
                        stringAddC(QLatin1Char('&'));
                        for (int i=0; i<(int)reference.size(); i++) {
                            stringAddC(reference[i]);
                        }
                        stringAddC(QLatin1Char(';'));
                        parseReference_charDataRead = true;
                    }
                    break;
                case InDTD:
                    // Forbidden
                    parseReference_charDataRead = false;
                    reportParseError(QLatin1String(XMLERR_INTERNALGENERALENTITYINDTD));
                    return false;
            }
        } else {
            QMap<QString,QXmlSimpleReaderPrivate::ExternEntity>::Iterator itExtern;
            itExtern = externEntities.find(reference);
            if (itExtern == externEntities.end()) {
                // entity not declared
                // ### check this case for conformance
                if (parseReference_context == InEntityValue) {
                    // Bypassed
                    stringAddC(QLatin1Char('&'));
                    for (int i=0; i<(int)reference.size(); i++) {
                        stringAddC(reference[i]);
                    }
                    stringAddC(QLatin1Char(';'));
                    parseReference_charDataRead = true;
                } else {
                    // if we have some char data read, report it now
                    if (parseReference_context == InContent) {
                        if (contentCharDataRead) {
                            if (reportWhitespaceCharData || !string().simplified().isEmpty()) {
                                if (contentHnd != nullptr && !contentHnd->characters(string())) {
                                    reportParseError(contentHnd->errorString());
                                    return false;
                                }
                            }
                            stringClear();
                            contentCharDataRead = false;
                        }
                    }

                    if (contentHnd) {
                        skipped_entity_in_content = parseReference_context == InContent;
                        if (!contentHnd->skippedEntity(reference)) {
                            skipped_entity_in_content = false;
                            reportParseError(contentHnd->errorString());
                            return false; // error
                        }
                        skipped_entity_in_content = false;
                    }
                }
            } else if ((*itExtern).notation.isNull()) {
                // "External Parsed General"
                switch (parseReference_context) {
                    case InContent:
                        {
                            // Included if validating
                            bool skipIt = true;
                            if (entityRes) {
                                QXmlInputSource *ret = nullptr;
                                if (!entityRes->resolveEntity((*itExtern).publicId, (*itExtern).systemId, ret)) {
                                    delete ret;
                                    reportParseError(entityRes->errorString());
                                    return false;
                                }
                                if (ret) {
                                    QString xmlRefString;
                                    QString buffer = ret->data();
                                    while (!buffer.isEmpty()) {
                                        xmlRefString += buffer;
                                        ret->fetchData();
                                        buffer = ret->data();
                                    }

                                    delete ret;
                                    if (!stripTextDecl(xmlRefString)) {
                                        reportParseError(QLatin1String(XMLERR_ERRORINTEXTDECL));
                                        return false;
                                    }
                                    if (!insertXmlRef(xmlRefString, reference, false))
                                        return false;
                                    skipIt = false;
                                }
                            }
                            if (skipIt && contentHnd) {
                                skipped_entity_in_content = true;
                                if (!contentHnd->skippedEntity(reference)) {
                                    skipped_entity_in_content = false;
                                    reportParseError(contentHnd->errorString());
                                    return false; // error
                                }
                                skipped_entity_in_content = false;
                            }
                            parseReference_charDataRead = false;
                        } break;
                    case InAttributeValue:
                        // Forbidden
                        parseReference_charDataRead = false;
                        reportParseError(QLatin1String(XMLERR_EXTERNALGENERALENTITYINAV));
                        return false;
                    case InEntityValue:
                        {
                            // Bypassed
                            stringAddC(QLatin1Char('&'));
                            for (int i=0; i<(int)reference.size(); i++) {
                                stringAddC(reference[i]);
                            }
                            stringAddC(QLatin1Char(';'));
                            parseReference_charDataRead = true;
                        }
                        break;
                    case InDTD:
                        // Forbidden
                        parseReference_charDataRead = false;
                        reportParseError(QLatin1String(XMLERR_EXTERNALGENERALENTITYINDTD));
                        return false;
                }
            } else {
                // "Unparsed"
                // ### notify for "Occurs as Attribute Value" missing (but this is no reference, anyway)
                // Forbidden
                parseReference_charDataRead = false;
                reportParseError(QLatin1String(XMLERR_UNPARSEDENTITYREFERENCE));
                return false; // error
            }
        }
    }
    return true; // no error
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7484, as _ZN23QXmlSimpleReaderPrivate12insertXmlRefERK7QStringS2_b
inline bool QXmlSimpleReaderPrivate::insertXmlRef(const QString &data, const QString &name, bool inLiteral)
{
    if (inLiteral) {
        QString tmp = data;
        xmlRefStack.push(XmlRef(name, tmp.replace(QLatin1Char('\"'),
                            QLatin1String("&quot;")).replace(QLatin1Char('\''), QLatin1String("&apos;"))));
    } else {
        xmlRefStack.push(XmlRef(name, data));
    }
    int n = qMax(parameterEntities.size(), entities.size());
    if (xmlRefStack.size() > n+1) {
        // recursive entities
        reportParseError(QLatin1String(XMLERR_RECURSIVEENTITIES));
        return false;
    }
    if (reportEntities && lexicalHnd) {
        if (!lexicalHnd->startEntity(name)) {
            reportParseError(lexicalHnd->errorString());
            return false;
        }
    }
    return true;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 4315, as _ZN23QXmlSimpleReaderPrivate17reportEndEntitiesEv
inline bool QXmlSimpleReaderPrivate::reportEndEntities()
{
    int count = (int)xmlRefStack.size();
    while (count != 0 && xmlRefStack.top().isEmpty()) {
        if (contentHnd) {
            if (reportWhitespaceCharData || !string().simplified().isEmpty()) {
                if (!contentHnd->characters(string())) {
                    reportParseError(contentHnd->errorString());
                    return false;
                }
            }
        }
        stringClear();
        if (lexicalHnd) {
            if (!lexicalHnd->endEntity(xmlRefStack.top().name)) {
                reportParseError(lexicalHnd->errorString());
                return false;
            }
        }
        xmlRefStack.pop_back();
        count--;
    }
    return true;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7627, as _ZN23QXmlSimpleReaderPrivate16reportParseErrorERK7QString
inline void QXmlSimpleReaderPrivate::reportParseError(const QString& error)
{
    this->error = error;
    if (errorHnd) {
        if (this->error.isNull()) {
            const QXmlParseException ex(QLatin1String(XMLERR_OK), columnNr+1, lineNr+1,
                                        thisPublicId, thisSystemId);
            errorHnd->fatalError(ex);
        } else {
            const QXmlParseException ex(this->error, columnNr+1, lineNr+1,
                                        thisPublicId, thisSystemId);
            errorHnd->fatalError(ex);
        }
    }
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 6284, as _ZN23QXmlSimpleReaderPrivate29isExpandedEntityValueTooLargeEP7QString
inline bool QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString *errorMessage)
{
    QString entityNameBuffer;

    // For every entity, check how many times all entity names were referenced in its value.
    for (QMap<QString,QString>::const_iterator toSearchIt = entities.constBegin();
         toSearchIt != entities.constEnd();
         ++toSearchIt) {
        const QString &toSearch = toSearchIt.key();

        // Don't check the same entities twice.
        if (!literalEntitySizes.contains(toSearch)) {
            // The amount of characters that weren't entity names, but literals, like 'X'.
            QString leftOvers = entities.value(toSearch);
            // How many times was entityName referenced by toSearch?
            for (QMap<QString,QString>::const_iterator referencedIt = entities.constBegin();
                 referencedIt != entities.constEnd();
                 ++referencedIt) {
                const QString &entityName = referencedIt.key();

                for (int i = 0; i < leftOvers.size() && i != -1; ) {
                    entityNameBuffer = QLatin1Char('&') + entityName + QLatin1Char(';');

                    i = leftOvers.indexOf(entityNameBuffer, i);
                    if (i != -1) {
                        leftOvers.remove(i, entityName.size() + 2);
                        // The entityName we're currently trying to find was matched in this string; increase our count.
                        ++referencesToOtherEntities[toSearch][entityName];
                    }
                }
            }
            literalEntitySizes[toSearch] = leftOvers.size();
        }
    }

    for (QHash<QString, QHash<QString, int> >::const_iterator entityIt = referencesToOtherEntities.constBegin();
         entityIt != referencesToOtherEntities.constEnd();
         ++entityIt) {
        const QString &entity = entityIt.key();

        QHash<QString, int>::iterator expandedIt = expandedSizes.find(entity);
        if (expandedIt == expandedSizes.end()) {
            expandedIt = expandedSizes.insert(entity, literalEntitySizes.value(entity));
            for (QHash<QString, int>::const_iterator referenceIt = entityIt->constBegin();
                 referenceIt != entityIt->constEnd();
                 ++referenceIt) {
                const QString &referenceTo = referenceIt.key();
                const int references = referencesToOtherEntities.value(entity).value(referenceTo);
                // The total size of an entity's value is the expanded size of all of its referenced entities, plus its literal size.
                *expandedIt += expandedSizes.value(referenceTo) * references + literalEntitySizes.value(referenceTo) * references;
            }

            if (*expandedIt > entityCharacterLimit) {
                if (errorMessage) {
                    *errorMessage = QString::fromLatin1("The XML entity \"%1\" expands to a string that is too large to process (%2 characters > %3).")
                        .arg(entity, QString::number(*expandedIt), QString::number(entityCharacterLimit));
                }
                return true;
            }
        }
    }
    return false;
}
//  -----------------------------------------------------------------------

//  QXmlSimpleReaderPrivate::~QXmlSimpleReaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivateD1Ev(QXmlSimpleReaderPrivate *self) {
  delete self;
}

//  QXmlSimpleReaderPrivate::QXmlSimpleReaderPrivate(QXmlSimpleReader
//      *reader)
extern "C" Q_DECL_EXPORT
QXmlSimpleReaderPrivate *ritual_ZN23QXmlSimpleReaderPrivateC1EP16QXmlSimpleReader(
    QXmlSimpleReader *reader) {
  return new QXmlSimpleReaderPrivate(reader);
}

//  void QXmlSimpleReaderPrivate::initIncrementalParsing()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate22initIncrementalParsingEv(
    QXmlSimpleReaderPrivate *self) {
  self->initIncrementalParsing();
}

//  const QString &QXmlSimpleReaderPrivate::string()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QXmlSimpleReaderPrivate6stringEv(
    QXmlSimpleReaderPrivate *self) {
  return new QString(self->string());
}

//  void QXmlSimpleReaderPrivate::stringClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate11stringClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->stringClear();
}

//  void QXmlSimpleReaderPrivate::stringAddC()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate10stringAddCEv(
    QXmlSimpleReaderPrivate *self) {
  self->stringAddC();
}

//  void QXmlSimpleReaderPrivate::nameClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate9nameClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->nameClear();
}

//  void QXmlSimpleReaderPrivate::nameAddC()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate8nameAddCEv(
    QXmlSimpleReaderPrivate *self) {
  self->nameAddC();
}

//  void QXmlSimpleReaderPrivate::refClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate8refClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->refClear();
}

//  void QXmlSimpleReaderPrivate::refAddC()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate7refAddCEv(
    QXmlSimpleReaderPrivate *self) {
  self->refAddC();
}

//  void QXmlSimpleReaderPrivate::next()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate4nextEv(
    QXmlSimpleReaderPrivate *self) {
  self->next();
}

//  bool QXmlSimpleReaderPrivate::atEnd()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate5atEndEv(
    QXmlSimpleReaderPrivate *self) {
  return self->atEnd();
}

//  void QXmlSimpleReaderPrivate::init(const QXmlInputSource *i)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate4initEPK15QXmlInputSource(
    QXmlSimpleReaderPrivate *self,
    const QXmlInputSource *i) {
  self->init(i);
}

//  void QXmlSimpleReaderPrivate::initData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate8initDataEv(
    QXmlSimpleReaderPrivate *self) {
  self->initData();
}

//  bool QXmlSimpleReaderPrivate::entityExist(const QString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QXmlSimpleReaderPrivate11entityExistERK7QString(
    const QXmlSimpleReaderPrivate *self,
    const QString *a0) {
  return self->entityExist(*a0);
}

//  bool QXmlSimpleReaderPrivate::processElementEmptyTag()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate22processElementEmptyTagEv(
    QXmlSimpleReaderPrivate *self) {
  return self->processElementEmptyTag();
}

//  bool QXmlSimpleReaderPrivate::processElementAttribute()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate23processElementAttributeEv(
    QXmlSimpleReaderPrivate *self) {
  return self->processElementAttribute();
}

//  bool QXmlSimpleReaderPrivate::processReference()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate16processReferenceEv(
    QXmlSimpleReaderPrivate *self) {
  return self->processReference();
}

//  bool QXmlSimpleReaderPrivate::insertXmlRef(const QString &a0, const
//      QString &a1, bool a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate12insertXmlRefERK7QStringS2_b(
    QXmlSimpleReaderPrivate *self,
    const QString *a0,
    const QString *a1,
    bool a2) {
  return self->insertXmlRef(*a0, *a1, a2);
}

//  bool QXmlSimpleReaderPrivate::reportEndEntities()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate17reportEndEntitiesEv(
    QXmlSimpleReaderPrivate *self) {
  return self->reportEndEntities();
}

//  void QXmlSimpleReaderPrivate::reportParseError(const QString &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate16reportParseErrorERK7QString(
    QXmlSimpleReaderPrivate *self,
    const QString *error) {
  self->reportParseError(*error);
}

//  bool QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate29isExpandedEntityValueTooLargeEP7QString(
    QXmlSimpleReaderPrivate *self,
    QString *errorMessage) {
  return self->isExpandedEntityValueTooLarge(errorMessage);
}

//  QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXmlSimpleReader *ritual_ZN23QXmlSimpleReaderPrivate6q_funcEv(
    QXmlSimpleReaderPrivate *self) {
  return self->q_func();
}

//  const QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXmlSimpleReader *ritual_ZNK23QXmlSimpleReaderPrivate6q_funcEv(
    const QXmlSimpleReaderPrivate *self) {
  return self->q_func();
}
