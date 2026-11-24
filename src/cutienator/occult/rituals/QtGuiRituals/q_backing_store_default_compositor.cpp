//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbackingstoredefaultcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbackingstoredefaultcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qbackingstoredefaultcompositor_p.h>
#include <QtGui/qtransform.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformgraphicsbuffer.h>
#include <QtCore/qfile.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 16, as _ZN30QBackingStoreDefaultCompositorD1Ev
inline QBackingStoreDefaultCompositor::~QBackingStoreDefaultCompositor()
{
    reset();
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 21, as _ZN30QBackingStoreDefaultCompositor5resetEv
inline void QBackingStoreDefaultCompositor::reset()
{
    m_rhi = nullptr;
    m_psNoBlend.reset();
    m_psBlend.reset();
    m_psPremulBlend.reset();
    m_samplerNearest.reset();
    m_samplerLinear.reset();
    m_vbuf.reset();
    m_texture.reset();
    m_widgetQuadData.reset();
    for (PerQuadData &d : m_textureQuadData)
        d.reset();
}
//  -----------------------------------------------------------------------

//  QBackingStoreDefaultCompositor::~QBackingStoreDefaultCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBackingStoreDefaultCompositorD1Ev(
    QBackingStoreDefaultCompositor *self) {
  delete self;
}

//  void QBackingStoreDefaultCompositor::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBackingStoreDefaultCompositor5resetEv(
    QBackingStoreDefaultCompositor *self) {
  self->reset();
}
