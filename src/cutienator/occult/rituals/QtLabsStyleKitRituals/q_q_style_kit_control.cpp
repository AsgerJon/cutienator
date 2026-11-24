//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrol_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrolstate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
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
