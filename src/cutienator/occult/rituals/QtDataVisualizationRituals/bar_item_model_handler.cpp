//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/baritemmodelhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/baritemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/baritemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/baritemmodelhandler.cpp, line 68, as _ZN19BarItemModelHandler12resolveModelEv
inline void BarItemModelHandler::resolveModel()
{
    if (m_itemModel.isNull()) {
        m_proxy->resetArray(0);
        return;
    }

    if (!m_proxy->useModelCategories()
            && (m_proxy->rowRole().isEmpty() || m_proxy->columnRole().isEmpty())) {
        m_proxy->resetArray(0);
        return;
    }

    // Value and rotation patterns can be reused on single item changes,
    // so store them to member variables.
    QRegularExpression rowPattern(m_proxy->rowRolePattern());
    QRegularExpression colPattern(m_proxy->columnRolePattern());
    m_valuePattern = m_proxy->valueRolePattern();
    m_rotationPattern = m_proxy->rotationRolePattern();
    QString rowReplace = m_proxy->rowRoleReplace();
    QString colReplace = m_proxy->columnRoleReplace();
    m_valueReplace = m_proxy->valueRoleReplace();
    m_rotationReplace = m_proxy->rotationRoleReplace();
    bool haveRowPattern = !rowPattern.namedCaptureGroups().isEmpty() && rowPattern.isValid();
    bool haveColPattern = !colPattern.namedCaptureGroups().isEmpty() && colPattern.isValid();
    m_haveValuePattern = !m_valuePattern.namedCaptureGroups().isEmpty() && m_valuePattern.isValid();
    m_haveRotationPattern = !m_rotationPattern.namedCaptureGroups().isEmpty() && m_rotationPattern.isValid();

    QStringList rowLabels;
    QStringList columnLabels;

    QHash<int, QByteArray> roleHash = m_itemModel->roleNames();

    // Default value role to display role if no mapping
    m_valueRole = roleHash.key(m_proxy->valueRole().toLatin1(), Qt::DisplayRole);
    m_rotationRole = roleHash.key(m_proxy->rotationRole().toLatin1(), noRoleIndex);
    int rowCount = m_itemModel->rowCount();
    int columnCount = m_itemModel->columnCount();

    if (m_proxy->useModelCategories()) {
        // If dimensions have changed, recreate the array
        if (m_proxyArray != m_proxy->array() || columnCount != m_columnCount
                || rowCount != m_proxyArray->size()) {
            m_proxyArray = new QBarDataArray;
            m_proxyArray->reserve(rowCount);
            for (int i = 0; i < rowCount; i++)
                m_proxyArray->append(new QBarDataRow(columnCount));
        }
        for (int i = 0; i < rowCount; i++) {
            QBarDataRow &newProxyRow = *m_proxyArray->at(i);
            for (int j = 0; j < columnCount; j++) {
                QModelIndex index = m_itemModel->index(i, j);
                QVariant valueVar = index.data(m_valueRole);
                float value;
                if (m_haveValuePattern)
                    value = valueVar.toString().replace(m_valuePattern, m_valueReplace).toFloat();
                else
                    value = valueVar.toFloat();
                newProxyRow[j].setValue(value);
                if (m_rotationRole != noRoleIndex) {
                    QVariant rotationVar = index.data(m_rotationRole);
                    float rotation;
                    if (m_haveRotationPattern) {
                        rotation = rotationVar.toString().replace(m_rotationPattern,
                                                                  m_rotationReplace).toFloat();
                    } else {
                        rotation = rotationVar.toFloat();
                    }
                    newProxyRow[j].setRotation(rotation);
                }
            }
        }
        // Generate labels from headers if using model rows/columns
        for (int i = 0; i < rowCount; i++)
            rowLabels << m_itemModel->headerData(i, Qt::Vertical).toString();
        for (int i = 0; i < columnCount; i++)
            columnLabels << m_itemModel->headerData(i, Qt::Horizontal).toString();
        m_columnCount = columnCount;
    } else {
        int rowRole = roleHash.key(m_proxy->rowRole().toLatin1());
        int columnRole = roleHash.key(m_proxy->columnRole().toLatin1());

        bool generateRows = m_proxy->autoRowCategories();
        bool generateColumns = m_proxy->autoColumnCategories();
        QStringList rowList;
        QStringList columnList;
        // For detecting duplicates in categories generation, using QHashes should be faster than
        // simple QStringList::contains() check.
        QHash<QString, bool> rowListHash;
        QHash<QString, bool> columnListHash;

        // Sort values into rows and columns
        typedef QHash<QString, float> ColumnValueMap;
        QHash<QString, ColumnValueMap> itemValueMap;
        QHash<QString, ColumnValueMap> itemRotationMap;

        bool cumulative = m_proxy->multiMatchBehavior() == QItemModelBarDataProxy::MMBAverage
                || m_proxy->multiMatchBehavior() == QItemModelBarDataProxy::MMBCumulative;
        bool countMatches = m_proxy->multiMatchBehavior() == QItemModelBarDataProxy::MMBAverage;
        bool takeFirst = m_proxy->multiMatchBehavior() == QItemModelBarDataProxy::MMBFirst;
        QHash<QString, QHash<QString, int> > *matchCountMap = 0;
        if (countMatches)
            matchCountMap = new QHash<QString, QHash<QString, int> >;

        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < columnCount; j++) {
                QModelIndex index = m_itemModel->index(i, j);
                QString rowRoleStr = index.data(rowRole).toString();
                if (haveRowPattern)
                    rowRoleStr.replace(rowPattern, rowReplace);
                QString columnRoleStr = index.data(columnRole).toString();
                if (haveColPattern)
                    columnRoleStr.replace(colPattern, colReplace);
                QVariant valueVar = index.data(m_valueRole);
                float value;
                if (m_haveValuePattern)
                    value = valueVar.toString().replace(m_valuePattern, m_valueReplace).toFloat();
                else
                    value = valueVar.toFloat();
                if (countMatches)
                    (*matchCountMap)[rowRoleStr][columnRoleStr]++;

                if (cumulative) {
                    itemValueMap[rowRoleStr][columnRoleStr] += value;
                } else {
                    if (takeFirst && itemValueMap.contains(rowRoleStr)) {
                        if (itemValueMap.value(rowRoleStr).contains(columnRoleStr))
                            continue; // We already have a value for this row/column combo
                    }
                    itemValueMap[rowRoleStr][columnRoleStr] = value;
                }

                if (m_rotationRole != noRoleIndex) {
                    QVariant rotationVar = index.data(m_rotationRole);
                    float rotation;
                    if (m_haveRotationPattern) {
                        rotation = rotationVar.toString().replace(m_rotationPattern,
                                                                  m_rotationReplace).toFloat();
                    } else {
                        rotation = rotationVar.toFloat();
                    }
                    if (cumulative) {
                        itemRotationMap[rowRoleStr][columnRoleStr] += rotation;
                    } else {
                        // We know we are in take last mode if we get here,
                        // as take first mode skips to next loop already earlier
                        itemRotationMap[rowRoleStr][columnRoleStr] = rotation;
                    }
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
        if (m_proxyArray != m_proxy->array() || columnList.size() != m_columnCount
                || rowList.size() != m_proxyArray->size()) {
            m_proxyArray = new QBarDataArray;
            m_proxyArray->reserve(rowList.size());
            for (int i = 0; i < rowList.size(); i++)
                m_proxyArray->append(new QBarDataRow(columnList.size()));
        }
        // Create new data array from itemValueMap
        for (int i = 0; i < rowList.size(); i++) {
            QString rowKey = rowList.at(i);
            QBarDataRow &newProxyRow = *m_proxyArray->at(i);
            for (int j = 0; j < columnList.size(); j++) {
                float value = itemValueMap[rowKey][columnList.at(j)];
                if (countMatches)
                    value /= float((*matchCountMap)[rowKey][columnList.at(j)]);
                newProxyRow[j].setValue(value);
                if (m_rotationRole != noRoleIndex) {
                    float angle = itemRotationMap[rowKey][columnList.at(j)];
                    if (countMatches)
                        angle /= float((*matchCountMap)[rowKey][columnList.at(j)]);
                    newProxyRow[j].setRotation(angle);
                }
            }
        }

        rowLabels = rowList;
        columnLabels = columnList;
        m_columnCount = columnList.size();

        delete matchCountMap;
    }

    m_proxy->resetArray(m_proxyArray, rowLabels, columnLabels);
}
//  -----------------------------------------------------------------------

//  Only a class built on BarItemModelHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnBarItemModelHandler : BarItemModelHandler {
  using BarItemModelHandler::resolveModel;
};

//  A BarItemModelHandler that Python can take functions over in. Every BarItemModelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteBarItemModelHandlerCall0)(const void *, int *);
typedef void (*CuteBarItemModelHandlerCall1)(const void *, QAbstractItemModel *, int *);
typedef void * (*CuteBarItemModelHandlerCall2)(const void *, int *);
typedef void (*CuteBarItemModelHandlerCall3)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteBarItemModelHandlerCall4)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteBarItemModelHandlerCall5)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteBarItemModelHandlerCall6)(const void *, int *);
typedef void (*CuteBarItemModelHandlerCall7)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteBarItemModelHandlerCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteBarItemModelHandlerCall9)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteBarItemModelHandlerCall10)(const void *, int *);
typedef void (*CuteBarItemModelHandlerCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarItemModelHandlerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarItemModelHandlerCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarItemModelHandlerCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarItemModelHandlerCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarItemModelHandlerCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarItemModelHandlerCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarItemModelHandlerCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBarItemModelHandler : public BarItemModelHandler {
public:
  using BarItemModelHandler::BarItemModelHandler;
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

  //  void BarItemModelHandler::resolveModel()
  void resolveModel() override {
    if (taken[0]) {
      int handled = 0;
      CuteBarItemModelHandlerCall0 call = reinterpret_cast<CuteBarItemModelHandlerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    BarItemModelHandler::resolveModel();
  }

  //  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
  //      *itemModel)
  void setItemModel(QAbstractItemModel *itemModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteBarItemModelHandlerCall1 call = reinterpret_cast<CuteBarItemModelHandlerCall1>(taken[1]);
      call(this, itemModel, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::setItemModel(itemModel);
  }

  //  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
  QAbstractItemModel *itemModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteBarItemModelHandlerCall2 call = reinterpret_cast<CuteBarItemModelHandlerCall2>(taken[2]);
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
      CuteBarItemModelHandlerCall3 call = reinterpret_cast<CuteBarItemModelHandlerCall3>(taken[3]);
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
      CuteBarItemModelHandlerCall4 call = reinterpret_cast<CuteBarItemModelHandlerCall4>(taken[4]);
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
      CuteBarItemModelHandlerCall5 call = reinterpret_cast<CuteBarItemModelHandlerCall5>(taken[5]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleModelReset()
  void handleModelReset() override {
    if (taken[6]) {
      int handled = 0;
      CuteBarItemModelHandlerCall6 call = reinterpret_cast<CuteBarItemModelHandlerCall6>(taken[6]);
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
      CuteBarItemModelHandlerCall7 call = reinterpret_cast<CuteBarItemModelHandlerCall7>(taken[7]);
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
      CuteBarItemModelHandlerCall8 call = reinterpret_cast<CuteBarItemModelHandlerCall8>(taken[8]);
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
      CuteBarItemModelHandlerCall9 call = reinterpret_cast<CuteBarItemModelHandlerCall9>(taken[9]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleMappingChanged()
  void handleMappingChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteBarItemModelHandlerCall10 call = reinterpret_cast<CuteBarItemModelHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleMappingChanged();
  }

  //  void AbstractItemModelHandler::handlePendingResolve()
  void handlePendingResolve() override {
    if (taken[11]) {
      int handled = 0;
      CuteBarItemModelHandlerCall11 call = reinterpret_cast<CuteBarItemModelHandlerCall11>(taken[11]);
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
      CuteBarItemModelHandlerCall12 call = reinterpret_cast<CuteBarItemModelHandlerCall12>(taken[12]);
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
      CuteBarItemModelHandlerCall13 call = reinterpret_cast<CuteBarItemModelHandlerCall13>(taken[13]);
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
      CuteBarItemModelHandlerCall14 call = reinterpret_cast<CuteBarItemModelHandlerCall14>(taken[14]);
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
      CuteBarItemModelHandlerCall15 call = reinterpret_cast<CuteBarItemModelHandlerCall15>(taken[15]);
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
      CuteBarItemModelHandlerCall16 call = reinterpret_cast<CuteBarItemModelHandlerCall16>(taken[16]);
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
      CuteBarItemModelHandlerCall17 call = reinterpret_cast<CuteBarItemModelHandlerCall17>(taken[17]);
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
      CuteBarItemModelHandlerCall18 call = reinterpret_cast<CuteBarItemModelHandlerCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BarItemModelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19BarItemModelHandler10metaObjectEv(
    const BarItemModelHandler *self) {
  return self->metaObject();
}

//  void *BarItemModelHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19BarItemModelHandler11qt_metacastEPKc(
    BarItemModelHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int BarItemModelHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19BarItemModelHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    BarItemModelHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  BarItemModelHandler::~BarItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19BarItemModelHandlerD1Ev(BarItemModelHandler *self) {
  delete self;
}

//  void BarItemModelHandler::handleDataChanged(const QModelIndex &topLeft,
//      const QModelIndex &bottomRight, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN19BarItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE(
    BarItemModelHandler *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight,
    const QList<int> *roles) {
  self->handleDataChanged(*topLeft, *bottomRight, *roles);
}

//  void BarItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19BarItemModelHandler12resolveModelEv(
    BarItemModelHandler *self) {
  self->resolveModel();
}

//  a Python function taken by a CuteBarItemModelHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BarItemModelHandler(
    BarItemModelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteBarItemModelHandler *>(self)->take(key, call);
}

//  void BarItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19BarItemModelHandler12resolveModelEv(
    BarItemModelHandler *self) {
  static_cast<OwnBarItemModelHandler *>(self)->OwnBarItemModelHandler::resolveModel();
}
