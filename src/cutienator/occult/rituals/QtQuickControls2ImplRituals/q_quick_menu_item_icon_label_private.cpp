//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qkeysequence.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/private/qquickiconlabel_p.h>
#include <QtQuickControls2Impl/private/qquickiconlabel_p_p.h>
#include <QtQuickControls2Impl/private/qquickiconimage_p.h>
#include <QtQuickControls2Impl/private/qquickmnemoniclabel_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuickTemplates2/private/qquickicon_p.h>
#include <QtQuickTemplates2/private/qquickicon_p_p.h>
#include <QtQuickControls2Impl/private/qquickiconimage_p.h>
#include <QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h>
#include <QtQuickControls2Impl/private/qquickmenuitemiconlabel_p_p.h>
#include <QtQuickControls2Impl/private/qquickmnemoniclabel_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuickTemplates2/private/qquickaction_p.h>
#include <QtQuickTemplates2/private/qquickmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 312, as local:qquickiconlabel.cpp:itemChangeTypes
static const QQuickItemPrivate::ChangeTypes itemChangeTypes =
    QQuickItemPrivate::ImplicitWidth
    | QQuickItemPrivate::ImplicitHeight
    | QQuickItemPrivate::Destroyed;

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 18, as _ZN22QQuickIconLabelPrivate10beginClassEP10QQuickItem
inline void QQuickIconLabelPrivate::beginClass(QQuickItem *item)
{
    if (QQmlParserStatus *parserStatus = qobject_cast<QQmlParserStatus *>(item))
        parserStatus->classBegin();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 317, as _ZN22QQuickIconLabelPrivate12watchChangesEP10QQuickItem
inline void QQuickIconLabelPrivate::watchChanges(QQuickItem *item)
{
    QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);
    itemPrivate->addItemChangeListener(this, itemChangeTypes);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 24, as _ZN22QQuickIconLabelPrivate17completeComponentEP10QQuickItem
inline void QQuickIconLabelPrivate::completeComponent(QQuickItem *item)
{
    if (QQmlParserStatus *parserStatus = qobject_cast<QQmlParserStatus *>(item))
        parserStatus->componentComplete();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 86, as _ZN30QQuickMenuItemIconLabelPrivate18updateImplicitSizeEv
inline void QQuickMenuItemIconLabelPrivate::updateImplicitSize()
{
    Q_Q(QQuickMenuItemIconLabel);
    const bool showIcon = image && hasIcon();
    const bool showText = label && hasText();
#if QT_CONFIG(shortcut)
    const bool showShortcutText = shortcutLabel && !shortcut().isEmpty();
#else
    const bool showShortcutText = false;
#endif
    const qreal horizontalPadding = leftPadding + rightPadding;
    const qreal verticalPadding = topPadding + bottomPadding;
    const qreal iconImplicitWidth = showIcon ? image->implicitWidth() : 0;
    const qreal iconImplicitHeight = showIcon ? image->implicitHeight() : 0;
    const qreal textImplicitWidth = showText ? label->implicitWidth() : 0;
    const qreal textImplicitHeight = showText ? label->implicitHeight() : 0;
    const qreal shortcutTextImplicitWidth = showShortcutText ? shortcutLabel->implicitWidth() : 0;
    const qreal shortcutTextImplicitHeight = showShortcutText ? shortcutLabel->implicitHeight() : 0;
    qreal effectiveSpacing = showText && showIcon && image->implicitWidth() > 0 ? spacing : 0;
    if (showShortcutText && shortcutLabel->implicitWidth() > 0)
        effectiveSpacing += spacing;
    const qreal implicitWidth = display == QQuickIconLabel::TextBesideIcon
        ? iconImplicitWidth + textImplicitWidth + shortcutTextImplicitHeight + effectiveSpacing
        : qMax(qMax(iconImplicitWidth, textImplicitWidth), shortcutTextImplicitWidth);
    const qreal implicitHeight = display == QQuickIconLabel::TextUnderIcon
        ? iconImplicitHeight + textImplicitHeight + shortcutTextImplicitHeight + effectiveSpacing
        : qMax(qMax(iconImplicitHeight, textImplicitHeight), shortcutTextImplicitHeight);
    q->setImplicitSize(implicitWidth + horizontalPadding, implicitHeight + verticalPadding);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 116, as _ZN30QQuickMenuItemIconLabelPrivate6layoutEv
inline void QQuickMenuItemIconLabelPrivate::layout()
{
    Q_Q(QQuickIconLabel);
    if (!componentComplete)
        return;

    const qreal availableWidth = width - leftPadding - rightPadding;
    const qreal availableHeight = height - topPadding - bottomPadding;

    auto layoutShortcutLabel = [this, availableWidth, availableHeight](const qreal availableWidthForShortcut){
        if (availableWidthForShortcut - spacing - shortcutLabel->implicitWidth() > 0) {
            // There's enough space for everyone.
            shortcutLabel->setVisible(true);

            // We can simply align ourselves to the right of the entire available space.
            const QRectF shortcutTextRect = alignedRect(mirrored, Qt::AlignRight | Qt::AlignVCenter, QSizeF(
                    qMin(shortcutLabel->implicitWidth(), availableWidth),
                    qMin(shortcutLabel->implicitHeight(), availableHeight)),
                QRectF(leftPadding, topPadding, availableWidth, availableHeight));
            shortcutLabel->setSize(shortcutTextRect.size());
            shortcutLabel->setPosition(shortcutTextRect.topLeft());
        } else {
            // No space for us. As Widgets doesn't bother with eliding, neither do we; we just
            // don't show the shortcut if there's no room for it. The most important part of the
            // menu item is the text, anyway.
            shortcutLabel->setVisible(false);
        }
    };

    switch (display) {
    case QQuickIconLabel::IconOnly:
        QQuickIconLabelPrivate::layout();
        return;
    case QQuickIconLabel::TextOnly: {
        if (label) {
            const QRectF textRect = alignedRect(mirrored, alignment, QSizeF(
                    qMin(label->implicitWidth(), availableWidth),
                    qMin(label->implicitHeight(), availableHeight)),
                QRectF(leftPadding, topPadding, availableWidth, availableHeight));
            label->setSize(textRect.size());
            label->setPosition(textRect.topLeft());
        }

        if (shortcutLabel)
            layoutShortcutLabel(availableWidth - (label->width() + spacing));
        break;
    } case QQuickIconLabel::TextUnderIcon: {
        // TextUnderIcon doesn't make sense for menu items, but we don't need to break
        // any existing behaviour, so while we don't support showing shortcuts for it, we can
        // continue doing what we were doing before.
        QQuickIconLabelPrivate::layout();
        return;
    }
    case QQuickIconLabel::TextBesideIcon:
    default:
        QSizeF iconSize(0, 0);
        QSizeF textSize(0, 0);
        QSizeF shortcutLabelSize(0, 0);
        if (image) {
            iconSize.setWidth(qMin(image->implicitWidth(), availableWidth));
            iconSize.setHeight(qMin(image->implicitHeight(), availableHeight));
        }
        qreal spacingBetweenIconAndLabel = 0;
        if (label) {
            if (!iconSize.isEmpty())
                spacingBetweenIconAndLabel = spacing;
            textSize.setWidth(qMin(label->implicitWidth(), availableWidth - iconSize.width()
                - spacingBetweenIconAndLabel));
            textSize.setHeight(qMin(label->implicitHeight(), availableHeight));
        }

        qreal spacingBetweenLabelAndShortcutLabel = 0;
        if (shortcutLabel) {
            if (!textSize.isEmpty())
                spacingBetweenLabelAndShortcutLabel = spacing;
            shortcutLabelSize.setWidth(qMin(shortcutLabel->implicitWidth(), availableWidth - iconSize.width()
                - spacingBetweenIconAndLabel - textSize.width() - spacingBetweenLabelAndShortcutLabel));
            shortcutLabelSize.setHeight(qMin(shortcutLabel->implicitHeight(), availableHeight));
        }

        /*!
            For IconLabel, the layout would look like this:

            +-------+-+--------------+
            |       | |              |
            | Icon  | | Text         |
            |       | |              |
            +-------+-+--------------+

            For us, it looks like this:

            +-------+-+--------------+-+------------+
            |       | |              | |            |
            | Icon  | | Text         | | Shortcut   |
            |       | |              | |            |
            +-------+-+--------------+-+------------+
        */
        const QRectF combinedImageAndLabelRect = alignedRect(mirrored, alignment, QSizeF(
                iconSize.width() + spacingBetweenIconAndLabel + textSize.width(),
                qMax(iconSize.height(), textSize.height())),
            QRectF(leftPadding, topPadding, availableWidth, availableHeight));
        if (image) {
            const QRectF iconRect = alignedRect(mirrored, Qt::AlignLeft | Qt::AlignVCenter, iconSize, combinedImageAndLabelRect);
            image->setSize(iconRect.size());
            image->snapPositionTo(iconRect.topLeft());
        }
        if (label) {
            const QRectF textRect = alignedRect(mirrored, Qt::AlignRight | Qt::AlignVCenter, textSize, combinedImageAndLabelRect);
            label->setSize(textRect.size());
            label->setPosition(textRect.topLeft());
        }
        if (shortcutLabel)
            layoutShortcutLabel(availableWidth - combinedImageAndLabelRect.width());
        break;
    }

    q->setBaselineOffset(label ? label->y() + label->baselineOffset() : 0);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 235, as _ZN30QQuickMenuItemIconLabelPrivate13itemDestroyedEP10QQuickItem
inline void QQuickMenuItemIconLabelPrivate::itemDestroyed(QQuickItem *item)
{
    QQuickIconLabelPrivate::itemDestroyed(item);

    if (item == shortcutLabel)
        shortcutLabel = nullptr;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 243, as _ZN30QQuickMenuItemIconLabelPrivate10textChangeEv
inline void QQuickMenuItemIconLabelPrivate::textChange()
{
    updateOrSyncShortcutLabel();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 248, as _ZN30QQuickMenuItemIconLabelPrivate13displayChangeEv
inline void QQuickMenuItemIconLabelPrivate::displayChange()
{
    updateOrSyncShortcutLabel();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 32, as _ZNK22QQuickIconLabelPrivate7hasIconEv
inline bool QQuickIconLabelPrivate::hasIcon() const
{
    return display != QQuickIconLabel::TextOnly && !icon.isEmpty();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 37, as _ZNK22QQuickIconLabelPrivate7hasTextEv
inline bool QQuickIconLabelPrivate::hasText() const
{
    return display != QQuickIconLabel::IconOnly && !text.isEmpty();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 192, as _ZN22QQuickIconLabelPrivate11alignedRectEb6QFlagsIN2Qt13AlignmentFlagEERK6QSizeFRK6QRectF
inline QRectF QQuickIconLabelPrivate::alignedRect(bool mirrored, Qt::Alignment alignment,
    const QSizeF &size, const QRectF &rectangle)
{
    alignment = QGuiApplicationPrivate::visualAlignment(mirrored ? Qt::RightToLeft : Qt::LeftToRight, alignment);
    qreal x = rectangle.x();
    qreal y = rectangle.y();
    const qreal w = size.width();
    const qreal h = size.height();
    if ((alignment & Qt::AlignVCenter) == Qt::AlignVCenter)
        y += rectangle.height() / 2 - h / 2;
    else if ((alignment & Qt::AlignBottom) == Qt::AlignBottom)
        y += rectangle.height() - h;
    if ((alignment & Qt::AlignRight) == Qt::AlignRight)
        x += rectangle.width() - w;
    else if ((alignment & Qt::AlignHCenter) == Qt::AlignHCenter)
        x += rectangle.width() / 2 - w / 2;
    return QRectF(x, y, w, h);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 211, as _ZN22QQuickIconLabelPrivate6layoutEv
inline void QQuickIconLabelPrivate::layout()
{
    Q_Q(QQuickIconLabel);
    if (!componentComplete)
        return;

    const qreal availableWidth = width - leftPadding - rightPadding;
    const qreal availableHeight = height - topPadding - bottomPadding;

    switch (display) {
    case QQuickIconLabel::IconOnly:
        if (image) {
            const QRectF iconRect = alignedRect(mirrored, alignment,
                                                QSizeF(qMin(image->implicitWidth(), availableWidth),
                                                       qMin(image->implicitHeight(), availableHeight)),
                                                QRectF(leftPadding, topPadding, availableWidth, availableHeight));
            image->setSize(iconRect.size());
            image->snapPositionTo(iconRect.topLeft());
        }
        break;
    case QQuickIconLabel::TextOnly:
        if (label) {
            const QRectF textRect = alignedRect(mirrored, alignment,
                                                QSizeF(qMin(label->implicitWidth(), availableWidth),
                                                       qMin(label->implicitHeight(), availableHeight)),
                                                QRectF(leftPadding, topPadding, availableWidth, availableHeight));
            label->setSize(textRect.size());
            label->setPosition(textRect.topLeft());
        }
        break;

    case QQuickIconLabel::TextUnderIcon: {
        // Work out the sizes first, as the positions depend on them.
        QSizeF iconSize;
        QSizeF textSize;
        if (image) {
            iconSize.setWidth(qMin(image->implicitWidth(), availableWidth));
            iconSize.setHeight(qMin(image->implicitHeight(), availableHeight));
        }
        qreal effectiveSpacing = 0;
        if (label) {
            if (!iconSize.isEmpty())
                effectiveSpacing = spacing;
            textSize.setWidth(qMin(label->implicitWidth(), availableWidth));
            textSize.setHeight(qMin(label->implicitHeight(), availableHeight - iconSize.height() - effectiveSpacing));
        }

        QRectF combinedRect = alignedRect(mirrored, alignment,
                                          QSizeF(qMax(iconSize.width(), textSize.width()),
                                                 iconSize.height() + effectiveSpacing + textSize.height()),
                                          QRectF(leftPadding, topPadding, availableWidth, availableHeight));
        if (image) {
            QRectF iconRect = alignedRect(mirrored, Qt::AlignHCenter | Qt::AlignTop, iconSize, combinedRect);
            image->setSize(iconRect.size());
            image->snapPositionTo(iconRect.topLeft());
        }
        if (label) {
            QRectF textRect = alignedRect(mirrored, Qt::AlignHCenter | Qt::AlignBottom, textSize, combinedRect);
            label->setSize(textRect.size());
            label->setPosition(textRect.topLeft());
        }
        break;
    }

    case QQuickIconLabel::TextBesideIcon:
    default:
        // Work out the sizes first, as the positions depend on them.
        QSizeF iconSize(0, 0);
        QSizeF textSize(0, 0);
        if (image) {
            iconSize.setWidth(qMin(image->implicitWidth(), availableWidth));
            iconSize.setHeight(qMin(image->implicitHeight(), availableHeight));
        }
        qreal effectiveSpacing = 0;
        if (label) {
            if (!iconSize.isEmpty())
                effectiveSpacing = spacing;
            textSize.setWidth(qMin(label->implicitWidth(), availableWidth - iconSize.width() - effectiveSpacing));
            textSize.setHeight(qMin(label->implicitHeight(), availableHeight));
        }

        const QRectF combinedRect = alignedRect(mirrored, alignment,
                                                QSizeF(iconSize.width() + effectiveSpacing + textSize.width(),
                                                       qMax(iconSize.height(), textSize.height())),
                                                QRectF(leftPadding, topPadding, availableWidth, availableHeight));
        if (image) {
            const QRectF iconRect = alignedRect(mirrored, Qt::AlignLeft | Qt::AlignVCenter, iconSize, combinedRect);
            image->setSize(iconRect.size());
            image->snapPositionTo(iconRect.topLeft());
        }
        if (label) {
            const QRectF textRect = alignedRect(mirrored, Qt::AlignRight | Qt::AlignVCenter, textSize, combinedRect);
            label->setSize(textRect.size());
            label->setPosition(textRect.topLeft());
        }
        break;
    }

    q->setBaselineOffset(label ? label->y() + label->baselineOffset() : 0);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 341, as _ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem
inline void QQuickIconLabelPrivate::itemDestroyed(QQuickItem *item)
{
    unwatchChanges(item);
    if (item == image)
        image = nullptr;
    else if (item == label)
        label = nullptr;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 18, as _ZNK30QQuickMenuItemIconLabelPrivate11hasShortcutEv
inline bool QQuickMenuItemIconLabelPrivate::hasShortcut() const
{
#if QT_CONFIG(shortcut)
    // See comment in layout() for why we don't support TextUnderIcon for shortcuts.
    return (display == QQuickIconLabel::TextOnly || display == QQuickIconLabel::TextBesideIcon)
        // Don't store this statically because we want to be able to auto-test it.
        && !QCoreApplication::testAttribute(Qt::AA_DontShowShortcutsInContextMenus)
        && !shortcut().isEmpty();
#else
    return false;
#endif
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 32, as _ZNK30QQuickMenuItemIconLabelPrivate8shortcutEv
#if QT_CONFIG(shortcut)
inline QKeySequence QQuickMenuItemIconLabelPrivate::shortcut() const
{
    return menuItem && menuItem->action() ? menuItem->action()->shortcut() : QKeySequence();
}
#endif  // QT_CONFIG(shortcut)

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 38, as _ZN30QQuickMenuItemIconLabelPrivate19createShortcutLabelEv
inline bool QQuickMenuItemIconLabelPrivate::createShortcutLabel()
{
    Q_Q(QQuickIconLabel);
    if (shortcutLabel)
        return false;

    shortcutLabel = new QQuickText(q);
    watchChanges(shortcutLabel);
    beginClass(shortcutLabel);
    shortcutLabel->setObjectName(QStringLiteral("shortcutLabel"));
    shortcutLabel->setFont(font);
    shortcutLabel->setColor(color);
    // We don't set elide because it shouldn't.
    shortcutLabel->setVAlign(QQuickText::AlignVCenter);
    shortcutLabel->setHAlign(QQuickText::AlignHCenter);
#if QT_CONFIG(shortcut)
    shortcutLabel->setText(shortcut().toString(QKeySequence::NativeText));
#endif
    if (componentComplete)
        completeComponent(shortcutLabel);
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 260, as _ZN30QQuickMenuItemIconLabelPrivate17syncShortcutLabelEv
inline void QQuickMenuItemIconLabelPrivate::syncShortcutLabel()
{
    if (!shortcutLabel)
        return;

#if QT_CONFIG(shortcut)
    shortcutLabel->setText(shortcut().toString(QKeySequence::NativeText));
#endif
}
//  -----------------------------------------------------------------------

//  A QQuickMenuItemIconLabelPrivate that Python can take functions over in. Every QQuickMenuItemIconLabelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall7)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall8)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickMenuItemIconLabelPrivateCall9)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall10)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickMenuItemIconLabelPrivateCall11)(const void *, int, int *);
typedef qreal (*CuteQQuickMenuItemIconLabelPrivateCall12)(const void *, int *);
typedef qreal (*CuteQQuickMenuItemIconLabelPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickMenuItemIconLabelPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickMenuItemIconLabelPrivateCall17)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickMenuItemIconLabelPrivateCall18)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickMenuItemIconLabelPrivateCall19)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall20)(const void *, bool, int *);
typedef void * (*CuteQQuickMenuItemIconLabelPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall23)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelPrivateCall24)(const void *, int, int *);
class CuteQQuickMenuItemIconLabelPrivate : public QQuickMenuItemIconLabelPrivate {
public:
  using QQuickMenuItemIconLabelPrivate::QQuickMenuItemIconLabelPrivate;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate6layoutEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate10textChangeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate13displayChangeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[18] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
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
    return false;
  }

  //  void QQuickMenuItemIconLabelPrivate::updateImplicitSize()
  void updateImplicitSize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall0 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabelPrivate::updateImplicitSize();
  }

  //  void QQuickMenuItemIconLabelPrivate::layout()
  void layout() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall1 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabelPrivate::layout();
  }

  //  void QQuickMenuItemIconLabelPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall2 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabelPrivate::itemDestroyed(item);
  }

  //  void QQuickMenuItemIconLabelPrivate::textChange()
  void textChange() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall3 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabelPrivate::textChange();
  }

  //  void QQuickMenuItemIconLabelPrivate::displayChange()
  void displayChange() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall4 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabelPrivate::displayChange();
  }

  //  void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall5 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::itemImplicitWidthChanged(a0);
  }

  //  void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall6 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall7 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall7>(taken[7]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall8 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall9 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall9>(taken[9]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall10 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall10>(taken[10]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall11 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall11>(taken[11]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall12 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall13 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall14 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall15 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall16 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall17 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall17>(taken[17]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall18 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall18>(taken[18]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall19 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall20 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall20>(taken[20]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall21 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall22 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall23 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelPrivateCall24 call = reinterpret_cast<CuteQQuickMenuItemIconLabelPrivateCall24>(taken[24]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickMenuItemIconLabel *QQuickMenuItemIconLabelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMenuItemIconLabel *ritual_ZN30QQuickMenuItemIconLabelPrivate6q_funcEv(
    QQuickMenuItemIconLabelPrivate *self) {
  return self->q_func();
}

//  const QQuickMenuItemIconLabel *QQuickMenuItemIconLabelPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMenuItemIconLabel *ritual_ZNK30QQuickMenuItemIconLabelPrivate6q_funcEv(
    const QQuickMenuItemIconLabelPrivate *self) {
  return self->q_func();
}

//  QQuickMenuItemIconLabelPrivate::~QQuickMenuItemIconLabelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivateD1Ev(
    QQuickMenuItemIconLabelPrivate *self) {
  delete self;
}

#if QT_CONFIG(shortcut)
//  bool QQuickMenuItemIconLabelPrivate::hasShortcut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickMenuItemIconLabelPrivate11hasShortcutEv(
    const QQuickMenuItemIconLabelPrivate *self) {
  return self->hasShortcut();
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  QKeySequence QQuickMenuItemIconLabelPrivate::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK30QQuickMenuItemIconLabelPrivate8shortcutEv(
    const QQuickMenuItemIconLabelPrivate *self) {
  return new QKeySequence(self->shortcut());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  bool QQuickMenuItemIconLabelPrivate::createShortcutLabel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QQuickMenuItemIconLabelPrivate19createShortcutLabelEv(
    QQuickMenuItemIconLabelPrivate *self) {
  return self->createShortcutLabel();
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QQuickMenuItemIconLabelPrivate::syncShortcutLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate17syncShortcutLabelEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->syncShortcutLabel();
}
#endif  // QT_CONFIG(shortcut)

//  void QQuickMenuItemIconLabelPrivate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate18updateImplicitSizeEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->updateImplicitSize();
}

//  void QQuickMenuItemIconLabelPrivate::layout()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate6layoutEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->layout();
}

//  void QQuickMenuItemIconLabelPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate13itemDestroyedEP10QQuickItem(
    QQuickMenuItemIconLabelPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickMenuItemIconLabelPrivate::textChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate10textChangeEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->textChange();
}

//  void QQuickMenuItemIconLabelPrivate::displayChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMenuItemIconLabelPrivate13displayChangeEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->displayChange();
}

//  a Python function taken by a CuteQQuickMenuItemIconLabelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenuItemIconLabelPrivate(
    QQuickMenuItemIconLabelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMenuItemIconLabelPrivate *>(self)->take(key, call);
}

#if QT_CONFIG(shortcut)
//  void QQuickMenuItemIconLabelPrivate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickMenuItemIconLabelPrivate18updateImplicitSizeEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->QQuickMenuItemIconLabelPrivate::updateImplicitSize();
}
#endif  // QT_CONFIG(shortcut)

//  void QQuickMenuItemIconLabelPrivate::layout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickMenuItemIconLabelPrivate6layoutEv(
    QQuickMenuItemIconLabelPrivate *self) {
  self->QQuickMenuItemIconLabelPrivate::layout();
}
