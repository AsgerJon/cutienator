//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 191, as _ZNK27QQStyleKitVariationAttached10variationsEv
inline QStringList QQStyleKitVariationAttached::variations() const
{
    return m_variations;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 205, as _ZNK27QQStyleKitVariationAttached11controlTypeEv
inline QQStyleKitExtendableControlType QQStyleKitVariationAttached::controlType() const
{
    return m_controlType;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitVariationAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQStyleKitVariationAttached10metaObjectEv(
    const QQStyleKitVariationAttached *self) {
  return self->metaObject();
}

//  void *QQStyleKitVariationAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQStyleKitVariationAttached11qt_metacastEPKc(
    QQStyleKitVariationAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitVariationAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQStyleKitVariationAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitVariationAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QStringList QQStyleKitVariationAttached::variations() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK27QQStyleKitVariationAttached10variationsEv(
    const QQStyleKitVariationAttached *self) {
  return new QList<QString>(self->variations());
}

//  QQStyleKitExtendableControlType
//      QQStyleKitVariationAttached::controlType() const
extern "C" Q_DECL_EXPORT
QQStyleKitExtendableControlType ritual_ZNK27QQStyleKitVariationAttached11controlTypeEv(
    const QQStyleKitVariationAttached *self) {
  return self->controlType();
}

//  void QQStyleKitVariationAttached::variationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached17variationsChangedEv(
    QQStyleKitVariationAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitVariationAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "variationsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "variationsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitVariationAttached::controlTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached18controlTypeChangedEv(
    QQStyleKitVariationAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitVariationAttached")) {
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
