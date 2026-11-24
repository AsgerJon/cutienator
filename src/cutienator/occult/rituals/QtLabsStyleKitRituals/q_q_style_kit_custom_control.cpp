//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitcontrol_p.h"
#include "qqstylekitcontrols_p.h"
#include "qqstylekitpropertyresolver_p.h"
#include "qqstylekitcustomcontrol_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrol.cpp, line 67, as _ZN17QQStyleKitControlC2EP7QObject
inline QQStyleKitControl::QQStyleKitControl(QObject *parent)
    : QQStyleKitControlState(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomcontrol.cpp, line 67, as _ZNK23QQStyleKitCustomControl11controlTypeEv
inline int QQStyleKitCustomControl::controlType() const
{
    return m_controlType;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitCustomControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQStyleKitCustomControl10metaObjectEv(
    const QQStyleKitCustomControl *self) {
  return self->metaObject();
}

//  int QQStyleKitCustomControl::controlType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQStyleKitCustomControl11controlTypeEv(
    const QQStyleKitCustomControl *self) {
  return self->controlType();
}
