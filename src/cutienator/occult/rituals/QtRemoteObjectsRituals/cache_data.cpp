//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qdebug.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 30, as _ZN9CacheDataC1EP39QAbstractItemModelReplicaImplementationPS_
inline CacheData::CacheData(QAbstractItemModelReplicaImplementation *model, CacheData *parentItem)
    : replicaModel(model)
    , parent(parentItem)
    , hasChildren(false)
    , columnCount(0)
    , rowCount(0)
{
    if (parent)
        replicaModel->m_activeParents.insert(parent);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 41, as _ZN9CacheDataD1Ev
inline CacheData::~CacheData() {
    if (parent && !replicaModel->m_activeParents.empty())
        replicaModel->m_activeParents.erase(this);
}
//  -----------------------------------------------------------------------

//  CacheData::CacheData(QAbstractItemModelReplicaImplementation *model,
//      CacheData *parentItem)
extern "C" Q_DECL_EXPORT
CacheData *ritual_ZN9CacheDataC1EP39QAbstractItemModelReplicaImplementationPS_(
    QAbstractItemModelReplicaImplementation *model,
    CacheData *parentItem) {
  return new CacheData(model, parentItem);
}

//  CacheData::~CacheData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9CacheDataD1Ev(CacheData *self) {
  delete self;
}

//  void CacheData::ensureChildren(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9CacheData14ensureChildrenEii(
    CacheData *self,
    int start,
    int end) {
  self->ensureChildren(start, end);
}

//  void CacheData::insertChildren(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9CacheData14insertChildrenEii(
    CacheData *self,
    int start,
    int end) {
  self->insertChildren(start, end);
}

//  void CacheData::removeChildren(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9CacheData14removeChildrenEii(
    CacheData *self,
    int start,
    int end) {
  self->removeChildren(start, end);
}

//  void CacheData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9CacheData5clearEv(CacheData *self) {
  self->clear();
}
