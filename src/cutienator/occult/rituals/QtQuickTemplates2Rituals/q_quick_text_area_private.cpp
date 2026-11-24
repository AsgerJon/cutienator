//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicktextarea_p.h>
#include <QtQuickTemplates2/private/qquicktextarea_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquickscrollview_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtQuickTemplates2/private/qquicktooltip_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickclipnode_p.h>
#include <QtQuick/private/qquickflickable_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 126, as _ZN21QQuickTextAreaPrivateC1Ev
inline QQuickTextAreaPrivate::QQuickTextAreaPrivate()
{
#if QT_CONFIG(accessibility)
    setAccessible();
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 133, as _ZN21QQuickTextAreaPrivateD1Ev
inline QQuickTextAreaPrivate::~QQuickTextAreaPrivate()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 137, as _ZN21QQuickTextAreaPrivate11setTopInsetEdb
inline void QQuickTextAreaPrivate::setTopInset(qreal value, bool reset)
{
    Q_Q(QQuickTextArea);
    const QMarginsF oldInset = getInset();
    extra.value().topInset = value;
    extra.value().hasTopInset = !reset;
    if (!qFuzzyCompare(oldInset.top(), value)) {
        emit q->topInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 149, as _ZN21QQuickTextAreaPrivate12setLeftInsetEdb
inline void QQuickTextAreaPrivate::setLeftInset(qreal value, bool reset)
{
    Q_Q(QQuickTextArea);
    const QMarginsF oldInset = getInset();
    extra.value().leftInset = value;
    extra.value().hasLeftInset = !reset;
    if (!qFuzzyCompare(oldInset.left(), value)) {
        emit q->leftInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 161, as _ZN21QQuickTextAreaPrivate13setRightInsetEdb
inline void QQuickTextAreaPrivate::setRightInset(qreal value, bool reset)
{
    Q_Q(QQuickTextArea);
    const QMarginsF oldInset = getInset();
    extra.value().rightInset = value;
    extra.value().hasRightInset = !reset;
    if (!qFuzzyCompare(oldInset.right(), value)) {
        emit q->rightInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 173, as _ZN21QQuickTextAreaPrivate14setBottomInsetEdb
inline void QQuickTextAreaPrivate::setBottomInset(qreal value, bool reset)
{
    Q_Q(QQuickTextArea);
    const QMarginsF oldInset = getInset();
    extra.value().bottomInset = value;
    extra.value().hasBottomInset = !reset;
    if (!qFuzzyCompare(oldInset.bottom(), value)) {
        emit q->bottomInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 185, as _ZN21QQuickTextAreaPrivate16resizeBackgroundEv
inline void QQuickTextAreaPrivate::resizeBackground()
{
    if (!background)
        return;

    resizingBackground = true;

    // When using the attached property TextArea.flickable, we reparent the background out
    // of TextArea and into the Flickable since we don't want the background to move while
    // flicking. This means that the size of the background should also follow the size of
    // the Flickable rather than the size of the TextArea.
    const auto flickable = qobject_cast<QQuickFlickable *>(background->parentItem());

    QQuickItemPrivate *p = QQuickItemPrivate::get(background);
    if (((!p->widthValid() || !extra.isAllocated() || !extra->hasBackgroundWidth) && qFuzzyIsNull(background->x()))
            || (extra.isAllocated() && (extra->hasLeftInset || extra->hasRightInset))) {
        const qreal bgWidth = flickable ? flickable->width() : width;
        background->setX(getLeftInset());
        background->setWidth(bgWidth - getLeftInset() - getRightInset());
    }

    if (((!p->heightValid() || !extra.isAllocated() || !extra->hasBackgroundHeight) && qFuzzyIsNull(background->y()))
            || (extra.isAllocated() && (extra->hasTopInset || extra->hasBottomInset))) {
        const qreal bgHeight = flickable ? flickable->height() : height;
        background->setY(getTopInset());
        background->setHeight(bgHeight - getTopInset() - getBottomInset());
    }

    resizingBackground = false;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 224, as _ZN21QQuickTextAreaPrivate11resolveFontEv
inline void QQuickTextAreaPrivate::resolveFont()
{
    Q_Q(QQuickTextArea);
    inheritFont(QQuickControlPrivate::parentFont(q));
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 230, as _ZN21QQuickTextAreaPrivate11inheritFontERK5QFont
inline void QQuickTextAreaPrivate::inheritFont(const QFont &font)
{
    QFont parentFont = extra.isAllocated() ? extra->requestedFont.resolve(font) : font;
    parentFont.setResolveMask(extra.isAllocated() ? extra->requestedFont.resolveMask() | font.resolveMask() : font.resolveMask());

    const QFont defaultFont = QQuickTheme::font(QQuickTheme::TextArea);
    QFont resolvedFont = parentFont.resolve(defaultFont);

    setFont_helper(resolvedFont);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 246, as _ZN21QQuickTextAreaPrivate10updateFontERK5QFont
inline void QQuickTextAreaPrivate::updateFont(const QFont &font)
{
    Q_Q(QQuickTextArea);
    QFont oldFont = sourceFont;
    q->QQuickTextEdit::setFont(font);

    QQuickControlPrivate::updateFontRecur(q, font);

    if (oldFont != font)
        emit q->fontChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 259, as _ZN21QQuickTextAreaPrivate18updateHoverEnabledEbb
#if QT_CONFIG(quicktemplates2_hover)
inline void QQuickTextAreaPrivate::updateHoverEnabled(bool enabled, bool xplicit)
{
    Q_Q(QQuickTextArea);
    if (!xplicit && explicitHoverEnabled)
        return;

    bool wasEnabled = q->isHoverEnabled();
    explicitHoverEnabled = xplicit;
    if (wasEnabled != enabled) {
        q->setAcceptHoverEvents(enabled);
        QQuickControlPrivate::updateHoverEnabledRecur(q, enabled);
        emit q->hoverEnabledChanged();
    }
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 275, as _ZN21QQuickTextAreaPrivate15attachFlickableEP15QQuickFlickable
inline void QQuickTextAreaPrivate::attachFlickable(QQuickFlickable *item)
{
    Q_Q(QQuickTextArea);
    flickable = item;
    q->setParentItem(flickable->contentItem());

    if (background)
        background->setParentItem(flickable);

    QObjectPrivate::connect(q, &QQuickTextArea::contentSizeChanged, this, &QQuickTextAreaPrivate::resizeFlickableContent);
    QObjectPrivate::connect(q, &QQuickTextEdit::cursorRectangleChanged, this, &QQuickTextAreaPrivate::ensureCursorVisible);

    QObject::connect(flickable, &QQuickFlickable::contentXChanged, q, &QQuickItem::update);
    QObject::connect(flickable, &QQuickFlickable::contentYChanged, q, &QQuickItem::update);

    QQuickItemPrivate::get(flickable)->updateOrAddGeometryChangeListener(this, QQuickGeometryChange::Size);
    QQuickItemPrivate::get(flickable)->addItemChangeListener(this, QQuickItemPrivate::Destroyed);
    QObjectPrivate::connect(flickable, &QQuickFlickable::contentWidthChanged, this, &QQuickTextAreaPrivate::resizeFlickableControl);
    QObjectPrivate::connect(flickable, &QQuickFlickable::contentHeightChanged, this, &QQuickTextAreaPrivate::resizeFlickableControl);

    resizeFlickableControl();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 298, as _ZN21QQuickTextAreaPrivate15detachFlickableEv
inline void QQuickTextAreaPrivate::detachFlickable()
{
    Q_Q(QQuickTextArea);
    q->setParentItem(nullptr);
    if (background && background->parentItem() == flickable)
        background->setParentItem(q);

    QObjectPrivate::disconnect(q, &QQuickTextArea::contentSizeChanged, this, &QQuickTextAreaPrivate::resizeFlickableContent);
    QObjectPrivate::disconnect(q, &QQuickTextEdit::cursorRectangleChanged, this, &QQuickTextAreaPrivate::ensureCursorVisible);

    QObject::disconnect(flickable, &QQuickFlickable::contentXChanged, q, &QQuickItem::update);
    QObject::disconnect(flickable, &QQuickFlickable::contentYChanged, q, &QQuickItem::update);

    QQuickItemPrivate::get(flickable)->updateOrRemoveGeometryChangeListener(this, QQuickGeometryChange::Nothing);
    QQuickItemPrivate::get(flickable)->removeItemChangeListener(this, QQuickItemPrivate::Destroyed);
    QObjectPrivate::disconnect(flickable, &QQuickFlickable::contentWidthChanged, this, &QQuickTextAreaPrivate::resizeFlickableControl);
    QObjectPrivate::disconnect(flickable, &QQuickFlickable::contentHeightChanged, this, &QQuickTextAreaPrivate::resizeFlickableControl);

    flickable = nullptr;

    resizeBackground();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 321, as _ZN21QQuickTextAreaPrivate19ensureCursorVisibleEv
inline void QQuickTextAreaPrivate::ensureCursorVisible()
{
    Q_Q(QQuickTextArea);
    if (!flickable)
        return;

    const qreal cx = flickable->contentX();
    const qreal cy = flickable->contentY();
    const qreal w = flickable->width();
    const qreal h = flickable->height();

    const qreal tp = q->topPadding();
    const qreal lp = q->leftPadding();
    const QRectF cr = q->cursorRectangle();

    if (cr.left() <= cx + lp) {
        flickable->setContentX(cr.left() - lp);
    } else {
        // calculate the rectangle of the next character and ensure that
        // it's visible if it's on the same line with the cursor
        const qreal rp = q->rightPadding();
        const QRectF nr = q->cursorPosition() < q->length() ? q->positionToRectangle(q->cursorPosition() + 1) : QRectF();
        if (qFuzzyCompare(nr.y(), cr.y()) && nr.right() >= cx + lp + w - rp)
            flickable->setContentX(nr.right() - w + rp);
        else if (cr.right() >= cx + lp + w - rp)
            flickable->setContentX(cr.right() - w + rp);
    }

    if (cr.top() <= cy + tp) {
        flickable->setContentY(cr.top() - tp);
    } else {
        const qreal bp = q->bottomPadding();
        if (cr.bottom() >= cy + tp + h - bp && cr.bottom() <= flickable->contentHeight())
            flickable->setContentY(cr.bottom() - h + bp);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 358, as _ZN21QQuickTextAreaPrivate22resizeFlickableControlEv
inline void QQuickTextAreaPrivate::resizeFlickableControl()
{
    Q_Q(QQuickTextArea);
    if (!flickable)
        return;

    const qreal w = wrapMode == QQuickTextArea::NoWrap ? qMax(flickable->width(), flickable->contentWidth()) : flickable->width();
    const qreal h = qMax(flickable->height(), flickable->contentHeight());
    q->setSize(QSizeF(w, h));

    resizeBackground();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 371, as _ZN21QQuickTextAreaPrivate22resizeFlickableContentEv
inline void QQuickTextAreaPrivate::resizeFlickableContent()
{
    Q_Q(QQuickTextArea);
    if (!flickable)
        return;

    flickable->setContentWidth(q->implicitWidth());
    flickable->setContentHeight(q->implicitHeight());
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 381, as _ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change, const QRectF &diff)
{
    Q_UNUSED(diff);
    if (!resizingBackground && item == background) {
        QQuickItemPrivate *p = QQuickItemPrivate::get(item);
        // Only set hasBackgroundWidth/Height if it was a width/height change,
        // otherwise we're prevented from setting a width/height in the future.
        if (change.widthChange())
            extra.value().hasBackgroundWidth = p->widthValid();
        if (change.heightChange())
            extra.value().hasBackgroundHeight = p->heightValid();
    }

    if (flickable)
        resizeFlickableControl();
    else
        resizeBackground();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 400, as _ZNK21QQuickTextAreaPrivate16getImplicitWidthEv
inline qreal QQuickTextAreaPrivate::getImplicitWidth() const
{
    return QQuickItemPrivate::getImplicitWidth();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 405, as _ZNK21QQuickTextAreaPrivate17getImplicitHeightEv
inline qreal QQuickTextAreaPrivate::getImplicitHeight() const
{
    return QQuickItemPrivate::getImplicitHeight();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 410, as _ZN21QQuickTextAreaPrivate20implicitWidthChangedEv
inline void QQuickTextAreaPrivate::implicitWidthChanged()
{
    if (!initialized) {
        QQuickTextEditPrivate::implicitWidthChanged();
        return;
    }
    Q_Q(QQuickTextArea);
    QQuickItemPrivate::implicitWidthChanged();
    emit q->implicitWidthChanged3();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 421, as _ZN21QQuickTextAreaPrivate21implicitHeightChangedEv
inline void QQuickTextAreaPrivate::implicitHeightChanged()
{
    if (!initialized) {
        QQuickTextEditPrivate::implicitHeightChanged();
        return;
    }
    Q_Q(QQuickTextArea);
    QQuickItemPrivate::implicitHeightChanged();
    emit q->implicitHeightChanged3();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 433, as _ZN21QQuickTextAreaPrivate26accessibilityActiveChangedEb
#if QT_CONFIG(accessibility)
inline void QQuickTextAreaPrivate::accessibilityActiveChanged(bool active)
{
    QQuickTextEditPrivate::accessibilityActiveChanged(active);
    if (QQuickAccessibleAttached *accessibleAttached = QQuickControlPrivate::accessibleAttached(q_func()))
        accessibleAttached->setDescriptionImplicitly(placeholder);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 441, as _ZN21QQuickTextAreaPrivate16cancelBackgroundEv
inline void QQuickTextAreaPrivate::cancelBackground()
{
    Q_Q(QQuickTextArea);
    quickCancelDeferred(q, backgroundName());
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 447, as _ZN21QQuickTextAreaPrivate17executeBackgroundEb
inline void QQuickTextAreaPrivate::executeBackground(bool complete)
{
    Q_Q(QQuickTextArea);
    if (background.wasExecuted())
        return;

    if (!background || complete)
        quickBeginDeferred(q, backgroundName(), background);
    if (complete)
        quickCompleteDeferred(q, backgroundName(), background);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 459, as _ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickTextArea);
    if (item == background)
        emit q->implicitBackgroundWidthChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 466, as _ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickTextArea);
    if (item == background)
        emit q->implicitBackgroundHeightChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 473, as _ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem
inline void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)
{
    Q_Q(QQuickTextArea);
    if (item == background) {
        background = nullptr;
        emit q->implicitBackgroundWidthChanged();
        emit q->implicitBackgroundHeightChanged();
    } else if (item == flickable) {
        detachFlickable();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 485, as _ZNK21QQuickTextAreaPrivate14defaultPaletteEv
inline QPalette QQuickTextAreaPrivate::defaultPalette() const
{
    return QQuickTheme::palette(QQuickTheme::TextArea);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextarea.cpp, line 490, as _ZN21QQuickTextAreaPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE
inline bool QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason reason)
{
    Q_Q(QQuickTextArea);
    const auto focusReasonChanged = QQuickItemPrivate::setLastFocusChangeReason(reason);
    if (focusReasonChanged)
        emit q->focusReasonChanged();

    return focusReasonChanged;
}
//  -----------------------------------------------------------------------

//  A QQuickTextAreaPrivate that Python can take functions over in. Every QQuickTextAreaPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextAreaPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef qreal (*CuteQQuickTextAreaPrivateCall1)(const void *, int *);
typedef qreal (*CuteQQuickTextAreaPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall4)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextAreaPrivateCall5)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextAreaPrivateCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall8)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickTextAreaPrivateCall9)(const void *, int *);
typedef bool (*CuteQQuickTextAreaPrivateCall10)(const void *, int, int *);
typedef void (*CuteQQuickTextAreaPrivateCall11)(const void *, int *);
typedef bool (*CuteQQuickTextAreaPrivateCall12)(const void *, QQuickItem *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTextAreaPrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTextAreaPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextAreaPrivateCall15)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall16)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTextAreaPrivateCall17)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall18)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTextAreaPrivateCall19)(const void *, QPointerEvent *, bool, int *);
typedef void (*CuteQQuickTextAreaPrivateCall20)(const void *, bool, int *);
typedef void * (*CuteQQuickTextAreaPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickTextAreaPrivateCall23)(const void *, int, int *);
class CuteQQuickTextAreaPrivate : public QQuickTextAreaPrivate {
public:
  using QQuickTextAreaPrivate::QQuickTextAreaPrivate;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQuickTextAreaPrivate14defaultPaletteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[23] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall0 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall0>(taken[0]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::itemGeometryChanged(item, change, diff);
  }

  //  qreal QQuickTextAreaPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall1 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextAreaPrivate::getImplicitWidth();
  }

  //  qreal QQuickTextAreaPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall2 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextAreaPrivate::getImplicitHeight();
  }

  //  void QQuickTextAreaPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall3 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::implicitWidthChanged();
  }

  //  void QQuickTextAreaPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall4 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickTextAreaPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall5 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall5>(taken[5]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall6 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall7 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall8 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextAreaPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickTextAreaPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall9 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall9>(taken[9]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextAreaPrivate::defaultPalette();
  }

  //  bool QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall10 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall10>(taken[10]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickTextAreaPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickTextEditPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall11 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEditPrivate::mirrorChange();
  }

  //  bool QQuickTextEditPrivate::transformChanged(QQuickItem
  //      *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall12 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall12>(taken[12]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickTextEditPrivate::transformChanged(transformedItem);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall13 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickTextEditPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickTextEditPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall14 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickTextEditPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall15 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall15>(taken[15]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall16 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall16>(taken[16]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall17 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall17>(taken[17]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall18 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall18>(taken[18]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall19 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall19>(taken[19]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall20 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall20>(taken[20]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall21 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall22 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextAreaPrivateCall23 call = reinterpret_cast<CuteQQuickTextAreaPrivateCall23>(taken[23]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTextArea *QQuickTextAreaPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextArea *ritual_ZN21QQuickTextAreaPrivate6q_funcEv(
    QQuickTextAreaPrivate *self) {
  return self->q_func();
}

//  const QQuickTextArea *QQuickTextAreaPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextArea *ritual_ZNK21QQuickTextAreaPrivate6q_funcEv(
    const QQuickTextAreaPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(accessibility)
//  QQuickTextAreaPrivate::QQuickTextAreaPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextAreaPrivate *ritual_ZN21QQuickTextAreaPrivateC1Ev() {
  return new CuteQQuickTextAreaPrivate();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickTextAreaPrivate::~QQuickTextAreaPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivateD1Ev(QQuickTextAreaPrivate *self) {
  delete self;
}

//  QQuickTextAreaPrivate *QQuickTextAreaPrivate::get(QQuickTextArea *item)
extern "C" Q_DECL_EXPORT
QQuickTextAreaPrivate *ritual_ZN21QQuickTextAreaPrivate3getEP14QQuickTextArea(
    QQuickTextArea *item) {
  return QQuickTextAreaPrivate::get(item);
}

//  QMarginsF QQuickTextAreaPrivate::getInset() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK21QQuickTextAreaPrivate8getInsetEv(
    const QQuickTextAreaPrivate *self) {
  return new QMarginsF(self->getInset());
}

//  qreal QQuickTextAreaPrivate::getTopInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate11getTopInsetEv(
    const QQuickTextAreaPrivate *self) {
  return self->getTopInset();
}

//  qreal QQuickTextAreaPrivate::getLeftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate12getLeftInsetEv(
    const QQuickTextAreaPrivate *self) {
  return self->getLeftInset();
}

//  qreal QQuickTextAreaPrivate::getRightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate13getRightInsetEv(
    const QQuickTextAreaPrivate *self) {
  return self->getRightInset();
}

//  qreal QQuickTextAreaPrivate::getBottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate14getBottomInsetEv(
    const QQuickTextAreaPrivate *self) {
  return self->getBottomInset();
}

//  void QQuickTextAreaPrivate::setTopInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate11setTopInsetEdb(
    QQuickTextAreaPrivate *self,
    qreal value,
    bool reset) {
  self->setTopInset(value, reset);
}

//  void QQuickTextAreaPrivate::setLeftInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate12setLeftInsetEdb(
    QQuickTextAreaPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftInset(value, reset);
}

//  void QQuickTextAreaPrivate::setRightInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate13setRightInsetEdb(
    QQuickTextAreaPrivate *self,
    qreal value,
    bool reset) {
  self->setRightInset(value, reset);
}

//  void QQuickTextAreaPrivate::setBottomInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate14setBottomInsetEdb(
    QQuickTextAreaPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomInset(value, reset);
}

//  void QQuickTextAreaPrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate16resizeBackgroundEv(
    QQuickTextAreaPrivate *self) {
  self->resizeBackground();
}

//  void QQuickTextAreaPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate11resolveFontEv(
    QQuickTextAreaPrivate *self) {
  self->resolveFont();
}

//  void QQuickTextAreaPrivate::inheritFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate11inheritFontERK5QFont(
    QQuickTextAreaPrivate *self,
    const QFont *font) {
  self->inheritFont(*font);
}

//  void QQuickTextAreaPrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate10updateFontERK5QFont(
    QQuickTextAreaPrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  void QQuickTextAreaPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate14setFont_helperERK5QFont(
    QQuickTextAreaPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextAreaPrivate::updateHoverEnabled(bool h, bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate18updateHoverEnabledEbb(
    QQuickTextAreaPrivate *self,
    bool h,
    bool e) {
  self->updateHoverEnabled(h, e);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickTextAreaPrivate::attachFlickable(QQuickFlickable *flickable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate15attachFlickableEP15QQuickFlickable(
    QQuickTextAreaPrivate *self,
    QQuickFlickable *flickable) {
  self->attachFlickable(flickable);
}

//  void QQuickTextAreaPrivate::detachFlickable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate15detachFlickableEv(
    QQuickTextAreaPrivate *self) {
  self->detachFlickable();
}

//  void QQuickTextAreaPrivate::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate19ensureCursorVisibleEv(
    QQuickTextAreaPrivate *self) {
  self->ensureCursorVisible();
}

//  void QQuickTextAreaPrivate::resizeFlickableControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate22resizeFlickableControlEv(
    QQuickTextAreaPrivate *self) {
  self->resizeFlickableControl();
}

//  void QQuickTextAreaPrivate::resizeFlickableContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate22resizeFlickableContentEv(
    QQuickTextAreaPrivate *self) {
  self->resizeFlickableContent();
}

//  void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTextAreaPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  qreal QQuickTextAreaPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate16getImplicitWidthEv(
    const QQuickTextAreaPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickTextAreaPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextAreaPrivate17getImplicitHeightEv(
    const QQuickTextAreaPrivate *self) {
  return self->getImplicitHeight();
}

//  void QQuickTextAreaPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate20implicitWidthChangedEv(
    QQuickTextAreaPrivate *self) {
  self->implicitWidthChanged();
}

//  void QQuickTextAreaPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate21implicitHeightChangedEv(
    QQuickTextAreaPrivate *self) {
  self->implicitHeightChanged();
}

#if QT_CONFIG(accessibility)
//  void QQuickTextAreaPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate26accessibilityActiveChangedEb(
    QQuickTextAreaPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickTextAreaPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate16cancelBackgroundEv(
    QQuickTextAreaPrivate *self) {
  self->cancelBackground();
}

//  void QQuickTextAreaPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate17executeBackgroundEb(
    QQuickTextAreaPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  void QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QPalette QQuickTextAreaPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK21QQuickTextAreaPrivate14defaultPaletteEv(
    const QQuickTextAreaPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  bool QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextAreaPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickTextAreaPrivate *self,
    Qt::FocusReason reason) {
  return self->setLastFocusChangeReason(reason);
}

//  a Python function taken by a CuteQQuickTextAreaPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextAreaPrivate(
    QQuickTextAreaPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextAreaPrivate *>(self)->take(key, call);
}

//  void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTextAreaPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickTextAreaPrivate::itemGeometryChanged(item, *change, *diff);
}

//  qreal QQuickTextAreaPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QQuickTextAreaPrivate16getImplicitWidthEv(
    const QQuickTextAreaPrivate *self) {
  return self->QQuickTextAreaPrivate::getImplicitWidth();
}

//  qreal QQuickTextAreaPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QQuickTextAreaPrivate17getImplicitHeightEv(
    const QQuickTextAreaPrivate *self) {
  return self->QQuickTextAreaPrivate::getImplicitHeight();
}

//  void QQuickTextAreaPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate20implicitWidthChangedEv(
    QQuickTextAreaPrivate *self) {
  self->QQuickTextAreaPrivate::implicitWidthChanged();
}

//  void QQuickTextAreaPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate21implicitHeightChangedEv(
    QQuickTextAreaPrivate *self) {
  self->QQuickTextAreaPrivate::implicitHeightChanged();
}

#if QT_CONFIG(accessibility)
//  void QQuickTextAreaPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate26accessibilityActiveChangedEb(
    QQuickTextAreaPrivate *self,
    bool active) {
  self->QQuickTextAreaPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->QQuickTextAreaPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->QQuickTextAreaPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem(
    QQuickTextAreaPrivate *self,
    QQuickItem *item) {
  self->QQuickTextAreaPrivate::itemDestroyed(item);
}

//  QPalette QQuickTextAreaPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK21QQuickTextAreaPrivate14defaultPaletteEv(
    const QQuickTextAreaPrivate *self) {
  return new QPalette(self->QQuickTextAreaPrivate::defaultPalette());
}

//  bool QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickTextAreaPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickTextAreaPrivate *self,
    Qt::FocusReason reason) {
  return self->QQuickTextAreaPrivate::setLastFocusChangeReason(reason);
}
