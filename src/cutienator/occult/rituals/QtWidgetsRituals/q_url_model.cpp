//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include "qsidebar_p.h"
#include <qaction.h>
#include <qurl.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <qmimedata.h>
#include <qevent.h>
#include <qdebug.h>
#include <qfilesystemmodel.h>
#include <qabstractfileiconprovider.h>
#include <qfiledialog.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/dialogs/qsidebar.cpp, line 47, as _ZN9QUrlModelD1Ev
inline QUrlModel::~QUrlModel()
{
    for (auto &conn : modelConnections)
        disconnect(conn);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 91, as _ZNK9QUrlModel8mimeDataERK5QListI11QModelIndexE
inline QMimeData *QUrlModel::mimeData(const QModelIndexList &indexes) const
{
    QList<QUrl> list;
    for (const auto &index : indexes) {
        if (index.column() == 0)
           list.append(index.data(UrlRole).toUrl());
    }
    QMimeData *data = new QMimeData();
    data->setUrls(list);
    return data;
}

//  from src/widgets/dialogs/qsidebar.cpp, line 73, as _ZNK9QUrlModel5flagsERK11QModelIndex
inline Qt::ItemFlags QUrlModel::flags(const QModelIndex &index) const
{
    Qt::ItemFlags flags = QStandardItemModel::flags(index);
    if (index.isValid()) {
        flags &= ~Qt::ItemIsEditable;
        // ### some future version could support "moving" urls onto a folder
        flags &= ~Qt::ItemIsDropEnabled;
    }

    if (index.data(Qt::DecorationRole).isNull())
        flags &= ~Qt::ItemIsEnabled;

    return flags;
}

//  from src/widgets/dialogs/qsidebar.cpp, line 146, as _ZN9QUrlModel7setDataERK11QModelIndexRK8QVarianti
inline bool QUrlModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (value.userType() == QMetaType::QUrl) {
        QUrl url = value.toUrl();
        QModelIndex dirIndex = fileSystemModel->index(url.toLocalFile());
        //On windows the popup display the "C:\", convert to nativeSeparators
        if (showFullPath)
            QStandardItemModel::setData(index, QDir::toNativeSeparators(fileSystemModel->data(dirIndex, QFileSystemModel::FilePathRole).toString()));
        else {
            QStandardItemModel::setData(index, QDir::toNativeSeparators(fileSystemModel->data(dirIndex, QFileSystemModel::FilePathRole).toString()), Qt::ToolTipRole);
            QStandardItemModel::setData(index, fileSystemModel->data(dirIndex).toString());
        }
        QStandardItemModel::setData(index, fileSystemModel->data(dirIndex, Qt::DecorationRole),
                                               Qt::DecorationRole);
        QStandardItemModel::setData(index, url, UrlRole);
        return true;
    }
    return QStandardItemModel::setData(index, value, role);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 273, as _ZNK9QUrlModel4urlsEv
inline QList<QUrl> QUrlModel::urls() const
{
    QList<QUrl> list;
    const int numRows = rowCount();
    list.reserve(numRows);
    for (int i = 0; i < numRows; ++i)
        list.append(data(index(i, 0), UrlRole).toUrl());
    return list;
}

//  from src/widgets/dialogs/qsidebar.cpp, line 312, as _ZN9QUrlModel11dataChangedERK11QModelIndexS2_
inline void QUrlModel::dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight)
{
    QModelIndex parent = topLeft.parent();
    for (int i = 0; i < watching.size(); ++i) {
        QModelIndex index = watching.at(i).index;
        if (index.model() && topLeft.model()) {
            Q_ASSERT(index.model() == topLeft.model());
        }
        if (   index.row() >= topLeft.row()
            && index.row() <= bottomRight.row()
            && index.column() >= topLeft.column()
            && index.column() <= bottomRight.column()
            && index.parent() == parent) {
                changed(watching.at(i).path);
        }
    }
}

//  from src/widgets/dialogs/qsidebar.cpp, line 333, as _ZN9QUrlModel13layoutChangedEv
inline void QUrlModel::layoutChanged()
{
    QStringList paths;
    paths.reserve(watching.size());
    for (const WatchItem &item : std::as_const(watching))
        paths.append(item.path);
    watching.clear();
    for (const auto &path : paths) {
        QModelIndex newIndex = fileSystemModel->index(path);
        watching.append({newIndex, path});
        if (newIndex.isValid())
            changed(path);
     }
}

//  from src/widgets/dialogs/qsidebar.cpp, line 166, as _ZN9QUrlModel6setUrlERK11QModelIndexRK4QUrlS2_
inline void QUrlModel::setUrl(const QModelIndex &index, const QUrl &url, const QModelIndex &dirIndex)
{
    setData(index, url, UrlRole);
    if (url.path().isEmpty()) {
        setData(index, fileSystemModel->myComputer());
        setData(index, fileSystemModel->myComputer(Qt::DecorationRole), Qt::DecorationRole);
    } else {
        QString newName;
        if (showFullPath) {
            //On windows the popup display the "C:\", convert to nativeSeparators
            newName = QDir::toNativeSeparators(dirIndex.data(QFileSystemModel::FilePathRole).toString());
        } else {
            newName = dirIndex.data().toString();
        }

        QIcon newIcon = qvariant_cast<QIcon>(dirIndex.data(Qt::DecorationRole));
        if (!dirIndex.isValid()) {
            const QAbstractFileIconProvider *provider = fileSystemModel->iconProvider();
            if (provider)
                newIcon = provider->icon(QAbstractFileIconProvider::Folder);
            newName = QFileInfo(url.toLocalFile()).fileName();
            if (!invalidUrls.contains(url))
                invalidUrls.append(url);
            //The bookmark is invalid then we set to false the EnabledRole
            setData(index, false, EnabledRole);
        } else {
            //The bookmark is valid then we set to true the EnabledRole
            setData(index, true, EnabledRole);
        }

        // newIcon could be null if fileSystemModel->iconProvider() returns null
        if (!newIcon.isNull()) {
        // Make sure that we have at least 32x32 images
            const QSize size = newIcon.actualSize(QSize(32,32));
            if (size.width() < 32) {
                const auto widget = qobject_cast<QWidget *>(parent());
                const auto dpr = widget ? widget->devicePixelRatio() : qApp->devicePixelRatio();
                const auto smallPixmap = newIcon.pixmap(QSize(32, 32), dpr);
                const auto newPixmap = smallPixmap.scaledToWidth(32 * dpr, Qt::SmoothTransformation);
                newIcon.addPixmap(newPixmap);
            }
        }

        if (index.data().toString() != newName)
            setData(index, newName);
        QIcon oldIcon = qvariant_cast<QIcon>(index.data(Qt::DecorationRole));
        if (oldIcon.cacheKey() != newIcon.cacheKey())
            setData(index, newIcon, Qt::DecorationRole);
    }
}

//  from src/widgets/dialogs/qsidebar.cpp, line 353, as _ZN9QUrlModel7changedERK7QString
inline void QUrlModel::changed(const QString &path)
{
    for (int i = 0; i < rowCount(); ++i) {
        QModelIndex idx = index(i, 0);
        if (idx.data(UrlRole).toUrl().toLocalFile() == path) {
            setData(idx, idx.data(UrlRole).toUrl());
        }
    }
}
//  -----------------------------------------------------------------------

//  A QUrlModel that Python can take functions over in. Every QUrlModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQUrlModelCall0)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQUrlModelCall1)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall2)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef const QModelIndex * (*CuteQUrlModelCall3)(const void *, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQUrlModelCall4)(const void *, const QModelIndex *, int *);
typedef int (*CuteQUrlModelCall5)(const void *, const QModelIndex *, int *);
typedef int (*CuteQUrlModelCall6)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall7)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQUrlModelCall8)(const void *, const QModelIndex *, int, int *);
typedef void (*CuteQUrlModelCall9)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef bool (*CuteQUrlModelCall10)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQUrlModelCall11)(const void *, int, int, int, int *);
typedef bool (*CuteQUrlModelCall12)(const void *, int, int, const QVariant *, int, int *);
typedef bool (*CuteQUrlModelCall13)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall14)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall15)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall16)(const void *, int, int, const QModelIndex *, int *);
typedef int (*CuteQUrlModelCall17)(const void *, int *);
typedef void (*CuteQUrlModelCall18)(const void *, int, int, int *);
typedef const QModelIndex * (*CuteQUrlModelCall19)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQUrlModelCall21)(const void *, int *);
typedef bool (*CuteQUrlModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQUrlModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteQUrlModelCall24)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall25)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQUrlModelCall26)(const void *, const QModelIndex *, int *);
typedef const QSize * (*CuteQUrlModelCall27)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQUrlModelCall28)(const void *, int *);
typedef void (*CuteQUrlModelCall29)(const void *, int *);
typedef void (*CuteQUrlModelCall30)(const void *, int *);
typedef bool (*CuteQUrlModelCall31)(const void *, QEvent *, int *);
typedef bool (*CuteQUrlModelCall32)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQUrlModelCall33)(const void *, QTimerEvent *, int *);
typedef void (*CuteQUrlModelCall34)(const void *, QChildEvent *, int *);
typedef void (*CuteQUrlModelCall35)(const void *, QEvent *, int *);
typedef void (*CuteQUrlModelCall36)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQUrlModelCall37)(const void *, const QMetaMethod *, int *);
class CuteQUrlModel : public QUrlModel {
public:
  using QUrlModel::QUrlModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[37] = call;
      return true;
    }
    return false;
  }

  //  bool QUrlModel::dropMimeData(const QMimeData *data, Qt::DropAction
  //      action, int row, int column, const QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUrlModelCall0 call = reinterpret_cast<CuteQUrlModelCall0>(taken[0]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QUrlModel::dropMimeData(data, action, row, column, parent);
  }

  //  Qt::ItemFlags QUrlModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUrlModelCall1 call = reinterpret_cast<CuteQUrlModelCall1>(taken[1]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QUrlModel::flags(index);
  }

  //  bool QUrlModel::setData(const QModelIndex &index, const QVariant
  //      &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[2]) {
      int handled = 0;
      CuteQUrlModelCall2 call = reinterpret_cast<CuteQUrlModelCall2>(taken[2]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QUrlModel::setData(index, value, role);
  }

  //  QModelIndex QStandardItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQUrlModelCall3 call = reinterpret_cast<CuteQUrlModelCall3>(taken[3]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::index(row, column, parent);
  }

  //  QModelIndex QStandardItemModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQUrlModelCall4 call = reinterpret_cast<CuteQUrlModelCall4>(taken[4]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::parent(child);
  }

  //  int QStandardItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQUrlModelCall5 call = reinterpret_cast<CuteQUrlModelCall5>(taken[5]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::rowCount(parent);
  }

  //  int QStandardItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQUrlModelCall6 call = reinterpret_cast<CuteQUrlModelCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::columnCount(parent);
  }

  //  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQUrlModelCall7 call = reinterpret_cast<CuteQUrlModelCall7>(taken[7]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::hasChildren(parent);
  }

  //  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQUrlModelCall8 call = reinterpret_cast<CuteQUrlModelCall8>(taken[8]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::data(index, role);
  }

  //  void QStandardItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQUrlModelCall9 call = reinterpret_cast<CuteQUrlModelCall9>(taken[9]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QStandardItemModel::multiData(index, roleDataSpan);
  }

  //  bool QStandardItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQUrlModelCall10 call = reinterpret_cast<CuteQUrlModelCall10>(taken[10]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::clearItemData(index);
  }

  //  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQUrlModelCall11 call = reinterpret_cast<CuteQUrlModelCall11>(taken[11]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::headerData(section, orientation, role);
  }

  //  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[12]) {
      int handled = 0;
      CuteQUrlModelCall12 call = reinterpret_cast<CuteQUrlModelCall12>(taken[12]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::setHeaderData(section, orientation, value, role);
  }

  //  bool QStandardItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQUrlModelCall13 call = reinterpret_cast<CuteQUrlModelCall13>(taken[13]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertRows(row, count, parent);
  }

  //  bool QStandardItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQUrlModelCall14 call = reinterpret_cast<CuteQUrlModelCall14>(taken[14]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertColumns(column, count, parent);
  }

  //  bool QStandardItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQUrlModelCall15 call = reinterpret_cast<CuteQUrlModelCall15>(taken[15]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeRows(row, count, parent);
  }

  //  bool QStandardItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[16]) {
      int handled = 0;
      CuteQUrlModelCall16 call = reinterpret_cast<CuteQUrlModelCall16>(taken[16]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeColumns(column, count, parent);
  }

  //  Qt::DropActions QStandardItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQUrlModelCall17 call = reinterpret_cast<CuteQUrlModelCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QStandardItemModel::supportedDropActions();
  }

  //  void QStandardItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[18]) {
      int handled = 0;
      CuteQUrlModelCall18 call = reinterpret_cast<CuteQUrlModelCall18>(taken[18]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QStandardItemModel::sort(column, order);
  }

  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQUrlModelCall19 call = reinterpret_cast<CuteQUrlModelCall19>(taken[19]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }

  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQUrlModelCall20 call = reinterpret_cast<CuteQUrlModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }

  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQUrlModelCall21 call = reinterpret_cast<CuteQUrlModelCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDragActions();
  }

  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[22]) {
      int handled = 0;
      CuteQUrlModelCall22 call = reinterpret_cast<CuteQUrlModelCall22>(taken[22]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }

  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[23]) {
      int handled = 0;
      CuteQUrlModelCall23 call = reinterpret_cast<CuteQUrlModelCall23>(taken[23]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[24]) {
      int handled = 0;
      CuteQUrlModelCall24 call = reinterpret_cast<CuteQUrlModelCall24>(taken[24]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }

  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQUrlModelCall25 call = reinterpret_cast<CuteQUrlModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }

  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQUrlModelCall26 call = reinterpret_cast<CuteQUrlModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }

  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQUrlModelCall27 call = reinterpret_cast<CuteQUrlModelCall27>(taken[27]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }

  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQUrlModelCall28 call = reinterpret_cast<CuteQUrlModelCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }

  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[29]) {
      int handled = 0;
      CuteQUrlModelCall29 call = reinterpret_cast<CuteQUrlModelCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[30]) {
      int handled = 0;
      CuteQUrlModelCall30 call = reinterpret_cast<CuteQUrlModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQUrlModelCall31 call = reinterpret_cast<CuteQUrlModelCall31>(taken[31]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQUrlModelCall32 call = reinterpret_cast<CuteQUrlModelCall32>(taken[32]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQUrlModelCall33 call = reinterpret_cast<CuteQUrlModelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQUrlModelCall34 call = reinterpret_cast<CuteQUrlModelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQUrlModelCall35 call = reinterpret_cast<CuteQUrlModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQUrlModelCall36 call = reinterpret_cast<CuteQUrlModelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[37]) {
      int handled = 0;
      CuteQUrlModelCall37 call = reinterpret_cast<CuteQUrlModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QUrlModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QUrlModel10metaObjectEv(
    const QUrlModel *self) {
  return self->metaObject();
}

//  QUrlModel::~QUrlModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModelD1Ev(QUrlModel *self) {
  delete self;
}

//  QMimeData *QUrlModel::mimeData(const QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK9QUrlModel8mimeDataERK5QListI11QModelIndexE(
    const QUrlModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  Qt::ItemFlags QUrlModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QUrlModel5flagsERK11QModelIndex(
    const QUrlModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  bool QUrlModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QUrlModel7setDataERK11QModelIndexRK8QVarianti(
    QUrlModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QList<QUrl> QUrlModel::urls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK9QUrlModel4urlsEv(const QUrlModel *self) {
  return new QList<QUrl>(self->urls());
}

//  void QUrlModel::dataChanged(const QModelIndex &topLeft, const QModelIndex
//      &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel11dataChangedERK11QModelIndexS2_(
    QUrlModel *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->dataChanged(*topLeft, *bottomRight);
}

//  void QUrlModel::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel13layoutChangedEv(QUrlModel *self) {
  self->layoutChanged();
}

//  void QUrlModel::setUrl(const QModelIndex &index, const QUrl &url, const
//      QModelIndex &dirIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel6setUrlERK11QModelIndexRK4QUrlS2_(
    QUrlModel *self,
    const QModelIndex *index,
    const QUrl *url,
    const QModelIndex *dirIndex) {
  self->setUrl(*index, *url, *dirIndex);
}

//  void QUrlModel::changed(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel7changedERK7QString(
    QUrlModel *self,
    const QString *path) {
  self->changed(*path);
}

//  a Python function taken by a CuteQUrlModel, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUrlModel(QUrlModel *self, const char *key, void *call) {
  return static_cast<CuteQUrlModel *>(self)->take(key, call);
}

//  Qt::ItemFlags QUrlModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QUrlModel5flagsERK11QModelIndex(
    const QUrlModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QUrlModel::flags(*index).toInt());
}

//  bool QUrlModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QUrlModel7setDataERK11QModelIndexRK8QVarianti(
    QUrlModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QUrlModel::setData(*index, *value, role);
}
