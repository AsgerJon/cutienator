//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdialogbuttonbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdialogbuttonbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qabstractbutton.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qhash.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qdialog.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformdialoghelper.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qaction.h>
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtWidgets/private/qdialogbuttonbox_p.h>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 138, as _ZN23QDialogButtonBoxPrivateC1EN2Qt11OrientationE
inline QDialogButtonBoxPrivate::QDialogButtonBoxPrivate(Qt::Orientation orient)
    : orientation(orient), buttonLayout(nullptr), center(false)
{
    struct EventFilter : public QObject
    {
        EventFilter(QDialogButtonBoxPrivate *d) : d(d) {};

        bool eventFilter(QObject *obj, QEvent *event) override
        {
            QAbstractButton *button = qobject_cast<QAbstractButton *>(obj);
            return button ? d->handleButtonShowAndHide(button, event) : false;
        }

    private:
        QDialogButtonBoxPrivate *d;

    };

    filter.reset(new EventFilter(this));
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 437, as _ZN23QDialogButtonBoxPrivate21createStandardButtonsE6QFlagsIN16QDialogButtonBox14StandardButtonEE
inline void QDialogButtonBoxPrivate::createStandardButtons(QDialogButtonBox::StandardButtons buttons)
{
    uint i = QDialogButtonBox::FirstButton;
    while (i <= QDialogButtonBox::LastButton) {
        if (i & buttons)
            createButton(QDialogButtonBox::StandardButton(i), LayoutRule::SkipLayout);
        i = i << 1;
    }
    layoutButtons();
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 754, as _ZN23QDialogButtonBoxPrivate12removeButtonEP15QAbstractButtonNS_12RemoveReasonE
inline void QDialogButtonBoxPrivate::removeButton(QAbstractButton *button, RemoveReason reason)
{
    if (!button)
        return;

    // Remove button from hidden buttons and roles
    hiddenButtons.remove(button);
    for (int i = 0; i < QDialogButtonBox::NRoles; ++i)
        buttonLists[i].removeOne(button);

    switch (reason) {
    case RemoveReason::ManualRemove:
        button->setParent(nullptr);
        QObjectPrivate::disconnect(button, &QAbstractButton::clicked,
                                   this, &QDialogButtonBoxPrivate::handleButtonClicked);
        QObjectPrivate::disconnect(button, &QAbstractButton::destroyed,
                                   this, &QDialogButtonBoxPrivate::handleButtonDestroyed);
        button->removeEventFilter(filter.get());
        Q_FALLTHROUGH();
    case RemoveReason::Destroyed:
        standardButtonMap.remove(reinterpret_cast<QPushButton *>(button));
        break;
    case RemoveReason::HideEvent:
        break;
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 208, as _ZN23QDialogButtonBoxPrivate13layoutButtonsEv
inline void QDialogButtonBoxPrivate::layoutButtons()
{
    Q_Q(QDialogButtonBox);
    const int MacGap = 36 - 8;    // 8 is the default gap between a widget and a spacer item

    QScopedValueRollback blocker(ignoreShowAndHide, true);
    for (int i = buttonLayout->count() - 1; i >= 0; --i) {
        QLayoutItem *item = buttonLayout->takeAt(i);
        if (QWidget *widget = item->widget())
            widget->hide();
        delete item;
    }

    int tmpPolicy = layoutPolicy;

    static const int M = 5;
    static const int ModalRoles[M] = { QPlatformDialogHelper::AcceptRole, QPlatformDialogHelper::RejectRole,
        QPlatformDialogHelper::DestructiveRole, QPlatformDialogHelper::YesRole, QPlatformDialogHelper::NoRole };
    if (tmpPolicy == QDialogButtonBox::MacLayout) {
        bool hasModalButton = false;
        for (int i = 0; i < M; ++i) {
            if (!buttonLists[ModalRoles[i]].isEmpty()) {
                hasModalButton = true;
                break;
            }
        }
        if (!hasModalButton)
            tmpPolicy = 4;  // Mac modeless
    }

    const int *currentLayout = QPlatformDialogHelper::buttonLayout(
        orientation, static_cast<QPlatformDialogHelper::ButtonLayout>(tmpPolicy));

    if (center)
        buttonLayout->addStretch();

    const QList<QAbstractButton *> &acceptRoleList = buttonLists[QPlatformDialogHelper::AcceptRole];

    while (*currentLayout != QPlatformDialogHelper::EOL) {
        int role = (*currentLayout & ~QPlatformDialogHelper::Reverse);
        bool reverse = (*currentLayout & QPlatformDialogHelper::Reverse);

        switch (role) {
        case QPlatformDialogHelper::Stretch:
            if (!center)
                buttonLayout->addStretch();
            break;
        case QPlatformDialogHelper::AcceptRole: {
            if (acceptRoleList.isEmpty())
                break;
            // Only the first one
            QAbstractButton *button = acceptRoleList.first();
            buttonLayout->addWidget(button);
            button->show();
        }
            break;
        case QPlatformDialogHelper::AlternateRole:
            if (acceptRoleList.size() > 1)
                addButtonsToLayout(acceptRoleList.mid(1), reverse);
            break;
        case QPlatformDialogHelper::DestructiveRole:
            {
                const QList<QAbstractButton *> &list = buttonLists[role];

                /*
                    Mac: Insert a gap on the left of the destructive
                    buttons to ensure that they don't get too close to
                    the help and action buttons (but only if there are
                    some buttons to the left of the destructive buttons
                    (and the stretch, whence buttonLayout->count() > 1
                    and not 0)).
                */
                if (tmpPolicy == QDialogButtonBox::MacLayout
                        && !list.isEmpty() && buttonLayout->count() > 1)
                    buttonLayout->addSpacing(MacGap);

                addButtonsToLayout(list, reverse);

                /*
                    Insert a gap between the destructive buttons and the
                    accept and reject buttons.
                */
                if (tmpPolicy == QDialogButtonBox::MacLayout && !list.isEmpty())
                    buttonLayout->addSpacing(MacGap);
            }
            break;
        case QPlatformDialogHelper::RejectRole:
        case QPlatformDialogHelper::ActionRole:
        case QPlatformDialogHelper::HelpRole:
        case QPlatformDialogHelper::YesRole:
        case QPlatformDialogHelper::NoRole:
        case QPlatformDialogHelper::ApplyRole:
        case QPlatformDialogHelper::ResetRole:
            addButtonsToLayout(buttonLists[role], reverse);
        }
        ++currentLayout;
    }

    QWidgetList layoutWidgets;
    for (int i = 0; i < buttonLayout->count(); ++i) {
        if (auto *widget = buttonLayout->itemAt(i)->widget())
            layoutWidgets << widget;
    }

    q->setFocusProxy(nullptr);
    if (!layoutWidgets.isEmpty()) {
        QWidget *prev = layoutWidgets.constLast();
        for (QWidget *here : layoutWidgets) {
            QWidget::setTabOrder(prev, here);
            prev = here;
            if (auto *pushButton = qobject_cast<QPushButton *>(prev); pushButton && pushButton->isDefault())
                q->setFocusProxy(pushButton);
        }
    }

    if (center)
        buttonLayout->addStretch();
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 159, as _ZN23QDialogButtonBoxPrivate10initLayoutEv
inline void QDialogButtonBoxPrivate::initLayout()
{
    Q_Q(QDialogButtonBox);
    layoutPolicy = QDialogButtonBox::ButtonLayout(q->style()->styleHint(QStyle::SH_DialogButtonLayout, nullptr, q));
    bool createNewLayout = buttonLayout == nullptr
        || (orientation == Qt::Horizontal && qobject_cast<QVBoxLayout *>(buttonLayout) != 0)
        || (orientation == Qt::Vertical && qobject_cast<QHBoxLayout *>(buttonLayout) != 0);
    if (createNewLayout) {
        delete buttonLayout;
        if (orientation == Qt::Horizontal)
            buttonLayout = new QHBoxLayout(q);
        else
            buttonLayout = new QVBoxLayout(q);
    }

    int left, top, right, bottom;
    setLayoutItemMargins(QStyle::SE_PushButtonLayoutItem);
    getLayoutItemMargins(&left, &top, &right, &bottom);
    buttonLayout->setContentsMargins(-left, -top, -right, -bottom);

    if (!q->testAttribute(Qt::WA_WState_OwnSizePolicy)) {
        QSizePolicy sp(QSizePolicy::Expanding, QSizePolicy::Fixed, QSizePolicy::ButtonBox);
        if (orientation == Qt::Vertical)
            sp.transpose();
        q->setSizePolicy(sp);
        q->setAttribute(Qt::WA_WState_OwnSizePolicy, false);
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 188, as _ZN23QDialogButtonBoxPrivate11resetLayoutEv
inline void QDialogButtonBoxPrivate::resetLayout()
{
    initLayout();
    layoutButtons();
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 327, as _ZN23QDialogButtonBoxPrivate12createButtonEN16QDialogButtonBox14StandardButtonENS_10LayoutRuleE
inline QPushButton *QDialogButtonBoxPrivate::createButton(QDialogButtonBox::StandardButton sbutton,
                                                   LayoutRule layoutRule)
{
    Q_Q(QDialogButtonBox);
    int icon = 0;

    switch (sbutton) {
    case QDialogButtonBox::Ok:
        icon = QStyle::SP_DialogOkButton;
        break;
    case QDialogButtonBox::Save:
        icon = QStyle::SP_DialogSaveButton;
        break;
    case QDialogButtonBox::Open:
        icon = QStyle::SP_DialogOpenButton;
        break;
    case QDialogButtonBox::Cancel:
        icon = QStyle::SP_DialogCancelButton;
        break;
    case QDialogButtonBox::Close:
        icon = QStyle::SP_DialogCloseButton;
        break;
    case QDialogButtonBox::Apply:
        icon = QStyle::SP_DialogApplyButton;
        break;
    case QDialogButtonBox::Reset:
        icon = QStyle::SP_DialogResetButton;
        break;
    case QDialogButtonBox::Help:
        icon = QStyle::SP_DialogHelpButton;
        break;
    case QDialogButtonBox::Discard:
        icon = QStyle::SP_DialogDiscardButton;
        break;
    case QDialogButtonBox::Yes:
        icon = QStyle::SP_DialogYesButton;
        break;
    case QDialogButtonBox::No:
        icon = QStyle::SP_DialogNoButton;
        break;
    case QDialogButtonBox::YesToAll:
        icon = QStyle::SP_DialogYesToAllButton;
        break;
    case QDialogButtonBox::NoToAll:
        icon = QStyle::SP_DialogNoToAllButton;
        break;
    case QDialogButtonBox::SaveAll:
        icon = QStyle::SP_DialogSaveAllButton;
        break;
    case QDialogButtonBox::Abort:
        icon = QStyle::SP_DialogAbortButton;
        break;
    case QDialogButtonBox::Retry:
        icon = QStyle::SP_DialogRetryButton;
        break;
    case QDialogButtonBox::Ignore:
        icon = QStyle::SP_DialogIgnoreButton;
        break;
    case QDialogButtonBox::RestoreDefaults:
        icon = QStyle::SP_RestoreDefaultsButton;
        break;
    case QDialogButtonBox::NoButton:
        return nullptr;
        ;
    }
    QPushButton *button = new QPushButton(QDialogButtonBox::standardButtonText(sbutton), q);
    QStyle *style = q->style();
    if (style->styleHint(QStyle::SH_DialogButtonBox_ButtonsHaveIcons, nullptr, q) && icon != 0)
        button->setIcon(style->standardIcon(QStyle::StandardPixmap(icon), nullptr, q));
    if (style != QApplication::style()) // Propagate style
        button->setStyle(style);
    standardButtonMap.insert(button, sbutton);
    QPlatformDialogHelper::ButtonRole role = QPlatformDialogHelper::buttonRole(static_cast<QPlatformDialogHelper::StandardButton>(sbutton));
    if (Q_UNLIKELY(role == QPlatformDialogHelper::InvalidRole))
        qWarning("QDialogButtonBox::createButton: Invalid ButtonRole, button not added");
    else
        addButton(button, static_cast<QDialogButtonBox::ButtonRole>(role), layoutRule);
#if QT_CONFIG(shortcut)
    const QKeySequence standardShortcut = QDialogButtonBox::standardButtonShortcut(sbutton);
    if (!standardShortcut.isEmpty())
        button->setShortcut(standardShortcut);
#endif
    return button;
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 412, as _ZN23QDialogButtonBoxPrivate9addButtonEP15QAbstractButtonN16QDialogButtonBox10ButtonRoleENS_10LayoutRuleENS_7AddRuleE
inline void QDialogButtonBoxPrivate::addButton(QAbstractButton *button, QDialogButtonBox::ButtonRole role,
                                        LayoutRule layoutRule, AddRule addRule)
{
    buttonLists[role].append(button);
    switch (addRule) {
    case AddRule::Connect:
        QObjectPrivate::connect(button, &QAbstractButton::clicked,
                               this, &QDialogButtonBoxPrivate::handleButtonClicked);
        QObjectPrivate::connect(button, &QAbstractButton::destroyed,
                               this, &QDialogButtonBoxPrivate::handleButtonDestroyed);
        button->installEventFilter(filter.get());
        break;
    case AddRule::SkipConnect:
        break;
    }

    switch (layoutRule) {
    case LayoutRule::DoLayout:
        layoutButtons();
        break;
    case LayoutRule::SkipLayout:
        break;
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 956, as _ZN23QDialogButtonBoxPrivate21handleButtonDestroyedEv
inline void QDialogButtonBoxPrivate::handleButtonDestroyed()
{
    Q_Q(QDialogButtonBox);
    if (QObject *object = q->sender())
        removeButton(reinterpret_cast<QAbstractButton *>(object), RemoveReason::Destroyed);
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 922, as _ZN23QDialogButtonBoxPrivate19handleButtonClickedEv
inline void QDialogButtonBoxPrivate::handleButtonClicked()
{
    Q_Q(QDialogButtonBox);
    if (QAbstractButton *button = qobject_cast<QAbstractButton *>(q->sender())) {
        // Can't fetch this *after* emitting clicked, as clicked may destroy the button
        // or change its role. Now changing the role is not possible yet, but arguably
        // both clicked and accepted/rejected/etc. should be emitted "atomically"
        // depending on whatever role the button had at the time of the click.
        const QDialogButtonBox::ButtonRole buttonRole = q->buttonRole(button);
        QPointer<QDialogButtonBox> guard(q);

        emit q->clicked(button);

        if (!guard)
            return;

        switch (QPlatformDialogHelper::ButtonRole(buttonRole)) {
        case QPlatformDialogHelper::AcceptRole:
        case QPlatformDialogHelper::YesRole:
            emit q->accepted();
            break;
        case QPlatformDialogHelper::RejectRole:
        case QPlatformDialogHelper::NoRole:
            emit q->rejected();
            break;
        case QPlatformDialogHelper::HelpRole:
            emit q->helpRequested();
            break;
        default:
            break;
        }
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 963, as _ZN23QDialogButtonBoxPrivate23handleButtonShowAndHideEP15QAbstractButtonP6QEvent
inline bool QDialogButtonBoxPrivate::handleButtonShowAndHide(QAbstractButton *button, QEvent *event)
{
    Q_Q(QDialogButtonBox);

    const QEvent::Type type = event->type();

    if ((type != QEvent::HideToParent && type != QEvent::ShowToParent) || ignoreShowAndHide)
        return false;

    switch (type) {
    case QEvent::HideToParent: {
        const QDialogButtonBox::ButtonRole role = q->buttonRole(button);
        if (role != QDialogButtonBox::ButtonRole::InvalidRole) {
            removeButton(button, RemoveReason::HideEvent);
            hiddenButtons.insert(button, role);
            layoutButtons();
        }
        break;
    }
    case QEvent::ShowToParent:
        if (hiddenButtons.contains(button)) {
            const auto role = hiddenButtons.take(button);
            addButton(button, role, LayoutRule::DoLayout, AddRule::SkipConnect);
            if (role == QDialogButtonBox::AcceptRole)
                ensureFirstAcceptIsDefault();
        }
        break;
    default: break;
    }

    return false;
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 194, as _ZN23QDialogButtonBoxPrivate18addButtonsToLayoutERK5QListIP15QAbstractButtonEb
inline void QDialogButtonBoxPrivate::addButtonsToLayout(const QList<QAbstractButton *> &buttonList,
                                                 bool reverse)
{
    int start = reverse ? buttonList.size() - 1 : 0;
    int end = reverse ? -1 : buttonList.size();
    int step = reverse ? -1 : 1;

    for (int i = start; i != end; i += step) {
        QAbstractButton *button = buttonList.at(i);
        buttonLayout->addWidget(button);
        button->show();
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 1048, as _ZN23QDialogButtonBoxPrivate26ensureFirstAcceptIsDefaultEv
inline void QDialogButtonBoxPrivate::ensureFirstAcceptIsDefault()
{
    Q_Q(QDialogButtonBox);
    const QList<QAbstractButton *> &acceptRoleList = buttonLists[QDialogButtonBox::AcceptRole];
    QPushButton *firstAcceptButton = acceptRoleList.isEmpty()
                                   ? nullptr
                                   : qobject_cast<QPushButton *>(acceptRoleList.at(0));

    if (!firstAcceptButton)
        return;

    bool hasDefault = false;
    QWidget *dialog = nullptr;
    QWidget *p = q;
    while (p && !p->isWindow()) {
        p = p->parentWidget();
        if ((dialog = qobject_cast<QDialog *>(p)))
            break;
    }

    QWidget *parent = dialog ? dialog : q;
    Q_ASSERT(parent);

    const auto pushButtons = parent->findChildren<QPushButton *>();
    for (QPushButton *pushButton : pushButtons) {
        if (pushButton->isDefault() && pushButton != firstAcceptButton) {
            hasDefault = true;
            break;
        }
    }
    if (!hasDefault && firstAcceptButton) {
        firstAcceptButton->setDefault(true);
        // When the QDialogButtonBox is focused, and it doesn't have an
        // explicit focus widget, it will transfer focus to its focus
        // proxy, which is the first button in the layout. This behavior,
        // combined with the behavior that QPushButtons in a QDialog will
        // by default have their autoDefault set to true, results in the
        // focus proxy/first button stealing the default button status
        // immediately when the button box is focused, which is not what
        // we want. Account for this by explicitly making the firstAcceptButton
        // focused as well, unless an explicit focus widget has been set, or
        // a dialog child has Qt::StrongFocus.
        if (dialog && !(QWidgetPrivate::get(dialog)->hasChildWithFocusPolicy(Qt::StrongFocus, q)
                        || dialog->focusWidget()))
            firstAcceptButton->setFocus();
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 448, as _ZN23QDialogButtonBoxPrivate18retranslateStringsEv
inline void QDialogButtonBoxPrivate::retranslateStrings()
{
    for (const auto &it : std::as_const(standardButtonMap)) {
        const QString text = QDialogButtonBox::standardButtonText(it.second);
        if (!text.isEmpty())
            it.first->setText(text);
    }
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 1096, as _ZN23QDialogButtonBoxPrivate13disconnectAllEv
inline void QDialogButtonBoxPrivate::disconnectAll()
{
    Q_Q(QDialogButtonBox);
    const auto buttons = q->findChildren<QAbstractButton *>();
    for (auto *button : buttons)
        button->disconnect(q);
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 704, as _ZNK23QDialogButtonBoxPrivate10allButtonsEv
inline QList<QAbstractButton *> QDialogButtonBoxPrivate::allButtons() const
{
    QList<QAbstractButton *> ret(visibleButtons());
    ret.reserve(ret.size() + hiddenButtons.size());
    for (const auto &it : hiddenButtons)
        ret.push_back(it.first);
    return ret;
}

//  from src/widgets/widgets/qdialogbuttonbox.cpp, line 693, as _ZNK23QDialogButtonBoxPrivate14visibleButtonsEv
inline QList<QAbstractButton *> QDialogButtonBoxPrivate::visibleButtons() const
{
    QList<QAbstractButton *> finalList;
    for (int i = 0; i < QDialogButtonBox::NRoles; ++i) {
        const QList<QAbstractButton *> &list = buttonLists[i];
        for (int j = 0; j < list.size(); ++j)
            finalList.append(list.at(j));
    }
    return finalList;
}
//  -----------------------------------------------------------------------

//  A QDialogButtonBoxPrivate that Python can take functions over in. Every QDialogButtonBoxPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDialogButtonBoxPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall1)(const void *, int, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall2)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall3)(const void *, int *);
typedef void * (*CuteQDialogButtonBoxPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQDialogButtonBoxPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQDialogButtonBoxPrivateCall6)(const void *, int *);
typedef int (*CuteQDialogButtonBoxPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQDialogButtonBoxPrivateCall8)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall9)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall10)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall11)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall12)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall13)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall14)(const void *, int *);
typedef void (*CuteQDialogButtonBoxPrivateCall15)(const void *, int *);
typedef bool (*CuteQDialogButtonBoxPrivateCall16)(const void *, int *);
typedef bool (*CuteQDialogButtonBoxPrivateCall17)(const void *, int *);
class CuteQDialogButtonBoxPrivate : public QDialogButtonBoxPrivate {
public:
  using QDialogButtonBoxPrivate::QDialogButtonBoxPrivate;
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
      CuteQDialogButtonBoxPrivateCall0 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall1 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall2 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall3 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall4 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall5 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall6 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall7 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall8 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall9 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall10 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall11 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall12 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall13 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall14 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall15 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall16 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQDialogButtonBoxPrivateCall17 call = reinterpret_cast<CuteQDialogButtonBoxPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QDialogButtonBox *QDialogButtonBoxPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN23QDialogButtonBoxPrivate6q_funcEv(
    QDialogButtonBoxPrivate *self) {
  return self->q_func();
}

//  const QDialogButtonBox *QDialogButtonBoxPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDialogButtonBox *ritual_ZNK23QDialogButtonBoxPrivate6q_funcEv(
    const QDialogButtonBoxPrivate *self) {
  return self->q_func();
}

//  QDialogButtonBoxPrivate::QDialogButtonBoxPrivate(Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
QDialogButtonBoxPrivate *ritual_ZN23QDialogButtonBoxPrivateC1EN2Qt11OrientationE(
    Qt::Orientation orient) {
  return new CuteQDialogButtonBoxPrivate(orient);
}

//  void QDialogButtonBoxPrivate::createStandardButtons(QDialogButtonBox::Sta
//      ndardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate21createStandardButtonsE6QFlagsIN16QDialogButtonBox14StandardButtonEE(
    QDialogButtonBoxPrivate *self,
    int buttons) {
  self->createStandardButtons(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons));
}

//  void QDialogButtonBoxPrivate::removeButton(QAbstractButton *button,
//      RemoveReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate12removeButtonEP15QAbstractButtonNS_12RemoveReasonE(
    QDialogButtonBoxPrivate *self,
    QAbstractButton *button,
    QDialogButtonBoxPrivate::RemoveReason reason) {
  self->removeButton(button, reason);
}

//  void QDialogButtonBoxPrivate::layoutButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate13layoutButtonsEv(
    QDialogButtonBoxPrivate *self) {
  self->layoutButtons();
}

//  void QDialogButtonBoxPrivate::initLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate10initLayoutEv(
    QDialogButtonBoxPrivate *self) {
  self->initLayout();
}

//  void QDialogButtonBoxPrivate::resetLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate11resetLayoutEv(
    QDialogButtonBoxPrivate *self) {
  self->resetLayout();
}

//  QPushButton
//      *QDialogButtonBoxPrivate::createButton(QDialogButtonBox::StandardButt
//      on button, LayoutRule layoutRule)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN23QDialogButtonBoxPrivate12createButtonEN16QDialogButtonBox14StandardButtonENS_10LayoutRuleE(
    QDialogButtonBoxPrivate *self,
    QDialogButtonBox::StandardButton button,
    QDialogButtonBoxPrivate::LayoutRule layoutRule) {
  return self->createButton(button, layoutRule);
}

//  void QDialogButtonBoxPrivate::addButton(QAbstractButton *button,
//      QDialogButtonBox::ButtonRole role, LayoutRule layoutRule, AddRule
//      addRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate9addButtonEP15QAbstractButtonN16QDialogButtonBox10ButtonRoleENS_10LayoutRuleENS_7AddRuleE(
    QDialogButtonBoxPrivate *self,
    QAbstractButton *button,
    QDialogButtonBox::ButtonRole role,
    QDialogButtonBoxPrivate::LayoutRule layoutRule,
    QDialogButtonBoxPrivate::AddRule addRule) {
  self->addButton(button, role, layoutRule, addRule);
}

//  void QDialogButtonBoxPrivate::handleButtonDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate21handleButtonDestroyedEv(
    QDialogButtonBoxPrivate *self) {
  self->handleButtonDestroyed();
}

//  void QDialogButtonBoxPrivate::handleButtonClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate19handleButtonClickedEv(
    QDialogButtonBoxPrivate *self) {
  self->handleButtonClicked();
}

//  bool QDialogButtonBoxPrivate::handleButtonShowAndHide(QAbstractButton
//      *button, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDialogButtonBoxPrivate23handleButtonShowAndHideEP15QAbstractButtonP6QEvent(
    QDialogButtonBoxPrivate *self,
    QAbstractButton *button,
    QEvent *event) {
  return self->handleButtonShowAndHide(button, event);
}

//  void QDialogButtonBoxPrivate::addButtonsToLayout(const
//      QList<QAbstractButton *> &buttonList, bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate18addButtonsToLayoutERK5QListIP15QAbstractButtonEb(
    QDialogButtonBoxPrivate *self,
    const QList<QAbstractButton *> *buttonList,
    bool reverse) {
  self->addButtonsToLayout(*buttonList, reverse);
}

//  void QDialogButtonBoxPrivate::ensureFirstAcceptIsDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate26ensureFirstAcceptIsDefaultEv(
    QDialogButtonBoxPrivate *self) {
  self->ensureFirstAcceptIsDefault();
}

//  void QDialogButtonBoxPrivate::retranslateStrings()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate18retranslateStringsEv(
    QDialogButtonBoxPrivate *self) {
  self->retranslateStrings();
}

//  void QDialogButtonBoxPrivate::disconnectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDialogButtonBoxPrivate13disconnectAllEv(
    QDialogButtonBoxPrivate *self) {
  self->disconnectAll();
}

//  QList<QAbstractButton *> QDialogButtonBoxPrivate::allButtons() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK23QDialogButtonBoxPrivate10allButtonsEv(
    const QDialogButtonBoxPrivate *self) {
  return new QList<QAbstractButton *>(self->allButtons());
}

//  QList<QAbstractButton *> QDialogButtonBoxPrivate::visibleButtons() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK23QDialogButtonBoxPrivate14visibleButtonsEv(
    const QDialogButtonBoxPrivate *self) {
  return new QList<QAbstractButton *>(self->visibleButtons());
}

//  a Python function taken by a CuteQDialogButtonBoxPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDialogButtonBoxPrivate(
    QDialogButtonBoxPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDialogButtonBoxPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dialogbuttonbox)
