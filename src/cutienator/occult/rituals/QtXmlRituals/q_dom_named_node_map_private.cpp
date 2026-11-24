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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/xml/dom/qdom.cpp, line 2681, as _ZN23QDomNamedNodeMapPrivateC1EP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNamedNodeMapPrivate::QDomNamedNodeMapPrivate(QDomNodePrivate *pimpl)
    : ref(1)
    , parent(pimpl)
    , readonly(false)
    , appendToParent(false)
{
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2689, as _ZN23QDomNamedNodeMapPrivateD1Ev
#if QT_CONFIG(dom)
inline QDomNamedNodeMapPrivate::~QDomNamedNodeMapPrivate()
{
    clearMap();
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

//  from src/xml/dom/qdom.cpp, line 2760, as _ZN23QDomNamedNodeMapPrivate14setNamedItemNSEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::setNamedItemNS(QDomNodePrivate* arg)
{
    if (readonly || !arg)
        return nullptr;

    if (appendToParent)
        return parent->appendChild(arg);

    if (!arg->prefix.isNull()) {
        // node has a namespace
        QDomNodePrivate *n = namedItemNS(arg->namespaceURI, arg->name);
        // We take a reference
        arg->ref.ref();
        map.insert(arg->nodeName(), arg);
        return n;
    } else {
        // ### check the following code if it is ok
        return setNamedItem(arg);
    }
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

//  from src/xml/dom/qdom.cpp, line 2798, as _ZNK23QDomNamedNodeMapPrivate4itemEi
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNamedNodeMapPrivate::item(int index) const
{
    if (index >= length() || index < 0)
        return nullptr;
    return std::next(map.begin(), index).value();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2805, as _ZNK23QDomNamedNodeMapPrivate6lengthEv
#if QT_CONFIG(dom)
inline int QDomNamedNodeMapPrivate::length() const
{
    return map.size();
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

//  from src/xml/dom/qdom.cpp, line 2712, as _ZN23QDomNamedNodeMapPrivate8clearMapEv
#if QT_CONFIG(dom)
inline void QDomNamedNodeMapPrivate::clearMap()
{
    // Dereference all of our children if we took references
    if (!appendToParent) {
        auto it = map.constBegin();
        for (; it != map.constEnd(); ++it)
            if (!it.value()->ref.deref())
                delete it.value();
    }
    map.clear();
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 2694, as _ZN23QDomNamedNodeMapPrivate5cloneEP15QDomNodePrivate
#if QT_CONFIG(dom)
inline QDomNamedNodeMapPrivate* QDomNamedNodeMapPrivate::clone(QDomNodePrivate *pimpl)
{
    std::unique_ptr<QDomNamedNodeMapPrivate> m(new QDomNamedNodeMapPrivate(pimpl));
    m->readonly = readonly;
    m->appendToParent = appendToParent;

    auto it = map.constBegin();
    for (; it != map.constEnd(); ++it) {
        QDomNodePrivate *new_node = it.value()->cloneNode();
        new_node->setParent(pimpl);
        m->setNamedItem(new_node);
    }

    // we are no longer interested in ownership
    m->ref.deref();
    return m.release();
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  QDomNamedNodeMapPrivate::QDomNamedNodeMapPrivate(QDomNodePrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNamedNodeMapPrivate *ritual_ZN23QDomNamedNodeMapPrivateC1EP15QDomNodePrivate(
    QDomNodePrivate *a0) {
  return new QDomNamedNodeMapPrivate(a0);
}

#if QT_CONFIG(dom)
//  QDomNamedNodeMapPrivate::~QDomNamedNodeMapPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDomNamedNodeMapPrivateD1Ev(QDomNamedNodeMapPrivate *self) {
  delete self;
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::namedItem(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK23QDomNamedNodeMapPrivate9namedItemERK7QString(
    const QDomNamedNodeMapPrivate *self,
    const QString *name) {
  return self->namedItem(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::namedItemNS(const QString
//      &nsURI, const QString &localName) const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK23QDomNamedNodeMapPrivate11namedItemNSERK7QStringS2_(
    const QDomNamedNodeMapPrivate *self,
    const QString *nsURI,
    const QString *localName) {
  return self->namedItemNS(*nsURI, *localName);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::setNamedItem(QDomNodePrivate
//      *arg)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN23QDomNamedNodeMapPrivate12setNamedItemEP15QDomNodePrivate(
    QDomNamedNodeMapPrivate *self,
    QDomNodePrivate *arg) {
  return self->setNamedItem(arg);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::setNamedItemNS(QDomNodePrivate
//      *arg)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN23QDomNamedNodeMapPrivate14setNamedItemNSEP15QDomNodePrivate(
    QDomNamedNodeMapPrivate *self,
    QDomNodePrivate *arg) {
  return self->setNamedItemNS(arg);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::removeNamedItem(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN23QDomNamedNodeMapPrivate15removeNamedItemERK7QString(
    QDomNamedNodeMapPrivate *self,
    const QString *name) {
  return self->removeNamedItem(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNamedNodeMapPrivate::item(int index) const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK23QDomNamedNodeMapPrivate4itemEi(
    const QDomNamedNodeMapPrivate *self,
    int index) {
  return self->item(index);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  int QDomNamedNodeMapPrivate::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QDomNamedNodeMapPrivate6lengthEv(
    const QDomNamedNodeMapPrivate *self) {
  return self->length();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomNamedNodeMapPrivate::contains(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QDomNamedNodeMapPrivate8containsERK7QString(
    const QDomNamedNodeMapPrivate *self,
    const QString *name) {
  return self->contains(*name);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  bool QDomNamedNodeMapPrivate::containsNS(const QString &nsURI, const
//      QString &localName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QDomNamedNodeMapPrivate10containsNSERK7QStringS2_(
    const QDomNamedNodeMapPrivate *self,
    const QString *nsURI,
    const QString *localName) {
  return self->containsNS(*nsURI, *localName);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomNamedNodeMapPrivate::clearMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDomNamedNodeMapPrivate8clearMapEv(
    QDomNamedNodeMapPrivate *self) {
  self->clearMap();
}
#endif  // QT_CONFIG(dom)

//  bool QDomNamedNodeMapPrivate::isReadOnly()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDomNamedNodeMapPrivate10isReadOnlyEv(
    QDomNamedNodeMapPrivate *self) {
  return self->isReadOnly();
}

//  void QDomNamedNodeMapPrivate::setReadOnly(bool r)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDomNamedNodeMapPrivate11setReadOnlyEb(
    QDomNamedNodeMapPrivate *self,
    bool r) {
  self->setReadOnly(r);
}

//  bool QDomNamedNodeMapPrivate::isAppendToParent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDomNamedNodeMapPrivate16isAppendToParentEv(
    QDomNamedNodeMapPrivate *self) {
  return self->isAppendToParent();
}

//  void QDomNamedNodeMapPrivate::setAppendToParent(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDomNamedNodeMapPrivate17setAppendToParentEb(
    QDomNamedNodeMapPrivate *self,
    bool b) {
  self->setAppendToParent(b);
}

#if QT_CONFIG(dom)
//  QDomNamedNodeMapPrivate *QDomNamedNodeMapPrivate::clone(QDomNodePrivate
//      *parent)
extern "C" Q_DECL_EXPORT
QDomNamedNodeMapPrivate *ritual_ZN23QDomNamedNodeMapPrivate5cloneEP15QDomNodePrivate(
    QDomNamedNodeMapPrivate *self,
    QDomNodePrivate *parent) {
  return self->clone(parent);
}
#endif  // QT_CONFIG(dom)

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
