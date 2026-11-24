//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/objecthelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/objecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 8, as _ZN20AbstractObjectHelperC2Ev
inline AbstractObjectHelper::AbstractObjectHelper()
    : m_vertexbuffer(0),
      m_normalbuffer(0),
      m_uvbuffer(0),
      m_elementbuffer(0),
      m_indexCount(0),
      m_meshDataLoaded(false)
{
    initializeOpenGLFunctions();
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 19, as _ZN20AbstractObjectHelperD2Ev
inline AbstractObjectHelper::~AbstractObjectHelper()
{
    if (QOpenGLContext::currentContext()) {
        glDeleteBuffers(1, &m_vertexbuffer);
        glDeleteBuffers(1, &m_uvbuffer);
        glDeleteBuffers(1, &m_normalbuffer);
        glDeleteBuffers(1, &m_elementbuffer);
    }
}
//  -----------------------------------------------------------------------

//  ObjectHelper::~ObjectHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ObjectHelperD1Ev(ObjectHelper *self) {
  delete self;
}

//  const QString &ObjectHelper::objectFile()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12ObjectHelper10objectFileEv(ObjectHelper *self) {
  return new QString(self->objectFile());
}

//  const QList<QVector3D> &ObjectHelper::indexedvertices() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK12ObjectHelper15indexedverticesEv(
    const ObjectHelper *self) {
  return new QList<QVector3D>(self->indexedvertices());
}

//  const QList<QVector2D> &ObjectHelper::indexedUVs() const
extern "C" Q_DECL_EXPORT
QList<QVector2D> *ritual_ZNK12ObjectHelper10indexedUVsEv(
    const ObjectHelper *self) {
  return new QList<QVector2D>(self->indexedUVs());
}

//  const QList<QVector3D> &ObjectHelper::indexedNormals() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK12ObjectHelper14indexedNormalsEv(
    const ObjectHelper *self) {
  return new QList<QVector3D>(self->indexedNormals());
}
