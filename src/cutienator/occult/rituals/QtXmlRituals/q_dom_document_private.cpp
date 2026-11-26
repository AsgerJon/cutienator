//  Written by dev_tooling.RitualGenerator from the records of
//  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtXml/qtxmlglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtXml/QtXml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtXml/6.12.0/QtXml/private/qdom_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from src/xml/dom/qdom.cpp, line 1480, as local:qdom.cpp:qNormalizeNode
#if QT_CONFIG(dom)
static void qNormalizeNode(QDomNodePrivate* n)
{
    QDomNodePrivate* p = n->first;
    QDomTextPrivate* t = nullptr;

    while (p) {
        if (p->isText()) {
            if (t) {
                QDomNodePrivate* tmp = p->next;
                t->appendData(p->nodeValue());
                n->removeChild(p);
                p = tmp;
            } else {
                t = static_cast<QDomTextPrivate *>(p);
                p = p->next;
            }
        } else {
            p = p->next;
            t = nullptr;
        }
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1454, as _ZN15QDomNodePrivate11appendChildEPS_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::appendChild(QDomNodePrivate* newChild)
{
    // No reference manipulation needed. Done in insertAfter.
    return insertAfter(newChild, nullptr);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1230, as _ZN15QDomNodePrivate11insertAfterEPS_S0_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::insertAfter(QDomNodePrivate* newChild, QDomNodePrivate* refChild)
{
    // Error check
    if (!newChild)
        return nullptr;

    // Error check
    if (newChild == refChild)
        return nullptr;

    // Error check
    if (refChild && refChild->parent() != this)
        return nullptr;

    // "mark lists as dirty"
    QDomDocumentPrivate *const doc = ownerDocument();
    if (doc)
        doc->nodeListTime++;

    // Special handling for inserting a fragment. We just insert
    // all elements of the fragment instead of the fragment itself.
    if (newChild->isDocumentFragment()) {
        // Fragment is empty ?
        if (newChild->first == nullptr)
            return newChild;

        // New parent
        QDomNodePrivate* n = newChild->first;
        while (n) {
            n->setParent(this);
            n = n->next;
        }

        // Insert at the end
        if (!refChild || refChild->next == nullptr) {
            if (last)
                last->next = newChild->first;
            newChild->first->prev = last;
            if (!first)
                first = newChild->first;
            last = newChild->last;
        } else { // Insert in the middle
            newChild->first->prev = refChild;
            newChild->last->next = refChild->next;
            refChild->next->prev = newChild->last;
            refChild->next = newChild->first;
        }

        // No need to increase the reference since QDomDocumentFragment
        // does not decrease the reference.

        // Remove the nodes from the fragment
        newChild->first = nullptr;
        newChild->last = nullptr;
        return newChild;
    }

    // Release new node from its current parent
    if (newChild->parent())
        newChild->parent()->removeChild(newChild);

    // No more errors can occur now, so we take
    // ownership of the node
    newChild->ref.ref();

    newChild->setParent(this);

    // Insert at the end
    if (!refChild) {
        if (last)
            last->next = newChild;
        newChild->prev = last;
        if (!first)
            first = newChild;
        last = newChild;
        return newChild;
    }

    if (refChild->next == nullptr) {
        if (last)
            last->next = newChild;
        newChild->prev = last;
        if (!first)
            first = newChild;
        last = newChild;
        return newChild;
    }

    newChild->prev = refChild;
    newChild->next = refChild->next;
    refChild->next->prev = newChild;
    refChild->next = newChild;

    return newChild;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1418, as _ZN15QDomNodePrivate11removeChildEPS_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::removeChild(QDomNodePrivate* oldChild)
{
    // Error check
    if (oldChild->parent() != this)
        return nullptr;

    // "mark lists as dirty"
    QDomDocumentPrivate *const doc = ownerDocument();
    if (doc)
        doc->nodeListTime++;

    // Perhaps oldChild was just created with "createElement" or that. In this case
    // its parent is QDomDocument but it is not part of the documents child list.
    if (oldChild->next == nullptr && oldChild->prev == nullptr && first != oldChild)
        return nullptr;

    if (oldChild->next)
        oldChild->next->prev = oldChild->prev;
    if (oldChild->prev)
        oldChild->prev->next = oldChild->next;

    if (last == oldChild)
        last = oldChild->prev;
    if (first == oldChild)
        first = oldChild->next;

    oldChild->setNoParent();
    oldChild->next = nullptr;
    oldChild->prev = nullptr;

    // We are no longer interested in the old node
    oldChild->ref.deref();

    return oldChild;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1135, as _ZN15QDomNodePrivate12insertBeforeEPS_S0_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::insertBefore(QDomNodePrivate* newChild, QDomNodePrivate* refChild)
{
    // Error check
    if (!newChild)
        return nullptr;

    // Error check
    if (newChild == refChild)
        return nullptr;

    // Error check
    if (refChild && refChild->parent() != this)
        return nullptr;

    // "mark lists as dirty"
    QDomDocumentPrivate *const doc = ownerDocument();
    if (doc)
        doc->nodeListTime++;

    // Special handling for inserting a fragment. We just insert
    // all elements of the fragment instead of the fragment itself.
    if (newChild->isDocumentFragment()) {
        // Fragment is empty ?
        if (newChild->first == nullptr)
            return newChild;

        // New parent
        QDomNodePrivate* n = newChild->first;
        while (n)  {
            n->setParent(this);
            n = n->next;
        }

        // Insert at the beginning ?
        if (!refChild || refChild->prev == nullptr) {
            if (first)
                first->prev = newChild->last;
            newChild->last->next = first;
            if (!last)
                last = newChild->last;
            first = newChild->first;
        } else {
            // Insert in the middle
            newChild->last->next = refChild;
            newChild->first->prev = refChild->prev;
            refChild->prev->next = newChild->first;
            refChild->prev = newChild->last;
        }

        // No need to increase the reference since QDomDocumentFragment
        // does not decrease the reference.

        // Remove the nodes from the fragment
        newChild->first = nullptr;
        newChild->last = nullptr;
        return newChild;
    }

    // No more errors can occur now, so we take
    // ownership of the node.
    newChild->ref.ref();

    if (newChild->parent())
        newChild->parent()->removeChild(newChild);

    newChild->setParent(this);

    if (!refChild) {
        if (first)
            first->prev = newChild;
        newChild->next = first;
        if (!last)
            last = newChild;
        first = newChild;
        return newChild;
    }

    if (refChild->prev == nullptr) {
        if (first)
            first->prev = newChild;
        newChild->next = first;
        if (!last)
            last = newChild;
        first = newChild;
        return newChild;
    }

    newChild->next = refChild;
    newChild->prev = refChild->prev;
    refChild->prev->next = newChild;
    refChild->prev = newChild;

    return newChild;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1326, as _ZN15QDomNodePrivate12replaceChildEPS_S0_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::replaceChild(QDomNodePrivate* newChild, QDomNodePrivate* oldChild)
{
    if (!newChild || !oldChild)
        return nullptr;
    if (oldChild->parent() != this)
        return nullptr;
    if (newChild == oldChild)
        return nullptr;

    // mark lists as dirty
    QDomDocumentPrivate *const doc = ownerDocument();
    if (doc)
        doc->nodeListTime++;

    // Special handling for inserting a fragment. We just insert
    // all elements of the fragment instead of the fragment itself.
    if (newChild->isDocumentFragment()) {
        // Fragment is empty ?
        if (newChild->first == nullptr)
            return newChild;

        // New parent
        QDomNodePrivate* n = newChild->first;
        while (n) {
            n->setParent(this);
            n = n->next;
        }


        if (oldChild->next)
            oldChild->next->prev = newChild->last;
        if (oldChild->prev)
            oldChild->prev->next = newChild->first;

        newChild->last->next = oldChild->next;
        newChild->first->prev = oldChild->prev;

        if (first == oldChild)
            first = newChild->first;
        if (last == oldChild)
            last = newChild->last;

        oldChild->setNoParent();
        oldChild->next = nullptr;
        oldChild->prev = nullptr;

        // No need to increase the reference since QDomDocumentFragment
        // does not decrease the reference.

        // Remove the nodes from the fragment
        newChild->first = nullptr;
        newChild->last = nullptr;

        // We are no longer interested in the old node
        oldChild->ref.deref();

        return oldChild;
    }

    // No more errors can occur now, so we take
    // ownership of the node
    newChild->ref.ref();

    // Release new node from its current parent
    if (newChild->parent())
        newChild->parent()->removeChild(newChild);

    newChild->setParent(this);

    if (oldChild->next)
        oldChild->next->prev = newChild;
    if (oldChild->prev)
        oldChild->prev->next = newChild;

    newChild->next = oldChild->next;
    newChild->prev = oldChild->prev;

    if (first == oldChild)
        first = newChild;
    if (last == oldChild)
        last = newChild;

    oldChild->setNoParent();
    oldChild->next = nullptr;
    oldChild->prev = nullptr;

    // We are no longer interested in the old node
    oldChild->ref.deref();

    return oldChild;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1502, as _ZN15QDomNodePrivate9normalizeEv
#if QT_CONFIG(dom)
inline void QDomNodePrivate::normalize()
{
    // ### This one has moved from QDomElementPrivate to this position. It is
    // not tested.
    qNormalizeNode(this);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdomhelpers.cpp, line 253, as _ZN10QDomParser5parseEv
#if QT_CONFIG(dom)
inline bool QDomParser::parse()
{
    return parseProlog() && parseBody();
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

//  from src/xml/dom/qdomhelpers.cpp, line 48, as _ZN11QDomBuilderD1Ev
#if QT_CONFIG(dom)
inline QDomBuilder::~QDomBuilder() {}
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

//  from src/xml/dom/qdom.cpp, line 4855, as _ZN15QDomTextPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomTextPrivate::QDomTextPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent, const QString& val)
    : QDomCharacterDataPrivate(d, parent, val)
{
    name = u"#text"_s;
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

//  from src/xml/dom/qdom.cpp, line 5101, as _ZN23QDomCDATASectionPrivateC1EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomCDATASectionPrivate::QDomCDATASectionPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent,
                                                    const QString& val)
    : QDomTextPrivate(d, parent, val)
{
    name = u"#cdata-section"_s;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 3742, as _ZN15QDomAttrPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomAttrPrivate::QDomAttrPrivate(QDomAttrPrivate* n, bool deep)
    : QDomNodePrivate(n, deep)
{
    m_specified = n->specified();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1044, as _ZN15QDomNodePrivate16setOwnerDocumentEP19QDomDocumentPrivate
#if QT_CONFIG(dom)
inline void QDomNodePrivate::setOwnerDocument(QDomDocumentPrivate *doc)
{
    ownerNode = doc;
    hasParent = false;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4861, as _ZN15QDomTextPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomTextPrivate::QDomTextPrivate(QDomTextPrivate* n, bool deep)
    : QDomCharacterDataPrivate(n, deep)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5360, as _ZN17QDomEntityPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomEntityPrivate::QDomEntityPrivate(QDomEntityPrivate* n, bool deep)
    : QDomNodePrivate(n, deep)
{
    m_sys = n->m_sys;
    m_pub = n->m_pub;
    m_notationName = n->m_notationName;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4998, as _ZN18QDomCommentPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomCommentPrivate::QDomCommentPrivate(QDomCommentPrivate* n, bool deep)
    : QDomCharacterDataPrivate(n, deep)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4037, as _ZN18QDomElementPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomElementPrivate::QDomElementPrivate(QDomElementPrivate* n, bool deep) :
    QDomNodePrivate(n, deep)
{
    m_attr = n->m_attr->clone(this);
    // Reference is down to 0, so we set it to 1 here.
    m_attr->ref.ref();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5216, as _ZN19QDomNotationPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomNotationPrivate::QDomNotationPrivate(QDomNotationPrivate* n, bool deep)
    : QDomNodePrivate(n, deep)
{
    m_sys = n->m_sys;
    m_pub = n->m_pub;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5108, as _ZN23QDomCDATASectionPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomCDATASectionPrivate::QDomCDATASectionPrivate(QDomCDATASectionPrivate* n, bool deep)
    : QDomTextPrivate(n, deep)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5563, as _ZN26QDomEntityReferencePrivateC1EP15QDomNodePrivateb
#if QT_CONFIG(dom)
inline QDomEntityReferencePrivate::QDomEntityReferencePrivate(QDomNodePrivate* n, bool deep)
    : QDomNodePrivate(n, deep)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1509, as _ZNK15QDomNodePrivate11saveSubTreeEPKS_R11QTextStreamii
#if QT_CONFIG(dom)
inline void QDomNodePrivate::saveSubTree(const QDomNodePrivate *n, QTextStream &s,
                                  int depth, int indent) const
{
    if (!n)
        return;

    const QDomNodePrivate *root = n->first;
    n->save(s, depth, indent);
    if (root) {
        const int branchDepth = depth + 1;
        int layerDepth = 0;
        while (root) {
            root->save(s, layerDepth + branchDepth, indent);
            // A flattened (non-recursive) depth-first walk through the node tree.
            if (root->first) {
                layerDepth ++;
                root = root->first;
                continue;
            }
            root->afterSave(s, layerDepth + branchDepth, indent);
            const QDomNodePrivate *prev = root;
            root = root->next;
            // Close QDomElementPrivate groups
            while (!root && (layerDepth > 0)) {
                root = prev->parent();
                layerDepth --;
                root->afterSave(s, layerDepth + branchDepth, indent);
                prev = root;
                root = root->next;
            }
        }
        Q_ASSERT(layerDepth == 0);
    }
    n->afterSave(s, depth, indent);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5907, as _ZN19QDomDocumentPrivate9cloneNodeEb
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomDocumentPrivate::cloneNode(bool deep)
{
    QDomNodePrivate *p = new QDomDocumentPrivate(this, deep);
    // We are not interested in this node
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5879, as _ZN19QDomDocumentPrivate5clearEv
#if QT_CONFIG(dom)
inline void QDomDocumentPrivate::clear()
{
    impl.reset();
    type.reset();
    QDomNodePrivate::clear();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5866, as _ZN19QDomDocumentPrivateC1EPS_b
#if QT_CONFIG(dom)
inline QDomDocumentPrivate::QDomDocumentPrivate(QDomDocumentPrivate* n, bool deep)
    : QDomNodePrivate(n, deep),
      impl(n->impl->clone()),
      nodeListTime(1)
{
    type = static_cast<QDomDocumentTypePrivate*>(n->type->cloneNode());
    type->setParent(this);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1108, as _ZN15QDomNodePrivate5clearEv
#if QT_CONFIG(dom)
inline void QDomNodePrivate::clear()
{
    QDomNodePrivate* p = first;
    QDomNodePrivate* n;

    while (p) {
        n = p->next;
        if (!p->ref.deref())
            delete p;
        p = n;
    }
    first = nullptr;
    last = nullptr;
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

//  from src/xml/dom/qdom.cpp, line 5875, as _ZN19QDomDocumentPrivateD1Ev
#if QT_CONFIG(dom)
inline QDomDocumentPrivate::~QDomDocumentPrivate()
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5915, as _ZN19QDomDocumentPrivate15documentElementEv
#if QT_CONFIG(dom)
inline QDomElementPrivate* QDomDocumentPrivate::documentElement()
{
    QDomNodePrivate *p = first;
    while (p && !p->isElement())
        p = p->next;

    return static_cast<QDomElementPrivate *>(p);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 6093, as _ZNK19QDomDocumentPrivate12saveDocumentER11QTextStreamiN8QDomNode14EncodingPolicyE
#if QT_CONFIG(dom)
inline void QDomDocumentPrivate::saveDocument(QTextStream& s, const int indent, QDomNode::EncodingPolicy encUsed) const
{
    const QDomNodePrivate* n = first;

    if (encUsed == QDomNode::EncodingFromDocument) {
#if QT_CONFIG(regularexpression)
        const QDomNodePrivate* n = first;

        if (n && n->isProcessingInstruction() && n->nodeName() == "xml"_L1) {
            // we have an XML declaration
            QString data = n->nodeValue();
            QRegularExpression encoding(QString::fromLatin1("encoding\\s*=\\s*((\"([^\"]*)\")|('([^']*)'))"));
            auto match = encoding.match(data);
            QString enc = match.captured(3);
            if (enc.isEmpty())
                enc = match.captured(5);
            if (!enc.isEmpty()) {
                auto encoding = QStringConverter::encodingForName(enc.toUtf8().constData());
                if (!encoding)
                    qWarning() << "QDomDocument::save(): Unsupported encoding" << enc << "specified.";
                else
                    s.setEncoding(encoding.value());
            }
        }
#endif
        bool doc = false;

        while (n) {
            if (!doc && !(n->isProcessingInstruction() && n->nodeName() == "xml"_L1)) {
                // save doctype after XML declaration
                type->save(s, 0, indent);
                doc = true;
            }
            n->saveSubTree(n, s, 0, indent);
            n = n->next;
        }
    }
    else {

        // Write out the XML declaration.
        const QByteArray codecName = QStringConverter::nameForEncoding(s.encoding());

        s << "<?xml version=\"1.0\" encoding=\""
          << codecName
          << "\"?>\n";

        //  Skip the first processing instruction by name "xml", if any such exists.
        const QDomNodePrivate* startNode = n;

        // First, we try to find the PI and sets the startNode to the one appearing after it.
        while (n) {
            if (n->isProcessingInstruction() && n->nodeName() == "xml"_L1) {
                startNode = n->next;
                break;
            }
            else
                n = n->next;
        }

        // Now we serialize all the nodes after the faked XML declaration(the PI).
        while (startNode) {
            startNode->saveSubTree(startNode, s, 0, indent);
            startNode = startNode->next;
        }
    }
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  A QDomDocumentPrivate that Python can take functions over in. Every QDomDocumentPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef int (*CuteQDomDocumentPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomDocumentPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomDocumentPrivateCall3)(const void *, const QString *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall4)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall5)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall6)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall7)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomDocumentPrivateCall8)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomDocumentPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(dom)
class CuteQDomDocumentPrivate : public QDomDocumentPrivate {
public:
  using QDomDocumentPrivate::QDomDocumentPrivate;
  CuteQDomDocumentPrivate(const QDomDocumentPrivate & other) : QDomDocumentPrivate(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9cloneNodeEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZNK15QDomNodePrivate8nodeTypeEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate5clearEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12setNodeValueERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12insertBeforeEPS_S0_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11insertAfterEPS_S0_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12replaceChildEPS_S0_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11removeChildEPS_")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11appendChildEPS_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9normalizeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
    return false;
  }

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomDocumentPrivate::cloneNode(bool deep)
  QDomNodePrivate *cloneNode(bool deep) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall0 call = reinterpret_cast<CuteQDomDocumentPrivateCall0>(taken[0]);
      void * given = call(this, deep, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomDocumentPrivate::cloneNode(deep);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNode::NodeType QDomDocumentPrivate::nodeType() const
  QDomNode::NodeType nodeType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall1 call = reinterpret_cast<CuteQDomDocumentPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDomNode::NodeType>(given);
    }
    return QDomDocumentPrivate::nodeType();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomDocumentPrivate::clear()
  void clear() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall2 call = reinterpret_cast<CuteQDomDocumentPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDomDocumentPrivate::clear();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::setNodeValue(const QString &v)
  void setNodeValue(const QString &v) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall3 call = reinterpret_cast<CuteQDomDocumentPrivateCall3>(taken[3]);
      call(this, &v, &handled);
      if (handled) return;
    }
    QDomNodePrivate::setNodeValue(v);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::insertBefore(QDomNodePrivate
  //      *newChild, QDomNodePrivate *refChild)
  QDomNodePrivate *insertBefore(
      QDomNodePrivate *newChild,
      QDomNodePrivate *refChild) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall4 call = reinterpret_cast<CuteQDomDocumentPrivateCall4>(taken[4]);
      void * given = call(this, newChild, refChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::insertBefore(newChild, refChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::insertAfter(QDomNodePrivate
  //      *newChild, QDomNodePrivate *refChild)
  QDomNodePrivate *insertAfter(
      QDomNodePrivate *newChild,
      QDomNodePrivate *refChild) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall5 call = reinterpret_cast<CuteQDomDocumentPrivateCall5>(taken[5]);
      void * given = call(this, newChild, refChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::insertAfter(newChild, refChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::replaceChild(QDomNodePrivate
  //      *newChild, QDomNodePrivate *oldChild)
  QDomNodePrivate *replaceChild(
      QDomNodePrivate *newChild,
      QDomNodePrivate *oldChild) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall6 call = reinterpret_cast<CuteQDomDocumentPrivateCall6>(taken[6]);
      void * given = call(this, newChild, oldChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::replaceChild(newChild, oldChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::removeChild(QDomNodePrivate
  //      *oldChild)
  QDomNodePrivate *removeChild(QDomNodePrivate *oldChild) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall7 call = reinterpret_cast<CuteQDomDocumentPrivateCall7>(taken[7]);
      void * given = call(this, oldChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::removeChild(oldChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::appendChild(QDomNodePrivate
  //      *newChild)
  QDomNodePrivate *appendChild(QDomNodePrivate *newChild) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall8 call = reinterpret_cast<CuteQDomDocumentPrivateCall8>(taken[8]);
      void * given = call(this, newChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::appendChild(newChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::normalize()
  void normalize() override {
    if (taken[9]) {
      int handled = 0;
      CuteQDomDocumentPrivateCall9 call = reinterpret_cast<CuteQDomDocumentPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::normalize();
  }
#endif  // QT_CONFIG(dom)
};

//  QDomDocumentPrivate::~QDomDocumentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDomDocumentPrivateD1Ev(QDomDocumentPrivate *self) {
  delete self;
}

//  QDomDocumentTypePrivate *QDomDocumentPrivate::doctype()
extern "C" Q_DECL_EXPORT
QDomDocumentTypePrivate *ritual_ZN19QDomDocumentPrivate7doctypeEv(
    QDomDocumentPrivate *self) {
  return self->doctype();
}

//  QDomImplementationPrivate *QDomDocumentPrivate::implementation()
extern "C" Q_DECL_EXPORT
QDomImplementationPrivate *ritual_ZN19QDomDocumentPrivate14implementationEv(
    QDomDocumentPrivate *self) {
  return self->implementation();
}

#if QT_CONFIG(dom)
//  QDomElementPrivate *QDomDocumentPrivate::documentElement()
extern "C" Q_DECL_EXPORT
QDomElementPrivate *ritual_ZN19QDomDocumentPrivate15documentElementEv(
    QDomDocumentPrivate *self) {
  return self->documentElement();
}
#endif  // QT_CONFIG(dom)

//  QDomNodePrivate *QDomDocumentPrivate::cloneNode(bool deep)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN19QDomDocumentPrivate9cloneNodeEb(
    QDomDocumentPrivate *self,
    bool deep) {
  return self->cloneNode(deep);
}

//  QDomNode::NodeType QDomDocumentPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK19QDomDocumentPrivate8nodeTypeEv(
    const QDomDocumentPrivate *self) {
  return self->nodeType();
}

//  void QDomDocumentPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDomDocumentPrivate5clearEv(QDomDocumentPrivate *self) {
  self->clear();
}

#if QT_CONFIG(dom)
//  void QDomDocumentPrivate::saveDocument(QTextStream &stream, const int
//      indent, QDomNode::EncodingPolicy encUsed) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QDomDocumentPrivate12saveDocumentER11QTextStreamiN8QDomNode14EncodingPolicyE(
    const QDomDocumentPrivate *self,
    QTextStream *stream,
    int indent,
    QDomNode::EncodingPolicy encUsed) {
  self->saveDocument(*stream, indent, encUsed);
}
#endif  // QT_CONFIG(dom)

//  a Python function taken by a CuteQDomDocumentPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDomDocumentPrivate(
    QDomDocumentPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDomDocumentPrivate *>(self)->take(key, call);
}

//  QDomNode::NodeType QDomDocumentPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_own_ZNK19QDomDocumentPrivate8nodeTypeEv(
    const QDomDocumentPrivate *self) {
  return self->QDomDocumentPrivate::nodeType();
}

#if QT_CONFIG(dom)
//  void QDomDocumentPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QDomDocumentPrivate5clearEv(QDomDocumentPrivate *self) {
  self->QDomDocumentPrivate::clear();
}
#endif  // QT_CONFIG(dom)

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
