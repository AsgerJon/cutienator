//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::SignatureModel' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 3 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/qdesigner_formwindowcommand_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/membersheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qvalidator.h>
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtDesigner__qdesigner_internal_SignatureModel.cpp, line 1, as moc:qdesigner_internal::SignatureModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::SignatureModel::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::SignatureModel",
        "checkSignature",
        "",
        "signature",
        "bool*",
        "ok"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'checkSignature'
        QtMocHelpers::SignalData<void(const QString &, bool *)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 3 }, { 0x80000000 | 4, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<SignatureModel, qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::SignatureModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QStandardItemModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::SignatureModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<SignatureModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->checkSignature((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<bool*>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (SignatureModel::*)(const QString & , bool * )>(_a, &SignatureModel::checkSignature, 0))
            return;
    }
}

const QMetaObject *qdesigner_internal::SignatureModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::SignatureModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignatureModelE_t>.strings))
        return static_cast<void*>(this);
    return QStandardItemModel::qt_metacast(_clname);
}

int qdesigner_internal::SignatureModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QStandardItemModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void qdesigner_internal::SignatureModel::checkSignature(const QString & _t1, bool * _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 165, as _ZN18qdesigner_internal14SignatureModel7setDataERK11QModelIndexRK8QVarianti
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline bool SignatureModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (role != Qt::EditRole)
        return QStandardItemModel::setData(index, value, role);
    // check via signal (unless it is the same), in which case we can't be bothered.
    const QStandardItem *item = itemFromIndex(index);
    Q_ASSERT(item);
    const QString signature = value.toString();
    if (item->text() == signature)
        return true;

    bool ok = true;
    emit checkSignature(signature, &ok);
    if (!ok)
        return false;

    return QStandardItemModel::setData(index, value, role);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 160, as _ZN18qdesigner_internal14SignatureModelC1EP7QObject
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline SignatureModel::SignatureModel(QObject *parent) :
     QStandardItemModel(parent)
{
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::SignatureModel that Python can take functions over in. Every qdesigner_internal::SignatureModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall0)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*Cuteqdesigner_internal_SignatureModelCall1)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*Cuteqdesigner_internal_SignatureModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*Cuteqdesigner_internal_SignatureModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*Cuteqdesigner_internal_SignatureModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*Cuteqdesigner_internal_SignatureModelCall6)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*Cuteqdesigner_internal_SignatureModelCall7)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*Cuteqdesigner_internal_SignatureModelCall9)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall10)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall11)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*Cuteqdesigner_internal_SignatureModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*Cuteqdesigner_internal_SignatureModelCall16)(const void *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*Cuteqdesigner_internal_SignatureModelCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall18)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*Cuteqdesigner_internal_SignatureModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*Cuteqdesigner_internal_SignatureModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*Cuteqdesigner_internal_SignatureModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*Cuteqdesigner_internal_SignatureModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*Cuteqdesigner_internal_SignatureModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*Cuteqdesigner_internal_SignatureModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*Cuteqdesigner_internal_SignatureModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_SignatureModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SignatureModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SignatureModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SignatureModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SignatureModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SignatureModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_SignatureModel : public qdesigner_internal::SignatureModel {
public:
  using qdesigner_internal::SignatureModel::SignatureModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
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
  //  bool qdesigner_internal::SignatureModel::setData(const QModelIndex
  //      &index, const QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall0 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall0>(taken[0]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::SignatureModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QModelIndex QStandardItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall1 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QModelIndex QStandardItemModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall2 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall2>(taken[2]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::parent(child);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  int QStandardItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall3 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::rowCount(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  int QStandardItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall4 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall4>(taken[4]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::columnCount(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall5 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall5>(taken[5]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall6 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall6>(taken[6]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::data(index, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  void QStandardItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall7 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall7>(taken[7]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QStandardItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall8 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall8>(taken[8]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::clearItemData(index);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall9 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall9>(taken[9]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall10 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall10>(taken[10]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall11 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall11>(taken[11]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall12 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall12>(taken[12]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall13 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall13>(taken[13]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall14 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall14>(taken[14]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall15 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall15>(taken[15]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QStandardItemModel::flags(index);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  Qt::DropActions QStandardItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall16 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QStandardItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  void QStandardItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall17 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall17>(taken[17]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QStandardItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall18 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall18>(taken[18]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall19 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall19>(taken[19]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
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
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall20 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall21 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDragActions();
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
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall22 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall23 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall23>(taken[23]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall24 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall25 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall26 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall27 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall27>(taken[27]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_SignatureModelCall28 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall28>(taken[28]);
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
      Cuteqdesigner_internal_SignatureModelCall29 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall29>(taken[29]);
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
      Cuteqdesigner_internal_SignatureModelCall30 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall30>(taken[30]);
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
      Cuteqdesigner_internal_SignatureModelCall31 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall31>(taken[31]);
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
      Cuteqdesigner_internal_SignatureModelCall32 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall32>(taken[32]);
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
      Cuteqdesigner_internal_SignatureModelCall33 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall33>(taken[33]);
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
      Cuteqdesigner_internal_SignatureModelCall34 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall34>(taken[34]);
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
      Cuteqdesigner_internal_SignatureModelCall35 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall35>(taken[35]);
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
      Cuteqdesigner_internal_SignatureModelCall36 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall36>(taken[36]);
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
      Cuteqdesigner_internal_SignatureModelCall37 call = reinterpret_cast<Cuteqdesigner_internal_SignatureModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::SignatureModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14SignatureModel10metaObjectEv(
    const qdesigner_internal::SignatureModel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SignatureModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14SignatureModel11qt_metacastEPKc(
    qdesigner_internal::SignatureModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SignatureModel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14SignatureModel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SignatureModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::SignatureModel::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14SignatureModel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::SignatureModel::tr(s, c, n));
}

//  qdesigner_internal::SignatureModel::SignatureModel(QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::SignatureModel *ritual_ZN18qdesigner_internal14SignatureModelC1EP7QObject(
    QObject *parent) {
  return new Cuteqdesigner_internal_SignatureModel(parent);
}

//  bool qdesigner_internal::SignatureModel::setData(const QModelIndex
//      &index, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14SignatureModel7setDataERK11QModelIndexRK8QVarianti(
    qdesigner_internal::SignatureModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  void qdesigner_internal::SignatureModel::checkSignature(const QString
//      &signature, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignatureModel14checkSignatureERK7QStringPb(
    qdesigner_internal::SignatureModel *self,
    const QString *signature,
    bool *ok) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignatureModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkSignature(const QString &,bool *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkSignature(const QString &,bool *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(signature)),
      const_cast<void *>(static_cast<const void *>(&ok)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a Cuteqdesigner_internal_SignatureModel, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_SignatureModel(
    qdesigner_internal::SignatureModel *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_SignatureModel *>(self)->take(key, call);
}

//  bool qdesigner_internal::SignatureModel::setData(const QModelIndex
//      &index, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal14SignatureModel7setDataERK11QModelIndexRK8QVarianti(
    qdesigner_internal::SignatureModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->qdesigner_internal::SignatureModel::setData(
      *index,
      *value,
      role);
}
