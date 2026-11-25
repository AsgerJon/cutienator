//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  declarativetheme_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject(), the destructor, and
//  'classBegin' and 'componentComplete', which override those of
//  QQmlParserStatus.
//  Not written: the constructor and 'tr'; the signals; and the
//  functions that are not virtual, which Qt's library offers not,
//  'themeChildren', 'baseColors', 'baseGradients' and the static
//  '...Func' among them.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/declarativetheme_p.h>

//  const QMetaObject *DeclarativeTheme3D::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18DeclarativeTheme3D10metaObjectEv(
    const DeclarativeTheme3D *self) {
  return self->metaObject();
}

//  DeclarativeTheme3D::~DeclarativeTheme3D()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeTheme3DD1Ev(DeclarativeTheme3D *self) {
  delete self;
}

//  void DeclarativeTheme3D::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeTheme3D10classBeginEv(DeclarativeTheme3D *self) {
  self->classBegin();
}

//  void DeclarativeTheme3D::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeTheme3D17componentCompleteEv(
    DeclarativeTheme3D *self) {
  self->componentComplete();
}
