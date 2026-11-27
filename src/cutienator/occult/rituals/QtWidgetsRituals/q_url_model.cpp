//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-26: moc's output for 'QUrlModel' is pasted in, cut from
//  what the moc of Qt 6.12.0 writes for its header: Qt's library keeps it to
//  itself; added are 3 rituals that lean on what moc writes for a class of
//  the part Qt keeps to itself, whose ritual file carries moc's output,
//  drafted by a copy of the generator that lets those names through. A copy
//  of a meta-object is a second one: 'qobject_cast' between it and Qt's own
//  does not match. Edited by hand on 2026-11-27: code taken from Qt's source
//  no longer stands under defined(Q_OS_LINUX), which Qt does not write
//  there; its rituals no longer stand under defined(Q_OS_LINUX), as the code
//  taken from Qt they call no longer does; the constructors and the
//  destructor of QUrlModel taken from Qt are no longer 'inline' (2): the one
//  definition the target file has of each, which the ritual files of other
//  classes of the part call, as Microsoft's ABI emits an 'inline' one only
//  where it is used. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(filedialog)
#if QT_CONFIG(filedialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/private/qsidebar_p.h>
#include <QtWidgets/qaction.h>
#include <QtCore/qurl.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtCore/qmimedata.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qfilesystemmodel.h>
#include <QtGui/qabstractfileiconprovider.h>
#include <QtWidgets/qfiledialog.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/dialogs/qsidebar.cpp, line 53, as local:qsidebar.cpp:uriListMimeType
constexpr char uriListMimeType[] = "text/uri-list";

//  from src/widgets/dialogs/qsidebar.cpp, line 56, as local:qsidebar.cpp:hasSupportedFormat
#if QT_CONFIG(draganddrop)
static bool hasSupportedFormat(const QMimeData *data)
{
    return data->hasFormat(QLatin1StringView(uriListMimeType));
}
#endif  // QT_CONFIG(draganddrop)

//  from QtWidgets__QUrlModel.cpp, line 1, as moc:QUrlModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9QUrlModelE_t {};
} // unnamed namespace

template <> constexpr inline auto QUrlModel::qt_create_metaobjectdata<qt_meta_tag_ZN9QUrlModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QUrlModel",
        "dataChanged",
        "",
        "QModelIndex",
        "topLeft",
        "bottomRight",
        "layoutChanged"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'dataChanged'
        QtMocHelpers::SlotData<void(const QModelIndex &, const QModelIndex &)>(1, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { 0x80000000 | 3, 5 },
        }}),
        // Slot 'layoutChanged'
        QtMocHelpers::SlotData<void()>(6, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QUrlModel, qt_meta_tag_ZN9QUrlModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QUrlModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QStandardItemModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QUrlModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QUrlModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9QUrlModelE_t>.metaTypes,
    nullptr
} };

void QUrlModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QUrlModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->dataChanged((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[2]))); break;
        case 1: _t->layoutChanged(); break;
        default: ;
        }
    }
}

const QMetaObject *QUrlModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QUrlModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QUrlModelE_t>.strings))
        return static_cast<void*>(this);
    return QStandardItemModel::qt_metacast(_clname);
}

int QUrlModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QStandardItemModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

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

//  from src/widgets/dialogs/qsidebar.cpp, line 127, as _ZN9QUrlModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex
#if QT_CONFIG(draganddrop)
inline bool QUrlModel::dropMimeData(const QMimeData *data, Qt::DropAction action,
                                 int row, int column, const QModelIndex &parent)
{
    if (!hasSupportedFormat(data))
        return false;
    Q_UNUSED(action);
    Q_UNUSED(column);
    Q_UNUSED(parent);
    addUrls(data->urls(), row);
    return true;
}
#endif  // QT_CONFIG(draganddrop)

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

//  from src/widgets/dialogs/qsidebar.cpp, line 65, as _ZNK9QUrlModel9mimeTypesEv
inline QStringList QUrlModel::mimeTypes() const
{
    return QStringList(QLatin1StringView(uriListMimeType));
}

//  from src/widgets/dialogs/qsidebar.cpp, line 43, as _ZN9QUrlModelC1EP7QObject
QUrlModel::QUrlModel(QObject *parent) : QStandardItemModel(parent), showFullPath(false), fileSystemModel(nullptr)
{
}

//  from src/widgets/dialogs/qsidebar.cpp, line 47, as _ZN9QUrlModelD1Ev
QUrlModel::~QUrlModel()
{
    for (auto &conn : modelConnections)
        disconnect(conn);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 110, as _ZN9QUrlModel7canDropEP15QDragEnterEvent
#if QT_CONFIG(draganddrop)
inline bool QUrlModel::canDrop(QDragEnterEvent *event)
{
    if (!hasSupportedFormat(event->mimeData()))
        return false;

    const QList<QUrl> list = event->mimeData()->urls();
    for (const auto &url : list) {
        const QModelIndex idx = fileSystemModel->index(url.toLocalFile());
        if (!fileSystemModel->isDir(idx))
            return false;
    }
    return true;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/dialogs/qsidebar.cpp, line 217, as _ZN9QUrlModel7setUrlsERK5QListI4QUrlE
inline void QUrlModel::setUrls(const QList<QUrl> &list)
{
    removeRows(0, rowCount());
    invalidUrls.clear();
    watching.clear();
    addUrls(list, 0);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 231, as _ZN9QUrlModel7addUrlsERK5QListI4QUrlEib
inline void QUrlModel::addUrls(const QList<QUrl> &list, int row, bool move)
{
    if (row == -1)
        row = rowCount();
    row = qMin(row, rowCount());
    const auto rend = list.crend();
    for (auto it = list.crbegin(); it != rend; ++it) {
        QUrl url = *it;
        if (!url.isValid() || url.scheme() != "file"_L1)
            continue;
        //this makes sure the url is clean
        const QString cleanUrl = QDir::cleanPath(url.toLocalFile());
        if (!cleanUrl.isEmpty())
            url = QUrl::fromLocalFile(cleanUrl);

        for (int j = 0; move && j < rowCount(); ++j) {
            QString local = index(j, 0).data(UrlRole).toUrl().toLocalFile();
#if defined(Q_OS_WIN)
            const Qt::CaseSensitivity cs = Qt::CaseInsensitive;
#else
            const Qt::CaseSensitivity cs = Qt::CaseSensitive;
#endif
            if (!cleanUrl.compare(local, cs)) {
                removeRow(j);
                if (j <= row)
                    row--;
                break;
            }
        }
        row = qMax(row, 0);
        QModelIndex idx = fileSystemModel->index(cleanUrl);
        if (!fileSystemModel->isDir(idx))
            continue;
        insertRows(row, 1);
        setUrl(index(row, 0), url, idx);
        watching.append({idx, cleanUrl});
    }
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

//  from src/widgets/dialogs/qsidebar.cpp, line 286, as _ZN9QUrlModel18setFileSystemModelEP16QFileSystemModel
inline void QUrlModel::setFileSystemModel(QFileSystemModel *model)
{
    if (model == fileSystemModel)
        return;
    if (fileSystemModel != nullptr) {
        for (auto &conn : modelConnections)
            disconnect(conn);
    }
    fileSystemModel = model;
    if (fileSystemModel != nullptr) {
        modelConnections = {
            connect(model, &QFileSystemModel::dataChanged,
                    this, &QUrlModel::dataChanged),
            connect(model, &QFileSystemModel::layoutChanged,
                    this, &QUrlModel::layoutChanged),
            connect(model, &QFileSystemModel::rowsRemoved,
                    this, &QUrlModel::layoutChanged),
        };
    }
    clear();
    insertColumns(0, 1);
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
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQUrlModelCall0)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
typedef int (*CuteQUrlModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
typedef bool (*CuteQUrlModelCall2)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*CuteQUrlModelCall3)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*CuteQUrlModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQUrlModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQUrlModelCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*CuteQUrlModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*CuteQUrlModelCall9)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*CuteQUrlModelCall11)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall12)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall15)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQUrlModelCall16)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQUrlModelCall17)(const void *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*CuteQUrlModelCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQUrlModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQUrlModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQUrlModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQUrlModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQUrlModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQUrlModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQUrlModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQUrlModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQUrlModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQUrlModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQUrlModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQUrlModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUrlModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUrlModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUrlModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUrlModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUrlModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUrlModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUrlModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUrlModel : public QUrlModel {
public:
  using QUrlModel::QUrlModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
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
#if QT_CONFIG(filedialog)
#if QT_CONFIG(draganddrop)
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
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
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
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(filedialog)
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
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
    if (taken[11]) {
      int handled = 0;
      CuteQUrlModelCall11 call = reinterpret_cast<CuteQUrlModelCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQUrlModelCall12 call = reinterpret_cast<CuteQUrlModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQUrlModelCall13 call = reinterpret_cast<CuteQUrlModelCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQUrlModelCall14 call = reinterpret_cast<CuteQUrlModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQUrlModelCall15 call = reinterpret_cast<CuteQUrlModelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQUrlModelCall16 call = reinterpret_cast<CuteQUrlModelCall16>(taken[16]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
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
      CuteQUrlModelCall19 call = reinterpret_cast<CuteQUrlModelCall19>(taken[19]);
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
      CuteQUrlModelCall20 call = reinterpret_cast<CuteQUrlModelCall20>(taken[20]);
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
      CuteQUrlModelCall21 call = reinterpret_cast<CuteQUrlModelCall21>(taken[21]);
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
      CuteQUrlModelCall22 call = reinterpret_cast<CuteQUrlModelCall22>(taken[22]);
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
      CuteQUrlModelCall23 call = reinterpret_cast<CuteQUrlModelCall23>(taken[23]);
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
      CuteQUrlModelCall24 call = reinterpret_cast<CuteQUrlModelCall24>(taken[24]);
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
      CuteQUrlModelCall25 call = reinterpret_cast<CuteQUrlModelCall25>(taken[25]);
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
      CuteQUrlModelCall26 call = reinterpret_cast<CuteQUrlModelCall26>(taken[26]);
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
      CuteQUrlModelCall27 call = reinterpret_cast<CuteQUrlModelCall27>(taken[27]);
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
      CuteQUrlModelCall28 call = reinterpret_cast<CuteQUrlModelCall28>(taken[28]);
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
      CuteQUrlModelCall29 call = reinterpret_cast<CuteQUrlModelCall29>(taken[29]);
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
      CuteQUrlModelCall30 call = reinterpret_cast<CuteQUrlModelCall30>(taken[30]);
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
      CuteQUrlModelCall31 call = reinterpret_cast<CuteQUrlModelCall31>(taken[31]);
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
      CuteQUrlModelCall32 call = reinterpret_cast<CuteQUrlModelCall32>(taken[32]);
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
      CuteQUrlModelCall33 call = reinterpret_cast<CuteQUrlModelCall33>(taken[33]);
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
      CuteQUrlModelCall34 call = reinterpret_cast<CuteQUrlModelCall34>(taken[34]);
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
      CuteQUrlModelCall35 call = reinterpret_cast<CuteQUrlModelCall35>(taken[35]);
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
      CuteQUrlModelCall36 call = reinterpret_cast<CuteQUrlModelCall36>(taken[36]);
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
      CuteQUrlModelCall37 call = reinterpret_cast<CuteQUrlModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUrlModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QUrlModel10metaObjectEv(
    const QUrlModel *self) {
  return self->metaObject();
}

//  void *QUrlModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QUrlModel11qt_metacastEPKc(QUrlModel *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QUrlModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QUrlModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QUrlModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_CONFIG(draganddrop)
//  QString QUrlModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QUrlModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUrlModel::tr(s, c, n));
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  QUrlModel::QUrlModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QUrlModel *ritual_ZN9QUrlModelC1EP7QObject(QObject *parent) {
  return new CuteQUrlModel(parent);
}
#endif  // QT_CONFIG(draganddrop)

//  QUrlModel::~QUrlModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModelD1Ev(QUrlModel *self) {
  delete self;
}

//  QStringList QUrlModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QUrlModel9mimeTypesEv(const QUrlModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QUrlModel::mimeData(const QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK9QUrlModel8mimeDataERK5QListI11QModelIndexE(
    const QUrlModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

#if QT_CONFIG(draganddrop)
//  bool QUrlModel::canDrop(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QUrlModel7canDropEP15QDragEnterEvent(
    QUrlModel *self,
    QDragEnterEvent *event) {
  return self->canDrop(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QUrlModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QUrlModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QUrlModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}
#endif  // QT_CONFIG(draganddrop)

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

//  void QUrlModel::setUrls(const QList<QUrl> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel7setUrlsERK5QListI4QUrlE(
    QUrlModel *self,
    const QList<QUrl> *list) {
  self->setUrls(*list);
}

//  void QUrlModel::addUrls(const QList<QUrl> &urls, int row, bool move)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel7addUrlsERK5QListI4QUrlEib(
    QUrlModel *self,
    const QList<QUrl> *urls,
    int row,
    bool move) {
  self->addUrls(*urls, row, move);
}

//  QList<QUrl> QUrlModel::urls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK9QUrlModel4urlsEv(const QUrlModel *self) {
  return new QList<QUrl>(self->urls());
}

#if QT_CONFIG(draganddrop)
//  void QUrlModel::setFileSystemModel(QFileSystemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel18setFileSystemModelEP16QFileSystemModel(
    QUrlModel *self,
    QFileSystemModel *model) {
  self->setFileSystemModel(model);
}
#endif  // QT_CONFIG(draganddrop)

//  void QUrlModel::dataChanged(const QModelIndex &topLeft, const QModelIndex
//      &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel11dataChangedERK11QModelIndexS2_(
    QUrlModel *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QUrlModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dataChanged(const QModelIndex &,const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dataChanged(const QModelIndex &,const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(topLeft)),
      const_cast<void *>(static_cast<const void *>(bottomRight)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QUrlModel::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlModel13layoutChangedEv(QUrlModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QUrlModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "layoutChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "layoutChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

#if QT_CONFIG(draganddrop)
//  bool QUrlModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QUrlModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QUrlModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QUrlModel::dropMimeData(data, action, row, column, *parent);
}
#endif  // QT_CONFIG(draganddrop)

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

#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(filedialog)
