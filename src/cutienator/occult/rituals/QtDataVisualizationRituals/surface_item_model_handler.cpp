//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/surfaceitemmodelhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/surfaceitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  SurfaceItemModelHandler::~SurfaceItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SurfaceItemModelHandlerD1Ev(SurfaceItemModelHandler *self) {
  delete self;
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
