//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  colorgradient_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject() and the implicit destructor,
//  virtual through QObject.
//  Not written: the constructor and 'tr'; the signals; and
//  'position', 'setPosition', 'color' and 'setColor', which are
//  not virtual and which Qt's library offers not.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/colorgradient_p.h>

//  const QMetaObject *ColorGradientStop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17ColorGradientStop10metaObjectEv(
    const ColorGradientStop *self) {
  return self->metaObject();
}

//  ColorGradientStop::~ColorGradientStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ColorGradientStopD1Ev(ColorGradientStop *self) {
  delete self;
}
