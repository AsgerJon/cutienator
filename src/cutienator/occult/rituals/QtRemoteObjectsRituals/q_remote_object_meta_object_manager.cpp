//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectregistry.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
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

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 781, as _ZN30QRemoteObjectMetaObjectManager17metaObjectForTypeERK7QString
inline const QMetaObject *QRemoteObjectMetaObjectManager::metaObjectForType(const QString &type)
{
    qCDebug(QT_REMOTEOBJECT) << "metaObjectForType: looking for" << type << "static keys:" << staticTypes.keys() << "dynamic keys:" << dynamicTypes.keys();
    Q_ASSERT(staticTypes.contains(type) || dynamicTypes.contains(type));
    auto it = staticTypes.constFind(type);
    if (it != staticTypes.constEnd())
        return it.value();
    return dynamicTypes.value(type);
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

//  const QMetaObject
//      *QRemoteObjectMetaObjectManager::metaObjectForType(const QString
//      &type)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN30QRemoteObjectMetaObjectManager17metaObjectForTypeERK7QString(
    QRemoteObjectMetaObjectManager *self,
    const QString *type) {
  return self->metaObjectForType(*type);
}

//  void QRemoteObjectMetaObjectManager::addFromMetaObject(const QMetaObject
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRemoteObjectMetaObjectManager17addFromMetaObjectEPK11QMetaObject(
    QRemoteObjectMetaObjectManager *self,
    const QMetaObject *a0) {
  self->addFromMetaObject(a0);
}
