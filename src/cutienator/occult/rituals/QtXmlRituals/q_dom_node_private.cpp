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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from src/xml/dom/qdom.cpp, line 3556, as _ZN24QDomCharacterDataPrivate10appendDataERK7QString
#if QT_CONFIG(dom)
inline void QDomCharacterDataPrivate::appendData(const QString& arg)
{
    value += arg;
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

//  from src/xml/dom/qdom.cpp, line 1044, as _ZN15QDomNodePrivate16setOwnerDocumentEP19QDomDocumentPrivate
#if QT_CONFIG(dom)
inline void QDomNodePrivate::setOwnerDocument(QDomDocumentPrivate *doc)
{
    ownerNode = doc;
    hasParent = false;
}
#endif  // QT_CONFIG(dom)

//  from src/xml/dom/qdom.cpp, line 1123, as _ZN15QDomNodePrivate9namedItemERK7QString
#if QT_CONFIG(dom)
inline QDomNodePrivate* QDomNodePrivate::namedItem(const QString &n)
{
    QDomNodePrivate* p = first;
    while (p) {
        if (p->nodeName() == n)
            return p;
        p = p->next;
    }
    return nullptr;
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

//  from src/xml/dom/qdom.cpp, line 1545, as _ZN15QDomNodePrivate11setLocationEii
#if QT_CONFIG(dom)
inline void QDomNodePrivate::setLocation(int lineNumber, int columnNumber)
{
    this->lineNumber = lineNumber;
    this->columnNumber = columnNumber;
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  A QDomNodePrivate that Python can take functions over in. Every QDomNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dom)
typedef void (*CuteQDomNodePrivateCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall1)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall2)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall3)(const void *, QDomNodePrivate *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall4)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall5)(const void *, QDomNodePrivate *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void * (*CuteQDomNodePrivateCall6)(const void *, bool, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomNodePrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef void (*CuteQDomNodePrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
typedef int (*CuteQDomNodePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(dom)
class CuteQDomNodePrivate : public QDomNodePrivate {
public:
  using QDomNodePrivate::QDomNodePrivate;
  CuteQDomNodePrivate(const QDomNodePrivate & other) : QDomNodePrivate(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12setNodeValueERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12insertBeforeEPS_S0_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11insertAfterEPS_S0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate12replaceChildEPS_S0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11removeChildEPS_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate11appendChildEPS_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9cloneNodeEb")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate9normalizeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZN15QDomNodePrivate5clearEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
#if QT_CONFIG(dom)
    if (!std::strcmp(key, "_ZNK15QDomNodePrivate8nodeTypeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dom)
    return false;
  }

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::setNodeValue(const QString &v)
  void setNodeValue(const QString &v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDomNodePrivateCall0 call = reinterpret_cast<CuteQDomNodePrivateCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQDomNodePrivateCall1 call = reinterpret_cast<CuteQDomNodePrivateCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQDomNodePrivateCall2 call = reinterpret_cast<CuteQDomNodePrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQDomNodePrivateCall3 call = reinterpret_cast<CuteQDomNodePrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQDomNodePrivateCall4 call = reinterpret_cast<CuteQDomNodePrivateCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDomNodePrivateCall5 call = reinterpret_cast<CuteQDomNodePrivateCall5>(taken[5]);
      void * given = call(this, newChild, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::appendChild(newChild);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNodePrivate *QDomNodePrivate::cloneNode(bool deep)
  QDomNodePrivate *cloneNode(bool deep) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDomNodePrivateCall6 call = reinterpret_cast<CuteQDomNodePrivateCall6>(taken[6]);
      void * given = call(this, deep, &handled);
      if (handled) return static_cast<QDomNodePrivate *>(given);
    }
    return QDomNodePrivate::cloneNode(deep);
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::normalize()
  void normalize() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDomNodePrivateCall7 call = reinterpret_cast<CuteQDomNodePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::normalize();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  void QDomNodePrivate::clear()
  void clear() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDomNodePrivateCall8 call = reinterpret_cast<CuteQDomNodePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDomNodePrivate::clear();
  }
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
  //  QDomNode::NodeType QDomNodePrivate::nodeType() const
  QDomNode::NodeType nodeType() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDomNodePrivateCall9 call = reinterpret_cast<CuteQDomNodePrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDomNode::NodeType>(given);
    }
    return QDomNodePrivate::nodeType();
  }
#endif  // QT_CONFIG(dom)
};

//  QDomNodePrivate::~QDomNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivateD1Ev(QDomNodePrivate *self) {
  delete self;
}

//  QString QDomNodePrivate::nodeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDomNodePrivate8nodeNameEv(
    const QDomNodePrivate *self) {
  return new QString(self->nodeName());
}

//  QString QDomNodePrivate::nodeValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDomNodePrivate9nodeValueEv(
    const QDomNodePrivate *self) {
  return new QString(self->nodeValue());
}

//  void QDomNodePrivate::setNodeValue(const QString &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate12setNodeValueERK7QString(
    QDomNodePrivate *self,
    const QString *v) {
  self->setNodeValue(*v);
}

#if QT_CONFIG(dom)
//  QDomDocumentPrivate *QDomNodePrivate::ownerDocument()
extern "C" Q_DECL_EXPORT
QDomDocumentPrivate *ritual_ZN15QDomNodePrivate13ownerDocumentEv(
    QDomNodePrivate *self) {
  return self->ownerDocument();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomNodePrivate::setOwnerDocument(QDomDocumentPrivate *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate16setOwnerDocumentEP19QDomDocumentPrivate(
    QDomNodePrivate *self,
    QDomDocumentPrivate *doc) {
  self->setOwnerDocument(doc);
}
#endif  // QT_CONFIG(dom)

//  QDomNodePrivate *QDomNodePrivate::insertBefore(QDomNodePrivate *newChild,
//      QDomNodePrivate *refChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate12insertBeforeEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *refChild) {
  return self->insertBefore(newChild, refChild);
}

//  QDomNodePrivate *QDomNodePrivate::insertAfter(QDomNodePrivate *newChild,
//      QDomNodePrivate *refChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate11insertAfterEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *refChild) {
  return self->insertAfter(newChild, refChild);
}

//  QDomNodePrivate *QDomNodePrivate::replaceChild(QDomNodePrivate *newChild,
//      QDomNodePrivate *oldChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate12replaceChildEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *oldChild) {
  return self->replaceChild(newChild, oldChild);
}

//  QDomNodePrivate *QDomNodePrivate::removeChild(QDomNodePrivate *oldChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate11removeChildEPS_(
    QDomNodePrivate *self,
    QDomNodePrivate *oldChild) {
  return self->removeChild(oldChild);
}

//  QDomNodePrivate *QDomNodePrivate::appendChild(QDomNodePrivate *newChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate11appendChildEPS_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild) {
  return self->appendChild(newChild);
}

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::namedItem(const QString &name)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate9namedItemERK7QString(
    QDomNodePrivate *self,
    const QString *name) {
  return self->namedItem(*name);
}
#endif  // QT_CONFIG(dom)

//  QDomNodePrivate *QDomNodePrivate::cloneNode(bool deep)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZN15QDomNodePrivate9cloneNodeEb(
    QDomNodePrivate *self,
    bool deep) {
  return self->cloneNode(deep);
}

//  void QDomNodePrivate::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate9normalizeEv(QDomNodePrivate *self) {
  self->normalize();
}

//  void QDomNodePrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate5clearEv(QDomNodePrivate *self) {
  self->clear();
}

//  QDomNodePrivate *QDomNodePrivate::parent() const
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_ZNK15QDomNodePrivate6parentEv(
    const QDomNodePrivate *self) {
  return self->parent();
}

//  void QDomNodePrivate::setParent(QDomNodePrivate *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate9setParentEPS_(
    QDomNodePrivate *self,
    QDomNodePrivate *p) {
  self->setParent(p);
}

#if QT_CONFIG(dom)
//  void QDomNodePrivate::setNoParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate11setNoParentEv(QDomNodePrivate *self) {
  self->setNoParent();
}
#endif  // QT_CONFIG(dom)

//  bool QDomNodePrivate::isAttr() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate6isAttrEv(const QDomNodePrivate *self) {
  return self->isAttr();
}

//  bool QDomNodePrivate::isCDATASection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate14isCDATASectionEv(
    const QDomNodePrivate *self) {
  return self->isCDATASection();
}

//  bool QDomNodePrivate::isDocumentFragment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate18isDocumentFragmentEv(
    const QDomNodePrivate *self) {
  return self->isDocumentFragment();
}

//  bool QDomNodePrivate::isDocument() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate10isDocumentEv(const QDomNodePrivate *self) {
  return self->isDocument();
}

//  bool QDomNodePrivate::isDocumentType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate14isDocumentTypeEv(
    const QDomNodePrivate *self) {
  return self->isDocumentType();
}

//  bool QDomNodePrivate::isElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate9isElementEv(const QDomNodePrivate *self) {
  return self->isElement();
}

//  bool QDomNodePrivate::isEntityReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate17isEntityReferenceEv(
    const QDomNodePrivate *self) {
  return self->isEntityReference();
}

//  bool QDomNodePrivate::isText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate6isTextEv(const QDomNodePrivate *self) {
  return self->isText();
}

//  bool QDomNodePrivate::isEntity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate8isEntityEv(const QDomNodePrivate *self) {
  return self->isEntity();
}

//  bool QDomNodePrivate::isNotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate10isNotationEv(const QDomNodePrivate *self) {
  return self->isNotation();
}

//  bool QDomNodePrivate::isProcessingInstruction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate23isProcessingInstructionEv(
    const QDomNodePrivate *self) {
  return self->isProcessingInstruction();
}

//  bool QDomNodePrivate::isCharacterData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate15isCharacterDataEv(
    const QDomNodePrivate *self) {
  return self->isCharacterData();
}

//  bool QDomNodePrivate::isComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDomNodePrivate9isCommentEv(const QDomNodePrivate *self) {
  return self->isComment();
}

//  QDomNode::NodeType QDomNodePrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK15QDomNodePrivate8nodeTypeEv(
    const QDomNodePrivate *self) {
  return self->nodeType();
}

#if QT_CONFIG(dom)
//  void QDomNodePrivate::saveSubTree(const QDomNodePrivate *n, QTextStream
//      &s, int depth, int indent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QDomNodePrivate11saveSubTreeEPKS_R11QTextStreamii(
    const QDomNodePrivate *self,
    const QDomNodePrivate *n,
    QTextStream *s,
    int depth,
    int indent) {
  self->saveSubTree(n, *s, depth, indent);
}
#endif  // QT_CONFIG(dom)

//  void QDomNodePrivate::save(QTextStream &a0, int a1, int a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QDomNodePrivate4saveER11QTextStreamii(
    const QDomNodePrivate *self,
    QTextStream *a0,
    int a1,
    int a2) {
  self->save(*a0, a1, a2);
}

//  void QDomNodePrivate::afterSave(QTextStream &a0, int a1, int a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QDomNodePrivate9afterSaveER11QTextStreamii(
    const QDomNodePrivate *self,
    QTextStream *a0,
    int a1,
    int a2) {
  self->afterSave(*a0, a1, a2);
}

#if QT_CONFIG(dom)
//  void QDomNodePrivate::setLocation(int lineNumber, int columnNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDomNodePrivate11setLocationEii(
    QDomNodePrivate *self,
    int lineNumber,
    int columnNumber) {
  self->setLocation(lineNumber, columnNumber);
}
#endif  // QT_CONFIG(dom)

//  a Python function taken by a CuteQDomNodePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDomNodePrivate(
    QDomNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDomNodePrivate *>(self)->take(key, call);
}

//  void QDomNodePrivate::setNodeValue(const QString &v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QDomNodePrivate12setNodeValueERK7QString(
    QDomNodePrivate *self,
    const QString *v) {
  self->QDomNodePrivate::setNodeValue(*v);
}

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::insertBefore(QDomNodePrivate *newChild,
//      QDomNodePrivate *refChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_own_ZN15QDomNodePrivate12insertBeforeEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *refChild) {
  return self->QDomNodePrivate::insertBefore(newChild, refChild);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::insertAfter(QDomNodePrivate *newChild,
//      QDomNodePrivate *refChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_own_ZN15QDomNodePrivate11insertAfterEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *refChild) {
  return self->QDomNodePrivate::insertAfter(newChild, refChild);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::replaceChild(QDomNodePrivate *newChild,
//      QDomNodePrivate *oldChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_own_ZN15QDomNodePrivate12replaceChildEPS_S0_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild,
    QDomNodePrivate *oldChild) {
  return self->QDomNodePrivate::replaceChild(newChild, oldChild);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::removeChild(QDomNodePrivate *oldChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_own_ZN15QDomNodePrivate11removeChildEPS_(
    QDomNodePrivate *self,
    QDomNodePrivate *oldChild) {
  return self->QDomNodePrivate::removeChild(oldChild);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  QDomNodePrivate *QDomNodePrivate::appendChild(QDomNodePrivate *newChild)
extern "C" Q_DECL_EXPORT
QDomNodePrivate *ritual_own_ZN15QDomNodePrivate11appendChildEPS_(
    QDomNodePrivate *self,
    QDomNodePrivate *newChild) {
  return self->QDomNodePrivate::appendChild(newChild);
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomNodePrivate::normalize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QDomNodePrivate9normalizeEv(QDomNodePrivate *self) {
  self->QDomNodePrivate::normalize();
}
#endif  // QT_CONFIG(dom)

#if QT_CONFIG(dom)
//  void QDomNodePrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QDomNodePrivate5clearEv(QDomNodePrivate *self) {
  self->QDomNodePrivate::clear();
}
#endif  // QT_CONFIG(dom)

//  QDomNode::NodeType QDomNodePrivate::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_own_ZNK15QDomNodePrivate8nodeTypeEv(
    const QDomNodePrivate *self) {
  return self->QDomNodePrivate::nodeType();
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
