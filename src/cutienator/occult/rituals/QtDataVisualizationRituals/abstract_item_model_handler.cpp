//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstractitemmodelhandler_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AbstractItemModelHandler'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstractitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/abstractitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__AbstractItemModelHandler.cpp, line 1, as moc:AbstractItemModelHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24AbstractItemModelHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto AbstractItemModelHandler::qt_create_metaobjectdata<qt_meta_tag_ZN24AbstractItemModelHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AbstractItemModelHandler",
        "itemModelChanged",
        "",
        "const QAbstractItemModel*",
        "itemModel",
        "handleColumnsInserted",
        "QModelIndex",
        "parent",
        "start",
        "end",
        "handleColumnsMoved",
        "sourceParent",
        "sourceStart",
        "sourceEnd",
        "destinationParent",
        "destinationColumn",
        "handleColumnsRemoved",
        "handleDataChanged",
        "topLeft",
        "bottomRight",
        "QList<int>",
        "roles",
        "handleLayoutChanged",
        "QList<QPersistentModelIndex>",
        "parents",
        "QAbstractItemModel::LayoutChangeHint",
        "hint",
        "handleModelReset",
        "handleRowsInserted",
        "handleRowsMoved",
        "destinationRow",
        "handleRowsRemoved",
        "handleMappingChanged",
        "handlePendingResolve"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'itemModelChanged'
        QtMocHelpers::SignalData<void(const QAbstractItemModel *)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'handleColumnsInserted'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 }, { QMetaType::Int, 8 }, { QMetaType::Int, 9 },
        }}),
        // Slot 'handleColumnsMoved'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int, const QModelIndex &, int)>(10, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 11 }, { QMetaType::Int, 12 }, { QMetaType::Int, 13 }, { 0x80000000 | 6, 14 },
            { QMetaType::Int, 15 },
        }}),
        // Slot 'handleColumnsRemoved'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int)>(16, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 }, { QMetaType::Int, 8 }, { QMetaType::Int, 9 },
        }}),
        // Slot 'handleDataChanged'
        QtMocHelpers::SlotData<void(const QModelIndex &, const QModelIndex &, const QList<int> &)>(17, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 18 }, { 0x80000000 | 6, 19 }, { 0x80000000 | 20, 21 },
        }}),
        // Slot 'handleDataChanged'
        QtMocHelpers::SlotData<void(const QModelIndex &, const QModelIndex &)>(17, 2, QMC::AccessPublic | QMC::MethodCloned, QMetaType::Void, {{
            { 0x80000000 | 6, 18 }, { 0x80000000 | 6, 19 },
        }}),
        // Slot 'handleLayoutChanged'
        QtMocHelpers::SlotData<void(const QList<QPersistentModelIndex> &, QAbstractItemModel::LayoutChangeHint)>(22, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 23, 24 }, { 0x80000000 | 25, 26 },
        }}),
        // Slot 'handleLayoutChanged'
        QtMocHelpers::SlotData<void(const QList<QPersistentModelIndex> &)>(22, 2, QMC::AccessPublic | QMC::MethodCloned, QMetaType::Void, {{
            { 0x80000000 | 23, 24 },
        }}),
        // Slot 'handleLayoutChanged'
        QtMocHelpers::SlotData<void()>(22, 2, QMC::AccessPublic | QMC::MethodCloned, QMetaType::Void),
        // Slot 'handleModelReset'
        QtMocHelpers::SlotData<void()>(27, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'handleRowsInserted'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int)>(28, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 }, { QMetaType::Int, 8 }, { QMetaType::Int, 9 },
        }}),
        // Slot 'handleRowsMoved'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int, const QModelIndex &, int)>(29, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 11 }, { QMetaType::Int, 12 }, { QMetaType::Int, 13 }, { 0x80000000 | 6, 14 },
            { QMetaType::Int, 30 },
        }}),
        // Slot 'handleRowsRemoved'
        QtMocHelpers::SlotData<void(const QModelIndex &, int, int)>(31, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 }, { QMetaType::Int, 8 }, { QMetaType::Int, 9 },
        }}),
        // Slot 'handleMappingChanged'
        QtMocHelpers::SlotData<void()>(32, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'handlePendingResolve'
        QtMocHelpers::SlotData<void()>(33, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AbstractItemModelHandler, qt_meta_tag_ZN24AbstractItemModelHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AbstractItemModelHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24AbstractItemModelHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24AbstractItemModelHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24AbstractItemModelHandlerE_t>.metaTypes,
    nullptr
} };

void AbstractItemModelHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AbstractItemModelHandler *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->itemModelChanged((*reinterpret_cast<std::add_pointer_t<const QAbstractItemModel*>>(_a[1]))); break;
        case 1: _t->handleColumnsInserted((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3]))); break;
        case 2: _t->handleColumnsMoved((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[4])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[5]))); break;
        case 3: _t->handleColumnsRemoved((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3]))); break;
        case 4: _t->handleDataChanged((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QList<int>>>(_a[3]))); break;
        case 5: _t->handleDataChanged((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[2]))); break;
        case 6: _t->handleLayoutChanged((*reinterpret_cast<std::add_pointer_t<QList<QPersistentModelIndex>>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QAbstractItemModel::LayoutChangeHint>>(_a[2]))); break;
        case 7: _t->handleLayoutChanged((*reinterpret_cast<std::add_pointer_t<QList<QPersistentModelIndex>>>(_a[1]))); break;
        case 8: _t->handleLayoutChanged(); break;
        case 9: _t->handleModelReset(); break;
        case 10: _t->handleRowsInserted((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3]))); break;
        case 11: _t->handleRowsMoved((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[4])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[5]))); break;
        case 12: _t->handleRowsRemoved((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[3]))); break;
        case 13: _t->handleMappingChanged(); break;
        case 14: _t->handlePendingResolve(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 4:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 2:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QList<int> >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (AbstractItemModelHandler::*)(const QAbstractItemModel * )>(_a, &AbstractItemModelHandler::itemModelChanged, 0))
            return;
    }
}

const QMetaObject *AbstractItemModelHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AbstractItemModelHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24AbstractItemModelHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int AbstractItemModelHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 15)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 15;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 15)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 15;
    }
    return _id;
}

// SIGNAL 0
void AbstractItemModelHandler::itemModelChanged(const QAbstractItemModel * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 22, as _ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel
inline void AbstractItemModelHandler::setItemModel(QAbstractItemModel *itemModel)
{
    if (itemModel != m_itemModel.data()) {
        if (!m_itemModel.isNull())
            QObject::disconnect(m_itemModel, 0, this, 0);

        m_itemModel = itemModel;

        if (!m_itemModel.isNull()) {
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::columnsInserted,
                             this, &AbstractItemModelHandler::handleColumnsInserted);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::columnsMoved,
                             this, &AbstractItemModelHandler::handleColumnsMoved);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::columnsRemoved,
                             this, &AbstractItemModelHandler::handleColumnsRemoved);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::dataChanged,
                             this, &AbstractItemModelHandler::handleDataChanged);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::layoutChanged,
                             this, &AbstractItemModelHandler::handleLayoutChanged);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::modelReset,
                             this, &AbstractItemModelHandler::handleModelReset);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::rowsInserted,
                             this, &AbstractItemModelHandler::handleRowsInserted);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::rowsMoved,
                             this, &AbstractItemModelHandler::handleRowsMoved);
            QObject::connect(m_itemModel.data(), &QAbstractItemModel::rowsRemoved,
                             this, &AbstractItemModelHandler::handleRowsRemoved);
        }
        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);

        emit itemModelChanged(itemModel);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 166, as _ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i
inline void AbstractItemModelHandler::handleRowsMoved(const QModelIndex &sourceParent,
                                               int sourceStart,
                                               int sourceEnd,
                                               const QModelIndex &destinationParent,
                                               int destinationRow)
{
    Q_UNUSED(sourceParent);
    Q_UNUSED(sourceStart);
    Q_UNUSED(sourceEnd);
    Q_UNUSED(destinationParent);
    Q_UNUSED(destinationRow);

    // Default handling for rowsMoved is to do full reset, as it cannot be optimized
    // in a general case, where we do not know which row/column/index the item model item
    // actually ended up to in the proxy.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 142, as _ZN24AbstractItemModelHandler16handleModelResetEv
inline void AbstractItemModelHandler::handleModelReset()
{
    // Data cleared, reset array
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 112, as _ZN24AbstractItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE
inline void AbstractItemModelHandler::handleDataChanged(const QModelIndex &topLeft,
                                                 const QModelIndex &bottomRight,
                                                 const QList<int> &roles)
{
    Q_UNUSED(topLeft);
    Q_UNUSED(bottomRight);
    Q_UNUSED(roles);

    // Default handling for dataChanged is to do full reset, as it cannot be optimized
    // in a general case, where we do not know which row/column/index the item model item
    // actually ended up to in the proxy.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 187, as _ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii
inline void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    Q_UNUSED(start);
    Q_UNUSED(end);

    // Default handling for rowsRemoved is to do full reset, as it cannot be optimized
    // in a general case, where we do not know which row/column/index the item model item
    // actually ended up to in the proxy.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 77, as _ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i
inline void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex &sourceParent,
                                                  int sourceStart,
                                                  int sourceEnd,
                                                  const QModelIndex &destinationParent,
                                                  int destinationColumn)
{
    Q_UNUSED(sourceParent);
    Q_UNUSED(sourceStart);
    Q_UNUSED(sourceEnd);
    Q_UNUSED(destinationParent);
    Q_UNUSED(destinationColumn);

    // Manipulating columns changes all rows in proxies that map rows/columns directly,
    // and its effects are not clearly defined in others -> always do full reset.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 151, as _ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii
inline void AbstractItemModelHandler::handleRowsInserted(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    Q_UNUSED(start);
    Q_UNUSED(end);

    // Default handling for rowsInserted is to do full reset, as it cannot be optimized
    // in a general case, where we do not know which row/column/index the item model item
    // actually ended up to in the proxy.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 129, as _ZN24AbstractItemModelHandler19handleLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void AbstractItemModelHandler::handleLayoutChanged(const QList<QPersistentModelIndex> &parents,
                                                   QAbstractItemModel::LayoutChangeHint hint)
{
    Q_UNUSED(parents);
    Q_UNUSED(hint);

    // Resolve entire model if layout changes
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 97, as _ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii
inline void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex &parent,
                                                    int start, int end)
{
    Q_UNUSED(parent);
    Q_UNUSED(start);
    Q_UNUSED(end);

    // Manipulating columns changes all rows in proxies that map rows/columns directly,
    // and its effects are not clearly defined in others -> always do full reset.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 202, as _ZN24AbstractItemModelHandler20handleMappingChangedEv
inline void AbstractItemModelHandler::handleMappingChanged()
{
    if (!m_resolveTimer.isActive())
        m_resolveTimer.start(0);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 208, as _ZN24AbstractItemModelHandler20handlePendingResolveEv
inline void AbstractItemModelHandler::handlePendingResolve()
{
    resolveModel();
    m_fullReset = false;
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 62, as _ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii
inline void AbstractItemModelHandler::handleColumnsInserted(const QModelIndex &parent,
                                                     int start, int end)
{
    Q_UNUSED(parent);
    Q_UNUSED(start);
    Q_UNUSED(end);

    // Manipulating columns changes all rows in proxies that map rows/columns directly,
    // and its effects are not clearly defined in others -> always do full reset.
    if (!m_resolveTimer.isActive()) {
        m_fullReset = true;
        m_resolveTimer.start(0);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 18, as _ZN24AbstractItemModelHandlerD0Ev
inline AbstractItemModelHandler::~AbstractItemModelHandler()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 57, as _ZNK24AbstractItemModelHandler9itemModelEv
inline QAbstractItemModel *AbstractItemModelHandler::itemModel() const
{
    return m_itemModel.data();
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 8, as _ZN24AbstractItemModelHandlerC1EP7QObject
inline AbstractItemModelHandler::AbstractItemModelHandler(QObject *parent)
    : QObject(parent),
      resolvePending(0),
      m_fullReset(true)
{
    m_resolveTimer.setSingleShot(true);
    QObject::connect(&m_resolveTimer, &QTimer::timeout,
                     this, &AbstractItemModelHandler::handlePendingResolve);
}
//  -----------------------------------------------------------------------

//  A AbstractItemModelHandler that Python can take functions over in. Every AbstractItemModelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAbstractItemModelHandlerCall0)(const void *, QAbstractItemModel *, int *);
typedef void * (*CuteAbstractItemModelHandlerCall1)(const void *, int *);
typedef void (*CuteAbstractItemModelHandlerCall2)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall3)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall4)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall5)(const void *, int *);
typedef void (*CuteAbstractItemModelHandlerCall6)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall7)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall8)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteAbstractItemModelHandlerCall9)(const void *, int *);
typedef void (*CuteAbstractItemModelHandlerCall10)(const void *, int *);
typedef void (*CuteAbstractItemModelHandlerCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstractItemModelHandlerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstractItemModelHandlerCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractItemModelHandlerCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractItemModelHandlerCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractItemModelHandlerCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractItemModelHandlerCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractItemModelHandlerCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAbstractItemModelHandler : public AbstractItemModelHandler {
public:
  using AbstractItemModelHandler::AbstractItemModelHandler;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24AbstractItemModelHandler9itemModelEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler16handleModelResetEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleMappingChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handlePendingResolveEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12resolveModelEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
  //      *itemModel)
  void setItemModel(QAbstractItemModel *itemModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall0 call = reinterpret_cast<CuteAbstractItemModelHandlerCall0>(taken[0]);
      call(this, itemModel, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::setItemModel(itemModel);
  }

  //  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
  QAbstractItemModel *itemModel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall1 call = reinterpret_cast<CuteAbstractItemModelHandlerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractItemModel *>(given);
    }
    return AbstractItemModelHandler::itemModel();
  }

  //  void AbstractItemModelHandler::handleColumnsInserted(const
  //      QModelIndex &parent, int start, int end)
  void handleColumnsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[2]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall2 call = reinterpret_cast<CuteAbstractItemModelHandlerCall2>(taken[2]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsInserted(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex
  //      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
  //      &destinationParent, int destinationColumn)
  void handleColumnsMoved(
      const QModelIndex &sourceParent,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destinationParent,
      int destinationColumn) override {
    if (taken[3]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall3 call = reinterpret_cast<CuteAbstractItemModelHandlerCall3>(taken[3]);
      call(this, &sourceParent, sourceStart, sourceEnd, &destinationParent, destinationColumn, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsMoved(sourceParent, sourceStart, sourceEnd, destinationParent, destinationColumn);
  }

  //  void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void handleColumnsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[4]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall4 call = reinterpret_cast<CuteAbstractItemModelHandlerCall4>(taken[4]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleModelReset()
  void handleModelReset() override {
    if (taken[5]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall5 call = reinterpret_cast<CuteAbstractItemModelHandlerCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleModelReset();
  }

  //  void AbstractItemModelHandler::handleRowsInserted(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[6]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall6 call = reinterpret_cast<CuteAbstractItemModelHandlerCall6>(taken[6]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsInserted(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleRowsMoved(const QModelIndex
  //      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
  //      &destinationParent, int destinationRow)
  void handleRowsMoved(
      const QModelIndex &sourceParent,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destinationParent,
      int destinationRow) override {
    if (taken[7]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall7 call = reinterpret_cast<CuteAbstractItemModelHandlerCall7>(taken[7]);
      call(this, &sourceParent, sourceStart, sourceEnd, &destinationParent, destinationRow, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsMoved(sourceParent, sourceStart, sourceEnd, destinationParent, destinationRow);
  }

  //  void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[8]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall8 call = reinterpret_cast<CuteAbstractItemModelHandlerCall8>(taken[8]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleMappingChanged()
  void handleMappingChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall9 call = reinterpret_cast<CuteAbstractItemModelHandlerCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleMappingChanged();
  }

  //  void AbstractItemModelHandler::handlePendingResolve()
  void handlePendingResolve() override {
    if (taken[10]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall10 call = reinterpret_cast<CuteAbstractItemModelHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handlePendingResolve();
  }

  //  void AbstractItemModelHandler::resolveModel()
  void resolveModel() override {
    if (taken[11]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall11 call = reinterpret_cast<CuteAbstractItemModelHandlerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall12 call = reinterpret_cast<CuteAbstractItemModelHandlerCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall13 call = reinterpret_cast<CuteAbstractItemModelHandlerCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall14 call = reinterpret_cast<CuteAbstractItemModelHandlerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall15 call = reinterpret_cast<CuteAbstractItemModelHandlerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall16 call = reinterpret_cast<CuteAbstractItemModelHandlerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall17 call = reinterpret_cast<CuteAbstractItemModelHandlerCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteAbstractItemModelHandlerCall18 call = reinterpret_cast<CuteAbstractItemModelHandlerCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AbstractItemModelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24AbstractItemModelHandler10metaObjectEv(
    const AbstractItemModelHandler *self) {
  return self->metaObject();
}

//  void *AbstractItemModelHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24AbstractItemModelHandler11qt_metacastEPKc(
    AbstractItemModelHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AbstractItemModelHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24AbstractItemModelHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    AbstractItemModelHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AbstractItemModelHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24AbstractItemModelHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AbstractItemModelHandler::tr(s, c, n));
}

//  AbstractItemModelHandler::AbstractItemModelHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
AbstractItemModelHandler *ritual_ZN24AbstractItemModelHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteAbstractItemModelHandler(parent);
}

//  AbstractItemModelHandler::~AbstractItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandlerD1Ev(
    AbstractItemModelHandler *self) {
  delete self;
}

//  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
//      *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel(
    AbstractItemModelHandler *self,
    QAbstractItemModel *itemModel) {
  self->setItemModel(itemModel);
}

//  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK24AbstractItemModelHandler9itemModelEv(
    const AbstractItemModelHandler *self) {
  return self->itemModel();
}

//  void AbstractItemModelHandler::handleColumnsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleColumnsInserted(*parent, start, end);
}

//  void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i(
    AbstractItemModelHandler *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationColumn) {
  self->handleColumnsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationColumn);
}

//  void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleColumnsRemoved(*parent, start, end);
}

//  void AbstractItemModelHandler::handleDataChanged(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE(
    AbstractItemModelHandler *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight,
    const QList<int> *roles) {
  self->handleDataChanged(*topLeft, *bottomRight, *roles);
}

//  void AbstractItemModelHandler::handleLayoutChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler19handleLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    AbstractItemModelHandler *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->handleLayoutChanged(*parents, hint);
}

//  void AbstractItemModelHandler::handleModelReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler16handleModelResetEv(
    AbstractItemModelHandler *self) {
  self->handleModelReset();
}

//  void AbstractItemModelHandler::handleRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleRowsInserted(*parent, start, end);
}

//  void AbstractItemModelHandler::handleRowsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i(
    AbstractItemModelHandler *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationRow) {
  self->handleRowsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationRow);
}

//  void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleRowsRemoved(*parent, start, end);
}

//  void AbstractItemModelHandler::handleMappingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler20handleMappingChangedEv(
    AbstractItemModelHandler *self) {
  self->handleMappingChanged();
}

//  void AbstractItemModelHandler::handlePendingResolve()
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler20handlePendingResolveEv(
    AbstractItemModelHandler *self) {
  self->handlePendingResolve();
}

//  void AbstractItemModelHandler::itemModelChanged(const QAbstractItemModel
//      *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler16itemModelChangedEPK18QAbstractItemModel(
    AbstractItemModelHandler *self,
    const QAbstractItemModel *itemModel) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AbstractItemModelHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemModelChanged(const QAbstractItemModel *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemModelChanged(const QAbstractItemModel *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&itemModel)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AbstractItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24AbstractItemModelHandler12resolveModelEv(
    AbstractItemModelHandler *self) {
  self->resolveModel();
}

//  a Python function taken by a CuteAbstractItemModelHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractItemModelHandler(
    AbstractItemModelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractItemModelHandler *>(self)->take(key, call);
}

//  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
//      *itemModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel(
    AbstractItemModelHandler *self,
    QAbstractItemModel *itemModel) {
  self->AbstractItemModelHandler::setItemModel(itemModel);
}

//  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_own_ZNK24AbstractItemModelHandler9itemModelEv(
    const AbstractItemModelHandler *self) {
  return self->AbstractItemModelHandler::itemModel();
}

//  void AbstractItemModelHandler::handleColumnsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->AbstractItemModelHandler::handleColumnsInserted(*parent, start, end);
}

//  void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationColumn)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i(
    AbstractItemModelHandler *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationColumn) {
  self->AbstractItemModelHandler::handleColumnsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationColumn);
}

//  void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->AbstractItemModelHandler::handleColumnsRemoved(*parent, start, end);
}

//  void AbstractItemModelHandler::handleModelReset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler16handleModelResetEv(
    AbstractItemModelHandler *self) {
  self->AbstractItemModelHandler::handleModelReset();
}

//  void AbstractItemModelHandler::handleRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->AbstractItemModelHandler::handleRowsInserted(*parent, start, end);
}

//  void AbstractItemModelHandler::handleRowsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i(
    AbstractItemModelHandler *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationRow) {
  self->AbstractItemModelHandler::handleRowsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationRow);
}

//  void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii(
    AbstractItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->AbstractItemModelHandler::handleRowsRemoved(*parent, start, end);
}

//  void AbstractItemModelHandler::handleMappingChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler20handleMappingChangedEv(
    AbstractItemModelHandler *self) {
  self->AbstractItemModelHandler::handleMappingChanged();
}

//  void AbstractItemModelHandler::handlePendingResolve()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24AbstractItemModelHandler20handlePendingResolveEv(
    AbstractItemModelHandler *self) {
  self->AbstractItemModelHandler::handlePendingResolve();
}
