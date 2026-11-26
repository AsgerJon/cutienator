//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicktextfield_p.h>
#include <QtQuickTemplates2/private/qquicktextfield_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtQuickTemplates2/private/qquicktooltip_p_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquicktextinput_p.h>
#include <QtQuick/private/qquickclipnode_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
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

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 259, as _ZN22QQuickTextFieldPrivate15readOnlyChangedEb
inline void QQuickTextFieldPrivate::readOnlyChanged(bool isReadOnly)
{
    QQuickTextInputPrivate::readOnlyChanged(isReadOnly);
#if QT_CONFIG(cursor)
    q_func()->setCursor(isReadOnly && !selectByMouse ? Qt::ArrowCursor : Qt::IBeamCursor);
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 91, as _ZN22QQuickTextFieldPrivateC1Ev
inline QQuickTextFieldPrivate::QQuickTextFieldPrivate()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 95, as _ZN22QQuickTextFieldPrivateD1Ev
inline QQuickTextFieldPrivate::~QQuickTextFieldPrivate()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 99, as _ZN22QQuickTextFieldPrivate11setTopInsetEdb
inline void QQuickTextFieldPrivate::setTopInset(qreal value, bool reset)
{
    Q_Q(QQuickTextField);
    const QMarginsF oldInset = getInset();
    extra.value().topInset = value;
    extra.value().hasTopInset = !reset;
    if (!qFuzzyCompare(oldInset.top(), value)) {
        emit q->topInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 111, as _ZN22QQuickTextFieldPrivate12setLeftInsetEdb
inline void QQuickTextFieldPrivate::setLeftInset(qreal value, bool reset)
{
    Q_Q(QQuickTextField);
    const QMarginsF oldInset = getInset();
    extra.value().leftInset = value;
    extra.value().hasLeftInset = !reset;
    if (!qFuzzyCompare(oldInset.left(), value)) {
        emit q->leftInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 123, as _ZN22QQuickTextFieldPrivate13setRightInsetEdb
inline void QQuickTextFieldPrivate::setRightInset(qreal value, bool reset)
{
    Q_Q(QQuickTextField);
    const QMarginsF oldInset = getInset();
    extra.value().rightInset = value;
    extra.value().hasRightInset = !reset;
    if (!qFuzzyCompare(oldInset.right(), value)) {
        emit q->rightInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 135, as _ZN22QQuickTextFieldPrivate14setBottomInsetEdb
inline void QQuickTextFieldPrivate::setBottomInset(qreal value, bool reset)
{
    Q_Q(QQuickTextField);
    const QMarginsF oldInset = getInset();
    extra.value().bottomInset = value;
    extra.value().hasBottomInset = !reset;
    if (!qFuzzyCompare(oldInset.bottom(), value)) {
        emit q->bottomInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 147, as _ZN22QQuickTextFieldPrivate16resizeBackgroundEv
inline void QQuickTextFieldPrivate::resizeBackground()
{
    if (!background)
        return;

    resizingBackground = true;

    QQuickItemPrivate *p = QQuickItemPrivate::get(background);
    if (((!p->widthValid() || !extra.isAllocated() || !extra->hasBackgroundWidth) && qFuzzyIsNull(background->x()))
            || (extra.isAllocated() && (extra->hasLeftInset || extra->hasRightInset))) {
        const bool wasWidthValid = p->widthValid();
        background->setX(getLeftInset());
        background->setWidth(width - getLeftInset() - getRightInset());
        // If the user hadn't previously set the width, that shouldn't change when we set it for them.
        if (!wasWidthValid)
            p->widthValidFlag = false;
    }
    if (((!p->heightValid() || !extra.isAllocated() || !extra->hasBackgroundHeight) && qFuzzyIsNull(background->y()))
            || (extra.isAllocated() && (extra->hasTopInset || extra->hasBottomInset))) {
        const bool wasHeightValid = p->heightValid();
        background->setY(getTopInset());
        background->setHeight(height - getTopInset() - getBottomInset());
        if (!wasHeightValid)
            p->heightValidFlag = false;
    }

    resizingBackground = false;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 184, as _ZN22QQuickTextFieldPrivate11resolveFontEv
inline void QQuickTextFieldPrivate::resolveFont()
{
    Q_Q(QQuickTextField);
    inheritFont(QQuickControlPrivate::parentFont(q));
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 190, as _ZN22QQuickTextFieldPrivate11inheritFontERK5QFont
inline void QQuickTextFieldPrivate::inheritFont(const QFont &font)
{
    QFont parentFont = extra.isAllocated() ? extra->requestedFont.resolve(font) : font;
    parentFont.setResolveMask(extra.isAllocated() ? extra->requestedFont.resolveMask() | font.resolveMask() : font.resolveMask());

    const QFont defaultFont = QQuickTheme::font(QQuickTheme::TextField);
    QFont resolvedFont = parentFont.resolve(defaultFont);

    setFont_helper(resolvedFont);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 206, as _ZN22QQuickTextFieldPrivate10updateFontERK5QFont
inline void QQuickTextFieldPrivate::updateFont(const QFont &font)
{
    Q_Q(QQuickTextField);
    QFont oldFont = sourceFont;
    q->QQuickTextInput::setFont(font);

    QQuickControlPrivate::updateFontRecur(q, font);

    if (oldFont != font)
        emit q->fontChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 219, as _ZN22QQuickTextFieldPrivate18updateHoverEnabledEbb
#if QT_CONFIG(quicktemplates2_hover)
inline void QQuickTextFieldPrivate::updateHoverEnabled(bool enabled, bool xplicit)
{
    Q_Q(QQuickTextField);
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

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 235, as _ZNK22QQuickTextFieldPrivate16getImplicitWidthEv
inline qreal QQuickTextFieldPrivate::getImplicitWidth() const
{
    return QQuickItemPrivate::getImplicitWidth();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 240, as _ZNK22QQuickTextFieldPrivate17getImplicitHeightEv
inline qreal QQuickTextFieldPrivate::getImplicitHeight() const
{
    return QQuickItemPrivate::getImplicitHeight();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 245, as _ZN22QQuickTextFieldPrivate20implicitWidthChangedEv
inline void QQuickTextFieldPrivate::implicitWidthChanged()
{
    Q_Q(QQuickTextField);
    QQuickItemPrivate::implicitWidthChanged();
    emit q->implicitWidthChanged3();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 252, as _ZN22QQuickTextFieldPrivate21implicitHeightChangedEv
inline void QQuickTextFieldPrivate::implicitHeightChanged()
{
    Q_Q(QQuickTextField);
    QQuickItemPrivate::implicitHeightChanged();
    emit q->implicitHeightChanged3();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 268, as _ZN22QQuickTextFieldPrivate26accessibilityActiveChangedEb
#if QT_CONFIG(accessibility)
inline void QQuickTextFieldPrivate::accessibilityActiveChanged(bool active)
{
    QQuickTextInputPrivate::accessibilityActiveChanged(active);

    if (!active)
        return;
    Q_Q(QQuickTextField);
    QQuickAccessibleAttached *accessibleAttached = qobject_cast<QQuickAccessibleAttached *>(qmlAttachedPropertiesObject<QQuickAccessibleAttached>(q, true));
    Q_ASSERT(accessibleAttached);
    accessibleAttached->setDescriptionImplicitly(placeholder);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 282, as _ZN22QQuickTextFieldPrivate16cancelBackgroundEv
inline void QQuickTextFieldPrivate::cancelBackground()
{
    Q_Q(QQuickTextField);
    quickCancelDeferred(q, backgroundName());
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 288, as _ZN22QQuickTextFieldPrivate17executeBackgroundEb
inline void QQuickTextFieldPrivate::executeBackground(bool complete)
{
    Q_Q(QQuickTextField);
    if (background.wasExecuted())
        return;

    if (!background || complete)
        quickBeginDeferred(q, backgroundName(), background);
    if (complete)
        quickCompleteDeferred(q, backgroundName(), background);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 300, as _ZN22QQuickTextFieldPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change, const QRectF &diff)
{
    Q_UNUSED(diff);
    if (resizingBackground || item != background || !change.sizeChange())
        return;

    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    // QTBUG-71875: only allocate the extra data if we have to.
    // resizeBackground() relies on the value of extra.isAllocated()
    // as part of its checks to see whether it should resize the background or not.
    if (p->widthValid() || extra.isAllocated())
        extra.value().hasBackgroundWidth = p->widthValid();
    if (p->heightValid() || extra.isAllocated())
        extra.value().hasBackgroundHeight = p->heightValid();
    resizeBackground();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 317, as _ZN22QQuickTextFieldPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickTextField);
    if (item == background)
        emit q->implicitBackgroundWidthChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 324, as _ZN22QQuickTextFieldPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickTextField);
    if (item == background)
        emit q->implicitBackgroundHeightChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 331, as _ZN22QQuickTextFieldPrivate13itemDestroyedEP10QQuickItem
inline void QQuickTextFieldPrivate::itemDestroyed(QQuickItem *item)
{
    Q_Q(QQuickTextField);
    if (item == background) {
        background = nullptr;
        emit q->implicitBackgroundWidthChanged();
        emit q->implicitBackgroundHeightChanged();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 341, as _ZNK22QQuickTextFieldPrivate14defaultPaletteEv
inline QPalette QQuickTextFieldPrivate::defaultPalette() const
{
    return QQuickTheme::palette(QQuickTheme::TextField);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktextfield.cpp, line 346, as _ZN22QQuickTextFieldPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE
inline bool QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason reason)
{
    Q_Q(QQuickTextField);
    const auto focusReasonChanged = QQuickItemPrivate::setLastFocusChangeReason(reason);
    if (focusReasonChanged)
        emit q->focusReasonChanged();

    return focusReasonChanged;
}
//  -----------------------------------------------------------------------

//  A QQuickTextFieldPrivate that Python can take functions over in. Every QQuickTextFieldPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickTextFieldPrivateCall0)(const void *, int *);
typedef qreal (*CuteQQuickTextFieldPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall4)(const void *, bool, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextFieldPrivateCall5)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextFieldPrivateCall6)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall9)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickTextFieldPrivateCall10)(const void *, int *);
typedef bool (*CuteQQuickTextFieldPrivateCall11)(const void *, int, int *);
typedef void (*CuteQQuickTextFieldPrivateCall12)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTextFieldPrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTextFieldPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextFieldPrivateCall15)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall16)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTextFieldPrivateCall17)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall18)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTextFieldPrivateCall19)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickTextFieldPrivateCall20)(const void *, QPointerEvent *, bool, int *);
typedef void (*CuteQQuickTextFieldPrivateCall21)(const void *, bool, int *);
typedef void * (*CuteQQuickTextFieldPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall23)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall24)(const void *, int, int *);
typedef void (*CuteQQuickTextFieldPrivateCall25)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall26)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall27)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall28)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall29)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall30)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall31)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall32)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall33)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickTextFieldPrivateCall34)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall35)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickTextFieldPrivateCall36)(const void *, int *);
typedef bool (*CuteQQuickTextFieldPrivateCall37)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickTextFieldPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall39)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTextFieldPrivateCall40)(const void *, QQuickItem *, int *);
class CuteQQuickTextFieldPrivate : public QQuickTextFieldPrivate {
public:
  using QQuickTextFieldPrivate::QQuickTextFieldPrivate;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickTextInputPrivate15readOnlyChangedEb")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickTextFieldPrivate14defaultPaletteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
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
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[40] = call;
      return true;
    }
    return false;
  }

  //  qreal QQuickTextFieldPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall0 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextFieldPrivate::getImplicitWidth();
  }

  //  qreal QQuickTextFieldPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall1 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextFieldPrivate::getImplicitHeight();
  }

  //  void QQuickTextFieldPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall2 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::implicitWidthChanged();
  }

  //  void QQuickTextFieldPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall3 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::implicitHeightChanged();
  }

  //  void QQuickTextFieldPrivate::readOnlyChanged(bool isReadOnly)
  void readOnlyChanged(bool isReadOnly) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall4 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall4>(taken[4]);
      call(this, isReadOnly, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::readOnlyChanged(isReadOnly);
  }

#if QT_CONFIG(accessibility)
  //  void QQuickTextFieldPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall5 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall5>(taken[5]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall6 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall6>(taken[6]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall7 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall8 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickTextFieldPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall9 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTextFieldPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickTextFieldPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall10 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall10>(taken[10]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextFieldPrivate::defaultPalette();
  }

  //  bool QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall11 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall11>(taken[11]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickTextFieldPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickTextInputPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall12 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInputPrivate::mirrorChange();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall13 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickTextInputPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickTextInputPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall14 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickTextInputPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall15 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall15>(taken[15]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall16 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall16>(taken[16]);
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
      CuteQQuickTextFieldPrivateCall17 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall17>(taken[17]);
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
      CuteQQuickTextFieldPrivateCall18 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall18>(taken[18]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall19 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall19>(taken[19]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall20 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall20>(taken[20]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall21 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall21>(taken[21]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall22 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall23 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall24 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall24>(taken[24]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall25 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall26 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall27 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall28 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall29 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall29>(taken[29]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall30 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall30>(taken[30]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall31 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall32 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall33 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall33>(taken[33]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall34 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall35 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall35>(taken[35]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall36 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall37 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall37>(taken[37]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall38 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall38>(taken[38]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickItemChangeListener::debugName();
  }

  //  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
  void addSourceItem(QQuickItem *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall39 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTextFieldPrivateCall40 call = reinterpret_cast<CuteQQuickTextFieldPrivateCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }
};

//  QQuickTextField *QQuickTextFieldPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZN22QQuickTextFieldPrivate6q_funcEv(
    QQuickTextFieldPrivate *self) {
  return self->q_func();
}

//  const QQuickTextField *QQuickTextFieldPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextField *ritual_ZNK22QQuickTextFieldPrivate6q_funcEv(
    const QQuickTextFieldPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(accessibility)
//  QQuickTextFieldPrivate::QQuickTextFieldPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextFieldPrivate *ritual_ZN22QQuickTextFieldPrivateC1Ev() {
  return new CuteQQuickTextFieldPrivate();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickTextFieldPrivate::~QQuickTextFieldPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivateD1Ev(QQuickTextFieldPrivate *self) {
  delete self;
}

//  QQuickTextFieldPrivate *QQuickTextFieldPrivate::get(QQuickTextField
//      *item)
extern "C" Q_DECL_EXPORT
QQuickTextFieldPrivate *ritual_ZN22QQuickTextFieldPrivate3getEP15QQuickTextField(
    QQuickTextField *item) {
  return QQuickTextFieldPrivate::get(item);
}

//  QMarginsF QQuickTextFieldPrivate::getInset() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK22QQuickTextFieldPrivate8getInsetEv(
    const QQuickTextFieldPrivate *self) {
  return new QMarginsF(self->getInset());
}

//  qreal QQuickTextFieldPrivate::getTopInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate11getTopInsetEv(
    const QQuickTextFieldPrivate *self) {
  return self->getTopInset();
}

//  qreal QQuickTextFieldPrivate::getLeftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate12getLeftInsetEv(
    const QQuickTextFieldPrivate *self) {
  return self->getLeftInset();
}

//  qreal QQuickTextFieldPrivate::getRightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate13getRightInsetEv(
    const QQuickTextFieldPrivate *self) {
  return self->getRightInset();
}

//  qreal QQuickTextFieldPrivate::getBottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate14getBottomInsetEv(
    const QQuickTextFieldPrivate *self) {
  return self->getBottomInset();
}

//  void QQuickTextFieldPrivate::setTopInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate11setTopInsetEdb(
    QQuickTextFieldPrivate *self,
    qreal value,
    bool reset) {
  self->setTopInset(value, reset);
}

//  void QQuickTextFieldPrivate::setLeftInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate12setLeftInsetEdb(
    QQuickTextFieldPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftInset(value, reset);
}

//  void QQuickTextFieldPrivate::setRightInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate13setRightInsetEdb(
    QQuickTextFieldPrivate *self,
    qreal value,
    bool reset) {
  self->setRightInset(value, reset);
}

//  void QQuickTextFieldPrivate::setBottomInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate14setBottomInsetEdb(
    QQuickTextFieldPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomInset(value, reset);
}

//  void QQuickTextFieldPrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate16resizeBackgroundEv(
    QQuickTextFieldPrivate *self) {
  self->resizeBackground();
}

//  void QQuickTextFieldPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate11resolveFontEv(
    QQuickTextFieldPrivate *self) {
  self->resolveFont();
}

//  void QQuickTextFieldPrivate::inheritFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate11inheritFontERK5QFont(
    QQuickTextFieldPrivate *self,
    const QFont *font) {
  self->inheritFont(*font);
}

//  void QQuickTextFieldPrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate10updateFontERK5QFont(
    QQuickTextFieldPrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  void QQuickTextFieldPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate14setFont_helperERK5QFont(
    QQuickTextFieldPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextFieldPrivate::updateHoverEnabled(bool h, bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate18updateHoverEnabledEbb(
    QQuickTextFieldPrivate *self,
    bool h,
    bool e) {
  self->updateHoverEnabled(h, e);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  qreal QQuickTextFieldPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate16getImplicitWidthEv(
    const QQuickTextFieldPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickTextFieldPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextFieldPrivate17getImplicitHeightEv(
    const QQuickTextFieldPrivate *self) {
  return self->getImplicitHeight();
}

//  void QQuickTextFieldPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate20implicitWidthChangedEv(
    QQuickTextFieldPrivate *self) {
  self->implicitWidthChanged();
}

//  void QQuickTextFieldPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate21implicitHeightChangedEv(
    QQuickTextFieldPrivate *self) {
  self->implicitHeightChanged();
}

//  void QQuickTextFieldPrivate::readOnlyChanged(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate15readOnlyChangedEb(
    QQuickTextFieldPrivate *self,
    bool isReadOnly) {
  self->readOnlyChanged(isReadOnly);
}

#if QT_CONFIG(accessibility)
//  void QQuickTextFieldPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate26accessibilityActiveChangedEb(
    QQuickTextFieldPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickTextFieldPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate16cancelBackgroundEv(
    QQuickTextFieldPrivate *self) {
  self->cancelBackground();
}

//  void QQuickTextFieldPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate17executeBackgroundEb(
    QQuickTextFieldPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTextFieldPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickTextFieldPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextFieldPrivate13itemDestroyedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QPalette QQuickTextFieldPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK22QQuickTextFieldPrivate14defaultPaletteEv(
    const QQuickTextFieldPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  bool QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextFieldPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickTextFieldPrivate *self,
    Qt::FocusReason reason) {
  return self->setLastFocusChangeReason(reason);
}

//  QQuickTextFieldPrivate as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickTextFieldPrivate_QQuickItemChangeListener(
    QQuickTextFieldPrivate *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickTextFieldPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextFieldPrivate(
    QQuickTextFieldPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextFieldPrivate *>(self)->take(key, call);
}

//  qreal QQuickTextFieldPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QQuickTextFieldPrivate16getImplicitWidthEv(
    const QQuickTextFieldPrivate *self) {
  return self->QQuickTextFieldPrivate::getImplicitWidth();
}

//  qreal QQuickTextFieldPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QQuickTextFieldPrivate17getImplicitHeightEv(
    const QQuickTextFieldPrivate *self) {
  return self->QQuickTextFieldPrivate::getImplicitHeight();
}

//  void QQuickTextFieldPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate20implicitWidthChangedEv(
    QQuickTextFieldPrivate *self) {
  self->QQuickTextFieldPrivate::implicitWidthChanged();
}

//  void QQuickTextFieldPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate21implicitHeightChangedEv(
    QQuickTextFieldPrivate *self) {
  self->QQuickTextFieldPrivate::implicitHeightChanged();
}

//  void QQuickTextFieldPrivate::readOnlyChanged(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate15readOnlyChangedEb(
    QQuickTextFieldPrivate *self,
    bool isReadOnly) {
  self->QQuickTextFieldPrivate::readOnlyChanged(isReadOnly);
}

#if QT_CONFIG(accessibility)
//  void QQuickTextFieldPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate26accessibilityActiveChangedEb(
    QQuickTextFieldPrivate *self,
    bool active) {
  self->QQuickTextFieldPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTextFieldPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickTextFieldPrivate::itemGeometryChanged(item, *change, *diff);
}

//  void QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->QQuickTextFieldPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->QQuickTextFieldPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickTextFieldPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextFieldPrivate13itemDestroyedEP10QQuickItem(
    QQuickTextFieldPrivate *self,
    QQuickItem *item) {
  self->QQuickTextFieldPrivate::itemDestroyed(item);
}

//  QPalette QQuickTextFieldPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK22QQuickTextFieldPrivate14defaultPaletteEv(
    const QQuickTextFieldPrivate *self) {
  return new QPalette(self->QQuickTextFieldPrivate::defaultPalette());
}

//  bool QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickTextFieldPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickTextFieldPrivate *self,
    Qt::FocusReason reason) {
  return self->QQuickTextFieldPrivate::setLastFocusChangeReason(reason);
}
