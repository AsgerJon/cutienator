//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  foreigntypes_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  An empty struct the header's macro DEFINE_FOREIGN_UNCREATABLE_TYPE makes,
//  whose class line has no export macro. It only tells QML, by QML_FOREIGN,
//  the name Object3D of Q3DObject, and by QML_UNCREATABLE that QML makes
//  none.
//  Q_GADGET gives it staticMetaObject, a variable, and no function to
//  call. Written: the implicit destructor and what the QML macros
//  give it, all inline.
//  Not written: its implicit constructors, which a class Qt does not
//  export does not get, and 'operator='; qt_check_for_QGADGET_macro,
//  which Q_GADGET declares and nothing defines; qt_static_metacall,
//  moc's.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/foreigntypes_p.h>

//  Q3DObjectDataVisForeign::~Q3DObjectDataVisForeign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23Q3DObjectDataVisForeignD1Ev(Q3DObjectDataVisForeign *self) {
  delete self;
}
