//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstractobjecthelper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstractobjecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 43, as _ZN20AbstractObjectHelper5uvBufEv
inline GLuint AbstractObjectHelper::uvBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_uvbuffer;
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

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 8, as _ZN20AbstractObjectHelperC1Ev
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

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 29, as _ZN20AbstractObjectHelper9vertexBufEv
inline GLuint AbstractObjectHelper::vertexBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_vertexbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 36, as _ZN20AbstractObjectHelper9normalBufEv
inline GLuint AbstractObjectHelper::normalBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_normalbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 50, as _ZN20AbstractObjectHelper10elementBufEv
inline GLuint AbstractObjectHelper::elementBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_elementbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 57, as _ZN20AbstractObjectHelper10indexCountEv
inline GLuint AbstractObjectHelper::indexCount()
{
    return m_indexCount;
}
//  -----------------------------------------------------------------------

//  A AbstractObjectHelper that Python can take functions over in. Every AbstractObjectHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef GLuint (*CuteAbstractObjectHelperCall0)(const void *, int *);
class CuteAbstractObjectHelper : public AbstractObjectHelper {
public:
  using AbstractObjectHelper::AbstractObjectHelper;
  CuteAbstractObjectHelper(const AbstractObjectHelper & other) : AbstractObjectHelper(other) {}
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
      CuteAbstractObjectHelperCall0 call = reinterpret_cast<CuteAbstractObjectHelperCall0>(taken[0]);
      GLuint given = call(this, &handled);
      if (handled) return given;
    }
    return AbstractObjectHelper::uvBuf();
  }
};

//  AbstractObjectHelper::AbstractObjectHelper()
extern "C" Q_DECL_EXPORT
AbstractObjectHelper *ritual_ZN20AbstractObjectHelperC1Ev() {
  return new CuteAbstractObjectHelper();
}

//  AbstractObjectHelper::~AbstractObjectHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AbstractObjectHelperD1Ev(AbstractObjectHelper *self) {
  delete self;
}

//  GLuint AbstractObjectHelper::vertexBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20AbstractObjectHelper9vertexBufEv(
    AbstractObjectHelper *self) {
  return self->vertexBuf();
}

//  GLuint AbstractObjectHelper::normalBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20AbstractObjectHelper9normalBufEv(
    AbstractObjectHelper *self) {
  return self->normalBuf();
}

//  GLuint AbstractObjectHelper::uvBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20AbstractObjectHelper5uvBufEv(AbstractObjectHelper *self) {
  return self->uvBuf();
}

//  GLuint AbstractObjectHelper::elementBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20AbstractObjectHelper10elementBufEv(
    AbstractObjectHelper *self) {
  return self->elementBuf();
}

//  GLuint AbstractObjectHelper::indexCount()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN20AbstractObjectHelper10indexCountEv(
    AbstractObjectHelper *self) {
  return self->indexCount();
}

//  a Python function taken by a CuteAbstractObjectHelper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractObjectHelper(
    AbstractObjectHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractObjectHelper *>(self)->take(key, call);
}

//  GLuint AbstractObjectHelper::uvBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_own_ZN20AbstractObjectHelper5uvBufEv(
    AbstractObjectHelper *self) {
  return self->AbstractObjectHelper::uvBuf();
}
