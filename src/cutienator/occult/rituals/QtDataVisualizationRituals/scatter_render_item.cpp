//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/scatterrenderitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/scatterrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#include <QtDataVisualization/private/scatterrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 8, as _ZN18AbstractRenderItemC2Ev
inline AbstractRenderItem::AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/scatterrenderitem.cpp, line 21, as _ZN17ScatterRenderItemD1Ev
inline ScatterRenderItem::~ScatterRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 12, as _ZN18AbstractRenderItemC2ERKS_
inline AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem &other)
{
    m_translation = other.m_translation;
    m_rotation = other.m_rotation;
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 18, as _ZN18AbstractRenderItemD2Ev
inline AbstractRenderItem::~AbstractRenderItem()
{
}
//  -----------------------------------------------------------------------

//  ScatterRenderItem &ScatterRenderItem::operator=(const ScatterRenderItem
//      &a0)
extern "C" Q_DECL_EXPORT
ScatterRenderItem *ritual_ZN17ScatterRenderItemaSERKS_(
    ScatterRenderItem *self,
    const ScatterRenderItem *a0) {
  return &(self->operator=(*a0));
}

//  ScatterRenderItem::~ScatterRenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterRenderItemD1Ev(ScatterRenderItem *self) {
  delete self;
}

//  const QVector3D &ScatterRenderItem::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17ScatterRenderItem8positionEv(
    const ScatterRenderItem *self) {
  return new QVector3D(self->position());
}

//  void ScatterRenderItem::setPosition(const QVector3D &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterRenderItem11setPositionERK9QVector3D(
    ScatterRenderItem *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  bool ScatterRenderItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17ScatterRenderItem9isVisibleEv(
    const ScatterRenderItem *self) {
  return self->isVisible();
}

//  void ScatterRenderItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterRenderItem10setVisibleEb(
    ScatterRenderItem *self,
    bool visible) {
  self->setVisible(visible);
}
