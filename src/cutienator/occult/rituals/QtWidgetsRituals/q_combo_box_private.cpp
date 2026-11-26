//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcombobox_p.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlistview.h>
#if QT_CONFIG(tableview)
#include <QtWidgets/qtableview.h>
#endif
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qmap.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#endif
#include <QtWidgets/qheaderview.h>
#include <QtCore/qmath.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(proxymodel)
#include <QtCore/qabstractproxymodel.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qlineedit_p.h>
#if QT_CONFIG(completer)
#include <QtWidgets/private/qcompleter_p.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(effects)
# include <QtWidgets/private/qeffects_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qpainter.h>
#include <QtCore/qpointer.h>
#include <array>
#include <chrono>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmapcache.h>
#include <QtCore/qset.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/private/qstyle_p.h>
#include <QtWidgets/private/qstylehelper_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#ifndef QT_NO_DEBUG
#include <QtCore/qdebug.h>
#endif
#include <QtCore/q20utility.h>
#include <limits.h>
#include <algorithm>
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

//  from src/widgets/widgets/qcombobox.cpp, line 384, as _ZN17QComboBoxDelegateC1EP7QObjectP9QComboBox
inline QComboBoxDelegate::QComboBoxDelegate(QObject *parent, QComboBox *cmb)
    : QStyledItemDelegate(parent),
      mCombo(cmb)
{}

//  from src/widgets/widgets/qcombobox.cpp, line 74, as _ZN17QComboBoxListViewC1EP9QComboBox
inline QComboBoxListView::QComboBoxListView(QComboBox *cmb) : combo(cmb)
{
    if (cmb)
        setScreen(cmb->screen());
}

//  from src/widgets/widgets/qcombobox.cpp, line 227, as _ZN18QComboMenuDelegateC1EP7QObjectP9QComboBox
inline QComboMenuDelegate::QComboMenuDelegate(QObject *parent, QComboBox *cmb)
    : QAbstractItemDelegate(parent), mCombo(cmb), pressedIndex(-1)
{
}

//  from src/widgets/styles/qstyle.cpp, line 2475, as _ZN13QStylePrivate21useFullScreenForPopupEv
inline bool QStylePrivate::useFullScreenForPopup()
{
    auto theme = QGuiApplicationPrivate::platformTheme();
    return theme && theme->themeHint(QPlatformTheme::UseFullScreenForPopupMenu).toBool();
}

//  from src/widgets/widgets/qcombobox.cpp, line 205, as _ZN16QComboBoxPrivateC1Ev
inline QComboBoxPrivate::QComboBoxPrivate()
    : QWidgetPrivate(),
      shownOnce(false),
      duplicatesEnabled(false),
      frame(true),
      inserting(false),
      hidingPopup(false)
{
}

//  from src/widgets/widgets/qcombobox.cpp, line 215, as _ZN16QComboBoxPrivateD1Ev
#if defined(Q_OS_LINUX)
inline QComboBoxPrivate::~QComboBoxPrivate()
{
    disconnectModel();
#ifdef Q_OS_MACOS
    cleanupNativePopup();
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qcombobox.cpp, line 1292, as _ZN16QComboBoxPrivate4initEv
#if defined(Q_OS_LINUX)
inline void QComboBoxPrivate::init()
{
    Q_Q(QComboBox);
#ifdef Q_OS_MACOS
    // On OS X, only line edits and list views always get tab focus. It's only
    // when we enable full keyboard access that other controls can get tab focus.
    // When it's not editable, a combobox looks like a button, and it behaves as
    // such in this respect.
    if (!q->isEditable())
        q->setFocusPolicy(Qt::TabFocus);
    else
#endif
        q->setFocusPolicy(Qt::WheelFocus);

    q->setSizePolicy(QSizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed,
                                 QSizePolicy::ComboBox));
    setLayoutItemMargins(QStyle::SE_ComboBoxLayoutItem);
    q->setModel(new QStandardItemModel(0, 1, q));
    if (!q->isEditable())
        q->setAttribute(Qt::WA_InputMethodEnabled, false);
    else
        q->setAttribute(Qt::WA_InputMethodEnabled);
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qcombobox.cpp, line 1316, as _ZN16QComboBoxPrivate13viewContainerEv
inline QComboBoxPrivateContainer* QComboBoxPrivate::viewContainer()
{
    if (container)
        return container;

    Q_Q(QComboBox);
    container = new QComboBoxPrivateContainer(new QComboBoxListView(q), q);
    disconnectModel();
    container->itemView()->setModel(model);
    connectModel();
    container->itemView()->setTextElideMode(Qt::ElideMiddle);
    updateDelegate(true);
    updateLayoutDirection();
    updateViewContainerPaletteAndOpacity();
    QObjectPrivate::connect(container, &QComboBoxPrivateContainer::itemSelected,
                            this, &QComboBoxPrivate::itemSelected);
    QObjectPrivate::connect(container->itemView()->selectionModel(),
                            &QItemSelectionModel::currentChanged,
                            this, &QComboBoxPrivate::emitHighlighted);
    QObjectPrivate::connect(container, &QComboBoxPrivateContainer::resetButton,
                            this, &QComboBoxPrivate::resetButton);
    return container;
}

//  from src/widgets/widgets/qcombobox.cpp, line 1530, as _ZN16QComboBoxPrivate22updateLineEditGeometryEv
inline void QComboBoxPrivate::updateLineEditGeometry()
{
    if (!lineEdit)
        return;

    Q_Q(QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    QRect editRect = q->style()->subControlRect(QStyle::CC_ComboBox, &opt,
                                                QStyle::SC_ComboBoxEditField, q);
    if (currentIndex.isValid() && !q->itemIcon(q->currentIndex()).isNull()) {
        QRect comboRect(editRect);
        editRect.setWidth(editRect.width() - q->iconSize().width() - 4);
        editRect = QStyle::alignedRect(q->layoutDirection(), Qt::AlignRight,
                                       editRect.size(), comboRect);
    }
    lineEdit->setGeometry(editRect);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1549, as _ZNK16QComboBoxPrivate10matchFlagsEv
inline Qt::MatchFlags QComboBoxPrivate::matchFlags() const
{
    // Base how duplicates are determined on the autocompletion case sensitivity
    Qt::MatchFlags flags = Qt::MatchFixedString;
#if QT_CONFIG(completer)
    if (!lineEdit->completer() || lineEdit->completer()->caseSensitivity() == Qt::CaseSensitive)
#endif
        flags |= Qt::MatchCaseSensitive;
    return flags;
}

//  from src/widgets/widgets/qcombobox.cpp, line 1561, as _ZN16QComboBoxPrivate15editingFinishedEv
inline void QComboBoxPrivate::editingFinished()
{
    Q_Q(QComboBox);
    if (!lineEdit)
        return;
    const auto leText = lineEdit->text();
    if (!leText.isEmpty() && itemText(currentIndex) != leText) {
#if QT_CONFIG(completer)
        const auto *leCompleter = lineEdit->completer();
        const auto *popup = leCompleter ? QCompleterPrivate::get(leCompleter)->popup : nullptr;
        if (popup && popup->isVisible()) {
            // QLineEdit::editingFinished() will be emitted before the code flow returns
            // to QCompleter::eventFilter(), where QCompleter::activated() may be emitted.
            // We know that the completer popup will still be visible at this point, and
            // that any selection should be valid.
            const QItemSelectionModel *selModel = popup->selectionModel();
            const QModelIndex curIndex = popup->currentIndex();
            const bool completerIsActive = selModel && selModel->selectedIndexes().contains(curIndex);

            if (completerIsActive)
                return;
        }
#endif
        const int index = q_func()->findText(leText, matchFlags());
        if (index != -1) {
            q->setCurrentIndex(index);
            emitActivated(currentIndex);
        }
    }

}

//  from src/widgets/widgets/qcombobox.cpp, line 1593, as _ZN16QComboBoxPrivate13returnPressedEv
inline void QComboBoxPrivate::returnPressed()
{
    Q_Q(QComboBox);

    // The insertion code below does not apply when the policy is QComboBox::NoInsert.
    // In case a completer is installed, item activation via the completer is handled
    // in completerActivated(). Otherwise editingFinished() updates the current
    // index as appropriate.
    if (insertPolicy == QComboBox::NoInsert)
        return;

    if (lineEdit && !lineEdit->text().isEmpty()) {
        if (q->count() >= maxCount && !(this->insertPolicy == QComboBox::InsertAtCurrent))
            return;
        lineEdit->deselect();
        lineEdit->end(false);
        QString text = lineEdit->text();
        // check for duplicates (if not enabled) and quit
        int index = -1;
        if (!duplicatesEnabled) {
            index = q->findText(text, matchFlags());
            if (index != -1) {
                q->setCurrentIndex(index);
                emitActivated(currentIndex);
                return;
            }
        }
        switch (insertPolicy) {
        case QComboBox::InsertAtTop:
            index = 0;
            break;
        case QComboBox::InsertAtBottom:
            index = q->count();
            break;
        case QComboBox::InsertAtCurrent:
        case QComboBox::InsertAfterCurrent:
        case QComboBox::InsertBeforeCurrent:
            if (!q->count() || !currentIndex.isValid())
                index = 0;
            else if (insertPolicy == QComboBox::InsertAtCurrent)
                q->setItemText(q->currentIndex(), text);
            else if (insertPolicy == QComboBox::InsertAfterCurrent)
                index = q->currentIndex() + 1;
            else if (insertPolicy == QComboBox::InsertBeforeCurrent)
                index = q->currentIndex();
            break;
        case QComboBox::InsertAlphabetically:
            index = 0;
            for (int i = 0; i < q->count(); ++i, ++index) {
                if (text.toLower() < q->itemText(i).toLower())
                    break;
            }
            break;
        default:
            break;
        }
        if (index >= 0) {
            q->insertItem(index, text);
            q->setCurrentIndex(index);
            emitActivated(currentIndex);
        }
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 1657, as _ZN16QComboBoxPrivate12itemSelectedERK11QModelIndex
inline void QComboBoxPrivate::itemSelected(const QModelIndex &item)
{
    Q_Q(QComboBox);
    if (item != currentIndex) {
        setCurrentIndex(item);
    } else if (lineEdit) {
        lineEdit->selectAll();
        lineEdit->setText(q->itemText(currentIndex.row()));
    }
    emitActivated(currentIndex);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1669, as _ZN16QComboBoxPrivate13emitActivatedERK11QModelIndex
inline void QComboBoxPrivate::emitActivated(const QModelIndex &index)
{
    Q_Q(QComboBox);
    if (!index.isValid())
        return;
    QString text(itemText(index));
    emit q->activated(index.row());
    emit q->textActivated(text);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1679, as _ZN16QComboBoxPrivate15emitHighlightedERK11QModelIndex
inline void QComboBoxPrivate::emitHighlighted(const QModelIndex &index)
{
    Q_Q(QComboBox);
    if (!index.isValid())
        return;
    QString text(itemText(index));
    emit q->highlighted(index.row());
    emit q->textHighlighted(text);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1689, as _ZN16QComboBoxPrivate23emitCurrentIndexChangedERK11QModelIndex
inline void QComboBoxPrivate::emitCurrentIndexChanged(const QModelIndex &index)
{
    Q_Q(QComboBox);
    const QString text = itemText(index);
    emit q->currentIndexChanged(index.row());
    // signal lineEdit.textChanged already connected to signal currentTextChanged, so don't emit double here
    if (!lineEdit)
        updateCurrentText(text);
#if QT_CONFIG(accessibility)
    QAccessibleValueChangeEvent event(q, text);
    QAccessible::updateAccessibility(&event);
#endif
}

//  from src/widgets/widgets/qcombobox.cpp, line 487, as _ZN16QComboBoxPrivate14modelDestroyedEv
inline void QComboBoxPrivate::modelDestroyed()
{
    model = QAbstractItemModelPrivate::staticEmptyModel();
}

//  from src/widgets/widgets/qcombobox.cpp, line 475, as _ZN16QComboBoxPrivate10modelResetEv
inline void QComboBoxPrivate::modelReset()
{
    Q_Q(QComboBox);
    if (lineEdit) {
        lineEdit->setText(QString());
        updateLineEditGeometry();
    }
    trySetValidIndex();
    modelChanged();
    q->update();
}

//  from src/widgets/widgets/qcombobox.cpp, line 435, as _ZN16QComboBoxPrivate18completerActivatedERK11QModelIndex
#if QT_CONFIG(completer)
inline void QComboBoxPrivate::completerActivated(const QModelIndex &index)
{
    Q_Q(QComboBox);
#if QT_CONFIG(proxymodel)
    if (index.isValid() && q->completer()) {
        QAbstractProxyModel *proxy = qobject_cast<QAbstractProxyModel *>(q->completer()->completionModel());
        if (proxy) {
            const QModelIndex &completerIndex = proxy->mapToSource(index);
            int row = -1;
            if (completerIndex.model() == model) {
                row = completerIndex.row();
            } else {
                // if QCompleter uses a proxy model to host widget's one - map again
                QAbstractProxyModel *completerProxy = qobject_cast<QAbstractProxyModel *>(q->completer()->model());
                if (completerProxy && completerProxy->sourceModel() == model) {
                    row = completerProxy->mapToSource(completerIndex).row();
                } else {
                    QString match = q->completer()->model()->data(completerIndex).toString();
                    row = q->findText(match, matchFlags());
                }
            }
            q->setCurrentIndex(row);
            emitActivated(currentIndex);
        }
    }
#endif
}
#endif  // QT_CONFIG(completer)

//  from src/widgets/widgets/qcombobox.cpp, line 1341, as _ZN16QComboBoxPrivate11resetButtonEv
inline void QComboBoxPrivate::resetButton()
{
    updateArrow(QStyle::State_None);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1346, as _ZN16QComboBoxPrivate11dataChangedERK11QModelIndexS2_
inline void QComboBoxPrivate::dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight)
{
    Q_Q(QComboBox);
    if (inserting || topLeft.parent() != root)
        return;

    if (sizeAdjustPolicy == QComboBox::AdjustToContents) {
        sizeHint = QSize();
        adjustComboBoxSize();
        q->updateGeometry();
    }

    if (currentIndex.row() >= topLeft.row() && currentIndex.row() <= bottomRight.row()) {
        const QString text = q->itemText(currentIndex.row());
        if (lineEdit) {
            lineEdit->setText(text);
            updateLineEditGeometry();
        } else {
            updateCurrentText(text);
        }
        q->update();
#if QT_CONFIG(accessibility)
        QAccessibleValueChangeEvent event(q, text);
        QAccessible::updateAccessibility(&event);
#endif
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 1408, as _ZN16QComboBoxPrivate23updateIndexBeforeChangeEv
inline void QComboBoxPrivate::updateIndexBeforeChange()
{
    indexBeforeChange = currentIndex.row();
}

//  from src/widgets/widgets/qcombobox.cpp, line 1374, as _ZN16QComboBoxPrivate12rowsInsertedERK11QModelIndexii
inline void QComboBoxPrivate::rowsInserted(const QModelIndex &parent, int start, int end)
{
    Q_Q(QComboBox);
    if (inserting || parent != root)
        return;

    if (sizeAdjustPolicy == QComboBox::AdjustToContents) {
        sizeHint = QSize();
        adjustComboBoxSize();
        q->updateGeometry();
    }

    // set current index if combo was previously empty and there is no placeholderText
    if (start == 0 && (end - start + 1) == q->count() && !currentIndex.isValid() &&
        placeholderText.isEmpty()) {
#if QT_CONFIG(accessibility)
        // This might have been called by the model emitting rowInserted(), at which
        // point the view won't have updated the accessibility bridge yet about its new
        // dimensions. Do it now so that the change of the selection matches the row
        // indexes of the accessibility bridge's representation.
        if (container && container->itemView()) {
            QAccessibleTableModelChangeEvent event(container->itemView(),
                                                   QAccessibleTableModelChangeEvent::ModelReset);
            QAccessible::updateAccessibility(&event);
        }
#endif
        q->setCurrentIndex(0);
        // need to emit changed if model updated index "silently"
    } else if (currentIndex.row() != indexBeforeChange) {
        q->update();
        emitCurrentIndexChanged(currentIndex);
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 1413, as _ZN16QComboBoxPrivate11rowsRemovedERK11QModelIndexii
inline void QComboBoxPrivate::rowsRemoved(const QModelIndex &parent, int /*start*/, int /*end*/)
{
    Q_Q(QComboBox);
    if (parent != root)
        return;

    if (sizeAdjustPolicy == QComboBox::AdjustToContents) {
        sizeHint = QSize();
        adjustComboBoxSize();
        q->updateGeometry();
    }

    // model has removed the last row
    if (model->rowCount(root) == 0) {
        setCurrentIndex(QModelIndex());
        return;
    }

    // model has changed the currentIndex
    if (currentIndex.row() != indexBeforeChange) {
        if (!currentIndex.isValid() && q->count()) {
            q->setCurrentIndex(qMin(q->count() - 1, qMax(indexBeforeChange, 0)));
            return;
        }
        if (lineEdit) {
            lineEdit->setText(q->itemText(currentIndex.row()));
            updateLineEditGeometry();
        }
        q->update();
        emitCurrentIndexChanged(currentIndex);
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 464, as _ZN16QComboBoxPrivate11updateArrowEN6QStyle9StateFlagE
inline void QComboBoxPrivate::updateArrow(QStyle::StateFlag state)
{
    Q_Q(QComboBox);
    if (arrowState == state)
        return;
    arrowState = state;
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    q->update(q->rect());
}

//  from src/widgets/widgets/qcombobox.cpp, line 519, as _ZN16QComboBoxPrivate18updateHoverControlERK6QPoint
inline bool QComboBoxPrivate::updateHoverControl(const QPoint &pos)
{

    Q_Q(QComboBox);
    QRect lastHoverRect = hoverRect;
    QStyle::SubControl lastHoverControl = hoverControl;
    bool doesHover = q->testAttribute(Qt::WA_Hover);
    if (lastHoverControl != newHoverControl(pos) && doesHover) {
        q->update(lastHoverRect);
        q->update(hoverRect);
        return true;
    }
    return !doesHover;
}

//  from src/widgets/widgets/qcombobox.cpp, line 492, as _ZN16QComboBoxPrivate16trySetValidIndexEv
inline void QComboBoxPrivate::trySetValidIndex()
{
    Q_Q(QComboBox);
    bool currentReset = false;

    const int rowCount = q->count();
    for (int pos = 0; pos < rowCount; ++pos) {
        const QModelIndex idx(model->index(pos, modelColumn, root));
        if (idx.flags() & Qt::ItemIsEnabled) {
            setCurrentIndex(idx);
            currentReset = true;
            break;
        }
    }

    if (!currentReset)
        setCurrentIndex(QModelIndex());
}

//  from src/widgets/widgets/qcombobox.cpp, line 511, as _ZNK16QComboBoxPrivate13popupGeometryERK6QPoint
inline QRect QComboBoxPrivate::popupGeometry(const QPoint &globalPosition) const
{
    Q_Q(const QComboBox);
    return QStylePrivate::useFullScreenForPopup()
        ? QWidgetPrivate::screenGeometry(q, globalPosition)
        : QWidgetPrivate::availableScreenGeometry(q, globalPosition);
}

//  from src/widgets/widgets/qcombobox.cpp, line 534, as _ZN16QComboBoxPrivate15newHoverControlERK6QPoint
inline QStyle::SubControl QComboBoxPrivate::newHoverControl(const QPoint &pos)
{
    Q_Q(QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    opt.subControls = QStyle::SC_All;
    hoverControl = q->style()->hitTestComplexControl(QStyle::CC_ComboBox, &opt, pos, q);
    hoverRect = (hoverControl != QStyle::SC_None)
                   ? q->style()->subControlRect(QStyle::CC_ComboBox, &opt, hoverControl, q)
                   : QRect();
    return hoverControl;
}

//  from src/widgets/widgets/qcombobox.cpp, line 551, as _ZNK16QComboBoxPrivate16computeWidthHintEv
inline int QComboBoxPrivate::computeWidthHint() const
{
    Q_Q(const QComboBox);

    int width = 0;
    const int count = q->count();
    const int iconWidth = q->iconSize().width() + 4;
    const QFontMetrics &fontMetrics = q->fontMetrics();

    for (int i = 0; i < count; ++i) {
        const int textWidth = fontMetrics.horizontalAdvance(q->itemText(i));
        if (q->itemIcon(i).isNull())
            width = (qMax(width, textWidth));
        else
            width = (qMax(width, textWidth + iconWidth));
    }

    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    QSize tmp(width, 0);
    tmp = q->style()->sizeFromContents(QStyle::CT_ComboBox, &opt, tmp, q);
    return tmp.width();
}

//  from src/widgets/widgets/qcombobox.cpp, line 575, as _ZNK16QComboBoxPrivate17recomputeSizeHintER5QSize
inline QSize QComboBoxPrivate::recomputeSizeHint(QSize &sh) const
{
    Q_Q(const QComboBox);
    if (!sh.isValid()) {
        if (q->itemDelegate() && q->labelDrawingMode() == QComboBox::LabelDrawingMode::UseDelegate) {
            QStyleOptionViewItem option;
            initViewItemOption(&option);
            sh = q->itemDelegate()->sizeHint(option, currentIndex);
        }

        bool hasIcon = sizeAdjustPolicy == QComboBox::AdjustToMinimumContentsLengthWithIcon;
        int count = q->count();
        QSize iconSize = q->iconSize();
        const QFontMetrics &fm = q->fontMetrics();

        // text width
        if (&sh == &sizeHint || minimumContentsLength == 0) {
            switch (sizeAdjustPolicy) {
            case QComboBox::AdjustToContents:
            case QComboBox::AdjustToContentsOnFirstShow:
                if (count == 0) {
                    sh.rwidth() = 7 * fm.horizontalAdvance(u'x');
                } else {
                    for (int i = 0; i < count; ++i) {
                        if (!q->itemIcon(i).isNull()) {
                            hasIcon = true;
                            sh.setWidth(qMax(sh.width(), fm.boundingRect(q->itemText(i)).width() + iconSize.width() + 4));
                        } else {
                            sh.setWidth(qMax(sh.width(), fm.boundingRect(q->itemText(i)).width()));
                        }
                    }
                }
                break;
            case QComboBox::AdjustToMinimumContentsLengthWithIcon:
                ;
            }
        } else {
            for (int i = 0; i < count && !hasIcon; ++i)
                hasIcon = !q->itemIcon(i).isNull();
        }
        if (minimumContentsLength > 0) {
            auto r = qint64{minimumContentsLength} * fm.horizontalAdvance(u'X');
            if (hasIcon)
                r += iconSize.width() + 4;
            if (r <= QWIDGETSIZE_MAX) {
                sh.setWidth(qMax(sh.width(), int(r)));
            } else {
                qWarning("QComboBox: cannot take minimumContentsLength %d into account for sizeHint(), "
                         "since it causes the widget to be wider than QWIDGETSIZE_MAX. "
                         "Consider setting it to a less extreme value.",
                         minimumContentsLength);
            }
        }
        if (!placeholderText.isEmpty())
            sh.setWidth(qMax(sh.width(), fm.boundingRect(placeholderText).width()));


        // height
        sh.setHeight(qMax(qCeil(QFontMetricsF(fm).height()), 14) + 2);
        if (hasIcon) {
            sh.setHeight(qMax(sh.height(), iconSize.height() + 2));
        }

        // add style and strut values
        QStyleOptionComboBox opt;
        q->initStyleOption(&opt);
        sh = q->style()->sizeFromContents(QStyle::CT_ComboBox, &opt, sh, q);
    }
    return sh;
}

//  from src/widgets/widgets/qcombobox.cpp, line 646, as _ZN16QComboBoxPrivate18adjustComboBoxSizeEv
inline void QComboBoxPrivate::adjustComboBoxSize()
{
    viewContainer()->adjustSizeTimer.start(20, container);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1703, as _ZNK16QComboBoxPrivate8itemTextERK11QModelIndex
inline QString QComboBoxPrivate::itemText(const QModelIndex &index) const
{
    return index.isValid() ? model->data(index, itemRole()).toString() : QString();
}

//  from src/widgets/widgets/qcombobox.cpp, line 2046, as _ZNK16QComboBoxPrivate8itemIconERK11QModelIndex
inline QIcon QComboBoxPrivate::itemIcon(const QModelIndex &index) const
{
    if (!index.isValid())
        return {};
    QVariant decoration = model->data(index, Qt::DecorationRole);
    if (decoration.userType() == QMetaType::QPixmap)
        return QIcon(qvariant_cast<QPixmap>(decoration));
    else
        return qvariant_cast<QIcon>(decoration);
}

//  from src/widgets/widgets/qcombobox.cpp, line 1708, as _ZNK16QComboBoxPrivate8itemRoleEv
inline int QComboBoxPrivate::itemRole() const
{
    return q_func()->isEditable() ? Qt::EditRole : Qt::DisplayRole;
}

//  from src/widgets/widgets/qcombobox.cpp, line 651, as _ZN16QComboBoxPrivate21updateLayoutDirectionEv
inline void QComboBoxPrivate::updateLayoutDirection()
{
    Q_Q(const QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    Qt::LayoutDirection dir = Qt::LayoutDirection(
        q->style()->styleHint(QStyle::SH_ComboBox_LayoutDirection, &opt, q));
    if (lineEdit)
        lineEdit->setLayoutDirection(dir);
    if (container)
        container->setLayoutDirection(dir);
}

//  from src/widgets/widgets/qcombobox.cpp, line 2434, as _ZN16QComboBoxPrivate15setCurrentIndexERK11QModelIndex
inline void QComboBoxPrivate::setCurrentIndex(const QModelIndex &mi)
{
    Q_Q(QComboBox);

    QModelIndex normalized = mi.sibling(mi.row(), modelColumn); // no-op if mi.column() == modelColumn
    if (!normalized.isValid())
        normalized = mi;    // Fallback to passed index.

    bool indexChanged = (normalized != currentIndex);
    if (indexChanged)
        currentIndex = QPersistentModelIndex(normalized);
    if (lineEdit) {
        const QString newText = itemText(normalized);
        if (lineEdit->text() != newText) {
            lineEdit->setText(newText); // may cause lineEdit -> nullptr (QTBUG-54191)
#if QT_CONFIG(completer)
            if (lineEdit && lineEdit->completer())
                lineEdit->completer()->setCompletionPrefix(newText);
#endif
        }
        updateLineEditGeometry();
    }
    // If the model was reset to an empty one, currentIndex will be invalidated
    // (because it's a QPersistentModelIndex), but the index change will never
    // be advertised. So an explicit check for this condition is needed.
    // The variable used for that check has to be reset when a previously valid
    // index becomes invalid.
    const bool modelResetToEmpty = !normalized.isValid() && indexBeforeChange != -1;
    if (modelResetToEmpty)
        indexBeforeChange = -1;

    if (indexChanged || modelResetToEmpty) {
        QItemSelectionModel::SelectionFlags selectionMode = QItemSelectionModel::ClearAndSelect;
        if (q->view()->selectionBehavior() == QAbstractItemView::SelectRows)
            selectionMode.setFlag(QItemSelectionModel::Rows);
        if (auto *model = q->view()->selectionModel())
            model->setCurrentIndex(currentIndex, selectionMode);

        q->update();
        emitCurrentIndexChanged(currentIndex);
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 2032, as _ZN16QComboBoxPrivate14updateDelegateEb
inline void QComboBoxPrivate::updateDelegate(bool force)
{
    Q_Q(QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    if (q->style()->styleHint(QStyle::SH_ComboBox_Popup, &opt, q)) {
        if (force || qobject_cast<QComboBoxDelegate *>(q->itemDelegate()))
            q->setItemDelegate(new QComboMenuDelegate(q->view(), q));
    } else {
        if (force || qobject_cast<QComboMenuDelegate *>(q->itemDelegate()))
            q->setItemDelegate(new QComboBoxDelegate(q->view(), q));
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 1520, as _ZNK16QComboBoxPrivate18initViewItemOptionEP20QStyleOptionViewItem
inline void QComboBoxPrivate::initViewItemOption(QStyleOptionViewItem *option) const
{
    Q_Q(const QComboBox);
    q->view()->initViewItemOption(option);
    option->widget = q;
    option->index = currentIndex;
    option->text = q->currentText();
    option->icon = itemIcon(currentIndex);
}

//  from src/widgets/widgets/qcombobox.cpp, line 3667, as _ZN16QComboBoxPrivate20keyboardSearchStringERK7QString
inline void QComboBoxPrivate::keyboardSearchString(const QString &text)
{
    // use keyboardSearch from the listView so we do not duplicate code
    QAbstractItemView *view = viewContainer()->itemView();
    view->setCurrentIndex(currentIndex);
    int currentRow = view->currentIndex().row();
    view->keyboardSearch(text);
    if (currentRow != view->currentIndex().row()) {
        setCurrentIndex(view->currentIndex());
        emitActivated(currentIndex);
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 3680, as _ZN16QComboBoxPrivate12modelChangedEv
inline void QComboBoxPrivate::modelChanged()
{
    Q_Q(QComboBox);

    if (sizeAdjustPolicy == QComboBox::AdjustToContents) {
        sizeHint = QSize();
        adjustComboBoxSize();
        q->updateGeometry();
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 1447, as _ZN16QComboBoxPrivate36updateViewContainerPaletteAndOpacityEv
inline void QComboBoxPrivate::updateViewContainerPaletteAndOpacity()
{
    if (!container)
        return;
    Q_Q(QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
#if QT_CONFIG(menu)
    if (q->style()->styleHint(QStyle::SH_ComboBox_Popup, &opt, q)) {
        QMenu menu;
        menu.ensurePolished();
        container->setPalette(menu.palette());
        container->setWindowOpacity(menu.windowOpacity());
    } else
#endif
    {
        container->setPalette(q->palette());
        container->setWindowOpacity(1.0);
    }
    if (lineEdit)
        lineEdit->setPalette(q->palette());
}

//  from src/widgets/widgets/qcombobox.cpp, line 1470, as _ZN16QComboBoxPrivate17updateFocusPolicyEv
#if defined(Q_OS_LINUX)
inline void QComboBoxPrivate::updateFocusPolicy()
{
#ifdef Q_OS_MACOS
    Q_Q(QComboBox);

    // See comment in QComboBoxPrivate::init()
    if (q->isEditable())
        q->setFocusPolicy(Qt::WheelFocus);
    else
        q->setFocusPolicy(Qt::TabFocus);
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qcombobox.cpp, line 3434, as _ZN16QComboBoxPrivate23showPopupFromMouseEventEP11QMouseEvent
inline void QComboBoxPrivate::showPopupFromMouseEvent(QMouseEvent *e)
{
    Q_Q(QComboBox);
    QStyleOptionComboBox opt;
    q->initStyleOption(&opt);
    QStyle::SubControl sc = q->style()->hitTestComplexControl(QStyle::CC_ComboBox, &opt, e->position().toPoint(), q);

    if (e->button() == Qt::LeftButton
            && !(sc == QStyle::SC_None && e->type() == QEvent::MouseButtonRelease)
            && (sc == QStyle::SC_ComboBoxArrow || !q->isEditable())
            && !viewContainer()->isVisible()) {
        if (sc == QStyle::SC_ComboBoxArrow)
            updateArrow(QStyle::State_Sunken);
        // We've restricted the next couple of lines, because by not calling
        // viewContainer(), we avoid creating the QComboBoxPrivateContainer.
        viewContainer()->initialClickPosition = q->mapToGlobal(e->position());
        QPointer<QComboBox> guard = q;
        q->showPopup();
        if (!guard)
            return;
        // The code below ensures that regular mousepress and pick item still works
        // If it was not called the viewContainer would ignore event since it didn't have
        // a mousePressEvent first.
        if (viewContainer()) {
            viewContainer()->blockMouseReleaseTimer.start(QApplication::doubleClickInterval());
            viewContainer()->maybeIgnoreMouseButtonRelease = false;
        }
    } else {
        e->ignore();
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 3189, as _ZN16QComboBoxPrivate11doHidePopupEv
inline void QComboBoxPrivate::doHidePopup()
{
    if (container && container->isVisible())
        container->hide();

    resetButton();
}

//  from src/widgets/widgets/qcombobox.cpp, line 3197, as _ZN16QComboBoxPrivate17updateCurrentTextERK7QString
inline void QComboBoxPrivate::updateCurrentText(const QString &text)
{
    if (text == currentText)
        return;

    currentText = text;
    emit q_func()->currentTextChanged(text);
}

//  from src/widgets/widgets/qcombobox.cpp, line 2343, as _ZN16QComboBoxPrivate12connectModelEv
inline void QComboBoxPrivate::connectModel()
{
    if (!model)
        return;

    modelConnections = {
        QObjectPrivate::connect(model, &QAbstractItemModel::dataChanged,
                                this, &QComboBoxPrivate::dataChanged),
        QObjectPrivate::connect(model, &QAbstractItemModel::rowsAboutToBeInserted,
                                this, &QComboBoxPrivate::updateIndexBeforeChange),
        QObjectPrivate::connect(model, &QAbstractItemModel::rowsInserted,
                                this, &QComboBoxPrivate::rowsInserted),
        QObjectPrivate::connect(model, &QAbstractItemModel::rowsAboutToBeRemoved,
                                this, &QComboBoxPrivate::updateIndexBeforeChange),
        QObjectPrivate::connect(model, &QAbstractItemModel::rowsRemoved,
                                this, &QComboBoxPrivate::rowsRemoved),
        QObjectPrivate::connect(model, &QObject::destroyed,
                                this, &QComboBoxPrivate::modelDestroyed),
        QObjectPrivate::connect(model, &QAbstractItemModel::modelAboutToBeReset,
                                this, &QComboBoxPrivate::updateIndexBeforeChange),
        QObjectPrivate::connect(model, &QAbstractItemModel::modelReset,
                                this, &QComboBoxPrivate::modelReset)
    };
}

//  from src/widgets/widgets/qcombobox.cpp, line 2368, as _ZN16QComboBoxPrivate15disconnectModelEv
inline void QComboBoxPrivate::disconnectModel()
{
    for (auto &connection : modelConnections)
        QObject::disconnect(connection);
}
//  -----------------------------------------------------------------------

//  A QComboBoxPrivate that Python can take functions over in. Every QComboBoxPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQComboBoxPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQComboBoxPrivateCall1)(const void *, int, int *);
typedef void (*CuteQComboBoxPrivateCall2)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall3)(const void *, int *);
typedef void * (*CuteQComboBoxPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQComboBoxPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQComboBoxPrivateCall6)(const void *, int *);
typedef int (*CuteQComboBoxPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQComboBoxPrivateCall8)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall9)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall10)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall11)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall12)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall13)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall14)(const void *, int *);
typedef void (*CuteQComboBoxPrivateCall15)(const void *, int *);
typedef bool (*CuteQComboBoxPrivateCall16)(const void *, int *);
typedef bool (*CuteQComboBoxPrivateCall17)(const void *, int *);
class CuteQComboBoxPrivate : public QComboBoxPrivate {
public:
  using QComboBoxPrivate::QComboBoxPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxPrivateCall0 call = reinterpret_cast<CuteQComboBoxPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxPrivateCall1 call = reinterpret_cast<CuteQComboBoxPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboBoxPrivateCall2 call = reinterpret_cast<CuteQComboBoxPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboBoxPrivateCall3 call = reinterpret_cast<CuteQComboBoxPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQComboBoxPrivateCall4 call = reinterpret_cast<CuteQComboBoxPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQComboBoxPrivateCall5 call = reinterpret_cast<CuteQComboBoxPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQComboBoxPrivateCall6 call = reinterpret_cast<CuteQComboBoxPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQComboBoxPrivateCall7 call = reinterpret_cast<CuteQComboBoxPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQComboBoxPrivateCall8 call = reinterpret_cast<CuteQComboBoxPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQComboBoxPrivateCall9 call = reinterpret_cast<CuteQComboBoxPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQComboBoxPrivateCall10 call = reinterpret_cast<CuteQComboBoxPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQComboBoxPrivateCall11 call = reinterpret_cast<CuteQComboBoxPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQComboBoxPrivateCall12 call = reinterpret_cast<CuteQComboBoxPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQComboBoxPrivateCall13 call = reinterpret_cast<CuteQComboBoxPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboBoxPrivateCall14 call = reinterpret_cast<CuteQComboBoxPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQComboBoxPrivateCall15 call = reinterpret_cast<CuteQComboBoxPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQComboBoxPrivateCall16 call = reinterpret_cast<CuteQComboBoxPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQComboBoxPrivateCall17 call = reinterpret_cast<CuteQComboBoxPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QComboBox *QComboBoxPrivate::q_func()
extern "C" Q_DECL_EXPORT
QComboBox *ritual_ZN16QComboBoxPrivate6q_funcEv(QComboBoxPrivate *self) {
  return self->q_func();
}

//  const QComboBox *QComboBoxPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QComboBox *ritual_ZNK16QComboBoxPrivate6q_funcEv(
    const QComboBoxPrivate *self) {
  return self->q_func();
}

//  QComboBoxPrivate::QComboBoxPrivate()
extern "C" Q_DECL_EXPORT
QComboBoxPrivate *ritual_ZN16QComboBoxPrivateC1Ev() {
  return new CuteQComboBoxPrivate();
}

//  QComboBoxPrivate::~QComboBoxPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivateD1Ev(QComboBoxPrivate *self) {
  delete self;
}

#if defined(Q_OS_LINUX)
//  void QComboBoxPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate4initEv(QComboBoxPrivate *self) {
  self->init();
}
#endif  // defined(Q_OS_LINUX)

//  void QComboBoxPrivate::updateLineEditGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate22updateLineEditGeometryEv(
    QComboBoxPrivate *self) {
  self->updateLineEditGeometry();
}

//  Qt::MatchFlags QComboBoxPrivate::matchFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QComboBoxPrivate10matchFlagsEv(
    const QComboBoxPrivate *self) {
  return static_cast<int>(self->matchFlags().toInt());
}

//  void QComboBoxPrivate::editingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate15editingFinishedEv(QComboBoxPrivate *self) {
  self->editingFinished();
}

//  void QComboBoxPrivate::returnPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate13returnPressedEv(QComboBoxPrivate *self) {
  self->returnPressed();
}

//  void QComboBoxPrivate::itemSelected(const QModelIndex &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate12itemSelectedERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *item) {
  self->itemSelected(*item);
}

//  void QComboBoxPrivate::emitActivated(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate13emitActivatedERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *index) {
  self->emitActivated(*index);
}

//  void QComboBoxPrivate::emitHighlighted(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate15emitHighlightedERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *index) {
  self->emitHighlighted(*index);
}

//  void QComboBoxPrivate::emitCurrentIndexChanged(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate23emitCurrentIndexChangedERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *index) {
  self->emitCurrentIndexChanged(*index);
}

//  void QComboBoxPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate14modelDestroyedEv(QComboBoxPrivate *self) {
  self->modelDestroyed();
}

//  void QComboBoxPrivate::updateMicroFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate16updateMicroFocusEv(
    QComboBoxPrivate *self) {
  self->updateMicroFocus();
}

#if QT_CONFIG(completer)
//  void QComboBoxPrivate::completerActivated(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate18completerActivatedERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *index) {
  self->completerActivated(*index);
}
#endif  // QT_CONFIG(completer)

//  void QComboBoxPrivate::resetButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate11resetButtonEv(QComboBoxPrivate *self) {
  self->resetButton();
}

//  void QComboBoxPrivate::updateIndexBeforeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate23updateIndexBeforeChangeEv(
    QComboBoxPrivate *self) {
  self->updateIndexBeforeChange();
}

//  void QComboBoxPrivate::updateArrow(QStyle::StateFlag state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate11updateArrowEN6QStyle9StateFlagE(
    QComboBoxPrivate *self,
    QStyle::StateFlag state) {
  self->updateArrow(state);
}

//  bool QComboBoxPrivate::updateHoverControl(const QPoint &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QComboBoxPrivate18updateHoverControlERK6QPoint(
    QComboBoxPrivate *self,
    const QPoint *pos) {
  return self->updateHoverControl(*pos);
}

//  void QComboBoxPrivate::trySetValidIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate16trySetValidIndexEv(
    QComboBoxPrivate *self) {
  self->trySetValidIndex();
}

//  QRect QComboBoxPrivate::popupGeometry(const QPoint &globalPos) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QComboBoxPrivate13popupGeometryERK6QPoint(
    const QComboBoxPrivate *self,
    const QPoint *globalPos) {
  return new QRect(self->popupGeometry(*globalPos));
}

//  QStyle::SubControl QComboBoxPrivate::newHoverControl(const QPoint &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZN16QComboBoxPrivate15newHoverControlERK6QPoint(
    QComboBoxPrivate *self,
    const QPoint *pos) {
  return self->newHoverControl(*pos);
}

//  int QComboBoxPrivate::computeWidthHint() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QComboBoxPrivate16computeWidthHintEv(
    const QComboBoxPrivate *self) {
  return self->computeWidthHint();
}

//  QSize QComboBoxPrivate::recomputeSizeHint(QSize &sh) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QComboBoxPrivate17recomputeSizeHintER5QSize(
    const QComboBoxPrivate *self,
    QSize *sh) {
  return new QSize(self->recomputeSizeHint(*sh));
}

//  QString QComboBoxPrivate::itemText(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QComboBoxPrivate8itemTextERK11QModelIndex(
    const QComboBoxPrivate *self,
    const QModelIndex *index) {
  return new QString(self->itemText(*index));
}

//  QIcon QComboBoxPrivate::itemIcon(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QComboBoxPrivate8itemIconERK11QModelIndex(
    const QComboBoxPrivate *self,
    const QModelIndex *index) {
  return new QIcon(self->itemIcon(*index));
}

//  int QComboBoxPrivate::itemRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QComboBoxPrivate8itemRoleEv(const QComboBoxPrivate *self) {
  return self->itemRole();
}

//  void QComboBoxPrivate::updateLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate21updateLayoutDirectionEv(
    QComboBoxPrivate *self) {
  self->updateLayoutDirection();
}

//  void QComboBoxPrivate::setCurrentIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate15setCurrentIndexERK11QModelIndex(
    QComboBoxPrivate *self,
    const QModelIndex *index) {
  self->setCurrentIndex(*index);
}

//  void QComboBoxPrivate::updateDelegate(bool force)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate14updateDelegateEb(
    QComboBoxPrivate *self,
    bool force) {
  self->updateDelegate(force);
}

//  void QComboBoxPrivate::initViewItemOption(QStyleOptionViewItem *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QComboBoxPrivate18initViewItemOptionEP20QStyleOptionViewItem(
    const QComboBoxPrivate *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  void QComboBoxPrivate::updateViewContainerPaletteAndOpacity()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate36updateViewContainerPaletteAndOpacityEv(
    QComboBoxPrivate *self) {
  self->updateViewContainerPaletteAndOpacity();
}

#if defined(Q_OS_LINUX)
//  void QComboBoxPrivate::updateFocusPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate17updateFocusPolicyEv(
    QComboBoxPrivate *self) {
  self->updateFocusPolicy();
}
#endif  // defined(Q_OS_LINUX)

//  void QComboBoxPrivate::doHidePopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate11doHidePopupEv(QComboBoxPrivate *self) {
  self->doHidePopup();
}

//  void QComboBoxPrivate::updateCurrentText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate17updateCurrentTextERK7QString(
    QComboBoxPrivate *self,
    const QString *text) {
  self->updateCurrentText(*text);
}

//  void QComboBoxPrivate::disconnectModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QComboBoxPrivate15disconnectModelEv(QComboBoxPrivate *self) {
  self->disconnectModel();
}

//  a Python function taken by a CuteQComboBoxPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBoxPrivate(
    QComboBoxPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboBoxPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(combobox)
