//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
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

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 323, as _ZN22QQuickIconLabelPrivate14unwatchChangesEP10QQuickItem
inline void QQuickIconLabelPrivate::unwatchChanges(QQuickItem* item)
{
    QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);
    itemPrivate->removeItemChangeListener(this, itemChangeTypes);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 172, as _ZN22QQuickIconLabelPrivate18updateImplicitSizeEv
inline void QQuickIconLabelPrivate::updateImplicitSize()
{
    Q_Q(QQuickIconLabel);
    const bool showIcon = image && hasIcon();
    const bool showText = label && hasText();
    const qreal horizontalPadding = leftPadding + rightPadding;
    const qreal verticalPadding = topPadding + bottomPadding;
    const qreal iconImplicitWidth = showIcon ? image->implicitWidth() : 0;
    const qreal iconImplicitHeight = showIcon ? image->implicitHeight() : 0;
    const qreal textImplicitWidth = showText ? label->implicitWidth() : 0;
    const qreal textImplicitHeight = showText ? label->implicitHeight() : 0;
    const qreal effectiveSpacing = showText && showIcon && image->implicitWidth() > 0 ? spacing : 0;
    const qreal implicitWidth = display == QQuickIconLabel::TextBesideIcon ? iconImplicitWidth + textImplicitWidth + effectiveSpacing
                                                                           : qMax(iconImplicitWidth, textImplicitWidth);
    const qreal implicitHeight = display == QQuickIconLabel::TextUnderIcon ? iconImplicitHeight + textImplicitHeight + effectiveSpacing
                                                                           : qMax(iconImplicitHeight, textImplicitHeight);
    q->setImplicitSize(implicitWidth + horizontalPadding, implicitHeight + verticalPadding);
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

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 329, as _ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *)
{
    updateImplicitSize();
    layout();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 335, as _ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem *)
{
    updateImplicitSize();
    layout();
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

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 350, as _ZN22QQuickIconLabelPrivate10textChangeEv
inline void QQuickIconLabelPrivate::textChange()
{
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 354, as _ZN22QQuickIconLabelPrivate13displayChangeEv
inline void QQuickIconLabelPrivate::displayChange()
{
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

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 42, as _ZN22QQuickIconLabelPrivate11createImageEv
inline bool QQuickIconLabelPrivate::createImage()
{
    Q_Q(QQuickIconLabel);
    if (image)
        return false;

    image = new QQuickIconImage(q);
    watchChanges(image);
    beginClass(image);
    image->setObjectName(QStringLiteral("image"));
    image->setName(icon.name());
    image->setSource(icon.resolvedSource());
    image->setSourceSize(QSize(icon.width(), icon.height()));
    const bool explicitColor = QQuickIconPrivate::isResolved(icon, QQuickIconPrivate::ColorResolved);
    image->setColor(explicitColor ? icon.color() : defaultIconColor);
    image->setCache(icon.cache());
    QQmlEngine::setContextForObject(image, qmlContext(q));
    if (componentComplete)
        completeComponent(image);
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 64, as _ZN22QQuickIconLabelPrivate12destroyImageEv
inline bool QQuickIconLabelPrivate::destroyImage()
{
    if (!image)
        return false;

    unwatchChanges(image);
    delete image;
    image = nullptr;
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 75, as _ZN22QQuickIconLabelPrivate11updateImageEv
inline bool QQuickIconLabelPrivate::updateImage()
{
    if (!hasIcon())
        return destroyImage();
    return createImage();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 82, as _ZN22QQuickIconLabelPrivate9syncImageEv
inline void QQuickIconLabelPrivate::syncImage()
{
    if (!image || icon.isEmpty())
        return;

    image->setName(icon.name());
    image->setSource(icon.resolvedSource());
    image->setSourceSize(QSize(icon.width(), icon.height()));
    const bool explicitColor = QQuickIconPrivate::isResolved(icon, QQuickIconPrivate::ColorResolved);
    image->setColor(explicitColor ? icon.color() : defaultIconColor);
    image->setCache(icon.cache());
    const int valign = alignment & Qt::AlignVertical_Mask;
    image->setVerticalAlignment(static_cast<QQuickImage::VAlignment>(valign));
    const int halign = alignment & Qt::AlignHorizontal_Mask;
    image->setHorizontalAlignment(static_cast<QQuickImage::HAlignment>(halign));
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 99, as _ZN22QQuickIconLabelPrivate17updateOrSyncImageEv
inline void QQuickIconLabelPrivate::updateOrSyncImage()
{
    if (updateImage()) {
        if (componentComplete) {
            updateImplicitSize();
            layout();
        }
    } else {
        syncImage();
    }
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 111, as _ZN22QQuickIconLabelPrivate11createLabelEv
inline bool QQuickIconLabelPrivate::createLabel()
{
    Q_Q(QQuickIconLabel);
    if (label)
        return false;

    label = new QQuickMnemonicLabel(q);
    watchChanges(label);
    beginClass(label);
    label->setObjectName(QStringLiteral("label"));
    label->setFont(font);
    label->setColor(color);
    label->setElideMode(QQuickText::ElideRight);
    const int valign = alignment & Qt::AlignVertical_Mask;
    label->setVAlign(static_cast<QQuickText::VAlignment>(valign));
    const int halign = alignment & Qt::AlignHorizontal_Mask;
    label->setHAlign(static_cast<QQuickText::HAlignment>(halign));
    label->setText(text);
    if (componentComplete)
        completeComponent(label);
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 134, as _ZN22QQuickIconLabelPrivate12destroyLabelEv
inline bool QQuickIconLabelPrivate::destroyLabel()
{
    if (!label)
        return false;

    unwatchChanges(label);
    delete label;
    label = nullptr;
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 145, as _ZN22QQuickIconLabelPrivate11updateLabelEv
inline bool QQuickIconLabelPrivate::updateLabel()
{
    if (!hasText())
        return destroyLabel();
    return createLabel();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 152, as _ZN22QQuickIconLabelPrivate9syncLabelEv
inline void QQuickIconLabelPrivate::syncLabel()
{
    if (!label)
        return;

    label->setText(text);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 160, as _ZN22QQuickIconLabelPrivate17updateOrSyncLabelEv
inline void QQuickIconLabelPrivate::updateOrSyncLabel()
{
    if (updateLabel()) {
        if (componentComplete) {
            updateImplicitSize();
            layout();
        }
    } else {
        syncLabel();
    }
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 317, as _ZN22QQuickIconLabelPrivate12watchChangesEP10QQuickItem
inline void QQuickIconLabelPrivate::watchChanges(QQuickItem *item)
{
    QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);
    itemPrivate->addItemChangeListener(this, itemChangeTypes);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 18, as _ZN22QQuickIconLabelPrivate10beginClassEP10QQuickItem
inline void QQuickIconLabelPrivate::beginClass(QQuickItem *item)
{
    if (QQmlParserStatus *parserStatus = qobject_cast<QQmlParserStatus *>(item))
        parserStatus->classBegin();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 24, as _ZN22QQuickIconLabelPrivate17completeComponentEP10QQuickItem
inline void QQuickIconLabelPrivate::completeComponent(QQuickItem *item)
{
    if (QQmlParserStatus *parserStatus = qobject_cast<QQmlParserStatus *>(item))
        parserStatus->componentComplete();
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
//  -----------------------------------------------------------------------

//  A QQuickIconLabelPrivate that Python can take functions over in. Every QQuickIconLabelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickIconLabelPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall7)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall8)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickIconLabelPrivateCall9)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall10)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickIconLabelPrivateCall11)(const void *, int, int *);
typedef qreal (*CuteQQuickIconLabelPrivateCall12)(const void *, int *);
typedef qreal (*CuteQQuickIconLabelPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickIconLabelPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickIconLabelPrivateCall17)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickIconLabelPrivateCall18)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickIconLabelPrivateCall19)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickIconLabelPrivateCall20)(const void *, bool, int *);
typedef void * (*CuteQQuickIconLabelPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall23)(const void *, int *);
typedef void (*CuteQQuickIconLabelPrivateCall24)(const void *, int, int *);
class CuteQQuickIconLabelPrivate : public QQuickIconLabelPrivate {
public:
  using QQuickIconLabelPrivate::QQuickIconLabelPrivate;
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
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate10textChangeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickIconLabelPrivate13displayChangeEv")) {
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

  //  void QQuickIconLabelPrivate::updateImplicitSize()
  void updateImplicitSize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall0 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::updateImplicitSize();
  }

  //  void QQuickIconLabelPrivate::layout()
  void layout() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall1 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::layout();
  }

  //  void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall2 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::itemImplicitWidthChanged(a0);
  }

  //  void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall3 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::itemImplicitHeightChanged(a0);
  }

  //  void QQuickIconLabelPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall4 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::itemDestroyed(item);
  }

  //  void QQuickIconLabelPrivate::textChange()
  void textChange() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall5 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::textChange();
  }

  //  void QQuickIconLabelPrivate::displayChange()
  void displayChange() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall6 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickIconLabelPrivate::displayChange();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall7 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall7>(taken[7]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall8 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall8>(taken[8]);
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
      CuteQQuickIconLabelPrivateCall9 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall9>(taken[9]);
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
      CuteQQuickIconLabelPrivateCall10 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall10>(taken[10]);
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
      CuteQQuickIconLabelPrivateCall11 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall11>(taken[11]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall12 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall13 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall14 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall15 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall15>(taken[15]);
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
      CuteQQuickIconLabelPrivateCall16 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall16>(taken[16]);
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
      CuteQQuickIconLabelPrivateCall17 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall17>(taken[17]);
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
      CuteQQuickIconLabelPrivateCall18 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall18>(taken[18]);
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
      CuteQQuickIconLabelPrivateCall19 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall19>(taken[19]);
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
      CuteQQuickIconLabelPrivateCall20 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall20>(taken[20]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall21 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall22 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall23 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickIconLabelPrivateCall24 call = reinterpret_cast<CuteQQuickIconLabelPrivateCall24>(taken[24]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickIconLabel *QQuickIconLabelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickIconLabel *ritual_ZN22QQuickIconLabelPrivate6q_funcEv(
    QQuickIconLabelPrivate *self) {
  return self->q_func();
}

//  const QQuickIconLabel *QQuickIconLabelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickIconLabel *ritual_ZNK22QQuickIconLabelPrivate6q_funcEv(
    const QQuickIconLabelPrivate *self) {
  return self->q_func();
}

//  QQuickIconLabelPrivate::~QQuickIconLabelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivateD1Ev(QQuickIconLabelPrivate *self) {
  delete self;
}

//  bool QQuickIconLabelPrivate::hasIcon() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickIconLabelPrivate7hasIconEv(
    const QQuickIconLabelPrivate *self) {
  return self->hasIcon();
}

//  bool QQuickIconLabelPrivate::hasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickIconLabelPrivate7hasTextEv(
    const QQuickIconLabelPrivate *self) {
  return self->hasText();
}

//  bool QQuickIconLabelPrivate::createImage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate11createImageEv(
    QQuickIconLabelPrivate *self) {
  return self->createImage();
}

//  bool QQuickIconLabelPrivate::destroyImage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate12destroyImageEv(
    QQuickIconLabelPrivate *self) {
  return self->destroyImage();
}

//  bool QQuickIconLabelPrivate::updateImage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate11updateImageEv(
    QQuickIconLabelPrivate *self) {
  return self->updateImage();
}

//  void QQuickIconLabelPrivate::syncImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate9syncImageEv(
    QQuickIconLabelPrivate *self) {
  self->syncImage();
}

//  void QQuickIconLabelPrivate::updateOrSyncImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate17updateOrSyncImageEv(
    QQuickIconLabelPrivate *self) {
  self->updateOrSyncImage();
}

//  bool QQuickIconLabelPrivate::createLabel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate11createLabelEv(
    QQuickIconLabelPrivate *self) {
  return self->createLabel();
}

//  bool QQuickIconLabelPrivate::destroyLabel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate12destroyLabelEv(
    QQuickIconLabelPrivate *self) {
  return self->destroyLabel();
}

//  bool QQuickIconLabelPrivate::updateLabel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconLabelPrivate11updateLabelEv(
    QQuickIconLabelPrivate *self) {
  return self->updateLabel();
}

//  void QQuickIconLabelPrivate::syncLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate9syncLabelEv(
    QQuickIconLabelPrivate *self) {
  self->syncLabel();
}

//  void QQuickIconLabelPrivate::updateOrSyncLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate17updateOrSyncLabelEv(
    QQuickIconLabelPrivate *self) {
  self->updateOrSyncLabel();
}

//  void QQuickIconLabelPrivate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv(
    QQuickIconLabelPrivate *self) {
  self->updateImplicitSize();
}

//  void QQuickIconLabelPrivate::layout()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate6layoutEv(
    QQuickIconLabelPrivate *self) {
  self->layout();
}

//  void QQuickIconLabelPrivate::watchChanges(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate12watchChangesEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *item) {
  self->watchChanges(item);
}

//  void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *a0) {
  self->itemImplicitWidthChanged(a0);
}

//  void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *a0) {
  self->itemImplicitHeightChanged(a0);
}

//  void QQuickIconLabelPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickIconLabelPrivate::textChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate10textChangeEv(
    QQuickIconLabelPrivate *self) {
  self->textChange();
}

//  void QQuickIconLabelPrivate::displayChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate13displayChangeEv(
    QQuickIconLabelPrivate *self) {
  self->displayChange();
}

//  void QQuickIconLabelPrivate::beginClass(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate10beginClassEP10QQuickItem(
    QQuickItem *item) {
  QQuickIconLabelPrivate::beginClass(item);
}

//  void QQuickIconLabelPrivate::completeComponent(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconLabelPrivate17completeComponentEP10QQuickItem(
    QQuickItem *item) {
  QQuickIconLabelPrivate::completeComponent(item);
}

//  QRectF QQuickIconLabelPrivate::alignedRect(bool mirrored, Qt::Alignment
//      alignment, const QSizeF &size, const QRectF &rectangle)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN22QQuickIconLabelPrivate11alignedRectEb6QFlagsIN2Qt13AlignmentFlagEERK6QSizeFRK6QRectF(
    bool mirrored,
    int alignment,
    const QSizeF *size,
    const QRectF *rectangle) {
  return new QRectF(
      QQuickIconLabelPrivate::alignedRect(
          mirrored,
          QFlags<Qt::AlignmentFlag>::fromInt(alignment),
          *size,
          *rectangle));
}

//  a Python function taken by a CuteQQuickIconLabelPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickIconLabelPrivate(
    QQuickIconLabelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickIconLabelPrivate *>(self)->take(key, call);
}

//  void QQuickIconLabelPrivate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv(
    QQuickIconLabelPrivate *self) {
  self->QQuickIconLabelPrivate::updateImplicitSize();
}

//  void QQuickIconLabelPrivate::layout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate6layoutEv(
    QQuickIconLabelPrivate *self) {
  self->QQuickIconLabelPrivate::layout();
}

//  void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *a0) {
  self->QQuickIconLabelPrivate::itemImplicitWidthChanged(a0);
}

//  void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *a0) {
  self->QQuickIconLabelPrivate::itemImplicitHeightChanged(a0);
}

//  void QQuickIconLabelPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem(
    QQuickIconLabelPrivate *self,
    QQuickItem *item) {
  self->QQuickIconLabelPrivate::itemDestroyed(item);
}

//  void QQuickIconLabelPrivate::textChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate10textChangeEv(
    QQuickIconLabelPrivate *self) {
  self->QQuickIconLabelPrivate::textChange();
}

//  void QQuickIconLabelPrivate::displayChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickIconLabelPrivate13displayChangeEv(
    QQuickIconLabelPrivate *self) {
  self->QQuickIconLabelPrivate::displayChange();
}
