//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  Impl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsStyleKitImpl/QtLabsStyleKitImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 74, as _ZNK20QQStyleKitLayoutItem4itemEv
inline QQuickItem *QQStyleKitLayoutItem::item() const
{
    return m_item;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 97, as _ZNK20QQStyleKitLayoutItem1xEv
inline qreal QQStyleKitLayoutItem::x() const
{
    return m_x;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 111, as _ZNK20QQStyleKitLayoutItem1yEv
inline qreal QQStyleKitLayoutItem::y() const
{
    return m_y;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 125, as _ZNK20QQStyleKitLayoutItem5widthEv
inline qreal QQStyleKitLayoutItem::width() const
{
    return m_width;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 139, as _ZNK20QQStyleKitLayoutItem6heightEv
inline qreal QQStyleKitLayoutItem::height() const
{
    return m_height;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 153, as _ZNK20QQStyleKitLayoutItem9alignmentEv
inline Qt::Alignment QQStyleKitLayoutItem::alignment() const
{
    return m_alignment;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 167, as _ZNK20QQStyleKitLayoutItem7marginsEv
inline QMarginsF QQStyleKitLayoutItem::margins() const
{
    return m_margins;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 181, as _ZNK20QQStyleKitLayoutItem9fillWidthEv
inline bool QQStyleKitLayoutItem::fillWidth() const
{
    return m_fillWidth;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 195, as _ZNK20QQStyleKitLayoutItem10fillHeightEv
inline bool QQStyleKitLayoutItem::fillHeight() const
{
    return m_fillHeight;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitLayoutItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQStyleKitLayoutItem10metaObjectEv(
    const QQStyleKitLayoutItem *self) {
  return self->metaObject();
}

//  void *QQStyleKitLayoutItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQStyleKitLayoutItem11qt_metacastEPKc(
    QQStyleKitLayoutItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitLayoutItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQStyleKitLayoutItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitLayoutItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickItem *QQStyleKitLayoutItem::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQStyleKitLayoutItem4itemEv(
    const QQStyleKitLayoutItem *self) {
  return self->item();
}

//  qreal QQStyleKitLayoutItem::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1xEv(
    const QQStyleKitLayoutItem *self) {
  return self->x();
}

//  qreal QQStyleKitLayoutItem::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1yEv(
    const QQStyleKitLayoutItem *self) {
  return self->y();
}

//  qreal QQStyleKitLayoutItem::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem5widthEv(
    const QQStyleKitLayoutItem *self) {
  return self->width();
}

//  qreal QQStyleKitLayoutItem::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem6heightEv(
    const QQStyleKitLayoutItem *self) {
  return self->height();
}

//  Qt::Alignment QQStyleKitLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQStyleKitLayoutItem9alignmentEv(
    const QQStyleKitLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  QMarginsF QQStyleKitLayoutItem::margins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QQStyleKitLayoutItem7marginsEv(
    const QQStyleKitLayoutItem *self) {
  return new QMarginsF(self->margins());
}

//  bool QQStyleKitLayoutItem::fillWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem9fillWidthEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillWidth();
}

//  bool QQStyleKitLayoutItem::fillHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem10fillHeightEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillHeight();
}

//  void QQStyleKitLayoutItem::itemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem11itemChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::xChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem8xChangedEv(QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "xChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "xChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::yChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem8yChangedEv(QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem12widthChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "widthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "widthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem13heightChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "heightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "heightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::alignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem16alignmentChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
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

//  void QQStyleKitLayoutItem::marginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem14marginsChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "marginsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "marginsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::fillWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem16fillWidthChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fillWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fillWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::fillHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem17fillHeightChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fillHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fillHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
