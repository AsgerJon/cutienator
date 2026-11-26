//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSidebar' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 4 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
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
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qvariant.h>
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

//  from QtWidgets__QSidebar.cpp, line 1, as moc:QSidebar
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8QSidebarE_t {};
} // unnamed namespace

template <> constexpr inline auto QSidebar::qt_create_metaobjectdata<qt_meta_tag_ZN8QSidebarE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSidebar",
        "goToUrl",
        "",
        "QUrl",
        "url",
        "clicked",
        "QModelIndex",
        "index",
        "showContextMenu",
        "QPoint",
        "position",
        "removeEntry"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'goToUrl'
        QtMocHelpers::SignalData<void(const QUrl &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'clicked'
        QtMocHelpers::SlotData<void(const QModelIndex &)>(5, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
        // Slot 'showContextMenu'
        QtMocHelpers::SlotData<void(const QPoint &)>(8, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 9, 10 },
        }}),
        // Slot 'removeEntry'
        QtMocHelpers::SlotData<void()>(11, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSidebar, qt_meta_tag_ZN8QSidebarE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSidebar::staticMetaObject = { {
    QMetaObject::SuperData::link<QListView::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8QSidebarE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8QSidebarE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8QSidebarE_t>.metaTypes,
    nullptr
} };

void QSidebar::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSidebar *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->goToUrl((*reinterpret_cast<std::add_pointer_t<QUrl>>(_a[1]))); break;
        case 1: _t->clicked((*reinterpret_cast<std::add_pointer_t<QModelIndex>>(_a[1]))); break;
        case 2: _t->showContextMenu((*reinterpret_cast<std::add_pointer_t<QPoint>>(_a[1]))); break;
        case 3: _t->removeEntry(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QSidebar::*)(const QUrl & )>(_a, &QSidebar::goToUrl, 0))
            return;
    }
}

const QMetaObject *QSidebar::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSidebar::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8QSidebarE_t>.strings))
        return static_cast<void*>(this);
    return QListView::qt_metacast(_clname);
}

int QSidebar::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QListView::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void QSidebar::goToUrl(const QUrl & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from src/widgets/dialogs/qsidebar.cpp, line 458, as _ZN8QSidebar11removeEntryEv
inline void QSidebar::removeEntry()
{
    const QList<QModelIndex> idxs = selectionModel()->selectedIndexes();
    // Create a list of QPersistentModelIndex as the removeRow() calls below could
    // invalidate the indexes in "idxs"
    const QList<QPersistentModelIndex> persIndexes(idxs.cbegin(), idxs.cend());
    for (const QPersistentModelIndex &persistent : persIndexes) {
        if (!persistent.data(QUrlModel::UrlRole).toUrl().path().isEmpty())
            model()->removeRow(persistent.row());
    }
}

//  from src/widgets/dialogs/qsidebar.cpp, line 485, as _ZN8QSidebar12focusInEventEP11QFocusEvent
inline void QSidebar::focusInEvent(QFocusEvent *event)
{
    QAbstractScrollArea::focusInEvent(event);
    viewport()->update();
}

//  from src/widgets/dialogs/qsidebar.cpp, line 399, as _ZN8QSidebar14dragEnterEventEP15QDragEnterEvent
#if QT_CONFIG(draganddrop)
inline void QSidebar::dragEnterEvent(QDragEnterEvent *event)
{
    if (urlModel->canDrop(event))
        QListView::dragEnterEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/dialogs/qsidebar.cpp, line 438, as _ZN8QSidebar15showContextMenuERK6QPoint
#if QT_CONFIG(menu)
inline void QSidebar::showContextMenu(const QPoint &position)
{
    QList<QAction *> actions;
    if (indexAt(position).isValid()) {
        QAction *action = new QAction(QFileDialog::tr("Remove"), this);
        if (indexAt(position).data(QUrlModel::UrlRole).toUrl().path().isEmpty())
            action->setEnabled(false);
        connect(action, &QAction::triggered, this, &QSidebar::removeEntry);
        actions.append(action);
    }
    if (actions.size() > 0)
        QMenu::exec(actions, mapToGlobal(position));
}
#endif  // QT_CONFIG(menu)

//  from src/widgets/dialogs/qsidebar.cpp, line 494, as _ZN8QSidebar5eventEP6QEvent
inline bool QSidebar::event(QEvent * event)
{
    if (event->type() == QEvent::KeyRelease) {
        QKeyEvent *ke = static_cast<QKeyEvent *>(event);
        if (ke->key() == Qt::Key_Delete) {
            removeEntry();
            return true;
        }
    }
    return QListView::event(event);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 475, as _ZN8QSidebar7clickedERK11QModelIndex
inline void QSidebar::clicked(const QModelIndex &index)
{
    QUrl url = model()->index(index.row(), 0).data(QUrlModel::UrlRole).toUrl();
    selectUrl(url);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 406, as _ZNK8QSidebar8sizeHintEv
inline QSize QSidebar::sizeHint() const
{
    if (model())
        return QListView::sizeHintForIndex(model()->index(0, 0)) + QSize(2 * frameWidth(), 2 * frameWidth());
    return QListView::sizeHint();
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

//  from src/widgets/dialogs/qsidebar.cpp, line 217, as _ZN9QUrlModel7setUrlsERK5QListI4QUrlE
inline void QUrlModel::setUrls(const QList<QUrl> &list)
{
    removeRows(0, rowCount());
    invalidUrls.clear();
    watching.clear();
    addUrls(list, 0);
}

//  from src/widgets/dialogs/qsidebar.cpp, line 43, as _ZN9QUrlModelC1EP7QObject
inline QUrlModel::QUrlModel(QObject *parent) : QStandardItemModel(parent), showFullPath(false), fileSystemModel(nullptr)
{
}

//  from src/widgets/dialogs/qsidebar.cpp, line 23, as _ZNK16QSideBarDelegate15initStyleOptionEP20QStyleOptionViewItemRK11QModelIndex
inline void QSideBarDelegate::initStyleOption(QStyleOptionViewItem *option,
                                         const QModelIndex &index) const
{
    QStyledItemDelegate::initStyleOption(option,index);
    QVariant value = index.data(QUrlModel::EnabledRole);
    if (value.isValid()) {
        //If the bookmark/entry is not enabled then we paint it in gray
        if (!qvariant_cast<bool>(value))
            option->state &= ~QStyle::State_Enabled;
    }
}

//  from src/widgets/dialogs/qsidebar.cpp, line 231, as _ZN9QUrlModel7addUrlsERK5QListI4QUrlEib
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)

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

//  from src/widgets/dialogs/qsidebar.cpp, line 368, as _ZN8QSidebarC1EP7QWidget
inline QSidebar::QSidebar(QWidget *parent) : QListView(parent)
{
}

//  from src/widgets/dialogs/qsidebar.cpp, line 372, as _ZN8QSidebar15setModelAndUrlsEP16QFileSystemModelRK5QListI4QUrlE
inline void QSidebar::setModelAndUrls(QFileSystemModel *model, const QList<QUrl> &newUrls)
{
    setUniformItemSizes(true);
    urlModel = new QUrlModel(this);
    urlModel->setFileSystemModel(model);
    setModel(urlModel);
    setItemDelegate(new QSideBarDelegate(this));

    connect(selectionModel(), &QItemSelectionModel::currentChanged,
            this, &QSidebar::clicked);
#if QT_CONFIG(draganddrop)
    setDragDropMode(QAbstractItemView::DragDrop);
#endif
#if QT_CONFIG(menu)
    setContextMenuPolicy(Qt::CustomContextMenu);
    connect(this, &QSidebar::customContextMenuRequested,
            this, &QSidebar::showContextMenu);
#endif
    urlModel->setUrls(newUrls);
    setCurrentIndex(this->model()->index(0,0));
}

//  from src/widgets/dialogs/qsidebar.cpp, line 394, as _ZN8QSidebarD1Ev
inline QSidebar::~QSidebar()
{
}

//  from src/widgets/dialogs/qsidebar.cpp, line 413, as _ZN8QSidebar9selectUrlERK4QUrl
inline void QSidebar::selectUrl(const QUrl &url)
{
    disconnect(selectionModel(), &QItemSelectionModel::currentChanged,
               this, &QSidebar::clicked);

    selectionModel()->clear();
    for (int i = 0; i < model()->rowCount(); ++i) {
        if (model()->index(i, 0).data(QUrlModel::UrlRole).toUrl() == url) {
            emit goToUrl(url);
            selectionModel()->setCurrentIndex(model()->index(i, 0),
                                              QItemSelectionModel::SelectCurrent);
            break;
        }
    }

    connect(selectionModel(), &QItemSelectionModel::currentChanged,
            this, &QSidebar::clicked);
}
//  -----------------------------------------------------------------------

//  Only a class built on QSidebar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSidebar : QSidebar {
  using QSidebar::event;
  using QSidebar::focusInEvent;
  using QSidebar::dragEnterEvent;
};

//  A QSidebar that Python can take functions over in. Every QSidebar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(filedialog)
typedef const QSize * (*CuteQSidebarCall0)(const void *, int *);
#endif  // QT_CONFIG(filedialog)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filedialog)
typedef bool (*CuteQSidebarCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filedialog)
typedef void (*CuteQSidebarCall2)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(filedialog)
typedef void (*CuteQSidebarCall3)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRect * (*CuteQSidebarCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QModelIndex * (*CuteQSidebarCall6)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall7)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall8)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall10)(const void *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall11)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall12)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall16)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall17)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall18)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall19)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall20)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall21)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall22)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall23)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQSidebarCall24)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQSidebarCall25)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall26)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRegion * (*CuteQSidebarCall27)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall28)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQSidebarCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall30)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQSidebarCall31)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef const QSize * (*CuteQSidebarCall32)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall33)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall34)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall35)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQSidebarCall36)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQSidebarCall37)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQSidebarCall38)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQSidebarCall39)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall40)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall41)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall42)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall44)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall45)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall46)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall47)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall48)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall49)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQSidebarCall50)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQSidebarCall51)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQSidebarCall52)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQSidebarCall53)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall54)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall55)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall56)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall57)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQSidebarCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQSidebarCall59)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQSidebarCall60)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQSidebarCall61)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQSidebarCall62)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQSidebarCall63)(const void *, QEvent *, int *);
typedef void (*CuteQSidebarCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQSidebarCall65)(const void *, int *);
typedef void (*CuteQSidebarCall66)(const void *, bool, int *);
typedef int (*CuteQSidebarCall67)(const void *, int, int *);
typedef bool (*CuteQSidebarCall68)(const void *, int *);
typedef void * (*CuteQSidebarCall69)(const void *, int *);
typedef void (*CuteQSidebarCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSidebarCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSidebarCall72)(const void *, QEvent *, int *);
typedef void (*CuteQSidebarCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSidebarCall74)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQSidebarCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQSidebarCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQSidebarCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQSidebarCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQSidebarCall79)(const void *, int, int *);
typedef void (*CuteQSidebarCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQSidebarCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQSidebarCall82)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSidebarCall83)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSidebarCall84)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSidebarCall85)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSidebarCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSidebar : public QSidebar {
public:
  using QSidebar::QSidebar;
  void *taken[87] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[74] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[75] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[76] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[82] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[83] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[84] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[85] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[86] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(filedialog)
  //  QSize QSidebar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSidebarCall0 call = reinterpret_cast<CuteQSidebarCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSidebar::sizeHint();
  }
#endif  // QT_CONFIG(filedialog)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filedialog)
  //  bool QSidebar::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSidebarCall1 call = reinterpret_cast<CuteQSidebarCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QSidebar::event(e);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(filedialog)
  //  void QSidebar::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSidebarCall2 call = reinterpret_cast<CuteQSidebarCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSidebar::focusInEvent(event);
  }
#endif  // QT_CONFIG(filedialog)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(filedialog)
  //  void QSidebar::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSidebarCall3 call = reinterpret_cast<CuteQSidebarCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSidebar::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QRect QListView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSidebarCall4 call = reinterpret_cast<CuteQSidebarCall4>(taken[4]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRect(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSidebarCall5 call = reinterpret_cast<CuteQSidebarCall5>(taken[5]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QListView::scrollTo(index, hint);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QModelIndex QListView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSidebarCall6 call = reinterpret_cast<CuteQSidebarCall6>(taken[6]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QListView::indexAt(p);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSidebarCall7 call = reinterpret_cast<CuteQSidebarCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::doItemsLayout();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::reset()
  void reset() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSidebarCall8 call = reinterpret_cast<CuteQSidebarCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::reset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSidebarCall9 call = reinterpret_cast<CuteQSidebarCall9>(taken[9]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QListView::setRootIndex(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
  //  void QListView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSidebarCall10 call = reinterpret_cast<CuteQSidebarCall10>(taken[10]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QListView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSidebarCall11 call = reinterpret_cast<CuteQSidebarCall11>(taken[11]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
  //      start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSidebarCall12 call = reinterpret_cast<CuteQSidebarCall12>(taken[12]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(listview)
  //  void QListView::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSidebarCall13 call = reinterpret_cast<CuteQSidebarCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QListView::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSidebarCall14 call = reinterpret_cast<CuteQSidebarCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
  //  void QListView::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSidebarCall15 call = reinterpret_cast<CuteQSidebarCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::wheelEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
  //  void QListView::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSidebarCall16 call = reinterpret_cast<CuteQSidebarCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::timerEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(listview)
  //  void QListView::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSidebarCall17 call = reinterpret_cast<CuteQSidebarCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::resizeEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSidebarCall18 call = reinterpret_cast<CuteQSidebarCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSidebarCall19 call = reinterpret_cast<CuteQSidebarCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSidebarCall20 call = reinterpret_cast<CuteQSidebarCall20>(taken[20]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dropEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSidebarCall21 call = reinterpret_cast<CuteQSidebarCall21>(taken[21]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QListView::startDrag(supportedActions);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::initViewItemOption(QStyleOptionViewItem *option)
  //      const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSidebarCall22 call = reinterpret_cast<CuteQSidebarCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QListView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(listview)
  //  void QListView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSidebarCall23 call = reinterpret_cast<CuteQSidebarCall23>(taken[23]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::paintEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  int QListView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSidebarCall24 call = reinterpret_cast<CuteQSidebarCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::horizontalOffset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  int QListView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSidebarCall25 call = reinterpret_cast<CuteQSidebarCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::verticalOffset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSidebarCall26 call = reinterpret_cast<CuteQSidebarCall26>(taken[26]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QListView::setSelection(rect, command);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QRegion QListView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQSidebarCall27 call = reinterpret_cast<CuteQSidebarCall27>(taken[27]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRegionForSelection(selection);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::updateGeometries()
  void updateGeometries() override {
    if (taken[28]) {
      int handled = 0;
      CuteQSidebarCall28 call = reinterpret_cast<CuteQSidebarCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::updateGeometries();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  bool QListView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQSidebarCall29 call = reinterpret_cast<CuteQSidebarCall29>(taken[29]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListView::isIndexHidden(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSidebarCall30 call = reinterpret_cast<CuteQSidebarCall30>(taken[30]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QListView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSidebarCall31 call = reinterpret_cast<CuteQSidebarCall31>(taken[31]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QListView::currentChanged(current, previous);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
  //  QSize QListView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQSidebarCall32 call = reinterpret_cast<CuteQSidebarCall32>(taken[32]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QListView::viewportSizeHint();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSidebarCall33 call = reinterpret_cast<CuteQSidebarCall33>(taken[33]);
      call(this, model, &handled);
      if (handled) return;
    }
    QAbstractItemView::setModel(model);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSidebarCall34 call = reinterpret_cast<CuteQSidebarCall34>(taken[34]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QAbstractItemView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[35]) {
      int handled = 0;
      CuteQSidebarCall35 call = reinterpret_cast<CuteQSidebarCall35>(taken[35]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSidebarCall36 call = reinterpret_cast<CuteQSidebarCall36>(taken[36]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQSidebarCall37 call = reinterpret_cast<CuteQSidebarCall37>(taken[37]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForColumn(column);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSidebarCall38 call = reinterpret_cast<CuteQSidebarCall38>(taken[38]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQSidebarCall39 call = reinterpret_cast<CuteQSidebarCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[40]) {
      int handled = 0;
      CuteQSidebarCall40 call = reinterpret_cast<CuteQSidebarCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[41]) {
      int handled = 0;
      CuteQSidebarCall41 call = reinterpret_cast<CuteQSidebarCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[42]) {
      int handled = 0;
      CuteQSidebarCall42 call = reinterpret_cast<CuteQSidebarCall42>(taken[42]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[43]) {
      int handled = 0;
      CuteQSidebarCall43 call = reinterpret_cast<CuteQSidebarCall43>(taken[43]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[44]) {
      int handled = 0;
      CuteQSidebarCall44 call = reinterpret_cast<CuteQSidebarCall44>(taken[44]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[45]) {
      int handled = 0;
      CuteQSidebarCall45 call = reinterpret_cast<CuteQSidebarCall45>(taken[45]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[46]) {
      int handled = 0;
      CuteQSidebarCall46 call = reinterpret_cast<CuteQSidebarCall46>(taken[46]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::closeEditor(QWidget *editor,
  //      QAbstractItemDelegate::EndEditHint hint)
  void closeEditor(
      QWidget *editor,
      QAbstractItemDelegate::EndEditHint hint) override {
    if (taken[47]) {
      int handled = 0;
      CuteQSidebarCall47 call = reinterpret_cast<CuteQSidebarCall47>(taken[47]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[48]) {
      int handled = 0;
      CuteQSidebarCall48 call = reinterpret_cast<CuteQSidebarCall48>(taken[48]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[49]) {
      int handled = 0;
      CuteQSidebarCall49 call = reinterpret_cast<CuteQSidebarCall49>(taken[49]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::editorDestroyed(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
  //      trigger, QEvent *event)
  bool edit(
      const QModelIndex &index,
      QAbstractItemView::EditTrigger trigger,
      QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQSidebarCall50 call = reinterpret_cast<CuteQSidebarCall50>(taken[50]);
      bool given = call(this, &index, static_cast<int>(trigger), event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::edit(index, trigger, event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QItemSelectionModel::SelectionFlags
  //      QAbstractItemView::selectionCommand(const QModelIndex &index,
  //      const QEvent *event) const
  QItemSelectionModel::SelectionFlags selectionCommand(
      const QModelIndex &index,
      const QEvent *event) const override {
    if (taken[51]) {
      int handled = 0;
      CuteQSidebarCall51 call = reinterpret_cast<CuteQSidebarCall51>(taken[51]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[52]) {
      int handled = 0;
      CuteQSidebarCall52 call = reinterpret_cast<CuteQSidebarCall52>(taken[52]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQSidebarCall53 call = reinterpret_cast<CuteQSidebarCall53>(taken[53]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::viewportEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQSidebarCall54 call = reinterpret_cast<CuteQSidebarCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQSidebarCall55 call = reinterpret_cast<CuteQSidebarCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQSidebarCall56 call = reinterpret_cast<CuteQSidebarCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQSidebarCall57 call = reinterpret_cast<CuteQSidebarCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQSidebarCall58 call = reinterpret_cast<CuteQSidebarCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQSidebarCall59 call = reinterpret_cast<CuteQSidebarCall59>(taken[59]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQSidebarCall60 call = reinterpret_cast<CuteQSidebarCall60>(taken[60]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[61]) {
      int handled = 0;
      CuteQSidebarCall61 call = reinterpret_cast<CuteQSidebarCall61>(taken[61]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQSidebarCall62 call = reinterpret_cast<CuteQSidebarCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQSidebarCall63 call = reinterpret_cast<CuteQSidebarCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQSidebarCall64 call = reinterpret_cast<CuteQSidebarCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQSidebarCall65 call = reinterpret_cast<CuteQSidebarCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQSidebarCall66 call = reinterpret_cast<CuteQSidebarCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQSidebarCall67 call = reinterpret_cast<CuteQSidebarCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQSidebarCall68 call = reinterpret_cast<CuteQSidebarCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQSidebarCall69 call = reinterpret_cast<CuteQSidebarCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQSidebarCall70 call = reinterpret_cast<CuteQSidebarCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQSidebarCall71 call = reinterpret_cast<CuteQSidebarCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQSidebarCall72 call = reinterpret_cast<CuteQSidebarCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQSidebarCall73 call = reinterpret_cast<CuteQSidebarCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQSidebarCall74 call = reinterpret_cast<CuteQSidebarCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQSidebarCall75 call = reinterpret_cast<CuteQSidebarCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQSidebarCall76 call = reinterpret_cast<CuteQSidebarCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQSidebarCall77 call = reinterpret_cast<CuteQSidebarCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQSidebarCall78 call = reinterpret_cast<CuteQSidebarCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQSidebarCall79 call = reinterpret_cast<CuteQSidebarCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQSidebarCall80 call = reinterpret_cast<CuteQSidebarCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQSidebarCall81 call = reinterpret_cast<CuteQSidebarCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQSidebarCall82 call = reinterpret_cast<CuteQSidebarCall82>(taken[82]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[83]) {
      int handled = 0;
      CuteQSidebarCall83 call = reinterpret_cast<CuteQSidebarCall83>(taken[83]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQSidebarCall84 call = reinterpret_cast<CuteQSidebarCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[85]) {
      int handled = 0;
      CuteQSidebarCall85 call = reinterpret_cast<CuteQSidebarCall85>(taken[85]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQSidebarCall86 call = reinterpret_cast<CuteQSidebarCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSidebar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QSidebar10metaObjectEv(const QSidebar *self) {
  return self->metaObject();
}

//  void *QSidebar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QSidebar11qt_metacastEPKc(QSidebar *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSidebar::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QSidebar11qt_metacallEN11QMetaObject4CallEiPPv(
    QSidebar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(menu)
//  QString QSidebar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSidebar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSidebar::tr(s, c, n));
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(draganddrop)

//  void QSidebar::goToUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar7goToUrlERK4QUrl(QSidebar *self, const QUrl *url) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSidebar")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "goToUrl(const QUrl &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "goToUrl(const QUrl &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(url)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(menu)
//  QSidebar::QSidebar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSidebar *ritual_ZN8QSidebarC1EP7QWidget(QWidget *parent) {
  return new CuteQSidebar(parent);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(menu)
#if defined(Q_OS_LINUX)
//  void QSidebar::setModelAndUrls(QFileSystemModel *model, const QList<QUrl>
//      &newUrls)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar15setModelAndUrlsEP16QFileSystemModelRK5QListI4QUrlE(
    QSidebar *self,
    QFileSystemModel *model,
    const QList<QUrl> *newUrls) {
  self->setModelAndUrls(model, *newUrls);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(draganddrop)

//  QSidebar::~QSidebar()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebarD1Ev(QSidebar *self) {
  delete self;
}

//  QSize QSidebar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QSidebar8sizeHintEv(const QSidebar *self) {
  return new QSize(self->sizeHint());
}

#if defined(Q_OS_LINUX)
//  void QSidebar::setUrls(const QList<QUrl> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar7setUrlsERK5QListI4QUrlE(
    QSidebar *self,
    const QList<QUrl> *list) {
  self->setUrls(*list);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QSidebar::addUrls(const QList<QUrl> &list, int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar7addUrlsERK5QListI4QUrlEi(
    QSidebar *self,
    const QList<QUrl> *list,
    int row) {
  self->addUrls(*list, row);
}
#endif  // defined(Q_OS_LINUX)

//  QList<QUrl> QSidebar::urls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK8QSidebar4urlsEv(const QSidebar *self) {
  return new QList<QUrl>(self->urls());
}

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(menu)
//  void QSidebar::selectUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar9selectUrlERK4QUrl(QSidebar *self, const QUrl *url) {
  self->selectUrl(*url);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(draganddrop)

//  bool QSidebar::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QSidebar5eventEP6QEvent(QSidebar *self, QEvent *e) {
  return self->event(e);
}

//  void QSidebar::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar12focusInEventEP11QFocusEvent(
    QSidebar *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

#if QT_CONFIG(draganddrop)
//  void QSidebar::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar14dragEnterEventEP15QDragEnterEvent(
    QSidebar *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(menu)
//  void QSidebar::showContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar15showContextMenuERK6QPoint(
    QSidebar *self,
    const QPoint *position) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSidebar")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "showContextMenu(const QPoint &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "showContextMenu(const QPoint &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(position)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(menu)

//  void QSidebar::removeEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSidebar11removeEntryEv(QSidebar *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSidebar")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeEntry()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeEntry()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQSidebar, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSidebar(QSidebar *self, const char *key, void *call) {
  return static_cast<CuteQSidebar *>(self)->take(key, call);
}

//  QSize QSidebar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK8QSidebar8sizeHintEv(const QSidebar *self) {
  return new QSize(self->QSidebar::sizeHint());
}

//  bool QSidebar::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QSidebar5eventEP6QEvent(QSidebar *self, QEvent *e) {
  return static_cast<OwnQSidebar *>(self)->OwnQSidebar::event(e);
}

//  void QSidebar::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QSidebar12focusInEventEP11QFocusEvent(
    QSidebar *self,
    QFocusEvent *event) {
  static_cast<OwnQSidebar *>(self)->OwnQSidebar::focusInEvent(event);
}

#if QT_CONFIG(draganddrop)
//  void QSidebar::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QSidebar14dragEnterEventEP15QDragEnterEvent(
    QSidebar *self,
    QDragEnterEvent *event) {
  static_cast<OwnQSidebar *>(self)->OwnQSidebar::dragEnterEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(filedialog)
