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

//  from src/xml/dom/qdom.cpp, line 757, as _ZNK19QDomNodeListPrivate11forEachNodeEN3qxp12function_refIJFvP15QDomNodePrivateEEEE
#if QT_CONFIG(dom)
inline void QDomNodeListPrivate::forEachNode(qxp::function_ref<void(QDomNodePrivate*)> yield) const
{
    if (!node_impl)
        return;

    QDomNodePrivate *current = findNextInOrder(node_impl);
    while (current && current != node_impl) {
        yield(current);
        current = findNextInOrder(current);
    }
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 609, as _ZN19QDomNodeListPrivateC1EP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *n_impl) : ref(1)
{
    node_impl = n_impl;
    if (node_impl)
        node_impl->ref.ref();
    timestamp = 0;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 617, as _ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QString
#if QT_CONFIG(dom)
inline QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *n_impl, const QString &name) :
    ref(1)
{
    node_impl = n_impl;
    if (node_impl)
        node_impl->ref.ref();
    tagname = name;
    timestamp = 0;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 627, as _ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QStringS4_
#if QT_CONFIG(dom)
inline QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *n_impl, const QString &_nsURI, const QString &localName) :
    ref(1)
{
    node_impl = n_impl;
    if (node_impl)
        node_impl->ref.ref();
    tagname = localName;
    nsURI = _nsURI;
    timestamp = 0;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 638, as _ZN19QDomNodeListPrivateD1Ev
#if QT_CONFIG(dom)
inline QDomNodeListPrivate::~QDomNodeListPrivate()
{
    if (node_impl && !node_impl->ref.deref())
        delete node_impl;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 649, as _ZNK19QDomNodeListPrivate10createListEv
#if QT_CONFIG(dom)
inline void QDomNodeListPrivate::createList() const
{
    if (!node_impl)
        return;

    list.clear();
    const QDomDocumentPrivate *const doc = node_impl->ownerDocument();
    if (doc && timestamp != doc->nodeListTime)
        timestamp = doc->nodeListTime;
    forEachNode([&](QDomNodePrivate *p){ list.append(p); });
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 666, as _ZNK19QDomNodeListPrivate9checkNodeEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline bool QDomNodeListPrivate::checkNode(QDomNodePrivate *p) const
{
    return p && p->isElement() && (nsURI.isNull()
                                   ? p->nodeName() == tagname
                                   : p->name == tagname && p->namespaceURI == nsURI);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 682, as _ZNK19QDomNodeListPrivate15findNextInOrderEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNodePrivate *QDomNodeListPrivate::findNextInOrder(QDomNodePrivate *p) const
{
    if (!p)
        return p;

    if (tagname.isNull()) {
        if (p == node_impl)
            return p->first;
        else if (p && p->next)
            return p->next;
    }

    if (p == node_impl) {
        p = p->first;
        if (checkNode(p))
            return p;
    }
    while (p && p != node_impl) {
        if (p->first) { // go down in the tree
            p = p->first;
        } else if (p->next) { // traverse the tree
            p = p->next;
        } else { // go up in the tree
            p = p->parent();
            while (p && p != node_impl && !p->next)
                p = p->parent();
            if (p && p != node_impl)
                p = p->next;
        }
        if (checkNode(p))
            return p;
    }
    return node_impl;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 723, as _ZNK19QDomNodeListPrivate15findPrevInOrderEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNodePrivate *QDomNodeListPrivate::findPrevInOrder(QDomNodePrivate *p) const
{
    if (!p)
        return p;

    if (tagname.isNull() && p == node_impl)
        return p->last;
    if (tagname.isNull())
        return p->prev;

    // We end all the way down in the tree
    // so that is where we have to start
    if (p == node_impl) {
        while (p->last)
            p = p->last;
        if (checkNode(p))
            return p;
    }

    while (p) {
        if (p->prev) {// traverse the tree backwards
            p = p->prev;
            // go mmediately down if an item has children
            while (p->last)
                p = p->last;
        } else { // go up in the tree
            p = p->parent();
        }
        if (checkNode(p))
            return p;
    }
    return node_impl;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 769, as _ZNK19QDomNodeListPrivate15maybeCreateListEv
#if QT_CONFIG(dom)
inline bool QDomNodeListPrivate::maybeCreateList() const
{
    if (!node_impl)
        return false;

    const QDomDocumentPrivate *const doc = node_impl->ownerDocument();
    if (!doc || timestamp != doc->nodeListTime)
        createList();

    return true;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 781, as _ZN19QDomNodeListPrivate4itemEi
#if QT_CONFIG(dom)
inline QDomNodePrivate *QDomNodeListPrivate::item(int index)
{
    if (!maybeCreateList() || index >= list.size() || index < 0)
        return nullptr;

    return list.at(index);
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 789, as _ZNK19QDomNodeListPrivate6lengthEv
#if QT_CONFIG(dom)
inline int QDomNodeListPrivate::length() const
{
    if (!maybeCreateList())
        return 0;

    return list.size();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 797, as _ZNK19QDomNodeListPrivate14noexceptLengthEv
#if QT_CONFIG(dom)
inline int QDomNodeListPrivate::noexceptLength() const noexcept
{
    int count = 0;
    forEachNode([&](QDomNodePrivate*){ ++count; });
    return count;
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNodeListPrivate *ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivate(
    QDomNodePrivate *a0) {
  return new QDomNodeListPrivate(a0);
}

//  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
//      QString &a1)
extern "C" Q_DECL_EXPORT
QDomNodeListPrivate *ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QString(
    QDomNodePrivate *a0,
    const QString *a1) {
  return new QDomNodeListPrivate(a0, *a1);
}

//  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
//      QString &a1, const QString &a2)
extern "C" Q_DECL_EXPORT
QDomNodeListPrivate *ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QStringS4_(
    QDomNodePrivate *a0,
    const QString *a1,
    const QString *a2) {
  return new QDomNodeListPrivate(a0, *a1, *a2);
}

//  QDomNodeListPrivate::~QDomNodeListPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDomNodeListPrivateD1Ev(QDomNodeListPrivate *self) {
  delete self;
}

#if QT_CONFIG(dom)
//  void QDomNodeListPrivate::createList() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QDomNodeListPrivate10createListEv(
    const QDomNodeListPrivate *self) {
  self->createList();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomNodeListPrivate::checkNode(QDomNodePrivate *p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDomNodeListPrivate9checkNodeEP15QDomNodePrivate(
    const QDomNodeListPrivate *self,
    QDomNodePrivate *p) {
  return self->checkNode(p);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodeListPrivate::findNextInOrder(QDomNodePrivate *p)
//      const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK19QDomNodeListPrivate15findNextInOrderEP15QDomNodePrivate(
    const QDomNodeListPrivate *self,
    QDomNodePrivate *p) {
  return self->findNextInOrder(p);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodeListPrivate::findPrevInOrder(QDomNodePrivate *p)
//      const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK19QDomNodeListPrivate15findPrevInOrderEP15QDomNodePrivate(
    const QDomNodeListPrivate *self,
    QDomNodePrivate *p) {
  return self->findPrevInOrder(p);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomNodeListPrivate::maybeCreateList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDomNodeListPrivate15maybeCreateListEv(
    const QDomNodeListPrivate *self) {
  return self->maybeCreateList();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodeListPrivate::item(int index)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN19QDomNodeListPrivate4itemEi(
    QDomNodeListPrivate *self,
    int index) {
  return self->item(index);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  int QDomNodeListPrivate::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDomNodeListPrivate6lengthEv(
    const QDomNodeListPrivate *self) {
  return self->length();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  int QDomNodeListPrivate::noexceptLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDomNodeListPrivate14noexceptLengthEv(
    const QDomNodeListPrivate *self) {
  return self->noexceptLength();
}
#endif  // QT_CONFIG(dom)

#endif  // QT_CONFIG(dom)
