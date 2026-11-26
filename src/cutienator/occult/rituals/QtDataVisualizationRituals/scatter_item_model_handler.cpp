//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/scatteritemmodelhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/scatteritemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/scatteritemmodelhandler_p.h>
#include <QtGui/qquaternion.h>
#include <QtDataVisualization/private/abstractitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 87, as local:scatteritemmodelhandler.cpp:toQuaternion
static inline QQuaternion toQuaternion(const QVariant &variant)
{
    if (variant.canConvert<QQuaternion>()) {
        return variant.value<QQuaternion>();
    } else if (variant.canConvert<QString>()) {
        QString s = variant.toString();
        if (!s.isEmpty()) {
            bool angleAndAxis = false;
            if (s.startsWith(QLatin1Char('@'))) {
                angleAndAxis = true;
                s = s.mid(1);
            }
            if (s.count(QLatin1Char(',')) == 3) {
                int index = s.indexOf(QLatin1Char(','));
                int index2 = s.indexOf(QLatin1Char(','), index + 1);
                int index3 = s.indexOf(QLatin1Char(','), index2 + 1);

                bool sGood, xGood, yGood, zGood;
                float sCoord = s.left(index).toFloat(&sGood);
                float xCoord = s.mid(index + 1, index2 - index - 1).toFloat(&xGood);
                float yCoord = s.mid(index2 + 1, index3 - index2 - 1).toFloat(&yGood);
                float zCoord = s.mid(index3 + 1).toFloat(&zGood);

                if (sGood && xGood && yGood && zGood) {
                    if (angleAndAxis)
                        return QQuaternion::fromAxisAndAngle(xCoord, yCoord, zCoord, sCoord);
                    else
                        return QQuaternion(sCoord, xCoord, yCoord, zCoord);
                }
            }
        }
    }
    return QQuaternion();
}

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 52, as _ZN23ScatterItemModelHandler18handleRowsInsertedERK11QModelIndexii
inline void ScatterItemModelHandler::handleRowsInserted(const QModelIndex &parent, int start, int end)
{
    // Do nothing if full reset already pending
    if (!m_fullReset) {
        if (!m_proxy->itemCount() || m_itemModel->columnCount() > 1) {
            // If inserting into an empty array, do full asynchronous reset to avoid multiple
            // separate inserts when initializing the model.
            // If the data model is multi-column, do full asynchronous reset to simplify things
            AbstractItemModelHandler::handleRowsInserted(parent, start, end);
        } else {
            QScatterDataArray array(end - start + 1);
            int count = 0;
            for (int i = start; i <= end; i++)
                modelPosToScatterItem(i, 0, array[count++]);

            m_proxy->insertItems(start, array);
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 72, as _ZN23ScatterItemModelHandler17handleRowsRemovedERK11QModelIndexii
inline void ScatterItemModelHandler::handleRowsRemoved(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);

    // Do nothing if full reset already pending
    if (!m_fullReset) {
        if (m_itemModel->columnCount() > 1) {
            // If the data model is multi-column, do full asynchronous reset to simplify things
            AbstractItemModelHandler::handleRowsRemoved(parent, start, end);
        } else {
            m_proxy->removeItems(start, end - start + 1);
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 172, as _ZN23ScatterItemModelHandler12resolveModelEv
inline void ScatterItemModelHandler::resolveModel()
{
    if (m_itemModel.isNull()) {
        m_proxy->resetArray(0);
        m_proxyArray = 0;
        return;
    }

    m_xPosPattern = m_proxy->xPosRolePattern();
    m_yPosPattern = m_proxy->yPosRolePattern();
    m_zPosPattern = m_proxy->zPosRolePattern();
    m_rotationPattern = m_proxy->rotationRolePattern();
    m_xPosReplace = m_proxy->xPosRoleReplace();
    m_yPosReplace = m_proxy->yPosRoleReplace();
    m_zPosReplace = m_proxy->zPosRoleReplace();
    m_rotationReplace = m_proxy->rotationRoleReplace();
    m_haveXPosPattern = !m_xPosPattern.namedCaptureGroups().isEmpty() && m_xPosPattern.isValid();
    m_haveYPosPattern = !m_yPosPattern.namedCaptureGroups().isEmpty() && m_yPosPattern.isValid();
    m_haveZPosPattern = !m_zPosPattern.namedCaptureGroups().isEmpty() && m_zPosPattern.isValid();
    m_haveRotationPattern = !m_rotationPattern.namedCaptureGroups().isEmpty() && m_rotationPattern.isValid();

    QHash<int, QByteArray> roleHash = m_itemModel->roleNames();
    m_xPosRole = roleHash.key(m_proxy->xPosRole().toLatin1(), noRoleIndex);
    m_yPosRole = roleHash.key(m_proxy->yPosRole().toLatin1(), noRoleIndex);
    m_zPosRole = roleHash.key(m_proxy->zPosRole().toLatin1(), noRoleIndex);
    m_rotationRole = roleHash.key(m_proxy->rotationRole().toLatin1(), noRoleIndex);
    const int columnCount = m_itemModel->columnCount();
    const int rowCount = m_itemModel->rowCount();
    const int totalCount = rowCount * columnCount;
    int runningCount = 0;

    // If dimensions have changed, recreate the array
    if (m_proxyArray != m_proxy->array() || totalCount != m_proxyArray->size())
        m_proxyArray = new QScatterDataArray(totalCount);

    // Parse data into newProxyArray
    for (int i = 0; i < rowCount; i++) {
        for (int j = 0; j < columnCount; j++) {
            modelPosToScatterItem(i, j, (*m_proxyArray)[runningCount]);
            runningCount++;
        }
    }

    m_proxy->resetArray(m_proxyArray);
}

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 122, as _ZN23ScatterItemModelHandler21modelPosToScatterItemEiiR16QScatterDataItem
inline void ScatterItemModelHandler::modelPosToScatterItem(int modelRow, int modelColumn,
                                                    QScatterDataItem &item)
{
    QModelIndex index = m_itemModel->index(modelRow, modelColumn);
    float xPos;
    float yPos;
    float zPos;
    if (m_xPosRole != noRoleIndex) {
        QVariant xValueVar = index.data(m_xPosRole);
        if (m_haveXPosPattern)
            xPos = xValueVar.toString().replace(m_xPosPattern, m_xPosReplace).toFloat();
        else
            xPos = xValueVar.toFloat();
    } else {
        xPos = 0.0f;
    }
    if (m_yPosRole != noRoleIndex) {
        QVariant yValueVar = index.data(m_yPosRole);
        if (m_haveYPosPattern)
            yPos = yValueVar.toString().replace(m_yPosPattern, m_yPosReplace).toFloat();
        else
            yPos = yValueVar.toFloat();
    } else {
        yPos = 0.0f;
    }
    if (m_zPosRole != noRoleIndex) {
        QVariant zValueVar = index.data(m_zPosRole);
        if (m_haveZPosPattern)
            zPos = zValueVar.toString().replace(m_zPosPattern, m_zPosReplace).toFloat();
        else
            zPos = zValueVar.toFloat();
    } else {
        zPos = 0.0f;
    }
    if (m_rotationRole != noRoleIndex) {
        QVariant rotationVar = index.data(m_rotationRole);
        if (m_haveRotationPattern) {
            item.setRotation(
                        toQuaternion(
                            QVariant(rotationVar.toString().replace(m_rotationPattern,
                                                                    m_rotationReplace))));
        } else {
            item.setRotation(toQuaternion(rotationVar));
        }
    }

    item.setPosition(QVector3D(xPos, yPos, zPos));
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
//  -----------------------------------------------------------------------

//  Only a class built on ScatterItemModelHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnScatterItemModelHandler : ScatterItemModelHandler {
  using ScatterItemModelHandler::resolveModel;
};

//  A ScatterItemModelHandler that Python can take functions over in. Every ScatterItemModelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteScatterItemModelHandlerCall0)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteScatterItemModelHandlerCall1)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteScatterItemModelHandlerCall2)(const void *, int *);
typedef void (*CuteScatterItemModelHandlerCall3)(const void *, QAbstractItemModel *, int *);
typedef void * (*CuteScatterItemModelHandlerCall4)(const void *, int *);
typedef void (*CuteScatterItemModelHandlerCall5)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteScatterItemModelHandlerCall6)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteScatterItemModelHandlerCall7)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteScatterItemModelHandlerCall8)(const void *, int *);
typedef void (*CuteScatterItemModelHandlerCall9)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteScatterItemModelHandlerCall10)(const void *, int *);
typedef void (*CuteScatterItemModelHandlerCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteScatterItemModelHandlerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteScatterItemModelHandlerCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterItemModelHandlerCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterItemModelHandlerCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterItemModelHandlerCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterItemModelHandlerCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterItemModelHandlerCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteScatterItemModelHandler : public ScatterItemModelHandler {
public:
  using ScatterItemModelHandler::ScatterItemModelHandler;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12resolveModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24AbstractItemModelHandler9itemModelEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler16handleModelResetEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i")) {
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

  //  void ScatterItemModelHandler::handleRowsInserted(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[0]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall0 call = reinterpret_cast<CuteScatterItemModelHandlerCall0>(taken[0]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    ScatterItemModelHandler::handleRowsInserted(parent, start, end);
  }

  //  void ScatterItemModelHandler::handleRowsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[1]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall1 call = reinterpret_cast<CuteScatterItemModelHandlerCall1>(taken[1]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    ScatterItemModelHandler::handleRowsRemoved(parent, start, end);
  }

  //  void ScatterItemModelHandler::resolveModel()
  void resolveModel() override {
    if (taken[2]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall2 call = reinterpret_cast<CuteScatterItemModelHandlerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    ScatterItemModelHandler::resolveModel();
  }

  //  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
  //      *itemModel)
  void setItemModel(QAbstractItemModel *itemModel) override {
    if (taken[3]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall3 call = reinterpret_cast<CuteScatterItemModelHandlerCall3>(taken[3]);
      call(this, itemModel, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::setItemModel(itemModel);
  }

  //  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
  QAbstractItemModel *itemModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall4 call = reinterpret_cast<CuteScatterItemModelHandlerCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall5 call = reinterpret_cast<CuteScatterItemModelHandlerCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall6 call = reinterpret_cast<CuteScatterItemModelHandlerCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall7 call = reinterpret_cast<CuteScatterItemModelHandlerCall7>(taken[7]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleModelReset()
  void handleModelReset() override {
    if (taken[8]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall8 call = reinterpret_cast<CuteScatterItemModelHandlerCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleModelReset();
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
    if (taken[9]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall9 call = reinterpret_cast<CuteScatterItemModelHandlerCall9>(taken[9]);
      call(this, &sourceParent, sourceStart, sourceEnd, &destinationParent, destinationRow, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsMoved(sourceParent, sourceStart, sourceEnd, destinationParent, destinationRow);
  }

  //  void AbstractItemModelHandler::handleMappingChanged()
  void handleMappingChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall10 call = reinterpret_cast<CuteScatterItemModelHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleMappingChanged();
  }

  //  void AbstractItemModelHandler::handlePendingResolve()
  void handlePendingResolve() override {
    if (taken[11]) {
      int handled = 0;
      CuteScatterItemModelHandlerCall11 call = reinterpret_cast<CuteScatterItemModelHandlerCall11>(taken[11]);
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
      CuteScatterItemModelHandlerCall12 call = reinterpret_cast<CuteScatterItemModelHandlerCall12>(taken[12]);
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
      CuteScatterItemModelHandlerCall13 call = reinterpret_cast<CuteScatterItemModelHandlerCall13>(taken[13]);
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
      CuteScatterItemModelHandlerCall14 call = reinterpret_cast<CuteScatterItemModelHandlerCall14>(taken[14]);
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
      CuteScatterItemModelHandlerCall15 call = reinterpret_cast<CuteScatterItemModelHandlerCall15>(taken[15]);
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
      CuteScatterItemModelHandlerCall16 call = reinterpret_cast<CuteScatterItemModelHandlerCall16>(taken[16]);
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
      CuteScatterItemModelHandlerCall17 call = reinterpret_cast<CuteScatterItemModelHandlerCall17>(taken[17]);
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
      CuteScatterItemModelHandlerCall18 call = reinterpret_cast<CuteScatterItemModelHandlerCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ScatterItemModelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23ScatterItemModelHandler10metaObjectEv(
    const ScatterItemModelHandler *self) {
  return self->metaObject();
}

//  void *ScatterItemModelHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23ScatterItemModelHandler11qt_metacastEPKc(
    ScatterItemModelHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ScatterItemModelHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23ScatterItemModelHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    ScatterItemModelHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  ScatterItemModelHandler::~ScatterItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23ScatterItemModelHandlerD1Ev(ScatterItemModelHandler *self) {
  delete self;
}

//  void ScatterItemModelHandler::handleDataChanged(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN23ScatterItemModelHandler17handleDataChangedERK11QModelIndexS2_RK5QListIiE(
    ScatterItemModelHandler *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight,
    const QList<int> *roles) {
  self->handleDataChanged(*topLeft, *bottomRight, *roles);
}

//  void ScatterItemModelHandler::handleRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN23ScatterItemModelHandler18handleRowsInsertedERK11QModelIndexii(
    ScatterItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleRowsInserted(*parent, start, end);
}

//  void ScatterItemModelHandler::handleRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN23ScatterItemModelHandler17handleRowsRemovedERK11QModelIndexii(
    ScatterItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->handleRowsRemoved(*parent, start, end);
}

//  void ScatterItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23ScatterItemModelHandler12resolveModelEv(
    ScatterItemModelHandler *self) {
  self->resolveModel();
}

//  a Python function taken by a CuteScatterItemModelHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ScatterItemModelHandler(
    ScatterItemModelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteScatterItemModelHandler *>(self)->take(key, call);
}

//  void ScatterItemModelHandler::handleRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23ScatterItemModelHandler18handleRowsInsertedERK11QModelIndexii(
    ScatterItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->ScatterItemModelHandler::handleRowsInserted(*parent, start, end);
}

//  void ScatterItemModelHandler::handleRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23ScatterItemModelHandler17handleRowsRemovedERK11QModelIndexii(
    ScatterItemModelHandler *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->ScatterItemModelHandler::handleRowsRemoved(*parent, start, end);
}

//  void ScatterItemModelHandler::resolveModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23ScatterItemModelHandler12resolveModelEv(
    ScatterItemModelHandler *self) {
  static_cast<OwnScatterItemModelHandler *>(self)->OwnScatterItemModelHandler::resolveModel();
}
