//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllist_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllist_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmllist.h"
#include "qqmllist_p.h"
#include <private/qqmlcontextdata_p.h>
#include <private/qqmlproperty_p.h>
#include <private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmllist.cpp, line 24, as _ZN24QQmlListReferencePrivateC1Ev
inline QQmlListReferencePrivate::QQmlListReferencePrivate()
: refCount(1)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmllist.cpp, line 44, as _ZN24QQmlListReferencePrivate6addrefEv
inline void QQmlListReferencePrivate::addref()
{
    Q_ASSERT(refCount > 0);
    ++refCount;
}

//  from ../qtdeclarative/src/qml/qml/qqmllist.cpp, line 50, as _ZN24QQmlListReferencePrivate7releaseEv
inline void QQmlListReferencePrivate::release()
{
    Q_ASSERT(refCount > 0);
    --refCount;
    if (!refCount)
        delete this;
}
//  -----------------------------------------------------------------------

//  QQmlListReferencePrivate::QQmlListReferencePrivate()
extern "C" Q_DECL_EXPORT
QQmlListReferencePrivate *ritual_ZN24QQmlListReferencePrivateC1Ev() {
  return new QQmlListReferencePrivate();
}

//  void QQmlListReferencePrivate::addref()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListReferencePrivate6addrefEv(
    QQmlListReferencePrivate *self) {
  self->addref();
}

//  void QQmlListReferencePrivate::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListReferencePrivate7releaseEv(
    QQmlListReferencePrivate *self) {
  self->release();
}

//  QQmlListReferencePrivate *QQmlListReferencePrivate::get(QQmlListReference
//      *ref)
extern "C" Q_DECL_EXPORT
QQmlListReferencePrivate *ritual_ZN24QQmlListReferencePrivate3getEP17QQmlListReference(
    QQmlListReference *ref) {
  return QQmlListReferencePrivate::get(ref);
}

//  const QMetaObject *QQmlListReferencePrivate::elementType()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN24QQmlListReferencePrivate11elementTypeEv(
    QQmlListReferencePrivate *self) {
  return self->elementType();
}

//  QQmlListReferencePrivate::~QQmlListReferencePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListReferencePrivateD1Ev(
    QQmlListReferencePrivate *self) {
  delete self;
}
