//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  declarativescene_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject() and the destructor; and the
//  marker QML_UNCREATABLE gives it, inline.
//  Not written: the constructor and 'tr'; the signal; and
//  'setSelectionQueryPosition', 'selectionQueryPosition' and
//  'invalidSelectionPoint', which are not virtual and which Qt's
//  library offers not.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/declarativescene_p.h>

//  const QMetaObject *Declarative3DScene::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18Declarative3DScene10metaObjectEv(
    const Declarative3DScene *self) {
  return self->metaObject();
}

//  Declarative3DScene::~Declarative3DScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN18Declarative3DSceneD1Ev(Declarative3DScene *self) {
  delete self;
}
