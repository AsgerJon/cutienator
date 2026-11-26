//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfilesystemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(filesystemmodel)
#if QT_CONFIG(filesystemmodel)
#include <QtGui/qfilesystemmodel.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdir.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QFile>
#include <QtCore/QModelIndex>

//  Only a class built on QFileSystemModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileSystemModel : QFileSystemModel {
  using QFileSystemModel::timerEvent;
  using QFileSystemModel::event;
};

//  A QFileSystemModel that Python can take functions over in. Every QFileSystemModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef const QModelIndex * (*CuteQFileSystemModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef const QModelIndex * (*CuteQFileSystemModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef const QModelIndex * (*CuteQFileSystemModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileSystemModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileSystemModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef void (*CuteQFileSystemModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef int (*CuteQFileSystemModelCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef int (*CuteQFileSystemModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef const QVariant * (*CuteQFileSystemModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileSystemModelCall9)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef const QVariant * (*CuteQFileSystemModelCall10)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef int (*CuteQFileSystemModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef void (*CuteQFileSystemModelCall12)(const void *, int, int, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileSystemModelCall13)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
typedef int (*CuteQFileSystemModelCall14)(const void *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
typedef void (*CuteQFileSystemModelCall15)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileSystemModelCall16)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall17)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall18)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall19)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQFileSystemModelCall20)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall25)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall26)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQFileSystemModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQFileSystemModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQFileSystemModelCall29)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQFileSystemModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQFileSystemModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQFileSystemModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSystemModelCall33)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileSystemModel : public QFileSystemModel {
public:
  using QFileSystemModel::QFileSystemModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
#if QT_CONFIG(filesystemmodel)
  //  QModelIndex QFileSystemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileSystemModelCall0 call = reinterpret_cast<CuteQFileSystemModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QFileSystemModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  QModelIndex QFileSystemModel::parent(const QModelIndex &child) const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileSystemModelCall1 call = reinterpret_cast<CuteQFileSystemModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QFileSystemModel::parent(child);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  QModelIndex QFileSystemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileSystemModelCall2 call = reinterpret_cast<CuteQFileSystemModelCall2>(taken[2]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QFileSystemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileSystemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileSystemModelCall3 call = reinterpret_cast<CuteQFileSystemModelCall3>(taken[3]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileSystemModel::canFetchMore(const QModelIndex &parent) const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileSystemModelCall4 call = reinterpret_cast<CuteQFileSystemModelCall4>(taken[4]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  void QFileSystemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileSystemModelCall5 call = reinterpret_cast<CuteQFileSystemModelCall5>(taken[5]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QFileSystemModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  int QFileSystemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileSystemModelCall6 call = reinterpret_cast<CuteQFileSystemModelCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::rowCount(parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  int QFileSystemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileSystemModelCall7 call = reinterpret_cast<CuteQFileSystemModelCall7>(taken[7]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::columnCount(parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  QVariant QFileSystemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileSystemModelCall8 call = reinterpret_cast<CuteQFileSystemModelCall8>(taken[8]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QFileSystemModel::data(index, role);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileSystemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileSystemModelCall9 call = reinterpret_cast<CuteQFileSystemModelCall9>(taken[9]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  QVariant QFileSystemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileSystemModelCall10 call = reinterpret_cast<CuteQFileSystemModelCall10>(taken[10]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QFileSystemModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  Qt::ItemFlags QFileSystemModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFileSystemModelCall11 call = reinterpret_cast<CuteQFileSystemModelCall11>(taken[11]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QFileSystemModel::flags(index);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  void QFileSystemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFileSystemModelCall12 call = reinterpret_cast<CuteQFileSystemModelCall12>(taken[12]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QFileSystemModel::sort(column, order);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileSystemModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFileSystemModelCall13 call = reinterpret_cast<CuteQFileSystemModelCall13>(taken[13]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filesystemmodel)
  //  Qt::DropActions QFileSystemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFileSystemModelCall14 call = reinterpret_cast<CuteQFileSystemModelCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QFileSystemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
  //  void QFileSystemModel::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFileSystemModelCall15 call = reinterpret_cast<CuteQFileSystemModelCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QFileSystemModel::timerEvent(event);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileSystemModel::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileSystemModelCall16 call = reinterpret_cast<CuteQFileSystemModelCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QFileSystemModel::event(event);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileSystemModelCall17 call = reinterpret_cast<CuteQFileSystemModelCall17>(taken[17]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileSystemModelCall18 call = reinterpret_cast<CuteQFileSystemModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQFileSystemModelCall19 call = reinterpret_cast<CuteQFileSystemModelCall19>(taken[19]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFileSystemModelCall20 call = reinterpret_cast<CuteQFileSystemModelCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQFileSystemModelCall21 call = reinterpret_cast<CuteQFileSystemModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQFileSystemModelCall22 call = reinterpret_cast<CuteQFileSystemModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQFileSystemModelCall23 call = reinterpret_cast<CuteQFileSystemModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQFileSystemModelCall24 call = reinterpret_cast<CuteQFileSystemModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQFileSystemModelCall25 call = reinterpret_cast<CuteQFileSystemModelCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQFileSystemModelCall26 call = reinterpret_cast<CuteQFileSystemModelCall26>(taken[26]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQFileSystemModelCall27 call = reinterpret_cast<CuteQFileSystemModelCall27>(taken[27]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQFileSystemModelCall28 call = reinterpret_cast<CuteQFileSystemModelCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQFileSystemModelCall29 call = reinterpret_cast<CuteQFileSystemModelCall29>(taken[29]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[30]) {
      int handled = 0;
      CuteQFileSystemModelCall30 call = reinterpret_cast<CuteQFileSystemModelCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[31]) {
      int handled = 0;
      CuteQFileSystemModelCall31 call = reinterpret_cast<CuteQFileSystemModelCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[32]) {
      int handled = 0;
      CuteQFileSystemModelCall32 call = reinterpret_cast<CuteQFileSystemModelCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFileSystemModelCall33 call = reinterpret_cast<CuteQFileSystemModelCall33>(taken[33]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQFileSystemModelCall34 call = reinterpret_cast<CuteQFileSystemModelCall34>(taken[34]);
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
      CuteQFileSystemModelCall35 call = reinterpret_cast<CuteQFileSystemModelCall35>(taken[35]);
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
      CuteQFileSystemModelCall36 call = reinterpret_cast<CuteQFileSystemModelCall36>(taken[36]);
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
      CuteQFileSystemModelCall37 call = reinterpret_cast<CuteQFileSystemModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileSystemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QFileSystemModel10metaObjectEv(
    const QFileSystemModel *self) {
  return self->metaObject();
}

//  void *QFileSystemModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QFileSystemModel11qt_metacastEPKc(
    QFileSystemModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QFileSystemModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QFileSystemModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QFileSystemModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QFileSystemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QFileSystemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSystemModel::tr(s, c, n));
}

//  void QFileSystemModel::rootPathChanged(const QString &newPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel15rootPathChangedERK7QString(
    QFileSystemModel *self,
    const QString *newPath) {
  self->rootPathChanged(*newPath);
}

//  void QFileSystemModel::fileRenamed(const QString &path, const QString
//      &oldName, const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel11fileRenamedERK7QStringS2_S2_(
    QFileSystemModel *self,
    const QString *path,
    const QString *oldName,
    const QString *newName) {
  self->fileRenamed(*path, *oldName, *newName);
}

//  void QFileSystemModel::directoryLoaded(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel15directoryLoadedERK7QString(
    QFileSystemModel *self,
    const QString *path) {
  self->directoryLoaded(*path);
}

//  QFileSystemModel::QFileSystemModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSystemModel *ritual_ZN16QFileSystemModelC1EP7QObject(QObject *parent) {
  return new CuteQFileSystemModel(parent);
}

//  QFileSystemModel::~QFileSystemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModelD1Ev(QFileSystemModel *self) {
  delete self;
}

//  QModelIndex QFileSystemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel5indexEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QFileSystemModel::index(const QString &path, int column)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel5indexERK7QStringi(
    const QFileSystemModel *self,
    const QString *path,
    int column) {
  return new QModelIndex(self->index(*path, column));
}

//  QModelIndex QFileSystemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel6parentERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QFileSystemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel7siblingEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QFileSystemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel11hasChildrenERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  bool QFileSystemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel12canFetchMoreERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QFileSystemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9fetchMoreERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  int QFileSystemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel8rowCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QFileSystemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel11columnCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QFileSystemModel::myComputer(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel10myComputerEi(
    const QFileSystemModel *self,
    int role) {
  return new QVariant(self->myComputer(role));
}

//  QVariant QFileSystemModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel4dataERK11QModelIndexi(
    const QFileSystemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QFileSystemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel7setDataERK11QModelIndexRK8QVarianti(
    QFileSystemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QFileSystemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel10headerDataEiN2Qt11OrientationEi(
    const QFileSystemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  Qt::ItemFlags QFileSystemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel5flagsERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QFileSystemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel4sortEiN2Qt9SortOrderE(
    QFileSystemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QStringList QFileSystemModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QFileSystemModel9mimeTypesEv(
    const QFileSystemModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QFileSystemModel::mimeData(const QModelIndexList &indexes)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK16QFileSystemModel8mimeDataERK5QListI11QModelIndexE(
    const QFileSystemModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QFileSystemModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QFileSystemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QFileSystemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel20supportedDropActionsEv(
    const QFileSystemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  QHash<int, QByteArray> QFileSystemModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK16QFileSystemModel9roleNamesEv(
    const QFileSystemModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QModelIndex QFileSystemModel::setRootPath(const QString &path)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN16QFileSystemModel11setRootPathERK7QString(
    QFileSystemModel *self,
    const QString *path) {
  return new QModelIndex(self->setRootPath(*path));
}

//  QString QFileSystemModel::rootPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8rootPathEv(
    const QFileSystemModel *self) {
  return new QString(self->rootPath());
}

//  QDir QFileSystemModel::rootDirectory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK16QFileSystemModel13rootDirectoryEv(
    const QFileSystemModel *self) {
  return new QDir(self->rootDirectory());
}

//  void QFileSystemModel::setIconProvider(QAbstractFileIconProvider
//      *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel15setIconProviderEP25QAbstractFileIconProvider(
    QFileSystemModel *self,
    QAbstractFileIconProvider *provider) {
  self->setIconProvider(provider);
}

//  QAbstractFileIconProvider *QFileSystemModel::iconProvider() const
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZNK16QFileSystemModel12iconProviderEv(
    const QFileSystemModel *self) {
  return self->iconProvider();
}

//  void QFileSystemModel::setFilter(QDir::Filters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9setFilterE6QFlagsIN4QDir6FilterEE(
    QFileSystemModel *self,
    int filters) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filters));
}

//  QDir::Filters QFileSystemModel::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel6filterEv(const QFileSystemModel *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QFileSystemModel::setResolveSymlinks(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel18setResolveSymlinksEb(
    QFileSystemModel *self,
    bool enable) {
  self->setResolveSymlinks(enable);
}

//  bool QFileSystemModel::resolveSymlinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel15resolveSymlinksEv(
    const QFileSystemModel *self) {
  return self->resolveSymlinks();
}

//  void QFileSystemModel::setReadOnly(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel11setReadOnlyEb(
    QFileSystemModel *self,
    bool enable) {
  self->setReadOnly(enable);
}

//  bool QFileSystemModel::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel10isReadOnlyEv(
    const QFileSystemModel *self) {
  return self->isReadOnly();
}

//  void QFileSystemModel::setNameFilterDisables(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel21setNameFilterDisablesEb(
    QFileSystemModel *self,
    bool enable) {
  self->setNameFilterDisables(enable);
}

//  bool QFileSystemModel::nameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel18nameFilterDisablesEv(
    const QFileSystemModel *self) {
  return self->nameFilterDisables();
}

//  void QFileSystemModel::setNameFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel14setNameFiltersERK5QListI7QStringE(
    QFileSystemModel *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  QStringList QFileSystemModel::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QFileSystemModel11nameFiltersEv(
    const QFileSystemModel *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QFileSystemModel::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9setOptionENS_6OptionEb(
    QFileSystemModel *self,
    QFileSystemModel::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFileSystemModel::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel10testOptionENS_6OptionE(
    const QFileSystemModel *self,
    QFileSystemModel::Option option) {
  return self->testOption(option);
}

//  void QFileSystemModel::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel10setOptionsE6QFlagsINS_6OptionEE(
    QFileSystemModel *self,
    int options) {
  self->setOptions(QFlags<QFileSystemModel::Option>::fromInt(options));
}

//  Options QFileSystemModel::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel7optionsEv(const QFileSystemModel *self) {
  return static_cast<int>(self->options().toInt());
}

//  QString QFileSystemModel::filePath(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8filePathERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->filePath(*index));
}

//  bool QFileSystemModel::isDir(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel5isDirERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return self->isDir(*index);
}

//  qint64 QFileSystemModel::size(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QFileSystemModel4sizeERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return self->size(*index);
}

//  QString QFileSystemModel::type(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel4typeERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->type(*index));
}

//  QDateTime QFileSystemModel::lastModified(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QDateTime(self->lastModified(*index));
}

//  QDateTime QFileSystemModel::lastModified(const QModelIndex &index, const
//      QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndexRK9QTimeZone(
    const QFileSystemModel *self,
    const QModelIndex *index,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*index, *tz));
}

//  QModelIndex QFileSystemModel::mkdir(const QModelIndex &parent, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN16QFileSystemModel5mkdirERK11QModelIndexRK7QString(
    QFileSystemModel *self,
    const QModelIndex *parent,
    const QString *name) {
  return new QModelIndex(self->mkdir(*parent, *name));
}

//  bool QFileSystemModel::rmdir(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel5rmdirERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *index) {
  return self->rmdir(*index);
}

//  QString QFileSystemModel::fileName(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8fileNameERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->fileName(*index));
}

//  QIcon QFileSystemModel::fileIcon(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QFileSystemModel8fileIconERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QIcon(self->fileIcon(*index));
}

//  QFile::Permissions QFileSystemModel::permissions(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QFile::Permissions *ritual_ZNK16QFileSystemModel11permissionsERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QFile::Permissions(self->permissions(*index));
}

//  QFileInfo QFileSystemModel::fileInfo(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK16QFileSystemModel8fileInfoERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QFileInfo(self->fileInfo(*index));
}

//  bool QFileSystemModel::remove(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel6removeERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *index) {
  return self->remove(*index);
}

//  QFileSystemModel::QFileSystemModel(QFileSystemModelPrivate &a0, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QFileSystemModel *ritual_ZN16QFileSystemModelC1ER23QFileSystemModelPrivateP7QObject(
    QFileSystemModelPrivate *a0,
    QObject *parent) {
  return new CuteQFileSystemModel(*a0, parent);
}

//  void QFileSystemModel::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel10timerEventEP11QTimerEvent(
    QFileSystemModel *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  bool QFileSystemModel::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel5eventEP6QEvent(
    QFileSystemModel *self,
    QEvent *event) {
  return self->event(event);
}

//  QFileSystemModelPrivate *QFileSystemModel::d_func()
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate *ritual_ZN16QFileSystemModel6d_funcEv(
    QFileSystemModel *self) {
  return self->d_func();
}

//  const QFileSystemModelPrivate *QFileSystemModel::d_func() const
extern "C" Q_DECL_EXPORT
const QFileSystemModelPrivate *ritual_ZNK16QFileSystemModel6d_funcEv(
    const QFileSystemModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQFileSystemModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSystemModel(
    QFileSystemModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSystemModel *>(self)->take(key, call);
}

//  QModelIndex QFileSystemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QFileSystemModel5indexEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QFileSystemModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QFileSystemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QFileSystemModel6parentERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QFileSystemModel::parent(*child));
}

//  QModelIndex QFileSystemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QFileSystemModel7siblingEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->QFileSystemModel::sibling(row, column, *idx));
}

//  bool QFileSystemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QFileSystemModel11hasChildrenERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->QFileSystemModel::hasChildren(*parent);
}

//  bool QFileSystemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QFileSystemModel12canFetchMoreERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->QFileSystemModel::canFetchMore(*parent);
}

//  void QFileSystemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QFileSystemModel9fetchMoreERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *parent) {
  self->QFileSystemModel::fetchMore(*parent);
}

//  int QFileSystemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QFileSystemModel8rowCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->QFileSystemModel::rowCount(*parent);
}

//  int QFileSystemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QFileSystemModel11columnCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->QFileSystemModel::columnCount(*parent);
}

//  QVariant QFileSystemModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QFileSystemModel4dataERK11QModelIndexi(
    const QFileSystemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QFileSystemModel::data(*index, role));
}

//  bool QFileSystemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QFileSystemModel7setDataERK11QModelIndexRK8QVarianti(
    QFileSystemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QFileSystemModel::setData(*index, *value, role);
}

//  QVariant QFileSystemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QFileSystemModel10headerDataEiN2Qt11OrientationEi(
    const QFileSystemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QFileSystemModel::headerData(
          section,
          orientation,
          role));
}

//  Qt::ItemFlags QFileSystemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QFileSystemModel5flagsERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QFileSystemModel::flags(*index).toInt());
}

//  void QFileSystemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QFileSystemModel4sortEiN2Qt9SortOrderE(
    QFileSystemModel *self,
    int column,
    Qt::SortOrder order) {
  self->QFileSystemModel::sort(column, order);
}

//  bool QFileSystemModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QFileSystemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QFileSystemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QFileSystemModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  Qt::DropActions QFileSystemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QFileSystemModel20supportedDropActionsEv(
    const QFileSystemModel *self) {
  return static_cast<int>(
      self->QFileSystemModel::supportedDropActions().toInt());
}

//  void QFileSystemModel::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QFileSystemModel10timerEventEP11QTimerEvent(
    QFileSystemModel *self,
    QTimerEvent *event) {
  static_cast<OwnQFileSystemModel *>(self)->OwnQFileSystemModel::timerEvent(
      event);
}

//  bool QFileSystemModel::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QFileSystemModel5eventEP6QEvent(
    QFileSystemModel *self,
    QEvent *event) {
  return static_cast<OwnQFileSystemModel *>(self)->OwnQFileSystemModel::event(
      event);
}

//  a QFile::Permissions a ritual of QFileSystemModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFileSystemModel__QFile_Permissions(
    QFile::Permissions *self) {
  delete self;
}

#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(filesystemmodel)
