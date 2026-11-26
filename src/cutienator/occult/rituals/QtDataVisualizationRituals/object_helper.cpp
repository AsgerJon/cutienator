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
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/meshloader_p.h>
#include <QtDataVisualization/private/vertexindexer_p.h>
#include <QtDataVisualization/private/objecthelper_p.h>
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 16, as local:objecthelper.cpp:ObjectHelperRef
struct ObjectHelperRef {
    int refCount;
    ObjectHelper *obj;
};

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 24, as _ZN12ObjectHelperD2Ev
inline ObjectHelper::~ObjectHelper()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 43, as _ZN20AbstractObjectHelper5uvBufEv
inline GLuint AbstractObjectHelper::uvBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_uvbuffer;
}

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

//  A ObjectHelper that Python can take functions over in. Every ObjectHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef GLuint (*CuteObjectHelperCall0)(const void *, int *);
class CuteObjectHelper : public ObjectHelper {
public:
  using ObjectHelper::ObjectHelper;
  CuteObjectHelper(const ObjectHelper & other) : ObjectHelper(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20AbstractObjectHelper5uvBufEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  GLuint AbstractObjectHelper::uvBuf()
  GLuint uvBuf() override {
    if (taken[0]) {
      int handled = 0;
      CuteObjectHelperCall0 call = reinterpret_cast<CuteObjectHelperCall0>(taken[0]);
      GLuint given = call(this, &handled);
      if (handled) return given;
    }
    return AbstractObjectHelper::uvBuf();
  }
};

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

//  const QList<GLuint> &ObjectHelper::indices() const
extern "C" Q_DECL_EXPORT
const QList<GLuint> *ritual_ZNK12ObjectHelper7indicesEv(
    const ObjectHelper *self) {
  return &(self->indices());
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

//  a Python function taken by a CuteObjectHelper, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ObjectHelper(
    ObjectHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteObjectHelper *>(self)->take(key, call);
}
