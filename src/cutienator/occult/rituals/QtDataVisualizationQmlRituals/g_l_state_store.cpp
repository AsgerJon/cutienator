//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  glstatestore_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject() and the destructor, virtual
//  through QObject.
//  Not written: the constructor and 'tr'; 'storeGLState',
//  'restoreGLState' and 'initGLDefaultState', which are not
//  virtual and which Qt's library offers not; and the variables
//  holding the state of OpenGL, which are no functions.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/glstatestore_p.h>

//  const QMetaObject *GLStateStore::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12GLStateStore10metaObjectEv(
    const GLStateStore *self) {
  return self->metaObject();
}

//  GLStateStore::~GLStateStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN12GLStateStoreD1Ev(GLStateStore *self) {
  delete self;
}
