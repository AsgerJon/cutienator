//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/labelitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/labelitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/labelitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 8, as _ZN9LabelItemC1Ev
inline LabelItem::LabelItem()
    : m_size(QSize(0, 0)),
      m_textureId(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 14, as _ZN9LabelItemD1Ev
inline LabelItem::~LabelItem()
{
    clear();
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 19, as _ZN9LabelItem7setSizeERK5QSize
inline void LabelItem::setSize(const QSize &size)
{
    m_size = size;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 24, as _ZNK9LabelItem4sizeEv
inline QSize LabelItem::size() const
{
    return m_size;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 29, as _ZN9LabelItem12setTextureIdEj
inline void LabelItem::setTextureId(GLuint textureId)
{
    QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = textureId;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 35, as _ZNK9LabelItem9textureIdEv
inline GLuint LabelItem::textureId() const
{
    return m_textureId;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 40, as _ZN9LabelItem5clearEv
inline void LabelItem::clear()
{
    if (m_textureId && QOpenGLContext::currentContext())
        QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = 0;
    m_size = QSize(0, 0);
}
//  -----------------------------------------------------------------------

//  LabelItem::LabelItem()
extern "C" Q_DECL_EXPORT
LabelItem *ritual_ZN9LabelItemC1Ev() {
  return new LabelItem();
}

//  LabelItem::~LabelItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN9LabelItemD1Ev(LabelItem *self) {
  delete self;
}

//  void LabelItem::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9LabelItem7setSizeERK5QSize(
    LabelItem *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QSize LabelItem::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9LabelItem4sizeEv(const LabelItem *self) {
  return new QSize(self->size());
}

//  void LabelItem::setTextureId(GLuint textureId)
extern "C" Q_DECL_EXPORT
void ritual_ZN9LabelItem12setTextureIdEj(LabelItem *self, GLuint textureId) {
  self->setTextureId(textureId);
}

//  GLuint LabelItem::textureId() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK9LabelItem9textureIdEv(const LabelItem *self) {
  return self->textureId();
}

//  void LabelItem::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9LabelItem5clearEv(LabelItem *self) {
  self->clear();
}
