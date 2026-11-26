//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  void *QQStyleKitCustomControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQStyleKitCustomControl11qt_metacastEPKc(
    QQStyleKitCustomControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitCustomControl::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQStyleKitCustomControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitCustomControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  int QQStyleKitCustomControl::controlType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQStyleKitCustomControl11controlTypeEv(
    const QQStyleKitCustomControl *self) {
  return self->controlType();
}

//  void QQStyleKitCustomControl::controlTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQStyleKitCustomControl18controlTypeChangedEv(
    QQStyleKitCustomControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitCustomControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
