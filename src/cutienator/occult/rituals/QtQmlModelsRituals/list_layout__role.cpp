//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmllistmodel_p_p.h"
#include "qqmllistmodelworkeragent_p.h"
#include <private/qjsvalue_p.h>
#include <private/qqmlcustomparser_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmljsast_p.h>
#include <private/qqmljsengine_p.h>
#include <private/qqmllistwrapper_p.h>
#include <private/qqmlnotifier_p.h>
#include <private/qqmlopenmetaobject_p.h>
#include <private/qv4alloca_p.h>
#include <private/qv4dateobject_p.h>
#include <private/qv4lookup_p.h>
#include <private/qv4object_p.h>
#include <private/qv4objectiterator_p.h>
#include <private/qv4qmlcontext_p.h>
#include <private/qv4sequenceobject_p.h>
#include <private/qv4urlobject_p.h>
#include <qqmlcontext.h>
#include <qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 156, as _ZN10ListLayoutC1EPKS_
inline ListLayout::ListLayout(const ListLayout *other) : currentBlock(0), currentBlockOffset(0)
{
    const int otherRolesCount = other->roles.size();
    roles.reserve(otherRolesCount);
    for (int i=0 ; i < otherRolesCount; ++i) {
        Role *role = new Role(other->roles[i]);
        roles.append(role);
        roleHash.insert(role->name, role);
    }
    currentBlockOffset = other->currentBlockOffset;
    currentBlock = other->currentBlock;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 169, as _ZN10ListLayoutD1Ev
inline ListLayout::~ListLayout()
{
    qDeleteAll(roles);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 189, as _ZN10ListLayout4RoleC1EPKS0_
inline ListLayout::Role::Role(const Role *other)
{
    name = other->name;
    type = other->type;
    blockIndex = other->blockIndex;
    blockOffset = other->blockOffset;
    index = other->index;
    if (other->subLayout)
        subLayout = new ListLayout(other->subLayout);
    else
        subLayout = nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 202, as _ZN10ListLayout4RoleD1Ev
inline ListLayout::Role::~Role()
{
    delete subLayout;
}
//  -----------------------------------------------------------------------

//  ListLayout::Role::Role()
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZN10ListLayout4RoleC1Ev() {
  return new ListLayout::Role();
}

//  ListLayout::Role::Role(const Role *other)
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZN10ListLayout4RoleC1EPKS0_(
    const ListLayout::Role *other) {
  return new ListLayout::Role(other);
}

//  ListLayout::Role::~Role()
extern "C" Q_DECL_EXPORT
void ritual_ZN10ListLayout4RoleD1Ev(ListLayout::Role *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_list_model)
