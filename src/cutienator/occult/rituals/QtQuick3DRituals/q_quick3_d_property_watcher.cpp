//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dshaderutils_p.h"
#include <QtCore/qfile.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include "qquick3dviewport_p.h"
#include "qquick3dcustommaterial_p.h"
#include "qquick3deffect_p.h"
#include "qquick3dtextureproviderextension.h"
#include <ssg/qssgrenderextensions.h>
#include <ssg/qquick3dextensionhelpers.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderimage_p.h>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dshaderutils.cpp, line 2000, as _ZN23QQuick3DPropertyWatcher22onValuePropertyChangedEv
inline void QQuick3DPropertyWatcher::onValuePropertyChanged()
{
    m_tracker->m_dirtyProperties.push_back(m_property.propertyIndex());
    m_tracker->markTrackedPropertyDirty(m_property, QQuick3DPropertyChangedTracker::DirtyPropertyHint::Value);
}

//  from ../qtquick3d/src/quick3d/qquick3dshaderutils.cpp, line 2006, as _ZN23QQuick3DPropertyWatcher24onPointerPropertyChangedEv
inline void QQuick3DPropertyWatcher::onPointerPropertyChanged()
{
    m_tracker->m_dirtyProperties.push_back(m_property.propertyIndex());
    m_tracker->markTrackedPropertyDirty(m_property, QQuick3DPropertyChangedTracker::DirtyPropertyHint::Reference);;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DPropertyWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DPropertyWatcher10metaObjectEv(
    const QQuick3DPropertyWatcher *self) {
  return self->metaObject();
}

//  void QQuick3DPropertyWatcher::onValuePropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher22onValuePropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  self->onValuePropertyChanged();
}

//  void QQuick3DPropertyWatcher::onPointerPropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher24onPointerPropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  self->onPointerPropertyChanged();
}
