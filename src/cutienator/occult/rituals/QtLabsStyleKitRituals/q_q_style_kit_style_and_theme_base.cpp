//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitfont_p.h>
#include <QtLabsStyleKit/private/qqstylekitpalette_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 8, as _ZN14QQStyleKitFontC1EP7QObject
inline QQStyleKitFont::QQStyleKitFont(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 8, as _ZN17QQStyleKitPaletteC1EP7QObject
inline QQStyleKitPalette::QQStyleKitPalette(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 604, as _ZN18QQStyleKitControlsC2EP7QObject
inline QQStyleKitControls::QQStyleKitControls(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 43, as _ZN27QQStyleKitStyleAndThemeBase5fontsEv
inline QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
{
    return &m_fonts;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 67, as _ZN27QQStyleKitStyleAndThemeBase8palettesEv
inline QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
{
    return &m_palettes;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitStyleAndThemeBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQStyleKitStyleAndThemeBase10metaObjectEv(
    const QQStyleKitStyleAndThemeBase *self) {
  return self->metaObject();
}

//  void *QQStyleKitStyleAndThemeBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQStyleKitStyleAndThemeBase11qt_metacastEPKc(
    QQStyleKitStyleAndThemeBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitStyleAndThemeBase::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQStyleKitStyleAndThemeBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitStyleAndThemeBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQStyleKitStyleAndThemeBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitStyleAndThemeBase24qt_qmlMarker_uncreatableEv(
    QQStyleKitStyleAndThemeBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZN27QQStyleKitStyleAndThemeBase5fontsEv(
    QQStyleKitStyleAndThemeBase *self) {
  return self->fonts();
}

//  QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZN27QQStyleKitStyleAndThemeBase8palettesEv(
    QQStyleKitStyleAndThemeBase *self) {
  return self->palettes();
}

//  void QQStyleKitStyleAndThemeBase::fontsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitStyleAndThemeBase12fontsChangedEv(
    QQStyleKitStyleAndThemeBase *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitStyleAndThemeBase")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fontsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fontsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitStyleAndThemeBase::palettesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitStyleAndThemeBase15palettesChangedEv(
    QQStyleKitStyleAndThemeBase *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitStyleAndThemeBase")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "palettesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "palettesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
