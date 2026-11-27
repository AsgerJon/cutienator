//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-26: added are 3 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Edited by hand on 2026-11-27: code taken from
//  Qt's source no longer stands under defined(Q_OS_LINUX), which Qt does not
//  write there; its rituals no longer stand under defined(Q_OS_LINUX), as
//  the code taken from Qt they call no longer does; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qicon.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#if QT_CONFIG(action)
#  include <QtWidgets/qwidgetaction.h>
#endif
#include <QtGui/qclipboard.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifndef QT_NO_IM
#include <QtGui/qinputmethod.h>
#include <QtCore/qlist.h>
#endif
#include <QtGui/qpainter.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/qvalidator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qlineedit_p.cpp, line 447, as local:qlineedit_p.cpp:displayWidgets
#if QT_CONFIG(animation) && QT_CONFIG(toolbutton)
static void displayWidgets(const QLineEditPrivate::SideWidgetEntryList &widgets, bool display)
{
    for (const auto &e : widgets) {
        if (e.flags & QLineEditPrivate::SideWidgetFadeInWithText)
            static_cast<QLineEditIconButton *>(e.widget)->animateShow(display);
    }
}
#endif  // QT_CONFIG(animation) && QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 667, as local:qlineedit_p.cpp:effectiveTextMargin
static int effectiveTextMargin(int defaultMargin, const QLineEditPrivate::SideWidgetEntryList &widgets,
                               const QLineEditPrivate::SideWidgetParameters &parameters)
{
    if (widgets.empty())
        return defaultMargin;

    const auto visibleSideWidgetCount = std::count_if(widgets.begin(), widgets.end(),
                             [](const QLineEditPrivate::SideWidgetEntry &e) {
#if QT_CONFIG(toolbutton) && QT_CONFIG(animation)
        // a button that's fading out doesn't get any space
        if (auto* iconButton = qobject_cast<QLineEditIconButton*>(e.widget))
            return iconButton->needsSpace();

#endif
        return e.widget->isVisibleTo(e.widget->parentWidget());
    });

    return defaultMargin + (parameters.margin + parameters.widgetWidth) * visibleSideWidgetCount;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 687, as _ZNK16QLineEditPrivate20effectiveTextMarginsEv
inline QMargins QLineEditPrivate::effectiveTextMargins() const
{
    return {effectiveTextMargin(textMargins.left(), leftSideWidgetList(), sideWidgetParameters()),
            textMargins.top(),
            effectiveTextMargin(textMargins.right(), rightSideWidgetList(), sideWidgetParameters()),
            textMargins.bottom()};
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 456, as _ZN16QLineEditPrivate11textChangedERK7QString
inline void QLineEditPrivate::textChanged(const QString &text)
{
    if (hasSideWidgets()) {
        const int newTextSize = text.size();
        if (!newTextSize || !lastTextSize) {
            lastTextSize = newTextSize;
#if QT_CONFIG(animation) && QT_CONFIG(toolbutton)
            const bool display = newTextSize > 0;
            displayWidgets(leadingSideWidgets, display);
            displayWidgets(trailingSideWidgets, display);
#endif
        }
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 380, as _ZN19QLineEditIconButton10setOpacityEd
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::setOpacity(qreal value)
{
    if (!qFuzzyCompare(m_opacity, value)) {
        m_opacity = value;
        updateCursor();
        update();
    }
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 395, as _ZN19QLineEditIconButton15setHideWithTextEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::setHideWithText(bool hide)
{
    m_hideWithText = hide;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 334, as _ZN19QLineEditIconButtonC1EP7QWidget
#if QT_CONFIG(toolbutton)
inline QLineEditIconButton::QLineEditIconButton(QWidget *parent)
    : QToolButton(parent)
    , m_opacity(0)
{
    setFocusPolicy(Qt::NoFocus);
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 412, as _ZN19QLineEditIconButton11animateShowEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::animateShow(bool visible)
{
    m_fadingOut = !visible;

    if (shouldHideWithText() && !isVisible()) {
        show();

        // Invalidate previous geometry to take into account new size of side widgets
        if (auto le = lineEditPrivate())
            le->updateGeometry_helper(true);
    }

    startOpacityAnimation(visible ? 1.0 : 0.0);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 438, as _ZN19QLineEditIconButton12updateCursorEv
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::updateCursor()
{
#ifndef QT_NO_CURSOR
    setCursor(qFuzzyCompare(m_opacity, qreal(1.0)) || !parentWidget() ? QCursor(Qt::ArrowCursor) : parentWidget()->cursor());
#endif
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 427, as _ZN19QLineEditIconButton21startOpacityAnimationEd
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::startOpacityAnimation(qreal endValue)
{
    QPropertyAnimation *animation = new QPropertyAnimation(this, QByteArrayLiteral("opacity"), this);
    connect(animation, &QPropertyAnimation::finished, this, &QLineEditIconButton::onAnimationFinished);

    animation->setDuration(160);
    animation->setEndValue(endValue);
    animation->start(QAbstractAnimation::DeleteWhenStopped);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 341, as _ZNK19QLineEditIconButton15lineEditPrivateEv
#if QT_CONFIG(toolbutton)
inline QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
{
    QLineEdit *le = qobject_cast<QLineEdit *>(parentWidget());
    return le ? static_cast<QLineEditPrivate *>(qt_widget_private(le)) : nullptr;
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 390, as _ZNK19QLineEditIconButton18shouldHideWithTextEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline bool QLineEditIconButton::shouldHideWithText() const
{
    return m_hideWithText;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 400, as _ZN19QLineEditIconButton19onAnimationFinishedEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::onAnimationFinished()
{
    if (shouldHideWithText() && isVisible() && m_fadingOut) {
        hide();
        m_fadingOut = false;

        // Invalidate previous geometry to take into account new size of side widgets
        if (auto le = lineEditPrivate())
            le->updateGeometry_helper(true);
    }
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 235, as _ZN16QLineEditPrivate19initMouseYThresholdEv
inline void QLineEditPrivate::initMouseYThreshold()
{
    mouseYThreshold = QGuiApplication::styleHints()->mouseQuickSelectionThreshold();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 262, as _ZN16QLineEditPrivate7setTextERK7QString
inline void QLineEditPrivate::setText(const QString& text)
{
    edited = true;
    control->setText(text);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 54, as _ZNK16QLineEditPrivate16textBeforeCursorEi
inline QString QLineEditPrivate::textBeforeCursor(int curPos) const
{
    const QString &text = control->text();
    return text.mid(0, curPos);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 60, as _ZNK16QLineEditPrivate15textAfterCursorEi
inline QString QLineEditPrivate::textAfterCursor(int curPos) const
{
    const QString &text = control->text();
    return text.mid(curPos);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 268, as _ZN16QLineEditPrivate25updatePasswordEchoEditingEb
inline void QLineEditPrivate::updatePasswordEchoEditing(bool editing)
{
    Q_Q(QLineEdit);
    control->updatePasswordEchoEditing(editing);
    q->setAttribute(Qt::WA_InputMethodEnabled, shouldEnableInputMethod());
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 275, as _ZN16QLineEditPrivate16resetInputMethodEv
inline void QLineEditPrivate::resetInputMethod()
{
    Q_Q(QLineEdit);
    if (q->hasFocus() && qApp) {
        QGuiApplication::inputMethod()->reset();
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 240, as _ZNK16QLineEditPrivate20adjustedContentsRectEv
inline QRect QLineEditPrivate::adjustedContentsRect() const
{
    Q_Q(const QLineEdit);
    QStyleOptionFrame opt;
    q->initStyleOption(&opt);
    QRect r = q->style()->subElementRect(QStyle::SE_LineEditContents, &opt, q);
    r = r.marginsRemoved(effectiveTextMargins());
    return r;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 117, as _ZN16QLineEditPrivate20handleWindowActivateEv
inline void QLineEditPrivate::handleWindowActivate()
{
    Q_Q(QLineEdit);
    if (!q->hasFocus() && control->hasSelectedText())
        control->deselect();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 124, as _ZN16QLineEditPrivate10textEditedERK7QString
inline void QLineEditPrivate::textEdited(const QString &text)
{
    Q_Q(QLineEdit);
    edited = true;
    emit q->textEdited(text);
#if QT_CONFIG(completer)
    if (control->completer()
        && control->completer()->completionMode() != QCompleter::InlineCompletion)
        control->complete(-1); // update the popup on cut/paste/del
#endif
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 136, as _ZN16QLineEditPrivate21cursorPositionChangedEii
inline void QLineEditPrivate::cursorPositionChanged(int from, int to)
{
    Q_Q(QLineEdit);
    q->update();
    emit q->cursorPositionChanged(from, to);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 78, as _ZN16QLineEditPrivate16connectCompleterEv
#if QT_CONFIG(completer)
inline void QLineEditPrivate::connectCompleter()
{
    Q_Q(const QLineEdit);
    QObject::connect(control->completer(), qOverload<const QString &>(&QCompleter::activated),
                     q, &QLineEdit::setText);
    QObjectPrivate::connect(control->completer(), qOverload<const QString &>(&QCompleter::highlighted),
                            this, &QLineEditPrivate::completionHighlighted);
}
#endif  // QT_CONFIG(completer)

//  from src/widgets/widgets/qlineedit_p.cpp, line 87, as _ZN16QLineEditPrivate19disconnectCompleterEv
#if QT_CONFIG(completer)
inline void QLineEditPrivate::disconnectCompleter()
{
    Q_Q(const QLineEdit);
    QObject::disconnect(control->completer(), qOverload<const QString &>(&QCompleter::activated),
                        q, &QLineEdit::setText);
    QObjectPrivate::disconnect(control->completer(), qOverload<const QString &>(&QCompleter::highlighted),
                               this, &QLineEditPrivate::completionHighlighted);
}
#endif  // QT_CONFIG(completer)

//  from src/widgets/widgets/qlineedit_p.cpp, line 96, as _ZN16QLineEditPrivate21completionHighlightedERK7QString
#if QT_CONFIG(completer)
inline void QLineEditPrivate::completionHighlighted(const QString &newText)
{
    Q_Q(QLineEdit);
    if (control->completer()->completionMode() != QCompleter::InlineCompletion) {
        q->setText(newText);
    } else {
        int c = control->cursor();
        QString text = control->text();
        q->setText(QStringView{text}.left(c) + QStringView{newText}.mid(c));
        control->moveCursor(control->end(), false);
#ifndef Q_OS_ANDROID
        const bool mark = true;
#else
        const bool mark = (imHints & Qt::ImhNoPredictiveText);
#endif
        control->moveCursor(c, mark);
    }
}
#endif  // QT_CONFIG(completer)

//  from src/widgets/widgets/qlineedit_p.cpp, line 318, as _ZN16QLineEditPrivate4dragEv
#if QT_CONFIG(draganddrop)
inline void QLineEditPrivate::drag()
{
    Q_Q(QLineEdit);
    dndTimer.stop();
    QMimeData *data = new QMimeData;
    data->setText(control->selectedText());
    QDrag *drag = new QDrag(q);
    drag->setMimeData(data);
    Qt::DropAction action = drag->exec(Qt::CopyAction);
    if (action == Qt::MoveAction && !control->isReadOnly() && drag->target() != q)
        control->removeSelection();
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qlineedit_p.cpp, line 471, as _ZN16QLineEditPrivate18clearButtonClickedEv
inline void QLineEditPrivate::clearButtonClicked()
{
    Q_Q(QLineEdit);
    if (!q->text().isEmpty()) {
        q->clear();
        textEdited(QString());
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 480, as _ZN16QLineEditPrivate22controlEditingFinishedEv
inline void QLineEditPrivate::controlEditingFinished()
{
    Q_Q(QLineEdit);
    edited = false;
    emit q->returnPressed();
    emit q->editingFinished();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 568, as _ZN16QLineEditPrivate9addActionEP7QActionS1_N9QLineEdit14ActionPositionEi
#if QT_CONFIG(action)
inline QWidget *QLineEditPrivate::addAction(QAction *newAction, QAction *before, QLineEdit::ActionPosition position, int flags)
{
    Q_Q(QLineEdit);
    if (!newAction)
        return nullptr;
    if (!hasSideWidgets()) { // initial setup.
        QObjectPrivate::connect(q, &QLineEdit::textChanged,
                                this, &QLineEditPrivate::textChanged);
        lastTextSize = q->text().size();
    }
    QWidget *w = nullptr;
    // Store flags about QWidgetAction here since removeAction() may be called from ~QAction,
    // in which a qobject_cast<> no longer works.
    if (QWidgetAction *widgetAction = qobject_cast<QWidgetAction *>(newAction)) {
        if ((w = widgetAction->requestWidget(q)))
            flags |= SideWidgetCreatedByWidgetAction;
    }
    if (!w) {
#if QT_CONFIG(toolbutton)
        QLineEditIconButton *toolButton = new QLineEditIconButton(q);
        toolButton->setIcon(newAction->icon());
        toolButton->setOpacity(lastTextSize > 0 || !(flags & SideWidgetFadeInWithText) ? 1 : 0);
        if (flags & SideWidgetClearButton) {
            QObjectPrivate::connect(toolButton, &QToolButton::clicked,
                                    this, &QLineEditPrivate::clearButtonClicked);

#if QT_CONFIG(animation)
            // The clear button is handled only by this widget. The button should be really
            // shown/hidden in order to calculate size hints correctly.
            toolButton->setHideWithText(true);
#endif
        }
        toolButton->setDefaultAction(newAction);
        w = toolButton;
#else
        return nullptr;
#endif
    }

    // QTBUG-59957: clear button should be the leftmost action.
    if (!before && !(flags & SideWidgetClearButton) && position == QLineEdit::TrailingPosition) {
        for (const SideWidgetEntry &e : trailingSideWidgets) {
            if (e.flags & SideWidgetClearButton) {
                before = e.action;
                break;
            }
        }
    }

    // If there is a 'before' action, it takes preference

    // There's a bug in GHS compiler that causes internal error on the following code.
    // The affected GHS compiler versions are 2016.5.4 and 2017.1. GHS internal reference
    // to track the progress of this issue is TOOLS-26637.
    // This temporary workaround allows to compile with GHS toolchain and should be
    // removed when GHS provides a patch to fix the compiler issue.

#if defined(Q_CC_GHS)
    const SideWidgetLocation loc = {position, -1};
    const auto location = before ? findSideWidget(before) : loc;
#else
    const auto location = before ? findSideWidget(before) : SideWidgetLocation{position, -1};
#endif

    SideWidgetEntryList &list = location.position == QLineEdit::TrailingPosition ? trailingSideWidgets : leadingSideWidgets;
    list.insert(location.isValid() ? list.begin() + location.index : list.end(),
                SideWidgetEntry(w, newAction, flags));
    positionSideWidgets();
    w->show();
    return w;
}
#endif  // QT_CONFIG(action)

//  from src/widgets/widgets/qlineedit_p.cpp, line 640, as _ZN16QLineEditPrivate12removeActionEP7QAction
#if QT_CONFIG(action)
inline void QLineEditPrivate::removeAction(QAction *action)
{
    Q_Q(QLineEdit);
    const auto location = findSideWidget(action);
    if (!location.isValid())
        return;
    SideWidgetEntryList &list = location.position == QLineEdit::TrailingPosition ? trailingSideWidgets : leadingSideWidgets;
    SideWidgetEntry entry = list[location.index];
    list.erase(list.begin() + location.index);
    if (entry.flags & SideWidgetCreatedByWidgetAction) {
        // If the cast fails, the QAction is in the process of being deleted
        // and has already ceased to be a QWidgetAction; in the process, it
        // will release its widget itself, and calling releaseWidget() here
        // would be UB, so don't:
        if (const auto a = qobject_cast<QWidgetAction*>(entry.action))
            a->releaseWidget(entry.widget);
    } else {
         delete entry.widget;
    }
     positionSideWidgets();
     if (!hasSideWidgets()) // Last widget, remove connection
         QObjectPrivate::connect(q, &QLineEdit::textChanged,
                                 this, &QLineEditPrivate::textChanged);
     q->update();
}
#endif  // QT_CONFIG(action)

//  from src/widgets/widgets/qlineedit_p.cpp, line 488, as _ZNK16QLineEditPrivate20sideWidgetParametersEv
inline QLineEditPrivate::SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
{
    Q_Q(const QLineEdit);
    SideWidgetParameters result;
    result.iconSize = q->style()->pixelMetric(QStyle::PM_LineEditIconSize, nullptr, q);
    result.margin = q->style()->pixelMetric(QStyle::PM_LineEditIconMargin, nullptr, q);
    result.widgetWidth = result.iconSize + 6;
    result.widgetHeight = result.iconSize + 2;
    return result;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 499, as _ZNK16QLineEditPrivate15clearButtonIconEv
inline QIcon QLineEditPrivate::clearButtonIcon() const
{
    Q_Q(const QLineEdit);
    QStyleOptionFrame styleOption;
    q->initStyleOption(&styleOption);
    return q->style()->standardIcon(QStyle::SP_LineEditClearButton, &styleOption, q);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 507, as _ZN16QLineEditPrivate21setClearButtonEnabledEb
inline void QLineEditPrivate::setClearButtonEnabled(bool enabled)
{
#if QT_CONFIG(action)
    for (const SideWidgetEntry &e : trailingSideWidgets) {
        if (e.flags & SideWidgetClearButton) {
            e.action->setEnabled(enabled);
            break;
        }
    }
#else
    Q_UNUSED(enabled);
#endif
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 521, as _ZN16QLineEditPrivate19positionSideWidgetsEv
inline void QLineEditPrivate::positionSideWidgets()
{
    Q_Q(QLineEdit);
    if (hasSideWidgets()) {
        const QRect contentRect = q->rect();
        const SideWidgetParameters p = sideWidgetParameters();
        const int delta = p.margin + p.widgetWidth;
        QRect widgetGeometry(QPoint(p.margin, (contentRect.height() - p.widgetHeight) / 2),
                             QSize(p.widgetWidth, p.widgetHeight));
        for (const SideWidgetEntry &e : leftSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() + delta);
#else
            Q_UNUSED(delta);
#endif
        }
        widgetGeometry.moveLeft(contentRect.width() - p.widgetWidth - p.margin);
        for (const SideWidgetEntry &e : rightSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() - delta);
#endif
        }
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 551, as _ZNK16QLineEditPrivate14findSideWidgetEPK7QAction
#if QT_CONFIG(action)
inline QLineEditPrivate::SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction *a) const
{
    int i = 0;
    for (const auto &e : leadingSideWidgets) {
        if (a == e.action)
            return {QLineEdit::LeadingPosition, i};
        ++i;
    }
    i = 0;
    for (const auto &e : trailingSideWidgets) {
        if (a == e.action)
            return {QLineEdit::TrailingPosition, i};
        ++i;
    }
    return {QLineEdit::LeadingPosition, -1};
}
#endif  // QT_CONFIG(action)
//  -----------------------------------------------------------------------

//  A QLineEditPrivate that Python can take functions over in. Every QLineEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLineEditPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQLineEditPrivateCall1)(const void *, int, int *);
typedef void (*CuteQLineEditPrivateCall2)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall3)(const void *, int *);
typedef void * (*CuteQLineEditPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQLineEditPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQLineEditPrivateCall6)(const void *, int *);
typedef int (*CuteQLineEditPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQLineEditPrivateCall8)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall9)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall10)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall11)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall12)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall13)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall14)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall15)(const void *, int *);
typedef bool (*CuteQLineEditPrivateCall16)(const void *, int *);
typedef bool (*CuteQLineEditPrivateCall17)(const void *, int *);
class CuteQLineEditPrivate : public QLineEditPrivate {
public:
  using QLineEditPrivate::QLineEditPrivate;
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
      CuteQLineEditPrivateCall0 call = reinterpret_cast<CuteQLineEditPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLineEditPrivateCall1 call = reinterpret_cast<CuteQLineEditPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLineEditPrivateCall2 call = reinterpret_cast<CuteQLineEditPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLineEditPrivateCall3 call = reinterpret_cast<CuteQLineEditPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQLineEditPrivateCall4 call = reinterpret_cast<CuteQLineEditPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLineEditPrivateCall5 call = reinterpret_cast<CuteQLineEditPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLineEditPrivateCall6 call = reinterpret_cast<CuteQLineEditPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQLineEditPrivateCall7 call = reinterpret_cast<CuteQLineEditPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQLineEditPrivateCall8 call = reinterpret_cast<CuteQLineEditPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQLineEditPrivateCall9 call = reinterpret_cast<CuteQLineEditPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLineEditPrivateCall10 call = reinterpret_cast<CuteQLineEditPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQLineEditPrivateCall11 call = reinterpret_cast<CuteQLineEditPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQLineEditPrivateCall12 call = reinterpret_cast<CuteQLineEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQLineEditPrivateCall13 call = reinterpret_cast<CuteQLineEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQLineEditPrivateCall14 call = reinterpret_cast<CuteQLineEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQLineEditPrivateCall15 call = reinterpret_cast<CuteQLineEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQLineEditPrivateCall16 call = reinterpret_cast<CuteQLineEditPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQLineEditPrivateCall17 call = reinterpret_cast<CuteQLineEditPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QLineEdit *QLineEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN16QLineEditPrivate6q_funcEv(QLineEditPrivate *self) {
  return self->q_func();
}

//  const QLineEdit *QLineEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLineEdit *ritual_ZNK16QLineEditPrivate6q_funcEv(
    const QLineEditPrivate *self) {
  return self->q_func();
}

//  QLineEditPrivate::QLineEditPrivate()
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZN16QLineEditPrivateC1Ev() {
  return new CuteQLineEditPrivate();
}

//  QLineEditPrivate::~QLineEditPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivateD1Ev(QLineEditPrivate *self) {
  delete self;
}

//  void QLineEditPrivate::initMouseYThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate19initMouseYThresholdEv(
    QLineEditPrivate *self) {
  self->initMouseYThreshold();
}

//  void QLineEditPrivate::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate7setTextERK7QString(
    QLineEditPrivate *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QLineEditPrivate::textBeforeCursor(int curPos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QLineEditPrivate16textBeforeCursorEi(
    const QLineEditPrivate *self,
    int curPos) {
  return new QString(self->textBeforeCursor(curPos));
}

//  QString QLineEditPrivate::textAfterCursor(int curPos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QLineEditPrivate15textAfterCursorEi(
    const QLineEditPrivate *self,
    int curPos) {
  return new QString(self->textAfterCursor(curPos));
}

//  void QLineEditPrivate::updatePasswordEchoEditing(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate25updatePasswordEchoEditingEb(
    QLineEditPrivate *self,
    bool a0) {
  self->updatePasswordEchoEditing(a0);
}

//  void QLineEditPrivate::resetInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate16resetInputMethodEv(
    QLineEditPrivate *self) {
  self->resetInputMethod();
}

//  bool QLineEditPrivate::shouldEnableInputMethod() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate23shouldEnableInputMethodEv(
    const QLineEditPrivate *self) {
  return self->shouldEnableInputMethod();
}

//  bool QLineEditPrivate::shouldShowPlaceholderText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate25shouldShowPlaceholderTextEv(
    const QLineEditPrivate *self) {
  return self->shouldShowPlaceholderText();
}

//  QLineEditPrivate *QLineEditPrivate::get(QLineEdit *lineEdit)
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZN16QLineEditPrivate3getEP9QLineEdit(
    QLineEdit *lineEdit) {
  return QLineEditPrivate::get(lineEdit);
}

//  QRect QLineEditPrivate::adjustedContentsRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QLineEditPrivate20adjustedContentsRectEv(
    const QLineEditPrivate *self) {
  return new QRect(self->adjustedContentsRect());
}

//  void QLineEditPrivate::handleWindowActivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate20handleWindowActivateEv(
    QLineEditPrivate *self) {
  self->handleWindowActivate();
}

//  void QLineEditPrivate::textEdited(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate10textEditedERK7QString(
    QLineEditPrivate *self,
    const QString *a0) {
  self->textEdited(*a0);
}

//  void QLineEditPrivate::cursorPositionChanged(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate21cursorPositionChangedEii(
    QLineEditPrivate *self,
    int a0,
    int a1) {
  self->cursorPositionChanged(a0, a1);
}

#if QT_CONFIG(completer)
//  void QLineEditPrivate::connectCompleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate16connectCompleterEv(
    QLineEditPrivate *self) {
  self->connectCompleter();
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
//  void QLineEditPrivate::disconnectCompleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate19disconnectCompleterEv(
    QLineEditPrivate *self) {
  self->disconnectCompleter();
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
//  void QLineEditPrivate::completionHighlighted(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate21completionHighlightedERK7QString(
    QLineEditPrivate *self,
    const QString *a0) {
  self->completionHighlighted(*a0);
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(draganddrop)
//  void QLineEditPrivate::drag()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate4dragEv(QLineEditPrivate *self) {
  self->drag();
}
#endif  // QT_CONFIG(draganddrop)

//  void QLineEditPrivate::clearButtonClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate18clearButtonClickedEv(
    QLineEditPrivate *self) {
  self->clearButtonClicked();
}

//  void QLineEditPrivate::controlEditingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate22controlEditingFinishedEv(
    QLineEditPrivate *self) {
  self->controlEditingFinished();
}

#if QT_CONFIG(action)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
//  QWidget *QLineEditPrivate::addAction(QAction *newAction, QAction *before,
//      QLineEdit::ActionPosition a2, int flags)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN16QLineEditPrivate9addActionEP7QActionS1_N9QLineEdit14ActionPositionEi(
    QLineEditPrivate *self,
    QAction *newAction,
    QAction *before,
    QLineEdit::ActionPosition a2,
    int flags) {
  return self->addAction(newAction, before, a2, flags);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
//  void QLineEditPrivate::removeAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate12removeActionEP7QAction(
    QLineEditPrivate *self,
    QAction *action) {
  self->removeAction(action);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(action)

//  SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
extern "C" Q_DECL_EXPORT
QLineEditPrivate::SideWidgetParameters *ritual_ZNK16QLineEditPrivate20sideWidgetParametersEv(
    const QLineEditPrivate *self) {
  return new QLineEditPrivate::SideWidgetParameters(
      self->sideWidgetParameters());
}

//  QIcon QLineEditPrivate::clearButtonIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QLineEditPrivate15clearButtonIconEv(
    const QLineEditPrivate *self) {
  return new QIcon(self->clearButtonIcon());
}

//  void QLineEditPrivate::setClearButtonEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate21setClearButtonEnabledEb(
    QLineEditPrivate *self,
    bool enabled) {
  self->setClearButtonEnabled(enabled);
}

//  void QLineEditPrivate::positionSideWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate19positionSideWidgetsEv(
    QLineEditPrivate *self) {
  self->positionSideWidgets();
}

//  bool QLineEditPrivate::hasSideWidgets() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate14hasSideWidgetsEv(
    const QLineEditPrivate *self) {
  return self->hasSideWidgets();
}

//  const SideWidgetEntryList &QLineEditPrivate::leftSideWidgetList() const
extern "C" Q_DECL_EXPORT
const QLineEditPrivate::SideWidgetEntryList *ritual_ZNK16QLineEditPrivate18leftSideWidgetListEv(
    const QLineEditPrivate *self) {
  return &(self->leftSideWidgetList());
}

//  const SideWidgetEntryList &QLineEditPrivate::rightSideWidgetList() const
extern "C" Q_DECL_EXPORT
const QLineEditPrivate::SideWidgetEntryList *ritual_ZNK16QLineEditPrivate19rightSideWidgetListEv(
    const QLineEditPrivate *self) {
  return &(self->rightSideWidgetList());
}

#if QT_CONFIG(action)
//  SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction *a)
//      const
extern "C" Q_DECL_EXPORT
QLineEditPrivate::SideWidgetLocation *ritual_ZNK16QLineEditPrivate14findSideWidgetEPK7QAction(
    const QLineEditPrivate *self,
    const QAction *a) {
  return new QLineEditPrivate::SideWidgetLocation(self->findSideWidget(a));
}
#endif  // QT_CONFIG(action)

//  a Python function taken by a CuteQLineEditPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLineEditPrivate(
    QLineEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLineEditPrivate *>(self)->take(key, call);
}

//  a QLineEditPrivate::SideWidgetLocation a ritual of QLineEditPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLineEditPrivate__QLineEditPrivate_SideWidgetLocation(
    QLineEditPrivate::SideWidgetLocation *self) {
  delete self;
}

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
