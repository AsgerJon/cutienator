//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qstylekitstyle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/qtlabsstylekitexports.h>
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#if 1
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#include <QtLabsStyleKit/qstylekitstyle.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qstylekitstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qstylekitstyle.h"
#include "qstylekitstyle_p.h"
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(scrollarea)
#  include <QtWidgets/qabstractscrollarea.h>
#endif
#if QT_CONFIG(itemviews)
#  include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(lineedit)
#  include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(pushbutton)
#  include <QtWidgets/qpushbutton.h>
#endif
#if QT_CONFIG(checkbox)
#  include <QtWidgets/qcheckbox.h>
#endif
#if QT_CONFIG(radiobutton)
#  include <QtWidgets/qradiobutton.h>
#endif
#if QT_CONFIG(combobox)
#  include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(slider)
#  include <QtWidgets/qslider.h>
#endif
#if QT_CONFIG(scrollbar)
#  include <QtWidgets/qscrollbar.h>
#endif
#if QT_CONFIG(spinbox)
#  include <QtWidgets/qspinbox.h>
#endif
#if QT_CONFIG(progressbar)
#  include <QtWidgets/qprogressbar.h>
#endif
#if QT_CONFIG(textedit)
#  include <QtWidgets/qtextedit.h>
#  include <QtWidgets/qplaintextedit.h>
#endif
#if QT_CONFIG(tabbar)
#  include <QtWidgets/qtabbar.h>
#endif
#if QT_CONFIG(tabwidget)
#  include <QtWidgets/qtabwidget.h>
#endif
#if QT_CONFIG(toolbar)
#  include <QtWidgets/qtoolbar.h>
#endif
#if QT_CONFIG(toolbutton)
#  include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(groupbox)
#  include <QtWidgets/qgroupbox.h>
#endif
#if QT_CONFIG(menu)
#  include <QtWidgets/qmenu.h>
#  include <QtWidgets/qmenubar.h>
#endif
#if QT_CONFIG(label)
#  include <QtWidgets/qlabel.h>
#endif
#include <QtWidgets/private/qwidget_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpainterstateguard.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qnumeric.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtLabsStyleKit/private/qqstylekit_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 565, as _ZN21QStyleKitStylePrivateC1Ev
inline QStyleKitStylePrivate::QStyleKitStylePrivate()
    : QCommonStylePrivate()
{
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 670, as _ZNK21QStyleKitStylePrivate14effectiveStyleEv
inline QQStyleKitStyle *QStyleKitStylePrivate::effectiveStyle() const
{
    return style ? style : defaultStyle;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 714, as _ZN21QStyleKitStylePrivate14unsetStyleFontEP7QWidget
inline void QStyleKitStylePrivate::unsetStyleFont(QWidget *widget)
{
    auto it = customFontWidgets.find(widget);
    if (it == customFontWidgets.end())
        return;

    auto customFont = std::move(*it);
    customFontWidgets.erase(it);
    widget->setFont(std::move(customFont).reverted(widget->font()));
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 725, as _ZN21QStyleKitStylePrivate12setStyleFontEP7QWidgetRK5QFont
inline void QStyleKitStylePrivate::setStyleFont(QWidget *widget, const QFont &styleFont)
{
    if (!effectiveStyle() || !widget)
        return;

    const auto styleMask = styleFont.resolveMask();
    auto it = customFontWidgets.find(widget);

    if (it == customFontWidgets.end()) {
        if (styleMask == 0)
            return;
        it = customFontWidgets.insert(widget, { QWidgetPrivate::get(widget)->localFont(), 0 });
        QObject::connect(widget, &QObject::destroyed, widget,
                         [this, widget]() { customFontWidgets.remove(widget); });
    }

    it->resolveMask = styleMask;

    const QFont &baseline = it->oldWidgetValue;
    QFont merged = styleFont.resolve(baseline);
    merged.setResolveMask(baseline.resolveMask() | styleMask);
    if (widget->font() != merged)
        widget->setFont(merged);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 770, as _ZN21QStyleKitStylePrivate17unsetStylePaletteEP7QWidget
inline void QStyleKitStylePrivate::unsetStylePalette(QWidget *widget)
{
    auto it = customPaletteWidgets.find(widget);
    if (it == customPaletteWidgets.end())
        return;

    auto customPalette = std::move(*it);
    customPaletteWidgets.erase(it);
    widget->setPalette(std::move(customPalette).reverted(widget->palette()));
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 781, as _ZNK21QStyleKitStylePrivate15setStylePaletteEP7QWidgetRK8QPalette
inline void QStyleKitStylePrivate::setStylePalette(QWidget *widget, const QPalette &stylePalette) const
{
    if (!effectiveStyle() || !widget)
        return;

    const quint64 styleMask = stylePalette.resolveMask();
    if (styleMask == 0)
        return;

    if (!customPaletteWidgets.contains(widget)) {
        customPaletteWidgets.insert(widget, { widget->palette(), 0 });
        QObject::connect(widget, &QObject::destroyed, widget,
                         [this, widget]() { customPaletteWidgets.remove(widget); });
    }

    customPaletteWidgets[widget].resolveMask |= styleMask;
    QPalette merged = stylePalette.resolve(widget->palette());
    merged.setResolveMask(widget->palette().resolveMask() | styleMask);
    widget->setPalette(merged);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 882, as _ZNK21QStyleKitStylePrivate19cleanupWidgetReaderEPK7QWidget
inline void QStyleKitStylePrivate::cleanupWidgetReader(const QWidget *widget) const
{
    if (auto *reader = widgetReaders.take(widget))
        reader->deleteLater();
    cleanupSubElements(widget);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 889, as _ZNK21QStyleKitStylePrivate17onWidgetDestroyedEP7QObject
inline void QStyleKitStylePrivate::onWidgetDestroyed(QObject *w) const
{
    cleanupWidgetReader(static_cast<QWidget *>(w));
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1233, as _ZNK21QStyleKitStylePrivate18ensureSharedReaderEv
inline QQStyleKitReader *QStyleKitStylePrivate::ensureSharedReader() const
{
    if (sharedReader)
        return sharedReader;

    Q_Q(const QStyleKitStyle);
    QQStyleKitStyle *effective = effectiveStyle();
    if (!effective)
        return nullptr;
    sharedReader = new QQStyleKitReader(const_cast<QStyleKitStyle *>(q));
    // Disable transitions since this reader is used for one-off metric reads in layout queries
    sharedReader->setTransitionsEnabled(false);
    sharedReader->setExplicitStyle(effective);
    sharedReader->setCompleted(true);
    return sharedReader;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1250, as _ZNK21QStyleKitStylePrivate22ensureSubElementReaderEv
inline QQStyleKitReader *QStyleKitStylePrivate::ensureSubElementReader() const
{
    if (subElementReader)
        return subElementReader;

    Q_Q(const QStyleKitStyle);
    QQStyleKitStyle *effective = effectiveStyle();
    if (!effective)
        return nullptr;
    subElementReader = new QQStyleKitReader(const_cast<QStyleKitStyle *>(q));
    // Disable transitions: this reader is retargeted across many sub-elements
    // per paint pass and must never animate between their states
    subElementReader->setTransitionsEnabled(false);
    subElementReader->setExplicitStyle(effective);
    subElementReader->setCompleted(true);
    return subElementReader;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1006, as _ZNK21QStyleKitStylePrivate18cleanupSubElementsEPK7QWidget
inline void QStyleKitStylePrivate::cleanupSubElements(const QWidget *widget) const
{
    for (auto it = subElementStates.begin(); it != subElementStates.end();) {
        if (it.key().widget == widget)
            it = subElementStates.erase(it);
        else
            ++it;
    }
    for (auto it = subElementAnimationReaders.begin(); it != subElementAnimationReaders.end();) {
        if (it.key().widget == widget) {
            it.value()->deleteLater();
            it = subElementAnimationReaders.erase(it);
        } else {
            ++it;
        }
    }
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1027, as _ZNK21QStyleKitStylePrivate19clearAllSubElementsEv
inline void QStyleKitStylePrivate::clearAllSubElements() const
{
    subElementStates.clear();
    for (QQStyleKitReader *reader : std::as_const(subElementAnimationReaders))
        reader->deleteLater();
    subElementAnimationReaders.clear();
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1039, as _ZNK21QStyleKitStylePrivate16resolvedStateForEN16QQStyleKitReader11ControlTypeE6QFlagsIN6QStyle9StateFlagEEPK7QWidget
inline QQSK::State QStyleKitStylePrivate::resolvedStateFor(QQStyleKitReader::ControlType type,
                                                    QStyle::State state,
                                                    const QWidget *widget) const
{
    QQSK::State flags;
    flags.setFlag(QQSK::StateFlag::Hovered, (state & QStyle::State_MouseOver));
    flags.setFlag(QQSK::StateFlag::Pressed, state & QStyle::State_Sunken);
    flags.setFlag(QQSK::StateFlag::Checked, state & QStyle::State_On);
    flags.setFlag(QQSK::StateFlag::Focused, state & QStyle::State_HasFocus);
    flags.setFlag(QQSK::StateFlag::Highlighted, state & QStyle::State_Selected);

    bool hasOrientation = false;
    switch (type) {
    case QQStyleKitReader::ProgressBar:
    case QQStyleKitReader::ScrollBar:
    case QQStyleKitReader::ScrollIndicator:
    case QQStyleKitReader::Slider:
    case QQStyleKitReader::ToolBar:
    case QQStyleKitReader::ToolSeparator:
        hasOrientation = true;
        break;
    default:
        break;
    }
    if (hasOrientation)
        flags.setFlag(QQSK::StateFlag::Vertical, !(state & QStyle::State_Horizontal));
    // Some widgets don't set State_Enabled in their
    // style option even when the widget is enabled.
    // Fall back to widget->isEnabled() in that case
    const bool enabled = (state & QStyle::State_Enabled) || (widget && widget->isEnabled());
    flags.setFlag(QQSK::StateFlag::Disabled, !enabled);

    // ComboBox uses QStyle::State_On to indicate the popup is open, which is
    // not a "checked" semantic.
    if (type == QQStyleKitReader::ControlType::ComboBox)
        flags.setFlag(QQSK::StateFlag::Checked, false);

    // Popup has no hover state in the Controls style
    if (type == QQStyleKitReader::ControlType::Popup)
        flags.setFlag(QQSK::StateFlag::Hovered, false);

    // QTabBar sets State_Selected (not State_On) on the current tab
    if (type == QQStyleKitReader::ControlType::TabButton) {
        flags.setFlag(QQSK::StateFlag::Checked, state & QStyle::State_Selected);
        flags.setFlag(QQSK::StateFlag::Highlighted, false);
    }

    return flags;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1314, as _ZN21QStyleKitStylePrivate17clearMetricsCacheEv
inline void QStyleKitStylePrivate::clearMetricsCache()
{
    metricsCache.clear();
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1403, as _ZNK21QStyleKitStylePrivate22drawStyledItemContentsEPK28QQStyleKitDelegatePropertiesRK6QRectFP8QPainter
inline void QStyleKitStylePrivate::drawStyledItemContents(const QQStyleKitDelegateProperties *props,
                                                   const QRectF &rect, QPainter *painter) const
{
    if (!props || !props->visible() || props->opacity() <= 0 || !rect.isValid())
        return;

    QPainterStateGuard stateGuard(painter);
    painter->setRenderHint(QPainter::Antialiasing, true);
    if (props->clip())
        painter->setClipping(true);

    // opacity
    const auto opacity = props->opacity();

    // border
    const auto *border = props->border();
    auto borderWidth = 0;
    auto inset = 0.0;
    QColor borderColor;
    if (border) {
        borderWidth = border->width();
        borderColor = border->color();
        inset = borderWidth / 2.0;
    }
    if (borderWidth > 0 && borderColor.isValid() && borderColor.alpha() > 0) {
        QPen pen(borderColor, borderWidth);
        painter->setPen(pen);
    } else {
        painter->setPen(Qt::NoPen);
    }

    // radius
    // TODO: support different radius for each corner
    const qreal minDimension = qMin(rect.width(), rect.height());
    const qreal xRadius = qMax(0.0, qMin(props->topLeftRadius() - inset, minDimension / 2.0));
    const qreal yRadius = qMax(0.0, qMin(props->bottomLeftRadius() - inset, minDimension / 2.0));

    QRectF adjustedRect = rect.adjusted(inset, inset, -inset, -inset);

    // gradients/color
    // TODO: support palette roles for colors and gradients
    QColor color = props->color();
    QBrush colorBrush(color);
    painter->setBrush(colorBrush);
    if (color.isValid()) {
        painter->setOpacity(opacity);
        painter->drawRoundedRect(adjustedRect, xRadius, yRadius, Qt::AbsoluteSize);
    }
    if (QQuickGradient *gradient = props->gradient()) {
        QLinearGradient linearGradient(rect.topLeft(), rect.bottomLeft());
        QQmlListProperty<QQuickGradientStop> stops = gradient->stops();
        const int stopCount = stops.count(&stops);
        for (int i = 0; i < stopCount; i++) {
            QQuickGradientStop *stop = static_cast<QQuickGradientStop *>(stops.at(&stops, i));
            linearGradient.setColorAt(stop->position(), stop->color());
        }
        QBrush gradientBrush(linearGradient);
        painter->setBrush(gradientBrush);
        painter->setOpacity(opacity);
        painter->drawRoundedRect(adjustedRect, xRadius, yRadius, Qt::AbsoluteSize);
    }

    // image
    drawStyledItemImage(props->image(), adjustedRect, opacity, painter);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1469, as _ZNK21QStyleKitStylePrivate19drawStyledItemImageEPK25QQStyleKitImagePropertiesRK6QRectFdP8QPainter
inline void QStyleKitStylePrivate::drawStyledItemImage(const QQStyleKitImageProperties *image,
                                                const QRectF &rect, qreal opacity,
                                                QPainter *painter) const
{
    if (!image || image->source().isEmpty() || image->color().alpha() <= 0)
        return;

    QString imageSource = image->source().toString();
    if (imageSource.startsWith(QLatin1String("qrc:/")))
        imageSource = imageSource.mid(3);
    QUrl imageUrl(imageSource);
    QString imagePath = imageUrl.isLocalFile() ? imageUrl.toLocalFile() : imageSource;
    QPixmap pixmap(imagePath);
    if (pixmap.isNull())
        return;

    if (image->color().isValid()) {
        QImage coloredImage = pixmap.toImage();
        QPainter imagePainter(&coloredImage);
        imagePainter.setCompositionMode(QPainter::CompositionMode_SourceIn);
        imagePainter.fillRect(coloredImage.rect(), image->color());
        imagePainter.end();
        pixmap = QPixmap::fromImage(coloredImage);
    }
    painter->setOpacity(opacity);
    const QSizeF pixmapSize = pixmap.deviceIndependentSize();

    switch (image->fillMode()) {
    case QQuickImage::PreserveAspectFit: {
        const QSize scaled = pixmapSize.scaled(rect.size(), Qt::KeepAspectRatio).toSize();
        const QPointF topLeft(rect.x() + (rect.width() - scaled.width()) / 2.0,
                              rect.y() + (rect.height() - scaled.height()) / 2.0);
        painter->drawPixmap(QRectF(topLeft, scaled), pixmap, QRectF(QPointF(0, 0), pixmapSize));
        break;
    }
    case QQuickImage::PreserveAspectCrop: {
        const QSize scaled = pixmapSize
            .scaled(rect.size(), Qt::KeepAspectRatioByExpanding)
            .toSize();
        const QPointF topLeft(rect.x() + (rect.width() - scaled.width()) / 2.0,
                              rect.y() + (rect.height() - scaled.height()) / 2.0);
        QPainterStateGuard stateGuard(painter);
        painter->setClipRect(rect);
        painter->drawPixmap(QRectF(topLeft, scaled), pixmap, QRectF(QPointF(0, 0), pixmapSize));
        break;
    }
    // TODO: Support remaining fill modes
    case QQuickImage::Stretch:
    default:
        painter->drawPixmap(rect, pixmap, QRectF(QPointF(0, 0), pixmapSize));
        break;
    }
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1523, as _ZNK21QStyleKitStylePrivate25getAlignedRectInContainerERK5QRectRK5QSizejRK8QMarginsS8_
inline QRect QStyleKitStylePrivate::getAlignedRectInContainer(const QRect &container, const QSize &size,
                                                       uint alignment, const QMargins &padding,
                                                       const QMargins &margins) const
{
    QRect r(QPoint(0, 0), size);

    if (alignment & Qt::AlignLeft)
        r.moveLeft(container.x() + padding.left() + margins.left());
    else if (alignment & Qt::AlignHCenter)
        r.moveLeft(container.x() + (container.width() - size.width()) / 2);
    else // AlignRight
        r.moveLeft(container.right() + 1 - padding.right() - margins.right() - size.width());

    if (alignment & Qt::AlignTop)
        r.moveTop(container.y() + padding.top() + margins.top());
    else if (alignment & Qt::AlignVCenter)
        r.moveTop(container.y() + (container.height() - size.height()) / 2);
    else // AlignBottom
        r.moveTop(container.bottom() + 1 - padding.bottom() - margins.bottom() - size.height());

    return r;
}
//  -----------------------------------------------------------------------

//  QStyleKitStyle *QStyleKitStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QStyleKitStyle *ritual_ZN21QStyleKitStylePrivate6q_funcEv(
    QStyleKitStylePrivate *self) {
  return self->q_func();
}

//  const QStyleKitStyle *QStyleKitStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStyleKitStyle *ritual_ZNK21QStyleKitStylePrivate6q_funcEv(
    const QStyleKitStylePrivate *self) {
  return self->q_func();
}

//  QStyleKitStylePrivate::QStyleKitStylePrivate()
extern "C" Q_DECL_EXPORT
QStyleKitStylePrivate *ritual_ZN21QStyleKitStylePrivateC1Ev() {
  return new QStyleKitStylePrivate();
}

//  QQStyleKitStyle *QStyleKitStylePrivate::effectiveStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK21QStyleKitStylePrivate14effectiveStyleEv(
    const QStyleKitStylePrivate *self) {
  return self->effectiveStyle();
}

//  void QStyleKitStylePrivate::unsetStyleFont(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleKitStylePrivate14unsetStyleFontEP7QWidget(
    QStyleKitStylePrivate *self,
    QWidget *widget) {
  self->unsetStyleFont(widget);
}

//  void QStyleKitStylePrivate::setStyleFont(QWidget *widget, const QFont
//      &styleFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleKitStylePrivate12setStyleFontEP7QWidgetRK5QFont(
    QStyleKitStylePrivate *self,
    QWidget *widget,
    const QFont *styleFont) {
  self->setStyleFont(widget, *styleFont);
}

//  void QStyleKitStylePrivate::unsetStylePalette(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleKitStylePrivate17unsetStylePaletteEP7QWidget(
    QStyleKitStylePrivate *self,
    QWidget *widget) {
  self->unsetStylePalette(widget);
}

//  void QStyleKitStylePrivate::setStylePalette(QWidget *widget, const
//      QPalette &stylePalette) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate15setStylePaletteEP7QWidgetRK8QPalette(
    const QStyleKitStylePrivate *self,
    QWidget *widget,
    const QPalette *stylePalette) {
  self->setStylePalette(widget, *stylePalette);
}

//  void QStyleKitStylePrivate::cleanupWidgetReader(const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate19cleanupWidgetReaderEPK7QWidget(
    const QStyleKitStylePrivate *self,
    const QWidget *widget) {
  self->cleanupWidgetReader(widget);
}

//  void QStyleKitStylePrivate::onWidgetDestroyed(QObject *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate17onWidgetDestroyedEP7QObject(
    const QStyleKitStylePrivate *self,
    QObject *w) {
  self->onWidgetDestroyed(w);
}

//  QQStyleKitReader *QStyleKitStylePrivate::ensureSharedReader() const
extern "C" Q_DECL_EXPORT
QQStyleKitReader *ritual_ZNK21QStyleKitStylePrivate18ensureSharedReaderEv(
    const QStyleKitStylePrivate *self) {
  return self->ensureSharedReader();
}

//  QQStyleKitReader *QStyleKitStylePrivate::ensureSubElementReader() const
extern "C" Q_DECL_EXPORT
QQStyleKitReader *ritual_ZNK21QStyleKitStylePrivate22ensureSubElementReaderEv(
    const QStyleKitStylePrivate *self) {
  return self->ensureSubElementReader();
}

//  void QStyleKitStylePrivate::cleanupSubElements(const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate18cleanupSubElementsEPK7QWidget(
    const QStyleKitStylePrivate *self,
    const QWidget *widget) {
  self->cleanupSubElements(widget);
}

//  void QStyleKitStylePrivate::clearAllSubElements() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate19clearAllSubElementsEv(
    const QStyleKitStylePrivate *self) {
  self->clearAllSubElements();
}

//  QQSK::State
//      QStyleKitStylePrivate::resolvedStateFor(QQStyleKitReader::ControlType
//      type, QStyle::State state, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QStyleKitStylePrivate16resolvedStateForEN16QQStyleKitReader11ControlTypeE6QFlagsIN6QStyle9StateFlagEEPK7QWidget(
    const QStyleKitStylePrivate *self,
    QQStyleKitReader::ControlType type,
    int state,
    const QWidget *widget) {
  return static_cast<int>(
      self->resolvedStateFor(
          type,
          QFlags<QStyle::StateFlag>::fromInt(state),
          widget).toInt());
}

//  void QStyleKitStylePrivate::clearMetricsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleKitStylePrivate17clearMetricsCacheEv(
    QStyleKitStylePrivate *self) {
  self->clearMetricsCache();
}

//  void QStyleKitStylePrivate::drawStyledItemContents(const
//      QQStyleKitDelegateProperties *a0, const QRectF &rect, QPainter *p)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate22drawStyledItemContentsEPK28QQStyleKitDelegatePropertiesRK6QRectFP8QPainter(
    const QStyleKitStylePrivate *self,
    const QQStyleKitDelegateProperties *a0,
    const QRectF *rect,
    QPainter *p) {
  self->drawStyledItemContents(a0, *rect, p);
}

//  void QStyleKitStylePrivate::drawStyledItemImage(const
//      QQStyleKitImageProperties *image, const QRectF &rect, qreal opacity,
//      QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QStyleKitStylePrivate19drawStyledItemImageEPK25QQStyleKitImagePropertiesRK6QRectFdP8QPainter(
    const QStyleKitStylePrivate *self,
    const QQStyleKitImageProperties *image,
    const QRectF *rect,
    qreal opacity,
    QPainter *p) {
  self->drawStyledItemImage(image, *rect, opacity, p);
}

//  QRect QStyleKitStylePrivate::getAlignedRectInContainer(const QRect
//      &container, const QSize &indicatorSize, uint alignment, const
//      QMargins &padding, const QMargins &indicatorMargins) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK21QStyleKitStylePrivate25getAlignedRectInContainerERK5QRectRK5QSizejRK8QMarginsS8_(
    const QStyleKitStylePrivate *self,
    const QRect *container,
    const QSize *indicatorSize,
    uint alignment,
    const QMargins *padding,
    const QMargins *indicatorMargins) {
  return new QRect(
      self->getAlignedRectInContainer(
          *container,
          *indicatorSize,
          alignment,
          *padding,
          *indicatorMargins));
}

#endif  // 1
