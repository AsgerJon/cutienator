//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/private/qqstylekitdebug_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolstate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 92, as local:qqstylekitdebug.cpp:kDot
static const QChar kDot = '.'_L1;

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitglobal.cpp, line 8, as _ZN14PropertyPathIdC1EN4QQSK8PropertyEjNS0_13PropertyGroupE
inline PropertyPathId::PropertyPathId(
    const QQSK::Property property,
    const PropertyPathId_t groupStart,
    QQSK::PropertyGroup subtype)
    : m_property(property)
{
    /* Each style property in StyleKit needs a unique PropertyStorageId that can be used as
     * a key in the map that stores its value. To compute such an ID, we must consider the
     * property’s full nested path, since properties like 'background.color' and
     * 'background.border.color' refer to different values.
     *
     * Because a property may have multiple values depending on the control’s state and
     * subtype, we distinguish between a property’s path ID and its storage ID. The path
     * ID represents the portion of the property path that does not vary during lookups.
     * For example, in the full path:
     *
     *     "button.pressed.indicator.up.background.color"
     *
     * the portion that is invariant is:
     *
     *     "indicator.background.color"
     *
     * The other parts of the path—such as the control type ('button'), the state ('pressed'),
     * and the subtype ('up')—are resolved dynamically by the propagation engine. During lookup,
     * the engine substitutes these components in decreasing order of specificity. For instance:
     *
     * - If the property is not found on 'button', it falls back to 'abstractButton'.
     * - If it is not found in the 'pressed' state, it falls back to 'normal'.
     * - If it is not found in the 'up' subtype, it falls back to 'indicator'.
     *
     * These varying components are prepended in sequence by the propagation engine to form
     * the final PropertyStorageId, which uniquely identifies the stored value in the map.
     *
     * Note that a property path may also include groups known as Options. These are not part
     * of the Path ID or the Storage ID; they are simply flags used by QQStyleKitPropertyResolver
     * to control how a property should be read.
     *
     * In general, the structure of a property path is:
     *
     *     control.options.states.subtype.nested_group_path.property
     *
     * However, for API convenience, subtypes are written inside the delegate they belong to.
     * For example, although the storage path is "spinBox.up.indicator.background.color", the
     * style syntax is "spinBox.indicator.up.background.color". */
    const PropertyPathId_t subtypeIndex = PropertyPathId_t(subtype)
        - PropertyPathId_t(QQSK::PropertyGroup::DelegateSubtype0);
    const PropertyPathId_t subtypeStart = subtypeIndex * subtypeStorageSpaceSize;
    m_groupStart = subtypeStart + groupStart;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 258, as _ZN15QQStyleKitDebug19notifyPropertyWriteEPK23QQStyleKitPropertyGroupN4QQSK8PropertyEPK27QQStyleKitControlProperties6QFlagsINS3_9StateFlagEEjRK8QVariant
inline void QQStyleKitDebug::notifyPropertyWrite(
    const QQStyleKitPropertyGroup *group,
    const QQSK::Property property,
    const QQStyleKitControlProperties *storage,
    const QQSK::State state,
    const PropertyStorageId key,
    const QVariant &value)
{
#if 1
    Q_UNUSED(group);
    Q_UNUSED(property);
    Q_UNUSED(storage);
    Q_UNUSED(state);
    Q_UNUSED(key);
    Q_UNUSED(value);
#else
    /* Note: in order to catch _all_ writes, we cannot depend on enabling writes from
     * QML using a property, as that would resolve to 'true' too late. */
    QString storagePath;
    if (storage->subclass() == QQSK::Subclass::QQStyleKitReader) {
        storagePath = "[local storage]"_L1;
    } else {
        const QString _controlPathInStyle = objectPath(storage, storage->style());
        const QString _statePath = stateToString(state);
        storagePath = _controlPathInStyle + _statePath;
    }

    QString valueString = value.toString();
    if (!value.isValid()) // value was set, but probably to undefined
        valueString = "<undefined>"_L1;
    else if (valueString.isEmpty())
        valueString = "<object>"_L1;

    const QString path = propertyPath(group, property);
    const QString output = storagePath + kDot + path + " (storage key:"_L1 + QString::number(key) + ") = "_L1 + valueString;

    qDebug().nospace().noquote() << m_outputCount++ << " | [write] "_L1 << output;
#endif
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 110, as _ZN17QQStyleKitControl18writeStylePropertyEjRK8QVariant
inline void QQStyleKitControl::writeStyleProperty(PropertyStorageId key, const QVariant &value)
{
    m_storage.insert(key, value);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 105, as _ZNK17QQStyleKitControl17readStylePropertyEj
inline QVariant QQStyleKitControl::readStyleProperty(PropertyStorageId key) const
{
    return m_storage.value(key);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 115, as _ZNK17QQStyleKitControl8controlsEv
inline QQStyleKitControls *QQStyleKitControl::controls() const
{
    Q_ASSERT(qobject_cast<QQStyleKitControls *>(parent()));
    return static_cast<QQStyleKitControls *>(parent());
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolstate.cpp, line 137, as _ZNK22QQStyleKitControlState7controlEv
inline QQStyleKitControl *QQStyleKitControlState::control() const
{
    if (m_nestedState == QQSK::StateFlag::Normal) {
        Q_ASSERT(qobject_cast<const QQStyleKitControl *>(this));
        auto *self = const_cast<QQStyleKitControlState *>(this);
        return static_cast<QQStyleKitControl *>(self);
    }
    Q_ASSERT(qobject_cast<const QQStyleKitControl *>(parent()));
    return static_cast<QQStyleKitControl *>(parent());
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 972, as _ZNK23QQStyleKitPropertyGroup14propertyPathIdEN4QQSK8PropertyEN14PropertyPathId4FlagE
inline PropertyPathId QQStyleKitPropertyGroup::propertyPathId(QQSK::Property property, PropertyPathId::Flag flag) const
{
    if (flag == PropertyPathId::Flag::IncludeSubtype) {
        if (m_pathFlags.testFlag(QQSK::PropertyPathFlag::DelegateSubtype1))
            return PropertyPathId(property, m_groupSpace.start, QQSK::PropertyGroup::DelegateSubtype1);
        else if (m_pathFlags.testFlag(QQSK::PropertyPathFlag::DelegateSubtype2))
            return PropertyPathId(property, m_groupSpace.start, QQSK::PropertyGroup::DelegateSubtype2);
    }
    return PropertyPathId(property, m_groupSpace.start, QQSK::PropertyGroup::DelegateSubtype0);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 1029, as _ZNK23QQStyleKitPropertyGroup17controlPropertiesEv
inline QQStyleKitControlProperties *QQStyleKitPropertyGroup::controlProperties() const
{
    if (isControlProperties()) {
        Q_ASSERT(qobject_cast<const QQStyleKitControlProperties *>(this));
        auto *self = const_cast<QQStyleKitPropertyGroup *>(this);
        return static_cast<QQStyleKitControlProperties *>(self);
    }
    Q_ASSERT(qobject_cast<const QQStyleKitControlProperties *>(parent()));
    return static_cast<QQStyleKitControlProperties *>(parent());
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 298, as _ZN15QQStyleKitDebug25notifyPropertyNotResolvedE14PropertyPathId
inline void QQStyleKitDebug::notifyPropertyNotResolved(const PropertyPathId property)
{
    const QQStyleKitControlProperties *reader = QQStyleKitDebug::groupBeingRead->controlProperties();
    if (!insideControl(reader)) {
        // We should only debug reads that targets m_item. So return.
        return;
    }

    const QString _readerPath = objectPath(reader, m_item);
    const QString _propertyPath = propertyPath(QQStyleKitDebug::groupBeingRead, property);
    const QString queriedPath = _readerPath + kDot +_propertyPath;
    const QString output = queriedPath + " -> <property not set>"_L1;

    if (!QRegularExpression(m_filter).match(output).hasMatch())
        return;

    qDebug().nospace().noquote() << m_outputCount++ << " | [read] "_L1 << output;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 654, as _ZNK18QQStyleKitControls15getControlStyleEj
inline QQStyleKitControl* QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType controlType) const
{
    return m_controls.value(controlType, nullptr);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 172, as _ZNK19QQStyleKitVariation4nameEv
inline QString QQStyleKitVariation::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 191, as _ZNK27QQStyleKitVariationAttached10variationsEv
inline QStringList QQStyleKitVariationAttached::variations() const
{
    return m_variations;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 22, as _ZN26QQStyleKitPropertyResolver16baseTypesForTypeEj
inline const QList<QQStyleKitExtendableControlType> QQStyleKitPropertyResolver::baseTypesForType(
    QQStyleKitExtendableControlType exactType)
{
    /* By default, the base types should mirror the class hierarchy in Qt Quick Controls.
     * However, to make it possible to style a base type without having to "undo" it again
     * in a sub type, we choose to diverge in som cases:
     *
     * ItemDelegate — Normally used as a menu item in a ComboBox or as an item in a ListView.
     *     Although it behaves similarly to a button, it is typically styled very differently
     *     (e.g., without borders, drop shadows, gradients, etc.). For that reason, it falls
     *     back to Control rather than AbstractButton.
     *
     * MenuBarItem — Although it is technically a button, it is typically styled very differently
     *      from other buttons (e.g., without borders, drop shadows, gradients, etc.). For that
     *      reason, it falls back to Control rather than AbstractButton.
     *
     * MenuItem — In Qt Quick Controls, MenuItem inherits from AbstractButton. Although it
     *     behaves similarly to a button, it is typically styled very differently
     *     (e.g., without borders, drop shadows, gradients, etc.). For that reason, it falls
     *     back to Control rather than AbstractButton.
     *
     * TabBar — In Qt Quick Controls, ToolBar inherits Pane, while TabBar inherits Container.
     *     Since it is desirable for a TabBar to share styling characteristics (such as
     *     background color) with ToolBar and Pane, we let it fall back to Pane instead of
     *     Control.
     */
    switch (exactType) {
    case QQStyleKitReader::ApplicationWindow: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::ApplicationWindow };
        return t; }
    case QQStyleKitReader::Button:
    case QQStyleKitReader::DelayButton:
    case QQStyleKitReader::FlatButton:
    case QQStyleKitReader::ToolButton:
    case QQStyleKitReader::TabButton:
    case QQStyleKitReader::RadioButton:
    case QQStyleKitReader::RoundButton:
    case QQStyleKitReader::CheckBox:
    case QQStyleKitReader::SwitchControl: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::AbstractButton, QQStyleKitReader::Control };
        return t; }
    case QQStyleKitReader::CheckDelegate:
    case QQStyleKitReader::RadioDelegate:
    case QQStyleKitReader::SwipeDelegate:
    case QQStyleKitReader::SwitchDelegate: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::ItemDelegate, QQStyleKitReader::Control };
        return t; }
    case QQStyleKitReader::Menu:
    case QQStyleKitReader::Dialog: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::Popup, QQStyleKitReader::Control };
        return t; }
    case QQStyleKitReader::Page:
    case QQStyleKitReader::DialogButtonBox:
    case QQStyleKitReader::Frame:
    case QQStyleKitReader::TabBar:
    case QQStyleKitReader::ToolBar: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::Pane, QQStyleKitReader::Control };
        return t; }
    case QQStyleKitReader::GroupBox: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::Frame, QQStyleKitReader::Pane, QQStyleKitReader::Control };
        return t;
    }
    case QQStyleKitReader::TextField:
    case QQStyleKitReader::TextArea: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::TextInput, QQStyleKitReader::Control };
        return t; }
    default: {
        static QList<QQStyleKitExtendableControlType> t =
            { QQStyleKitReader::Control };
        return t; }
    }

    Q_UNREACHABLE();
    return {};
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 135, as _ZN26QQStyleKitPropertyResolver20addVariationToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseP19QQStyleKitVariation
inline void QQStyleKitPropertyResolver::addVariationToReader(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    QQStyleKitVariation *variation)
{
    /* Add the variation to the StyleReader's list of effective variations.
     * A variation may appear more than once in a type variation list or in
     * an instance variation list, but it only needs to be added once - the
     * first in the list will shadow the other ones anyway. */
    if (!styleReader->m_effectiveVariations.contains(variation))
        styleReader->m_effectiveVariations.append(variation);

    /* We also record in which Style or Theme the variation was found, so that
     * it only takes effect for that specific Style or Theme during property
     * propagation. Note that the same type variation can be used from both the
     * Style and the Theme (its ID can be added to several variation lists). */
    if (!variation->m_usageContext.contains(styleOrTheme))
        variation->m_usageContext.append(styleOrTheme);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 210, as _ZN26QQStyleKitPropertyResolver29addInstanceVariationsToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseRK15QVarLengthArrayIPK27QQStyleKitVariationAttachedLx20EE
inline void QQStyleKitPropertyResolver::addInstanceVariationsToReader(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    const AttachedVariationList &attachedVariations)
{
    /* Add the variations set from the application to the list of effective variations
     * in the styleReader. But, to speed up property look-up later on, we only add the
     * variations that has the potential to affect the control type, or its base types,
     * that the styleReader represents. The variations that are closest to styleReader
     * in the hierarchy will be added first and take precendence over the ones added last. */
    const QQStyleKitExtendableControlType styleReaderType = styleReader->controlType();
    const auto styleReaderBaseTypes = baseTypesForType(styleReaderType);

    for (const QQStyleKitVariationAttached *attached : attachedVariations) {
        for (const QString &instanceVariationName : attached->variations()) {
            for (QQStyleKitVariation *variation : styleOrTheme->m_styleVariations)  {
                if (variation->name() != instanceVariationName)
                    continue;

                /* Invariant: we found a variation in the given Style or a Theme with a name that matches
                 * a name in the attached variation list. Check if the found variation contains the
                 * type, or the subtypes, of the style reader. If not, it doesn't affect it and can
                 * therefore be skipped. */
                if (variation->getControlStyle(styleReaderType)) {
                    addVariationToReader(styleReader, styleOrTheme, variation);
                } else {
                    for (int baseType : styleReaderBaseTypes) {
                        if (variation->getControlStyle(baseType))
                            addVariationToReader(styleReader, styleOrTheme, variation);
                    }
                }
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  const QList<QQStyleKitExtendableControlType> QQStyleKitPropertyResolver::
//      baseTypesForType(QQStyleKitExtendableControlType exactType)
extern "C" Q_DECL_EXPORT
QList<QQStyleKitExtendableControlType> *ritual_ZN26QQStyleKitPropertyResolver16baseTypesForTypeEj(
    QQStyleKitExtendableControlType exactType) {
  return new QList<QQStyleKitExtendableControlType>(
      QQStyleKitPropertyResolver::baseTypesForType(
          exactType));
}

//  void QQStyleKitPropertyResolver::addVariationToReader(QQStyleKitReader
//      *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
//      QQStyleKitVariation *variation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitPropertyResolver20addVariationToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseP19QQStyleKitVariation(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    QQStyleKitVariation *variation) {
  QQStyleKitPropertyResolver::addVariationToReader(
      styleReader,
      styleOrTheme,
      variation);
}

//  void QQStyleKitPropertyResolver::addInstanceVariationsToReader(QQStyleKit
//      Reader *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme, const
//      AttachedVariationList &attachedVariations)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitPropertyResolver29addInstanceVariationsToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseRK15QVarLengthArrayIPK27QQStyleKitVariationAttachedLx20EE(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    const AttachedVariationList *attachedVariations) {
  QQStyleKitPropertyResolver::addInstanceVariationsToReader(
      styleReader,
      styleOrTheme,
      *attachedVariations);
}

//  QQStyleKitPropertyResolver::~QQStyleKitPropertyResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitPropertyResolverD1Ev(
    QQStyleKitPropertyResolver *self) {
  delete self;
}

//  a QList<QQStyleKitExtendableControlType> a ritual of
//      QQStyleKitPropertyResolver gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQStyleKitPropertyResolver__QList_QQStyleKitExtendableControlType(
    QList<QQStyleKitExtendableControlType> *self) {
  delete self;
}
