//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrol_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtQml/QQmlListProperty>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrolstate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitdebug_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolstate.cpp, line 132, as _ZN22QQStyleKitControlStateC2EP7QObject
inline QQStyleKitControlState::QQStyleKitControlState(QObject *parent)
    : QQStyleKitControlProperties(QQSK::PropertyGroup::Control, parent)
{
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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 645, as _ZN26QQStyleKitPropertyResolver18writeStylePropertyEPK23QQStyleKitPropertyGroupN4QQSK8PropertyERK8QVariant
inline bool QQStyleKitPropertyResolver::writeStyleProperty(
    const QQStyleKitPropertyGroup *group,
    const QQSK::Property property,
    const QVariant &value)
{
    // While readStyleProperty() takes propagation into account, writeStyleProperty() doesn't.
    // Instead it writes \a value directly to the storage that the group belongs to.
    Q_ASSERT(group);
    const QQStyleKitControlProperties *controlProperties = group->controlProperties();
    const QQSK::PropertyPathFlags pathFlags = group->pathFlags();
    const QQSK::Subclass subclass = controlProperties->subclass();
    const PropertyPathId propertyPathId = group->propertyPathId(property, PropertyPathId::Flag::IncludeSubtype);

    if (pathFlags.testFlag(QQSK::PropertyPathFlag::Global)) {
        qmlWarning(controlProperties) << "Properties inside 'global' are read-only!";
        return false;
    }

    if (subclass == QQSK::Subclass::QQStyleKitReader) {
        // This is a write to a StyleKitReader, probably from an ongoing transition
        QQStyleKitReader *reader = controlProperties->asQQStyleKitReader();
        const PropertyStorageId key = propertyPathId.storageId(QQSK::StateFlag::Normal);
        const QVariant currentValue = reader->readStyleProperty(key);
        const bool valueChanged = currentValue != value;
        if (valueChanged) {
            reader->writeStyleProperty(key, value);
            QQStyleKitDebug::notifyPropertyWrite(group, property, reader, QQSK::StateFlag::Normal, key, value);
        }
        return valueChanged;
    }

    if (subclass == QQSK::Subclass::QQStyleKitState) {
        // This is a write to a control inside the StyleKit style
        const QQStyleKitControlState *controlState = controlProperties->asQQStyleKitState();
        QQStyleKitControl *control = controlState->control();
        const QQSK::State nestedState = controlState->nestedState();
        const PropertyStorageId key = propertyPathId.storageId(nestedState);
        const QVariant currentValue = control->readStyleProperty(key);
        const bool valueChanged = currentValue != value;
        if (valueChanged) {
            /* Optimization: Allow a control to track which states it stores property values for.
             * When later reading a property via propagation, we can skip that control entirely
             * if it has no stored values corresponding to the state requested by the StyleKitReader. */
            control->m_writtenStates |= nestedState;
            /* Optimization: Track which properties a style, theme, or variation defines
             * values for, and for which states. When reading a property later, we can skip
             * the style/theme/variation entirely if it has no stored values for it, or if
             * none match the state requested by the StyleKitReader. */
            QQStyleKitControls *controls = control->controls();
            const QQSK::State alreadyWrittenStates = controls->m_writtenPropertyPaths[propertyPathId.pathId()];
            controls->m_writtenPropertyPaths[propertyPathId.pathId()] = alreadyWrittenStates | nestedState;

            control->writeStyleProperty(key, value);
            QQStyleKitDebug::notifyPropertyWrite(group, property, control, nestedState, key, value);
        }
        return valueChanged;
    }

    Q_UNREACHABLE();
    return false;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 707, as _ZN26QQStyleKitPropertyResolver21hasLocalStylePropertyEPK23QQStyleKitPropertyGroupN4QQSK8PropertyE
inline bool QQStyleKitPropertyResolver::hasLocalStyleProperty(
    const QQStyleKitPropertyGroup *group,
    const QQSK::Property property)
{
    Q_ASSERT(group);
    const QQStyleKitControlProperties *controlProperties = group->controlProperties();
    const QQSK::PropertyPathFlags pathFlags = group->pathFlags();
    const PropertyPathId propertyPathId = group->propertyPathId(property, PropertyPathId::Flag::IncludeSubtype);
    const QQSK::Subclass subclass = controlProperties->subclass();

    if (pathFlags.testFlag(QQSK::PropertyPathFlag::Global))
        return false;

    if (subclass == QQSK::Subclass::QQStyleKitReader) {
        const PropertyStorageId key = propertyPathId.storageId(QQSK::StateFlag::Normal);
        return controlProperties->asQQStyleKitReader()->readStyleProperty(key).isValid();
    }

    if (subclass == QQSK::Subclass::QQStyleKitState) {
        const QQStyleKitControlState *controlState = controlProperties->asQQStyleKitState();
        const QQStyleKitControl *control = controlState->control();
        const PropertyStorageId key = propertyPathId.storageId(controlState->nestedState());
        return control->readStyleProperty(key).isValid();
    }

    Q_UNREACHABLE();
    return false;
}

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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 105, as _ZNK17QQStyleKitControl17readStylePropertyEj
inline QVariant QQStyleKitControl::readStyleProperty(PropertyStorageId key) const
{
    return m_storage.value(key);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 110, as _ZN17QQStyleKitControl18writeStylePropertyEjRK8QVariant
inline void QQStyleKitControl::writeStyleProperty(PropertyStorageId key, const QVariant &value)
{
    m_storage.insert(key, value);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQStyleKitControl10metaObjectEv(
    const QQStyleKitControl *self) {
  return self->metaObject();
}

//  void *QQStyleKitControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQStyleKitControl11qt_metacastEPKc(
    QQStyleKitControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitControl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQStyleKitControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QVariant QQStyleKitControl::readStyleProperty(PropertyStorageId key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQStyleKitControl17readStylePropertyEj(
    const QQStyleKitControl *self,
    PropertyStorageId key) {
  return new QVariant(self->readStyleProperty(key));
}

//  void QQStyleKitControl::writeStyleProperty(PropertyStorageId key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitControl18writeStylePropertyEjRK8QVariant(
    QQStyleKitControl *self,
    PropertyStorageId key,
    const QVariant *value) {
  self->writeStyleProperty(key, *value);
}

//  a QQmlListProperty<QQStyleKitVariation> a ritual of QQStyleKitControl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQStyleKitControl__QQmlListProperty_QQStyleKitVariation(
    QQmlListProperty<QQStyleKitVariation> *self) {
  delete self;
}
