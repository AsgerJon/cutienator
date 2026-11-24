//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdebug_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitdebug_p.h"
#include "qqstylekitcontrol_p.h"
#include "qqstylekitcontrols_p.h"
#include "qqstylekitstyle_p.h"
#include "qqstylekittheme_p.h"
#include "qqstylekitvariation_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitDebug::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQStyleKitDebug10metaObjectEv(
    const QQStyleKitDebug *self) {
  return self->metaObject();
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
