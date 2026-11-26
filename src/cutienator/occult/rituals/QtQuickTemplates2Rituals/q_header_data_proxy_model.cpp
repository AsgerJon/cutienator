//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtCore/qglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QPointer>
#include <QtCore/QAbstractItemModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickheaderview_p_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 392, as _ZNK21QHeaderDataProxyModel12variantValueEv
inline QVariant QHeaderDataProxyModel::variantValue() const
{
    return QVariant::fromValue(static_cast<QObject *>(const_cast<QHeaderDataProxyModel *>(this)));
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 406, as _ZNK21QHeaderDataProxyModel11orientationEv
inline Qt::Orientation QHeaderDataProxyModel::orientation() const
{
    return m_orientation;
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 397, as _ZN21QHeaderDataProxyModel14setOrientationEN2Qt11OrientationE
inline void QHeaderDataProxyModel::setOrientation(Qt::Orientation o)
{
    if (o == m_orientation)
        return;
    beginResetModel();
    m_orientation = o;
    endResetModel();
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 416, as _ZN21QHeaderDataProxyModel14connectToModelEv
inline void QHeaderDataProxyModel::connectToModel()
{
    if (m_model.isNull())
        return;
    connect(m_model, &QAbstractItemModel::headerDataChanged,
        this, [this](Qt::Orientation orient, int first, int last) {
            if (orient != orientation())
                return;
            if (orient == Qt::Horizontal) {
                emit dataChanged(createIndex(0, first), createIndex(0, last));
            } else {
                emit dataChanged(createIndex(first, 0), createIndex(last, 0));
            }
        });
    connect(m_model, &QAbstractItemModel::modelAboutToBeReset,
        this, &QHeaderDataProxyModel::modelAboutToBeReset, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::modelReset,
        this, &QHeaderDataProxyModel::modelReset, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsAboutToBeMoved,
        this, &QHeaderDataProxyModel::rowsAboutToBeMoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsMoved,
        this, &QHeaderDataProxyModel::rowsMoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsAboutToBeInserted,
        this, &QHeaderDataProxyModel::rowsAboutToBeInserted, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsInserted,
        this, &QHeaderDataProxyModel::rowsInserted, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsAboutToBeRemoved,
        this, &QHeaderDataProxyModel::rowsAboutToBeRemoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::rowsRemoved,
        this, &QHeaderDataProxyModel::rowsRemoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsAboutToBeMoved,
        this, &QHeaderDataProxyModel::columnsAboutToBeMoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsMoved,
        this, &QHeaderDataProxyModel::columnsMoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsAboutToBeInserted,
        this, &QHeaderDataProxyModel::columnsAboutToBeInserted, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsInserted,
        this, &QHeaderDataProxyModel::columnsInserted, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsAboutToBeRemoved,
        this, &QHeaderDataProxyModel::columnsAboutToBeRemoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::columnsRemoved,
        this, &QHeaderDataProxyModel::columnsRemoved, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::layoutAboutToBeChanged,
        this, &QHeaderDataProxyModel::layoutAboutToBeChanged, Qt::UniqueConnection);
    connect(m_model, &QAbstractItemModel::layoutChanged,
        this, &QHeaderDataProxyModel::layoutChanged, Qt::UniqueConnection);
}

//  from ../qtdeclarative/src/quicktemplates/qquickheaderview.cpp, line 464, as _ZN21QHeaderDataProxyModel19disconnectFromModelEv
inline void QHeaderDataProxyModel::disconnectFromModel()
{
    if (m_model.isNull())
        return;
    m_model->disconnect(this);
}
//  -----------------------------------------------------------------------

//  A QHeaderDataProxyModel that Python can take functions over in. Every QHeaderDataProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQHeaderDataProxyModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQHeaderDataProxyModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQHeaderDataProxyModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQHeaderDataProxyModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQHeaderDataProxyModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQHeaderDataProxyModelCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall6)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQHeaderDataProxyModelCall8)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall9)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall11)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall12)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQHeaderDataProxyModelCall13)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQHeaderDataProxyModelCall14)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall15)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall16)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall17)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall19)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall20)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQHeaderDataProxyModelCall21)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall22)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQHeaderDataProxyModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQHeaderDataProxyModelCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQHeaderDataProxyModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQHeaderDataProxyModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQHeaderDataProxyModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQHeaderDataProxyModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQHeaderDataProxyModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQHeaderDataProxyModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeaderDataProxyModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeaderDataProxyModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderDataProxyModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderDataProxyModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderDataProxyModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderDataProxyModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderDataProxyModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHeaderDataProxyModel : public QHeaderDataProxyModel {
public:
  using QHeaderDataProxyModel::QHeaderDataProxyModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QHeaderDataProxyModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall0 call = reinterpret_cast<CuteQHeaderDataProxyModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QHeaderDataProxyModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QHeaderDataProxyModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall1 call = reinterpret_cast<CuteQHeaderDataProxyModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QHeaderDataProxyModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QHeaderDataProxyModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall2 call = reinterpret_cast<CuteQHeaderDataProxyModelCall2>(taken[2]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QHeaderDataProxyModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QHeaderDataProxyModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall3 call = reinterpret_cast<CuteQHeaderDataProxyModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QHeaderDataProxyModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QHeaderDataProxyModel::columnCount(const QModelIndex &parent)
  //      const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall4 call = reinterpret_cast<CuteQHeaderDataProxyModelCall4>(taken[4]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QHeaderDataProxyModel::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QHeaderDataProxyModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall5 call = reinterpret_cast<CuteQHeaderDataProxyModelCall5>(taken[5]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QHeaderDataProxyModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QHeaderDataProxyModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall6 call = reinterpret_cast<CuteQHeaderDataProxyModelCall6>(taken[6]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QHeaderDataProxyModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QHeaderDataProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall7 call = reinterpret_cast<CuteQHeaderDataProxyModelCall7>(taken[7]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QHeaderDataProxyModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall8 call = reinterpret_cast<CuteQHeaderDataProxyModelCall8>(taken[8]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall9 call = reinterpret_cast<CuteQHeaderDataProxyModelCall9>(taken[9]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall10 call = reinterpret_cast<CuteQHeaderDataProxyModelCall10>(taken[10]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::clearItemData(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall11 call = reinterpret_cast<CuteQHeaderDataProxyModelCall11>(taken[11]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall12 call = reinterpret_cast<CuteQHeaderDataProxyModelCall12>(taken[12]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall13 call = reinterpret_cast<CuteQHeaderDataProxyModelCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall14 call = reinterpret_cast<CuteQHeaderDataProxyModelCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDragActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall15 call = reinterpret_cast<CuteQHeaderDataProxyModelCall15>(taken[15]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[16]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall16 call = reinterpret_cast<CuteQHeaderDataProxyModelCall16>(taken[16]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[17]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall17 call = reinterpret_cast<CuteQHeaderDataProxyModelCall17>(taken[17]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall18 call = reinterpret_cast<CuteQHeaderDataProxyModelCall18>(taken[18]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall19 call = reinterpret_cast<CuteQHeaderDataProxyModelCall19>(taken[19]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[20]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall20 call = reinterpret_cast<CuteQHeaderDataProxyModelCall20>(taken[20]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall21 call = reinterpret_cast<CuteQHeaderDataProxyModelCall21>(taken[21]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall22 call = reinterpret_cast<CuteQHeaderDataProxyModelCall22>(taken[22]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall23 call = reinterpret_cast<CuteQHeaderDataProxyModelCall23>(taken[23]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractItemModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[24]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall24 call = reinterpret_cast<CuteQHeaderDataProxyModelCall24>(taken[24]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall25 call = reinterpret_cast<CuteQHeaderDataProxyModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall26 call = reinterpret_cast<CuteQHeaderDataProxyModelCall26>(taken[26]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall27 call = reinterpret_cast<CuteQHeaderDataProxyModelCall27>(taken[27]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall28 call = reinterpret_cast<CuteQHeaderDataProxyModelCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[29]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall29 call = reinterpret_cast<CuteQHeaderDataProxyModelCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[30]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall30 call = reinterpret_cast<CuteQHeaderDataProxyModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall31 call = reinterpret_cast<CuteQHeaderDataProxyModelCall31>(taken[31]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall32 call = reinterpret_cast<CuteQHeaderDataProxyModelCall32>(taken[32]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall33 call = reinterpret_cast<CuteQHeaderDataProxyModelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall34 call = reinterpret_cast<CuteQHeaderDataProxyModelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall35 call = reinterpret_cast<CuteQHeaderDataProxyModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall36 call = reinterpret_cast<CuteQHeaderDataProxyModelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[37]) {
      int handled = 0;
      CuteQHeaderDataProxyModelCall37 call = reinterpret_cast<CuteQHeaderDataProxyModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHeaderDataProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QHeaderDataProxyModel10metaObjectEv(
    const QHeaderDataProxyModel *self) {
  return self->metaObject();
}

//  void *QHeaderDataProxyModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QHeaderDataProxyModel11qt_metacastEPKc(
    QHeaderDataProxyModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHeaderDataProxyModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QHeaderDataProxyModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QHeaderDataProxyModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHeaderDataProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QHeaderDataProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeaderDataProxyModel::tr(s, c, n));
}

//  QHeaderDataProxyModel::QHeaderDataProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QHeaderDataProxyModel *ritual_ZN21QHeaderDataProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQHeaderDataProxyModel(parent);
}

//  QHeaderDataProxyModel::~QHeaderDataProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHeaderDataProxyModelD1Ev(QHeaderDataProxyModel *self) {
  delete self;
}

//  void QHeaderDataProxyModel::setSourceModel(QAbstractItemModel
//      *newSourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHeaderDataProxyModel14setSourceModelEP18QAbstractItemModel(
    QHeaderDataProxyModel *self,
    QAbstractItemModel *newSourceModel) {
  self->setSourceModel(newSourceModel);
}

//  QPointer<QAbstractItemModel> QHeaderDataProxyModel::sourceModel() const
extern "C" Q_DECL_EXPORT
QPointer<QAbstractItemModel> *ritual_ZNK21QHeaderDataProxyModel11sourceModelEv(
    const QHeaderDataProxyModel *self) {
  return new QPointer<QAbstractItemModel>(self->sourceModel());
}

//  QModelIndex QHeaderDataProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QHeaderDataProxyModel5indexEiiRK11QModelIndex(
    const QHeaderDataProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QHeaderDataProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QHeaderDataProxyModel6parentERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QHeaderDataProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QHeaderDataProxyModel7siblingEiiRK11QModelIndex(
    const QHeaderDataProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  int QHeaderDataProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QHeaderDataProxyModel8rowCountERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QHeaderDataProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QHeaderDataProxyModel11columnCountERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QHeaderDataProxyModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QHeaderDataProxyModel4dataERK11QModelIndexi(
    const QHeaderDataProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QHeaderDataProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHeaderDataProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QHeaderDataProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QHeaderDataProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHeaderDataProxyModel11hasChildrenERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QHash<int, QByteArray> QHeaderDataProxyModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK21QHeaderDataProxyModel9roleNamesEv(
    const QHeaderDataProxyModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QHeaderDataProxyModel::variantValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QHeaderDataProxyModel12variantValueEv(
    const QHeaderDataProxyModel *self) {
  return new QVariant(self->variantValue());
}

//  Qt::Orientation QHeaderDataProxyModel::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK21QHeaderDataProxyModel11orientationEv(
    const QHeaderDataProxyModel *self) {
  return self->orientation();
}

//  void QHeaderDataProxyModel::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHeaderDataProxyModel14setOrientationEN2Qt11OrientationE(
    QHeaderDataProxyModel *self,
    Qt::Orientation o) {
  self->setOrientation(o);
}

//  void QHeaderDataProxyModel::connectToModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHeaderDataProxyModel14connectToModelEv(
    QHeaderDataProxyModel *self) {
  self->connectToModel();
}

//  void QHeaderDataProxyModel::disconnectFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHeaderDataProxyModel19disconnectFromModelEv(
    QHeaderDataProxyModel *self) {
  self->disconnectFromModel();
}

//  a Python function taken by a CuteQHeaderDataProxyModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeaderDataProxyModel(
    QHeaderDataProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeaderDataProxyModel *>(self)->take(key, call);
}

//  QModelIndex QHeaderDataProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QHeaderDataProxyModel5indexEiiRK11QModelIndex(
    const QHeaderDataProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QHeaderDataProxyModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QHeaderDataProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QHeaderDataProxyModel6parentERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QHeaderDataProxyModel::parent(*child));
}

//  QModelIndex QHeaderDataProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QHeaderDataProxyModel7siblingEiiRK11QModelIndex(
    const QHeaderDataProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QHeaderDataProxyModel::sibling(
          row,
          column,
          *idx));
}

//  int QHeaderDataProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QHeaderDataProxyModel8rowCountERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->QHeaderDataProxyModel::rowCount(*parent);
}

//  int QHeaderDataProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QHeaderDataProxyModel11columnCountERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->QHeaderDataProxyModel::columnCount(*parent);
}

//  QVariant QHeaderDataProxyModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QHeaderDataProxyModel4dataERK11QModelIndexi(
    const QHeaderDataProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QHeaderDataProxyModel::data(*index, role));
}

//  bool QHeaderDataProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QHeaderDataProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QHeaderDataProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QHeaderDataProxyModel::setData(*index, *value, role);
}

//  bool QHeaderDataProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QHeaderDataProxyModel11hasChildrenERK11QModelIndex(
    const QHeaderDataProxyModel *self,
    const QModelIndex *parent) {
  return self->QHeaderDataProxyModel::hasChildren(*parent);
}

//  a QPointer<QAbstractItemModel> a ritual of QHeaderDataProxyModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHeaderDataProxyModel__QPointer_QAbstractItemModel(
    QPointer<QAbstractItemModel> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_tableview)
