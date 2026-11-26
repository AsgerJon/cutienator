//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/barrenderitem_p.h>
#include <QtDataVisualization/private/labelitem_p.h>
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 8, as _ZN13BarRenderItemC2Ev
inline BarRenderItem::BarRenderItem()
    : AbstractRenderItem(),
      m_value(0),
      m_height(0.0f)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 40, as _ZN18BarRenderSliceItemD1Ev
inline BarRenderSliceItem::~BarRenderSliceItem()
{
    delete m_sliceLabelItem;
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 15, as _ZN13BarRenderItemC2ERKS_
inline BarRenderItem::BarRenderItem(const BarRenderItem &other)
    : AbstractRenderItem(other)
{
    m_value = other.m_value;
    m_position = other.m_position;
    m_height = other.m_height;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 14, as _ZN9LabelItemD1Ev
inline LabelItem::~LabelItem()
{
    clear();
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 8, as _ZN9LabelItemC1Ev
inline LabelItem::LabelItem()
    : m_size(QSize(0, 0)),
      m_textureId(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 40, as _ZN9LabelItem5clearEv
inline void LabelItem::clear()
{
    if (m_textureId && QOpenGLContext::currentContext())
        QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = 0;
    m_size = QSize(0, 0);
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 23, as _ZN13BarRenderItemD2Ev
inline BarRenderItem::~BarRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 8, as _ZN18AbstractRenderItemC2Ev
inline AbstractRenderItem::AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 45, as _ZN18BarRenderSliceItem7setItemERK13BarRenderItem
inline void BarRenderSliceItem::setItem(const BarRenderItem &renderItem)
{
    m_translation = renderItem.translation();
    m_rotation = renderItem.rotation();
    m_value = renderItem.value();
    m_position = renderItem.position();
    m_height = renderItem.height();
    m_sliceLabel = QString();
    delete m_sliceLabelItem;
    m_sliceLabelItem = 0;
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 57, as _ZN18BarRenderSliceItem14sliceLabelItemEv
inline LabelItem &BarRenderSliceItem::sliceLabelItem()
{
    if (!m_sliceLabelItem)
        m_sliceLabelItem = new LabelItem;
    return *m_sliceLabelItem;
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 64, as _ZN18BarRenderSliceItem13setSliceLabelERK7QString
inline void BarRenderSliceItem::setSliceLabel(const QString &label)
{
    if (m_sliceLabelItem)
        m_sliceLabelItem->clear();
    m_sliceLabel = label;
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 71, as _ZNK18BarRenderSliceItem10sliceLabelEv
inline const QString &BarRenderSliceItem::sliceLabel() const
{
    return m_sliceLabel;
}
//  -----------------------------------------------------------------------

//  BarRenderSliceItem &BarRenderSliceItem::operator=(const
//      BarRenderSliceItem &other)
extern "C" Q_DECL_EXPORT
BarRenderSliceItem *ritual_ZN18BarRenderSliceItemaSERKS_(
    BarRenderSliceItem *self,
    const BarRenderSliceItem *other) {
  return &(self->operator=(*other));
}

//  BarRenderSliceItem::~BarRenderSliceItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18BarRenderSliceItemD1Ev(BarRenderSliceItem *self) {
  delete self;
}

//  void BarRenderSliceItem::setItem(const BarRenderItem &renderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN18BarRenderSliceItem7setItemERK13BarRenderItem(
    BarRenderSliceItem *self,
    const BarRenderItem *renderItem) {
  self->setItem(*renderItem);
}

//  LabelItem &BarRenderSliceItem::sliceLabelItem()
extern "C" Q_DECL_EXPORT
LabelItem *ritual_ZN18BarRenderSliceItem14sliceLabelItemEv(
    BarRenderSliceItem *self) {
  return &(self->sliceLabelItem());
}

//  void BarRenderSliceItem::setSliceLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN18BarRenderSliceItem13setSliceLabelERK7QString(
    BarRenderSliceItem *self,
    const QString *label) {
  self->setSliceLabel(*label);
}

//  const QString &BarRenderSliceItem::sliceLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18BarRenderSliceItem10sliceLabelEv(
    const BarRenderSliceItem *self) {
  return new QString(self->sliceLabel());
}
