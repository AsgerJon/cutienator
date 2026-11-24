//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "private/qmetaobjectbuilder_p.h"
#include "qremoteobjectcontainers_p.h"
#include "qremoteobjectnode.h"
#include "qremoteobjectnode_p.h"
#include "qremoteobjectregistry.h"
#include "qremoteobjectdynamicreplica.h"
#include "qremoteobjectpacket_p.h"
#include "qremoteobjectregistrysource_p.h"
#include "qremoteobjectreplica_p.h"
#include "qremoteobjectsource_p.h"
#include "qremoteobjectabstractitemmodelreplica_p.h"
#include "qremoteobjectabstractitemmodeladapter_p.h"
#include <QtCore/qabstractitemmodel.h>
#include <memory>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 771, as _ZN30QRemoteObjectMetaObjectManagerD1Ev
inline QRemoteObjectMetaObjectManager::~QRemoteObjectMetaObjectManager()
{
    for (QMetaObject *mo : std::as_const(dynamicTypes)) {
        for (auto metaType : std::as_const(enumTypes[mo]))
            QMetaType::unregisterMetaType(metaType);
        enumTypes.remove(mo);
        free(mo); //QMetaObjectBuilder uses malloc, not new
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1276, as _ZN30QRemoteObjectMetaObjectManager17addFromMetaObjectEPK11QMetaObject
inline void QRemoteObjectMetaObjectManager::addFromMetaObject(const QMetaObject *metaObject)
{
    QString className = QLatin1String(metaObject->className());
    if (!className.endsWith(QLatin1String("Replica")))
        return;
    if (className == QLatin1String("QRemoteObjectDynamicReplica") || staticTypes.contains(className))
        return;
    className.chop(7); //Remove 'Replica' from name
    staticTypes.insert(className, metaObject);
}
//  -----------------------------------------------------------------------

//  QRemoteObjectMetaObjectManager::QRemoteObjectMetaObjectManager()
extern "C" Q_DECL_EXPORT
QRemoteObjectMetaObjectManager *ritual_ZN30QRemoteObjectMetaObjectManagerC1Ev() {
  return new QRemoteObjectMetaObjectManager();
}

//  QRemoteObjectMetaObjectManager::~QRemoteObjectMetaObjectManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRemoteObjectMetaObjectManagerD1Ev(
    QRemoteObjectMetaObjectManager *self) {
  delete self;
}

//  void QRemoteObjectMetaObjectManager::addFromMetaObject(const QMetaObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRemoteObjectMetaObjectManager17addFromMetaObjectEPK11QMetaObject(
    QRemoteObjectMetaObjectManager *self,
    const QMetaObject *a0) {
  self->addFromMetaObject(a0);
}
