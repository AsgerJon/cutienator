//  Written by dev_tooling.RitualGenerator from the records of
//  QtXml/6.12.0/QtXml/private/qdomhelpers_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtXml/qtxmlglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtXml/QtXml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtXml/6.12.0/QtXml/private/qdomhelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtXml/qdom.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/private/qdomhelpers_p.h>
#include <QtXml/private/qdom_p.h>
#include <QtCore/qshareddata.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/private/qxmlstream_p.h>
#include <memory>
#include <stack>
#endif
#include <qplatformdefs.h>
#include <QtXml/qdom.h>
#include <QtCore/private/qxmlutils_p.h>
#if QT_CONFIG(dom)
#include <QtXml/private/qdom_p.h>
#include <QtXml/private/qdomhelpers_p.h>
#include <QtCore/qatomic.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qiodevice.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qtextstream.h>
#include <QtCore/qvariant.h>
#include <QtCore/qshareddata.h>
#include <QtCore/qdebug.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qstringiterator_p.h>
#include <QtCore/qvarlengtharray.h>
#include <stdio.h>
#include <limits>
#include <memory>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/xml/dom/qdomhelpers.cpp, line 40, as _ZN11QDomBuilderC1EP19QDomDocumentPrivateP16QXmlStreamReader6QFlagsIN12QDomDocument11ParseOptionEE
#if QT_CONFIG(dom)
inline QDomBuilder::QDomBuilder(QDomDocumentPrivate *d, QXmlStreamReader *r,
                         QDomDocument::ParseOptions options)
    : doc(d), node(d), reader(r), parseOptions(options)
{
    Q_ASSERT(doc);
    Q_ASSERT(reader);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 126, as _ZN11QDomBuilder10endElementEv
#if QT_CONFIG(dom)
inline bool QDomBuilder::endElement()
{
    if (!node || node == doc)
        return false;
    node = node->parent();

    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 184, as _ZN11QDomBuilder10fatalErrorERK7QString
#if QT_CONFIG(dom)
inline void QDomBuilder::fatalError(const QString &message)
{
    parseResult.errorMessage = message;
    parseResult.errorLine = reader->lineNumber();
    parseResult.errorColumn = reader->columnNumber();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 95, as _ZN11QDomBuilder12startElementERK7QStringS2_RK20QXmlStreamAttributes
#if QT_CONFIG(dom)
inline bool QDomBuilder::startElement(const QString &nsURI, const QString &qName,
                               const QXmlStreamAttributes &atts)
{
    const bool nsProcessing =
            parseOptions.testFlag(QDomDocument::ParseOption::UseNamespaceProcessing);
    QDomNodePrivate *n =
            nsProcessing ? doc->createElementNS(nsURI, qName) : doc->createElement(qName);
    if (!n)
        return false;

    n->setLocation(int(reader->lineNumber()), int(reader->columnNumber()));

    node->appendChild(n);
    node = n;

    // attributes
    for (const auto &attr : atts) {
        auto domElement = static_cast<QDomElementPrivate *>(node);
        if (nsProcessing) {
            domElement->setAttributeNS(attr.namespaceUri().toString(),
                                       attr.qualifiedName().toString(),
                                       attr.value().toString());
        } else {
            domElement->setAttribute(attr.qualifiedName().toString(),
                                     attr.value().toString());
        }
    }

    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 174, as _ZN11QDomBuilder13skippedEntityERK7QString
#if QT_CONFIG(dom)
inline bool QDomBuilder::skippedEntity(const QString &name)
{
    QDomNodePrivate *n = doc->createEntityReference(name);
    if (!n)
        return false;
    n->setLocation(int(reader->lineNumber()), int(reader->columnNumber()));
    node->appendChild(n);
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 162, as _ZN11QDomBuilder21processingInstructionERK7QStringS2_
#if QT_CONFIG(dom)
inline bool QDomBuilder::processingInstruction(const QString &target, const QString &data)
{
    QDomNodePrivate *n;
    n = doc->createProcessingInstruction(target, data);
    if (n) {
        n->setLocation(int(reader->lineNumber()), int(reader->columnNumber()));
        node->appendChild(n);
        return true;
    } else
        return false;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 203, as _ZN11QDomBuilder7commentERK7QString
#if QT_CONFIG(dom)
inline bool QDomBuilder::comment(const QString &characters)
{
    QDomNodePrivate *n;
    n = doc->createComment(characters);
    if (!n)
        return false;
    n->setLocation(int(reader->lineNumber()), int(reader->columnNumber()));
    node->appendChild(n);
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 231, as _ZN11QDomBuilder12notationDeclERK7QStringS2_S2_
#if QT_CONFIG(dom)
inline bool QDomBuilder::notationDecl(const QString &name, const QString &publicId,
                               const QString &systemId)
{
    QDomNotationPrivate *n = new QDomNotationPrivate(doc, nullptr, name, publicId, systemId);
    // keep the refcount balanced: appendChild() does a ref anyway.
    n->ref.deref();
    doc->doctype()->appendChild(n);
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 214, as _ZN11QDomBuilder18unparsedEntityDeclERK7QStringS2_S2_S2_
#if QT_CONFIG(dom)
inline bool QDomBuilder::unparsedEntityDecl(const QString &name, const QString &publicId,
                                     const QString &systemId, const QString &notationName)
{
    QDomEntityPrivate *e =
            new QDomEntityPrivate(doc, nullptr, name, publicId, systemId, notationName);
    // keep the refcount balanced: appendChild() does a ref anyway.
    e->ref.deref();
    doc->doctype()->appendChild(e);
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5349, as _ZN17QDomEntityPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QStringS6_S6_S6_
#if QT_CONFIG(dom)
inline QDomEntityPrivate::QDomEntityPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent,
                                        const QString& aname,
                                        const QString& pub, const QString& sys, const QString& notation)
    : QDomNodePrivate(d, parent)
{
    name = aname;
    m_pub = pub;
    m_sys = sys;
    m_notationName = notation;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5206, as _ZN19QDomNotationPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QStringS6_S6_
#if QT_CONFIG(dom)
inline QDomNotationPrivate::QDomNotationPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent,
                                            const QString& aname,
                                            const QString& pub, const QString& sys)
    : QDomNodePrivate(d, parent)
{
    name = aname;
    m_pub = pub;
    m_sys = sys;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 247, as _ZN10QDomParserC1EP19QDomDocumentPrivateP16QXmlStreamReader6QFlagsIN12QDomDocument11ParseOptionEE
#if QT_CONFIG(dom)
inline QDomParser::QDomParser(QDomDocumentPrivate *d, QXmlStreamReader *r,
                       QDomDocument::ParseOptions options)
    : reader(r), domBuilder(d, r, options)
{
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  QString QDomParser::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QDomParser2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QDomParser::tr(sourceText, disambiguation, n));
}

//  QDomParser::QDomParser(QDomDocumentPrivate *d, QXmlStreamReader *r,
//      QDomDocument::ParseOptions options)
extern "C" Q_DECL_EXPORT
QDomParser *ritual_ZN10QDomParserC1EP19QDomDocumentPrivateP16QXmlStreamReader6QFlagsIN12QDomDocument11ParseOptionEE(
    QDomDocumentPrivate *d,
    QXmlStreamReader *r,
    int options) {
  return new QDomParser(
      d,
      r,
      QFlags<QDomDocument::ParseOption>::fromInt(options));
}

//  QDomDocument::ParseResult QDomParser::result() const
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZNK10QDomParser6resultEv(
    const QDomParser *self) {
  return new QDomDocument::ParseResult(self->result());
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
