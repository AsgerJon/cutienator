//  Edited by hand on 2026-11-25: the include of
//  QtCore/private/qxmlstreamparser_p.h is taken out, as it defines
//  inline functions using 'getChar', 'reallocateStack' and others that
//  Qt defines only in qxmlstream.cpp, which the compiler warned of
//  and the test build refused; no ritual here needs it. Kept as it is
//  when the generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "QtCore/qxmlstream.h"
#if QT_CONFIG(xmlstream)
#include <QtCore/private/qxmlutils_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <stdio.h>
#include <QtCore/qstringconverter.h>
#include <QtCore/qstack.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/private/qtools_p.h>
#include <iterator>
#include <QtCore/private/qxmlstream_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/private/qstringiterator_p.h>
#include <algorithm>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qxmlstream.cpp, line 1142, as _ZN23QXmlStreamReaderPrivateD1Ev
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline QXmlStreamReaderPrivate::~QXmlStreamReaderPrivate()
{
    free(sym_stack);
    free(state_stack);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1045, as _ZN23QXmlStreamReaderPrivate4initEv
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::init()
{
    scanDtd = false;
    lastAttributeIsCData = false;
    token = -1;
    token_char = 0;
    isEmptyElement = false;
    isWhitespace = true;
    isCDATA = false;
    standalone = false;
    hasStandalone = false;
    tos = 0;
    resumeReduction = 0;
    state_stack[tos++] = 0;
    state_stack[tos] = 0;
    putStack.clear();
    putStack.reserve(32);
    textBuffer.clear();
    textBuffer.reserve(256);
    tagStack.clear();
    tagsDone = false;
    attributes.clear();
    attributes.reserve(16);
    lineNumber = lastLineStart = characterOffset = 0;
    readBufferPos = 0;
    nbytesread = 0;
    decoder = QStringDecoder();
    attributeStack.clear();
    attributeStack.reserve(16);
    entityParser.reset();
    hasCheckedStartDocument = false;
    normalizeLiterals = false;
    hasSeenTag = false;
    atEnd = false;
    inParseEntity = false;
    referenceToUnparsedEntityDetected = false;
    referenceToParameterEntityDetected = false;
    hasExternalDtdSubset = false;
    lockEncoding = false;
    namespaceProcessing = true;
    rawReadBuffer.clear();
    chunkDecoder = QStringDecoder();
    dataInfo.clear();
    readBuffer.clear();
    tagStackStringStorageSize = initialTagStackStringStorageSize;

    type = QXmlStreamReader::NoToken;
    error = QXmlStreamReader::NoError;
    currentContext = XmlContext::Prolog;
    foundDTD = false;
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1976, as _ZN23QXmlStreamReaderPrivate23resolvePublicNamespacesEv
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::resolvePublicNamespaces()
{
    const Tag &tag = tagStack.top();
    qsizetype n = namespaceDeclarations.size() - tag.namespaceDeclarationsSize;
    publicNamespaceDeclarations.resize(n);
    for (qsizetype i = 0; i < n; ++i) {
        const NamespaceDeclaration &namespaceDeclaration = namespaceDeclarations.at(tag.namespaceDeclarationsSize + i);
        QXmlStreamNamespaceDeclaration &publicNamespaceDeclaration = publicNamespaceDeclarations[i];
        publicNamespaceDeclaration.m_prefix = namespaceDeclaration.prefix;
        publicNamespaceDeclaration.m_namespaceUri = namespaceDeclaration.namespaceUri;
    }
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1989, as _ZN23QXmlStreamReaderPrivate10resolveDtdEv
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::resolveDtd()
{
    publicNotationDeclarations.resize(notationDeclarations.size());
    for (qsizetype i = 0; i < notationDeclarations.size(); ++i) {
        const QXmlStreamReaderPrivate::NotationDeclaration &notationDeclaration = notationDeclarations.at(i);
        QXmlStreamNotationDeclaration &publicNotationDeclaration = publicNotationDeclarations[i];
        publicNotationDeclaration.m_name = notationDeclaration.name;
        publicNotationDeclaration.m_systemId = notationDeclaration.systemId;
        publicNotationDeclaration.m_publicId = notationDeclaration.publicId;

    }
    notationDeclarations.clear();
    publicEntityDeclarations.resize(entityDeclarations.size());
    for (qsizetype i = 0; i < entityDeclarations.size(); ++i) {
        const QXmlStreamReaderPrivate::EntityDeclaration &entityDeclaration = entityDeclarations.at(i);
        QXmlStreamEntityDeclaration &publicEntityDeclaration = publicEntityDeclarations[i];
        publicEntityDeclaration.m_name = entityDeclaration.name;
        publicEntityDeclaration.m_notationName = entityDeclaration.notationName;
        publicEntityDeclaration.m_systemId = entityDeclaration.systemId;
        publicEntityDeclaration.m_publicId = entityDeclaration.publicId;
        publicEntityDeclaration.m_value = entityDeclaration.value;
    }
    entityDeclarations.clear();
    parameterEntityHash.clear();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 2015, as _ZN23QXmlStreamReaderPrivate14resolveCharRefEi
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline uint QXmlStreamReaderPrivate::resolveCharRef(int symbolIndex)
{
    bool ok = true;
    uint s;
    // ### add toXShort to XmlString?
    if (sym(symbolIndex).c == 'x')
        s = symString(symbolIndex).view().sliced(1).toUInt(&ok, 16);
    else
        s = symString(symbolIndex).view().toUInt(&ok, 10);

    ok &= (s == 0x9 || s == 0xa || s == 0xd || (s >= 0x20 && s <= 0xd7ff)
           || (s >= 0xe000 && s <= 0xfffd) || (s >= 0x10000 && s <= QChar::LastValidCodePoint));

    return ok ? s : 0;
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1123, as _ZN23QXmlStreamReaderPrivate15reallocateStackEv
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::reallocateStack()
{
    // The multiplication cannot overflow (we would have alloc'ed more than
    // half of the address space using the realloc()s below, before that
    // happens):
    const auto newStackSize = stack_size * 2;

    void *p = qt_reallocarray(sym_stack, size_t(newStackSize), sizeof(Value));
    Q_CHECK_PTR(p);
    sym_stack = static_cast<Value*>(p);
    p = qt_reallocarray(state_stack, size_t(newStackSize), sizeof(int));
    Q_CHECK_PTR(p);
    state_stack = static_cast<int*>(p);

    // only update this after _both_ allocations succeeded:
    stack_size = newStackSize;
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1680, as _ZN23QXmlStreamReaderPrivate9putStringE11QStringViewx
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::putString(QStringView s, qsizetype from)
{
    if (from != 0) {
        putString(s.mid(from));
        return;
    }
    putStack.reserve(s.size());
    for (auto it = s.rbegin(), end = s.rend(); it != end; ++it)
        putStack.rawPush() = it->unicode();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1691, as _ZN23QXmlStreamReaderPrivate16putStringLiteralE11QStringView
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::putStringLiteral(QStringView s)
{
    putStack.reserve(s.size());
    for (auto it = s.rbegin(), end = s.rend(); it != end; ++it)
        putStack.rawPush() = ((LETTER << 16) | it->unicode());
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1698, as _ZN23QXmlStreamReaderPrivate14putReplacementE11QStringView
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::putReplacement(QStringView s)
{
    putStack.reserve(s.size());
    for (auto it = s.rbegin(), end = s.rend(); it != end; ++it) {
        char16_t c = it->unicode();
        if (c == '\n' || c == '\r')
            putStack.rawPush() = ((LETTER << 16) | c);
        else
            putStack.rawPush() = c;
    }
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 1709, as _ZN23QXmlStreamReaderPrivate30putReplacementInAttributeValueE11QStringView
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::putReplacementInAttributeValue(QStringView s)
{
    putStack.reserve(s.size());
    for (auto it = s.rbegin(), end = s.rend(); it != end; ++it) {
        char16_t c = it->unicode();
        if (c == '&' || c == ';')
            putStack.rawPush() = c;
        else if (c == '\n' || c == '\r')
            putStack.rawPush() = ' ';
        else
            putStack.rawPush() = ((LETTER << 16) | c);
    }
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 291, as _ZN23QXmlStreamReaderPrivate23resolveUndeclaredEntityERK7QString
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline QString QXmlStreamReaderPrivate::resolveUndeclaredEntity(const QString &name)
{
    if (entityResolver)
        return entityResolver->resolveUndeclaredEntity(name);
    return QString();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 2149, as _ZN23QXmlStreamReaderPrivate10raiseErrorEN16QXmlStreamReader5ErrorERK7QString
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::raiseError(QXmlStreamReader::Error error, const QString& message)
{
    this->error = error;
    errorString = message;
    if (errorString.isNull()) {
        if (error == QXmlStreamReader::PrematureEndOfDocumentError)
            errorString = QXmlStream::tr("Premature end of document.");
        else if (error == QXmlStreamReader::CustomError)
            errorString = QXmlStream::tr("Invalid document.");
    }

    type = QXmlStreamReader::Invalid;
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 2163, as _ZN23QXmlStreamReaderPrivate20raiseWellFormedErrorERK7QString
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::raiseWellFormedError(const QString &message)
{
    raiseError(QXmlStreamReader::NotWellFormedError, message);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  from src/corelib/serialization/qxmlstream.cpp, line 2168, as _ZN23QXmlStreamReaderPrivate27raiseNamePrefixTooLongErrorEv
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
inline void QXmlStreamReaderPrivate::raiseNamePrefixTooLongError()
{
    // TODO: add a ImplementationLimitsExceededError and use it instead
    raiseError(QXmlStreamReader::NotWellFormedError,
               QXmlStream::tr("Length of XML attribute name exceeds implementation limits (4KiB "
                              "characters)."));
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)
//  -----------------------------------------------------------------------

//  QXmlStreamReader *QXmlStreamReaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXmlStreamReader *ritual_ZN23QXmlStreamReaderPrivate6q_funcEv(
    QXmlStreamReaderPrivate *self) {
  return self->q_func();
}

//  const QXmlStreamReader *QXmlStreamReaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXmlStreamReader *ritual_ZNK23QXmlStreamReaderPrivate6q_funcEv(
    const QXmlStreamReaderPrivate *self) {
  return self->q_func();
}

//  QXmlStreamReaderPrivate::~QXmlStreamReaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivateD1Ev(QXmlStreamReaderPrivate *self) {
  delete self;
}

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate4initEv(
    QXmlStreamReaderPrivate *self) {
  self->init();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  bool QXmlStreamReaderPrivate::referenceEntity(QHash<QStringView, Entity>
//      *hash, Entity &entity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlStreamReaderPrivate15referenceEntityEP5QHashI11QStringViewNS_6EntityEERS2_(
    QXmlStreamReaderPrivate *self,
    QHash<QStringView, QXmlStreamReaderPrivate::Entity> *hash,
    QXmlStreamReaderPrivate::Entity *entity) {
  return self->referenceEntity(hash, *entity);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::resolvePublicNamespaces()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate23resolvePublicNamespacesEv(
    QXmlStreamReaderPrivate *self) {
  self->resolvePublicNamespaces();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::resolveDtd()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate10resolveDtdEv(
    QXmlStreamReaderPrivate *self) {
  self->resolveDtd();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  uint QXmlStreamReaderPrivate::resolveCharRef(int symbolIndex)
extern "C" Q_DECL_EXPORT
uint ritual_ZN23QXmlStreamReaderPrivate14resolveCharRefEi(
    QXmlStreamReaderPrivate *self,
    int symbolIndex) {
  return self->resolveCharRef(symbolIndex);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  bool QXmlStreamReaderPrivate::entitiesMustBeDeclared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QXmlStreamReaderPrivate22entitiesMustBeDeclaredEv(
    const QXmlStreamReaderPrivate *self) {
  return self->entitiesMustBeDeclared();
}

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::reallocateStack()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate15reallocateStackEv(
    QXmlStreamReaderPrivate *self) {
  self->reallocateStack();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  Value &QXmlStreamReaderPrivate::sym(int index) const
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate::Value *ritual_ZNK23QXmlStreamReaderPrivate3symEi(
    const QXmlStreamReaderPrivate *self,
    int index) {
  return &(self->sym(index));
}

//  void QXmlStreamReaderPrivate::clearTextBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate15clearTextBufferEv(
    QXmlStreamReaderPrivate *self) {
  self->clearTextBuffer();
}

//  XmlStringRef QXmlStreamReaderPrivate::symString(int index)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate9symStringEi(
    QXmlStreamReaderPrivate *self,
    int index) {
  return new QtPrivate::XmlStringRef(self->symString(index));
}

//  QStringView QXmlStreamReaderPrivate::symView(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QXmlStreamReaderPrivate7symViewEi(
    const QXmlStreamReaderPrivate *self,
    int index) {
  return new QString(self->symView(index).toString());
}

//  XmlStringRef QXmlStreamReaderPrivate::symName(int index)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate7symNameEi(
    QXmlStreamReaderPrivate *self,
    int index) {
  return new QtPrivate::XmlStringRef(self->symName(index));
}

//  XmlStringRef QXmlStreamReaderPrivate::symPrefix(int index)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate9symPrefixEi(
    QXmlStreamReaderPrivate *self,
    int index) {
  return new QtPrivate::XmlStringRef(self->symPrefix(index));
}

//  XmlStringRef QXmlStreamReaderPrivate::symString(const Value &symbol)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate9symStringERKNS_5ValueE(
    QXmlStreamReaderPrivate *self,
    const QXmlStreamReaderPrivate::Value *symbol) {
  return new QtPrivate::XmlStringRef(self->symString(*symbol));
}

//  XmlStringRef QXmlStreamReaderPrivate::symName(const Value &symbol)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate7symNameERKNS_5ValueE(
    QXmlStreamReaderPrivate *self,
    const QXmlStreamReaderPrivate::Value *symbol) {
  return new QtPrivate::XmlStringRef(self->symName(*symbol));
}

//  XmlStringRef QXmlStreamReaderPrivate::symPrefix(const Value &symbol)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN23QXmlStreamReaderPrivate9symPrefixERKNS_5ValueE(
    QXmlStreamReaderPrivate *self,
    const QXmlStreamReaderPrivate::Value *symbol) {
  return new QtPrivate::XmlStringRef(self->symPrefix(*symbol));
}

//  void QXmlStreamReaderPrivate::clearSym()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate8clearSymEv(
    QXmlStreamReaderPrivate *self) {
  self->clearSym();
}

//  void QXmlStreamReaderPrivate::putChar(uint c)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate7putCharEj(
    QXmlStreamReaderPrivate *self,
    uint c) {
  self->putChar(c);
}

//  void QXmlStreamReaderPrivate::putChar(QChar c)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate7putCharE5QChar(
    QXmlStreamReaderPrivate *self,
    const QChar *c) {
  self->putChar(*c);
}

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::putString(QStringView s, qsizetype from)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate9putStringE11QStringViewx(
    QXmlStreamReaderPrivate *self,
    const QString *s,
    qsizetype from) {
  self->putString(QStringView(*s), from);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::putStringLiteral(QStringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate16putStringLiteralE11QStringView(
    QXmlStreamReaderPrivate *self,
    const QString *s) {
  self->putStringLiteral(QStringView(*s));
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::putReplacement(QStringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate14putReplacementE11QStringView(
    QXmlStreamReaderPrivate *self,
    const QString *s) {
  self->putReplacement(QStringView(*s));
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::putReplacementInAttributeValue(QStringView
//      s)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate30putReplacementInAttributeValueE11QStringView(
    QXmlStreamReaderPrivate *self,
    const QString *s) {
  self->putReplacementInAttributeValue(QStringView(*s));
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  void QXmlStreamReaderPrivate::injectToken(ushort tokenToInject)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate11injectTokenEt(
    QXmlStreamReaderPrivate *self,
    ushort tokenToInject) {
  self->injectToken(tokenToInject);
}

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  QString QXmlStreamReaderPrivate::resolveUndeclaredEntity(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QXmlStreamReaderPrivate23resolveUndeclaredEntityERK7QString(
    QXmlStreamReaderPrivate *self,
    const QString *name) {
  return new QString(self->resolveUndeclaredEntity(*name));
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::raiseError(QXmlStreamReader::Error error,
//      const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate10raiseErrorEN16QXmlStreamReader5ErrorERK7QString(
    QXmlStreamReaderPrivate *self,
    QXmlStreamReader::Error error,
    const QString *message) {
  self->raiseError(error, *message);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::raiseWellFormedError(const QString
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate20raiseWellFormedErrorERK7QString(
    QXmlStreamReaderPrivate *self,
    const QString *message) {
  self->raiseWellFormedError(*message);
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
//  void QXmlStreamReaderPrivate::raiseNamePrefixTooLongError()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate27raiseNamePrefixTooLongErrorEv(
    QXmlStreamReaderPrivate *self) {
  self->raiseNamePrefixTooLongError();
}
#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)

//  QXmlStreamReaderPrivate as the QXmlStreamPrivateTagStack it is built on
extern "C" Q_DECL_EXPORT
QXmlStreamPrivateTagStack *ritual_cast_QXmlStreamReaderPrivate_QXmlStreamPrivateTagStack(
    QXmlStreamReaderPrivate *self) {
  return static_cast<QXmlStreamPrivateTagStack *>(self);
}

#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)
