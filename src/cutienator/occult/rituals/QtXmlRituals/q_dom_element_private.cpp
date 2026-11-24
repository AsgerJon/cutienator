//  Written by dev_tooling.RitualGenerator from the records of
//  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtXml/qtxmlglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
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
#include <qdom.h>
#include "private/qxmlutils_p.h"
#if QT_CONFIG(dom)
#include "qdom_p.h"
#include "qdomhelpers_p.h"
#include <qatomic.h>
#include <qbuffer.h>
#include <qiodevice.h>
#if QT_CONFIG(regularexpression)
#include <qregularexpression.h>
#endif
#include <qtextstream.h>
#include <qvariant.h>
#include <qshareddata.h>
#include <qdebug.h>
#include <qxmlstream.h>
#include <private/qduplicatetracker_p.h>
#include <private/qstringiterator_p.h>
#include <qvarlengtharray.h>
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

//  from src/xml/dom/qdom.cpp, line 2724, as _ZNK23QDomNamedNodeMapPrivate9namedItemERK7QString
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::namedItem(const QString& name) const
{
    auto it = map.find(name);
    return it == map.end() ? nullptr : it.value();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2730, as _ZNK23QDomNamedNodeMapPrivate11namedItemNSERK7QStringS2_
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::namedItemNS(const QString& nsURI, const QString& localName) const
{
    auto it = map.constBegin();
    QDomNodePrivate *n;
    for (; it != map.constEnd(); ++it) {
        n = it.value();
        if (!n->prefix.isNull()) {
            // node has a namespace
            if (n->namespaceURI == nsURI && n->name == localName)
                return n;
        }
    }
    return nullptr;
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

//  from src/xml/dom/qdom.cpp, line 2745, as _ZN23QDomNamedNodeMapPrivate12setNamedItemEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::setNamedItem(QDomNodePrivate* arg)
{
    if (readonly || !arg)
        return nullptr;

    if (appendToParent)
        return parent->appendChild(arg);

    QDomNodePrivate *n = map.value(arg->nodeName());
    // We take a reference
    arg->ref.ref();
    map.insert(arg->nodeName(), arg);
    return n;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2781, as _ZN23QDomNamedNodeMapPrivate15removeNamedItemERK7QString
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::removeNamedItem(const QString& name)
{
    if (readonly)
        return nullptr;

    QDomNodePrivate* p = namedItem(name);
    if (p == nullptr)
        return nullptr;
    if (appendToParent)
        return parent->removeChild(p);

    map.remove(p->nodeName());
    // We took a reference, so we have to free one here
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2810, as _ZNK23QDomNamedNodeMapPrivate8containsERK7QString
#if QT_CONFIG(dom)
inline bool QDomNamedNodeMapPrivate::contains(const QString& name) const
{
    return map.contains(name);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2815, as _ZNK23QDomNamedNodeMapPrivate10containsNSERK7QStringS2_
#if QT_CONFIG(dom)
inline bool QDomNamedNodeMapPrivate::containsNS(const QString& nsURI, const QString & localName) const
{
    return namedItemNS(nsURI, localName) != nullptr;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2805, as _ZNK23QDomNamedNodeMapPrivate6lengthEv
#if QT_CONFIG(dom)
inline int QDomNamedNodeMapPrivate::length() const
{
    return map.size();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4045, as _ZN18QDomElementPrivateD1Ev
#if QT_CONFIG(dom)
inline QDomElementPrivate::~QDomElementPrivate()
{
    if (!m_attr->ref.deref())
        delete m_attr;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4059, as _ZNK18QDomElementPrivate9attributeERK7QStringS2_
#if QT_CONFIG(dom)
inline QString QDomElementPrivate::attribute(const QString& name_, const QString& defValue) const
{
    QDomNodePrivate* n = m_attr->namedItem(name_);
    if (!n)
        return defValue;

    return n->nodeValue();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4068, as _ZNK18QDomElementPrivate11attributeNSERK7QStringS2_S2_
#if QT_CONFIG(dom)
inline QString QDomElementPrivate::attributeNS(const QString& nsURI, const QString& localName, const QString& defValue) const
{
    QDomNodePrivate* n = m_attr->namedItemNS(nsURI, localName);
    if (!n)
        return defValue;

    return n->nodeValue();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4112, as _ZN18QDomElementPrivate15removeAttributeERK7QString
#if QT_CONFIG(dom)
inline void QDomElementPrivate::removeAttribute(const QString& aname)
{
    QDomNodePrivate* p = m_attr->removeNamedItem(aname);
    if (p && p->ref.loadRelaxed() == 0)
        delete p;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4119, as _ZN18QDomElementPrivate13attributeNodeERK7QString
#if QT_CONFIG(dom)
inline QDomAttrPrivate* QDomElementPrivate::attributeNode(const QString& aname)
{
    return static_cast<QDomAttrPrivate *>(m_attr->namedItem(aname));
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4124, as _ZN18QDomElementPrivate15attributeNodeNSERK7QStringS2_
#if QT_CONFIG(dom)
inline QDomAttrPrivate* QDomElementPrivate::attributeNodeNS(const QString& nsURI, const QString& localName)
{
    return static_cast<QDomAttrPrivate *>(m_attr->namedItemNS(nsURI, localName));
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4129, as _ZN18QDomElementPrivate16setAttributeNodeEP15QDomAttrPrivate
#if QT_CONFIG(dom)
inline QDomAttrPrivate* QDomElementPrivate::setAttributeNode(QDomAttrPrivate* newAttr)
{
    if (!newAttr)
        return nullptr;

    QDomNodePrivate* foundAttr = m_attr->namedItem(newAttr->nodeName());
    if (foundAttr)
        m_attr->removeNamedItem(newAttr->nodeName());

    // Referencing is done by the maps
    m_attr->setNamedItem(newAttr);
    newAttr->setParent(this);

    return static_cast<QDomAttrPrivate *>(foundAttr);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4145, as _ZN18QDomElementPrivate18setAttributeNodeNSEP15QDomAttrPrivate
#if QT_CONFIG(dom)
inline QDomAttrPrivate* QDomElementPrivate::setAttributeNodeNS(QDomAttrPrivate* newAttr)
{
    QDomNodePrivate* n = nullptr;
    if (!newAttr->prefix.isNull())
        n = m_attr->namedItemNS(newAttr->namespaceURI, newAttr->name);

    // Referencing is done by the maps
    m_attr->setNamedItem(newAttr);

    return static_cast<QDomAttrPrivate *>(n);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4157, as _ZN18QDomElementPrivate19removeAttributeNodeEP15QDomAttrPrivate
#if QT_CONFIG(dom)
inline QDomAttrPrivate* QDomElementPrivate::removeAttributeNode(QDomAttrPrivate* oldAttr)
{
    return static_cast<QDomAttrPrivate *>(m_attr->removeNamedItem(oldAttr->nodeName()));
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4162, as _ZNK18QDomElementPrivate12hasAttributeERK7QString
#if QT_CONFIG(dom)
inline bool QDomElementPrivate::hasAttribute(const QString& aname) const
{
    return m_attr->contains(aname);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4167, as _ZNK18QDomElementPrivate14hasAttributeNSERK7QStringS2_
#if QT_CONFIG(dom)
inline bool QDomElementPrivate::hasAttributeNS(const QString& nsURI, const QString& localName) const
{
    return m_attr->containsNS(nsURI, localName);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 4051, as _ZN18QDomElementPrivate9cloneNodeEb
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomElementPrivate::cloneNode(bool deep)
{
    QDomNodePrivate* p = new QDomElementPrivate(this, deep);
    // We are not interested in this node
    p->ref.deref();
    return p;
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  A QDomElementPrivate that Python can take functions over in. Every QDomElementPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dom)
typedef int (*CuteQDomElementPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomElementPrivateCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall3)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall4)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall5)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall6)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomElementPrivateCall7)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomElementPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomElementPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(dom)
class CuteQDomElementPrivate : public QDomElementPrivate {
public:
  using QDomElementPrivate::QDomElementPrivate;
  CuteQDomElementPrivate(const QDomElementPrivate &other) : QDomElementPrivate(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZNK15QDomNodePrivate8nodeTypeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9cloneNodeEb")) {
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
  //  QDomNode::NodeType QDomElementPrivate::nodeType() const
  QDomNode::NodeType nodeType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDomElementPrivateCall0 call = reinterpret_cast<CuteQDomElementPrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDomNode::NodeType>(given);
    }
    return QDomElementPrivate::nodeType();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomElementPrivate::cloneNode(bool deep)
  QDomNodePrivate *cloneNode(bool deep) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDomElementPrivateCall1 call = reinterpret_cast<CuteQDomElementPrivateCall1>(taken[1]);
      void * given = call(this, deep, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomElementPrivate::cloneNode(deep);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::setNodeValue(const QString &v)
  void setNodeValue(const QString &v) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDomElementPrivateCall2 call = reinterpret_cast<CuteQDomElementPrivateCall2>(taken[2]);
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
      CuteQDomElementPrivateCall3 call = reinterpret_cast<CuteQDomElementPrivateCall3>(taken[3]);
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
      CuteQDomElementPrivateCall4 call = reinterpret_cast<CuteQDomElementPrivateCall4>(taken[4]);
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
      CuteQDomElementPrivateCall5 call = reinterpret_cast<CuteQDomElementPrivateCall5>(taken[5]);
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
      CuteQDomElementPrivateCall6 call = reinterpret_cast<CuteQDomElementPrivateCall6>(taken[6]);
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
      CuteQDomElementPrivateCall7 call = reinterpret_cast<CuteQDomElementPrivateCall7>(taken[7]);
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
      CuteQDomElementPrivateCall8 call = reinterpret_cast<CuteQDomElementPrivateCall8>(taken[8]);
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
      CuteQDomElementPrivateCall9 call = reinterpret_cast<CuteQDomElementPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::clear();
  }
#endif  // QT_CONFIG(dom)
};

//  QDomElementPrivate::~QDomElementPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDomElementPrivateD1Ev(QDomElementPrivate *self) {
  delete self;
}

#if QT_CONFIG(dom)
//  QString QDomElementPrivate::attribute(const QString &name, const QString
//      &defValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QDomElementPrivate9attributeERK7QStringS2_(
    const QDomElementPrivate *self,
    const QString *name,
    const QString *defValue) {
  return new QString(self->attribute(*name, *defValue));
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QString QDomElementPrivate::attributeNS(const QString &nsURI, const
//      QString &localName, const QString &defValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QDomElementPrivate11attributeNSERK7QStringS2_S2_(
    const QDomElementPrivate *self,
    const QString *nsURI,
    const QString *localName,
    const QString *defValue) {
  return new QString(self->attributeNS(*nsURI, *localName, *defValue));
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomElementPrivate::removeAttribute(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDomElementPrivate15removeAttributeERK7QString(
    QDomElementPrivate *self,
    const QString *name) {
  self->removeAttribute(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomAttrPrivate *QDomElementPrivate::attributeNode(const QString &name)
extern "C" Q_DECL_EXPORT
QDomAttrPrivate *ritual_ZN18QDomElementPrivate13attributeNodeERK7QString(
    QDomElementPrivate *self,
    const QString *name) {
  return self->attributeNode(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomAttrPrivate *QDomElementPrivate::attributeNodeNS(const QString
//      &nsURI, const QString &localName)
extern "C" Q_DECL_EXPORT
QDomAttrPrivate *ritual_ZN18QDomElementPrivate15attributeNodeNSERK7QStringS2_(
    QDomElementPrivate *self,
    const QString *nsURI,
    const QString *localName) {
  return self->attributeNodeNS(*nsURI, *localName);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomAttrPrivate *QDomElementPrivate::setAttributeNode(QDomAttrPrivate
//      *newAttr)
extern "C" Q_DECL_EXPORT
QDomAttrPrivate *ritual_ZN18QDomElementPrivate16setAttributeNodeEP15QDomAttrPrivate(
    QDomElementPrivate *self,
    QDomAttrPrivate *newAttr) {
  return self->setAttributeNode(newAttr);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomAttrPrivate *QDomElementPrivate::setAttributeNodeNS(QDomAttrPrivate
//      *newAttr)
extern "C" Q_DECL_EXPORT
QDomAttrPrivate *ritual_ZN18QDomElementPrivate18setAttributeNodeNSEP15QDomAttrPrivate(
    QDomElementPrivate *self,
    QDomAttrPrivate *newAttr) {
  return self->setAttributeNodeNS(newAttr);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomAttrPrivate *QDomElementPrivate::removeAttributeNode(QDomAttrPrivate
//      *oldAttr)
extern "C" Q_DECL_EXPORT
QDomAttrPrivate *ritual_ZN18QDomElementPrivate19removeAttributeNodeEP15QDomAttrPrivate(
    QDomElementPrivate *self,
    QDomAttrPrivate *oldAttr) {
  return self->removeAttributeNode(oldAttr);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomElementPrivate::hasAttribute(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomElementPrivate12hasAttributeERK7QString(
    const QDomElementPrivate *self,
    const QString *name) {
  return self->hasAttribute(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomElementPrivate::hasAttributeNS(const QString &nsURI, const
//      QString &localName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomElementPrivate14hasAttributeNSERK7QStringS2_(
    const QDomElementPrivate *self,
    const QString *nsURI,
    const QString *localName) {
  return self->hasAttributeNS(*nsURI, *localName);
}
#endif  // QT_CONFIG(dom)

//  QDomNamedNodeMapPrivate *QDomElementPrivate::attributes()
extern "C" Q_DECL_EXPORT
QDomNamedNodeMapPrivate *ritual_ZN18QDomElementPrivate10attributesEv(
    QDomElementPrivate *self) {
  return self->attributes();
}

#if QT_CONFIG(dom)
//  bool QDomElementPrivate::hasAttributes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDomElementPrivate13hasAttributesEv(
    const QDomElementPrivate *self) {
  return self->hasAttributes();
}
#endif  // QT_CONFIG(dom)

//  QDomNode::NodeType QDomElementPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK18QDomElementPrivate8nodeTypeEv(
    const QDomElementPrivate *self) {
  return self->nodeType();
}

//  QDomNodePrivate *QDomElementPrivate::cloneNode(bool deep)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN18QDomElementPrivate9cloneNodeEb(
    QDomElementPrivate *self,
    bool deep) {
  return self->cloneNode(deep);
}

//  a Python function taken by a CuteQDomElementPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDomElementPrivate(
    QDomElementPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDomElementPrivate *>(self)->take(key, call);
}

//  QDomNode::NodeType QDomElementPrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_own_ZNK18QDomElementPrivate8nodeTypeEv(
    const QDomElementPrivate *self) {
  return self->QDomElementPrivate::nodeType();
}

#endif  // QT_CONFIG(dom)
