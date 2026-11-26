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

//  from src/xml/dom/qdom.cpp, line 3785, as local:qdom.cpp:encodeText
#if QT_CONFIG(dom)
static QString encodeText(const QString &str,
                          const bool encodeQuotes = true,
                          const bool performAVN = false,
                          const bool encodeEOLs = false)
{
    QString retval;
    qsizetype start = 0;
    auto appendToOutput = [&](qsizetype cur, const auto &replacement)
    {
        if (start < cur) {
            retval.reserve(str.size() + replacement.size());
            retval.append(QStringView(str).first(cur).sliced(start));
        }
        // Skip over str[cur], replaced by replacement
        start = cur + 1;
        retval.append(replacement);
    };

    const qsizetype len = str.size();
    for (qsizetype cur = 0; cur < len; ++cur) {
        switch (str[cur].unicode()) {
            case u'<':
                appendToOutput(cur, "&lt;"_L1);
                break;
            case u'"':
                if (encodeQuotes)
                    appendToOutput(cur, "&quot;"_L1);
                break;
            case u'&':
                appendToOutput(cur, "&amp;"_L1);
                break;
            case u'>':
                if (cur >= 2 && str[cur - 1] == u']' && str[cur - 2] == u']')
                    appendToOutput(cur, "&gt;"_L1);
                break;
            case u'\r':
                if (performAVN || encodeEOLs)
                    appendToOutput(cur, "&#xd;"_L1);    // \r == 0x0d
                break;
            case u'\n':
                if (performAVN)
                    appendToOutput(cur, "&#xa;"_L1);    // \n == 0x0a
                break;
            case u'\t':
                if (performAVN)
                    appendToOutput(cur, "&#x9;"_L1);    // \t == 0x09
                break;
            default:
                break;
        }
    }
    if (start > 0) {
        retval.append(QStringView(str).first(len).sliced(start));
        return retval;
    }
    return str;
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

//  from src/xml/dom/qdom.cpp, line 1502, as _ZN15QDomNodePrivate9normalizeEv
#if QT_CONFIG(dom)
inline void QDomNodePrivate::normalize()
{
    // ### This one has moved from QDomElementPrivate to this position. It is
    // not tested.
    qNormalizeNode(this);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1088, as _ZN15QDomNodePrivateD2Ev
#if QT_CONFIG(dom)
inline QDomNodePrivate::~QDomNodePrivate()
{
    QDomNodePrivate *p = this;

    // post-order depth-first-search; visitation is deletion (avoids recursion)
    while (true) {
        if (QDomNodePrivate *c = p->first) {
            p->first = c->next;          // peel firstChild off p
            if (c->ref.deref())
                c->setNoParent();        // survivor: detach, don't descend
            else
                p = c;                   // descend; c's parent() remembers p
        } else {                         // p ran out of children (= is a leaf now)
            if (p == this)
                break;                   // we're done, don't `delete this`
            delete std::exchange(p, p->parent());  // deletes and ascends
        }
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4855, as _ZN15QDomTextPrivateC2EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomTextPrivate::QDomTextPrivate(QDomDocumentPrivate* d, QDomNodePrivate* parent, const QString& val)
    : QDomCharacterDataPrivate(d, parent, val)
{
    name = u"#text"_s;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5113, as _ZN23QDomCDATASectionPrivate9cloneNodeEb
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomCDATASectionPrivate::cloneNode(bool deep)
{
    QDomNodePrivate* p = new QDomCDATASectionPrivate(this, deep);
    // We are not interested in this node
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 5121, as _ZNK23QDomCDATASectionPrivate4saveER11QTextStreamii
#if QT_CONFIG(dom)
inline void QDomCDATASectionPrivate::save(QTextStream& s, int, int) const
{
    // ### How do we escape "]]>" ?
    // "]]>" is not allowed; so there should be none in value anyway
    s << "<![CDATA[" << value << "]]>";
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4861, as _ZN15QDomTextPrivateC2EPS_b
#if QT_CONFIG(dom)
inline QDomTextPrivate::QDomTextPrivate(QDomTextPrivate* n, bool deep)
    : QDomCharacterDataPrivate(n, deep)
{
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

//  from src/xml/dom/qdom.cpp, line 1472, as _ZN15QDomNodePrivate9cloneNodeEb
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::cloneNode(bool deep)
{
    QDomNodePrivate* p = new QDomNodePrivate(this, deep);
    // We are not interested in this node
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 3556, as _ZN24QDomCharacterDataPrivate10appendDataERK7QString
#if QT_CONFIG(dom)
inline void QDomCharacterDataPrivate::appendData(const QString& arg)
{
    value += arg;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 3510, as _ZN24QDomCharacterDataPrivateC2EP19QDomDocumentPrivateP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomCharacterDataPrivate::QDomCharacterDataPrivate(QDomDocumentPrivate* d, QDomNodePrivate* p,
                                                      const QString& data)
    : QDomNodePrivate(d, p)
{
    value = data;
    name = u"#character-data"_s;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 3518, as _ZN24QDomCharacterDataPrivateC2EPS_b
#if QT_CONFIG(dom)
inline QDomCharacterDataPrivate::QDomCharacterDataPrivate(QDomCharacterDataPrivate* n, bool deep)
    : QDomNodePrivate(n, deep)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4866, as _ZN15QDomTextPrivate9cloneNodeEb
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomTextPrivate::cloneNode(bool deep)
{
    QDomNodePrivate* p = new QDomTextPrivate(this, deep);
    // We are not interested in this node
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4893, as _ZNK15QDomTextPrivate4saveER11QTextStreamii
#if QT_CONFIG(dom)
inline void QDomTextPrivate::save(QTextStream& s, int, int) const
{
    QDomTextPrivate *that = const_cast<QDomTextPrivate*>(this);
    s << encodeText(value, !(that->parent() && that->parent()->isElement()), false, true);
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  A QDomCDATASectionPrivate that Python can take functions over in. Every QDomCDATASectionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef int (*CuteQDomCDATASectionPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomCDATASectionPrivateCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall3)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall4)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall5)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall6)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomCDATASectionPrivateCall7)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomCDATASectionPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomCDATASectionPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(dom)
class CuteQDomCDATASectionPrivate : public QDomCDATASectionPrivate {
public:
  using QDomCDATASectionPrivate::QDomCDATASectionPrivate;
  CuteQDomCDATASectionPrivate(const QDomCDATASectionPrivate & other) : QDomCDATASectionPrivate(other) {}
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
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12setNodeValueERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12insertBeforeEPS_S0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11insertAfterEPS_S0_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12replaceChildEPS_S0_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11removeChildEPS_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11appendChildEPS_")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9normalizeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate5clearEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
    return false;
  }

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomCDATASectionPrivate::cloneNode(bool deep)
  QDomNodePrivate *cloneNode(bool deep) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall0 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall0>(taken[0]);
      void * given = call(this, deep, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomCDATASectionPrivate::cloneNode(deep);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNode::NodeType QDomCDATASectionPrivate::nodeType() const
  QDomNode::NodeType nodeType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall1 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDomNode::NodeType>(given);
    }
    return QDomCDATASectionPrivate::nodeType();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::setNodeValue(const QString &v)
  void setNodeValue(const QString &v) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall2 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall3 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall4 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall5 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall6 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall7 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall7>(taken[7]);
      void * given = call(this, newChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::appendChild(newChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::normalize()
  void normalize() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall8 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::normalize();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::clear()
  void clear() override {
    if (taken[9]) {
      int handled = 0;
      CuteQDomCDATASectionPrivateCall9 call = reinterpret_cast<CuteQDomCDATASectionPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::clear();
  }
#endif  // QT_CONFIG(dom)
};

//  QDomNodePrivate *QDomCDATASectionPrivate::cloneNode(bool deep)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN23QDomCDATASectionPrivate9cloneNodeEb(
    QDomCDATASectionPrivate *self,
    bool deep) {
  return self->cloneNode(deep);
}

//  QDomNode::NodeType QDomCDATASectionPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK23QDomCDATASectionPrivate8nodeTypeEv(
    const QDomCDATASectionPrivate *self) {
  return self->nodeType();
}

//  void QDomCDATASectionPrivate::save(QTextStream &s, int a1, int a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QDomCDATASectionPrivate4saveER11QTextStreamii(
    const QDomCDATASectionPrivate *self,
    QTextStream *s,
    int a1,
    int a2) {
  self->save(*s, a1, a2);
}

//  QDomCDATASectionPrivate::~QDomCDATASectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDomCDATASectionPrivateD1Ev(QDomCDATASectionPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQDomCDATASectionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDomCDATASectionPrivate(
    QDomCDATASectionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDomCDATASectionPrivate *>(self)->take(key, call);
}

//  QDomNode::NodeType QDomCDATASectionPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_own_ZNK23QDomCDATASectionPrivate8nodeTypeEv(
    const QDomCDATASectionPrivate *self) {
  return self->QDomCDATASectionPrivate::nodeType();
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
