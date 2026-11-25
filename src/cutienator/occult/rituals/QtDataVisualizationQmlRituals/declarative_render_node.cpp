//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  declarativerendernode_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject(), the destructor and
//  'preprocess', which overrides that of QSGNode; and its inline
//  function 'size'.
//  Not written: the constructor and 'tr'; and the slot
//  'handleControllerDestroyed' and the other functions that are
//  neither virtual nor inline, which Qt's library offers not.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/declarativerendernode_p.h>
#include <QtCore/qsize.h>

//  const QMetaObject *DeclarativeRenderNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21DeclarativeRenderNode10metaObjectEv(
    const DeclarativeRenderNode *self) {
  return self->metaObject();
}

//  DeclarativeRenderNode::~DeclarativeRenderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeRenderNodeD1Ev(DeclarativeRenderNode *self) {
  delete self;
}

//  QSize DeclarativeRenderNode::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21DeclarativeRenderNode4sizeEv(
    const DeclarativeRenderNode *self) {
  return new QSize(self->size());
}

//  void DeclarativeRenderNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeRenderNode10preprocessEv(
    DeclarativeRenderNode *self) {
  self->preprocess();
}
