//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquickimplicitsizeitem_p_p.h>
#include <QtQuickControls2Impl/private/qquickcolorimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 72, as _ZNK18QQStyleKitDelegate13delegateStyleEv
inline QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
{
    return m_delegateProperties;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 103, as _ZN18QQStyleKitDelegate18updateImplicitSizeEv
inline void QQStyleKitDelegate::updateImplicitSize()
{
    if (!m_delegateProperties)
        return;

    /* The implicit size of this item is determined by the following priority:
     * 1. The width/height set on DelegateStyle (clamped to minimumWidth/minimumHeight)
     * 2. The implicit size of the image overlay (if present)
     * 3. Zero */
    const qreal widthInStyle = qMax(m_delegateProperties->minimumWidth(), m_delegateProperties->width());
    const qreal heightInStyle = qMax(m_delegateProperties->minimumHeight(), m_delegateProperties->height());
    setImplicitWidth(widthInStyle > 0 || !m_imageOverlay ? widthInStyle : m_imageOverlay->implicitWidth());
    setImplicitHeight(heightInStyle > 0 || !m_imageOverlay ? heightInStyle : m_imageOverlay->implicitHeight());
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitDelegate10metaObjectEv(
    const QQStyleKitDelegate *self) {
  return self->metaObject();
}

//  void *QQStyleKitDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQStyleKitDelegate11qt_metacastEPKc(
    QQStyleKitDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQStyleKitDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitDelegateProperties *ritual_ZNK18QQStyleKitDelegate13delegateStyleEv(
    const QQStyleKitDelegate *self) {
  return self->delegateStyle();
}

//  void QQStyleKitDelegate::delegateStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate20delegateStyleChangedEv(
    QQStyleKitDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "delegateStyleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "delegateStyleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitDelegate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate18updateImplicitSizeEv(
    QQStyleKitDelegate *self) {
  self->updateImplicitSize();
}
