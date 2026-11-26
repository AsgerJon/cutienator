//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/surfaceitemmodelhandler_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'SurfaceItemModelHandler'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/surfaceitemmodelhandler_p.h>
#include <QtDataVisualization/private/abstractitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__SurfaceItemModelHandler.cpp, line 1, as moc:SurfaceItemModelHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23SurfaceItemModelHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto SurfaceItemModelHandler::qt_create_metaobjectdata<qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "SurfaceItemModelHandler",
        "handleDataChanged",
        "",
        "QModelIndex",
        "topLeft",
        "bottomRight",
        "QList<int>",
        "roles"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'handleDataChanged'
        QtMocHelpers::SlotData<void(const QModelIndex &, const QModelIndex &, const QList<int> &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 3, 5 }, { 0x80000000 | 6, 7 },
        }}),
        // Slot 'handleDataChanged'
        QtMocHelpers::SlotData<void(const QModelIndex &, const QModelIndex &)>(1, 2, QMC::AccessPublic | QMC::MethodCloned, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 3, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<SurfaceItemModelHandler, qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject SurfaceItemModelHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<AbstractItemModelHandler::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>.metaTypes,
    nullptr
} };

void SurfaceItemModelHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<SurfaceItemModelHandler *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->handleDataChanged((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QList<int>>>(_a[3]))); break;
        case 1: _t->handleDataChanged((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 2:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QList<int> >(); break;
            }
            break;
        }
    }
}

const QMetaObject *SurfaceItemModelHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *SurfaceItemModelHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23SurfaceItemModelHandlerE_t>.strings))
        return static_cast<void*>(this);
    return AbstractItemModelHandler::qt_metacast(_clname);
}

int SurfaceItemModelHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = AbstractItemModelHandler::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/surfaceitemmodelhandler.cpp, line 82, as _ZN23SurfaceItemModelHandler12resolveModelEv
inline void SurfaceItemModelHandler::resolveModel()
{
    if (m_itemModel.isNull()) {
        m_proxy->resetArray(0);
        m_proxyArray = 0;
        return;
    }

    if (!m_proxy->useModelCategories()
            && (m_proxy->rowRole().isEmpty() || m_proxy->columnRole().isEmpty())) {
        m_proxy->resetArray(0);
        m_proxyArray = 0;
        return;
    }

    // Position patterns can be reused on single item changes, so store them to member variables.
    QRegularExpression rowPattern(m_proxy->rowRolePattern());
    QRegularExpression colPattern(m_proxy->columnRolePattern());
    m_xPosPattern = m_proxy->xPosRolePattern();
    m_yPosPattern = m_proxy->yPosRolePattern();
    m_zPosPattern = m_proxy->zPosRolePattern();
    QString rowReplace = m_proxy->rowRoleReplace();
    QString colReplace = m_proxy->columnRoleReplace();
    m_xPosReplace = m_proxy->xPosRoleReplace();
    m_yPosReplace = m_proxy->yPosRoleReplace();
    m_zPosReplace = m_proxy->zPosRoleReplace();
    bool haveRowPattern = !rowPattern.namedCaptureGroups().isEmpty() && rowPattern.isValid();
    bool haveColPattern = !colPattern.namedCaptureGroups().isEmpty() && colPattern.isValid();
    m_haveXPosPattern = !m_xPosPattern.namedCaptureGroups().isEmpty() && m_xPosPattern.isValid();
    m_haveYPosPattern = !m_yPosPattern.namedCaptureGroups().isEmpty() && m_yPosPattern.isValid();
    m_haveZPosPattern = !m_zPosPattern.namedCaptureGroups().isEmpty() && m_zPosPattern.isValid();

    QHash<int, QByteArray> roleHash = m_itemModel->roleNames();

    // Default to display role if no mapping
    m_xPosRole = roleHash.key(m_proxy->xPosRole().toLatin1(), noRoleIndex);
    m_yPosRole = roleHash.key(m_proxy->yPosRole().toLatin1(), Qt::DisplayRole);
    m_zPosRole = roleHash.key(m_proxy->zPosRole().toLatin1(), noRoleIndex);
    int rowCount = m_itemModel->rowCount();
    int columnCount = m_itemModel->columnCount();

    if (m_proxy->useModelCategories()) {
        // If dimensions have changed, recreate the array
        if (m_proxyArray != m_proxy->array() || columnCount != m_proxy->columnCount()
                || rowCount != m_proxyArray->size()) {
            m_proxyArray = new QSurfaceDataArray;
            m_proxyArray->reserve(rowCount);
            for (int i = 0; i < rowCount; i++)
                m_proxyArray->append(new QSurfaceDataRow(columnCount));
        }
        for (int i = 0; i < rowCount; i++) {
            QSurfaceDataRow &newProxyRow = *m_proxyArray->at(i);
            for (int j = 0; j < columnCount; j++) {
                QModelIndex index = m_itemModel->index(i, j);
                QVariant xValueVar = index.data(m_xPosRole);
                QVariant yValueVar = index.data(m_yPosRole);
                QVariant zValueVar = index.data(m_zPosRole);
                float xPos;
                float yPos;
                float zPos;
                if (m_xPosRole != noRoleIndex) {
                    if (m_haveXPosPattern)
                        xPos = xValueVar.toString().replace(m_xPosPattern, m_xPosReplace).toFloat();
                    else
                        xPos = xValueVar.toFloat();
                } else {
                    QString header = m_itemModel->headerData(j, Qt::Horizontal).toString();
                    bool ok = false;
                    float headerValue = header.toFloat(&ok);
                    if (ok)
                        xPos = headerValue;
                    else
                        xPos = float(j);
                }

                if (m_haveYPosPattern)
                    yPos = yValueVar.toString().replace(m_yPosPattern, m_yPosReplace).toFloat();
                else
                    yPos = yValueVar.toFloat();

                if (m_zPosRole != noRoleIndex) {
                    if (m_haveZPosPattern)
                        zPos = zValueVar.toString().replace(m_zPosPattern, m_zPosReplace).toFloat();
                    else
                        zPos = zValueVar.toFloat();
                } else {
                    QString header = m_itemModel->headerData(i, Qt::Vertical).toString();
                    bool ok = false;
                    float headerValue = header.toFloat(&ok);
                    if (ok)
                        zPos = headerValue;
                    else
                        zPos = float(i);
                }

                newProxyRow[j].setPosition(QVector3D(xPos, yPos, zPos));
            }
        }
    } else {
        int rowRole = roleHash.key(m_proxy->rowRole().toLatin1());
        int columnRole = roleHash.key(m_proxy->columnRole().toLatin1());
        if (m_xPosRole == noRoleIndex)
            m_xPosRole = columnRole;
        if (m_zPosRole == noRoleIndex)
            m_zPosRole = rowRole;

        bool generateRows = m_proxy->autoRowCategories();
        bool generateColumns = m_proxy->autoColumnCategories();

        QStringList rowList;
        QStringList columnList;
        // For detecting duplicates in categories generation, using QHashes should be faster than
        // simple QStringList::contains() check.
        QHash<QString, bool> rowListHash;
        QHash<QString, bool> columnListHash;

        bool cumulative = m_proxy->multiMatchBehavior() == QItemModelSurfaceDataProxy::MMBAverage
                || m_proxy->multiMatchBehavior() == QItemModelSurfaceDataProxy::MMBCumulativeY;
        bool average = m_proxy->multiMatchBehavior() == QItemModelSurfaceDataProxy::MMBAverage;
        bool takeFirst = m_proxy->multiMatchBehavior() == QItemModelSurfaceDataProxy::MMBFirst;
        QHash<QString, QHash<QString, int> > *matchCountMap = 0;
        if (cumulative)
            matchCountMap = new QHash<QString, QHash<QString, int> >;

        // Sort values into rows and columns
        typedef QHash<QString, QVector3D> ColumnValueMap;
        QHash <QString, ColumnValueMap> itemValueMap;
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < columnCount; j++) {
                QModelIndex index = m_itemModel->index(i, j);
                QString rowRoleStr = index.data(rowRole).toString();
                if (haveRowPattern)
                    rowRoleStr.replace(rowPattern, rowReplace);
                QString columnRoleStr = index.data(columnRole).toString();
                if (haveColPattern)
                    columnRoleStr.replace(colPattern, colReplace);
                QVariant xValueVar = index.data(m_xPosRole);
                QVariant yValueVar = index.data(m_yPosRole);
                QVariant zValueVar = index.data(m_zPosRole);
                float xPos;
                float yPos;
                float zPos;
                if (m_haveXPosPattern)
                    xPos = xValueVar.toString().replace(m_xPosPattern, m_xPosReplace).toFloat();
                else
                    xPos = xValueVar.toFloat();
                if (m_haveYPosPattern)
                    yPos = yValueVar.toString().replace(m_yPosPattern, m_yPosReplace).toFloat();
                else
                    yPos = yValueVar.toFloat();
                if (m_haveZPosPattern)
                    zPos = zValueVar.toString().replace(m_zPosPattern, m_zPosReplace).toFloat();
                else
                    zPos = zValueVar.toFloat();

                QVector3D itemPos(xPos, yPos, zPos);

                if (cumulative)
                    (*matchCountMap)[rowRoleStr][columnRoleStr]++;

                if (cumulative) {
                    itemValueMap[rowRoleStr][columnRoleStr] += itemPos;
                } else {
                    if (takeFirst && itemValueMap.contains(rowRoleStr)) {
                        if (itemValueMap.value(rowRoleStr).contains(columnRoleStr))
                            continue; // We already have a value for this row/column combo
                    }
                    itemValueMap[rowRoleStr][columnRoleStr] = itemPos;
                }

                if (generateRows && !rowListHash.value(rowRoleStr, false)) {
                    rowListHash.insert(rowRoleStr, true);
                    rowList << rowRoleStr;
                }
                if (generateColumns && !columnListHash.value(columnRoleStr, false)) {
                    columnListHash.insert(columnRoleStr, true);
                    columnList << columnRoleStr;
                }
            }
        }

        if (generateRows)
            m_proxy->dptr()->m_rowCategories = rowList;
        else
            rowList = m_proxy->rowCategories();

        if (generateColumns)
            m_proxy->dptr()->m_columnCategories = columnList;
        else
            columnList = m_proxy->columnCategories();

        // If dimensions have changed, recreate the array
        if (m_proxyArray != m_proxy->array() || columnList.size() != m_proxy->columnCount()
                || rowList.size() != m_proxyArray->size()) {
            m_proxyArray = new QSurfaceDataArray;
            m_proxyArray->reserve(rowList.size());
            for (int i = 0; i < rowList.size(); i++)
                m_proxyArray->append(new QSurfaceDataRow(columnList.size()));
        }
        // Create data array from itemValueMap
        for (int i = 0; i < rowList.size(); i++) {
            QString rowKey = rowList.at(i);
            QSurfaceDataRow &newProxyRow = *m_proxyArray->at(i);
            for (int j = 0; j < columnList.size(); j++) {
                QVector3D &itemPos = itemValueMap[rowKey][columnList.at(j)];
                if (cumulative) {
                    float divisor = float((*matchCountMap)[rowKey][columnList.at(j)]);
                    if (divisor) {
                        if (average) {
                            itemPos /= divisor;
                        } else { // cumulativeY
                            itemPos.setX(itemPos.x() / divisor);
                            itemPos.setZ(itemPos.z() / divisor);
                        }
                    }
                }
                newProxyRow[j].setPosition(itemPos);
            }
        }

        delete matchCountMap;
    }

    m_proxy->resetArray(m_proxyArray);
}

//  from ../qtdatavis3d/src/datavisualization/data/surfaceitemmodelhandler.cpp, line 25, as _ZN23SurfaceItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE
inline void SurfaceItemModelHandler::handleDataChanged(const QModelIndex &topLeft,
                                                const QModelIndex &bottomRight,
                                                const QList<int> &roles)
{
    // Do nothing if full reset already pending
    if (!m_fullReset) {
        if (!m_proxy->useModelCategories()) {
            // If the data model doesn't directly map rows and columns, we cannot optimize
            AbstractItemModelHandler::handleDataChanged(topLeft, bottomRight, roles);
        } else {
            int startRow = qMin(topLeft.row(), bottomRight.row());
            int endRow = qMax(topLeft.row(), bottomRight.row());
            int startCol = qMin(topLeft.column(), bottomRight.column());
            int endCol = qMax(topLeft.column(), bottomRight.column());

            for (int i = startRow; i <= endRow; i++) {
                for (int j = startCol; j <= endCol; j++) {
                    QModelIndex index = m_itemModel->index(i, j);
                    QSurfaceDataItem item;
                    QVariant xValueVar = index.data(m_xPosRole);
                    QVariant yValueVar = index.data(m_yPosRole);
                    QVariant zValueVar = index.data(m_zPosRole);
                    const QSurfaceDataItem *oldItem = m_proxy->itemAt(i, j);
                    float xPos;
                    float yPos;
                    float zPos;
                    if (m_xPosRole != noRoleIndex) {
                        if (m_haveXPosPattern)
                            xPos = xValueVar.toString().replace(m_xPosPattern, m_xPosReplace).toFloat();
                        else
                            xPos = xValueVar.toFloat();
                    } else {
                        xPos = oldItem->x();
                    }

                    if (m_haveYPosPattern)
                        yPos = yValueVar.toString().replace(m_yPosPattern, m_yPosReplace).toFloat();
                    else
                        yPos = yValueVar.toFloat();

                    if (m_zPosRole != noRoleIndex) {
                        if (m_haveZPosPattern)
                            zPos = zValueVar.toString().replace(m_zPosPattern, m_zPosReplace).toFloat();
                        else
                            zPos = zValueVar.toFloat();
                    } else {
                        zPos = oldItem->z();
                    }
                    item.setPosition(QVector3D(xPos, yPos, zPos));
                    m_proxy->setItem(i, j, item);
                }
            }
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/surfaceitemmodelhandler.cpp, line 21, as _ZN23SurfaceItemModelHandlerD0Ev
inline SurfaceItemModelHandler::~SurfaceItemModelHandler()
{
}

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

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 57, as _ZNK24AbstractItemModelHandler9itemModelEv
inline QAbstractItemModel *AbstractItemModelHandler::itemModel() const
{
    return m_itemModel.data();
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 8, as _ZN24AbstractItemModelHandlerC2EP7QObject
inline AbstractItemModelHandler::AbstractItemModelHandler(QObject *parent)
    : QObject(parent),
      resolvePending(0),
      m_fullReset(true)
{
    m_resolveTimer.setSingleShot(true);
    QObject::connect(&m_resolveTimer, &QTimer::timeout,
                     this, &AbstractItemModelHandler::handlePendingResolve);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 18, as _ZN24AbstractItemModelHandlerD2Ev
inline AbstractItemModelHandler::~AbstractItemModelHandler()
{
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

//  from ../qtdatavis3d/src/datavisualization/data/surfaceitemmodelhandler.cpp, line 8, as _ZN23SurfaceItemModelHandlerC1EP26QItemModelSurfaceDataProxyP7QObject
inline SurfaceItemModelHandler::SurfaceItemModelHandler(QItemModelSurfaceDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent),
      m_proxy(proxy),
      m_proxyArray(0),
      m_xPosRole(noRoleIndex),
      m_yPosRole(noRoleIndex),
      m_zPosRole(noRoleIndex),
      m_haveXPosPattern(false),
      m_haveYPosPattern(false),
      m_haveZPosPattern(false)
{
}
//  -----------------------------------------------------------------------

//  Only a class built on SurfaceItemModelHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnSurfaceItemModelHandler : SurfaceItemModelHandler {
  using SurfaceItemModelHandler::resolveModel;
};

//  A SurfaceItemModelHandler that Python can take functions over in. Every SurfaceItemModelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteSurfaceItemModelHandlerCall0)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall1)(const void *, QAbstractItemModel *, int *);
typedef void * (*CuteSurfaceItemModelHandlerCall2)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall3)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall4)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall5)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall6)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall7)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall9)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall10)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurfaceItemModelHandlerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurfaceItemModelHandlerCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSurfaceItemModelHandler : public SurfaceItemModelHandler {
public:
  using SurfaceItemModelHandler::SurfaceItemModelHandler;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12resolveModelEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24AbstractItemModelHandler9itemModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler16handleModelResetEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleMappingChangedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handlePendingResolveEv")) {
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

  //  void SurfaceItemModelHandler::resolveModel()
  void resolveModel() override {
    if (taken[0]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall0 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    SurfaceItemModelHandler::resolveModel();
  }

  //  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
  //      *itemModel)
  void setItemModel(QAbstractItemModel *itemModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall1 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall1>(taken[1]);
      call(this, itemModel, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::setItemModel(itemModel);
  }

  //  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
  QAbstractItemModel *itemModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall2 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall3 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall4 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall5 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall5>(taken[5]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleModelReset()
  void handleModelReset() override {
    if (taken[6]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall6 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall7 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall8 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall9 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall9>(taken[9]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleMappingChanged()
  void handleMappingChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall10 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleMappingChanged();
  }

  //  void AbstractItemModelHandler::handlePendingResolve()
  void handlePendingResolve() override {
    if (taken[11]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall11 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handlePendingResolve();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall12 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall12>(taken[12]);
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
      CuteSurfaceItemModelHandlerCall13 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall13>(taken[13]);
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
      CuteSurfaceItemModelHandlerCall14 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall14>(taken[14]);
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
      CuteSurfaceItemModelHandlerCall15 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall15>(taken[15]);
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
      CuteSurfaceItemModelHandlerCall16 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall16>(taken[16]);
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
      CuteSurfaceItemModelHandlerCall17 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall17>(taken[17]);
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
      CuteSurfaceItemModelHandlerCall18 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *SurfaceItemModelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23SurfaceItemModelHandler10metaObjectEv(
    const SurfaceItemModelHandler *self) {
  return self->metaObject();
}

//  void *SurfaceItemModelHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23SurfaceItemModelHandler11qt_metacastEPKc(
    SurfaceItemModelHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int SurfaceItemModelHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23SurfaceItemModelHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    SurfaceItemModelHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString SurfaceItemModelHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23SurfaceItemModelHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(SurfaceItemModelHandler::tr(s, c, n));
}

//  SurfaceItemModelHandler::SurfaceItemModelHandler(QItemModelSurfaceDataPro
//      xy *proxy, QObject *parent)
extern "C" Q_DECL_EXPORT
SurfaceItemModelHandler *ritual_ZN23SurfaceItemModelHandlerC1EP26QItemModelSurfaceDataProxyP7QObject(
    QItemModelSurfaceDataProxy *proxy,
    QObject *parent) {
  return new CuteSurfaceItemModelHandler(proxy, parent);
}

//  SurfaceItemModelHandler::~SurfaceItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SurfaceItemModelHandlerD1Ev(SurfaceItemModelHandler *self) {
  delete self;
}

//  void SurfaceItemModelHandler::handleDataChanged(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN23SurfaceItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE(
    SurfaceItemModelHandler *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight,
    const QList<int> *roles) {
  self->handleDataChanged(*topLeft, *bottomRight, *roles);
}

//  void SurfaceItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SurfaceItemModelHandler12resolveModelEv(
    SurfaceItemModelHandler *self) {
  self->resolveModel();
}

//  a Python function taken by a CuteSurfaceItemModelHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SurfaceItemModelHandler(
    SurfaceItemModelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteSurfaceItemModelHandler *>(self)->take(key, call);
}

//  void SurfaceItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23SurfaceItemModelHandler12resolveModelEv(
    SurfaceItemModelHandler *self) {
  static_cast<OwnSurfaceItemModelHandler *>(self)->OwnSurfaceItemModelHandler::resolveModel();
}
