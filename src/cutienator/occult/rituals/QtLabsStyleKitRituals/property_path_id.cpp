//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  PropertyPathId::PropertyPathId(const QQSK::Property property, const
//      PropertyPathId_t groupStart, QQSK::PropertyGroup subtype)
extern "C" Q_DECL_EXPORT
PropertyPathId *ritual_ZN14PropertyPathIdC1EN4QQSK8PropertyEjNS0_13PropertyGroupE(
    const QQSK::Property *property,
    PropertyPathId_t groupStart,
    QQSK::PropertyGroup subtype) {
  return new PropertyPathId(*property, groupStart, subtype);
}

//  QQSK::Property PropertyPathId::property() const
extern "C" Q_DECL_EXPORT
QQSK::Property ritual_ZNK14PropertyPathId8propertyEv(
    const PropertyPathId *self) {
  return self->property();
}

//  PropertyPathId_t PropertyPathId::pathId() const
extern "C" Q_DECL_EXPORT
PropertyPathId_t ritual_ZNK14PropertyPathId6pathIdEv(
    const PropertyPathId *self) {
  return self->pathId();
}

//  PropertyStorageId PropertyPathId::storageId(QQSK::State state) const
extern "C" Q_DECL_EXPORT
PropertyStorageId ritual_ZNK14PropertyPathId9storageIdE6QFlagsIN4QQSK9StateFlagEE(
    const PropertyPathId *self,
    int state) {
  return self->storageId(QFlags<QQSK::StateFlag>::fromInt(state));
}

//  PropertyPathId::~PropertyPathId()
extern "C" Q_DECL_EXPORT
void ritual_ZN14PropertyPathIdD1Ev(PropertyPathId *self) {
  delete self;
}
