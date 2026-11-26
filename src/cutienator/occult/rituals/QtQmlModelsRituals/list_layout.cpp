//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistmodel_p_p.h>
#include <QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmlnotifier_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 56, as local:qqmllistmodel.cpp:roleTypeName
static QString roleTypeName(ListLayout::Role::DataType t)
{
    static const QString roleTypeNames[] = {
        QStringLiteral("String"), QStringLiteral("Number"), QStringLiteral("Bool"),
        QStringLiteral("List"), QStringLiteral("QObject"), QStringLiteral("VariantMap"),
        QStringLiteral("DateTime"), QStringLiteral("Url"), QStringLiteral("Function")
    };

    if (t > ListLayout::Role::Invalid && t < ListLayout::Role::MaxDataType)
        return roleTypeNames[t];

    return QString();
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 83, as _ZN10ListLayout15getRoleOrCreateEPN3QV46StringENS_4Role8DataTypeE
inline const ListLayout::Role &ListLayout::getRoleOrCreate(QV4::String *key, Role::DataType type)
{
    QStringHash<Role *>::Node *node = roleHash.findNode(key);
    if (node) {
        const Role &r = *node->value;
        if (type != r.type)
            qmlWarning(nullptr) << QStringLiteral("Can't assign to existing role '%1' of different type [%2 -> %3]").arg(r.name).arg(roleTypeName(type)).arg(roleTypeName(r.type));
        return r;
    }

    QString qkey = key->toQString();

    return createRole(qkey, type);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 246, as _ZNK10ListLayout15getExistingRoleERK7QString
inline const ListLayout::Role *ListLayout::getExistingRole(const QString &key) const
{
    Role *r = nullptr;
    QStringHash<Role *>::Node *node = roleHash.findNode(key);
    if (node)
        r = node->value;
    return r;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 255, as _ZNK10ListLayout15getExistingRoleEPN3QV46StringE
inline const ListLayout::Role *ListLayout::getExistingRole(QV4::String *key) const
{
    Role *r = nullptr;
    QStringHash<Role *>::Node *node = roleHash.findNode(key);
    if (node)
        r = node->value;
    return r;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 174, as _ZN10ListLayout4syncEPS_S0_
inline void ListLayout::sync(ListLayout *src, ListLayout *target)
{
    int roleOffset = target->roles.size();
    int newRoleCount = src->roles.size() - roleOffset;

    for (int i=0 ; i < newRoleCount ; ++i) {
        Role *role = new Role(src->roles[roleOffset + i]);
        target->roles.append(role);
        target->roleHash.insert(role->name, role);
    }

    target->currentBlockOffset = src->currentBlockOffset;
    target->currentBlock = src->currentBlock;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 98, as _ZN10ListLayout10createRoleERK7QStringNS_4Role8DataTypeE
inline const ListLayout::Role &ListLayout::createRole(const QString &key, ListLayout::Role::DataType type)
{
    const int dataSizes[] = {
        sizeof(StringOrTranslation),
        sizeof(double),
        sizeof(bool),
        sizeof(ListModel *),
        sizeof(QV4::PersistentValue),
        sizeof(QVariantMap),
        sizeof(QDateTime),
        sizeof(QUrl),
        sizeof(QJSValue)
    };
    const int dataAlignments[] = {
        alignof(StringOrTranslation),
        alignof(double),
        alignof(bool),
        alignof(ListModel *),
        alignof(QV4::PersistentValue),
        alignof(QVariantMap),
        alignof(QDateTime),
        alignof(QUrl),
        alignof(QJSValue)
    };

    Role *r = new Role;
    r->name = key;
    r->type = type;

    if (type == Role::List) {
        r->subLayout = new ListLayout;
    } else {
        r->subLayout = nullptr;
    }

    int dataSize = dataSizes[type];
    int dataAlignment = dataAlignments[type];

    int dataOffset = (currentBlockOffset + dataAlignment-1) & ~(dataAlignment-1);
    if (dataOffset + dataSize > ListElement::BLOCK_SIZE) {
        r->blockIndex = ++currentBlock;
        r->blockOffset = 0;
        currentBlockOffset = dataSize;
    } else {
        r->blockIndex = currentBlock;
        r->blockOffset = dataOffset;
        currentBlockOffset = dataOffset + dataSize;
    }

    int roleIndex = roles.size();
    r->index = roleIndex;

    roles.append(r);
    roleHash.insert(key, r);

    return *r;
}
//  -----------------------------------------------------------------------

//  ListLayout::ListLayout()
extern "C" Q_DECL_EXPORT
ListLayout *ritual_ZN10ListLayoutC1Ev() {
  return new ListLayout();
}

//  ListLayout::ListLayout(const ListLayout *other)
extern "C" Q_DECL_EXPORT
ListLayout *ritual_ZN10ListLayoutC1EPKS_(const ListLayout *other) {
  return new ListLayout(other);
}

//  ListLayout::~ListLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10ListLayoutD1Ev(ListLayout *self) {
  delete self;
}

//  const Role &ListLayout::getRoleOrCreate(QV4::String *key, Role::DataType
//      type)
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZN10ListLayout15getRoleOrCreateEPN3QV46StringENS_4Role8DataTypeE(
    ListLayout *self,
    QV4::String *key,
    ListLayout::Role::DataType type) {
  return new ListLayout::Role(self->getRoleOrCreate(key, type));
}

//  const Role &ListLayout::getExistingRole(int index) const
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZNK10ListLayout15getExistingRoleEi(
    const ListLayout *self,
    int index) {
  return new ListLayout::Role(self->getExistingRole(index));
}

//  const Role *ListLayout::getExistingRole(const QString &key) const
extern "C" Q_DECL_EXPORT
const ListLayout::Role *ritual_ZNK10ListLayout15getExistingRoleERK7QString(
    const ListLayout *self,
    const QString *key) {
  return self->getExistingRole(*key);
}

//  const Role *ListLayout::getExistingRole(QV4::String *key) const
extern "C" Q_DECL_EXPORT
const ListLayout::Role *ritual_ZNK10ListLayout15getExistingRoleEPN3QV46StringE(
    const ListLayout *self,
    QV4::String *key) {
  return self->getExistingRole(key);
}

//  int ListLayout::roleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10ListLayout9roleCountEv(const ListLayout *self) {
  return self->roleCount();
}

//  void ListLayout::sync(ListLayout *src, ListLayout *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN10ListLayout4syncEPS_S0_(ListLayout *src, ListLayout *target) {
  ListLayout::sync(src, target);
}

//  const Role &ListLayout::createRole(const QString &key, Role::DataType
//      type)
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZN10ListLayout10createRoleERK7QStringNS_4Role8DataTypeE(
    ListLayout *self,
    const QString *key,
    ListLayout::Role::DataType type) {
  return new ListLayout::Role(self->createRole(*key, type));
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
