//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstractrenderitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstractrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 18, as _ZN18AbstractRenderItemD1Ev
inline AbstractRenderItem::~AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 8, as _ZN18AbstractRenderItemC1Ev
inline AbstractRenderItem::AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 12, as _ZN18AbstractRenderItemC1ERKS_
inline AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem &other)
{
    m_translation = other.m_translation;
    m_rotation = other.m_rotation;
}
//  -----------------------------------------------------------------------

//  AbstractRenderItem::AbstractRenderItem()
extern "C" Q_DECL_EXPORT
AbstractRenderItem *ritual_ZN18AbstractRenderItemC1Ev() {
  return new AbstractRenderItem();
}

//  AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem &other)
extern "C" Q_DECL_EXPORT
AbstractRenderItem *ritual_ZN18AbstractRenderItemC1ERKS_(
    const AbstractRenderItem *other) {
  return new AbstractRenderItem(*other);
}

//  AbstractRenderItem &AbstractRenderItem::operator=(const
//      AbstractRenderItem &other)
extern "C" Q_DECL_EXPORT
AbstractRenderItem *ritual_ZN18AbstractRenderItemaSERKS_(
    AbstractRenderItem *self,
    const AbstractRenderItem *other) {
  return &(self->operator=(*other));
}

//  AbstractRenderItem::~AbstractRenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItemD1Ev(AbstractRenderItem *self) {
  delete self;
}

//  void AbstractRenderItem::setTranslation(const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItem14setTranslationERK9QVector3D(
    AbstractRenderItem *self,
    const QVector3D *translation) {
  self->setTranslation(*translation);
}

//  const QVector3D &AbstractRenderItem::translation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18AbstractRenderItem11translationEv(
    const AbstractRenderItem *self) {
  return new QVector3D(self->translation());
}

//  const QQuaternion &AbstractRenderItem::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK18AbstractRenderItem8rotationEv(
    const AbstractRenderItem *self) {
  return new QQuaternion(self->rotation());
}

//  void AbstractRenderItem::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18AbstractRenderItem11setRotationERK11QQuaternion(
    AbstractRenderItem *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}
