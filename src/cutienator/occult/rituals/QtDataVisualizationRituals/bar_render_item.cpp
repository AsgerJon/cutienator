//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#include <QtDataVisualization/private/barrenderitem_p.h>
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

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 23, as _ZN13BarRenderItemD1Ev
inline BarRenderItem::~BarRenderItem()
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

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 8, as _ZN13BarRenderItemC1Ev
inline BarRenderItem::BarRenderItem()
    : AbstractRenderItem(),
      m_value(0),
      m_height(0.0f)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 15, as _ZN13BarRenderItemC1ERKS_
inline BarRenderItem::BarRenderItem(const BarRenderItem &other)
    : AbstractRenderItem(other)
{
    m_value = other.m_value;
    m_position = other.m_position;
    m_height = other.m_height;
}
//  -----------------------------------------------------------------------

//  BarRenderItem::BarRenderItem()
extern "C" Q_DECL_EXPORT
BarRenderItem *ritual_ZN13BarRenderItemC1Ev() {
  return new BarRenderItem();
}

//  BarRenderItem::BarRenderItem(const BarRenderItem &other)
extern "C" Q_DECL_EXPORT
BarRenderItem *ritual_ZN13BarRenderItemC1ERKS_(const BarRenderItem *other) {
  return new BarRenderItem(*other);
}

//  BarRenderItem &BarRenderItem::operator=(const BarRenderItem &a0)
extern "C" Q_DECL_EXPORT
BarRenderItem *ritual_ZN13BarRenderItemaSERKS_(
    BarRenderItem *self,
    const BarRenderItem *a0) {
  return &(self->operator=(*a0));
}

//  BarRenderItem::~BarRenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarRenderItemD1Ev(BarRenderItem *self) {
  delete self;
}

//  void BarRenderItem::setPosition(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarRenderItem11setPositionERK6QPoint(
    BarRenderItem *self,
    const QPoint *pos) {
  self->setPosition(*pos);
}

//  const QPoint &BarRenderItem::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK13BarRenderItem8positionEv(const BarRenderItem *self) {
  return new QPoint(self->position());
}

//  void BarRenderItem::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarRenderItem8setValueEf(BarRenderItem *self, float value) {
  self->setValue(value);
}

//  float BarRenderItem::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13BarRenderItem5valueEv(const BarRenderItem *self) {
  return self->value();
}

//  void BarRenderItem::setHeight(GLfloat height)
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarRenderItem9setHeightEf(
    BarRenderItem *self,
    GLfloat height) {
  self->setHeight(height);
}

//  GLfloat BarRenderItem::height() const
extern "C" Q_DECL_EXPORT
GLfloat ritual_ZNK13BarRenderItem6heightEv(const BarRenderItem *self) {
  return self->height();
}
