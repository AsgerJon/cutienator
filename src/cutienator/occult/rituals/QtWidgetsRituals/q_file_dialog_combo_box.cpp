//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(filedialog)
#if QT_CONFIG(filedialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/qfiledialog.h>
#include <QtWidgets/private/qfiledialog_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qactiongroup.h>
#include <QtWidgets/qheaderview.h>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
#include <QtWidgets/qgridlayout.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <stdlib.h>
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(mimetype)
#include <QtCore/qmimedatabase.h>
#endif
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstylepainter.h>
#if defined(Q_OS_UNIX)
#include <pwd.h>
#include <unistd.h> // for pathconf() on OS X
#elif defined(Q_OS_WIN)
#  include <QtCore/qt_windows.h>
#endif
#if defined(Q_OS_WASM)
#include <QtGui/private/qwasmlocalfileaccess_p.h>
#endif
#include <algorithm>
#include <QtCore/QMetaEnum>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
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

//  from src/widgets/dialogs/qfiledialog.cpp, line 4052, as _ZN19QFileDialogComboBox9showPopupEv
inline void QFileDialogComboBox::showPopup()
{
    if (model()->rowCount() > 1)
        QComboBox::showPopup();

    urlModel->setUrls(QList<QUrl>());
    QList<QUrl> list;
    QModelIndex idx = d_ptr->model->index(d_ptr->rootPath());
    while (idx.isValid()) {
        QUrl url = QUrl::fromLocalFile(idx.data(QFileSystemModel::FilePathRole).toString());
        if (url.isValid())
            list.append(url);
        idx = idx.parent();
    }
    // add "my computer"
    list.append(QUrl("file:"_L1));
    urlModel->addUrls(list, 0);
    idx = model()->index(model()->rowCount() - 1, 0);

    // append history
    QList<QUrl> urls;
    for (int i = 0; i < m_history.size(); ++i) {
        QUrl path = QUrl::fromLocalFile(m_history.at(i));
        if (!urls.contains(path))
            urls.prepend(path);
    }
    if (urls.size() > 0) {
        model()->insertRow(model()->rowCount());
        idx = model()->index(model()->rowCount()-1, 0);
        // ### TODO maybe add a horizontal line before this
        model()->setData(idx, QFileDialog::tr("Recent Places"));
        QStandardItemModel *m = qobject_cast<QStandardItemModel*>(model());
        if (m) {
            Qt::ItemFlags flags = m->flags(idx);
            flags &= ~Qt::ItemIsEnabled;
            m->item(idx.row(), idx.column())->setFlags(flags);
        }
        urlModel->addUrls(urls, -1, false);
    }
    setCurrentIndex(0);

    QComboBox::showPopup();
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 4097, as _ZN19QFileDialogComboBox10paintEventEP11QPaintEvent
inline void QFileDialogComboBox::paintEvent(QPaintEvent *)
{
    QStylePainter painter(this);
    painter.setPen(palette().color(QPalette::Text));

    // draw the combobox frame, focusrect and selected etc.
    QStyleOptionComboBox opt;
    initStyleOption(&opt);

    QRect editRect = style()->subControlRect(QStyle::CC_ComboBox, &opt,
                                                QStyle::SC_ComboBoxEditField, this);
    int size = editRect.width() - opt.iconSize.width() - 4;
    opt.currentText = opt.fontMetrics.elidedText(opt.currentText, Qt::ElideMiddle, size);
    painter.drawComplexControl(QStyle::CC_ComboBox, opt);

    // draw the icon and text
    painter.drawControl(QStyle::CE_ComboBoxLabel, opt);
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

//  from src/widgets/dialogs/qsidebar.cpp, line 43, as _ZN9QUrlModelC1EP7QObject
inline QUrlModel::QUrlModel(QObject *parent) : QStandardItemModel(parent), showFullPath(false), fileSystemModel(nullptr)
{
}

//  from src/widgets/dialogs/qsidebar.cpp, line 217, as _ZN9QUrlModel7setUrlsERK5QListI4QUrlE
inline void QUrlModel::setUrls(const QList<QUrl> &list)
{
    removeRows(0, rowCount());
    invalidUrls.clear();
    watching.clear();
    addUrls(list, 0);
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

//  from src/widgets/dialogs/qfiledialog.cpp, line 4044, as _ZN19QFileDialogComboBox20setFileDialogPrivateEP18QFileDialogPrivate
inline void QFileDialogComboBox::setFileDialogPrivate(QFileDialogPrivate *d_pointer) {
    d_ptr = d_pointer;
    urlModel = new QUrlModel(this);
    urlModel->showFullPath = true;
    urlModel->setFileSystemModel(d_ptr->model);
    setModel(urlModel);
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 1904, as _ZN19QFileDialogComboBox10setHistoryERK5QListI7QStringE
inline void QFileDialogComboBox::setHistory(const QStringList &paths)
{
    m_history = paths;
    // Only populate the first item, showPopup will populate the rest if needed
    QList<QUrl> list;
    const QModelIndex idx = d_ptr->model->index(d_ptr->rootPath());
    //On windows the popup display the "C:\", convert to nativeSeparators
    const QUrl url = idx.isValid()
                   ? QUrl::fromLocalFile(QDir::toNativeSeparators(idx.data(QFileSystemModel::FilePathRole).toString()))
                   : QUrl("file:"_L1);
    if (url.isValid())
        list.append(url);
    urlModel->setUrls(list);
}
//  -----------------------------------------------------------------------

#if defined(Q_OS_LINUX)
//  QFileDialogComboBox::QFileDialogComboBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFileDialogComboBox *ritual_ZN19QFileDialogComboBoxC1EP7QWidget(
    QWidget *parent) {
  return new QFileDialogComboBox(parent);
}
#endif  // defined(Q_OS_LINUX)

//  void QFileDialogComboBox::setFileDialogPrivate(QFileDialogPrivate
//      *d_pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogComboBox20setFileDialogPrivateEP18QFileDialogPrivate(
    QFileDialogComboBox *self,
    QFileDialogPrivate *d_pointer) {
  self->setFileDialogPrivate(d_pointer);
}

//  void QFileDialogComboBox::showPopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogComboBox9showPopupEv(QFileDialogComboBox *self) {
  self->showPopup();
}

#if defined(Q_OS_LINUX)
//  void QFileDialogComboBox::setHistory(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogComboBox10setHistoryERK5QListI7QStringE(
    QFileDialogComboBox *self,
    const QList<QString> *paths) {
  self->setHistory(*paths);
}
#endif  // defined(Q_OS_LINUX)

//  QStringList QFileDialogComboBox::history() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QFileDialogComboBox7historyEv(
    const QFileDialogComboBox *self) {
  return new QList<QString>(self->history());
}

//  void QFileDialogComboBox::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogComboBox10paintEventEP11QPaintEvent(
    QFileDialogComboBox *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

#if defined(Q_OS_LINUX)
//  void QFileDialogComboBox::showPopup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogComboBox9showPopupEv(
    QFileDialogComboBox *self) {
  self->QFileDialogComboBox::showPopup();
}
#endif  // defined(Q_OS_LINUX)

//  void QFileDialogComboBox::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogComboBox10paintEventEP11QPaintEvent(
    QFileDialogComboBox *self,
    QPaintEvent *a0) {
  self->QFileDialogComboBox::paintEvent(a0);
}

#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(filedialog)
