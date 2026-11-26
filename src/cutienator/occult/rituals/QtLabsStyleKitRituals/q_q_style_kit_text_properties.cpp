//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrolproperties.cpp, line 967, as _ZN23QQStyleKitPropertyGroupC2EN4QQSK13PropertyGroupEP7QObject
inline QQStyleKitPropertyGroup::QQStyleKitPropertyGroup(QQSK::PropertyGroup, QObject *parent)
    : QObject(parent)
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

//  const QMetaObject *QQStyleKitTextProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQStyleKitTextProperties10metaObjectEv(
    const QQStyleKitTextProperties *self) {
  return self->metaObject();
}

//  void *QQStyleKitTextProperties::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQStyleKitTextProperties11qt_metacastEPKc(
    QQStyleKitTextProperties *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitTextProperties::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQStyleKitTextProperties11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitTextProperties *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitTextProperties::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties24qt_qmlMarker_uncreatableEv(
    QQStyleKitTextProperties *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQStyleKitTextProperties::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties12colorChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "colorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "colorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::alignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties16alignmentChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "alignmentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "alignmentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::boldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties11boldChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "boldChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "boldChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::italicChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties13italicChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "italicChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "italicChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::pointSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties16pointSizeChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pointSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pointSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties14paddingChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "paddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "paddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties18leftPaddingChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "leftPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "leftPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties19rightPaddingChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rightPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rightPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties17topPaddingChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "topPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "topPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties20bottomPaddingChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "bottomPaddingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "bottomPaddingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::firstChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties12firstChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "firstChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "firstChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitTextProperties::secondChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQStyleKitTextProperties13secondChangedEv(
    QQStyleKitTextProperties *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitTextProperties")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "secondChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "secondChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
