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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/xml/dom/qdom.cpp, line 74, as local:qdom.cpp:qt_split_namespace
#if QT_CONFIG(dom)
static void qt_split_namespace(QString& prefix, QString& name, const QString& qName, bool hasURI)
{
    qsizetype i = qName.indexOf(u':');
    if (i == -1) {
        if (hasURI)
            prefix = u""_s;
        else
            prefix.clear();
        name = qName;
    } else {
        prefix = qName.left(i);
        name = qName.mid(i + 1);
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 99, as local:qdom.cpp:fixedXmlName
#if QT_CONFIG(dom)
static QString fixedXmlName(const QString &_name, bool *ok, bool namespaces = false)
{
    QString name, prefix;
    if (namespaces)
        qt_split_namespace(prefix, name, _name, true);
    else
        name = _name;

    if (name.isEmpty()) {
        *ok = false;
        return QString();
    }

    if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::AcceptInvalidChars) {
        *ok = true;
        return _name;
    }

    QString result;
    bool firstChar = true;
    for (int i = 0; i < name.size(); ++i) {
        QChar c = name.at(i);
        if (firstChar) {
            if (QXmlUtils::isLetter(c) || c.unicode() == '_' || c.unicode() == ':') {
                result.append(c);
                firstChar = false;
            } else if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
                *ok = false;
                return QString();
            }
        } else {
            if (QXmlUtils::isNameChar(c))
                result.append(c);
            else if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
                *ok = false;
                return QString();
            }
        }
    }

    if (result.isEmpty()) {
        *ok = false;
        return QString();
    }

    *ok = true;
    if (namespaces && !prefix.isEmpty())
        return prefix + u':' + result;
    return result;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 153, as local:qdom.cpp:fixedCharData
#if QT_CONFIG(dom)
static QString fixedCharData(const QString &data, bool *ok)
{
    if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::AcceptInvalidChars) {
        *ok = true;
        return data;
    }

    QString result;
    QStringIterator it(data);
    while (it.hasNext()) {
        const char32_t c = it.next(QChar::Null);
        if (QXmlUtils::isChar(c)) {
            result.append(QChar::fromUcs4(c));
        } else if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
            *ok = false;
            return QString();
        }
    }

    *ok = true;
    return result;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 179, as local:qdom.cpp:fixedComment
#if QT_CONFIG(dom)
static QString fixedComment(const QString &data, bool *ok)
{
    if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::AcceptInvalidChars) {
        *ok = true;
        return data;
    }

    QString fixedData = fixedCharData(data, ok);
    if (!*ok)
        return QString();

    for (;;) {
        qsizetype idx = fixedData.indexOf("--"_L1);
        if (idx == -1)
            break;
        if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
            *ok = false;
            return QString();
        }
        fixedData.remove(idx, 2);
    }

    *ok = true;
    return fixedData;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 208, as local:qdom.cpp:fixedCDataSection
#if QT_CONFIG(dom)
static QString fixedCDataSection(const QString &data, bool *ok)
{
    if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::AcceptInvalidChars) {
        *ok = true;
        return data;
    }

    QString fixedData = fixedCharData(data, ok);
    if (!*ok)
        return QString();

    for (;;) {
        qsizetype idx = fixedData.indexOf("]]>"_L1);
        if (idx == -1)
            break;
        if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
            *ok = false;
            return QString();
        }
        fixedData.remove(idx, 3);
    }

    *ok = true;
    return fixedData;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 236, as local:qdom.cpp:fixedPIData
#if QT_CONFIG(dom)
static QString fixedPIData(const QString &data, bool *ok)
{
    if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::AcceptInvalidChars) {
        *ok = true;
        return data;
    }

    QString fixedData = fixedCharData(data, ok);
    if (!*ok)
        return QString();

    for (;;) {
        qsizetype idx = fixedData.indexOf("?>"_L1);
        if (idx == -1)
            break;
        if (QDomImplementationPrivate::invalidDataPolicy == QDomImplementation::ReturnNullNode) {
            *ok = false;
            return QString();
        }
        fixedData.remove(idx, 2);
    }

    *ok = true;
    return fixedData;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 23, as local:qdomhelpers.cpp:qdom_make_esdp
#if QT_CONFIG(dom)
template <typename T, typename...Args>
static QExplicitlySharedDataPointer<T> qdom_make_esdp(Args&&...args)
{
    QExplicitlySharedDataPointer<T> dp{
        new T(std::forward<Args>(args)...),
        QAdoptSharedDataTag{}
    };
    Q_ASSERT(dp->ref.loadRelaxed() == 1);
    return dp;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1545, as _ZN15QDomNodePrivate11setLocationEii
#if QT_CONFIG(dom)
inline void QDomNodePrivate::setLocation(int lineNumber, int columnNumber)
{
    this->lineNumber = lineNumber;
    this->columnNumber = columnNumber;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4077, as _ZN18QDomElementPrivate12setAttributeERK7QStringS2_
#if QT_CONFIG(dom)
inline void QDomElementPrivate::setAttribute(const QString& aname, const QString& newValue)
{
    QDomNodePrivate* n = m_attr->namedItem(aname);
    if (!n) {
        n = new QDomAttrPrivate(ownerDocument(), this, aname);
        n->setNodeValue(newValue);

        // Referencing is done by the map, so we set the reference counter back
        // to 0 here. This is ok since we created the QDomAttrPrivate.
        n->ref.deref();
        m_attr->setNamedItem(n);
    } else {
        n->setNodeValue(newValue);
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4093, as _ZN18QDomElementPrivate14setAttributeNSERK7QStringS2_S2_
#if QT_CONFIG(dom)
inline void QDomElementPrivate::setAttributeNS(const QString& nsURI, const QString& qName, const QString& newValue)
{
    QString prefix, localName;
    qt_split_namespace(prefix, localName, qName, true);
    QDomNodePrivate* n = m_attr->namedItemNS(nsURI, localName);
    if (!n) {
        n = new QDomAttrPrivate(ownerDocument(), this, nsURI, qName);
        n->setNodeValue(newValue);

        // Referencing is done by the map, so we set the reference counter back
        // to 0 here. This is ok since we created the QDomAttrPrivate.
        n->ref.deref();
        m_attr->setNamedItem(n);
    } else {
        n->setNodeValue(newValue);
        n->prefix = std::move(prefix);
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5924, as _ZN19QDomDocumentPrivate13createElementERK7QString
#if QT_CONFIG(dom)
inline QDomElementPrivate* QDomDocumentPrivate::createElement(const QString &tagName)
{
    bool ok;
    QString fixedName = fixedXmlName(tagName, &ok);
    if (!ok)
        return nullptr;

    QDomElementPrivate *e = new QDomElementPrivate(this, nullptr, fixedName);
    e->ref.deref();
    return e;
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

//  from src/xml/dom/qdom.cpp, line 5955, as _ZN19QDomDocumentPrivate14createTextNodeERK7QString
#if QT_CONFIG(dom)
inline QDomTextPrivate* QDomDocumentPrivate::createTextNode(const QString &data)
{
    bool ok;
    QString fixedData = fixedCharData(data, &ok);
    if (!ok)
        return nullptr;

    QDomTextPrivate *t = new QDomTextPrivate(this, nullptr, fixedData);
    t->ref.deref();
    return t;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5979, as _ZN19QDomDocumentPrivate18createCDATASectionERK7QString
#if QT_CONFIG(dom)
inline QDomCDATASectionPrivate* QDomDocumentPrivate::createCDATASection(const QString &data)
{
    bool ok;
    QString fixedData = fixedCDataSection(data, &ok);
    if (!ok)
        return nullptr;

    QDomCDATASectionPrivate *c = new QDomCDATASectionPrivate(this, nullptr, fixedData);
    c->ref.deref();
    return c;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5967, as _ZN19QDomDocumentPrivate13createCommentERK7QString
#if QT_CONFIG(dom)
inline QDomCommentPrivate* QDomDocumentPrivate::createComment(const QString &data)
{
    bool ok;
    QString fixedData = fixedComment(data, &ok);
    if (!ok)
        return nullptr;

    QDomCommentPrivate *c = new QDomCommentPrivate(this, nullptr, fixedData);
    c->ref.deref();
    return c;
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

//  from src/xml/dom/qdom.cpp, line 3726, as _ZN15QDomAttrPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent, const QString& name_)
    : QDomNodePrivate(d, parent)
{
    name = name_;
    m_specified = false;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 3733, as _ZN15QDomAttrPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QStringS6_
#if QT_CONFIG(dom)
inline QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate* d, QDomNodePrivate* p, const QString& nsURI, const QString& qName)
    : QDomNodePrivate(d, p)
{
    qt_split_namespace(prefix, name, qName, !nsURI.isNull());
    namespaceURI = nsURI;
    createdWithDom1Interface = false;
    m_specified = false;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1460, as _ZN15QDomNodePrivate13ownerDocumentEv
#if QT_CONFIG(dom)
inline QDomDocumentPrivate* QDomNodePrivate::ownerDocument()
{
    QDomNodePrivate* p = this;
    while (p && !p->isDocument()) {
        if (!p->hasParent)
            return static_cast<QDomDocumentPrivate *>(p->ownerNode);
        p = p->parent();
    }

    return static_cast<QDomDocumentPrivate *>(p);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4019, as _ZN18QDomElementPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomElementPrivate::QDomElementPrivate(QDomDocumentPrivate* d, QDomNodePrivate* p,
                                          const QString& tagname)
    : QDomNodePrivate(d, p)
{
    name = tagname;
    m_attr = new QDomNamedNodeMapPrivate(this);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4992, as _ZN18QDomCommentPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomCommentPrivate::QDomCommentPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent, const QString& val)
    : QDomCharacterDataPrivate(d, parent, val)
{
    name = u"#comment"_s;
}
#endif  // QT_CONFIG(dom)

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

//  from src/xml/dom/qdomhelpers.cpp, line 48, as _ZN11QDomBuilderD1Ev
#if QT_CONFIG(dom)
inline QDomBuilder::~QDomBuilder() {}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 50, as _ZN11QDomBuilder11endDocumentEv
#if QT_CONFIG(dom)
inline bool QDomBuilder::endDocument()
{
    // ### is this really necessary? (rms)
    if (node != doc)
        return false;
    return true;
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

//  from src/xml/dom/qdomhelpers.cpp, line 191, as _ZN11QDomBuilder11startEntityERK7QString
#if QT_CONFIG(dom)
inline bool QDomBuilder::startEntity(const QString &name)
{
    entityName = name;
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 197, as _ZN11QDomBuilder9endEntityEv
#if QT_CONFIG(dom)
inline bool QDomBuilder::endEntity()
{
    entityName.clear();
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 58, as _ZN11QDomBuilder8startDTDERK7QStringS2_S2_
#if QT_CONFIG(dom)
inline bool QDomBuilder::startDTD(const QString &name, const QString &publicId, const QString &systemId)
{
    doc->doctype()->name = name;
    doc->doctype()->publicId = publicId;
    doc->doctype()->systemId = systemId;
    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 89, as _ZN11QDomBuilder8parseDTDERK7QString
#if QT_CONFIG(dom)
inline bool QDomBuilder::parseDTD(const QString &dtd)
{
    doc->doctype()->internalSubset = dtdInternalSubset(dtd);
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

//  from src/xml/dom/qdomhelpers.cpp, line 66, as _ZN11QDomBuilder17dtdInternalSubsetERK7QString
#if QT_CONFIG(dom)
inline QString QDomBuilder::dtdInternalSubset(const QString &dtd)
{
    // https://www.w3.org/TR/xml/#NT-intSubset
    // doctypedecl: '<!DOCTYPE' S Name (S ExternalID)? S? ('[' intSubset ']' S?)? '>'
    const QString &name = doc->doctype()->name;
    QStringView tmp = QStringView(dtd).sliced(dtd.indexOf(name) + name.size());

    const QString &publicId = doc->doctype()->publicId;
    if (!publicId.isEmpty())
        tmp = tmp.sliced(tmp.indexOf(publicId) + publicId.size());

    const QString &systemId = doc->doctype()->systemId;
    if (!systemId.isEmpty())
        tmp = tmp.sliced(tmp.indexOf(systemId) + systemId.size());

    const qsizetype obra = tmp.indexOf(u'[');
    const qsizetype cbra = tmp.lastIndexOf(u']');
    if (obra >= 0 && cbra >= 0)
        return tmp.left(cbra).sliced(obra + 1).toString();

    return QString();
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  QDomBuilder::QDomBuilder(QDomDocumentPrivate *d, QXmlStreamReader *r,
//      QDomDocument::ParseOptions options)
extern "C" Q_DECL_EXPORT
QDomBuilder *ritual_ZN11QDomBuilderC1EP19QDomDocumentPrivateP16QXmlStreamReader6QFlagsIN12QDomDocument11ParseOptionEE(
    QDomDocumentPrivate *d,
    QXmlStreamReader *r,
    int options) {
  return new QDomBuilder(
      d,
      r,
      QFlags<QDomDocument::ParseOption>::fromInt(options));
}

//  QDomBuilder::~QDomBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomBuilderD1Ev(QDomBuilder *self) {
  delete self;
}

#if QT_CONFIG(dom)
//  bool QDomBuilder::endDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder11endDocumentEv(QDomBuilder *self) {
  return self->endDocument();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomBuilder::endElement()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder10endElementEv(QDomBuilder *self) {
  return self->endElement();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomBuilder::startEntity(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder11startEntityERK7QString(
    QDomBuilder *self,
    const QString *name) {
  return self->startEntity(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomBuilder::endEntity()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder9endEntityEv(QDomBuilder *self) {
  return self->endEntity();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomBuilder::startDTD(const QString &name, const QString &publicId,
//      const QString &systemId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder8startDTDERK7QStringS2_S2_(
    QDomBuilder *self,
    const QString *name,
    const QString *publicId,
    const QString *systemId) {
  return self->startDTD(*name, *publicId, *systemId);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomBuilder::parseDTD(const QString &dtd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDomBuilder8parseDTDERK7QString(
    QDomBuilder *self,
    const QString *dtd) {
  return self->parseDTD(*dtd);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomBuilder::fatalError(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomBuilder10fatalErrorERK7QString(
    QDomBuilder *self,
    const QString *message) {
  self->fatalError(*message);
}
#endif  // QT_CONFIG(dom)

//  QDomDocument::ParseResult QDomBuilder::result() const
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZNK11QDomBuilder6resultEv(
    const QDomBuilder *self) {
  return new QDomDocument::ParseResult(self->result());
}

//  bool QDomBuilder::preserveSpacingOnlyNodes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDomBuilder24preserveSpacingOnlyNodesEv(
    const QDomBuilder *self) {
  return self->preserveSpacingOnlyNodes();
}

#if QT_CONFIG(dom)
//  QString QDomBuilder::dtdInternalSubset(const QString &dtd)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QDomBuilder17dtdInternalSubsetERK7QString(
    QDomBuilder *self,
    const QString *dtd) {
  return new QString(self->dtdInternalSubset(*dtd));
}
#endif  // QT_CONFIG(dom)

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
