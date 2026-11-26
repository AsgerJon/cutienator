//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qstylekitstyle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/qtlabsstylekitexports.h>
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#if 1
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#if 1
#include <QtLabsStyleKit/QtLabsStyleKit>
#include <QtLabsStyleKit/qstylekitstyle.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qstylekitstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/qstylekitstyle.h>
#include <QtLabsStyleKit/private/qstylekitstyle_p.h>
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
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitdebug_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 432, as local:qstylekitstyle.cpp:paintTarget
static QWidget *paintTarget(const QWidget *widget)
{
#if QT_CONFIG(scrollarea)
    if (const auto *area = qobject_cast<const QAbstractScrollArea *>(widget))
        return area->viewport();
#endif
    return const_cast<QWidget *>(widget);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 443, as local:qstylekitstyle.cpp:isSelfPaintingWidget
static bool isSelfPaintingWidget(const QWidget *widget)
{
    return false
#if QT_CONFIG(label)
        || qobject_cast<const QLabel *>(widget)
#endif
#if QT_CONFIG(textedit)
        || qobject_cast<const QTextEdit *>(widget)
        || qobject_cast<const QPlainTextEdit *>(widget)
#endif
#if QT_CONFIG(lineedit)
        || qobject_cast<const QLineEdit *>(widget)
#endif
        ;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 476, as local:qstylekitstyle.cpp:resolvedAlignment
static uint resolvedAlignment(uint raw, Qt::Alignment hDefault, Qt::Alignment vDefault)
{
    uint result = 0;
    const uint h = raw & Qt::AlignHorizontal_Mask;
    const uint v = raw & Qt::AlignVertical_Mask;
    result |= h ? h : uint(hDefault);
    result |= v ? v : uint(vDefault);
    return result;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 486, as local:qstylekitstyle.cpp:resolvedWidth
static qreal resolvedWidth(const QQStyleKitDelegateProperties *element, qreal availableW)
{
    return qMax(0.0, element->fillWidth() ? availableW : element->width());
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 491, as local:qstylekitstyle.cpp:resolvedHeight
static qreal resolvedHeight(const QQStyleKitDelegateProperties *element, qreal availableH)
{
    return qMax(0.0, element->fillHeight() ? availableH : element->height());
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 496, as local:qstylekitstyle.cpp:elementMargins
static QMargins elementMargins(const QQStyleKitDelegateProperties *element)
{
    using QtPrivate::qSaturateRound;
    return QMargins(qSaturateRound(element->leftMargin()),
                    qSaturateRound(element->topMargin()),
                    qSaturateRound(element->rightMargin()),
                    qSaturateRound(element->bottomMargin()));
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 509, as local:qstylekitstyle.cpp:applyDelegateTransform
static bool applyDelegateTransform(QPainter *painter,
                                   const QQStyleKitDelegateProperties *element,
                                   const QRectF &box)
{
    if (!element)
        return false;

    const qreal scale = element->scale();
    if (qFuzzyIsNull(scale))
        return false;

    const qreal rotation = element->rotation();
    if (qFuzzyIsNull(rotation) && qFuzzyCompare(scale, 1.0))
        return true;

    const QPointF center = box.center();
    painter->translate(center);
    if (!qFuzzyIsNull(rotation))
        painter->rotate(rotation);
    if (!qFuzzyCompare(scale, 1.0))
        painter->scale(scale, scale);
    painter->translate(-center);
    return true;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 535, as local:qstylekitstyle.cpp:containerWidget
static const QWidget *containerWidget(const QWidget *w)
{
#if QT_CONFIG(lineedit)
    if (qobject_cast<const QLineEdit *>(w)) {
        // if the QLineEdit is an embeddedWidget, we need the real widget
        QWidget *parent = w->parentWidget();
        if (false
#  if QT_CONFIG(combobox)
            || qobject_cast<const QComboBox *>(parent)
#  endif
#  if QT_CONFIG(spinbox)
            || qobject_cast<const QAbstractSpinBox *>(parent)
#  endif
        ) {
            return parent;
        }
    }
#endif

#if QT_CONFIG(scrollarea)
    if (const QAbstractScrollArea *sa =
            qobject_cast<const QAbstractScrollArea *>(w->parentWidget())) {
        if (sa->viewport() == w)
            return w->parentWidget();
    }
#endif

    return w;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 570, as local:qstylekitstyle.cpp:urlFromStylePath
static QUrl urlFromStylePath(const QString &filePath)
{
    return filePath.startsWith(QLatin1Char(':')) ? QUrl(QLatin1String("qrc") + filePath)
                                                 : QUrl::fromLocalFile(filePath);
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 1546, as _ZNK21QStyleKitStylePrivate16metricsForReaderEP16QQStyleKitReader
inline QStyleKitStylePrivate::ControlMetrics
QStyleKitStylePrivate::metricsForReader(QQStyleKitReader *reader) const
{
    Q_ASSERT(reader);
    using QtPrivate::qSaturateRound;
    const QQStyleKitControlProperties *props = reader->global();
    ControlMetrics metrics;
    metrics.bgImplicitSize = QSize(0, 0);
    metrics.textPadding = QMargins(0, 0, 0, 0);
    metrics.padding = QMargins(qSaturateRound(props->leftPadding()),
                               qSaturateRound(props->topPadding()),
                               qSaturateRound(props->rightPadding()),
                               qSaturateRound(props->bottomPadding()));
    metrics.spacing = qSaturateRound(props->spacing());
    metrics.margins = QMargins(0, 0, 0, 0);
    metrics.indicatorImplicitSize = QSize(0, 0);
    metrics.indicatorMargins = QMargins(0, 0, 0, 0);
    metrics.foregroundImplicitSize = QSize(0, 0);
    metrics.foregroundMargins = QMargins(0, 0, 0, 0);
    const auto *background = props->background();

    // Note: scale is deliberately absent here as it should not affect layout
    const auto elementSize = [](qreal w, qreal h) {
        constexpr qreal zero(.0);
        return QSizeF(std::max(zero, w), std::max(zero, h)).toSize();
    };

    if (background) {
        metrics.bgImplicitSize = elementSize(background->width(), background->height());
        metrics.margins = elementMargins(background);
    }
    const auto *textProps = props->text();
    if (textProps) {
        metrics.textPadding = QMargins(qSaturateRound(textProps->leftPadding()),
                                       qSaturateRound(textProps->topPadding()),
                                       qSaturateRound(textProps->rightPadding()),
                                       qSaturateRound(textProps->bottomPadding()));
    }
    const auto *indicator = props->indicator();
    if (indicator) {
        metrics.indicatorMargins = elementMargins(indicator);
        metrics.indicatorImplicitSize = elementSize(indicator->width(), indicator->height());

        const auto *foreground = indicator->foreground();
        if (foreground) {
            metrics.foregroundMargins = elementMargins(foreground);
            const auto foregroundW = resolvedWidth(
                foreground,
                std::max(.0, qreal(metrics.indicatorImplicitSize.width()
                                    - metrics.foregroundMargins.left()
                                    - metrics.foregroundMargins.right())));
            const auto foregroundH = resolvedHeight(
                foreground,
                std::max(.0, qreal(metrics.indicatorImplicitSize.height()
                                    - metrics.foregroundMargins.top()
                                    - metrics.foregroundMargins.bottom())));
            metrics.foregroundImplicitSize = elementSize(foregroundW, foregroundH);
        }
    }
    const auto *handle = props->handle();
    if (handle) {
        metrics.handleImplicitSize = elementSize(handle->width(), handle->height());
        metrics.handleMargins = elementMargins(handle);
    }
    return metrics;
}

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 950, as _ZNK21QStyleKitStylePrivate25startSubElementTransitionERKNS_13SubElementKeyEN16QQStyleKitReader11ControlTypeE6QFlagsIN4QQSK9StateFlagEES8_P16QQuickTransition
inline QQStyleKitReader *QStyleKitStylePrivate::startSubElementTransition(
    const SubElementKey &key, QQStyleKitReader::ControlType type, QQSK::State fromState,
    QQSK::State toState, QQuickTransition *transition) const
{
    Q_Q(const QStyleKitStyle);
    QQStyleKitStyle *effective = effectiveStyle();
    if (!effective)
        return nullptr;

    // Reclaim finished readers. running() is per (shared) transition object, so
    // it turns false only once no instance of that transition animates anywhere
    for (auto it = subElementAnimationReaders.begin(); it != subElementAnimationReaders.end();) {
        const QQuickTransition *t = it.value()->transition();
        if (!t || !t->running()) {
            it.value()->deleteLater();
            it = subElementAnimationReaders.erase(it);
        } else {
            ++it;
        }
    }


    if (subElementAnimationReaders.size() >= kMaxSubElementAnimationReaders) {
        const auto it = subElementAnimationReaders.begin();
        if (const QWidget *widget = it.key().widget)
            paintTarget(widget)->update(); // snap to end state
        it.value()->deleteLater();
        subElementAnimationReaders.erase(it);
    }

    auto *reader = new QQStyleKitReader(const_cast<QStyleKitStyle *>(q));
    reader->setExplicitStyle(effective);
    reader->setTarget(paintTarget(key.widget));
    // just stores the fromState, doesn't start the animation yet
    reader->setControlTypeAndState(type, fromState);
    reader->setCompleted(true);
    // As delegates are created lazily, a fresh reader has none,
    // so we need to create them now so delegates can already start animating changes
    // Only create delegates actually used by subelements, ie: background, indicators
    reader->background();
    auto *indicator = reader->indicator();
    indicator->first()->foreground();
    indicator->second()->foreground();
    // Start the transition to the new state
    reader->setControlTypeAndState(type, toState);
    if (!transition || !transition->running()) {
        reader->deleteLater();
        return nullptr;
    }
    subElementAnimationReaders.insert(key, reader);
    return reader;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1945, as _ZNK24QQStyleKitTextProperties10topPaddingEv
inline qreal QQStyleKitTextProperties::topPadding() const
{
    return styleProperty<qreal>(QQSK::Property::TopPadding, QQSK::Property::Padding);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1923, as _ZNK24QQStyleKitTextProperties11leftPaddingEv
inline qreal QQStyleKitTextProperties::leftPadding() const
{
    return styleProperty<qreal>(QQSK::Property::LeftPadding, QQSK::Property::Padding);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1934, as _ZNK24QQStyleKitTextProperties12rightPaddingEv
inline qreal QQStyleKitTextProperties::rightPadding() const
{
    return styleProperty<qreal>(QQSK::Property::RightPadding, QQSK::Property::Padding);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1956, as _ZNK24QQStyleKitTextProperties13bottomPaddingEv
inline qreal QQStyleKitTextProperties::bottomPadding() const
{
    return styleProperty<qreal>(QQSK::Property::BottomPadding, QQSK::Property::Padding);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1789, as _ZNK29QQStyleKitIndicatorProperties10foregroundEv
inline QQStyleKitDelegateProperties *QQStyleKitIndicatorProperties::foreground() const
{
    return lazyCreateGroup(m_foreground, QQSK::PropertyGroup::Foreground);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1811, as _ZNK31QQStyleKitIndicatorWithSubTypes10foregroundEv
inline QQStyleKitDelegateProperties *QQStyleKitIndicatorWithSubTypes::foreground() const
{
    return lazyCreateGroup(m_foreground, QQSK::PropertyGroup::Foreground);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1826, as _ZNK31QQStyleKitIndicatorWithSubTypes5firstEv
inline QQStyleKitIndicatorProperties *QQStyleKitIndicatorWithSubTypes::first() const
{
    return lazyCreateGroup(m_first, QQSK::PropertyGroup::DelegateSubtype1);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1831, as _ZNK31QQStyleKitIndicatorWithSubTypes6secondEv
inline QQStyleKitIndicatorProperties *QQStyleKitIndicatorWithSubTypes::second() const
{
    return lazyCreateGroup(m_second, QQSK::PropertyGroup::DelegateSubtype2);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 562, as _ZN26QQStyleKitPropertyResolver17readStylePropertyEPK23QQStyleKitPropertyGroupN4QQSK8PropertyES4_
inline QVariant QQStyleKitPropertyResolver::readStyleProperty(
    const QQStyleKitPropertyGroup *group,
    const QQSK::Property property,
    const QQSK::Property alternative)
{
    const QQStyleKitControlProperties *controlProperties = group->controlProperties();
    const QQSK::PropertyPathFlags pathFlags = group->pathFlags();
    const QQSK::Subclass subclass = controlProperties->subclass();

    if (subclass != QQSK::Subclass::QQStyleKitReader) {
        /* Due to propagation, we must know the reader’s state in order to resolve the value
         * of a given property. For example, the background delegate’s color may follow a
         * completely different lookup path—and therefore produce a different result—depending
         * on whether the reader is a Slider or a Button, and whether it is hovered, pressed, etc.
         * For this reason, when a property is not read via a QQStyleKitReader, propagation and
         * fall back logic cannot be supported.
         * However, to still allow static (i.e., non-propagating) bindings between properties
         * _inside_ a Style, we fall back to return the value set directly on the accessed control. */
        Q_ASSERT(subclass == QQSK::Subclass::QQStyleKitState);
        const QQStyleKitControlState *controlState = controlProperties->asQQStyleKitState();
        const QQStyleKitControl *control = controlState->control();
        const PropertyPathId propertyPathId = group->propertyPathId(property, PropertyPathId::Flag::IncludeSubtype);
        const PropertyStorageId key = propertyPathId.storageId(controlState->nestedState());
        return control->readStyleProperty(key);
    }

    QQStyleKitStyle *style = controlProperties->style();
    if (!style || !style->loaded()) {
        /* No style has been set yet, or the style is still loading. The application should set
         * a style early (e.g. at the top of main.qml) before creating any controls, to avoid
         * premature property reads that end up here. However, some controls like the menu bar
         * are instantiated very early and may try to read properties before a style is available. */
        return {};
    }

    QQStyleKitDebug::groupBeingRead = group;
    QQStyleKitReader *styleReader = controlProperties->asQQStyleKitReader();

    if (s_isReadingProperty) {
        if (!s_styleWarningsIssued) {
            s_styleWarningsIssued = true;
            qmlWarning(styleReader) << "The style property '" << property << "' was read "
                                    << "before finishing the read of another style property. "
                                    << "This is likely to cause a style glitch.";
        }
    }
    QScopedValueRollback rollback(s_isReadingProperty, true);

    PropertyPathIds ids;
    ids.property = group->propertyPathId(property, PropertyPathId::Flag::ExcludeSubtype);
    ids.alternative = group->propertyPathId(alternative, PropertyPathId::Flag::ExcludeSubtype);
    const bool insideSubType = pathFlags &
        (QQSK::PropertyPathFlag::DelegateSubtype1 | QQSK::PropertyPathFlag::DelegateSubtype2);

    if (insideSubType) {
        ids.subTypeProperty = group->propertyPathId(property, PropertyPathId::Flag::IncludeSubtype);
        ids.subTypeAlternative = group->propertyPathId(alternative, PropertyPathId::Flag::IncludeSubtype);
    } else {
        ids.subTypeProperty = PropertyPathId();
        ids.subTypeAlternative = PropertyPathId();
    }

    if (!pathFlags.testFlag(QQSK::PropertyPathFlag::Global)) {
        /* A style reader can have a storage that contains local property overrides (that is,
         * interpolated values from an ongoing transition). When searching for a property, we
         * therefore need to check this storage first. The exception is if the property was read
         * inside the 'global' group, which means that we should read the values directly
         * from the style. */
        if (insideSubType) {
            const QVariant value = readPropertyInStorageForState(
                ids.subTypeProperty, ids.subTypeAlternative, styleReader, QQSK::StateFlag::Normal);
            if (value.isValid())
                return value;
        }
        const QVariant value = readPropertyInStorageForState(
            ids.property, ids.alternative, styleReader, QQSK::StateFlag::Normal);
        if (value.isValid())
            return value;
    }

    return readPropertyInStyle(style, ids, styleReader);
}

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

//  from ../qtdeclarative/src/labs/stylekit/widgets/qstylekitstyle.cpp, line 899, as _ZN21QStyleKitStylePrivate22subElementKeyForOptionEPK12QStyleOptionPK7QWidget
inline QStyleKitStylePrivate::SubElementKey
QStyleKitStylePrivate::subElementKeyForOption(const QStyleOption *opt, const QWidget *widget)
{
    SubElementKey key;
    if (!widget)
        return key;

#if QT_CONFIG(itemviews)
    if (const auto *viewOpt = qstyleoption_cast<const QStyleOptionViewItem *>(opt)) {
        const QModelIndex &idx = viewOpt->index;
        if (!idx.isValid())
            return key;
        key.widget = widget;
        key.id = SubElementKey::ItemViewCell{ idx.model(), idx.internalId(), idx.row(),
                                              idx.column() };
        return key;
    }
#endif
#if QT_CONFIG(menu)
    if (const auto *menuOpt = qstyleoption_cast<const QStyleOptionMenuItem *>(opt)) {
        if (menuOpt->menuItemType == QStyleOptionMenuItem::Separator)
            return key;
        QAction *action = nullptr;
        if (const auto *menu = qobject_cast<const QMenu *>(widget))
            action = menu->actionAt(menuOpt->rect.center());
        else if (const auto *menuBar = qobject_cast<const QMenuBar *>(widget))
            action = menuBar->actionAt(menuOpt->rect.center());
        if (action) {
            key.widget = widget;
            key.id = SubElementKey::Action{ action };
        }
        return key;
    }
#endif
#if QT_CONFIG(tabbar)
    if (const auto *tabOpt = qstyleoption_cast<const QStyleOptionTab *>(opt)) {
        if (tabOpt->tabIndex < 0)
            return key;
        key.widget = widget;
        key.id = SubElementKey::Tab{ tabOpt->tabIndex };
        return key;
    }
#endif
    return key;
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

//  SubElementKey QStyleKitStylePrivate::subElementKeyForOption(const
//      QStyleOption *opt, const QWidget *widget)
extern "C" Q_DECL_EXPORT
QStyleKitStylePrivate::SubElementKey *ritual_ZN21QStyleKitStylePrivate22subElementKeyForOptionEPK12QStyleOptionPK7QWidget(
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QStyleKitStylePrivate::SubElementKey(
      QStyleKitStylePrivate::subElementKeyForOption(
          opt,
          widget));
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

//  a QStyleKitStylePrivate::SubElementKey a ritual of QStyleKitStylePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStyleKitStylePrivate__QStyleKitStylePrivate_SubElementKey(
    QStyleKitStylePrivate::SubElementKey *self) {
  delete self;
}

//  a QStyleKitStylePrivate::QQStyleKitResolved a ritual of
//      QStyleKitStylePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStyleKitStylePrivate__QStyleKitStylePrivate_QQStyleKitResolved(
    QStyleKitStylePrivate::QQStyleKitResolved *self) {
  delete self;
}

//  a QStyleKitStylePrivate::QQStyleKitLayoutResolved a ritual of
//      QStyleKitStylePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStyleKitStylePrivate__QStyleKitStylePrivate_QQStyleKitLayoutResolved(
    QStyleKitStylePrivate::QQStyleKitLayoutResolved *self) {
  delete self;
}

//  a QStyleKitStylePrivate::ControlMetrics a ritual of QStyleKitStylePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStyleKitStylePrivate__QStyleKitStylePrivate_ControlMetrics(
    QStyleKitStylePrivate::ControlMetrics *self) {
  delete self;
}

#endif  // 1
