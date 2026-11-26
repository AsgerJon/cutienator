//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  Impl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsStyleKitImpl/QtLabsStyleKitImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtQml/QQmlListProperty>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 8, as local:qqstylekitlayout.cpp:layoutWidth
static qreal layoutWidth(QQStyleKitLayoutItem *li, qreal availableWidth = .0)
{
    Q_ASSERT(li);
    Q_ASSERT(li->item());
    QQuickItem *item = li->item();
    qreal w = item->implicitWidth();
    if (li->fillWidth())
        w = qMax(.0, availableWidth - li->margins().left() - li->margins().right());
    return qMax(.0, w);
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 19, as local:qqstylekitlayout.cpp:layoutHeight
static qreal layoutHeight(QQStyleKitLayoutItem *li, qreal availableHeight = .0)
{
    Q_ASSERT(li);
    Q_ASSERT(li->item());
    QQuickItem *item = li->item();
    qreal h = item->implicitHeight();
    if (li->fillHeight())
        h = qMax(.0, availableHeight - li->margins().top() - li->margins().bottom());
    return qMax(.0, h);
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 53, as local:qqstylekitlayout.cpp:vAlignY
static qreal vAlignY(QQStyleKitLayoutItem *li, qreal containerY, qreal containerHeight)
{
    Q_ASSERT(li);
    Q_ASSERT(li->item());

    const auto itemHeight = layoutHeight(li, containerHeight);
    const auto vAlign = li->alignment() & Qt::AlignVertical_Mask;
    const auto margins = li->margins();
    if (vAlign & Qt::AlignTop)
        return containerY + margins.top();
    if (vAlign & Qt::AlignBottom)
        return containerY + containerHeight - itemHeight - margins.bottom();
    return containerY + margins.top()
        + (containerHeight - margins.top() - margins.bottom() - itemHeight) / 2.0;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 216, as _ZNK16QQStyleKitLayout9containerEv
inline QQuickItem *QQStyleKitLayout::container() const
{
    return m_container;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 285, as _ZNK16QQStyleKitLayout7paddingEv
inline QMarginsF QQStyleKitLayout::padding() const
{
    return m_padding;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 290, as _ZNK16QQStyleKitLayout14contentMarginsEv
inline QMarginsF QQStyleKitLayout::contentMargins() const
{
    return m_contentMargins;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 305, as _ZNK16QQStyleKitLayout7spacingEv
inline qreal QQStyleKitLayout::spacing() const
{
    return m_spacing;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 320, as _ZNK16QQStyleKitLayout10isMirroredEv
inline bool QQStyleKitLayout::isMirrored() const
{
    return m_mirrored;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 335, as _ZNK16QQStyleKitLayout13implicitWidthEv
inline qreal QQStyleKitLayout::implicitWidth() const
{
    return m_implicitWidth;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 340, as _ZNK16QQStyleKitLayout14implicitHeightEv
inline qreal QQStyleKitLayout::implicitHeight() const
{
    return m_implicitHeight;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 365, as _ZNK16QQStyleKitLayout9isEnabledEv
inline bool QQStyleKitLayout::isEnabled() const
{
    return m_enabled;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQStyleKitLayout10metaObjectEv(
    const QQStyleKitLayout *self) {
  return self->metaObject();
}

//  void *QQStyleKitLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQStyleKitLayout11qt_metacastEPKc(
    QQStyleKitLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQStyleKitLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickItem *QQStyleKitLayout::container() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK16QQStyleKitLayout9containerEv(
    const QQStyleKitLayout *self) {
  return self->container();
}

//  QMarginsF QQStyleKitLayout::padding() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK16QQStyleKitLayout7paddingEv(
    const QQStyleKitLayout *self) {
  return new QMarginsF(self->padding());
}

//  QMarginsF QQStyleKitLayout::contentMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK16QQStyleKitLayout14contentMarginsEv(
    const QQStyleKitLayout *self) {
  return new QMarginsF(self->contentMargins());
}

//  qreal QQStyleKitLayout::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout7spacingEv(const QQStyleKitLayout *self) {
  return self->spacing();
}

//  bool QQStyleKitLayout::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitLayout10isMirroredEv(
    const QQStyleKitLayout *self) {
  return self->isMirrored();
}

//  qreal QQStyleKitLayout::implicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout13implicitWidthEv(
    const QQStyleKitLayout *self) {
  return self->implicitWidth();
}

//  qreal QQStyleKitLayout::implicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout14implicitHeightEv(
    const QQStyleKitLayout *self) {
  return self->implicitHeight();
}

//  bool QQStyleKitLayout::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitLayout9isEnabledEv(const QQStyleKitLayout *self) {
  return self->isEnabled();
}

//  void QQStyleKitLayout::containerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout16containerChangedEv(
    QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "containerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "containerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::layoutItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout18layoutItemsChangedEv(
    QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "layoutItemsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "layoutItemsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout13layoutChangedEv(QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "layoutChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "layoutChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout14paddingChangedEv(QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
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

//  void QQStyleKitLayout::contentMarginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout21contentMarginsChangedEv(
    QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "contentMarginsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "contentMarginsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout14spacingChangedEv(QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "spacingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "spacingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::mirroredChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout15mirroredChangedEv(QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "mirroredChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "mirroredChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout20implicitWidthChangedEv(
    QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "implicitWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "implicitWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout21implicitHeightChangedEv(
    QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "implicitHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "implicitHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout14enabledChangedEv(QQStyleKitLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayout::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQStyleKitLayout12updatePolishEv(QQStyleKitLayout *self) {
  self->updatePolish();
}

//  a QQmlListProperty<QQStyleKitLayoutItem> a ritual of QQStyleKitLayout
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQStyleKitLayout__QQmlListProperty_QQStyleKitLayoutItem(
    QQmlListProperty<QQStyleKitLayoutItem> *self) {
  delete self;
}
