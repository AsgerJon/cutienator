//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectstructs_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectstructs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 242, as _ZN26QRemoteObjectInternalTypes9ClassDataC1Eb
namespace QRemoteObjectInternalTypes {
using namespace QtRemoteObjects;
using namespace QRemoteObjectStringLiterals;
inline ClassData::ClassData(bool _isSource) : isSource(_isSource)
{
    baseMeta = _isSource ? &QObject::staticMetaObject : &QRemoteObjectReplica::staticMetaObject;
}
}  // namespace QRemoteObjectInternalTypes
//  -----------------------------------------------------------------------

//  QRemoteObjectInternalTypes::ClassData::ClassData(bool _isSource)
extern "C" Q_DECL_EXPORT
QRemoteObjectInternalTypes::ClassData *ritual_ZN26QRemoteObjectInternalTypes9ClassDataC1Eb(
    bool _isSource) {
  return new QRemoteObjectInternalTypes::ClassData(_isSource);
}

//  QRemoteObjectInternalTypes::ClassData::~ClassData()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRemoteObjectInternalTypes9ClassDataD1Ev(
    QRemoteObjectInternalTypes::ClassData *self) {
  delete self;
}
