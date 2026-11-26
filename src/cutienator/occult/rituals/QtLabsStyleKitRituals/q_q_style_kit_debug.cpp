//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdebug_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/QFlags>
#include <QtCore/QVariant>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitdebug_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 92, as local:qqstylekitdebug.cpp:kDot
static const QChar kDot = '.'_L1;

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 170, as _ZN15QQStyleKitDebug10objectPathEPK27QQStyleKitControlPropertiesP7QObject
inline QString QQStyleKitDebug::objectPath(const QQStyleKitControlProperties *properties, QObject *from)
{
    QString path;
    const QObject *obj = properties;

    while (obj) {
        if (!path.isEmpty())
            path.prepend(kDot);

        if (auto *theme = qobject_cast<const QQStyleKitCustomTheme *>(obj)) {
            path.prepend(theme->name() + kDot);
        } else if (auto *theme = qobject_cast<const QQStyleKitTheme *>(obj)) {
            // Note: only one theme is instantiated at a time
            path.prepend("Theme("_L1 + theme->style()->m_effectiveThemeName + ")"_L1);
        } else if (auto *variation = qobject_cast<const QQStyleKitVariation *>(obj)) {
            path.prepend("StyleVariation("_L1 + variation->name() + ")"_L1);
        } else if (auto *control = qobject_cast<const QQStyleKitControl *>(obj)) {
            path.prepend(controlToString(control));
        } else if (auto *reader = qobject_cast<const QQStyleKitReader *>(obj)) {
            path.prepend(styleReaderToString(reader));
        } else {
            path.prepend(objectName(obj));
        }

        if (obj == from)
            break;

        obj = obj->parent();
    }

    return path;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 129, as _ZN15QQStyleKitDebug12propertyPathEPK23QQStyleKitPropertyGroup14PropertyPathId
inline QString QQStyleKitDebug::propertyPath(const QQStyleKitPropertyGroup *group, const PropertyPathId property)
{
    const QString path = group->pathToString();
    QString propertyName = enumToString(property.property());
    propertyName[0] = propertyName[0].toLower();
    if (path.isEmpty())
        return propertyName;
    return path + kDot + propertyName;
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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 317, as _ZN15QQStyleKitDebug5traceE14PropertyPathIdPK27QQStyleKitControlProperties6QFlagsIN4QQSK9StateFlagEEj
inline void QQStyleKitDebug::trace(
    const PropertyPathId property,
    const QQStyleKitControlProperties *storage,
    const QQSK::State state,
    const PropertyStorageId key)
{
#if 1
    Q_UNUSED(property);
    Q_UNUSED(storage);
    Q_UNUSED(state);
    Q_UNUSED(key);
#else
    const QQStyleKitControlProperties *reader = QQStyleKitDebug::groupBeingRead->controlProperties();
    if (reader->subclass() == QQSK::Subclass::QQStyleKitState) {
        /* The reader is in the UnfiedStyle, and not in the users application (which can happen
         * when e.g resolving local bindings between properties in the style). Those are not
         * interesting to print out when inspecting control-to-style mappings. Ignore. */
        return;
    }

    if (!insideControl(reader)) {
        // We should only debug reads that targets m_item. So return.
        return;
    }

    const QString _readerPath = objectPath(reader, m_item);
    const QString _readPropertyPath = propertyPath(QQStyleKitDebug::groupBeingRead, property);
    const QString queriedPath = _readerPath + kDot +_readPropertyPath;

    QString storagePath;
    if (storage->subclass() == QQSK::Subclass::QQStyleKitReader) {
        /* We read an interpolated value stored directly in the reader itself. While this
         * can be interesting to print out whe debugging the styling engine itself, it
         * comes across as noise when inspecting control-to-style mappings. Ignore. */
#if 0
        storagePath = "[local storage]"_L1;
#else
        return;
#endif
    } else {
        const QString _controlPathInStyle = objectPath(storage, storage->style());
        const QString _statePath = stateToString(state);
        storagePath = _controlPathInStyle + _statePath;
    }

    const QString output = queriedPath + ", checking "_L1 + storagePath + " (storage key:"_L1 + QString::number(key)+ ")"_L1;

    if (!QRegularExpression(m_filter).match(output).hasMatch())
        return;

    qDebug().nospace().noquote() << m_outputCount++ << " | [trace] "_L1 << output;
#endif
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdebug.cpp, line 101, as _ZN15QQStyleKitDebug10objectNameEPK7QObject
inline QString QQStyleKitDebug::objectName(const QObject *obj) {
    if (!obj->objectName().isEmpty())
        return obj->objectName();

    QString str = QString::fromLatin1(obj->metaObject()->className());
    int idx = str.indexOf("_QMLTYPE"_L1);
    if (idx != -1)
        str = str.left(idx);
    else {
        const QString prefix("QQStyleKit"_L1);
        if (str.startsWith(prefix))
            str = str.mid(prefix.length());
    }

    return str;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitDebug::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQStyleKitDebug10metaObjectEv(
    const QQStyleKitDebug *self) {
  return self->metaObject();
}

//  void *QQStyleKitDebug::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQStyleKitDebug11qt_metacastEPKc(
    QQStyleKitDebug *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitDebug::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQStyleKitDebug11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitDebug *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitDebug::controlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitDebug14controlChangedEv(QQStyleKitDebug *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitDebug")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitDebug::filterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitDebug13filterChangedEv(QQStyleKitDebug *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitDebug")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filterChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filterChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitDebug::notifyPropertyWrite(const QQStyleKitPropertyGroup
//      *group, const QQSK::Property property, const
//      QQStyleKitControlProperties *storage, const QQSK::State state, const
//      PropertyStorageId key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitDebug19notifyPropertyWriteEPK23QQStyleKitPropertyGroupN4QQSK8PropertyEPK27QQStyleKitControlProperties6QFlagsINS3_9StateFlagEEjRK8QVariant(
    const QQStyleKitPropertyGroup *group,
    const QQSK::Property *property,
    const QQStyleKitControlProperties *storage,
    int state,
    PropertyStorageId key,
    const QVariant *value) {
  QQStyleKitDebug::notifyPropertyWrite(
      group,
      *property,
      storage,
      QFlags<QQSK::StateFlag>::fromInt(state),
      key,
      *value);
}

//  void QQStyleKitDebug::trace(const PropertyPathId property, const
//      QQStyleKitControlProperties *resolvedControl, const QQSK::State
//      state, const PropertyStorageId key)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitDebug5traceE14PropertyPathIdPK27QQStyleKitControlProperties6QFlagsIN4QQSK9StateFlagEEj(
    const PropertyPathId *property,
    const QQStyleKitControlProperties *resolvedControl,
    int state,
    PropertyStorageId key) {
  QQStyleKitDebug::trace(
      *property,
      resolvedControl,
      QFlags<QQSK::StateFlag>::fromInt(state),
      key);
}

//  QString QQStyleKitDebug::objectName(const QObject *obj)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQStyleKitDebug10objectNameEPK7QObject(
    const QObject *obj) {
  return new QString(QQStyleKitDebug::objectName(obj));
}
