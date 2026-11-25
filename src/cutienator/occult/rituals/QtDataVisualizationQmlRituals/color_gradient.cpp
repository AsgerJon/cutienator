//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  colorgradient_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class line
//  has no export macro. Written: its virtual functions, called
//  through the object: metaObject() and the destructor, virtual
//  through QObject.
//  Not written: the constructor and 'tr'; the signal 'updated';
//  'stops', which gives a 'QQmlListProperty', and 'doUpdate', which
//  are not virtual and which Qt's library offers not; and
//  'm_stops', a variable and a QList.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/colorgradient_p.h>

//  const QMetaObject *ColorGradient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13ColorGradient10metaObjectEv(
    const ColorGradient *self) {
  return self->metaObject();
}

//  ColorGradient::~ColorGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN13ColorGradientD1Ev(ColorGradient *self) {
  delete self;
}
